from django.db import models
class Person(models.Model):
    name=models.CharField(max_length=100)
    gen=models.CharField(max_length=100)
    age=models.IntegerField()
    mail=models.CharField(max_length=100)

    