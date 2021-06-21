from django.db import models
from library.models import Educational_Material
# Create your models here.
class Lesson(models.Model):
    #user_id
    name=models.CharField(max_length=250)
    date_created=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='lessons/')
    publish=models.BooleanField()

    class Meta:
        db_table='lessons'

class Lesson_Plan(models.Model):
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    sort=models.IntegerField()

    class Meta:
        db_table='lesson_plans'

class Plan_Detail(models.Model):
    plan=models.ForeignKey(Lesson_Plan,on_delete=models.CASCADE)
    content=models.TextField(blank=True)
    material=models.ForeignKey(Educational_Material,on_delete=models.SET_NULL,null=True)
    sort=models.IntegerField()

    class Meta:
        db_table="plan_details"

class Student_and_Lessons(models.Model):
    #student_id from users
    lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    progress=models.FloatField()

    class Meta:
        db_table="student_and_lessons"

