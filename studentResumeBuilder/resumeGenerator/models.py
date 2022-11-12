from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)
    mobile = models.PositiveIntegerField(blank=True)

    def full_name(self):
        return " ".join([self.first_name, self.last_name])


class Education(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    varsity_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=50)
    stream = models.CharField(max_length=100)
    passing_year = models.DateField()
    result = models.CharField(max_length=5)

    school10_name = models.CharField(max_length=255)
    board10 = models.CharField(max_length=100)
    passing_year10 = models.DateField()
    result10 = models.CharField(max_length=5)

    school12_name = models.CharField(max_length=255)
    board12 = models.CharField(max_length=100)
    passing_year12 = models.DateField()
    result12 = models.CharField(max_length=5)


class Skills(models.Model):
    person = models.ForeignKey(PersonalInfo,on_delete=models.CASCADE)
    skill_detail = models.TextField()


class Projects(models.Model):
    person = models.ForeignKey(PersonalInfo,on_delete=models.CASCADE)
    project_detail = models.TextField()
    

class Achievements(models.Model):
    person = models.ForeignKey(PersonalInfo,on_delete=models.CASCADE)
    achievement_detail = models.TextField()


class resume(models.Model):
    username = models.CharField(max_length=255,blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)
    mobile = models.PositiveIntegerField(blank=True)
    
    varsity_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=50)
    stream = models.CharField(max_length=100)
    passing_year = models.DateField()
    result = models.CharField(max_length=5)

    school10_name = models.CharField(max_length=255)
    board10 = models.CharField(max_length=100)
    passing_year10 = models.DateField()
    result10 = models.CharField(max_length=5)

    school12_name = models.CharField(max_length=255)
    board12 = models.CharField(max_length=100)
    passing_year12 = models.DateField()
    result12 = models.CharField(max_length=5)

    skill_detail = models.TextField()
    project_detail = models.TextField(blank=True)
    achievement_detail = models.TextField(blank=True)
