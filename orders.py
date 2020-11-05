from menu import Menu

class Orders(Menu):

    def __init__(self):
        super().__init__()
        self.order_list = []

    def taking_order(self):
        print("Hi,")
        super().main_course_display()
        print("What will you be having today?")
        i = 1
        while i < 4:
            order = input(f"Order {i}: ")
            if order in Menu().main_course:
                self.order_list.append(order)
                i += 1
            else:
                print("please choose an option from the menu")
                super().main_course_display()

# x = Orders()
# x.taking_order()
# print(x.order_list)
