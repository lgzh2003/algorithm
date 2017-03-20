student = []
grades = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    student.append([name,float(score)])
    grades.append([float(score)])

grades.sort()
secondM = [x for x in grades if x!=grades[0]]
secondScore = secondM[0][0]
nameList = [x for x in student if x[1]==secondScore]
nameList.sort()
for l in nameList:
    print l[0]
#https://www.hackerrank.com/challenges/nested-list
