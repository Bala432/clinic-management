from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

class Patient(models.Model):

    uid = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10,validators=[MinLengthValidator(10)])
    email = models.EmailField(blank=True)
    area = models.CharField(max_length=128)
    height = models.PositiveIntegerField(blank=True,default=0)
    weight = models.PositiveIntegerField(blank=True,default=0)
    bpi = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return str(self.uid)

    def get_absolute_url(self):
        return reverse("patient_detail",kwargs={'pk':self.pk})

    def get_email(self):
        return self.email

class Consult(models.Model):

    id = models.AutoField(primary_key=True)
    consult = models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    problem = models.CharField(max_length=128)
    treatment = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id)

class SendEmail(models.Model):

    pass_email = models.OneToOneField(Patient,on_delete=models.CASCADE,primary_key=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)


