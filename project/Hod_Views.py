from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Course, Session_Year ,CustomUser, Student, Teacher, Subject,Staff_Notification, Staff_Feedback, Student_Notification, Student_Feedback,Classe
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Teacher.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()

    student_gender_female = Student.objects.filter(gender = 'F').count() 
    studnet_gender_male = Student.objects.filter(gender = 'M').count()
    context = {
        'student_count' : student_count,
        'staff_count' : staff_count,
        'course_count' : course_count,
        'subject_count' : subject_count,
        'student_gender_female' : student_gender_female,
        'studnet_gender_male' : studnet_gender_male


    }
    return render(request, 'Hod/home.html',context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    session_year = Session_Year.objects.all()
    classe = Classe.objects.all()
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        student_k = request.POST.get('student_k')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        class__id = request.POST.get('class_id')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        profile_pic = request.FILES.get('profile_pic')
 #       course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        cin = request.POST.get('cin')
        father_mobile = request.POST.get('father_mobile')
        mother_mobile = request.POST.get('mother_mobile')
        permanent_address = request.POST.get('permanent_address')
        present_address = request.POST.get('present_address')

 
        if CustomUser.objects.filter(email = email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_student')
        
        if CustomUser.objects.filter(username = username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username= username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3    
            )
            user.set_password(password)
            user.save()

     #       course = Course.objects.get(id = course_id )
            session_year = Session_Year.objects.get(id = session_year_id)
            classe = Classe.objects.get(id = class__id)

            student = Student(
                admin = user,
         #       course_id = course,
                session_year_id = session_year,
                student_id = student_k,
                gender = gender,
                date_of_birth = date_of_birth,
                classe_id = classe,
                joining_date = joining_date,
                mobile_number = mobile_number,
                admission_number = admission_number,
                father_name = father_name,
                mother_name = mother_name,
                cin = cin,
                father_mobile = father_mobile,
                mother_mobile =  mother_mobile,
                permanent_address = permanent_address,
                present_address = present_address,
            )

            student.save()
            messages.success(request, user.first_name +" " + user.last_name + 'Are Successfuly Added')
            return redirect('view_student')
    context  = {
      #  'course' :course,
        'session_year' : session_year,
        'classe' : classe

        }
    return render(request, 'Hod/add_student.html', context) 


@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()
    context = {
        'student' : student
    }
    return render(request, 'Hod/view_student.html',context)

@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student =Student.objects.filter(id =id)
    session_year = Session_Year.objects.all()
    classe = Classe.objects.all()
    context = {
        'student' : student,
        'session_year' : session_year,
        'classe' : classe
    }
    return render(request, 'Hod/edit_student.html',context)
    
@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        student_k = request.POST.get('student_k')
        gender = request.POST.get('gender')
        class_id = request.POST.get('class_id')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        profile_pic = request.FILES.get('profile_pic')
        session_year_id = request.POST.get('session_year_id')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        cin = request.POST.get('cin')
        father_mobile = request.POST.get('father_mobile')
        mother_mobile = request.POST.get('mother_mobile')
        permanent_address = request.POST.get('permanent_address')
        present_address = request.POST.get('present_address')

        user = CustomUser.objects.get(id = id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if password is not None and password != "":
                user.set_password(password)
                
        if profile_pic is not None and profile_pic != "":
                user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin = id)
        student.student_id = student_k
        student.gender = gender
        student.class_id = class_id
        student.mobile_number = mobile_number
        student.admission_number = admission_number
        student.father_name = father_name
        student.mother_name = mother_name
        student.cin = cin
        student.father_mobile = father_mobile
        student.mother_mobile =  mother_mobile
        student.permanent_address = permanent_address
        student.present_address = present_address 
        


        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request, 'Student updated successfully.')
        return redirect('view_student')
        
    return render(request, 'Hod/edit_student.html') 

@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id= admin)
    student.delete()
    messages.success(request, 'Record Are Successfully Delete')
    return redirect('view_student')

#------------------------------course-------------------------------------------------
@login_required(login_url='/')
def ADD_COURSE(request):
    subject = Subject.objects.all()
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        subject_id = request.POST.get('subject_id')
        link = request.POST.get('link')
        subject = Subject.objects.get(id = subject_id )
        course = Course(
             name = course_name,
             subject = subject,
             link = link
        ) 
        course.save()
        messages.success(request, 'Course Are Successfully Sreated')
        return redirect('view_course')
    context = {
        'subject' : subject
    }
    return render(request, 'Hod/add_course.html',context)

@login_required(login_url='/')
def VIEW_COURSE(request):
    course = Course.objects.all()

    context = {
         'course' : course,
    }
    return render(request, 'Hod/view_course.html',context)

@login_required(login_url='/')
def EDIT_COURSE(request,id):
    course = Course.objects.get(id = id)
    subject = Subject.objects.all()
    context = {
         'course' : course,
         'subject' : subject
    }
    return render(request, 'Hod/edit_course.html',context)

@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method  == "POST":
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id = course_id)
        course.name = name
        course.save()
        messages.success(request, 'Course Are Successfully Updated !')
        return redirect('view_course')
    return render(request, 'Hod/edit_course.html')

@login_required(login_url='/')
def DELETE_COURSE(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request, 'Course Are Successfully Deleted !')
    return redirect('view_course')


#-----------------------Tecaher-----------------------------
@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == "POST":
        teacher_id = request.POST.get('teacher_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        mobile = request.POST.get('mobile')
        join_date = request.POST.get('join_date')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code  = request.POST.get('zip_code')
        country  = request.POST.get('country')

        if CustomUser.objects.filter(email = email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_staff')
        
        if CustomUser.objects.filter(username = username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username= username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2 
            )
            user.set_password(password)
            user.save()
            staff = Teacher(
                admin = user,
                teacher_id = teacher_id,
                gender = gender,
                date_of_birth = date_of_birth,
                mobile = mobile,
                join_date = join_date,
                qualification = qualification,
                experience = experience,
                address = address,
                city = city,
                zip_code = zip_code,
                country = country,
                  )
            staff.save()
            messages.success(request, user.first_name + " " + user.last_name + ' Are Successfuly Added')
            redirect('view_staff')
            
    return render(request, 'Hod/add_staff.html')

@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Teacher.objects.all()
    context = {
        'staff' : staff
    }
    return render(request,'Hod/view_staff.html',context)

@login_required(login_url='/')
def EDIT_STAFF(request,id):
    staff = Teacher.objects.get(id = id)
    context = {
        'staff' : staff,
    }
    return render(request,'Hod/edit_staff.html',context)

@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        teacher_id = request.POST.get('teacher_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
#        date_of_birth = request.POST.get('date_of_birth')
        mobile = request.POST.get('mobile')
 #       join_date = request.POST.get('join_date')
        qualification = request.POST.get('qualification')
        experience = request.POST.get('experience')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code  = request.POST.get('zip_code')
        country  = request.POST.get('country')

        user = CustomUser.objects.get(id= staff_id)
        user.first_name = first_name
        user.  last_name = last_name
        user.  username= username
        user.  email = email
        if password is not None and password != "":
                user.set_password(password)
                
        if profile_pic is not None and profile_pic != "":
                user.profile_pic = profile_pic
        user.save()

        staff = Teacher.objects.get(admin = staff_id)
        staff.address = address
        staff.city = city
        staff.gender = gender
        staff.country = country
        staff.experience = experience
        staff.qualification = qualification
        staff.mobile = mobile
        staff.zip_code = zip_code
        staff.teacher_id = teacher_id
        staff.save()
        messages.success(request, 'Staff Is Successfully Updated !')
        return redirect('view_staff')

    return render(request, 'Hod/edit_staff.html')

@login_required(login_url='/')
def DELETE_STAFF(request,admin):
     staff = CustomUser.objects.get(id= admin)
     staff.delete()
     messages.success(request, 'Record Are Successfully Deleted !')
     return redirect('view_staff')


#----------------------------Subject----------------------------------------
@login_required(login_url='/')
def ADD_SUBJECT(request):
    staff = Teacher.objects.all()
    classe = Classe.objects.all()
    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        class_id = request.POST.get('class_id')
        staff_id = request.POST.get('staff_id')
        link = request.POST.get('link')
        classe  = Classe.objects.get(id = class_id)
        staff = Teacher.objects.get(id = staff_id )
        
        subject = Subject(
             subject_name = subject_name,
             classe_id = classe,
             staff = staff,
             link = link

         )    
        subject.save()
        messages.success(request, 'Subject Are Successfully Added !')       
        return redirect('view_subject')

    context = {
        'classe':classe,
        'staff' : staff
     }
    return render(request,'Hod/add_subject.html',context)

@login_required(login_url='/')
def VIEW_SUBJECT(request):
     subject = Subject.objects.all()
     context = {
          'subject':subject
     }
     return render(request, 'Hod/view_subject.html',context)

@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id = id)
    classe = Classe.objects.all()
    staff = Teacher.objects.all()
    context = {
      'subject' : subject,
      'classe' : classe,
      'staff' : staff
    }
    return render(request, 'Hod/edit_subject.html',context)

@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        classe_id = request.POST.get('class_id')
        staff_id = request.POST.get('staff_id')
        link = request.POST.get('link')
        subject_name = request.POST.get('subject_name')

        classe = Classe.objects.get(id = classe_id)
        staff = Teacher.objects.get(id = staff_id)
        subject = Subject(
            id = subject_id,
            subject_name = subject_name,
            classe_id = classe,
            staff = staff,
            link = link
        )
        subject.save()
        messages.success(request, 'Subject Are Successfully Updated !')
        return redirect('view_subject')
    return render(request, 'Hod/edit_subject.html')

@login_required(login_url='/')
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.filter(id = id)
    subject.delete()
    messages.success(request, 'Subject Are Successfully Deleted !')
    return redirect('view_subject')

#--------------------------Session------------------------------------

@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        session = Session_Year(
        session_start = session_year_start,
        session_end = session_year_end,
        )
        session.save()
        messages.success(request, 'Session Are Successfully Added !')
        return redirect('view_session')
    return render(request, 'Hod/add_session.html')

@login_required(login_url='/')
def VIEW_SESSION(request):
    session = Session_Year.objects.all()
    context = {
        'session' : session
    }
    return render(request,'Hod/view_session.html',context)

@login_required(login_url='/')
def EDIT_SESSION(request,id):
    session = Session_Year.objects.filter(id = id)
    context = {
        'session' : session,
    }
    return render(request,'Hod/edit_session.html',context)


@login_required(login_url='/')
def UPDATE_SESSION(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            id = session_id,
            session_start = session_year_start,
            session_end = session_year_end

        )
        session.save()
        messages.success(request,'Session Are Successfully Updated ! ')
        return redirect('view_session')
    return render(request, 'Hod/edit_session.html')


@login_required(login_url='/')
def DELETE_SESSION(request,id):
    session = Session_Year.objects.filter(id = id)
    session.delete()
    messages.success(request, 'Session Are Successfully Deleted !')
    return redirect('view_session')
    

#--------------------------------NOtification-------------------
@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff = Teacher.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'staff' : staff,
        'see_notification' : see_notification
    }
    return render(request, 'Hod/staff_notification.html',context)


@login_required(login_url='/')
def SAVE_STAFF_NOTIFICATION(request):
    if request.method == "POST":
        staff_id  = request.POST.get('staff_id')
        message  = request.POST.get('message')

        staff = Teacher.objects.get(admin = staff_id)
        notification = Staff_Notification(
            staff_id = staff,
            message = message,
        )
        notification.save()
        messages.success(request, 'Notificaton Are Successfully Send !')
        return redirect('staff_send_notification')

#---------------------------------event ---------------------------------------------------


@login_required(login_url='/')
def EVENT(request):
    return render(request, 'Hod/event.html')

@login_required(login_url='/')
def ADDEVENT(request):
     return render(request, 'Hod/add_event.html')     


def HOD_STAFF_FEEDBACK(request):
    feedback = Staff_Feedback.objects.all()
    feedback_history = Staff_Feedback.objects.all()
    context = {
        'feedback' : feedback,
        'feedback_history' : feedback_history
    }
    
    return render(request, 'Hod/staff_feedback.html',context)

def HOD_STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()

        return redirect('hod_staff_feedback')
    

def STUDENT_SEND_NOTIFICATION(request):
    student = Student.objects.all()
    notification = Student_Notification.objects.all()

    context = {
        'student' : student,
        'notification' : notification
    }
    return render(request, 'Hod/student_notification.html', context)

def STUDENT_SAVE_NOTIFICATION(request):
    if request.method == "POST":
        message = request.POST.get('message')
        student_id = request.POST.get('student_id')

        student = Student.objects.get(admin = student_id)
        student_notification = Student_Notification(
            student_id = student,
            message = message,
        )
        student_notification.save()
        messages.success(request, 'Student Notification Are Successfully Send !')

        return redirect('student_send_notification')
    

def HOD_STUDENT_FEEDBACK(request):

    feedback = Student_Feedback.objects.all()
    feedback_history = Student_Feedback.objects.all()


    context = {
        'feedback' : feedback,
         'feedback_history' : feedback_history
    }
    return render(request, 'Hod/student_feedback.html',context)

def HOD_STUDENT_FEEDBACK_SAVE(request):
    if request.method =="POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Student_Feedback.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.status = 1
        feedback.save()
        return redirect('hod_student_feedback')
    return None