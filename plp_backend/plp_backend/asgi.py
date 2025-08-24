import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import learning.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plp_backend.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            learning.routing.websocket_urlpatterns
        )
    ),
})
