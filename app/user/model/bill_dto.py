
class BillDTO():
    
    def __init__(self, type, value, observation, date_bill, user_id) -> None:
        self.type = type
        self.value = value
        self.observation = observation
        self.date_bill = date_bill
        self.user_id = user_id