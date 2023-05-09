from sql_alchemy import db

class UserModel(db.Model):
    __tablename__ = 'suppliers'
    
    id: str = db.Column(db.String, primary_key=True)
    name: str = db.Column(db.String, nullable=False)
    cnpj: str = db.Column(db.String, nullable=False)
    
    
    def __init__(self, id, name, login, password, user_type):
        self.id = id
        self.name = name
        self.login = login
        self.password = password
        self.user_type = user_type
        self.is_active = True
        
    def json(self):
        return {
            'name': self.name,
            'login': self.login
        }
    
    
    @classmethod
    def find_user(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user
        return None

    
    @classmethod
    def change_password(cls, password):
        pass
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def deactivate_user(self):
        pass