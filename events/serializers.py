from rest_framework import serializers
from .models import Event, Category, Ticket

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)  

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])  
        event = Event.objects.create(**validated_data)  

        for category_data in categories_data:
            category, _ = Category.objects.get_or_create(**category_data)
            event.categories.add(category)  

        return event


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
