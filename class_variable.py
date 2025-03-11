class MyClass:
    class_variable = 1

    def __init__(self, value):
        self.instance_variable = value


my_class1 = MyClass(5)
my_class2 = MyClass(10)

print(f"instance variable = {my_class1.instance_variable}, class variable = {my_class1.class_variable}")
print(f"instance variable = {my_class2.instance_variable}, class variable = {my_class2.class_variable}")
print(f"{MyClass.class_variable}")

