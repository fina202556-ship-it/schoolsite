from django.contrib import admin
from .models import Department, Subject, AdmissionApplication, SchoolInfo, CampusLife, Notice, Job

admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(AdmissionApplication)
admin.site.register(SchoolInfo)
admin.site.register(CampusLife)
admin.site.register(Notice)
admin.site.register(Job)
