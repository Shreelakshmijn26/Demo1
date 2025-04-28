### STUDENT MANAGEMENT SYSTEM
This project is a python based application for managning student records.
It supports adding,viewing,deleting and updating of student data.
The zip folder have four files
   1. student_management.py         - The main application file containing:
                                         * The Student class for managing individual student information.
                                         * The StudentManagement class for handling operations like adding, viewing, updating, deleting, saving, and loading students.
    2. student.json                 - A JSON file used to store the student data.
    3. student_management_test.py   - A test file using python unittest to test the operations.
    4. .github\workflows\test.yml   - A github action workflow file to automate the tests.
## HOW TO RUN
1. Unzip folder
2. cd into folder
3. open the folder in vscode
4. python student_management.py (runs the main application)
5. python -m unittest student_management_test.py (to run the unittest program)
