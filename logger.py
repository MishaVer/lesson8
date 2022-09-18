import view
def get_data():
    with open("file.txt", 'r') as file:
        data = file.read().split(f'\n')
        return data

def add_data(a):
    with open("file.txt", 'a') as file:
        file.write(a)

def edit_data(a, b):
     with open("file.txt", 'r') as file:
        od = file.read()

        new_data = od.replace(a, b)

        with open('file.txt', 'w') as file:
            file.write(new_data)

def delete(a):
    with open('file.txt', 'r') as file:
        old_data = file.read()

    b = ''
    new_data = old_data.replace(a, b)

    with open('file.txt', 'w') as file:
        file.write(new_data)