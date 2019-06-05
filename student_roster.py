student_roster = {
    'Jordan': {
        'Homework 1': 92,
        'Homework 2': 87
    },
    'Gale': {
        'Homework 1': 88,
        'Homework 2': 76
    },
    'River': {
        'Homework 1': 85,
        'Homework 2': 91
    }
}


def get_scores(roster, assignment):
    scores = {}
    for student, grades in roster.items():
        scores[student] = grades.get(assignment)
    return scores


breakpoint()
print(get_scores(student_roster, 'Homework 2'))
