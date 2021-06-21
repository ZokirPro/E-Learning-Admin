from django.db import models

# Create your models here.
class Educational_Material(models.Model):
    date_created=models.DateTimeField(auto_now_add=True)
    #user_id
    material=models.FileField(upload_to='materials/')

    class Meta:
        db_table = "educational_materials"
