student = {
    "name" : "Mark",
    "student_id" : 12356,
    "feedback" : None
}

all_students = [
    {"name" : "Waqas", "studnet_id": 123456},
    {"name" : "Yousuf", "studnet_id": 4567},
    {"name" : "SAlman", "studnet_id": 3456},
]

print(student["name"])
print(student.get("last_name", "Unknow"))
print(student.keys())
print(student.values())

del student["name"]