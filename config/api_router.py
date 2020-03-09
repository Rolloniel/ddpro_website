from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from ddpro_website.users.api.v1.views import UserViewSet
from ddpro_website.base_ui.views import AboutViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("about", AboutViewSet)


app_name = "api"
urlpatterns = router.urls
