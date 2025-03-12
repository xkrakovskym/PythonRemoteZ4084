class Student:
    def __init__(self, full_name, contact_details, age, grades):
        self.full_name = full_name
        self.contact_details = contact_details
        self.age = age
        self.grades = grades

    def get_full_name(self):
        return self.full_name

    def get_contact_details(self):
        return self.contact_details

    def is_adult(self):
        return self.age >= 18

    def get_grades(self):
        return self.grades

class Favorite:
    def __init__(self, first_name, last_name, email, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.grades = grades

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_age(self):
        return self.age

    def get_grades(self):
        return self.grades


class FavoriteAdapter(Student):
    def __init__(self, favorite: Favorite):
        full_name = f"{favorite.get_first_name()} {favorite.get_last_name()}"
        contact_details = favorite.get_email()
        age = favorite.get_age()
        grades = favorite.get_grades()
        super().__init__(full_name, contact_details, age, grades)


favorite = Favorite("Michal", "Krakovsky", "m@k.com", 32, [1,2,3])

student1 = FavoriteAdapter(favorite)

print(student1.get_full_name())