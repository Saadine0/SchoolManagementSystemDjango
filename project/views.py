from django.shortcuts import render, redirect,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

def HOMES(request):
    return render(request, 'index.html')

def CONTACT(request):
    return render(request, 'contact.html')

def TEACHER(request):
    return render(request, 'teacher.html')

def ABOUT(request):
    return render(request, 'about.html')  

def VEHICLE(request):
    return render(request, 'vehicle.html') 
      
def BASE(request):
    return render(request, 'base.html')

def LOGIN(request):
    return render(request, 'login.html') 

def doLogin(request):
    if request.method == "POST":
        user = EmailBackEnd.authenticate(request,
                                        username=request.POST.get('email'),
                                        password = request.POST.get('password'),)
        if user is not None:
           login(request,user)
           user_type = user.user_type
           if user_type == '1':
               return redirect('hod_home')
           elif user_type == '2':
               return redirect('staff_home')
           elif user_type == '3':
              return redirect('student_home')
           else:
            messages.error(request, 'Email or Password are invalid !')
            return redirect('login')
        
        else:
           messages.error(request, 'Email or Password are invalid !')
           return redirect('login') 


def doLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        "user":user,
    }
    return render(request, 'profile.html',context )


@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('first_name')
        password = request.POST.get('password')
        
        try:
            customuser = CustomUser.objects.get(id = request.user.id)

            customuser.first_name = first_name
            customuser.last_name = last_name
            
            if password is not None and password != "":
                customuser.set_password(password)
                
            if profile_pic is not None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, 'Your Profile Updated Successfully !')
            return redirect('profile')

        except:
            messages.error('failed To Update Your profile')

    return render(request, 'profile.html')



