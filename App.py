from flask import Flask
from const import SECRET_KEY
from flask import request, render_template, flash, redirect, url_for
from service.db_service import *
import decimal

app = Flask(__name__)
app.secret_key = SECRET_KEY


def average_sal_count(ind):
    temp = dml_select_Empl_all_sal(ind)
    numerator = sum(tuple(map(lambda i: i.salary, temp)))
    denominator = len(temp)
    if not denominator:
        return 0
    return f'{numerator / denominator:.2f}'


@app.route('/')
def index():
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
    staff_temp = dml_select_Empl_all(dep_id)
    staff = {}
    for i in staff_temp:
        staff[i[0][0]] = {
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
    temp = data.split('-')

    return tuple(map(int, temp))


# this route is for inserting data to mysql
# database via html forms
@app.route('/insert_empl', methods=['POST'])
def insert_empl():
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

        # flash("Employee inserted successfully
        _temp = request.root_url

        return redirect(f'{_temp}select/{related_department}')


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']

        dml_insert_Dep(name)

        # flash("Department inserted successfully")

        return redirect(url_for('index'))


# this is our update route where we are going
# to update our employee
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        condition = ('id', request.form.get('id'))
        checked_data = dml_select_Dep_cur(condition)[0][0].__dict__
        print(checked_data)
        for attr in checked_data:
            temp = request.form.get(attr)
            if temp:
                if checked_data[attr] != temp:
                    dml_update_Dep(condition, (attr, temp))

        # flash("Department updated successfully")

        return redirect(url_for('index'))


@app.route('/update_empl', methods=['GET', 'POST'])
def update_empl():
    if request.method == 'POST':
        temp_id = request.form.get('related_department')
        condition = ('id', request.form.get('id'))
        checked_data = dml_select_Empl_cur(condition)[0][0].__dict__
        for attr in checked_data:
            temp = request.form.get(attr)
            if temp:
                if checked_data[attr] != temp:
                    dml_update_Empl(condition, (attr, temp))

        # flash("Employee updated successfully")

        return redirect(url_for('index_empl',
                                dep_id=checked_data.get('related_department')))


# This route is for deleting our employee
@app.route('/delete_dep/<id>/', methods=['GET', 'POST'])
def delete_item(id):
    dml_delete_Dep(id)
    # flash("Department deleted successfully")

    return redirect(url_for('index'))


@app.route('/delete_empl/<id>/<dep_item>', methods=['GET', 'POST'])
def delete_person(id, dep_item):
    dml_delete_Empl(('id', id))
    # flash("Employee deleted successfully")

    return redirect(url_for('index_empl', dep_id=dep_item))


if __name__ == '__main__':
    app.run()
