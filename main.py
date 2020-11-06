# Orders class imported, allowing inheritance of both Menu and Orders class
from orders import Orders

# customer created as instance of Orders class
customer = Orders()
# menu_display() function called from menu class to show menu to the customer in a user friendly format
customer.menu_display()
# taking_order() function called from Orders class, which takes customer's order and stores the content in a list
customer.taking_order()
# display_order() function called from Orders class, which displays customer's order in a user friendly format
customer.display_order()