from django.db import models

class SkillsModel(models.Model):
    skills = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.skills


class UserInformations(models.Model):
    profile_image = models.ImageField(upload_to='media',blank=True,null=True)
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)
    profession  = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    country = models.CharField(max_length=255,blank=True,null=True)
    phone_number = models.CharField(max_length=10)
    pin_code = models.CharField(max_length=8,blank=True,null=True)
    email = models.EmailField()
    social_links = models.URLField(blank=True,null=True)
    skills = models.ManyToManyField(SkillsModel,blank=True,null=True)
    profile_summary = models.TextField()

    def __str__(self) -> str:
        return self.first_name


class ExperienceModel(models.Model):
    user = models.ForeignKey(UserInformations,on_delete=models.CASCADE, null=True, blank=True)
    job_title = models.CharField(max_length=255)
    Company_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    job_discription = models.CharField(max_length=255)
    project_urls = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.job_title



class EducationModel(models.Model):
    user = models.ForeignKey(UserInformations,on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    school_location = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)

    def __str__(self) -> str:
        return self.school_name







# education = models.ManyToManyField(EducationModel,blank=True)
#     experience = models.ManyToManyField(ExperienceModel,blank=True)
#     skills = models.ManyToManyField(SkillsModel,blank=True)