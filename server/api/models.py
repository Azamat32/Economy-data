from django.db import models

class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'regions'
        managed = False

    def __str__(self):
        return self.name
    
##############################################################################
class GDP(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField()
    value = models.BigIntegerField()  # NUMERIC в PostgreSQL
    period = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    updated_at = models.DateField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        db_table = 'gdp'
        managed = False

########################################################################
class LaborProductivityActivityType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'labor_productivity_activity_types'
        managed = False

    def __str__(self):
        return self.name


class LaborProductivity(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField()
    value = models.BigIntegerField()
    period = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    updated_at = models.DateField()
    economic_activity = models.ForeignKey(LaborProductivityActivityType, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        db_table = 'labor_productivity'
        managed = False
    
    #######################################################