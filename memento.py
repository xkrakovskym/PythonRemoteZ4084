import pickle

class SomeSimpleClass:
    def __init__(self, name="", count=0):
        self.name = name
        self.count = count

    def get_state(self):
        return pickle.dumps(self.__dict__)

    def restore_state(self, memento):
        self.__dict__.clear()
        self.__dict__.update(pickle.loads(memento))

    def display(self):
        print(f"{self.name} - {self.count}")


my_simple_class = SomeSimpleClass("test", 10)
memento = my_simple_class.get_state()
other_simple_class = SomeSimpleClass()
other_simple_class.display()
other_simple_class.restore_state(memento)
other_simple_class.display()