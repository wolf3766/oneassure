import datetime
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models.meeting_model import Meeting
from .models.user_model import User
from .serializers.user_serializers import UserSerializer, UserUpdateSerializer
from .serializers.meeting_serializers import MeetingSerializer
from django.utils import timezone
now_aware = timezone.now()

# Create your views here.

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeetingView(APIView):
    def get(self, request, user_id):
        meetings = Meeting.objects.filter(user_id=user_id).order_by('-start_time')
        serializer = MeetingSerializer(meetings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        meeting = Meeting.objects.get(pk=pk)
        serializer = MeetingSerializer(meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        meeting = Meeting.objects.get(pk=pk)
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MeetingDetailView(APIView):
    def get(self, request):
        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')
        user_id = request.query_params.get('user_id')
        format = '%Y-%m-%dT%H:%M:%S'
        start_time = datetime.datetime.strptime(start_time, format)
        end_time = datetime.datetime.strptime(end_time, format)

        user_meetings = Meeting.objects.filter(
            start_time__gte=start_time,
            end_time__lte=end_time,
            user_id=user_id 
        ).order_by('start_time')

        free_slots = []
        if user_meetings:
            free_slots.append({
                'start_time': start_time,
                'end_time': user_meetings[0].start_time,
                'duration': user_meetings[0].start_time.replace(tzinfo=None) - start_time
            })

            for i in range(len(user_meetings) - 1):
                free_slots.append({
                    'start_time': user_meetings[i].end_time,
                    'end_time': user_meetings[i+1].start_time,
                    'duration': user_meetings[i+1].start_time - user_meetings[i].end_time
                })

            free_slots.append({
                'start_time': user_meetings[len(free_slots)-1].end_time,
                'end_time': end_time,
                'duration': end_time - user_meetings[len(free_slots)-1].end_time.replace(tzinfo=None)
            })
        else:
            free_slots.append({
                'start_time': start_time,
                'end_time': end_time,
                'duration': end_time - start_time
            })

        for i in range(len(free_slots)):
            free_slots[i]['duration'] = free_slots[i]['duration'].seconds/60

        serializer = MeetingSerializer(user_meetings, many=True)
        
        return Response({
            'meetings': serializer.data,
            'free_time_slots': free_slots
        })
    