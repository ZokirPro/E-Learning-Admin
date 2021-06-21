from django.db import models

# Create your models here.
class Region(models.Model):
    code=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=250)

    class Meta:
        db_table='regions'

class District(models.Model):
    code=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=250)
    region=models.ForeignKey(Region,on_delete=models.CASCADE,db_column='region_code')

    class Meta:
        db_table='districts'

class News(models.Model):
    keyword=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    description=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=255)
    img=models.ImageField(upload_to='news_blogs/')

    class Meta:
        db_table='news'

class Contact(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    fax=models.CharField(max_length=255)
    point=models.CharField(max_length=255)

    class Meta:
        db_table='contacts'

class Blog(models.Model):
    keyword=models.CharField(max_length=255)
    questions=models.CharField(max_length=255)
    description=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(upload_to='news_blogs/')

    class Meta:
        db_table='blogs'
class Payment(models.Model):
    #user_id 
    status=models.IntegerField()
    description=models.TextField()
    amount=models.CharField(max_length=255)
    date_created=models.DateTimeField(auto_now_add=True)
    date_pay=models.DateTimeField(auto_now_add=True)
    type_payment=models.CharField(max_length=255)

    class Meta:
        db_table='payments'

class Translate(models.Model):
    table_name=models.CharField(max_length=255)
    field_id=models.IntegerField()
    field_name=models.CharField(max_length=255)
    field_description=models.CharField(max_length=255)
    field_value=models.CharField(max_length=255)
    language_code=models.CharField(max_length=255)

    class Meta:
        db_table='translates'

class Lang(models.Model):
    name = models.CharField(max_length=255)
    url=models.CharField(max_length=255)
    img=models.ImageField(upload_to='additional/')
    status=models.IntegerField()
    default=models.BooleanField()

    class Meta:
        db_table='langs'


class Teacher_Educenter(models.Model):
    #teacher_id from users 
    #educenter_id from users
    pass