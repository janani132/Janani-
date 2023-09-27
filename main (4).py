class Student:
  def                        __init__(self, name, roll_number, cpga):
    self.name=name  
    self.roll_number=roll_number
    self.cpga=cpga
def sort_students(student_list):
  sorted_students=sorted( student_list, key=lambda student: student.cpga, reverse= True)
  return sorted_students
students = [ Student("Hari","A123",7.8)    ,Student("varsha","A124",8.3) ,Student("leena","A125", 9.1) ,Student("janu","A126",9.9)]
sorted_students= sort_students(students)
for student in sorted_students:
 print("Name :{}, Roll Number:{}, CPGA:{}".format(student.name,student.roll_number,student.cpga))