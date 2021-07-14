from django.db import models

# Create your models here.
class DiaryModel(models.Model):
    diary_msg=models.TextField(max_length=1000)
    time=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Diary {self.id}"