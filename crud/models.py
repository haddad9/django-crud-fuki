from django.db import models

# Create your models here.
class crud(models.Model):
    id = models.BigAutoField(primary_key=True)
    matkul = models.CharField(max_length=40) 
    
    
   
    dosen = models.CharField(max_length=40)
    jumlah_sks = models.CharField(max_length=40) 
    deskripsi = models.CharField(max_length=40)
    
    class Meta:
      db_table = "crud"
      