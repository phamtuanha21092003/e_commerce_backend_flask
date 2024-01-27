from app.services.base_service import BaseService
from models import Account


class AccountService(BaseService):
    model = Account
    
    