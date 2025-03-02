from django.urls import path

from .views import *

urlpatterns = [
    path('events/', CreateEvent.as_view(), name='events'),
    path('events/<int:event_id>/attend/', AttendEvent.as_view(), name='event-detail'),
    path('events/<int:event_id>/', DeleteEvent.as_view(), name='event-detail'),
    path('posts/', CreateListPost.as_view(), name='post-detail'),

]
