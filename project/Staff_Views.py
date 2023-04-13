from django.shortcuts import render, redirect
from app.models import Course, Session_Year ,CustomUser, Student, Teacher, Subject,Staff_Notification, Staff_Feedback, Student_Notification, Student_Feedback,Classe,StudentResult
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Staff/home.html')

@login_required(login_url='/')
def NOTIFICATIONS(request):
    staff = Teacher.objects.filter(admin=request.user.id)
    context = {}
    for i in staff:
        staff_id = i.id
        notification = Staff_Notification.objects.filter(staff_id=staff_id)
        context['notification'] = notification
    return render(request, 'Staff/notification.html', context)

@login_required(login_url='/')
def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notifications')   





@login_required(login_url='/')
def STAFF_VIEW_COURSE(request):

    staff = Teacher.objects.filter(admin=request.user.id)
    context = {}
    for i in staff:
            subject_id = i.id
            subject = Subject.objects.filter(staff = subject_id)
            context['notification'] = subject

    return render(request  , 'Staff/view_course.html',context)



@login_required(login_url='/')
def courses_by_subject(request, subject_id):
    # Récupérer le sujet pour lequel nous voulons afficher les cours
    subject = Subject.objects.get(pk=subject_id)
    # Récupérer tous les cours associés à ce sujet
    courses = Course.objects.filter(subject=subject)
    # Passer les cours et le sujet à notre template
    return render(request, 'Staff/view_subject.html', {'courses': courses, 'subject': subject})

@login_required(login_url='/')
def STAFF_FEEDBACK(request):
     staff_id = Teacher.objects.get(admin = request.user.id)

     feedback_history = Staff_Feedback.objects.filter(staff_id = staff_id)

     context = {
          'feedback_history' : feedback_history
     }
     return render(request, 'Staff/feedback.html',context)


@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
     if request.method == "POST":
            feedback = request.POST.get('feedback')
            
            staff = Teacher.objects.get(admin = request.user.id)
            feedback = Staff_Feedback(
                staff_id = staff,
                feedback = feedback,
                feedback_reply = "",
                
            )
            feedback.save()
            return redirect('staff_feedback')
     
def TEACHER_ADD_RESULT(request):
    teacher = Teacher.objects.get(admin = request.user.id)

    subjects = Subject.objects.filter(staff = teacher)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
           subject_id = request.POST.get('subject_id')
           session_year_id = request.POST.get('session_year_id')

           get_subject = Subject.objects.get(id = subject_id)
           get_session = Session_Year.objects.get(id = session_year_id)

           subjects = Subject.objects.filter(id = subject_id)
           for i in subjects:
               student_id = i.classe_id.id
               students = Student.objects.filter(classe_id = student_id)


    context = {
        'subjects':subjects,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,
    }

    return render(request,'Staff/add_result.html',context)

def TEACHER_SAVE_RESULT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        exam_mark = request.POST.get('Exam_mark')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exist = StudentResult.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        if check_exist:
            result = StudentResult.objects.get(subject_id=get_subject, student_id=get_student)
            result.subject_exam_marks = exam_mark
            result.save()
            messages.success(request, "Successfully Updated Result")
            return redirect('staff_add_result')
        else:
            result = StudentResult(student_id=get_student, subject_id=get_subject, exam_mark=exam_mark)
            result.save()
            messages.success(request, "Successfully Added Result")
            return redirect('staff_add_result')
