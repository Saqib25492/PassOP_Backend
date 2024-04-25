from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import Passwords, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passwords
        fields = [
            'id',
            'user',
            'site',
            'username',
            'password',
        ]
        
class CreateUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]
        
    def validate_email(self, value):
        if User.objects.filter(email = value).exist():
            raise serializers.ValidationError("Email Already Exists")
        return value
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['is_active'] = user.is_active
        
        return token