from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Experience, Education, Skill
from .forms import ContactForm


def home(request):
    projects = Project.objects.filter(featured=True)
    experiences = Experience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Message sent! I will get back to you soon.')
            return redirect('home')
        else:
            messages.error(request, '❌ Please fix the errors below.')

    return render(request, 'core/index.html', {
        'projects': projects,
        'experiences': experiences,
        'education': education,
        'skills': skills,
        'form': form,
    })
