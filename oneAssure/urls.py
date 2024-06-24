from django.urls import path
from .views import MeetingDetailView, UserView
from .views import MeetingView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', UserView.as_view()),
    path('meetings/', MeetingView.as_view()),
    path('meetings/detail/', MeetingDetailView.as_view()),
]
