from re import sub
from flask import render_template, request, url_for, redirect, flash
from database import *
from loguru import logger


logger.add("log.txt")
@app.route("/")
@app.route("/home")
def trang_chu():
    logger.info("Requested to Homepage")
    return render_template("home.html", title="Home")


@app.route("/classroom")
def lop_hoc():
    classrooms = Classroom.query.all()
    return render_template("classroom.html", classrooms=classrooms, title="Classroom")

@app.route("/classroom/insert", methods=["POST"])
def insert_lop_hoc():
    if request.method == "POST":
        capacity = request.form["capacity"]

        classroom_insert = Classroom(capacity)
        db.session.add(classroom_insert)
        db.session.commit()

        flash("Successed!")

        logger.info(f"Classroom PH{Classroom.query.filter_by(capacity=capacity).all()[-1].id}: inserted!")
        return redirect(url_for("lop_hoc"))

@app.route("/classroom/update", methods=["GET","POST"])
def update_lop_hoc():
    
    if request.method == "POST":
        edit_classroom = Classroom.query.get(request.form.get("id"))

        edit_classroom.capacity = request.form["capacity"]

        db.session.commit()
    
        flash("Successed!")

        logger.info(f"Classroom PH{edit_classroom.id}: updated!")
        return redirect(url_for("lop_hoc"))
    
@app.route("/classroom/delete/<id>/", methods=["GET", "POST"])
def delete_lop_hoc(id):
    del_classroom = Classroom.query.get(id)
    db.session.delete(del_classroom)
    db.session.commit()

    flash("Deleted!")

    logger.info(f"Classroom PH{del_classroom.id}: deleted!")
    return redirect(url_for("lop_hoc"))


@app.route("/student")
def hoc_sinh():
    students = Student.query.all()
    classlists = ClassList
    
    return render_template("student.html", students=students, classlists=classlists)

@app.route("/student/insert", methods=["POST"])
def insert_hoc_sinh():
    if request.method == "POST":
        classroom_list_id = Classroom.query.with_entities(Classroom.id).all()
        a = [i[0] for i in classroom_list_id]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        date_of_birth = request.form["date_of_birth"]
        classroom_id = request.form["classroom_id"]
        if int(classroom_id) in a:
            classlist = ClassList(student_id=classroom_id)
            db.session.add(classlist)
        else:
            raise

        subject_insert = Student(first_name, last_name, date_of_birth)
        db.session.add(subject_insert)
        db.session.commit()

        flash("Successed!")
        
        logger.info(f"""Classroom HS{Student.query.filter_by(first_name=first_name,
                    last_name=last_name,date_of_birth=date_of_birth).all()[-1].id}: inserted!""")
        return redirect(url_for("hoc_sinh"))

@app.route("/student/update", methods=["POST"])
def update_hoc_sinh():
    if request.method == "POST":
        edit_student= Student.query.get(request.form.get("id"))
        edit_class_list = ClassList.query.get(request.form.get("id"))
        classroom_list_id = Classroom.query.with_entities(Classroom.id).all()
        a = [i[0] for i in classroom_list_id]
        edit_student.first_name = request.form["first_name"]
        edit_student.last_name = request.form["last_name"]
        edit_student.date_of_birth = request.form["date_of_birth"]
        classroom_id = request.form["classroom_id"]
        if int(classroom_id) in a:
            edit_class_list.student_id = request.form["classroom_id"]
        else:
            raise
        db.session.commit()
    
        flash("Successed!")

        logger.info(f"Classroom HS{edit_student.id}: updated!")
        return redirect(url_for("hoc_sinh"))
    
@app.route("/student/delete/<id>/", methods=["GET", "POST"])
def delete_hoc_sinh(id):
    del_student = Student.query.get(id)
    del_class_list = ClassList.query.get(id)
    
    db.session.delete(del_student)
    db.session.delete(del_class_list)
    db.session.commit()

    flash("Deleted!")

    logger.info(f"Classroom HS{del_student.id}: deleted!")
    return redirect(url_for("hoc_sinh"))
    
@app.route("/subject")
def mon_hoc():
    subjects = Subject.query.all()
    return render_template("subject.html", subjects=subjects, title="Subject")

@app.route("/subject/insert", methods=["POST"])
def insert_mon_hoc():
    if request.method == "POST":
        name = request.form["name"]
        capacity = request.form["capacity"]

        subject_insert = Subject(name, capacity)
        db.session.add(subject_insert)
        db.session.commit()

        flash("Successed!")

        logger.info(f"Classroom MH{Subject.query.filter_by(name=name, capacity=capacity).all()[-1].id}: inserted!")
        return redirect(url_for("mon_hoc"))

@app.route("/subject/update", methods=["GET","POST"])
def update_mon_hoc():
    
    if request.method == "POST":
        edit_subject = Subject.query.get(request.form.get("id"))

        edit_subject.name = request.form["name"]
        edit_subject.capacity = request.form["capacity"]

        db.session.commit()
    
        flash("Successed!")
        
        logger.info(f"Classroom MH{edit_subject.id}: updated!")
        return redirect(url_for("mon_hoc"))
    
@app.route("/subject/delete/<id>/", methods=["GET", "POST"])
def delete_mon_hoc(id):
    del_subject = Subject.query.get(id)
    db.session.delete(del_subject)
    db.session.commit()

    flash("Deleted!")

    logger.info(f"Classroom MH{del_subject.id}: deleted!")
    return redirect(url_for("mon_hoc"))

@app.route("/teacher")
def giao_vien():
    teachers = Teacher.query.all()
    return render_template("teacher.html", teachers=teachers, title="Teacher")

@app.route("/teacher/insert", methods=["POST"])
def insert_giao_vien():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        subject_taught = request.form["subject_taught"]
        teacher_insert = Teacher(first_name, last_name, subject_taught)
        db.session.add(teacher_insert)
        db.session.commit()

        flash("Successed!")

        logger.info(f"""Classroom GV{Teacher.query.filter_by(first_name=first_name,
                    last_name=last_name, subject_taught=subject_taught).all()[-1].id}: inserted!""")
        return redirect(url_for("giao_vien"))

@app.route("/teacher/update", methods=["GET","POST"])
def update_giao_vien():
    
    if request.method == "POST":
        edit_teacher = Teacher.query.get(request.form.get("id"))

        edit_teacher.first_name = request.form["first_name"]
        edit_teacher.last_name = request.form["last_name"]
        edit_teacher.subject_taught = request.form["subject_taught"]

        db.session.commit()
    
        flash("Successed!")

        logger.info(f"Classroom GV{edit_teacher.id}: updated!")

        return redirect(url_for("giao_vien"))
    
@app.route("/teacher/delete/<id>/", methods=["GET", "POST"])
def delete_giao_vien(id):
    del_teacher = Teacher.query.get(id)
    db.session.delete(del_teacher)
    db.session.commit()

    flash("Deleted!")

    logger.info(f"Classroom GV{del_teacher.id}: deleted!")
    return redirect(url_for("giao_vien"))
    
@app.route("/school")
def truong_hoc():
    classes = Class.query.all()
    classroom_count = Classroom.query.count()
    student_count = Student.query.count()
    subject_count = Subject.query.count()
    teacher_count = Teacher.query.count()
    classrooms = Classroom
    return render_template("school.html", classes=classes, title="School",
                           classroom_count=classroom_count, student_count=student_count,
                           subject_count=subject_count, teacher_count=teacher_count,
                           classrooms=classrooms)

@app.route("/school/insert", methods=["POST"])
def insert_truong_hoc():
    if request.method == "POST":
        classroom_id = request.form["class_list_id"]
        subject_id = request.form["subject_id"]
        teacher_id = request.form["teacher_id"]

        class_insert = Class(classroom_id, subject_id, teacher_id,classroom_id)
        db.session.add(class_insert)
        db.session.commit()

        flash("Successed!")

        logger.info(f"""Classroom LH{Class.query.filter_by(classroom_id=classroom_id,
                    subject_id=subject_id,teacher_id=teacher_id).all()[-1].id}: inserted!""")
        return redirect(url_for("truong_hoc"))

@app.route("/school/update", methods=["GET","POST"])
def update_truong_hoc():
    
    if request.method == "POST":
        edit_class = Class.query.get(request.form.get("id"))

        edit_class.class_list_id = int(request.form["class_list_id"])
        edit_class.subject_id = int(request.form["subject_id"])
        edit_class.teacher_id = int(request.form["teacher_id"])

        db.session.commit()
    
        flash("Successed!")

        logger.info(f"Classroom LH{edit_class.id}: updated!")
        return redirect(url_for("truong_hoc"))
    
@app.route("/school/delete/<id>/", methods=["GET", "POST"])
def delete_truong_hoc(id):
    del_class = Class.query.get(id)
    db.session.delete(del_class)
    db.session.commit()

    flash("Deleted!")

    logger.info(f"Classroom LH{del_class.id}: deleted!")
    return redirect(url_for("truong_hoc"))


