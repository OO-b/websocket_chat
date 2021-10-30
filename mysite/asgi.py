"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack #추가
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing # chat import

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http" : get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # 추가
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})