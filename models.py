from extensions import db

# Schema that mimic the db , Using this we will interact with our Database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True) # Avoid duplicate
    password = db.Column(db.String(200))
    age = db.Column(db.Integer)
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))
    zip = db.Column(db.String(20))
    company = db.Column(db.String(100))
    web = db.Column(db.String(100))