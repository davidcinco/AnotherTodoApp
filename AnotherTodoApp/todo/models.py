from django.db import models

# Create your models here.
class Todo(models.Model):
    todoid = models.AutoField(primary_key=True)        
    tododescription = models.TextField(blank=True, null=True)
    tododone = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'todo'


class Users(models.Model):
    userid = models.AutoField(primary_key=True)        
    username = models.CharField(max_length=175)        
    password = models.CharField(max_length=85)
    email = models.CharField(max_length=195)

    class Meta:
        managed = False
        db_table = 'users'