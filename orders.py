from menu import Menu

class Orders(Menu):

    def __init__(self):
        super().__init__()
        self.order_list = []

    def taking_order(self):
        print("Hi, What will you be having today?")
        i = 1
        while i < 4:
            self.order_list.append(input(f"Order {i}: "))
            i += 1

# x = Orders()
# x.taking_order()
# print(x.order_list)