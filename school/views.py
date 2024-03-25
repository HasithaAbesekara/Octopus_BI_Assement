from django.shortcuts import render

from .import_data import import_data_from_csv
from django.http import HttpResponseRedirect
from .models import (
    School,
    Class,
    AssessmentAreas,
    Student,
    Answer,
    Awards,
    Subject,
    Summary,
)


def import_csv_view(request):
    if request.method == "POST" and request.FILES.get("csv_file"):
        csv_file = request.FILES["csv_file"]

        import_data_from_csv(csv_file)
        return HttpResponseRedirect("/display-data")
    return render(request, "import_csv.html")


def display_data_view(request):
    schools = School.objects.all()
    classes = Class.objects.all()
    assessment_areas = AssessmentAreas.objects.all()
    students = Student.objects.all()
    answers = Answer.objects.all()
    awards = Awards.objects.all()
    subjects = Subject.objects.all()
    summary = Summary.objects.all()
    return render(
        request,
        "display_data.html",
        {
            "schools": schools,
            "classes": classes,
            "assessment_areas": assessment_areas,
            "students": students,
            "answers": answers,
            "awards": awards,
            "subjects": subjects,
            "summary": summary,
        },
    )
