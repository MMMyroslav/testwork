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