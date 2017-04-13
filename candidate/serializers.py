__author__ = 'paulo'
from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate