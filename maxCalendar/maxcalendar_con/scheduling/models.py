from django.db import models

# Create your models here.


class Scheduling(models.Model):
    name=models.CharField(max_length=30,verbose_name="Başlık")
    description=models.TextField(verbose_name="Açıklama")
    location=models.CharField(max_length=20,verbose_name="Konum")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name=("Eklenme Tarihi"))

    def __str__(self): 
        return self.name