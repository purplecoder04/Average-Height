# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_students= 0
total_height= 0
for i in student_heights:
  total_students+=1
  total_height+= i
avg=round(total_height/total_students)
print(avg)



