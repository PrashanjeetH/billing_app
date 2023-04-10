from django.contrib import admin
from ProfileApp.models import Profile, Skill,About

# Register your models here.
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(About)