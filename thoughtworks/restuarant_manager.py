from services.thoughtworks.foodie_dao import RestuarantDAO
from services.loan.middleware.util.loan_middleware_util import get_transaction_manager

from core.lib.foundation import custom_logger
LOG = custom_logger.getLogger(__name__)

class FoodieManager():
    
    def __init__(self):
        self.tran_manager = None#get_transaction_manager()
        self.db = None#self.tran_manager.get_database_connection(section='loan', mode='READWRITE')
        
    def get_restuarant_by_id(self, rest_id):
        LOG.info("")
        res = RestuarantDAO(self.db).get_restuarant_by_id(rest_id)
        if res:
            res = self.object_to_dict(res)
        return res
    
    def get_all_restuarants(self):
        LOG.info("")
        rest_list = RestuarantDAO(self.db).get_all_restuarant()
        res_list = []
        for res in rest_list:
            res_list.append(self.object_to_dict(res))
        return res_list
        
    def get_by_name(self, name):
        LOG.info("")
        rest_list = RestuarantDAO(self.db).search_by_name(name)
        res_list = []
        for res in rest_list:
            res_list.append(self.object_to_dict(res))
        return res_list
    
    def authenticate(self, email, password):
        LOG.info("")
        return RestuarantDAO(self.db).authenticate(email, password)
    
    def create_user(self, user_data):
        LOG.info("")
        return RestuarantDAO(self.db).create_user(user_data)

    def add_user_review(self, user_data):
        LOG.info("")
        return RestuarantDAO(self.db).add_user_review(user_data)
    
    def create_oder(self, user_data):
        LOG.info("")
        return RestuarantDAO(self.db).create_order(user_data)
    
    def update_oder(self, user_data):
        LOG.info("")
        return RestuarantDAO(self.db).create_order(user_data)
    
    def object_to_dict(self, obj):
        """
        Note : This method identifies the property instance available in an object to
                convert into dictionary.
        :param: any class object
        :return: python dictionary
        """
        obj_dict = {}
        obj_dict['rest_name'] = obj.rest_name
        obj_dict['dish_list'] = []
        for food in obj.dish_list:
            food_obj_dict = {}
            food_obj_dict['dish_id'] = food.dish_id
            food_obj_dict['dish_name'] = food.dish_name
            food_obj_dict['dish_type'] = food.dish_type
            obj_dict['dish_list'].append(food_obj_dict)
        obj_dict['rating'] = obj.rating
        obj_dict['rest_id'] = obj.rest_id
        obj_dict['location'] = obj.location
        return obj_dict

if __name__ == '__main__':
    print FoodieManager().get_all_restuarants()
    print FoodieManager().get_by_name('barbequee')