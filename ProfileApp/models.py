from django.db import models
from UserApp.models import User


# All user profile details..
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    firstName = models.CharField(max_length=25, blank=True, null=True)
    lastName = models.CharField(max_length=25, blank=True, null=True)
    headLine = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=40, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)


class About(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=2000, blank=True, null=True)



class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100,blank=True,null=True)

    class Meta:
        unique_together = ['user', 'skill']