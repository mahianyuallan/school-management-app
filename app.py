from flask import Flask, render_template , redirect , session , request ,url_for
from datetime import datetime
# from models import db

from db import db

from models import COURSE, DEPARTMENT, STUDENT, UNIT, EXAM , LECTURER , STUDENT
import cx_Oracle
import config as cg



app = Flask(__name__)
app.secret_key ='lumber jack'
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://SYSTEM:Password1@localhost:1521/orcl'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://group:Password1@localhost:1521/management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Initialize the db with the app


def execute_sql_script(script_path):
    # Connect to the database
    connection = cx_Oracle.connect('SYSTEM', 'Password1', 'localhost:1521/orcl')
    cursor = connection.cursor()

    # Read the SQL script
    with open(script_path, 'r') as file:
        sql_script = file.read()

    # Execute the SQL script
    try:
        cursor.execute(sql_script)
        connection.commit()  # Commit changes
    except cx_Oracle.DatabaseError as e:
        print(f"Error executing script: {e}")
    finally:
        cursor.close()
        connection.close()


# DELETE CODES | easy way

#Course delete
def delete_course(Cname):
    if Cname:
        val = db.session.query(COURSE).filter(COURSE.COURSE_NAME == Cname ).delete()
        db.session.commit()
        return 'Course delete successful'
    else:
        return 'Enter valid details'

#Department delete
def delete_department(Dname):
    if Dname:
        val = db.session.query(DEPARTMENT).filter(DEPARTMENT.DEPARTMENT_NAME == Dname).delete()
        db.session.commit()
        return 'department delete successful'
    else:
        return 'Enter valid details'




    Stud = STUDENT(USERNAME= 'LEON05',FIRST_NAME='LEON',LAST_NAME='Njoroge',COURSE_ID=2,UNIT_ID=3)
    db.session.add(Stud)

#Lecturer delete
def delete_lecturer(Lname):
    if Lname:
        val = db.session.query(LECTURER).filter(LECTURER.LECTURER_NAME == Lname ).delete()
        db.session.commit()
        return 'lecturer delete successful'
    else:
        return 'Enter valid details'

#Unit delete
def delete_unit(Uname):
    if Uname:
        val = db.session.query(UNIT).filter(UNIT.UNIT_NAME == Uname ).delete()
        db.session.commit()
        return 'unit delete successful'
    else:
        return 'Enter valid details'

#Exam delete
def delete_exam(Ename):
    if Ename:
        val = db.session.query(EXAM).filter(EXAM.EXAM_NAME == Ename ).delete()
        db.session.commit()
        return 'exam delete successful'
    else:
        return 'Enter valid details'

#Student delete
def delete_student(Sname):
    if Sname:
        val = db.session.query(STUDENT).filter(STUDENT.USERNAME == Sname ).delete()
        db.session.commit()
        return 'student delete successful'
    else:
        return 'Enter valid details'

#Restult delete
def delete_results(Rid):
    if Rid:
        val = db.session.query(RESULTS).filter(RESULTS.RESULTS_ID == Rid ).delete()
        db.session.commit()
        return 'result delete successful'
    else:
        return 'Enter valid details'


# INSERT CODES | easy + hard way

#insert exams (Not complete)
def insert_exams(EXAM_NAME,UNIT_ID):
    if EXAM_NAME and UNIT_ID :
        sql = 'INSERT INTO EXAM (EXAM_NAME,UNIT_ID)' \
              ' VALUES (:EXAM_NAME,:UNIT_ID)'
        try:
            with cx_Oracle.connect(cg.name,cg.password,cg.host) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql,[EXAM_NAME,UNIT_ID])
                    connection.commit()
        except cx_Oracle.Error as error:
            print(error)
            return 1
    else:
        return 2

#insert department
def insert_department(DEPARTMENT_NAME):
    if DEPARTMENT_NAME:
        sql = 'INSERT INTO DEPARTMENT (DEPARTMENT_NAME) VALUES (:DEPARTMENT_NAME)'
        try:
            with cx_Oracle.connect(cg.name, cg.password, cg.host) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql, [DEPARTMENT_NAME])
                    connection.commit()
        except cx_Oracle.Error as error:
            print(error)
    else:
        return 'Enter valid inputs'

#insert course
def insert_course(COURSE_NAME,DEPARTMENT_ID):
    if COURSE_NAME and DEPARTMENT_ID:
        sql = 'INSERT INTO COURSE (COURSE_NAME,DEPARTMENT_ID) VALUES (:COURSE_NAME,:DEPARTMENT_ID)'
        try:
            with cx_Oracle.connect(cg.name,cg.password,cg.host) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql,[COURSE_NAME,DEPARTMENT_ID])
                    connection.commit()
        except cx_Oracle.Error as error:
            print(error)
    else:
        return 'Enter valid inputs'

#insert lec
def insert_lecturer(LECTURER_NAME,UNIT_ID,DEPARTMENT_ID):
    if LECTURER_NAME and UNIT_ID and DEPARTMENT_ID:
        lec = LECTURER(LECTURER_NAME = LECTURER_NAME,UNIT_ID = UNIT_ID,DEPARTMENT_ID = DEPARTMENT_ID)
        db.session.add(lec)
        db.session.commit()

    else:
        return 'Enter valid details'

#insert student
def insert_student(USERNAME,FIRST_NAME,LAST_NAME,COURSE_ID,UNIT_ID,PASSWORD):
    if USERNAME and FIRST_NAME and LAST_NAME and COURSE_ID and UNIT_ID and PASSWORD:
        stud = STUDENT(USERNAME = USERNAME, FIRST_NAME = FIRST_NAME, LAST_NAME = LAST_NAME,
                       COURSE_ID = COURSE_ID, UNIT_ID=UNIT_ID,PASSWORD = PASSWORD )
        db.session.add(stud)
        db.session.commit()

    else:
        return 'Enter valid details'

#insert unit
def insert_unit(UNIT_NAME,COURSE_ID):
    if UNIT_NAME and COURSE_ID:
        uni = UNIT(UNIT_NAME = UNIT_NAME,COURSE_ID = COURSE_ID)
        db.session.add(uni)
        db.session.commit()

    else:
        return 'Enter valid details'

#insert results
def insert_results(STUDENT_ID,EXAM_ID,CAT_1,CAT_2,CAT_3,EXAM_MARKS):
    if STUDENT_ID :
        sql = 'INSERT INTO RESULTS (STUDENT_ID,EXAM_ID,CAT_1,CAT_2,CAT_3,EXAM_MARKS)' \
              ' VALUES (:STUDENT_ID,:EXAM_ID,:CAT_1,:CAT_2,:CAT_3,:EXAM_MARKS)'
        try:
            with cx_Oracle.connect(cg.name,cg.password,cg.host) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql,[STUDENT_ID,EXAM_ID,CAT_1,CAT_2,CAT_3,EXAM_MARKS])
                    connection.commit()
        except cx_Oracle.Error as error:
            print(error)
            return 1
    else:
        return 2


# UPDATE CODES (not done yet)



#SIGN UP AND LOG IN CODE | easy+hard way  (*Still faulty)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods = ['POST','GET'])
def registration():
    if request.method == 'POST':
        USERNAME = request.form["USERNAME"]
        FIRST_NAME = request.form["FIRST_NAME"]
        LAST_NAME = request.form["LAST_NAME"]
        COURSE_ID = request.form['COURSE_ID']
        UNIT_ID = request.form['UNIT_ID']
        PASSWORD = request.form['PASSWORD']
        existing_user = db.session.query(STUDENT).filter(STUDENT.USERNAME == USERNAME).first()

        if existing_user is None:
            val = {"USERNAME":USERNAME,"FIRST_NAME":FIRST_NAME,"LAST_NAME":LAST_NAME,
                       "COURSE_ID":COURSE_ID,"UNIT_ID":UNIT_ID,"PASSWORD":PASSWORD}

            sql = 'INSERT INTO STUDENT (USERNAME, FIRST_NAME,LAST_NAME,COURSE_ID,UNIT_ID,PASSWORD) ' \
                      'VALUES (:USERNAME,:FIRST_NAME,:LAST_NAME,:COURSE_ID,:UNIT_ID,:PASSWORD)'
            try:
                    with cx_Oracle.connect(cg.name,cg.password,cg.host) as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(sql,val)
                            connection.commit()
                        word = "REGISTRATION SUCCESSFULL "
                        return render_template('registration.html', word=word)
            except cx_Oracle.Error as error:
                    fail = "REGISTRATION UNSUCCESSFULL PLEASE TRY AGAIN"
                    print(error)
                    return render_template('registration.html',fail= fail)
        else:
            userex = 'User already exists'
            return render_template('registration.html', userex=userex)
    return render_template("registration.html")

"""
#Login working but enable and fix user session
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        USERNAME = request.form["USERNAME"]
        PASSWORD = request.form["PASSWORD"]
        adm = "admin"
        pws = "admin"
        if  USERNAME == adm  and  PASSWORD== pws:
            session['name'] = request.form['USERNAME']
            return render_template('admin.html', user=session['name'])

        else:
            try:

                find = db.session.query(STUDENT).filter(STUDENT.USERNAME == USERNAME and STUDENT.PASSWORD == PASSWORD).first()

                if find != None:
                    session["name"] = request.form['USERNAME']
                    return render_template('student.html', user=session['name'])


            except:
                error = "Sign up first"
                return render_template('login.html', error=error)
    return  render_template('login.html')

"""


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        USERNAME = request.form["USERNAME"]
        PASSWORD = request.form["PASSWORD"]
        adm = "admin"
        pws = "admin"

        # Check if the user is admin
        if USERNAME == adm and PASSWORD == pws:
            session['name'] = USERNAME
            return render_template('admin.html', user=session['name'])

        try:
            # Correct the query logic using `==` instead of `and`
            find = db.session.query(STUDENT).filter(
                STUDENT.USERNAME == USERNAME,
                STUDENT.PASSWORD == PASSWORD
            ).first()

            # Check if the student is found
            if find:
                session['name'] = USERNAME
                return render_template('student.html', user=session['name'])
            else:
                error = "Invalid username or password"
                return render_template('login.html', error=error)

        except Exception as e:
            error = str(e)  # Capture the specific exception message
            return render_template('login.html', error=error)

    return render_template('login.html')




@app.route('/checkresults',methods=['POST','GET'])
def checkresults():
    USER = session['name']
    if request.method == 'POST':
        if  USER == "admin":
            STUDENT_ID = request.form['STUDENT_ID']
            USERNAME = request.form['USERNAME']
            sql = 'SELECT S.USERNAME,S.FIRST_NAME,S.STUDENT_ID,R.CAT_1,R.CAT_2,R.CAT_3,R.EXAM_MARKS,R.GRADE ' \
                  'FROM STUDENT S JOIN RESULTS R ' \
                  'ON S.STUDENT_ID = R.STUDENT_ID ' \
                  'WHERE S.USERNAME =:USERNAME AND S.STUDENT_ID =:STUDENT_ID'

            try:
                with cx_Oracle.connect(cg.name, cg.password, cg.host) as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(sql, [USERNAME,STUDENT_ID])
                        row = cursor.fetchone()
                        if row:
                            student_results = row
                            return render_template('report.html', student_results = student_results)
            except cx_Oracle.Error as error:
                return render_template('report.html', error=error)
        else:
                sql = 'SELECT * FROM STUDENT_RESULTS WHERE USERNAME=:USER'

                try:
                    with cx_Oracle.connect(cg.name, cg.password, cg.host) as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(sql, [USER])
                            row = cursor.fetchone()
                            if row:
                                student_results = row
                                return render_template('/report.html', student_results = student_results)
                            else:
                                 student_results = 'Your Results are not out yet. Please check again later'
                                 return render_template('/report.html', student_results = student_results)
                except cx_Oracle.Error as error:
                    return render_template('/report.html', error=error)
        err ="Nothing happened"
        return render_template('/report.html',err = err)
    error = "It has refused"
    return render_template('enterexams.html',error = error)




#@app.route for Editing values in db (INSERT, DELETE)

@app.route('/edexam',methods=['POST','GET'])
def edexam():
    if request.method == 'POST':
        ACTION = request.form['ACTION']
        EXAM_NAME = request.form['EXAM_NAME']
        UNIT_ID = request.form['UNIT_ID']
        
        if ACTION == 'INSERT':
            val = insert_exams(EXAM_NAME,UNIT_ID)
            if val == 1:
                msg = 'YOUR HAVE SUCCESSFULLY ENTERED EXAMS'
            elif val == 2:
                msg = 'AN ERROR HAS OCCURED PLEASE TRY AGAIN'
        elif ACTION == 'DELETE':
            val = delete_exam(EXAM_NAME)


    return render_template('adminedit.html')

@app.route('/edlec',methods=['POST','GET'])
def edlec():
    if request.method== 'POST':
        ACTION = request.form['ACTION']
        LECTURER_NAME = request.form['LECTURER_NAME']
        UNIT_ID = request.form['UNIT_ID']
        DEPARTMENT_ID = request.form['DEPARTMENT_ID']
        if ACTION == 'INSERT':
            val = insert_lecturer(LECTURER_NAME,UNIT_ID,DEPARTMENT_ID)
            if val == 1:
                msg = 'YOUR HAVE SUCCESSFULLY ENTERED EXAMS'
            elif val ==2:
                msg = 'AN ERROR HAS OCCURED PLEASE TRY AGAIN'
        elif ACTION =='DELETE':
            val = delete_lecturer(LECTURER_NAME)
    return render_template('adminedit.html')

@app.route('/edcourse',methods=['POST','GET'])
def edcourse():
    if request.method == 'POST':
        ACTION = request.form['ACTION']
        COURSE_NAME = request.form['COURSE_NAME']
        DEPARTMENT_ID = request.form['DEPARTMENT_ID']
        if ACTION == 'INSERT':
            val = insert_course(COURSE_NAME, DEPARTMENT_ID)
            if val == 1:
                msg = 'YOUR HAVE SUCCESSFULLY ENTERED EXAMS'
            elif val ==2:
                msg = 'AN ERROR HAS OCCURED PLEASE TRY AGAIN'
        elif ACTION == 'DELETE':
            val = delete_course(COURSE_NAME)

    return render_template('adminedit.html')

@app.route('/edunit',methods=['POST','GET'])
def edunit():
    if request.method == 'POST':
        ACTION = request.form ['ACTION']
        UNIT_NAME = request.form['UNIT_NAME']
        COURSE_ID = request.form['COURSE_ID']
        if ACTION == 'INSERT':
            val = insert_unit(UNIT_NAME,COURSE_ID)
            if val == 1:
                msg = 'YOUR HAVE SUCCESSFULLY ENTERED EXAMS'
            elif val ==2:
                msg = 'AN ERROR HAS OCCURED PLEASE TRY AGAIN'

        elif ACTION == 'DELETE':
            val = delete_unit(UNIT_NAME)
        
    return render_template('adminedit.html')


@app.route('/eddept', methods=['POST', 'GET'])
def eddept():
    if request.method == 'POST':
        ACTION = request.form['ACTION']
        DEPARTMENT_NAME = request.form['DEPARTMENT_NAME']
        if ACTION == 'INSERT':
            val = insert_department(DEPARTMENT_NAME)
            if val == 1:
                msg = 'YOUR HAVE SUCCESSFULLY ENTERED EXAMS'
            elif val == 2:
                msg = 'AN ERROR HAS OCCURED PLEASE TRY AGAIN'
        elif ACTION == 'DELETE':
            val = delete_department(DEPARTMENT_NAME)

    return render_template('adminedit.html')


@app.route('/edstud',methods = ['POST','GET'])
def edstud():
    if request.method== 'POST':
        ACTION = request.form['ACTION']
        USERNAME = request.form["USERNAME"]
        FIRST_NAME = request.form["FIRST_NAME"]
        LAST_NAME = request.form["LAST_NAME"]
        PASSWORD= request.form["PASSWORD"]
        COURSE_ID = request.form['COURSE_ID']
        UNIT_ID = request.form['UNIT_ID']
        if ACTION == 'INSERT':
            
            val = insert_student(USERNAME,FIRST_NAME,LAST_NAME,COURSE_ID,UNIT_ID,PASSWORD)
            if val == 1:
                msg = 'YOUR HAVE SUCCESSFULLY ENTERED EXAMS'
            elif val ==2:
                msg = 'AN ERROR HAS OCCURED PLEASE TRY AGAIN'
        elif ACTION == 'DELETE':
            val = delete_student(USERNAME)
    return render_template('adminedit.html')


@app.route('/edresults',methods=['POST','GET'])
def edresults():
    if request.method == 'POST':
        ACTION = request.form['ACTION']
        RESULT_ID = request.form['RESULT_ID']
        STUDENT_ID = request.form['STUDENT_ID']
        EXAM_ID = request.form['EXAM_ID']
        CAT_1 = request.form['CAT_1']
        CAT_2 = request.form['CAT_2']
        CAT_3 = request.form['CAT_3']
        EXAM_MARKS = request.form['EXAM_MARKS']
        if ACTION == 'INSERT':
            val = insert_results(STUDENT_ID,EXAM_ID,CAT_1,CAT_2,CAT_3,EXAM_MARKS)
            if val == 1:
                msg = 'YOUR HAVE SUCCESSFULLY ENTERED EXAMS'
            elif val ==2:
                msg = 'AN ERROR HAS OCCURED PLEASE TRY AGAIN'
        elif ACTION == 'DELETE':
            val = delete_results(RESULT_ID)


    return render_template('adminedit.html')

@app.route('/adminedit')
def adminedit():
    return render_template('/adminedit.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')

@app.route('/logout')
def logout():
	session.pop('name', None  )
	return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug = False)




