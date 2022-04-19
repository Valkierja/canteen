from django.db import models

class DinnerTables(models.Model):
    ID = models.IntegerField(name="ID",primary_key=True)
    date = models.DateTimeField(auto_now_add=True,name="date")

    def __str__(self) -> str:
        return "第"+str(self.ID)+"桌"

class TableOrders(models.Model):
    

