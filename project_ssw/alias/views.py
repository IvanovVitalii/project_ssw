from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from alias.models import Alias
from alias.serializers import AliasSerializer


class AliasViewSet(ModelViewSet):
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer

    # Подключаем filter, search и ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['alias', 'target', 'start', 'end']
    search_fields = ['alias', 'target', 'start', 'end']
    ordering_fields = ['alias', 'target', 'start', 'end']
