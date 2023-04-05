from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.topic_name
class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    p_name=models.CharField(max_length=30)
    p_age=models.IntegerField()
    p_url=models.URLField()
    def __str__(self):
        return self.p_name
class Avengers(models.Model):
    p_name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    P_power=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.p_name
    