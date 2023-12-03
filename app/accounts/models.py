from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import STATUS_CHOICES, PENDING_COMPLETE_DATA, GENDER_CHOICES, NONE, \
    CLOSET_CHOICES, FIRST_CLOSET


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    The default Django user model has the following fields:
    - username
    - password
    - email
    """
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    telephone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default=PENDING_COMPLETE_DATA)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=NONE)

    def __str__(self):
        return "{} {} - {}".format(self.first_name, self.last_name, self.email)


class Item(models.Model):
    """
    Item model that represents a product in the system.
    """
    item_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    closet_number = models.CharField(
        max_length=20,
        choices=CLOSET_CHOICES,
        default=FIRST_CLOSET
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Name: {} | Quantity: {} | Closet: {}".format(self.name,
                                                             self.quantity,
                                                             self.closet_number)
