from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    def to_dictionary(self):
        return {
            'name': self.name,
            'description': self.description
        }