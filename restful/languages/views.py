from django.shortcuts import render
from .models import Language, Paradigm, Programmer
from rest_framework import viewsets
from .serializers import LanguageSerializers, ParadigmSerializers, ProgrammerSerializers

class Languageview(viewsets.ModelViewSet):
    queryset= Language.objects.all()
    serializer_class= LanguageSerializers

class ProgrammerView(viewsets.ModelViewSet):
    queryset=Programmer.objects.all()
    serializer_class = ProgrammerSerializers