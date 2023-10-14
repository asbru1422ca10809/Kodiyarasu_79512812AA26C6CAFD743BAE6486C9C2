class student:
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

def sort_students(student_list):
  sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
  return sorted_students

#example usage
students=[student("kodi","A143",7.8),student("hasini","A144",7.9),student("kaviya","A145",6.8),student("Priya","A146",6.5),student("Nathiya","A147",7.8)]

#Print the sortedlist of student
sorted_students=sort_students(students)

for student in sorted_students:
  print("Name:",student.name,"/Roll Number :",student.roll_number,"/cgpa :",student.cgpa)