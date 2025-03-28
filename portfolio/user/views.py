from django.shortcuts import render, redirect, get_object_or_404
from user.models import *
from django.contrib import messages
from django.core.mail import send_mail
from .forms import *
from django.conf import settings

def indexpage(request):
    hero = HeroInfo.objects.first()
    educations = EducationAndTraining.objects.all().order_by('-id')
    skill_categories = SkillCategory.objects.all()
    projects = MyProject.objects.all().order_by('-id')
    footer = Footer.objects.first() 
    social_icons = SocialIcon.objects.all()
    context = {
        'hero': hero,
        'skill_categories': skill_categories,
        'educations': educations,
        'projects':projects,
        'footer': footer,
        'social_icons': social_icons,
    }
    return render(request, 'index.html', context)

def contactpage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            subject = f"New Contact Form Submission from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,  
                ["bonyaminshaznuz@gmail.com"],  
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})