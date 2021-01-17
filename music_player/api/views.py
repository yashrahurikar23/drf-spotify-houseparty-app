from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, CreateRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Room

# Create your views here.
class RoomView(generics.ListAPIView):
  queryset = Room.objects.all()
  serializer_class = RoomSerializer

class CreateRoomView(APIView):
  serializer_class = CreateRoomSerializer
  
  def post(self, request, format=None):
    # Check if the users session already exists if not then create a new session for the user 
    if not self.request.session.exists(self.request.session.session_key):
       self.request.session.create()

    serializer = self.serializer_class(data=request.data)
    # Deserializing the data which we receive from the POST request and check if the data is in desired format
    if serializer.is_valid():
      guest_can_pause = serializer.data.get('guest_can_pause')
      votes_to_skip = serializer.data.get('votes_to_skip')
      host = self.request.session.session_key
      # Checking if the host session already exists just update the room details else create a new room 
      queryset = Room.objects.filter(host=host)
      if queryset.exists():
        room = queryset[0]
        room.guest_can_pause = guest_can_pause
        room.votes_to_skip = votes_to_skip
        room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
      else:
        room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
        room.save()

      return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)  
         