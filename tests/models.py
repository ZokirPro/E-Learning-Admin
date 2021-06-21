from django.db import models

# Create your models here.
class Type_Questions(models.Model):
    name=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    
    class Meta:
        db_table = "type_questions"


class Question(models.Model):
    #user_id
    question=models.TextField()
    type=models.ForeignKey('Type_Questions',on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = "questions"

class Answer(models.Model):
    question=models.ForeignKey('Question',on_delete=models.CASCADE)
    answer=models.TextField()
    check=models.BooleanField()

    class Meta:
        db_table = "answers"

class Question_Group(models.Model):
    #user_id
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='tests/')
    duration=models.FloatField()
    min_grade=models.FloatField()

    class Meta:
        db_table="question_groups"

class Question_Group_Detail(models.Model):
    question_group=models.ForeignKey('Question_Group',on_delete=models.CASCADE)
    question=models.ForeignKey('Question',on_delete=models.CASCADE)  

    class Meta:
        db_table='question_group_details'           

class Question_Answer(models.Model):
    keyword=models.CharField(max_length=250)
    questions=models.CharField(max_length=250)
    answers=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='test/')

    class Meta:
        db_table='question_answers'

class Student_and_Test(models.Model):
    #user_id
    question_group=models.ForeignKey('Question_Group',on_delete=models.CASCADE)
    grade=models.FloatField()
    status=models.BooleanField()

    class Meta:
        db_table='students_and_tests'

class Student_Test_Details(models.Model):
    student_test=models.ForeignKey('Student_and_Test',on_delete=models.CASCADE)
    question_group_detail=models.ForeignKey('Question_Group_Detail',on_delete=models.CASCADE)
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    check=models.BooleanField()

    class Meta:
        db_table='student_test_details'