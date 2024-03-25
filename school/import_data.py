import csv
import pandas as pd

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


def import_data_from_csv(file_path):
    df = pd.read_csv(file_path, delimiter=",")
    print(df.values)
    listOf_csv = [row for row in df.to_dict(orient="records")]

    for row in listOf_csv:
        School.objects.get_or_create(name=row["school_name"])
        Class.objects.get_or_create(class_name=row["Class"])
        AssessmentAreas.objects.get_or_create(name=row["Assessment Areas"])

        Student.objects.get_or_create(
            fullname=[f"{row['First Name']} {row['Last Name']}"]
        )
        Answer.objects.get_or_create(answer_text=row["Answers"])
        Awards.objects.get_or_create(name=row["award"])
        Subject.objects.get_or_create(
            subject_name=row["Subject"], subject_score=row["student_score"]
        )
        Summary.objects.get_or_create(
            School_Id=row["StudentID"],
            Sydney_Participant=row["sydney_participants"],
            Syndey_Percentile=row["Syndey_Percentile"],
            Assesment_Area_Id=row["Assesment_Area_Id"],
            Award_Id=row["Award_Id"],
            Class_ID=row["Class_ID"],
            Corret_anbswer_percentage_per_calss=row[
                "correct_answer_percentage_per_class"
            ],
            Correct_Answer=row["Correct_Answer"],
            Student_Id=row["Student_Id"],
            Particippant=row["Particippant"],
            Student_score=row["Student_score"],
            Subject_Id=row["Subject_Id"],
            Category_Id=row["Category_Id"],
            Year_level_name=row["Year Level"],
            Answer_Id=row["Answers"],
            Correct_answer_id=row["Correct Answers"],
        )
