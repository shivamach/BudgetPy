from datetime import datetime, timezone, timedelta
from uuid import uuid4
from typing import Optional
from .transactions import Transaction
from .categories import Category

IST = timezone(timedelta(hours=5, minutes=30))

class SpendManager:
    """
    Docstring for SpendManager
    """

    def __init__(self) -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.transactions = {} # Dictionary: {transaction_id: Transaction object}
        self.categories = {} #map transaction ids to spend tags
        self.moods = {} #map transaction ids to mood tags in future

        #add later a fuunction that will check if saved json file exists, if yes, load one of them


    def add_transaction(self, type:str , mode:str, amount:float, description:str, sentiment:Optional[str] =None, transaction_date: Optional[datetime] =None):
        """
        Docstring for add_transaction
        
        :param self: Description
        :param type: Description
        :type type: str
        :param mode: Description
        :type mode: str
        :param amount: Description
        :type amount: float
        :param description: Description
        :type description: str
        :param sentiment: Description
        :type sentiment: Optional[str]
        :param transaction_date: Description
        :type transaction_date: Optional[datetime]
        """
        transaction_obj = Transaction(type , mode, amount, description, sentiment, transaction_date)
        self.transactions[transaction_obj.id] = transaction_obj
        print(f"Transaction Added: {transaction_obj.amount}/- Rs for {transaction_obj.description}")
    
    def add_category(self, category_name:str, budget_limit:Optional[int] =None):
        """
        Docstring for add_category
        
        :param self: Description
        :param category_name: Description
        :param budget_limit: Description
        """
        category_obj = Category(category_name, budget_limit)
        self.categories[category_name] = category_obj
        print(f"Created Category: {category_obj.category_name} with budget:{category_obj.budget_limit}/- Rs")
    

    def add_transaction_category(self, transaction_id, category_name):
        """
        Docstring for add_transaction_category
        
        :param self: Description
        :param transaction_id: Description
        :param category_name: Description
        """

        transaction_obj = self.transactions[transaction_id]
        if category_name not in self.categories:
            category_obj = Category(category_name)
        else:
            category_obj = self.categories.get(category_name, Category(category_name))

        transaction_obj.add_category(category_name)
        category_obj.add_transaction(transaction_id)

        self.transactions[transaction_obj.id] = transaction_obj
        self.categories[category_name] = category_obj




