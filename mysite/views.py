from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt;
import json
from . import models
import smtplib


current_user_count = 0
signed_in_user = ""
logged_in_user = ""

def send_mail(name, mail, access, rid):
     
    sender = 'anubhav8804602148@gmail.com'
    receivers = ['anubhav8804602148@gmail.com']

    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    # try:
    #     smtpObj = smtplib.SMTP('localhost')
    #     smtpObj.sendmail(sender, receivers, message)         
    #     print ("Successfully sent email")
    # except smtplib.SMTPException:
    #     print ("Error: unable to send email")


@csrf_exempt
def login(request):
    logged_in_user = open("logged_in.txt").read().split("\n")
    print("Inside login")
    if request.method=='POST':

        print(len(request.session))
        data = json.loads(request.read())
        userid = data['mail']
        password = data['password']
        print(userid, "trying to login via ", password)
        tuser = models.User.objects.filter(mail=userid)
        if tuser.count() != 1:
            print("Can't login. UserId/login either doen't exist or is multiple")
        else:
            print(tuser.count)
        

    return render(request, 'login.html', context={})


@csrf_exempt
def user_list(request):
    full_data = models.User.objects.all()
    res_list = []
    for user in full_data:
        res_list.append({
            'id' : user.id,
            'name' : user.name,
            'age' : user.age,
            'dob' : user.dob,
            'mail' : user.mail,
        })
    return render(request, 'UserList.html', context={'userList':res_list})

@csrf_exempt
def request_list(request):
    full_data = models.AccRequest.objects.all()
    res_list = []
    for user in full_data:
        res_list.append({
            'id' : user.id,
            'name' : user.name,
            'age' : user.age,
            'dob' : user.dob,
            'mail' : user.mail,
        })
    return render(request, 'requestList.html', context={'requestList':res_list})

def invalid(request):
    return HttpResponse("Invalid Password")


mess = ""
@csrf_exempt
def register(request):
    global mess
    mess = ''
    global current_user_count
    if request.method=='POST':
        data = json.loads(request.read())
        name = data['name']
        mail = data['mail']
        address = data['address']
        dob = data['dob']
        age = data['age']
        rid1 = models.User.objects.filter().order_by('id').last().id
        rid2 = models.AccRequest.objects.filter().order_by('id').last().id
        rid = rid1+1 if rid1 > rid2 else rid2 + 1
        pass1 = data['pass1']
        pass2 = data['pass2']
        access = data['access']
        if pass1==pass2: 
            if access=='on':
                req = models.AccRequest(rid, name, age, dob, mail, address, pass1, access)
                req.save()
                send_mail(name, mail, access, rid)
            else:
                req = models.User(rid, name, age, dob, mail, address, pass1, access)
                req.save()
                send_mail(name, mail, access, rid)
        else:
            mess = "Passwords do not match"
            return redirect('invalid')

    return render(request, 'register.html', context={
        'data':models.User.objects.count,
        'mess' : mess
    })
    
def invalid(request):
    return HttpResponse("Invalid")
