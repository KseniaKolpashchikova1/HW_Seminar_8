import os.path
import json
from pprint import pprint

company_as_dict = [{'Surname': 'surname', 'Name': 'name', 'Position': 'position', 'Salary': 100}]
file_name = './Seminar_8'

def read_json(company_as_dict):
    # file_name = './Seminar_8'
    # if not os.path.isfile(file_name):
    #     print(f'Файл не существует {file_name}')
    #     with open(file_name,'w') as f:
    #         json.dump(company_as_dict, f)
    with open(file_name,'r', encoding = 'utf-8') as f:
            company_as_dict = json.load(f)
    pprint(company_as_dict)

def save_json(company_as_dict):
    with open(file_name,'w') as f:
        json.dump(company_as_dict, f)
        print(f'Файл {file_name} сохранен')

def add_new_person(company_as_dict):
    with open(file_name,'r') as f:
        data = json.dump(company_as_dict, f)
    n_data = {'Surname': 'surname', 'Name': 'name', 'Position': 'position', 'Salary': 100}
    data[file_name].append(n_data)
    # save_json(company_as_dict)

file_name = './Seminar_8'

# def find_surname_per():
#         find = input('Введите фамилию для поиска сотрудника: ')
#         for find in file_name():
#             if file_name['surname'] == surname:
#                 print( 'find_surname:', surname)
    
# def del_per():
#     del file_name['surname']

