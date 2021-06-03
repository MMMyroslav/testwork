import decimal
from models.init_db import init_db, engine
from models.model import *
from sqlalchemy.orm import Session
from random import randint
from datetime import date
from sqlalchemy import select
from pprint import pprint
from service.db_service import *


def fill(n):

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
            name=f_name[randint(0, len(f_name)-1)],
            surname=res1[randint(0, len(res1)-1)],
            mid_name=f_name[randint(0, len(f_name)-1)]+'ovich',
            date_of_birth=date(randint(1975, 2002),randint(1,12), randint(1,28)),
            salary=randint(1800, 5200),
            related_department=randint(1,8)))

    session = Session(engine)
    session.add_all(res)
    session.commit()


def fill_dep():
    temp = ['Finance', 'Audit', 'Production', 'IT', 'Managers',
            'Sales', 'Support', 'Security']
    res = []

    for i in temp:
        res.append(Department(name=f'{i}'))
    session = Session(engine)
    session.add_all(res)
    session.commit()


def start():
    init_db()
    fill_dep()
    fill(100)

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


def correct_date(var):
    if isinstance(var, str):
        return '-'.join(tuple(map(str, tuple(map(int, var.split('-'))))))
    for i in var:
        var[i] = correct_date(var[i])
    return var



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


rer = dml_select_Dep_cur(('id','1'))[0][0].name
print(rer)