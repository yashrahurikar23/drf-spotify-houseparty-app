from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Room
    fields = ['id','code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at']

class CreateRoomSerializer(serializers.ModelSerializer):
  # Understand this what is this Meta class syntax what does it do
  class Meta:
      model = Room
      fields = ['guest_can_pause', 'votes_to_skip']
