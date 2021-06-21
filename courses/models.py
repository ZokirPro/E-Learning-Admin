from django.db import models
from lessons.models import Lesson
from library.models import Educational_Material
# Create your models here.
class Course_Category(models.Model):
    name=models.CharField(max_length=250)

    class Meta:
        db_table='course_categories'

class Course_Language(models.Model):
    name=models.CharField(max_length=250)

    class Meta:
        db_table='course_languages'

class Course(models.Model):
    #user_id 
    name=models.CharField(max_length=250)
    date_created=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='courses/')
    description=models.TextField()
    language=models.ForeignKey(Course_Language,on_delete=models.CASCADE)
    category=models.ForeignKey(Course_Category,on_delete=models.SET_NULL,null=True)
    type=models.CharField(max_length=200)
    grade=models.FloatField()
    publish=models.BooleanField()

    class Meta:
        db_table='courses'

class Tag(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        db_table='tags'

class Course_Tag(models.Model):
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    
    class Meta:
        db_table='course_tags'

class Course_Review(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    #user_id 
    comment=models.TextField()
    grade=models.IntegerField()

    class Meta:
        db_table='course_reviews'

class Comment_Course(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    #user_id
    comment=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='comment_courses'

class Course_Plan(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    lesson=models.ForeignKey(Lesson, on_delete=models.CASCADE)
    sort=models.IntegerField()

    class Meta:
        db_table='course_plans'

class Course_Material(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    material=models.ForeignKey(Educational_Material,on_delete=models.CASCADE)

    class Meta:
        db_table='course_materials'

class Course_Programme(models.Model):
    name=models.CharField(max_length=250)
    #user_id
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='courses/')
    description=models.TextField()
    language=models.ForeignKey(Course_Language,on_delete=models.CASCADE)
    category=models.ForeignKey(Course_Category,on_delete=models.CASCADE)
    type=models.CharField(max_length=250)
    grade=models.FloatField()
    publish=models.BooleanField()

    class Meta:
        db_table='course_programmes'

class Student_and_Course(models.Model):
    #student_id from users 
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    progress=models.FloatField(blank=True,null=True,default=0)

    class Meta:
        db_table='student_and_courses'