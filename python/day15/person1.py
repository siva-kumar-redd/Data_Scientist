class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class Doctor(Person):
    def __init__(self,name,age,specialization,experience):
        super().__init__(name,age)
        self.specialization = specialization
        self.experience = experience


class Patient(Person):
    def __init__(self,name,age,Disease,Room_number):
        super().__init__(name,age)
        self.Disease = Disease
        self.Room_number = Room_number

doctor = Doctor("swetha",25,"heart",1)
patient = Patient("swathi",30,"eye",5)

print(f"name: {doctor.name}\nage: {doctor.age}\nSpecialization: {doctor.specialization}\nExperience: {doctor.experience}")
print(f"name: {patient.name}\nage: {patient.age}\nDisease: {patient.Disease}\nRoom Number: {patient.Room_number}")
