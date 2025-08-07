student_data =[]

def add(name,grades):
    new_student={
        "name": name,
        "grades": grades
    }
    student_data.append(new_student)
    print(f"The {name} is added in student data")

def average(student):
        if not student["grades"]:
            return 0.0
        return sum(student["grades"])/ len(student["grades"])

def top_performance():
    if not student_data:
        return []
    student_averages = [
        {"student": student, "average": average(student)}
        for student in student_data
    ]
    max_average = max(sa["average"] for sa in student_averages)
    top_performers = [
        sa["student"] for sa in student_averages if sa["average"] == max_average
    ]
    return top_performers
print("    Adding students    ")
add("Aryan",[90,93,95,92])
add("Jenis",[85.94,63,44])
add("Rakesh",[85,98,83,85])
add("Prince",[93,28,58,83])

print("\n    Student Information    ")
for student in student_data:
    print(f"Name: {student['name']}, Grades: {student['grades']}")


print("\n    Calculating Averages    ")
for student in student_data:
    avg = average(student)
    print(f"The average grade for {student['name']} is: {avg:.2f}")


print("\n   Finding Top Performer    ")
top_students = top_performance()

if top_students:
    print("The top performer is:")
    for student in top_students:
        avg = average(student)
        print(f"{student['name']} with an average of {avg:.2f}")
else:
    print("No students have been added yet.")