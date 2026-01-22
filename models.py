from django.db import models

# ------------------------------
# Departments
# ------------------------------
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# ------------------------------
# Subjects linked to Department
# ------------------------------
class Subject(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='subjects'
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.department.name} - {self.name}"

# ------------------------------
# Admission Applications
# ------------------------------
class AdmissionApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True, blank=True
    )
    preferred_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='applicant_photos/', blank=True, null=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.department})"

# ------------------------------
# School Info
# ------------------------------
class SchoolInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='school_logos/', blank=True, null=True)

    def __str__(self):
        return self.title

# ------------------------------
# Campus Life
# ------------------------------
class CampusLife(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='campus_life_images/', blank=True, null=True)

    def __str__(self):
        return self.title

# ------------------------------
# Notices
# ------------------------------
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    attachment = models.FileField(upload_to='notices/', blank=True, null=True)

    def __str__(self):
        return self.title

# ------------------------------
# Jobs / Careers
# ------------------------------
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    apply_link = models.URLField(blank=True)
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
