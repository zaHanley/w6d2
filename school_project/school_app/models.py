from django.db import models
from django.core import validators as v
# OR from django.core.validators import * / specific ones you want
from .validators import validate_locker_combination

class Locker(models.Model):
    locker_number = models.IntegerField(unique=True, validators=[v.MinValueValidator(100)])
    combination = models.CharField(max_length=10, validators=[validate_locker_combination]) 
    #we want to add validation on front and back end
    #combination should adhere to a specific format
    #django has certain validators already built in
    #create validators.py to set them up

class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_date = models.DateField()
    locker = models.OneToOneField(Locker, null=True, on_delete=models.SET_NULL, related_name="student")
    #related_name is "how can i access this info from another class?"

    def __str__(self):
        return f"STUDENT: {self.first_name} {self.last_name}"

class Professor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    start_date = models.DateField()
    

    def __str__(self):
        return f"PROFESSOR: {self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    credits = models.IntegerField(validators=[v.MinValueValidator()])
    #based on this connection, a professor will have attribute courses
    #many to one - one prof can have many courses. we make the foreign key on the one
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="courses")
    #many to many - a course has many students, a student has many courses
    # students = models.ManyToManyField(Student, related_name="courses")
    #we can have a list of students directly in our course model BASED ON THE ENROLLMENT FIELD
    students = models.ManyToManyField(Student, through="Enrollment")
    def __str__(self):
        return f"COURSE: {self.name}"

class Enrollments(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    grade = models.CharField(max_length=2, validators=[v.RegexValidator(regex=r"ABCDF][+-]?")])

    class Meta:
        #set unique constraing on whatever we pass in
        unique_together = (("student", "course"))

    def __str__(self):
        return f"ENR: {self.student} in {self.course}"