class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Student Name:{self.name}, Marks:{self.marks}")

s1 = Student("Santhosh",100)
s1.display()