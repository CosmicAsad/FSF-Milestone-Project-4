from django.db import models
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    artist = models.CharField(max_length=254, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_src = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', null=True,
                                blank=True, on_delete=models.SET_NULL)
    profile = models.ForeignKey(UserProfile,
                                related_name='reviews', null=True,
                                blank=True, on_delete=models.SET_NULL)
    review_text = models.TextField()
