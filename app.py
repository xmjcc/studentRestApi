from flask import Flask, render_template, request, redirect
from models import db, StudentModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATcIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()


@app.route('/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
        
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        date_birth = request.form['date_birth']
        amount_due = request.form['amount_due']

        students = StudentModel (
            first_name=first_name,
            last_name=last_name,
            date_birth=date_birth,
            amount_due=amount_due

        )
        db.session.add(students)
        db.session.commit()
        return redirect('/')

@app.route('/', methods = ['GET'])
def RetriveList():
    students = StudentModel.query.all()
    return render_template('index.html', students = students)

@app.route('/<int:id>/delete', methods = ['GET','POST'])

def delete(id):
    students = StudentModel.query.filter_by(id=id).first()
    if request.method == 'POST':

        if students:
           db.session.delete(students)
           db.session.commit()
           return redirect('/')
        abort(404)
     # return redirect('/)   
    return render_template('delete.html')


@app.route('/<int:id>/edit', methods = ['GET','POST'])

def update(id):
    student = StudentModel.query.filter_by(id=id).first()

    if request.method == 'POST':
        

        if student:
            db.session.delete(student)
            db.session.commit()

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        date_birth = request.form['date_birth']
        amount_due = request.form['amount_due']

        student = StudentModel (
            first_name=first_name,
            last_name=last_name,
            date_birth=date_birth,
            amount_due=amount_due

        

        )
        db.session.add(student)
        db.session.commit()
        return redirect('/')
        return f"Student with id = {id} Does not exist"
    
    return render_template('update.html', student=student)






app.run(host = 'localhost', port=5000)