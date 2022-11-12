from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse
from django.contrib.sites.requests import RequestSite
from django.contrib.auth import get_user_model
from .models import resume
User = get_user_model()

# Create your views here.

def resume_form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        email = request.POST['email']
        website = request.POST['website']
        github = request.POST['github']
        linkedin = request.POST['linkedin']
        mobile = request.POST['mobile']
        degree = request.POST['degree']
        varsity_name = request.POST['varsity_name']
        passing_year = request.POST['passing_year']
        result = request.POST['result']
        skill_detail = request.POST['skill_detail']
        project_detail = request.POST['project_detail']
        award_detail = request.POST['award_detail']

        user_resume = resume.objects.create(username = request.user.username,first_name = first_name, last_name = last_name,
                        address = address, email = email, github = github, linkedin = linkedin,
                        website = website, mobile = mobile, degree = degree, varsity_name = varsity_name,
                        passing_year = passing_year, result = result, skill_detail = skill_detail,
                        project_detail = project_detail, award_detail = award_detail)
        user_resume.save()
        return redirect('dashboard')
    return render(request, 'resumeGenerator/input.html')

def choose_template(request):
    return render(request, 'resumeGenerator/chooseTemplate.html')
