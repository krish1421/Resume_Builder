from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class UserListView(APIView):
    def get(self, request):
        queryset = UserInformations.objects.all()
        serializers = UserSerializer(queryset,many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        # skill_data = request.data.getlist('skills_list',list())
        if serializer.is_valid():
            serializer.save()
            # for i in skill_data:
            #     new = SkillsModel.objects.filter(id=i).first()
            #     if new:
            #         user_detail.skills.add(new)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        # serializer = UserSerializer(data=request.data)
        # education_data = request.data.getlist('education_list',list())
        # experience_data = request.data.getlist('experience_list',list())
        # skill_data = request.data.getlist('skills_list',list())
        # if serializer.is_valid():
        #     user_detail= serializer.save()
        #     for i in education_data:
        #         new = EducationModel.objects.filter(id=i).first()
        #         if new:
        #             user_detail.education.add(new)
            
        #     for i in experience_data:
        #         new = ExperienceModel.objects.filter(id=i).first()
        #         if new:
        #             user_detail.experience.add(new)

        #     for i in skill_data:
        #         new = SkillsModel.objects.filter(id=i).first()
        #         if new:
        #             user_detail.skills.add(new)
            
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class EducationListView(APIView):
    def get(self, request):
        queryset = EducationModel.objects.all()
        serializer = EducationSerializer(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request_data = request.data.copy()
        user = UserInformations.objects.filter(id=request.data.get('user')).first()
        request_data['user'] = user.id
        serializer = EducationSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class ExperienceListView(APIView):
    def get(self, request):
        queryset = ExperienceModel.objects.all()
        serializer = ExperienceSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request_data = request.data.copy()
        user = UserInformations.objects.filter(id=request.data.get('user')).first()
        request_data['user'] = user.id
        serializer = ExperienceSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class SkillListView(APIView):
    def get(self, request):
        queryset = SkillsModel.objects.all()
        serializer = SkillSerializer(queryset,many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    def post(self, request): 
        new = UserInformations.objects.filter(id=request.data.get('id')).first()
        if new:
            data = request.data.get("skills")
            data = data.split(",")
            for i in data:
                request_data = request.data.copy()
                request_data.pop('skills')
                request_data['skills'] = i
                serializer = SkillSerializer(data=request_data)
                if serializer.is_valid():
                    serializer.save()
                    skill_obj = SkillsModel.objects.filter(skills=i).first()
                    new.skills.add(skill_obj)
                    new.save() 
                else:
                    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("user not found", status=status.HTTP_404_NOT_FOUND)
        
class ResumeView(APIView):
    def get(self, request):
        queryset = UserInformations.objects.all()
        serializer = ResumeSerializer(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ResumedetailView(APIView):
    def get(self, request,id):
        queryset = UserInformations.objects.filter(id=id).first()
        serializer = ResumeSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

