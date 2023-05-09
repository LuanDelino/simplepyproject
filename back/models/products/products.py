from sql_alchemy import db

class ProductModel(db.Model):
    __tablename__ = 'products'
    
    id: str = db.Column(db.String, primary_key=True)
    name: str = db.Column(db.String)
    price: float = db.Column(db.Float(precision=2))
    quantity: int = db.Column(db.Integer)
    supplier_id: str = db.Column(db.String, nullable=False)
    
    
    def __init__(self, id, name, price, quantity):
        self.id: str = id
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity
        
        
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity 
        }
        
        
    @classmethod
    def find_product(cls, product_id):
        product = cls.query.filter_by(id=product_id).first()
        
        if product:
            return product
        return None
    
    
    def delete_product(self):
        db.session.delete(self)
        db.session.commit()
    
    
    def update_product(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
    def save(self):
        db.session.add(self)
        db.session.commit()