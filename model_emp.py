from operator import truediv
import logger
import view

def search(emp):
    book = logger.get_data()
    ans = []
    flag = False
    for i in book:
        i.find(emp) != -1
        flag = True
        ans.append(i)
    if flag == True:
        return ans
    else:
        return "person not found"

def edit():
    emp = view.get_info()
    find_info = search(emp)
    print(find_info)
    n_info = view.new_emp()

    for i in find_info:
        info = i.split(' | ')

    for i in range(len(info)):
        if info[i].find(emp) !=1:
            info[i] = n_info
            break

    logger.edit_data(''.join(find_info), ' | '.join(info))

def delete_info():
    book = logger.get_data
    print(book)
    emp = view.get_info()
    find_info = search(emp)
    print(find_info)