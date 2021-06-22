from models.init_db import engine
from models.model import *
from sqlalchemy.orm import Session
from datetime import date
from uuid import uuid4


def uuid_format(data):
    return ''.join(str(uuid4()).split('-'))


def create_Session_one(func):
    def wrapper(*args, **kwargs):
        session = Session(engine)
        data = func(*args, **kwargs)
        session.add(data)
        session.commit()
        session.close()

    return wrapper


def create_Session_all(func):
    def wrapper(*args, **kwargs):
        session = Session(engine)
        data = func(*args, **kwargs)
        session.add_all(data)
        session.commit()
        session.close()

    return wrapper


def create_Session_upd(func):
    def wrapper(*args, **kwargs):
        from sqlalchemy import update
        session = Session(engine)
        session.execute(eval(func(*args, **kwargs)))
        session.commit()
        session.close()

    return wrapper


def create_Session_sel(func):
    def wrapper(*args, **kwargs):
        from sqlalchemy import select
        from sqlalchemy.orm import Bundle
        session = Session(engine)
        data = session.execute(
            eval(func(*args, **kwargs))).all()
        session.close()
        return data

    return wrapper


def create_Session_del(func):
    def wrapper(*args, **kwargs):
        from sqlalchemy import delete
        session = Session(engine)
        session.execute(eval(func(*args, **kwargs)))
        session.commit()
        session.close()

    return wrapper


@create_Session_one
def dml_insert_Empl(name, surname, mid_name,
                    date_of_birth: tuple, salary: float,
                    related_department: int):
    data = Employee(id=uuid_format(uuid4()),
                    name=name,
                    surname=surname,
                    mid_name=mid_name,
                    date_of_birth=date(*date_of_birth),
                    salary=salary,
                    related_department=related_department)

    return data


@create_Session_one
def dml_insert_Dep(name):
    data = Department(id=uuid_format(uuid4()),
                      name=name
                      )

    return data


@create_Session_all
def dml_insert_Dep_all(arr_arrs):
    res = []
    for arr in arr_arrs:
        res.append(Department(name=arr))

    return res


@create_Session_all
def dml_insert_Empl_all(arr_arrs):
    res = []
    for arr in arr_arrs:
        name, surname, mid_name, date_of_birth, salary, related_department = arr
        res.append(Employee(name=name,
                            surname=surname,
                            mid_name=mid_name,
                            date_of_birth=date(*date_of_birth),
                            salary=salary,
                            related_department=related_department))

    return res


@create_Session_upd
def dml_update_Empl(param_where: tuple, new_val: tuple):
    temp = "update(Employee)." \
           f"where(Employee.{param_where[0]} == {param_where[1]!r})." \
           "values({" + f"{new_val[0]!r}" + ": " + f"{new_val[1]!r}" + \
           "}" + ")"

    return temp


@create_Session_upd
def dml_update_Dep(param_where: tuple, new_val: tuple):
    temp = f"update(Department)." \
           f"where(Department.{param_where[0]} == {param_where[1]!r})." \
           "values({" + f"{new_val[0]!r}" + ": " + f"{new_val[1]!r}" + \
           "}" + ")"

    return temp


@create_Session_del
def dml_delete_Empl(param_where: tuple):
    temp = "delete(Employee)." \
           f"where(Employee.{param_where[0]} == {param_where[1]!r})"

    return temp


@create_Session_del
def dml_delete_Dep(param_where):
    temp = "delete(Department)." \
           f"where(Department.id == {param_where!r})"

    return temp


@create_Session_sel
def dml_select_Dep_all(sort='asc'):
    temp = "select(Department.id, Department.name)"

    return temp


@create_Session_sel
def dml_select_Empl_all(id):
    temp = "select(" \
           "Bundle(\'employee\', Employee.id, " \
           "Employee.name, Employee.surname, Employee.mid_name," \
           "Employee.date_of_birth, Employee.salary, " \
           "Employee.related_department)," \
           "Bundle(\'department\', Department.name))." \
           f"where(Employee.related_department == {id!r})." \
           'join_from(Employee, Department)'

    return temp


@create_Session_sel
def dml_select_Empl_all_sal(id):
    temp = "select(" \
           "Employee.salary)." \
           f"where(Employee.related_department == {id!r})"

    return temp


@create_Session_sel
def dml_select_Empl_cur(data: tuple):
    temp = "select(Employee)." \
           f"filter_by({data[0]}={data[1]!r})"

    return temp


@create_Session_sel
def dml_select_Dep_cur(data: tuple):
    temp = "select(Department)." \
           f"filter_by({data[0]}={data[1]!r})"

    return temp


def dml_sel_text(var: str) -> list:
    from sqlalchemy.sql import text
    session = Session(engine)
    v = text(f'SELECT * FROM employee WHERE employee.date_of_birth = :x')
    data = session.execute(v, {'x': f'{var}'}).all()
    session.close()

    return data


def dml_sel_text_per(var: dict) -> dict:
    from sqlalchemy.sql import text
    session = Session(engine)
    v = text(f'SELECT * FROM employee WHERE employee.date_of_birth BETWEEN :x AND :y')
    data = session.execute(v, {'x': f'{var.get("from_date")}',
                               'y': f'{var.get("to_date")}'}
                           ).all()
    session.close()
    return data
