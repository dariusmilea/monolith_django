import os
from django.conf import settings
import uvicorn

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

uvicorn.run(
    "app.asgi:application",
    host=settings.API_HOST,
    port=settings.API_PORT,
    reload=False,
)
