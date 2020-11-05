from menu import Menu

class Orders(Menu):

    def __init__(self):
        super().__init__()
        self.order_list = []

    def taking_order(self):
        print("What will you be having today?")
        i = 1
        while i < 4:
            order = input(f"Order {i}: ")
            if order in Menu().menu_list:
                self.order_list.append(order)
                i += 1
            else:
                print("please choose an option from the menu")
                super().menu_display()


    def display_order(self):
        print("This is your order:")
        for items in self.order_list:
            print(f"{self.order_list.index(items) + 1}. {items}")



