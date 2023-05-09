from uuid import uuid4
import bcrypt
from sqlalchemy import exc
from datetime import timedelta

from models.users.users import UserModel
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token


class User(Resource):
    def get(self):
        return {'message': 'get one user'}
    
    def post(self):
        try:
            args = reqparse.RequestParser()
            args.add_argument('name', type=str, required=True)
            args.add_argument('login', type=str, required=True)
            args.add_argument('password', type=str, required=True)
            args.add_argument('user_type', type=int, required=True)
            data = args.parse_args()
            
            user_id = str(uuid4())
            
            hash = bcrypt.hashpw(data.get('password').encode('utf8'), bcrypt.gensalt())
            data['password'] = hash.decode('utf-8')
            
            user = UserModel(user_id, **data)
            user.save()
            
            return {
                'status': 'success',
                'message': 'Usuario criado com sucesso!'
            }
        except exc.IntegrityError as e:
            return {
                'status': 'error',
                'message': 'Usuario já existe!'
            }
        except Exception as e:
            print(e)
            return {
                'status': 'error',
                'message': 'Um erro ocorreu, informe ao time responsavel!'
            }
            
        
    def put(self):
        pass
    
    def patch(self):
        pass
    
    def delete(self):
        pass
    

class Auth(Resource):
    def post(self):
        args = reqparse.RequestParser()
        args.add_argument('login', type=str, required=False)
        args.add_argument('password', type=str, required=True)
        data = args.parse_args()
        
        user = UserModel.find_user(data.get('login'))
        
        
        if bcrypt.checkpw(data.get('password').encode('utf8'), user.password.encode('utf-8')):
            token = create_access_token(identity=user.id, expires_delta=timedelta(minutes=1))
            
            return {
                'status': 'success',
                'data': {
                    'access_token': token,   
                }
            }
        return {'message': 'Usuario ou senha errado!'}
        