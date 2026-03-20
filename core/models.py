from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=80)
    category = models.CharField(max_length=50, default='Technical')

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    period = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=150)
    qualification = models.CharField(max_length=150)
    period = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.qualification} - {self.institution}"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} — {self.subject}"
