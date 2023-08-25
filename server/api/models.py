from django.db import models

    
class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class EconomicIndex(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    macro = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
