#!/usr/bin/python3
def best_score(a_dictionary):
    score = None
    student = None

    if a_dictionary is not None:
        for k, v in a_dictionary.items():
            if score is None or score < v:
                score = v
                student = k

    return student
