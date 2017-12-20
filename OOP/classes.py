students = []

class Student:

    school_name = "White Rose Grammar School"

    def __init__(self, name, student_id = 332):
        self.name = name
        self.student_id = student_id
        students.append(self)
    def __str__(self):
        return f"Student {self.name}"

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

class HighSchoolStudent(Student):

    school_name = "Comprehensive HSS"

    def get_school_name(self):
        return "This is High School Student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"

#salman = HighSchoolStudent("salman")
#print(salman.get_name_capitalize())
