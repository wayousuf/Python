number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")


text = "Python"
if text:
    print("Text is defined and truthy")


python_course = True
if python_course:
    print("This will execute")

aliens_found = None
if aliens_found:
    print("This will NOT execute")


number = 3
if number == 3 and python_course:
    print("This will execute")

if number == 17 or python_course:
    print("This will also execute")


a = 1
b = 2

print("bigger" if a > b else "smaller")
