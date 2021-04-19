scores = []
scores.append((int)(input("Test score 1: ")))
scores.append((int)(input("Test score 2: ")))
scores.append((int)(input("Test score 3: ")))
avg = (scores[0] + scores[1] + scores[2]) / 3
print("Average", avg)
grade = ""
if avg > 90:
  grade = "A"
elif avg > 80:
  grade = "B"
elif avg > 70:
  grade = "C"
elif avg > 60:
  grade = "D"
else:
  grade = "F"
print("Grade:", grade)
