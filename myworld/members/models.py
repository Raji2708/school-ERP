from django.db import models

class Register(models.Model):
  name = models.CharField(max_length=100)
  ids = models.CharField(max_length=100)
  age = models.CharField(max_length=100)
  classs = models.CharField(max_length=100)
  fee = models.CharField(max_length=100)
  balance = models.CharField(max_length=100)
  percent = models.CharField(max_length=100)

class Circular(models.Model):
  circular = models.CharField(max_length=1000)

class Employee(models.Model):
  name = models.CharField(max_length=1000)
  password = models.CharField(max_length=1000)
  designation = models.CharField(max_length=1000)

class Allocation(models.Model):
  staffname = models.CharField(max_length=1000)
  stdid1 = models.CharField(max_length=1000)
  stdid2 = models.CharField(max_length=1000)

class Assignmentx(models.Model):
  assignment = models.CharField(max_length=1000)
  name = models.CharField(max_length=1000)

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')  # Saves to /media/uploads/

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    clas = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='uploads/')  # Saves to /media/uploads/
    marksheet = models.ImageField(upload_to='uploads/')  # Saves to /media/uploads/

    def __str__(self):
        return self.title

class Staff(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='uploads/')  # Saves to /media/uploads/

    def __str__(self):
        return self.title