from django.shortcuts import redirect, render
import razorpay


# Create your views here.

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from .models import resume
from django.conf import settings
User = get_user_model()

# Create your views here.

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

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
    currency = 'INR'
    amount = 50000

    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request, 'resumeGenerator/chooseTemplate.html', context)

def resume1(request):
    my_resume = resume.objects.filter(username=request.user.username).get()
    my_resume.template_number = 1
    my_resume.save()

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

    if request.method == 'GET':
        return render(request,'resumeGenerator/resume1.html', context)
    
    return render(request, 'resumeGenerator/resume1.html')

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
        context = {'message': "Please build your resume first!!"}
        return render(request, 'dashboard/dashboard.html', context)
    else:
        return redirect('choose-template')

def resume_view(request):
    if not resume.objects.filter(username=request.user.username).exists():
        context = {'message': "Please build your resume first!!"}
        return render(request, 'dashboard/dashboard.html', context)
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

@csrf_exempt

def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 50000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    context = {'message': "Congratulations! Your payment is successful."}
                    return render(request, 'dashboard/dashboard.html', context)
                except:
 
                    # if there is an error while capturing payment.
                    context = {'message': "Payment unsuccessful! Please try again."}
                    return render(request, 'dashboard/dashboard.html', context)
            else:
 
                # if signature verification fails.
                context = {'message': "Payment unsuccessful! Please try again."}
                return render(request, 'dashboard/dashboard.html', context)
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
