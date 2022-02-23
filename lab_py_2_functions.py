import pickle
from datetime import datetime


def input_file(filename):
    print("Choose input mode:\n1) append info in the file\n2) create new file")
    input_mode = int(input())
    while True:
        if input_mode == 1:
            file = open(filename, "ab")
            break
        elif input_mode == 2:
            file = open(filename, "wb")
            break
        else:
            print("Invalid input mode")

    line = input("Enter information about the employees in format [surname dd.mm.yyyy dd.mm.yyyy] "
                 "(send empty line to finish):\n")
    while line != "":
        words = line.split()
        birthday = words[1].split('.')
        start_career = words[2].split('.')
        employee = {
            "surname": words[0],
            "birthday": {"day": int(birthday[0]),
                         "month": int(birthday[1]),
                         "year": int(birthday[2])},
            "start_career": {"day": int(start_career[0]),
                             "month": int(start_career[1]),
                             "year": int(start_career[2])}
        }
        pickle.dump(employee, file)
        line = input()

    file.close()


def output_file(filename):
    with open(filename, 'r') as file:
        size = file.seek(0, 2)
        file.seek(0)

        while file.tell() < size:
            employee = pickle.load(file)
            print("Surname: " + employee["surname"] + "\t \tBirthday: " + get_format(employee["birthday"])
                  + "\t \t Start career: " + get_format(employee["start_career"]))


def get_format(date):
    str_day = str(date["day"])
    str_month = str(date["month"])
    if date["day"] < 10:
        str_day = '0' + str_day

    if date["month"] < 10:
        str_month = '0' + str_month

    return str_day + '.' + str_month + '.' + str(date["year"])


def birthday_in_this_month(filename):
    with open(filename, 'r') as file:
        current_datetime = datetime.now()
        sys_date = {
            "day": current_datetime.day,
            "month": current_datetime.month,
            "year": current_datetime.year
        }
        size = file.seek(0, 2)
        file.seek(0)

        while file.tell() < size:
            employee = pickle.load(file)
            work_experience = get_years_between_dates(employee["start_career"], sys_date)
            if employee.birthday["month"] == sys_date["month"] and work_experience >= 5:
                print("Surname: " + employee["surname"] + "\t \tBirthday: " + get_format(employee["birthday"])
                      + "\t \t Start career: " + get_format(employee["start_career"]))


def get_years_between_dates(start_date, end_date):
    years = end_date["year"] - start_date["year"]
    if start_date["month"] > end_date["month"] or (start_date["month"] == end_date["month"] and
                                                   start_date["day"] > end_date["day"]):
        years -= 1
    return years
