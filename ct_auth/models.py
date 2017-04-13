# DJANGO #
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
import os
import uuid

import hashlib
import random

class CustomUserManager(UserManager):
    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        # username = email
        now = timezone.now()
        if not email:
            if username:
                key = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
                email = username.lower()+key+'@surf2dayapp.com'
            else:
                raise ValueError('The given email must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)
        
  
class AbstractUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(_('full name'), max_length=50, blank=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        abstract = True

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
    
    def get_short_name(self):
        return self.full_name

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

class User(AbstractUser):

    def upload_image_profile(self, filename):
        m = hashlib.md5()
        m.update(self.email.encode('utf-8'))
        extension = os.path.splitext(filename)[1]
        return 'profile/' + '/'.join([m.hexdigest(), uuid.uuid1().__str__()+extension])

    is_superuser = False
    # image_field = models.ImageField(upload_to=upload_image_profile,  blank=True, null=True, )
    username = models.CharField(unique=True,null=True, blank=True, max_length=255)
    confirm_username = models.BooleanField(default=False)
    is_social = models.BooleanField(default=False)
    phone = models.CharField(null=True, blank=True, max_length=50)
    publisher = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('full_name',)

    def __unicode__(self):
        return self.full_name
    
    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = User.objects.get(id=self.id)

            if this.image_field != self.path_picture:
                this.image_field.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(User, self).save(*args, **kwargs)

class RecoveryKey(models.Model):
    key = models.TextField(max_length=40)
    user = models.OneToOneField(User)

    class Meta:
        db_table = 'sos_recovery_key'
        
    def __unicode__(self):
        return self.key