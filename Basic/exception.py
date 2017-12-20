student = {
    "name" : "Mark",
    "student_id" : 1234,
    "feedback" : None
}

try:
    last_name = student["last_name"]
except KeyError as error :
    print(error)
    print("Error finding last_name")
except Exception:
    print("Unknow Error")
print("This code executed!")