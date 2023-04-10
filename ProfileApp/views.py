from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ProfileApp.models import Profile, Skill, About
from ProfileApp.serializers import ProfileSerializers, SkillSerializer, AboutSerializers

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializers
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
