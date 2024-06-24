from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
    def validate_email(self, value):
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError("Email must be from the domain '@gmail.com'.")
        return value

    def validate(self, data):
        if data['dnd_start_time'] >= data['dnd_end_time']:
            raise serializers.ValidationError("Do Not Disturb start time must be before end time.")
        return data
    
    def validate(self, data):
        if 'dnd_start_time' not in data or 'dnd_end_time' not in data:
            raise serializers.ValidationError("Both Do Not Disturb times must be provided.")
        return data

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['dnd_start_time', 'dnd_end_time', 'preferred_time_zone']

    
    def validate(self, data):
        if data['dnd_start_time'] >= data['dnd_end_time']:
            raise serializers.ValidationError("Do Not Disturb start time must be before end time.")
        return data
    
    def validate(self, data):
        if 'dnd_start_time' not in data or 'dnd_end_time' not in data:
            raise serializers.ValidationError("Both Do Not Disturb times must be provided.")
        return data
    
    