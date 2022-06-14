from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformations
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationModel
        fields = '__all__' 

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModel
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsModel
        fields = '__all__'