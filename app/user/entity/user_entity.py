from app.db import db
from sqlalchemy.orm import mapper
from ..model.user_dto import UserDTO
from werkzeug.security import check_password_hash, generate_password_hash


class UserEntity(db.Model):
    
    __tablename__="users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    passw = db.Column('pass',db.String(500))
    email = db.Column(db.String(100), unique=True)
    
    bill = db.relationship("BillEntity", back_populates="user")
    
    def start_mapper():
        mapper(UserDTO, UserEntity)
        
    @classmethod    
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)