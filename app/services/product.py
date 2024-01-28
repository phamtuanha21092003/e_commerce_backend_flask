from app.services import BaseService
from models import Product

class ProductService(BaseService):
    model = Product

