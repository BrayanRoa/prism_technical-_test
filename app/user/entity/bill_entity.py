from app.db import db
from sqlalchemy.orm import mapper
from ..model.bill_dto import BillDTO

class BillEntity(db.Model):
    
    __tablename__ = "bill"
    
    id = db.Column(db.Integer, primary_key=True)
    date_bill = db.Column(db.Date)
    value = db.Column(db.Numeric(9))
    type = db.Column(db.Integer)
    observation = db.Column(db.String(120))
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("UserEntity", back_populates="bill")
    
    def start_mapper():
        mapper(BillDTO, BillEntity)