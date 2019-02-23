from flask import Blueprint, request
from flask_restful import Api
from core.lib.foundation import custom_logger
from core.lib.foundation.base_controller import BaseController
from services.thoughtworks.restuarant_manager import FoodieManager

LOG = custom_logger.getLogger(__name__)
foodie_blueprint = Blueprint('foodie', __name__, url_prefix='/api/v1.0/foodie')
foodie_api = Api(foodie_blueprint)

class FoodieController(BaseController):
    
    def get(self):
        return FoodieManager().get_all_restuarants()

foodie_api.add_resource(FoodieController, '/foodie/')


class FoodieSearchController(BaseController):
    
    def get(self, rest_name):
        pass

foodie_api.add_resource(FoodieSearchController, '/foodie/<string:rest_name>/')