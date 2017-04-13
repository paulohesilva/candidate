from ct_auth.models import User
from django.db import models


# Create your models here.
class Candidate(User):
    name = models.CharField(max_length=15, unique=True, null=True)
    cpf = models.CharField(max_length=15, unique=True, null=True)
    rg = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    lattes = models.URLField(null=True, blank=True)
    about = models.TextField(max_length=10000, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.is_active = True
        self.set_password(self.password)
        super(Candidate, self).save(*args, **kwargs)
    
