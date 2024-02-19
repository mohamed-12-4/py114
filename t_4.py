"""
Task 4: A certain University gives 100 point exams that are graded on the scale 90-100:A, 80-89:B,
70-79:C, 60-69:D, <60:F. Write a program that accepts exam scores as input five times and prints out the
corresponding grade.
"""
def grade_to_letter(grade):
    """
    A function that accepts the grade as a number and convert it to the corresponding letter

    """
    assert grade >= 0 and grade <= 100, "Invalid grade number"
    if grade >= 90:
        return "A"
    elif grade < 90 and grade >= 80:
        return "B"
    elif grade < 80 and grade >= 70:
        return "C"
    elif grade < 70 and grade >= 60:
        return "D"
    else:
        return "F"

grades = []
for i in range(5):
    grades.append(int(input(f"Enter grade number {i+1}: ")))
for i in range(5):
    print(f"grade number {i+1} ({grades[i]}): {grade_to_letter(grades[i])}")
