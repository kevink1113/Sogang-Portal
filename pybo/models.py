from django.db import models
import datetime

# Create your models here.


class Student(models.Model):
    student_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=30)
    state = models.IntegerField()
    year = models.IntegerField()
    semester = models.IntegerField()
    major = models.CharField(max_length=100, null=True)
    advisor = models.CharField(max_length=30)
    login_cookie = models.CharField(max_length=50)
    objects = models.Manager()

    @classmethod
    def get_student_by_id(cls, student_id):
        return cls.objects.get(student_id=student_id)

    @classmethod
    def get_login_cookie(cls, student_id):
        return cls.objects.get(student_id=student_id).login_cookie

    def update_student_major(self, new_major):
        self.major = new_major
        self.save()

    def update_student_name(self, new_name):
        self.name = new_name
        self.save()

    def update_student_state(self, new_state):
        self.state = new_state
        self.save()

    def update_student_grade(self, new_year, new_semester):
        self.year = new_year
        self.semester = new_semester
        self.save()

    def update_student_cookie(self, new_cookie):
        self.cookie = new_cookie
        self.save()

    def delete_student(self):
        self.delete()

    @classmethod
    def get_takes(cls, student_id):
        return cls.objects.get(student_id=student_id).takes


class Course(models.Model):
    course_id = models.CharField(max_length=10, null=True)
    semester = models.IntegerField()
    name = models.CharField(max_length=30, null=True)
    day = models.IntegerField()
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    classroom = models.CharField(max_length=15, default='')
    advisor = models.CharField(max_length=30)
    major = models.CharField(max_length=30, null=True)
    objects = models.Manager()

    @classmethod
    def get_course_by_id(cls, course_id, semester):
        return cls.objects.get(course_id=course_id, semester=semester)

    def update_name(self, new_name):
        self.name = new_name
        self.save()

    def update_time(self, new_day, start_hour, start_minute, end_hour, end_minute):
        self.day = new_day
        self.start_time = datetime.time(start_hour, start_minute)
        self.end_time = datetime.time(end_hour, end_minute)
        self.save()

    def update_classroom(self, new_classroom):
        self.classroom = new_classroom
        self.save()

    def delete_course(self):
        self.delete()


class Takes(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='takes')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    middle_grade = models.FloatField(null=True)
    final_grade = models.FloatField(null=True)
    real = models.BooleanField()
    objects = models.Manager()

    def delete_takes(self):
        self.delete()


__all__ = ['Student', 'Course', 'Takes']
