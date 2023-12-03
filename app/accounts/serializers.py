from rest_framework import serializers

from .models import User, Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CompleteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'telephone', 'gender']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_id', 'name', 'description', 'quantity', 'closet_number']


class ExcelFileSerializer(serializers.Serializer):
    file = serializers.FileField()
