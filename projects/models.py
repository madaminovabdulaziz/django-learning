from django.db import models

# Create your models here.



class Projects(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField()


    def __str__(self):
        return f"{self.name} which costs {self.cost}"