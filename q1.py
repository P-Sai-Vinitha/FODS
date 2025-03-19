import numpy as np

student_scores = np.array([
    [85, 90, 78, 88],
    [92, 87, 85, 90],
    [76, 80, 82, 78],
    [89, 91, 88, 84]
])

avg_scores = np.mean(student_scores, axis=0)

subjects = ["Math", "Science", "English", "History"]
highest_avg_subject = subjects[np.argmax(avg_scores)]

print("Average Scores for each subject:", avg_scores)
print("Subject with the highest average score:", highest_avg_subject)
