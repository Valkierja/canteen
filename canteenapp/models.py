from django.db import models

class DinnerTable(models.Model):
    ID = models.CharField(primary_key=True,max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.ID

class ChaoCai(models.Model): #炒菜
    table = models.ManyToManyField(DinnerTable)
    name = models.CharField(max_length=64)
    num = models.PositiveIntegerField()
    price = models.FloatField(primary_key=True)

    def __str__(self) -> str:
        return self.name
    

