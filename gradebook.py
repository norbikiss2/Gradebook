"""
Campus Gradebook CLI
Starter script for Git branching and conflict resolution practice.
"""

def calculate_average(grades):
    """Calculates the standard arithmetic mean of a grade list."""
    if not grades:
        return 0.0
    return sum(grades) / len(grades)


def get_letter_grade(score):
    """TODO: Convert numerical score (0-100) into a letter grade."""
    # Starter baseline implementation:
    if score >= 60:
        return "PASS"
    return "FAIL"


def display_report(student_name, grades):
    avg = calculate_average(grades)
    status = get_letter_grade(avg)
    
    print("=" * 35)
    print(f"Student: {student_name}")
    print(f"Scores : {grades}")
    print(f"Average: {avg:.2f}")
    print(f"Status : {status}")
    print("=" * 35)


if __name__ == "__main__":
    sample_scores = [88, 92, 59, 78, 95]
    display_report("Alex Smith", sample_scores)