students = []

def get_student_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_student_titlecase()
    print(students_titlecase)

def add_student(name, student_id = 332):
    student = {"name": name, "student_id":student_id}
    students.append(name)

def var_args(name, *args):
    print(name)
    print(args)

def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["description"])
    print(kwargs["feedback"])
    print(kwargs["subscriber"])

student_list = get_student_titlecase()

add_student(name="Mark", student_id= 15)

print("Hello", "World", 3, None, "Something")

var_args("Mark", "Loves Python", None, "Hello", True)

var_kwargs("Waqas", description="Loves Python", feedback=None, subscriber= True)