import datetime
from django.utils import timezone
from rest_framework import serializers
from oneAssure.models.user_model import User
from ..models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value
    
    def validate_meeting_type(self, value):
        if value not in ['online', 'offline']:
            raise serializers.ValidationError("Meeting type must be either 'online' or 'offline'.")
        return value
    
    def validate_start_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Start time must be in the future.")
        return value
    
    def validate(self, data):
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        
        if start_time and end_time and start_time >= end_time:
            raise serializers.ValidationError("Start time must be before end time.")

        if start_time and end_time:
            # Check for overlapping meetings
            overlapping_meetings = Meeting.objects.filter(
                start_time__lte=end_time,
                end_time__gte=start_time
            )
            if overlapping_meetings.exists():
                raise serializers.ValidationError("Meeting overlaps with existing meetings.")
        
        return data
