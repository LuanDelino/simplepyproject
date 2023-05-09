from sql_alchemy import db

class UserModel(db.Model):
    __tablename__ = 'users'
    
    id: str = db.Column(db.String, primary_key=True)
    name: str = db.Column(db.String, nullable=False)
    login: str = db.Column(db.String, nullable=False, unique=True)
    identification: str= db.Column(db.String, nullable=False)
    password: str = db.Column(db.String, nullable=False)
    user_type: int = db.Column(db.Integer, nullable=False)
    is_active: bool = db.Column(db.Boolean, nullable=False, default=True)
    
    def __init__(self, id, name, login, identification, password, user_type):
        self.id = id
        self.name = name
        self.identification = identification
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