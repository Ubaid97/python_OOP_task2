from menu import Menu

class Orders(Menu):

    def __init__(self):
        super().__init__()
        self.order_list = []

    def taking_order(self):
