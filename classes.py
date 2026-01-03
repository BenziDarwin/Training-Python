from datetime import datetime

class Student:
    def __init__(self, name:str, date_of_birth:str, stream:str):
        self.name = name
        self.age = datetime.now().year - datetime.fromisoformat(date_of_birth).year 
        self.stream = stream
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name



class CampusStudent(Student):
    def set_age(self, age):
        self.age = age

adrian = CampusStudent("Adrian", "2002-07-04T17:57:24+00:00", "P4 West")

print(adrian.get_age())

adrian.set_age(12)

print(adrian.get_age())
