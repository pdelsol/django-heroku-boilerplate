from django.db import models


class Appmodel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'APPNAME'
