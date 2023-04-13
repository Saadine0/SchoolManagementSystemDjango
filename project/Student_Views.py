from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Student_Notification,Student, Student_Feedback,Classe,Course,Subject,StudentResult

@login_required(login_url='/')
def HOME_STUDENT(request):
    return render(request, 'Student/home_student.html')

@login_required(login_url='/')
def STUDENT_NOTIFICATIONS(request):
    student  = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id = student_id)

        context = {
            'notification' : notification
        }

    return render(request, 'Student/notification.html',context)

@login_required(login_url='/')
def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('student_notifications')


def STUDENT_FEEDBACK(request):
    student_id = Student.objects.get(admin = request.user.id)
    feedback_reply  = Student_Feedback.objects.filter(student_id = student_id)

    context = {
        'feedback_history' : feedback_reply,
    }
    return render(request , 'Student/feedback.html',context)


def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin = request.user.id)
        feedback = Student_Feedback(
            student_id = student,
            feedback = feedback,
            feedback_reply = "",
        )
        feedback.save()

        return redirect('student_feedback')
    
@login_required(login_url='/')
def STUDENT_VIEW_SUBJECT(request):
        student = Student.objects.get(admin=request.user.id)
        classe_id = student.classe_id
        subjects = Subject.objects.filter(classe_id=classe_id)
        context = {'subjects': subjects}
        return render(request, 'Student/view_subject.html', context)



@login_required(login_url='/')
def STUDENT_VIEW_COURSE(request, subject_id):
    # Récupérer le sujet pour lequel nous voulons afficher les cours
    subject = Subject.objects.get(pk=subject_id)
    # Récupérer tous les cours associés à ce sujet
    courses = Course.objects.filter(subject=subject)
    # Passer les cours et le sujet à notre template
    return render(request, 'Student/view_course.html', {'courses': courses, 'subject': subject})





def VIEW_RESULT(request):
    student = Student.objects.get(admin = request.user.id)
    result = StudentResult.objects.filter(student_id=student)
    context = {
        'result':result,
    }
    return render(request,'Student/view_result.html',context)
