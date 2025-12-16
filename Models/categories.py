from datetime import  timezone, timedelta
from uuid import uuid4
from typing import Optional

IST = timezone(timedelta(hours=5, minutes=30))

class Category:
    """
    Docstring for Categories
    """

    def __init__(self, category_name:str , budget_limit:Optional[int] =None):
        """
        Docstring for __init__
        
        :param self: Description
        :param category_name: Description
        :type category_name: Optional[str]
        :param budget_limit: Description
        :type budget_limit: int
        """
        self.category_name = category_name
        self.budget_limit = budget_limit
        self.tagged_transactions = []
    
        
    def add_transaction(self, transaction_id:str):
        """
        Docstring for add_transaction
        
        :param self: Description
        :param transaction_id: Description
        """

        if transaction_id not in self.tagged_transactions:
            self.tagged_transactions.append(transaction_id)

    
    def update_budget(self, new_limit:int):
        """
        Docstring for update_budget
        
        :param self: Description
        :param new_limit: Description
        :type new_limit: int
        """
        self.budget_limit = new_limit

    