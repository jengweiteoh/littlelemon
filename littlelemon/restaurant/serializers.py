from rest_framework.serializers import ModelSerializer
from .models import MenuItem
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'inventory']

        