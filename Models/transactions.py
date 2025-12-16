from datetime import datetime, timezone, timedelta
from uuid import uuid4
from typing import Optional

IST = timezone(timedelta(hours=5, minutes=30))

class Transaction:
    """ Defines a Transaction

    Attributes:
    
    """
    def __init__(self, type:str , mode:str, amount:float, description:str, sentiment:Optional[str] =None, transaction_date: Optional[datetime] =None):
        self.id = str(uuid4)
        self.type = type
        self.mode = mode
        self.amount = amount
        self.description = description
        self.sentiment = sentiment
        self.transaction_date = datetime.now(IST)
        self.tagged_categories = []
        self.mood_tags = []


        #For future shared spending tracking
        self.shared_tag = False
        self.people_shared = [] #list of people IDs derived from names selected/tagged or just add random person whatever is better
        self.myshare = 1 #divide total existing amount to get the actual amount 
        
    def add_category(self, category_name:str):
        """
        Docstring for add_category
        
        :param self: Description
        :param category_name: Description
        :type category_name: Optional[str]
        """
        if category_name not in self.tagged_categories:
            self.tagged_categories.append(category_name)