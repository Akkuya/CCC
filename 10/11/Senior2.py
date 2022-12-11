q = int(input())
student = []
answers = []
counter = 0
for i in range(q):
  x = input()
  student.append(x)
for i in range(q):
  y = input()
  answers.append(y)

for i in range(q):
  if student[i] == answers[i]:
    counter+=1

print(counter)
