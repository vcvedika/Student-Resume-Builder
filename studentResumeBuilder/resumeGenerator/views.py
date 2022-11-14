from django.shortcuts import redirect, render

# Create your views here.

from django.http import HttpResponse
from django.contrib.sites.requests import RequestSite
from django.contrib.auth import get_user_model
from .models import resume
User = get_user_model()

# Create your views here.

def resume_form(request):
    if resume.objects.filter(username=request.user.username).exists():
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            address = request.POST['address']
            email = request.POST['email']
            github = request.POST['github']
            linkedin = request.POST['linkedin']
            mobile = request.POST['mobile']
            degree = request.POST['degree']
            varsity_name = request.POST['varsity_name']
            passing_year = request.POST['passing_year']
            stream = request.POST['stream']
            school10_name = request.POST['school10_name']
            board10 = request.POST['board10']
            passing_year10 = request.POST['passing_year10']
            result10 = request.POST['result10']

            school12_name = request.POST['school12_name']
            board12 = request.POST['board12']
            passing_year12 = request.POST['passing_year12']
            result12 = request.POST['result12']
            result = request.POST['result']
            skill_detail = request.POST['skill_detail']
            project_detail = request.POST['project_detail']
            achievement_detail = request.POST['achievement_detail']

            user_resume = resume.objects.filter(username=request.user.username)
            user_resume.update(first_name = first_name, last_name = last_name,
                        address = address, email = email, github = github, linkedin = linkedin, mobile = mobile, degree = degree, varsity_name = varsity_name, 
                        stream = stream, passing_year = passing_year, result = result, school10_name = school10_name, board10 = board10, passing_year10 = passing_year10,
                        result10 = result10, school12_name = school12_name, board12 = board12, passing_year12 = passing_year12, result12 = result12,
                        skill_detail = skill_detail, project_detail = project_detail, achievement_detail = achievement_detail)
            return redirect('dashboard')
        else:
            my_resume = resume.objects.filter(username=request.user.username).get()
            context = {
                'first_name': my_resume.first_name,
                'last_name': my_resume.last_name,
                'address': my_resume.address,
                'email': my_resume.email,
                'github': my_resume.github,
                'linkedin': my_resume.linkedin,
                'mobile': my_resume.mobile,

                'degree': my_resume.degree,
                'varsity_name': my_resume.varsity_name,
                'passing_year': my_resume.passing_year,
                'stream': my_resume.stream,
                'result': my_resume.result,

                'school10_name': my_resume.school10_name,
                'school12_name': my_resume.school12_name,
                'board10': my_resume.board10,
                'board12': my_resume.board12,
                'passing_year10': my_resume.passing_year10,
                'passing_year12': my_resume.passing_year12,
                'result10': my_resume.result10,
                'result12': my_resume.result12,


                'skill_detail': my_resume.skill_detail,
                'project_detail': my_resume.project_detail,
                'achievement_detail': my_resume.achievement_detail,
            }

            return render(request, 'resumeGenerator/edit_resume.html', context)

    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        email = request.POST['email']
        github = request.POST['github']
        linkedin = request.POST['linkedin']
        mobile = request.POST['mobile']
        degree = request.POST['degree']
        varsity_name = request.POST['varsity_name']
        passing_year = request.POST['passing_year']
        stream = request.POST['stream']
        school10_name = request.POST['school10_name']
        board10 = request.POST['board10']
        passing_year10 = request.POST['passing_year10']
        result10 = request.POST['result10']

        school12_name = request.POST['school12_name']
        board12 = request.POST['board12']
        passing_year12 = request.POST['passing_year12']
        result12 = request.POST['result12']
        result = request.POST['result']
        skill_detail = request.POST['skill_detail']
        project_detail = request.POST['project_detail']
        achievement_detail = request.POST['achievement_detail']

        user_resume = resume.objects.create(username = request.user.username,first_name = first_name, last_name = last_name,
                        address = address, email = email, github = github, linkedin = linkedin, mobile = mobile, degree = degree, varsity_name = varsity_name, 
                        stream = stream, passing_year = passing_year, result = result, school10_name = school10_name, board10 = board10, passing_year10 = passing_year10,
                        result10 = result10, school12_name = school12_name, board12 = board12, passing_year12 = passing_year12, result12 = result12,
                        skill_detail = skill_detail, project_detail = project_detail, achievement_detail = achievement_detail)
        user_resume.save()
        return redirect('choose-template')
    return render(request, 'resumeGenerator/input.html')


def choose_template(request):
    return render(request, 'resumeGenerator/chooseTemplate.html')


def resume1(request):
    my_resume = resume.objects.filter(username=request.user.username).get()
    my_resume.template_number = 1
    my_resume.save()
    
    return redirect('dashboard')

def resume_view(request):
    if not resume.objects.filter(username=request.user.username).exists():
        return HttpResponse("Please build a resume first !!!!")
    my_resume = resume.objects.filter(username=request.user.username).get()
    context = {
        'first_name': my_resume.first_name,
        'last_name': my_resume.last_name,
        'address': my_resume.address,
        'email': my_resume.email,
        'github': my_resume.github,
        'linkedin': my_resume.linkedin,
        'mobile': my_resume.mobile,

        'degree': my_resume.degree,
        'varsity_name': my_resume.varsity_name,
        'passing_year': my_resume.passing_year,
        'stream': my_resume.stream,
        'result': my_resume.result,

        'school10_name': my_resume.school10_name,
        'school12_name': my_resume.school12_name,
        'board10': my_resume.board10,
        'board12': my_resume.board12,
        'passing_year10': my_resume.passing_year10,
        'passing_year12': my_resume.passing_year12,
        'result10': my_resume.result10,
        'result12': my_resume.result12,

        'skill_detail': my_resume.skill_detail,
        'project_detail': my_resume.project_detail,
        'achievement_detail': my_resume.achievement_detail,
    }
    if my_resume.template_number == 1:
        return render(request,'resumeGenerator/resume1.html', context)
    if my_resume.template_number == 2:
        return render(request,'resumeGenerator/resume2.html', context)
    return render(request,'resumeGenerator/resume3.html', context)

def resume2(request):
    my_resume = resume.objects.filter(username=request.user.username).get()
    my_resume.template_number = 2
    my_resume.save()
    
    return redirect('dashboard')

def resume3(request):
    my_resume = resume.objects.filter(username=request.user.username).get()
    my_resume.template_number = 3
    my_resume.save()
    
    return redirect('dashboard')

def switch_template(request):
    if not resume.objects.filter(username=request.user.username).exists():
        return HttpResponse("Please build a resume first !!!!")
    else:
        return redirect('choose-template')
    
