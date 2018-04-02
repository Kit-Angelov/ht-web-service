from ht_web_service.apps.ht import models
from ht_web_service.users.models import User as CustomUser
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import filters


class FeaturesViewSet(viewsets.ModelViewSet):

    model = models.Feature
    queryset = models.Feature.objects.all()
    serializer_class = serializers.FeatureSerializers
    filter_class = filters.FeatureFilter


class HistoriesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = models.History.objects.all()
    serializer_class = serializers.HistorySerializers
    filter_class = filters.HistoryFilter


class AttributesApiView(APIView):

    def get(self, request, format=None):
        attributes = models.get_attributes()
        return Response(attributes)


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializers
