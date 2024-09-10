# 과목, 학점, 등급(과목평점)
# ObjectOrientedProgramming1 3.0 A+

gpaScore = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, 'F':0.0}

totalcredits = 0
score = 0

for i in range(20) :
    subject, credits, gpa = input().split(' ')
    
    if(gpa in gpaScore) :
        totalcredits += float(credits)
        score += float(credits) * gpaScore[gpa]

print(score / totalcredits)