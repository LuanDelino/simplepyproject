from sql_alchemy import db
from datetime import datetime
import pytz

tz = pytz.timezone('America/Sao_Paulo')


class ProductLogModel(db.Model):
    __tablename__ = 'products_log'
    
    id: str = db.Column(db.String, primary_key=True)
    product_id: str = db.Column(db.String)
    modify_user: str = db.Column(db.String, nullable=False)
    modify_date: str = db.Column(db.DateTime, nullable=False, default=datetime.now(tz))
    changelog: str = db.Column(db.String, nullable=False)
    
    
    def __init__(self, id, product_id, modify_user, changelog):
        self.id: str = id
        self.product_id: str = product_id
        self.modify_user = modify_user
        self.changelog = changelog
        
    def json(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'user': self.modify_user,
            'date': self.modify_date,
            'changelog': self.changelog
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        