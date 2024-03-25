from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)


class Class(models.Model):
    class_name = models.CharField(max_length=100)


class AssessmentAreas(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    fullname = models.CharField(max_length=100)


class Answer(models.Model):
    answer_text = models.CharField(max_length=100)


class Awards(models.Model):
    name = models.CharField(max_length=100)


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_score = models.IntegerField()


class Summary(models.Model):
    School_Id = models.IntegerField()
    Sydney_Participant = models.IntegerField()
    Syndey_Percentile = models.IntegerField()
    Assesment_Area_Id = models.IntegerField()
    Award_Id = models.IntegerField()
    Class_ID = models.IntegerField()
    Corret_anbswer_percentage_per_calss = models.IntegerField()
    Correct_Answer = models.IntegerField()
    Student_Id = models.IntegerField()
    Particippant = models.IntegerField()
    Student_score = models.IntegerField()
    Subject_Id = models.IntegerField()
    Category_Id = models.IntegerField()
    Year_level_name = models.IntegerField()
    Answer_Id = models.IntegerField()
    Correct_answer_id = models.IntegerField()
