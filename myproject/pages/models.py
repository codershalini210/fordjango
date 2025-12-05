from django.db import models
class ContactSubmission(models.Model):
    name =models.CharField(max_length=80)
    email = models.EmailField()
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=150)
    don = models.DateField()
    isenrolled = models.BooleanField(default=True)
# Create your models here.

