from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.topic_name
class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    p_name=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.p_name