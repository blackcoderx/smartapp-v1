from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class CreateEvent(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


# join an event
class AttendEvent(APIView):
    def post(self, request, event_id):
        event = Event.objects.get(id=event_id)
        event.attendees += 1
        return Response("User has joined the event", status=status.HTTP_200_OK)


class DeleteEvent(generics.RetrieveDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'

    def delete(self, request, *args, **kwargs):
        event = self.get_object()
        if event.host == request.user:
            return self.destroy(request, *args, **kwargs)
        else:
            return Response("Only the host of the event can delete it.", status=status.HTTP_403_FORBIDDEN)


# posts
class CreateListPost(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
