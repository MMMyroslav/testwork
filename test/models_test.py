import unittest

from models.init_db import init_db
from models.model import Department, Employee
from service import db_service as db


class EmplTest(unittest.TestCase):
    const_type = "<class 'sqlalchemy.engine.row.Row'>"
    var_dep = db.dml_select_Dep_all()[0][0]
    temp_user = None

    def test_dml_ins_Empl(self):
        """
        passed
        :return:
        """
        from datetime import date
        test_salary = 100000

        self.assertIs(db.dml_insert_Empl(
            name='name',
            surname='surname',
            mid_name='midname',
            date_of_birth=(2001, 1, 1),
            salary=test_salary,
            related_department=EmplTest.var_dep), None)
        EmplTest.temp_user = db.dml_select_Empl_cur(
            ('salary', test_salary))[0][0]

    def test_dml_upd_Empl(self):
        """
        passed
        :return:
        """
        temp = db.dml_update_Empl(('id', EmplTest.temp_user.id),
                                  ('name', 'Ivanko2'))
        self.assertIs(temp, None)

    def test_dml_zdelete_Empl(self):
        temp = db.dml_delete_Empl(
            ('id', EmplTest.temp_user.id)
        )
        self.assertIs(temp, None)

    def test_sel_Empl(self):
        """
        passed
        :return:
        """
        temp = db.dml_select_Empl_cur(('name', 'Marko'))[0]
        self.assertEqual(len(temp), 1)
        self.assertEqual(str(type(temp)), EmplTest.const_type)
        self.assertTrue(temp[0].name)
        self.assertTrue(temp[0].surname)

    def test_sel_Empl_all(self):
        """
        passed
        :return:
        """
        temp = db.dml_select_Empl_all(EmplTest.var_dep)

        self.assertEqual(len(temp[0]), 2)
        self.assertEqual(str(type(temp[0])), EmplTest.const_type)
        self.assertTrue(temp[0][0].name)
        self.assertTrue(temp[0][0].surname)


class StaticTest(unittest.TestCase):

    def test_average_sal_count(self):
        """
        passed
        :return:
        """
        from App import average_sal_count
        temp = average_sal_count(EmplTest.var_dep)
        self.assertIsInstance(float(temp), float)

    def test_transform(self):
        """
        passed
        :return:
        """
        from App import transform
        temp = transform('1-2-3')
        self.assertEqual(temp, (1, 2, 3))


class MetaTest(unittest.TestCase):
    def test_init_db(self):
        """
        passed
        :return:
        """
        self.assertIsNone(init_db())

    def test_contain_name_Dep(self):
        """
        passed
        :return:
        """
        self.assertIn('__tablename__', Department.__dict__, "Didn't use tablename")

    def test_contain_name_Empl(self):
        """
        passed
        :return:
        """
        self.assertIn('__tablename__', Employee.__dict__, "Didn't use tablename")


class DecoratorTest(unittest.TestCase):

    def test_db_serv_decorators(self):
        """
        passed
        :return:
        """
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


class DepTest(unittest.TestCase):
    temp_dep = None

    def test_dml_ins_Dep(self):
        """
        passed
        :return:
        """
        ob = 'Improve'
        temp = db.dml_insert_Dep(ob)
        DepTest.temp_dep = db.dml_select_Dep_cur(
            ('name', ob))[0][0]
        self.assertIsInstance(self.temp_dep, Department)
        self.assertIs(temp, None)

    def test_dml_upd_Dep(self):
        """
        passed
        :return:
        """
        temp = db.dml_update_Dep(('id', self.temp_dep.id),
                                 ('name', 'Improve2'))
        self.assertIs(temp, None)

    def test_sel_Dep(self):
        """
        passed
        :return:
        """
        temp = db.dml_select_Dep_cur(('id', self.temp_dep.id))
        print('sel', self.temp_dep)
        self.assertEqual(len(temp), 1)
        self.assertEqual(str(type(temp[0])), EmplTest.const_type)
        self.assertTrue(temp[0][0].name)
        self.assertTrue(temp[0][0].id)

    def test_sel_Dep_all(self):
        """
        passed
        :return:
        """
        temp = db.dml_select_Dep_all()
        self.assertEqual(len(temp[0]), 2)
        self.assertEqual(str(type(temp[0])), EmplTest.const_type)
        self.assertTrue(temp[0].name)

    def test_zclean(self):
        """
        passed
        :return:
        """
        t1 = db.dml_delete_Dep(('name', 'Improve'))
        t2 = db.dml_delete_Dep(('name', 'Improve2'))
        self.assertEqual(t1, t2)


if __name__ == '__main__':
    unittest.main()
