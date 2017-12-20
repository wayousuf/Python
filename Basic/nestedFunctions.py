def get_students():
    studnets = ["waqas", "salman"]
    def get_students_titlecase():
        studnets_titlecase = []
        for studnet in studnets:
            studnets_titlecase.append(studnet.title())
        return studnets_titlecase
    students_titlecase_names = get_students_titlecase()
    print(students_titlecase_names)

get_students()