def average_score(scores):
    return sum(scores)

exam_scores = []

for value in range(10):
    score = int(input("Enter your score: "))
    exam_scores.append(score)


print(average_score(exam_scores))