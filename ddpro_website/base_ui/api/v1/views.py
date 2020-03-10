from rest_framework import viewsets
from .serializers import AboutSerializer, TeamMemberSerializer, ProductSerializer
from ...models import About, TeamMember, Product


class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()

    def get_serializer_class(self):
        return AboutSerializer