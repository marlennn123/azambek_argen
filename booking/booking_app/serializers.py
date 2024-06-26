from rest_framework.serializers import ModelSerializer
from .models import *
from django.db.models import Avg
from rest_framework import serializers

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class HotelSerializer(ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ('id', 'name', 'description', 'address', "country", "city", 'average_rating')

    def get_average_rating(self, obj):
        rating = Comment.objects.filter(hotel=obj)
        average = rating.aggregate(Avg('rating'))['rating__avg']
        return average if average is not None else 0


class HotelImageSerializer(ModelSerializer):
    class Meta:
        model = HotelImage
        fields = "__all__"

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class ImageRoomSerializer(ModelSerializer):
    class Meta:
        model = ImageRoom
        fields = "__all__"

class BookingSerializer(ModelSerializer):
    total_cost = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ["id", "user", "room", "check_in_date", "check_out_date", "total_cost", "status"]

    def get_total_cost(self, obj):
        cost = (obj.check_out_date - obj.check_in_date).days
        total_price = cost * obj.price
        return total_price

