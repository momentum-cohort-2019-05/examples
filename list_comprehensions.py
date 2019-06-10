def to_letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


scores = [74, 81, 62, 93, 87]
grades = []

# This is equivalent to the list comprehension below.
for score in scores:
    if score >= 60:
        grade = to_letter_grade(score)
        grades.append(grade)

# This is equivalent to the for loop above.
grades = [to_letter_grade(score) for score in scores if score >= 60]
