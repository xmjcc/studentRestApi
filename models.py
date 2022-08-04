from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class StudentModel(db.Model):
    __tablename__="students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    date_birth = db.Column(db.String())
    amount_due = db.Column(db.String())



    def __init__(self, first_name,last_name,date_birth,amount_due):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
        self.amount_due = amount_due
    
    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"

