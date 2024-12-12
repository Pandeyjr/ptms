from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=100)
    starting_point = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    start_lat = models.FloatField()  # Latitude of the starting point
    start_lon = models.FloatField()  # Longitude of the starting point
    end_lat = models.FloatField()    # Latitude of the destination point
    end_lon = models.FloatField()    # Longitude of the destination point
    # You can add more fields like stops, bus assignment, etc.

    def __str__(self):
        return self.name
