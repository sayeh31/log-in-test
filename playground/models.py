from django.db import models

# Create your models here.
class Userlevels(models.Model):
    id = models.IntegerField(db_column='id',primary_key=True)
    username = models.CharField(db_column='username',max_length=45)  # Field name made lowercase.
    FormLevel = models.IntegerField(db_column='FormLevel')  # Field name made lowercase.
    

    class Meta:
        managed = True
        db_table = 'test'