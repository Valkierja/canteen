from cProfile import label
from django.db import models

class DinnerTable(models.Model):
    ID = models.CharField(primary_key=True,max_length=64)
    date = models.DateTimeField(auto_now_add=True)

    a1 = models.CharField(verbose_name="米饭（1.1元/碗）",max_length=10,default=0)
    a2 = models.CharField(verbose_name="炒白菜（3.4元/份）",max_length=10,default=0)
    a3 = models.CharField(verbose_name="红烧猪蹄（18元/只）",max_length=10,default=0)
    a4 = models.CharField(verbose_name="可乐（3.3元/瓶）",max_length=10,default=0)
    price = 0
    def getPrice(self):
        self.price = 0
        self.price = int(self.a1[:]) * 1.1 + int(self.a2[:]) * 3.4 + int(self.a3[:]) *  18 + int(self.a4[:]) * 3.3
        print(self.price+"\n")
        print(self.date)
        return
    
    def __str__(self) -> str:
        return self.ID



# class ChaoCai(models.Model): #炒菜
#     table = models.ManyToManyField(DinnerTable)
#     name = models.CharField(max_length=64)
#     num = models.PositiveIntegerField()
#     price = models.FloatField(primary_key=True)

#     def __str__(self) -> str:
#         return self.name
    

