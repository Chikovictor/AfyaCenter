from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=30)
    appointment_date = models.DateTimeField()
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)    # ENSURES APPOINTMENTS ARE NOT DELETED IF A DOCTOR,SERVICE OR DEPARTMENT IS DEACTIVATED
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)   #Foreign key links appointments to available departments,doctors en services
    application_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.name} with {self.doctor} on {self.appointment_date}"

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=30)
    Message = models.TextField()

    def __str__(self):        # provides a readable form of each object when represented in the form or admin views
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)   #determines if the doctor is active ,that is,available in DB

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)    # a doctor belongs to a department which ensures proper data relationships
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

