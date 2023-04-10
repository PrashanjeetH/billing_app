from rest_framework import serializers
from ProfileApp.models import Profile,  Skill, About


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
