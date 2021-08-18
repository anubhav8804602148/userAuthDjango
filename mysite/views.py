from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt;
import json
from . import models

current_user_count = 0
signed_in_user = ""


@csrf_exempt
def login(request):
    print("Inside login")
    if request.method=='POST':
        print("inside post")
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


@csrf_exempt
def register(request):
    global current_user_count
    if request.method=='POST':
        data = json.loads(request.read())
        name = data['name']
        mail = data['mail']
        address = data['address']
        dob = data['dob']
        age = data['age']
        trid =  models.AccRequest.objects.all()
        rid = 0
        try:
            rid = trid.order_by("id")[0].id + 1
        except:
            pass
        pass1 = data['pass1']
        pass2 = data['pass2']
        access = data['access']
        if pass1==pass2: 
            if access=='on':
                req = models.AccRequest(rid, name, age, dob, mail, address, pass1, access)
                req.save()
            else:
                req = models.User(rid, name, age, dob, mail, address, pass1, access)
                req.save()
        else:
            print("Invalid")
            return render(request, 'invalid.html')
        
    return render(request, 'register.html', context={'data':current_user_count})