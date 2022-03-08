from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = "hello_world"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://minhduc@localhost/minhduc"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Integer, nullable=False)
    classes = db.relationship("Class", backref="classroom")

    @property
    def uid(self):
        return f"PH{self.id}"

    def __init__(self, capacity):
        self.capacity = capacity


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    classes = db.relationship("Class", backref="subject")

    @property
    def uid(self):
        return f"MH{self.id}"

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    subject_taught = db.Column(db.String(100), nullable=False)
    classes = db.relationship("Class", backref="teacher")

    @property
    def uid(self):
        return f"GV{self.id}"

    def __init__(self, first_name, last_name, subject_taught):
        self.first_name = first_name
        self.last_name = last_name
        self.subject_taught = subject_taught


# class_list = db.Table("class_list",
#     db.Column("student_id", db.Integer, db.ForeignKey("student.id")),
#     db.Column("class_id", db.Integer, db.ForeignKey("class.id"))                   
# )

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    # class_lists = db.relationship("ClassList")
    # studying = db.relationship("Class", secondary="class_list", backref="studier")

    @property
    def uid(self):
        return f"HS{self.id}"

    def __init__(self, first_name, last_name, date_of_birth=datetime.now()):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth


class ClassList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, nullable=False)
    classes = db.relationship("Class")


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classroom_id = db.Column(db.Integer, db.ForeignKey("classroom.id"))
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    class_list_id = db.Column(db.Integer, db.ForeignKey("class_list.id"))

    @property
    def uid(self):
        return f"LH{self.id}"
    def __init__(self, classroom_id, subject_id, teacher_id, class_list_id):
        self.classroom_id = classroom_id
        self.subject_id = subject_id
        self.teacher_id = teacher_id
        self.class_list_id = class_list_id


# db.drop_all()
# db.create_all()
