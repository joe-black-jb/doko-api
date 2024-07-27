from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, blank=True)
    position_x_start = models.IntegerField()
    position_x_end = models.IntegerField()
    position_y_start = models.IntegerField()
    position_y_end = models.IntegerField()

    def __str__(self):
        return self.name


