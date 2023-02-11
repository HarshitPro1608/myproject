from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Client, Artist, Work
from .filters import WorkFilter
from .serializers import ClientSerializer, ArtistSerializer, WorkSerializer,UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    search_fields=['name']

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class WorkList(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_class =WorkFilter

class WorkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def work(request):
  return HttpResponse('<h1>works</h1>')


