from flask import Blueprint
import flask_restful
from flask import Blueprint, request, jsonify

from core.lib.foundation.base_controller import BaseController

from core.lib.foundation import custom_logger
LOG = custom_logger.getLogger(__name__)

thoughworks_blueprint = Blueprint('thoughtwork', __name__, url_prefix='/api/v1.0/thoughtwork')
application_api = flask_restful.Api(thoughworks_blueprint)

#Order Controller
class FoodieController(BaseController):
    
    def get(self):
        from services.thoughtworks.restuarant_manager import FoodieManager
        return FoodieManager().get_all_restuarants()

application_api.add_resource(FoodieController, '/foodie/')


class FoodieSearchController(BaseController):
    
    def get(self, rest_name):
        try:
            from services.thoughtworks.restuarant_manager import FoodieManager
            return FoodieManager().get_by_name(rest_name)
        except Exception as ex:
            LOG.exception("exception occured in controller %s" % ex)
application_api.add_resource(FoodieSearchController, '/foodie/<string:rest_name>/')

class RestuarantController(BaseController):
    
    def get(self, rest_id):
        try:
            from services.thoughtworks.restuarant_manager import FoodieManager
            return FoodieManager().get_restuarant_by_id(int(rest_id))
        except Exception as ex:
            LOG.exception("exception occured in controller %s" % ex)
application_api.add_resource(RestuarantController, '/restuarant/<string:rest_id>')

class UserController(BaseController):
    
    def post(self):
        try:
            LOG.info(request.data)
            user_name = request.data['username']
            password = request.data['password']
            from services.thoughtworks.restuarant_manager import FoodieManager
            return FoodieManager().authenticate(user_name, password)
        except Exception as ex:
            LOG.exception("exception occured in controller %s" % ex)
application_api.add_resource(UserController, '/user/authenticate/')

class UserRegistrationController(BaseController):
    
    def post(self):
        try:
            LOG.info(request.data)
            from services.thoughtworks.restuarant_manager import FoodieManager
            return FoodieManager().create_user(request.data)
        except Exception as ex:
            LOG.exception("exception occured in controller %s" % ex)
application_api.add_resource(UserRegistrationController, '/user/registration/')

class UserReviewController(BaseController):
    
    def post(self):
        try:
            LOG.info(request.data)
            from services.thoughtworks.restuarant_manager import FoodieManager
            return FoodieManager().add_user_review(request.data)
        except Exception as ex:
            LOG.exception("exception occured in controller %s" % ex)
application_api.add_resource(UserReviewController, '/user/review/')

class OrderController(BaseController):
    
    def post(self):
        try:
            LOG.info(request.data)
            from services.thoughtworks.restuarant_manager import FoodieManager
            return FoodieManager().create_oder(request.data)
        except Exception as ex:
            LOG.exception("exception occured in controller %s" % ex)
            
    def put(self):
        try:
            LOG.info(request.data)
            from services.thoughtworks.restuarant_manager import FoodieManager
            return FoodieManager().update_oder(request.data)
        except Exception as ex:
            LOG.exception("exception occured in controller %s" % ex)
application_api.add_resource(OrderController, '/foodie/order/')

class OrderViewController(BaseController):
    
    def get(self, user_id):
        try:
            from services.thoughtworks.restuarant_manager import FoodieManager
            return #FoodieManager().get_order_by_user_id(int(user_id))
        except Exception as ex:
            LOG.exception("exception occured in controller %s" % ex)
application_api.add_resource(OrderViewController, '/userorder/<string:user_id>')

#PaymentController
class PaymentController(BaseController):

    def post(self):
        try:
            LOG.info(request.data)
            from services.thoughtworks.restuarant_manager import FoodieManager
            return FoodieManager().add_user_review(request.data)
        except Exception as ex:
            LOG.exception("exception occured in controller %s" % ex)
application_api.add_resource(PaymentController, '/payment/')

class PaymentStatusController(BaseController):
    
    def get(self, orderid):
        try:
            from services.thoughtworks.restuarant_manager import FoodieManager
            return FoodieManager().get_restuarant_by_id(int(orderid))
        except Exception as ex:
            LOG.exception("exception occured in controller %s" % ex)
application_api.add_resource(PaymentStatusController, '/paymentstatus/<string:orderid>')

