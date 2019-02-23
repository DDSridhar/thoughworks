from services.thoughtworks.restuarant import Restuartant
from services.thoughtworks.dish import Dish
from services.thoughtworks.user import User

from core.lib.foundation import custom_logger
LOG = custom_logger.getLogger(__name__)

user1 = User(1, 'Sridhar', 'DD', 'sridhar@gmail.com', '9789153012', 'sridhar', 'madambakkam')
user2 = User(2, 'Divya', 'DD', 'divya@gmail.com', '9789153013', 'divya', 'madambakkam')
CH_BRIYANI = Dish(1, 'Chicken Briyani', 'NON VEG')
MT_BRIYANI = Dish(2, 'Mutton Briyani', 'NON VEG')
VG_BRIYANI = Dish(3, 'VEG Briyani', 'VEG')
EG_BRIYANI = Dish(4, 'Egg Briyani', 'NON VEG')
RESTUARANT = [
              Restuartant(1, 'coal barbequee', [CH_BRIYANI, MT_BRIYANI, EG_BRIYANI], 2, 'Navalur'),
              Restuartant(2, 'absolute barbequee', [VG_BRIYANI], 3, 'T Nagar'),
              Restuartant(3, 'sea shell', [CH_BRIYANI, MT_BRIYANI], 4, 'Perungudi'),
              ]
USERS = [user1, user2]


class RestuarantDAO():
    
    def __init__(self, conn):
        #set up connection
        self.conn = conn
        pass
        
    def get_all_restuarant(self):
        LOG.info("")
        return RESTUARANT
    
    def get_restuarant_by_id(self, rest_id):
        LOG.info("")
        for rest in RESTUARANT:
            if rest_id == rest.rest_id:
                LOG.info("")
                return rest
        return None
        
    def search_by_name(self, name):
        LOG.info("")
        restuar_list = []
        for rest in RESTUARANT:
            if name in rest.rest_name:
                restuar_list.append(rest)
        LOG.info("")
        return restuar_list
    
    def fill_restuarant_object(self, rest_row):
        values = dict(rest_name=rest_row.get('rest_name'),
                      dish_list=rest_row.get('dish_list'),
                      rating=rest_row.get('rating'),
                      rest_id=rest_row.get('rest_id'),
                      location=rest_row.get('location'))
        pay_cal = Restuartant(**values)
        return pay_cal

    def authenticate(self, email, password):
        LOG.info("")
        for user in USERS:
            if user.email == email and user.password == password:
                return True
        LOG.info("")
        return False
    
    def create_user(self, user_data):
        LOG.info("")
        #Save User Data
        return "SUCCESS"
    
    def create_order(self, user_data):
        LOG.info("")
        #Save User Data
        return "#ORDER_ID"
    
    def add_user_review(self, user_data):
        LOG.info("")
        #Save User Review
        return "SUCCESS"