from django.db import models
from django.contrib.auth.models import User


class UserProfile(User):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=30)
    photo = models.ImageField(blank=True, null=True, upload_to='images')
    phone_number = models.IntegerField()
    # email = models.EmailField()

    def __str__(self):
        return self.first_name


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField()
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.CASCADE, blank=True, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],)

    def __str__(self):
        return self.text


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        pass


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    price_per_night = models.BigIntegerField(default=0)

class ImageRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        pass


STATUS_CHOICES = (
    ("Бронь", "Бронь"),
    ("Cвободный", "Cвободный"),
    ('Отменено', 'Отменено'),
    ('В ожидании', 'В ожидании'),
)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    price = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=32)

