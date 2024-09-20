from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import db
"""
#app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+cx_oracle://group:Password1@localhost:1521/management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
"""

class COURSE(db.Model):
    __tablename__ = 'COURSE'
    COURSE_ID = db.Column('COURSE_ID',db.Integer(),primary_key=True)
    COURSE_NAME = db.Column('COURSE_NAME',db.String(50),nullable=False)
    DEPARTMENT_ID = db.Column('DEPARTMENT_ID',db.Integer())

class DEPARTMENT(db.Model):
    __tablename__ = 'DEPARTMENT'
    DEPARTMENT_ID = db.Column('DEPARTMENT_ID',db.Integer(),primary_key=True)
    DEPARTMENT_NAME = db.Column('DEPARTMENT_NAME',db.String(50),nullable=False)
    LECTURER_ID = db.Column('LECTURER_NAME',db.Integer())

class EXAM (db.Model):
    __tablename__ = 'EXAM'
    EXAM_ID = db.Column('EXAM_ID',db.Integer(),primary_key=True)
    EXAM_NAME = db.Column('EXAM_NAME',db.String(50),nullable=False)
    UNIT_ID = db.Column('UNIT_ID',db.Integer())


class LECTURER(db.Model):
    __tablename__ = 'LECTURER'
    LECTURER_ID = db.Column('LECTURER_ID',db.Integer(),primary_key=True)
    LECTURER_NAME = db.Column('LECTURER_NAME',db.String(50),nullable=False)
    UNIT_ID = db.Column('UNIT_ID',db.Integer())
    DEPARTMENT_ID = db.Column('DEPARTMENT_ID',db.Integer())

class UNIT(db.Model):
    __tablename__ = 'UNIT'
    UNIT_ID = db.Column('UNIT_ID',db.Integer(),primary_key=True)
    UNIT_NAME = db.Column('UNIT_NAME',db.String(50),nullable=False)
    COURSE_ID = db.Column('COURSE_ID',db.Integer())

class STUDENT(db.Model):
    __tablename__ = 'STUDENT'
    USERNAME = db.Column('USERNAME',db.String(50), unique=True)
    STUDENT_ID = db.Column('STUDENT_ID',db.Integer(),primary_key=True)
    FIRST_NAME = db.Column('FIRST_NAME',db.String(50),nullable=False)
    LAST_NAME = db.Column('LAST_NAME',db.String(50),nullable=False)
    PASSWORD = db.Column('PASSWORD',db.String(50),nullable=False)
    COURSE_ID = db.Column('COURSE_ID',db.Integer())
    UNIT_ID = db.Column('UNIT_ID',db.Integer())

class RESULTS(db.Model):
    __tablename__ = 'RESULTS'
    RESULTS_ID = db.Column('RESULTS_ID',db.Integer(),primary_key=True)
    STUDENT_ID = db.Column('STUDENT_ID',db.Integer(),nullable=False)
    EXAM_ID = db.Column('EXAM_ID',db.Integer())
    CAT_1 = db.Column('CAT_1',db.Integer())
    CAT_2 = db.Column('CAT_2',db.Integer())
    CAT_3 = db.Column('CAT_3',db.Integer())
    EXAM_MARKS = db.Column('EXAM_MARKS',db.Integer())
    GRADE  = db.Column('GRADE',db.String(50))