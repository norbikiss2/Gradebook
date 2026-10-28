def calculate_average_drop_lowest(grades):
    if len(grades) <= 1:
        return calculate_average(grades)
    sorted_grades = sorted(grades)[1:]
    return sum(sorted_grades) / len(sorted_grades)