# Menu class imported as parent class
from menu import Menu

# This class implements functions to take a user's order and display it
class Orders(Menu):

    def __init__(self):
        super().__init__() # inherits all attributes and functions from parent class Menu
        self.order_list = [] # an empty list to store the user's order in

    # function to take and store user's order
    def taking_order(self):
        print("What will you be having today?")
        order_number = 1
        # while loop that loops 3 times - the number of times user wants to order
        while i < 4:
            # user is asked to input their 1st, 2nd or 3rd order, depending on how many orders they've already made
            order = input(f"Order {order_number}: ")

            # if loop that iterates over the menu list inheroted from Menu class and checks if user's ordered item matches an item in the menu
            if order in Menu().menu_list:
                # if ordered item is in menu, the item is added to the order_list (see line 9)
                self.order_list.append(order)
                order_number += 1
            else:
                # if ordered item is not in menu, uder is asked to choose an option from the menu
                print("please choose an option from the menu")
                super().menu_display() # menu displayed to remind user

    # seperate function to display user's order in a formatted way
    def display_order(self):
        print("This is your order:")
        # for loop iterates over every item in the user's order list and displays them as an ordered list
        for items in self.order_list:
            print(f"{self.order_list.index(items) + 1}. {items}")



