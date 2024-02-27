from django.db import models

# Create your models here.

class Photo(models.Model):
    url = models.URLField(max_length=255, null = True)

    def __str__(self):
        return self.url

class Product(models.Model):
    name = models.CharField(max_length=255, null = True)
    description = models.TextField(null = True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null = True)
    url = models.URLField(max_length=255, null = True)
    view_count = models.IntegerField(default=0)

    similar_products = models.ManyToManyField('self', blank=True)
    # status = {None, "error", "complete"} - None = not yet scraped, "error" = error while scraping, "complete" = scraped
    status = models.CharField(max_length=255, null = True)
    store = models.CharField(max_length=255, null = True)
    
    photos = models.ManyToManyField(Photo)

    def __str__(self):
        return self.name
    


