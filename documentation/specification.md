# Software Requirements Specification
>Web-application allows users to view information about departments and employees.

_Application should provide:_

 - Display list of employees of current department
 - Display a list of departments and the average salary for these departments
 - Display a list of employees in the departments with an indication of the salary for each 
   employee
 - The search field to search for employees born on a certain date 
   or in the period between dates
 - Updating the list of departments (add / edit / delete)
 - Updating the list of employees (add / edit / delete)

##1. Departments
###1.1 Display list of departments
The mode is designed to view the list of departments.<br>

_**Main scenario:**_
 - _Application displays list of departments_

![View the list](./images%20for%20srs/d1.1.png)
   Pic. 1.1 View the list<br>

_**The list displays the following columns:<br>**_
 - `#`– sequence integer number 
 - Name of department – name of current department, link for displaying  all employees  of current department
 - Average salary – contains  value of average salary of all employees of current department
 - Action – contains two buttons – 'Edit' and 'Delete'<br>
###1.2 Add new department
**_Main scenario:_**<br>
 - User clicks the “Add new department” button in the main page
 - Button opens modal form for entering  department name
 - If any data is entered incorrectly, warning messages is displaying
 - If entered data is valid, then record is adding to database
 - If error occurs, then error message is displaying
 - If new record is successfully added, then list of departments is displaying

![pic](./images%20for%20srs/d1.2.png)
Pic. 1.2 'Add new department' button

![pic](./images%20for%20srs/d1.2.1.png)
Pic.1.2.1 Modal window

When adding a new department, the following data must be entered:
 - Department name – text field
###1.3 Edit department
_**Main scenario:**_<br>
 - User clicks the “Edit” button in the orders list view mode;
 - Application displays form to enter new department name
 - User enters data and click on the “Edit department” button
 - The field 'Name' displays the current department's name
 - If any data isn't entered unique, incorrect data messages are displayed
 - If entered data is valid, then edited data is added to database
 - If error occurs, then error message is displaying

_**Cancel operation scenario:**_<br>
 - User clicks the “Edit” button
 - Application displays form to entering a new data
 - Press the 'Close' button for closing modal window

![](./images%20for%20srs/d1.3.jpg)
Pic. 1.3 Edit department

When editing a department's name, the following data are entered:
 - Name – departments name

>**Constraints for a data validation:**<br>
> - Name– maximum length of 30 characters

###1.4 Removing the department
_**Main scenario:**_

 - The user, while in the list of departments, presses the "Delete" button in the selected order line
 - If the department can be removed, a confirmation dialog is displayed
 - The user confirms the removal of the order
 - Record is deleted from database

![](./images%20for%20srs/d1.4.png)
Pic. 1.4 Delete order dialog

_**Cancel operation scenario:**_
 - User clicks the “Delete” button
 - Application displays form to entering a new data
 - Press the 'Close' button for closing modal window

##2. Employee
###2.1 Display list of employees
This mode is intended for viewing and editing the list of employees
_**Main scenario:**_
 - User click on a name of department on the main page
 - Application displays list of all employees of current department

![](./images%20for%20srs/empl_main%20(2).png)
Pic 2.1 View the employees

The list displays the following columns:

 - "#"– sequence number
 - First name – employee’s first name
 - Last name – employee’s last name
 - Middle name - employee’s middle name
 - Birthdate – employee’s birthdate
 - Salary – employee's salary
 - Department – employee's working department
 - Action – contains two buttons – 'Edit' and 'Delete'<br> 

Filtering by date:
 - Search field to search for employees born on a certain date or in the period between dates 
 - The application will show the employees only for a certain period of time

###2.2 Add employee
Main scenario:
 - User press the “Add new employee” button in the employees page
 - Application displays form to enter employee's data
 - User enters employee’s data and click  “Add new employee” button
 - If any data is entered incorrectly, incorrect data messages  are displayed
 - If entered data is valid, then record is adding to database
 - If error occurs, then error message is displaying
 - If new client record is successfully added, then list of clients with added records is displaying

![](./images%20for%20srs/d2.2.png)
Pic. 2.2 Add employee

**When adding a client, the following data are entered:**
 - First name – employee's first name
 - Last name – employee's last name
 - Middle name - employee’s middle name
 - Birthday –  employee’s date of birth
 - Salary – employee's salary
 - Department - employee's department

>**Constraints for data validation:**
 >- First name – maximum length of 50 characters
 >- Last name – maximum length of 50 characters
 >- Middle name - maximum length of 50 characters
 >- Birthday –  employee’s date of birth in format dd/mm/yyyy
 >- Salary – float value
 >- Department – uuid value of related department id

###2.3 Edit employee
Main scenario:
 - User clicks the “Edit” button in the list  of employees 
 - Application displays form to enter new employee data
 - Application displays  in the form of entering a new data,  current data
 - User enters employee’s data and presses “Edit employee” button
 - If any data is entered incorrectly, incorrect data messages are displayed
 - If entered data is valid, then edited data is added to database
 - If an error occurs, then error message is displaying
 - If a record is successfully edited, then a list of employees with added records is displaying

###2.4 Removing employee
Main scenario:
 - The user, while in the list of employees mode, presses the "Delete" button in the selected employee line;
 - Application displays confirmation dialog “Please confirm delete employee?”;
 - The user confirms the removal of the employee;
 - Record is deleted from database;
 - If an error occurs, then error message displays;
 - If an employee record is successfully deleted, then a list of employees without deleted records is displayed.
