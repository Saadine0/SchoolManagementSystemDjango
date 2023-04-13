"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE, name='base'),


    #homepage
    path('', views.HOMES , name='homes'),
    path('Contact', views.CONTACT , name='contact'),
    path('About', views.ABOUT , name='about'),
    path('Vehicle', views.VEHICLE , name='vehicle'),
    path('Teacher', views.TEACHER , name='teacher'),

    #login path
    path('home/login', views.LOGIN , name='login'),
    path('doLogin', views.doLogin , name='doLogin'),
    path('doLogout', views.doLogout , name='Logout'),


    #profile update
    path('profile', views.PROFILE , name='profile'),
    path('profile/Update', views.PROFILE_UPDATE , name='profile_update'),


    #this is Hod panel URL
    path('HOD/Home',Hod_Views.HOME, name="hod_home"),
    path('HOD/Student/Add',Hod_Views.ADD_STUDENT, name="add_student"),
    path('HOD/Student/View',Hod_Views.VIEW_STUDENT, name="view_student"),
    path('HOD/Student/Edit/<str:id>',Hod_Views.EDIT_STUDENT, name="edit_student"),
    path('HOD/Student/Update',Hod_Views.UPDATE_STUDENT, name="update_student"),
    path('HOD/Student/Delete/<str:admin>',Hod_Views.DELETE_STUDENT, name="delete_student"),


    path('HOD/Teacher/Add',Hod_Views.ADD_STAFF, name="add_staff"),
    path('HOD/Teacher/View',Hod_Views.VIEW_STAFF, name="view_staff"),
    path('HOD/Teacher/Edit/<str:id>',Hod_Views.EDIT_STAFF, name="edit_staff"),
    path('HOD/Teacher/Update',Hod_Views.UPDATE_STAFF, name="update_staff"),
    path('HOD/Teacher/Delete/<str:admin>',Hod_Views.DELETE_STAFF, name="delete_staff"),


    path('HOD/Course/Add',Hod_Views.ADD_COURSE, name="add_course"),
    path('HOD/Course/View',Hod_Views.VIEW_COURSE, name="view_course"),
    path('HOD/Course/Edit/<str:id>',Hod_Views.EDIT_COURSE, name="edit_course"),
    path('HOD/Course/Update',Hod_Views.UPDATE_COURSE, name="update_course"),
    path('HOD/Course/Delete/<str:id>',Hod_Views.DELETE_COURSE, name="delete_course"),

    path('HOD/Subject/Add',Hod_Views.ADD_SUBJECT, name="add_subject"),
    path('HOD/Subject/View',Hod_Views.VIEW_SUBJECT, name="view_subject"),
    path('HOD/Subject/Edit/<str:id>',Hod_Views.EDIT_SUBJECT, name="edit_subject"),
    path('HOD/Subject/Update',Hod_Views.UPDATE_SUBJECT, name="update_subject"),
    path('HOD/Subject/Delete/<str:id>',Hod_Views.DELETE_SUBJECT, name="delete_subject"),


    path('HOD/Session/Add',Hod_Views.ADD_SESSION, name="add_session"),
    path('HOD/Session/View',Hod_Views.VIEW_SESSION, name="view_session"),
    path('HOD/Session/Edit/<str:id>',Hod_Views.EDIT_SESSION, name="edit_session"),
    path('HOD/Session/Update',Hod_Views.UPDATE_SESSION, name="update_session"),
    path('HOD/Session/Delete/<str:id>',Hod_Views.DELETE_SESSION, name="delete_session"),


    path('HOD/Teacher/Send_Notification',Hod_Views.STAFF_SEND_NOTIFICATION, name="staff_send_notification"),
    path('HOD/Teacher/Save_Notification',Hod_Views.SAVE_STAFF_NOTIFICATION, name="save_staff_notification"),


    path('HOD/Teacher/Feedback',Hod_Views.HOD_STAFF_FEEDBACK, name="hod_staff_feedback"),
    path('HOD/Teacher/Feedback/Save',Hod_Views.HOD_STAFF_FEEDBACK_SAVE, name="hod_staff_feedback_save"),


    path('HOD/event',Hod_Views.EVENT, name="event"),
    path('HOD/add_event',Hod_Views.ADDEVENT, name="addevent"),

    path('HOD/Student/Send_Notification',Hod_Views.STUDENT_SEND_NOTIFICATION, name="student_send_notification"),
    path('HOD/Student/Save_Notification',Hod_Views.STUDENT_SAVE_NOTIFICATION, name="student_save_notification"),


    path('HOD/Student/Feedback',Hod_Views.HOD_STUDENT_FEEDBACK, name="hod_student_feedback"),
    path('HOD/Student/Feedback/Save',Hod_Views.HOD_STUDENT_FEEDBACK_SAVE, name="hod_student_feedback_save"),

# -------------------------  this is staff URLS -----------------------

    path('Teacher/Home',Staff_Views.HOME , name='staff_home'),
    

    path('Teacher/Notifications',Staff_Views.NOTIFICATIONS, name="notifications"),
    path('Teacher/Mark_As_Done/<str:status>',Staff_Views.STAFF_NOTIFICATION_MARK_AS_DONE, name="staf_notification_mark_as_done"),

    path('Teacher/View_Course',Staff_Views.STAFF_VIEW_COURSE, name="staff_view_course"),
    path('Teacher/<int:subject_id>/course',Staff_Views.courses_by_subject, name="staff_view_subject"),

    path('Teacher/Feedback',Staff_Views.STAFF_FEEDBACK, name="staff_feedback"),
    path('Teacher/Feedback/Save',Staff_Views.STAFF_FEEDBACK_SAVE, name="staff_feedback_save"),
    

    path('Teacher/Add/Result',Staff_Views.TEACHER_ADD_RESULT, name="staff_add_result"),
    path('Teacher/Save/Result',Staff_Views.TEACHER_SAVE_RESULT, name="staff_save_result"),

#----------------------Student URL----------------------------------------

    path('Student/Home',Student_Views.HOME_STUDENT, name="student_home"),

    path('Student/Notifications',Student_Views.STUDENT_NOTIFICATIONS, name="student_notifications"),
    path('Student/Mark_As_Done/<str:status>',Student_Views.STUDENT_NOTIFICATION_MARK_AS_DONE, name="student_notification_mark_as_done"),

    path('Student/Feedback',Student_Views.STUDENT_FEEDBACK, name="student_feedback"),
    path('Student/Feedback/Save',Student_Views.STUDENT_FEEDBACK_SAVE, name="student_feedback_save"),
   
    path('Student/View_Subject',Student_Views.STUDENT_VIEW_SUBJECT, name="student_view_subject"),
    path('Student/<int:subject_id>/course',Student_Views.STUDENT_VIEW_COURSE, name="student_view_course"),

    
    path('Student/view_Result',Student_Views.VIEW_RESULT, name="view_result"),



] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
