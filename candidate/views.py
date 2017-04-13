from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework.permissions import IsAuthenticated


class CandidateAPIView(ListCreateAPIView):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()

class Candidate_details(RetrieveUpdateAPIView):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()

class Candidate_delete(DestroyAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
        