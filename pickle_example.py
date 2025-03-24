import pickle

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def __repr__(self):
        return f"name: {self.name}: age: {self.age}, grades:{self.grades}"


alice = Student("Alice", 20, [1,1,1,1,2])
bob = Student("Bob", 25, [2,3,1,2,1,4])
students = [alice, bob]
file_path = "students.pkl"

with open(file_path, "wb") as file:
    pickle.dump(students, file)

with open(file_path, "rb") as file:
    loaded_students = pickle.load(file)

print(loaded_students)