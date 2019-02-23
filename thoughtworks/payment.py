
class Payment(object):
    
    def __init__(self, payment_id, order_id, payment_type, payment_amount, payment_created_time, payment_status):
        self.payment_id = payment_id
        self.order_id = order_id
        self.payment_type = payment_type
        self.payment_amount = payment_amount
        self.payment_created_time = payment_created_time
        self.payment_status = payment_status
        