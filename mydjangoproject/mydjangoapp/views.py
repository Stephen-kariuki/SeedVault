# mydjangoapp/views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    mydjangoapp_seeds, Monitoring, AdminFeedback, AdminSeedCatalog, AdminSubscription,
    DampnessAnalytics, Events, LightExposureAnalytics, Security, Storage,
    TemperatureAnalytics, User, Weather
)
from .serializers import (
    SeedSerializer, MonitoringSerializer, AdminFeedbackSerializer, AdminSeedCatalogSerializer,
    AdminSubscriptionSerializer, DampnessAnalyticsSerializer, EventsSerializer,
    LightExposureAnalyticsSerializer, SecuritySerializer, StorageSerializer,
    TemperatureAnalyticsSerializer, UserSerializer, WeatherSerializer
)

class SeedViewSet(viewsets.ModelViewSet):
    queryset = mydjangoapp_seeds.objects.all()
    serializer_class = SeedSerializer

class MonitoringViewSet(viewsets.ModelViewSet):
    queryset = Monitoring.objects.all()
    serializer_class = MonitoringSerializer

class AdminFeedbackViewSet(viewsets.ModelViewSet):
    queryset = AdminFeedback.objects.all()
    serializer_class = AdminFeedbackSerializer

class AdminSeedCatalogViewSet(viewsets.ModelViewSet):
    queryset = AdminSeedCatalog.objects.all()
    serializer_class = AdminSeedCatalogSerializer

class AdminSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = AdminSubscription.objects.all()
    serializer_class = AdminSubscriptionSerializer

class DampnessAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = DampnessAnalytics.objects.all()
    serializer_class = DampnessAnalyticsSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class LightExposureAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = LightExposureAnalytics.objects.all()
    serializer_class = LightExposureAnalyticsSerializer

class SecurityViewSet(viewsets.ModelViewSet):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer

class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

class TemperatureAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = TemperatureAnalytics.objects.all()
    serializer_class = TemperatureAnalyticsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class SeedAPIView(APIView):
    def get(self, request):
        seeds = mydjangoapp_seeds.objects.all()
        serializer = SeedSerializer(seeds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SeedSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MonitoringAPIView(APIView):
    def get(self, request):
        monitoring_data = Monitoring.objects.all()
        serializer = MonitoringSerializer(monitoring_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MonitoringSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminFeedbackAPIView(APIView):
    def get(self, request):
        feedbacks = AdminFeedback.objects.all()
        serializer = AdminFeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AdminFeedbackSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminSeedCatalogAPIView(APIView):
    def get(self, request):
        seed_catalog = AdminSeedCatalog.objects.all()
        serializer = AdminSeedCatalogSerializer(seed_catalog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AdminSeedCatalogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminSubscriptionAPIView(APIView):
    def get(self, request):
        subscriptions = AdminSubscription.objects.all()
        serializer = AdminSubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AdminSubscriptionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DampnessAnalyticsAPIView(APIView):
    def get(self, request):
        analytics = DampnessAnalytics.objects.all()
        serializer = DampnessAnalyticsSerializer(analytics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DampnessAnalyticsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventsAPIView(APIView):
    def get(self, request):
        events = Events.objects.all()
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LightExposureAnalyticsAPIView(APIView):
    def get(self, request):
        analytics = LightExposureAnalytics.objects.all()
        serializer = LightExposureAnalyticsSerializer(analytics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LightExposureAnalyticsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SecurityAPIView(APIView):
    def get(self, request):
        security_data = Security.objects.all()
        serializer = SecuritySerializer(security_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SecuritySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StorageAPIView(APIView):
    def get(self, request):
        storage_data = Storage.objects.all()
        serializer = StorageSerializer(storage_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StorageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TemperatureAnalyticsAPIView(APIView):
    def get(self, request):
        analytics = TemperatureAnalytics.objects.all()
        serializer = TemperatureAnalyticsSerializer(analytics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TemperatureAnalyticsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeatherAPIView(APIView):
    def get(self, request):
        weather_data = Weather.objects.all()
        serializer = WeatherSerializer(weather_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
