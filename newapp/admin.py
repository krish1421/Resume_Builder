from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(ExperienceModel)
admin.site.register(EducationModel)
admin.site.register(SkillsModel)

class ExperienceAdmin(admin.StackedInline):
    model = ExperienceModel

class EducationModelAdmin(admin.StackedInline):
    model = EducationModel

class UserAdmin(admin.ModelAdmin):
    model = UserInformations
    inlines = [ExperienceAdmin,EducationModelAdmin]


# class HOGEModelInline(admin.TabularInline):
#     model = UserInformations
#     readonly_fields = ('image_preview',)

#     def image_preview(self, obj):
#         # ex. the name of column is "image"
#         if obj.image:
#             return mark_safe('<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.image.url))
#         else:
#             return '(No image)'

#     image_preview.short_description = 'Preview'


admin.site.register(UserInformations,UserAdmin)
