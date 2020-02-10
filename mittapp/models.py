from django.db import models

# Create your models here.
class Achievements(models.Model):
    date = models.IntegerField()
    description = models.CharField(max_length=200)

    def __str__(self):
        description = self.description[:8]
        return str(self.date) + ": " +  description + "..."