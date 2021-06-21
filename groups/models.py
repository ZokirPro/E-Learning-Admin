from django.db import models

# Create your models here.
class Group(models.Model):
    name=models.CharField(max_length=250)
    #creator_id from users 
    date_created=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='groups/')
    description=models.TextField(blank=True,null=True)

    class Meta:
        db_table='groups'

class Student_Group(models.Model):
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    #student_id from users 
    date_joined=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='student_groups'