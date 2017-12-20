students_names = ["Waqas", "Yousuf", "Salman", "Ruhan", "Suli"]

for name in students_names:
    if name == "Yousuf":
        continue
        print("Found him! " + name)
        break
    print("Currently testing " + name)