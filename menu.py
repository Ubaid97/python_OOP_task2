# This class contains the menu and a function to display it
class Menu:

    print("Welcome!")

    def __init__(self):
        # menu items are stored as a list
        self.menu_list = ["spring rolls", "buffalo wings", "shawarma", "butter chicken", "rice platter"]

    # this function displays the menu in a formatted way
    def menu_display(self):
        print("This is our menu: ")
        # for loop iterates over every item in the menu list and displays them as an ordered list
        for items in self.menu_list:
            print(f"{self.menu_list.index(items) + 1}. {items}")
