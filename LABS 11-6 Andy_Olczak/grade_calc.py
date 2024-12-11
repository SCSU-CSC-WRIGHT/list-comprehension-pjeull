def grade_calc(scores):
    if len(scores) == 0:
        return "No scores provided."
    
    average = sum(scores) / len(scores)
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return average, grade

scores = []
print("Enter test scores, one per line. Hit 'enter' after each score, then type 'done' when finished: ")

while True:
    score = input()
    if score.lower() == 'done':
        break
    try:
        score = float(score)
        scores.append(score)
    except ValueError:
        print("Please enter a valid number.")
    
average, grade = grade_calc(scores)
print(f"Average score: {average:.2f}")
print(f"Letter grade: {grade}")