from django.shortcuts import render
from rest_framework import generics
from .models import Passwords, User
from .serializers import PasswordSerializer
from Manager.serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class Create(generics.CreateAPIView):
    queryset = Passwords.objects.all()
    serializer_class = PasswordSerializer
    

class Read(generics.ListAPIView):
    
    serializer_class = PasswordSerializer

    def get_queryset(self):
        queryset = Passwords.objects.all()
        
        id = self.kwargs.get('user')
        
        if id is not None:
            queryset = queryset.filter(user = id)
        return queryset 
    
    

class ReadOne(generics.RetrieveAPIView):
    queryset = Passwords.objects.all()
    serializer_class = PasswordSerializer

class Update(generics.UpdateAPIView):
    queryset = Passwords.objects.all()
    serializer_class = PasswordSerializer

class Delete(generics.DestroyAPIView):
    queryset = Passwords.objects.all()
    serializer_class = PasswordSerializer
    
    
class MyTokenObtain(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer 
    
