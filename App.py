from flask import Flask
from const import SECRET_KEY
from flask import request, render_template, redirect, url_for, flash
from service.db_service import *
import decimal


app = Flask(__name__)
app.secret_key = SECRET_KEY


def average_sal_count(ind):
    """
    Creates a sum of a map-object of integers, which are built from all instances
    with current parameter department.id. Takes attribute 'salary' from instances
    :param ind:  -> integer value of department.id
    :return: string of average salary of employees in current department  for displaying in the main paige
    """
    temp = dml_select_Empl_all_sal(ind)
    numerator = sum(map(lambda i: i.salary, temp))
    denominator = len(temp)
    if not denominator:
        return 0
    return f'{numerator / denominator:.2f}'


@app.route('/')
def index():
    """
    Represents the main page on the website
    :return: html page with all departments, send parameters title -> str and
    data -> dict for jinja2 rendering
    """
    staff_temp = dml_select_Dep_all()
    staff = {}
    for i in staff_temp:
        staff[i[0]] = {'name': i[1],
                       'salary': average_sal_count(i[0])
                       }

    return render_template("depart/index_dep.html",
                           title='Departments',
                           data=staff)


@app.route('/select/<dep_id>')
def index_empl(dep_id):
    """
    Shows all employees in current department
    :param dep_id: it's a value of related department column in db.employee
    :return:html page with all employees, send parameters title -> str and
    data -> dict for jinja2 rendering
    """
    staff_temp = dml_select_Empl_all(dep_id)
    staff = {}
    for i in staff_temp:
        staff[i[0][0]] = {
            'id': i[0].id,
            'name': i[0].name,
            'surname': i[0].surname,
            'mid_name': i[0].mid_name,
            'date_of_birth': i[0].date_of_birth,
            'salary': i[0].salary,
            'related_department': i[0].related_department,
            'dep_name': i[1].name_1
        }

    return render_template("employ/index_empl.html",
                           title='Employees',
                           data=staff)


def transform(data: str) -> list:
    """
    :param data: incoming request form from modal class of html-page
    in format string - 'y-m-d'
    :return: tuple of integers in format(y,m,d)
    """
    temp = data.split('-')

    return tuple(map(int, temp))


@app.route('/insert_empl', methods=['POST'])
def insert_empl():
    """
    This route is for inserting data to mysql
    database via html forms
    :return: redirect to changed department employees
    """
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        mid_name = request.form['mid_name']
        date_of_birth = transform(request.form['date_of_birth'])
        salary = decimal.Decimal(request.form['salary'])
        related_department = request.form['related_department']
        dml_insert_Empl(name, surname, mid_name,
                        date_of_birth, salary,
                        related_department)
        _temp = request.root_url

        return redirect(f'{_temp}select/{related_department}')


@app.route('/insert', methods=['POST'])
def insert():
    """
    This route is for inserting data to mysql
    database via html forms
    :return: redirect to the main page
    """
    if request.method == 'POST':
        name = request.form['name']

        dml_insert_Dep(name)

        return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    """
    This is update route where we are going
    to update department name
    :return: redirect to the main page
    """
    if request.method == 'POST':
        condition = ('id', request.form.get('id'))
        checked_data = dml_select_Dep_cur(condition)[0][0].__dict__
        print(checked_data)
        for attr in checked_data:
            temp = request.form.get(attr)
            if temp:
                if checked_data[attr] != temp:
                    dml_update_Dep(condition, (attr, temp))

        return redirect(url_for('index'))


@app.route('/update_empl/<id>', methods=['GET', 'POST'])
def update_empl(id):
    """
    This is update route where we are going
    to update employee
    :return:  redirect to changed department employees
    """
    if request.method == 'POST':
        condition = ('id', id)
        checked_data = dml_select_Empl_cur(condition)[0][0].__dict__
        for attr in checked_data:
            temp = request.form.get(attr)
            if temp:
                if checked_data[attr] != temp:
                    dml_update_Empl(condition, (attr, temp))

        return redirect(url_for('index_empl',
                                dep_id=checked_data.get('related_department')))


@app.route('/delete_dep/<id>/', methods=['GET', 'POST'])
def delete_item(id):
    """
    This route is for deleting current department
    :param id: department.id
    :return:  redirect to the main page
    """
    dml_delete_Dep(id)

    return redirect(url_for('index'))


@app.route('/delete_empl/<id>', methods=['GET', 'POST'])
def delete_person(id):
    """
    This route is for deleting current employee
    :param id: employee.id
    :param dep_item: auxiliary parameter for redirect
    :return:  redirect to the main page
    """
    condition = ('id', id)
    try:
        dep_item = dml_select_Empl_cur(condition)[0][0].related_department
        dml_delete_Empl(condition)
    except IndexError:
        flash('No data')
        return redirect(url_for('index'))

    return redirect(url_for('index_empl', dep_id=dep_item))


def correct_date(var):
    """
    Remove leading zeros
    :param var: str or tuple
    :return: str or dict without leading zeros in decimal integer literals
    """
    if isinstance(var, str):
        return '-'.join(tuple(map(str, tuple(map(int, var.split('-'))))))
    for i in var:
        var[i] = correct_date(var[i])
    return var


def sort_data_def(db_data: dict) -> dict:
    """
    Returns data base data into dict for further convert to json format by Flask
    :param db_data: dict
    :return: dict
    """
    temp1 = None
    if isinstance(db_data, str):
        temp1 = dml_sel_text(db_data)
    if isinstance(db_data, dict):
        temp1 = dml_sel_text_per(db_data)
    temp = {}
    for j, i in enumerate(temp1):
        temp[j] = {
                'id': i[0],
                'name': i[1],
                'surname': i[2],
                'mid_name': i[3],
                'date_of_birth': i[4],
                'salary': i[5],
                'related_department': i[6],
                'dep_name': dml_select_Dep_cur(('id', str(i[6])))[0][0].name
            }

    return temp


@app.route('/sort_empl', methods=['GET'])
def sort_empl():
    """
    Create sorted data for rendering
    :return: render_template
    """
    if request.method == 'GET':
        sort_date = correct_date(request.args.get('date'))
        temp = sort_data_def(sort_date)

        return render_template('employ/index_empl.html', title='Employees', data=temp)


@app.route('/sort_empl_per', methods=['GET'])
def sort_empl_per():
    """
    Create sorted data for rendering
    :return: render_template
    """
    if request.method == 'GET':
        sorted_date = correct_date(request.args.to_dict())
        temp = sort_data_def(sorted_date)

        return render_template('employ/index_empl.html',
                               title='Employees', data=temp)


if __name__ == '__main__':
    app.run()