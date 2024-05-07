from django.shortcuts import render
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView

class UserProfileView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class HotelView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['country', 'city']
    search_fields = ["name"]
    ordering_fields = ['rating',]
    permission_classes = [IsAuthenticatedOrReadOnly]

class HotelDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class CommentView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class HotelImageView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class HotelImageDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelImageSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class RoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["room_number"]
    permission_classes = [IsAuthenticatedOrReadOnly]

class RoomDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class ImageRoomView(ListAPIView):
    queryset = ImageRoom.objects.all()
    serializer_class = ImageRoomSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class ImageRoomDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ImageRoom.objects.all()
    serializer_class = ImageRoomSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class BookingView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]