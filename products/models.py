from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    content = RichTextField()
    price = models.FloatField()
    discount = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


