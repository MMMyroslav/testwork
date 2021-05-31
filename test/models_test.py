import unittest

from models.init_db import init_db
from models.model import Department, Employee
from service import db_service as db



class ModuleTest(unittest.TestCase):

    def test_init_db(self):
        self.assertIsNone(init_db())

    def test_contain_name_Dep(self):
        self.assertIn('__tablename__', Department.__dict__, "Didn't use tablename")

    def test_contain_name_Empl(self):
        self.assertIn('__tablename__', Employee.__dict__, "Didn't use tablename")

    def test_db_serv_decorators(self):
        elements = [
            db.create_Session_sel,
            db.create_Session_del,
            db.create_Session_upd,
            db.create_Session_one,
            db.create_Session_all,
        ]

        def t1():
            return None

        for i in elements:
            with self.subTest(i=True):
                self.assertTrue(callable(i(t1)))

    def test_dml_ins_Empl(self):
        from datetime import date

        self.assertIs(db.dml_insert_Empl(
                    name='name',
                    surname='surname',
                    mid_name='midname',
                    date_of_birth=(2001,1,1),
                    salary=3005,
                    related_department=1), None)

    def test_dml_ins_Dep(self):
        ob = Department(name='name')
        temp = db.dml_insert_Dep(name='name1')
        self.assertIsInstance(ob, Department)
        self.assertIs(temp, None)

    def test_dml_upd_Empl(self):
        temp = db.dml_update_Empl(('id', 1), ('name', 'Ivanko'))
        self.assertIs(temp, None)

    def test_dml_upd_Dep(self):
        temp = db.dml_update_Dep(('id', 21), ('name', 'Improve'))
        self.assertIs(temp, None)

    def test_dml_delete_Empl(self):
        temp = db.dml_delete_Empl(('id', 21))
        self.assertIs(temp, None)

    def test_sel_Dep(self):
        temp = db.dml_select_Dep_cur(('id', 1))
        self.assertEqual(len(temp), 1)
        self.assertEqual(str(type(temp[0])), "<class 'sqlalchemy.engine.row.Row'>")
        self.assertTrue(temp[0][0].name)
        self.assertTrue(temp[0][0].id)

    def test_sel_Empl(self):
        temp = db.dml_select_Empl_cur(('id', 2))
        self.assertEqual(len(temp), 1)
        self.assertEqual(str(type(temp[0])), "<class 'sqlalchemy.engine.row.Row'>")
        self.assertTrue(temp[0][0].name)
        self.assertTrue(temp[0][0].surname)

    def test_sel_Empl_all(self):
        temp = db.dml_select_Empl_all(2)

        self.assertEqual(len(temp[0]), 2)
        self.assertEqual(str(type(temp[0])), "<class 'sqlalchemy.engine.row.Row'>")
        self.assertTrue(temp[0][0].name)
        self.assertTrue(temp[0][0].surname)

    def test_sel_Dep_all(self):
        temp = db.dml_select_Dep_all()

        self.assertEqual(len(temp[0]), 2)
        self.assertEqual(str(type(temp[0])), "<class 'sqlalchemy.engine.row.Row'>")
        self.assertTrue(temp[0].name)

    def test_average_sal_count(self):
        from App import average_sal_count
        temp = average_sal_count(1)
        self.assertIsInstance(float(temp), float)

    def test_transform(self):
        from App import transform
        temp = transform('1-2-3')
        self.assertEqual(temp, (1,2,3))











if __name__ == '__main__':
    unittest.main()
