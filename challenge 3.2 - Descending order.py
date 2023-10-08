"""Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number(string), and cgpa(float). Test the function with different input lists of student."""
class student:
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students (student_list):      
# Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list, key=lambda student: student.cgpa,reverse=True)
  #Syntax = lambda arg:exp
  return sorted_students

#Example usage:
students = [student("priyanka", "A123", 9.2),
student("Akila", "A124", 6.8),
student("Sri", "A125", 4.9),
student("Divya", "A126", 7.5),
]
sorted_students = sort_students(students)
# Print the sorted list of students
for student in sorted_students: print("name: {}, roll Number: {}, cgpa: {}".format(student.name,student.roll_number,student.cgpa))