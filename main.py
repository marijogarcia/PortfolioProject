class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        total = (self.item_price * self.item_quantity)
        print("%s %d @ $%.2f = $%.2f" % (self.item_name, self.item_quantity, self.item_price, total))
        return total


class ShoppingCart:
    cart_items = []

    def __init__(self):
        return

    def __init__(self, customer_name, date):
        self.customer_name = customer_name
        self.current_date = date
        return

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        return

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                print("Removed " + item_name)
                return

        print("Item not found in cart. Nothing removed.")
        return

    def modify_item(self, ItemToPurchase):
        for item in self.cart_items:
            if item.item_name == ItemToPurchase.item_name:
                print("We found a match")
                if ItemToPurchase.item_description != "none":
                    item.item_description = ItemToPurchase.item_description
                    print("Updated Description")

                if ItemToPurchase.item_price != 0.0:
                    item.item_price = ItemToPurchase.item_price
                    print("Updated Price")

                if ItemToPurchase.item_quantity != 0:
                    item.item_quantity = ItemToPurchase.item_quantity
                    print("Updated Quantity")

                return

        print("Item not found in cart. Nothing removed.")
        return

    def get_num_items_in_cart(self, ):
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total

    def get_cost_of_cart(self, ):
        total = 0
        for item in self.cart_items:
            total += item.item_quantity * item.item_price
        return total

    def print_total(self, ):
        print(self.customer_name +"'s Shopping Cart - " + self.current_date)
        print("Number of items: " + str(self.get_num_items_in_cart()))
        for item in self.cart_items:
            item.print_item_cost()
        print("Total: $%.2f" % self.get_cost_of_cart())
        return

    def print_descriptions(self, ):
        print(self.customer_name +"'s Shopping Cart - " + self.current_date)
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.item_name + ": " + item.item_description)
        return


def print_menu(shopping_cart):
    menu = '''
    MENU
    a - Add item to cart
    r - Remove item from cart
    c - Change item quantity
    i - Output items' descriptions
    o - Output shopping cart
    q - Quit
    Choose an option:
    '''

    option = ""
    while True:
        print(menu)
        option = input().strip()
        if option == "a":
            print("ADD ITEM TO CART")
            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_description = input("Enter the item description:\n")
            item.item_quantity = int(input("Enter the item quantity:\n"))
            item.item_price = float(input("Enter the item price:\n"))
            shopping_cart.add_item(item)

        elif option == "r":
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter the item name:\n")
            shopping_cart.remove_item(item_name)

        elif option == "c":
            print("CHANGE ITEM QUANTITY")
            item = ItemToPurchase()
            item.item_name = input("Enter the item name:\n")
            item.item_quantity = int(input("Enter the new quantity:\n"))
            shopping_cart.modify_item(item)

        elif option == "o":
            print("OUTPUT SHOPPING CART")
            shopping_cart.print_total()

        elif option == "i":
            print("OUTPUT ITEMS DESCRIPTIONS")
            shopping_cart.print_descriptions()

        elif option == "q":
            break
        else:
            print("Enter a valid option")
    return

def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")

    cart = ShoppingCart(customer_name, current_date)

    ##################################################################
    nikes = ItemToPurchase()
    nikes.item_name = "Nike Romaleos"
    nikes.item_description = "Volt color, Weightlifting shoes"
    nikes.item_quantity = 2
    nikes.item_price = 189

    chocolate_chips = ItemToPurchase()
    chocolate_chips.item_name = "Chocolate Chips"
    chocolate_chips.item_description = "Semi-sweet"
    chocolate_chips.item_quantity = 5
    chocolate_chips.item_price = 3

    beats = ItemToPurchase()
    beats.item_name = "Powerbeats 2 Headphones"
    beats.item_description = "Bluetooth Headphones"
    beats.item_quantity = 1
    beats.item_price = 128

    cart.add_item(nikes)
    cart.add_item(chocolate_chips)
    cart.add_item(beats)
    ##################################################################

    print_menu(cart)


main()



