from turtle import clear


def menu():
    print("Choose action (1 - find person 2 - add person 3 - change data 4 - delete data)")
    res = int(input())
    return res

def get_info():
    return input("enter information")

def new_emp():
    fio = input("fio: ")
    date = input("date: ")
    work = input("position: ")
    salary = input("salary: ")
    phone = input("Phone: ")

    zap = "/n" + fio + " | " + date + " | " + work + " | " + salary + " | " + phone
    return zap