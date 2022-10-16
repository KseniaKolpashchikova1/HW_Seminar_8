import BD_model

def get_info():
    per_surname = input('Введите фамилию: ')
    per_name = input('Введите имя: ')
    per_position = input('Введите должность: ')
    per_salary = int(input('Введите зарплату: '))
    add_person = {"surname":per_surname, "name": per_name, "position": per_position, "salary": per_salary}
    return(add_person)

# def get_info():
#     per_surname = get_per_info('Фамилия')
#     per_name = get_per_info('Имя')
#     per_position = get_per_info('Должность')
#     per_salary = get_per_info('Зарплата')
#     per_as_dict = {"surname":per_surname, "name": per_name, "position": per_position, "salary": per_salary}
#     return(per_as_dict)