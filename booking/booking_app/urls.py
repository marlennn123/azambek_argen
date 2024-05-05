from django.urls import path, include
from .views import *

urlpatterns = [
    path("userprofiles/", UserProfileView.as_view()),
    path("userprofiles/<int:pk>/", UserProfileDetailView.as_view()),
    path("hotels/", HotelView.as_view()),
    path("hotels/<int:pk>/", HotelDetailView.as_view()),
    path("comments/", CommentView.as_view()),
    path("comments/<int:pk>/", CommentDetailView.as_view()),
    path("hotelimages/", HotelImageView.as_view()),
    path("hotelimages/<int:pk>/", HotelImageDetailView.as_view()),
    path("rooms/", RoomView.as_view()),
    path("rooms/<int:pk>/", RoomDetailView.as_view()),
    path("roomimages/", ImageRoomView.as_view()),
    path("roomimages/<int:pk>/", ImageRoomDetailView.as_view()),
    path("bookings/", BookingView.as_view()),
    path("bookings/<int:pk>/", BookingDetailView.as_view()),
]