# You've initialized the cash register with attributes for discount, total, items, and previous_transactions, 
# as specified in the constructor (__init__ method).
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

# The add_item method allows you to add items to the cash register, including an optional quantity. 
# It correctly updates the total, items, and previous_transactions attributes based on the item's price and quantity.
    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "quantity": quantity, "price": price}
        )

# The apply_discount method calculates and applies the discount correctly if discount is non-zero. 
# It updates the total attribute accordingly and prints a message indicating the discounted total.
    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

# The void_last_transaction method correctly reverses the last transaction, updating the total, items, and 
# previous_transactions attributes.
    def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void."
        self.total -= (
            self.previous_transactions[-1]["price"]
            * self.previous_transactions[-1]["quantity"]
        )
        for _ in range(self.previous_transactions[-1]["quantity"]):
            self.items.pop()
        self.previous_transactions.pop()