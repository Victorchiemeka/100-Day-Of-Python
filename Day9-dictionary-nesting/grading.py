student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for students in student_scores:
    if student_scores[students] >= 91 and student_scores[students] <= 100:
        student_grades[students] = "Outstanding"
    elif student_scores[students] >= 81 and student_scores[students] <= 90:
        student_grades[students] = "Exceed Expectations"
    elif student_scores[students] >= 71 and student_scores[students] <= 80:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fail"

print(student_grades)
