# Function to calculate total score
def calculate_total(student):
    # Total is the sum of Hindi, English, Maths, Science, and Computer scores
    total = student[4] + student[5] + student[6] + student[7] + student[8]
    return total

# List to store student data
students = []

# Adding student data
students.append(['01','Ashish'  ,   '10th'  ,15,85,88,92,90,95, 0])
students.append(['02','Abhi'    ,   '10th'  ,16,78,82,88,84,80, 0])
students.append(['03','Aman'    ,   '10th'  ,15,90,92,94,93,96, 0])
students.append(['04','Kratika' ,   '10th'  ,15,97,90,90,91,90, 0])
students.append(['05','Mona'    ,   '10th'  ,15,76,81,39,87,90, 0])
students.append(['06','kamal'   ,   '10th'  ,16,64,72,58,94,70, 0])
students.append(['07','Ragini'  ,   '10th'  ,15,92,95,91,92,59, 0])
students.append(['08','Kartik'  ,   '10th'  ,15,78,69,70,88,76, 0])
students.append(['09','Anshika' ,   '10th'  ,15,88,81,50,70,51, 0])
students.append(['10','Aira'    ,   '10th'  ,16,63, 2,89,87,89, 0])


# Calculate total score for each student
for student in students:
    student[9] = calculate_total(student)

# Print student data
print("ID  | Name    | Standard|  Age    |  Hindi  | English | Maths   | Science | Computer| Total   ")
print("----|---------|---------|---------|---------|---------|---------|---------|---------|---------")
for student in students:
    print(f"{student[0]}  | {student[1]:<7} | {student[2]:<8} | {student[3]:<3} | {student[4]:<5} | {student[5]:<7} | {student[6]:<5} | {student[7]:<7} | {student[8]:<8} | {student[9]:<5} ")


#Display the names of students whose marks in English are greater than 50
print("\nStudents with English marks greater than 50:")
for student in students:
    if student[5] > 50:
        print(student[1])

#Find the top four scorers in Maths
students_sorted_by_maths = sorted(students, key=lambda x: x[6], reverse=True)

print("\nTop four scorers in Maths:")
for student in students_sorted_by_maths[:4]:
    print(f"Name: {student[1]}, Age: {student[3]}")

#Find the bottom three scorers in Computer
students_sorted_by_computer = sorted(students, key=lambda x: x[8])
print("\nBottom three scorers in Computer:")
for student in students_sorted_by_computer[:3]:
    print(f"Name: {student[1]}, ID: {student[0]}, Age: {student[3]}") 