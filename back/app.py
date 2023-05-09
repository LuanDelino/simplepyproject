from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.healthcheck import Healthcheck
from resources.products import Product, Products
from resources.users import User, Auth


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://teste:teste@localhost:5432/crm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'Teste'

api = Api(app)
jwt = JWTManager(app)

api.add_resource(Healthcheck, '/healthcheck')
api.add_resource(Products, '/products')
api.add_resource(Product, '/products/<string:product_id>')
api.add_resource(User, '/users')
api.add_resource(Auth, '/auth')


if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    
    app.run(debug=True, host='0.0.0.0', port=8000)