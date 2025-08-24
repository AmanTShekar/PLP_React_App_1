from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/recommendations/<int:student_id>/", consumers.RecommendationConsumer.as_asgi()),
]
