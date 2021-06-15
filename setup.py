import decimal
from models.init_db import init_db, engine
from models.model import *
from sqlalchemy.orm import Session
from random import randint
from datetime import date
from sqlalchemy import select
from pprint import pprint
from service.db_service import *
import random
from uuid import uuid4


def uuid_format(data):
    return ''.join(str(uuid4()).split('-'))


def fill(n):
    d = dml_select_Dep_all()
    res_id = []
    for i in d:
        res_id.append(i.id)

    f_name = ['Ivan', 'Taras', 'Nazar', 'Andriy', 'Bogdan', 'Mykhailo', 'Klym', 'Volodymyr',
              'Myroslav', 'Igor', 'Oleksandr', 'Victor',
              'Danylo', 'Marko', 'Matviy', 'Maksym']

    f_surname = tuple(globals().keys())
    res1 = []
    for i in f_surname:
        if i.isalpha():
            if i.istitle():
                res1.append(i)
            else:
                res1.append(i.title())
        else:
            s = i.replace('_', '')
            res1.append(s.capitalize())

    res = []

    for i in range(n):
        res.append(Employee(
            id=uuid_format(uuid4()),
            name=f_name[randint(0, len(f_name)-1)],
            surname=res1[randint(0, len(res1)-1)],
            mid_name=f_name[randint(0, len(f_name)-1)]+'ovich',
            date_of_birth=date(randint(1975, 2002),randint(1,12), randint(1,28)),
            salary=randint(1800, 5200),
            related_department=random.choice(res_id)))

    session = Session(engine)
    session.add_all(res)
    session.commit()


def fill_dep():
    temp = ['Finance', 'Audit', 'Production', 'IT', 'Managers',
            'Sales', 'Support', 'Security']
    res = []

    for i in temp:
        res.append(Department(id=uuid_format(uuid4()), name=f'{i}'))
    session = Session(engine)
    session.add_all(res)
    session.commit()


def start():
    init_db()
    fill_dep()
    fill(100)


# start()

# start()
# session = Session(engine)
# from sqlalchemy.orm import Bundle
# b = select(
#     Bundle("employee", Employee.id,
#            Employee.name, Employee.surname,
#            Employee.mid_name,Employee.date_of_birth, Employee.salary),
#     Bundle("department", Department.name)).\
#     join_from(Employee, Department)
# bbb = dml_select_Empl_all()
# bb = session.execute(b).all()
# for dd in bbb:
#     print(dd)
# print(st1, type(st1))

# dml_select_Empl_cur(
#     name = 'qwerty',
#     surname ='qwerty',
#     mid_name = 'qwerty',
#     date_of_birth = (1,10,2001),
#     salary = decimal.Decimal('3000.25'),
#     related_department = 1
# )
#
# from sqlalchemy.sql import text
#
# session = Session(engine)
# # v = text('SELECT * FROM employee WHERE employee.date_of_birth = :x')
# # v = dml_select_Empl_cur(('id', 2))
# d = dml_select_Empl_cur(('date_of_birth', (2002,1,3)))


# print(data)
# import decimal
# def correct_date(var):
#     if isinstance(var, str):
#         return '-'.join(tuple(map(str, tuple(map(int, var.split('-'))))))
#     for i in var:
#         var[i] = correct_date(var[i])
#     return var
# d = 100
# voda = 99
# vtrata = 98
# vechir = decimal.Decimal(voda*vtrata/100 + 1)
# print(vechir)

# # d = dml_sel_text_per(qwer)
# print(qwer)
# v = text(f'SELECT * FROM employee WHERE employee.date_of_birth BETWEEN :x AND :y')
# data = session.execute(v, {'x': f'{qwer.get("from_date")}',
#                            'y': f'{qwer.get("to_date")}'}
#                        ).all()
# session.close()
#
# pprint(data)

# qwer = correct_date({'from_date': '1995-01-10', 'to_date': '2002-02-02'})
# werq = dml_sel_text_per(qwer)
# pprint(werq)

# rer = dml_sel_text_per({'from_date': '1900-01-10', 'to_date': '2022-02-02'})

# condition = ('id', '4')
# rer = dml_select_Empl_cur(condition)
# pprint(rer[0][0].__dict__)
# staff_temp = dml_select_Empl_all(1)
# staff = {}
# for i in staff_temp:
#         staff[i[0][0]] = {
#             'name': i[0].name,
#             'surname': i[0].surname,
#             'mid_name': i[0].mid_name,
#             'date_of_birth': i[0].date_of_birth,
#             'salary': i[0].salary,
#             'related_department': i[0].related_department,
#             'dep_name': i[1].name_1
#         }
# pprint(staff[6])

# qwe = dml_select_Empl_all('d57009a9-1ce4-45ce-93af-a5dfb536ea8a')
# pprint(qwe)