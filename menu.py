class Menu:

    print("Welcome!")
    def __init__(self):
        # self.starters = ["spring rolls", "stuffed mushrooms", "buffalo wings"]
        self.main_course = ["shawarma", "butter chicken", "rice platter"]
        # self.sides = ["naan", "fries", "garlic bread"]
        # self.drinks = ["pepsi", "orange fanta", "water"]

    # def starters_menu(self):
    #     print("This is our starters menu")
    #     for items in self.starters:
    #         print(f"{self.starters.index(items) + 1}. {items}")

    def main_course_display(self):
        print("This is our main course menu: ")
        for items in self.main_course:
            print(f"{self.main_course.index(items) + 1}. {items}")

    # def sides_menu(self):
    #     print("This is our sides menu")
    #     for items in self.sides:
    #         print(f"{self.sides.index(items) + 1}. {items}")
    #
    # def drinks_menu(self):
    #     print("This is our drinks menu")
    #     for items in self.drinks:
    #         print(f"{self.drinks.index(items) + 1}. {items}")

# x = Menu()
# x.starters_menu()
# x.drinks_menu()