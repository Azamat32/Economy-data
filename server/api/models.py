from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название разделала")
    

    def __str__(self):
        return f"Название раздела: {self.name}"
    

    def get_absolute_url(self):
        return reverse("topic", kwargs={"topic_id":self.pk})
    

    # class Meta:
    #     verbose_name = "Задания"
    #     verbose_name_plural = "Задания"
    #     ordering = ["name"]


class Economic_index(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255, null=True)
    macro_topic = models.ForeignKey("Topic", on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Название экономического показателя: {self.name}"
    
    
    # def get_absolute_url(self):
    #     return reverse("", kwargs={"topic_id":self.pk})