import random
s_name=['pushpendra','Akash','Vivek','rachit','prashant']
student_marks={students:random.randint(60,100) for students in s_name}
passed_student={students:marks for (students,marks) in student_marks.items() if marks>75}
print(passed_student)