from django.db import models

# Create your models here.
class PLZO(models.Model):
    city_name = models.CharField(max_length=255)
    postcode = models.IntegerField()
    additional_number = models.IntegerField()
    community_name = models.CharField(max_length=255)
    bfs_nr = models.IntegerField()
    canton_abbrev = models.CharField(max_length=2)
    wgs84_e = models.FloatField()
    wgs84_n = models.FloatField()
    lang = models.CharField(max_length=2)
    
    def __str__(self):
        return str(self.postcode) + ' ' + self.city_name + ' ' + self.canton_abbrev
