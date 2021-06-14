from models.init_db import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Date, DECIMAL
from sqlalchemy.orm import relationship


class MetaFields:
    """
    Base class
    """

    id = Column(String(50), primary_key=True, unique=True)
    name = Column(String(30), nullable=False, unique=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Employee(MetaFields, Base):
    __tablename__ = 'employee'

    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    mid_name = Column(String(30), nullable=True)
    date_of_birth = Column(Date, nullable=False)
    salary = Column(DECIMAL, nullable=False)
    related_department = Column(String(50), ForeignKey('department.id'))
    department = relationship('Department')

    def __init__(self, id, name, surname, mid_name,
                 date_of_birth, salary, related_department):
        super().__init__(id, name)

        self.surname = surname
        self.mid_name = mid_name
        self.date_of_birth = date_of_birth
        self.salary = salary
        self.related_department = related_department

    def __str__(self):
        return f'{self.name} {self.mid_name} {self.surname}'

    def __repr__(self):
        return f'{self.name} {self.mid_name} {self.surname}'


class Department(MetaFields, Base):
    __tablename__ = "department"
