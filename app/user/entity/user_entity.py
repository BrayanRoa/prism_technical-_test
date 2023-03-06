from app.db import db


class UserEntity(db.Model):
    
    __tablename__="users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    passw = db.Column(db.String(500))
    email = db.Column(db.String(100), unique=True)
    
    bill = db.relationship("BillEntity", back_populates="user")
    
