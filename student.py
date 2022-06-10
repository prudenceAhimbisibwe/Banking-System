class Student:
    school="Akirachix"
    def __init__(self,first_name,last_name,country,age,year_of_birth):
        self.first_name=first_name
        self.last_name=last_name
        self.country = country
        self.age = age
        self.year_of_birth=year_of_birth

    def full_name(self):
        return f"Hello {self.first_name} {self.last_name} from {self.country} welcome to {self.school}"

    def my_age(self):
        year=2022-self.age
        return f"Hello you were born in {year}"
    def initial(self):
        return f"Hello your initial is {self.first_name[0]} {self.last_name[0]}"
