from django.shortcuts import render
from .serializers import CandidateSerializer
from .models import Candidate
from rest_framework.generics import ListCreateAPIView

class CandidateAPIView(ListCreateAPIView):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()