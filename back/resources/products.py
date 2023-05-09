from uuid import uuid4
from flask_restful import Resource, reqparse
import http
from flask_jwt_extended import jwt_required

from models.products.products import ProductModel
from models.products.productlog import ProductLogModel

class Products(Resource):
    def get(self):
        """ Listar todos os produtos """
        
        try:
            products = [product.json() for product in ProductModel.query.all()]
            return {'status': 'success', 'data': products}
        except:
            return {
                'status': 'error', 
                'message': 'Erro ao realizar processo!'
            }, http.HTTPStatus.SERVICE_UNAVAILABLE
        
    @jwt_required()
    def post(self):
        """ Adicionar um produto """
        
        try:
            args = reqparse.RequestParser()
            args.add_argument('name', type=str, required=True)
            args.add_argument('price', type=float)
            args.add_argument('quantity', type=int)
            
            data = args.parse_args()
            product_id = str(uuid4())
            product = ProductModel(product_id, **data)
            
            # Salvar produto
            product.save()
            
            # Preparar para guardar log
            user = "GetUser"
            
            product_data = product.json()
            product_data.pop('id')
            product_log = ProductLogModel(id=str(uuid4()), product_id=product_id, modify_user=user, changelog='')

            
            # Salvar log
            product_log.save()
            
            return product.json(), http.HTTPStatus.CREATED
            
        except Exception as e:
            print(e)
            product = ProductModel.find_product(product_id)
            product.delete_product()
            return {
                'status': 'error', 
                'message': 'Erro ao realizar processo!'
            }, http.HTTPStatus.SERVICE_UNAVAILABLE
        
        
class Product(Resource):
    def get(self, product_id):
        """ Buscar por um produto """
        
        try:
            product = ProductModel.find_product(product_id)
            
            if product:
                return product.json()
            return {
                'status': 'error', 
                'message': 'Product not found!'
            }, http.HTTPStatus.NOT_FOUND
        except:
            return {
                'status': 'error', 
                'message': 'Erro ao realizar processo!'
            }, http.HTTPStatus.SERVICE_UNAVAILABLE
      
        
    @jwt_required()
    def put(self, product_id):
        """ Atualizar/Adicionar um produto """
        
        try:
            args = reqparse.RequestParser()
            args.add_argument('name', type=str, required=True)
            args.add_argument('price', type=float)
            args.add_argument('quantity', type=int)
            
            data = args.parse_args()
            product = ProductModel.find_product(product_id)
            
            if product:
                product.update_product(**data)
                product.save()
                return product.json(), http.HTTPStatus.ACCEPTED
            
            product = ProductModel(str(uuid4()), **data)
            
            try:
                product.save()
                return product.json(), http.HTTPStatus.CREATED
            except Exception as e:
                return {
                    'status': 'error', 
                    'message': 'Erro ao realizar processo!'
                }, http.HTTPStatus.SERVICE_UNAVAILABLE
        except:
            return {
                'status': 'error', 
                'message': 'Erro ao realizar processo!'
            }, http.HTTPStatus.SERVICE_UNAVAILABLE
      
        
    @jwt_required()
    def delete(self, product_id):
        """ Deletar um produto """
        
        try:
            product = ProductModel.find_product(product_id)
            
            if product:
                product.delete_product()
                return None, http.HTTPStatus.NO_CONTENT
            return {
                'status': 'error', 
                'message': 'Product not found!'
            }, http.HTTPStatus.NOT_FOUND
        except:
            return {
                'status': 'error', 
                'message': 'Erro ao realizar processo!'
            }, http.HTTPStatus.SERVICE_UNAVAILABLE