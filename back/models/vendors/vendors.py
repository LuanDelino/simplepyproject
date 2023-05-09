from sql_alchemy import db

class UserModel(db.Model):
    __tablename__ = 'vendors'
    
    id: str = db.Column(db.String, primary_key=True)
    supplier_id: str = db.Column(db.String, nullable=False)
    name: str = db.Column(db.String, nullable=False)
    phone: str = db.Column(db.String, nullable=False)
    
    def __init__(self, id, name, supplier_id, phone):
        self.id = id
        self.name = name
        self.supplier_id = supplier_id
        self.phone = phone
        
    def json(self):
        return {
            'name': self.name,
            'phone': self.phone
        }
    
    
    @classmethod
    def find_vendor(cls, name):
        vendor = cls.query.filter_by(name=name).first()
        if vendor:
            return vendor
        return None
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        