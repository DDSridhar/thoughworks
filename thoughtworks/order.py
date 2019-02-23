
class Order(object):
    
    def __init__(self, order_id, user_id, rest_id, order_time, order_amount, order_items, order_status, payment_id, payment_type):
        self.order_id = order_id
        self.user_id = user_id
        self.rest_id = rest_id
        self.order_time = order_time
        self.order_amount = order_amount
        self.order_items = order_items
        self.order_status = order_status
        self.payment_id = payment_id#NULLABLE
        self.payment_type = payment_type
        