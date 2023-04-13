from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    USER = (
        ('1','HOD'),
        ('2','STAFF'),
        ('3','STUDENT'),
    )


    user_type = models.CharField(choices=USER,max_length=50,default=1 )
    profile_pic = models.ImageField(upload_to = 'media/profile_pic')

    def _str_(self):
        return self.name

class Classe(models.Model):
    CLASS_CHOICES = [
        ('CP1', 'CP1'),
        ('CP2', 'CP2'),
        ('CE1', 'CE1'),
        ('CE2', 'CE2'),
        ('CM1', 'CM1'),
        ('CM2', 'CM2'),
    ]
    class_name = models.CharField(max_length=3, choices=CLASS_CHOICES)
    def __str__(self):
        return self.class_name

class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
        return self.session_start + " To " + self.session_end

class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    classe_id = models.ForeignKey(Classe,on_delete=models.CASCADE)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=10)
    admission_number = models.CharField(max_length=20, unique=True)
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    cin = models.CharField(max_length=20)
    father_mobile = models.CharField(max_length=10)
    mother_mobile = models.CharField(max_length=10)
    permanent_address = models.CharField(max_length=200)
    present_address = models.CharField(max_length=200)

    def __str__(self):
        return self.admin.first_name
    

class Teacher(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher_id = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=10)
    join_date = models.DateField()
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.admin.username
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    classe_id = models.ForeignKey(Classe,on_delete=models.CASCADE)
    staff = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True , null=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.CharField( max_length=200)

    def __str__(self):
        return self.subject_name
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.CharField( max_length=400)

    def __str__(self):
        return self.name

    
class Staff_Notification(models.Model):
     staff_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
     message = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True , null=True)
     status = models.IntegerField(null=True,default=0)

     def __str__(self):
         return self.staff_id.admin.first_name
     

class Staff_leave(models.Model):
    staff_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    data = models.CharField(max_length=108)
    message   = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True , null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name
    
class Staff_Feedback(models.Model):
    staff_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True , null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.staff_id.admin.first_name+ " "+ self.staff_id.admin.last_name


class Student_Notification(models.Model):
     student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
     message = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True , null=True)
     status = models.IntegerField(null=True,default=0)

     def __str__(self):
         return self.student_id.admin.first_name
     

class Student_Feedback(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True , null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name+ " "+ self.student_id.admin.last_name
    

class StudentResult(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    exam_mark = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True , null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name




    
    
