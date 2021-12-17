"""Making the Grade - Exercism Python Challenge"""


def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    rounded_scores = []
    for score in student_scores:
        student_score = int(round(score))
        rounded_scores.append(student_score)

    return rounded_scores


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    fail_count = 0
    for score in student_scores:
        if score <= 40:
            fail_count += 1

    return fail_count


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    pets = []
    for index, _ in enumerate(student_scores):
        if student_scores[index] >= threshold:
            pets.append(student_scores[index])

    return pets


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """
    spread = highest - 41
    increment = round(spread / 4)
    d = 41
    c = d + increment
    b = c + increment
    a = b + increment
    return [d, c, b, a]


def student_ranking(student_scores, student_names):
    """
    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    """
    student_ranking = []
    for index, score in enumerate(student_scores):
        result = f"{index + 1}. {student_names[index]}: {score}"
        student_ranking.append(result)

    return student_ranking


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for info in student_info:
        if info[1] == 100:
            return info

    return []
