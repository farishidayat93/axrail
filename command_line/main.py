import yaml


INVENTORY = {
    "1": {"name": "Soda", "price": 4, "quantity": 10},
    "2": {"name": "Cola", "price": 4, "quantity": 13},
    "3": {"name": "Lemonade", "price": 5, "quantity": 12},
    "4": {"name": "Coffee", "price": 8, "quantity": 5},
    "5": {"name": "Tea", "price": 7, "quantity": 15},
}


class VendingMachine:
    def __init__(self):
        self.items = INVENTORY

    def display_items(self, amount_inserted):
        print("Available Items:")
        price_check = False
        for key, value in self.items.items():
            if value['price'] <= amount_inserted and value["quantity"] > 0:
                print(f"{key}: {value['name']} - RM {value['price']} - Quantity: {value['quantity']}")
                price_check = True

        if not price_check:
            print("No items available at this price, please insert more cash")

        return price_check

    def purchase_item(self, choice, amount_inserted):
        if choice in self.items:
            item = self.items[choice]
            self.items[choice]['quantity'] -= 1 
            balance = amount_inserted - item['price']
            change = get_change(balance)
            print(f"Enjoy your {item['name']}! Your change is RM {balance}")
            print(yaml.dump(change, width=1,  sort_keys=False))
            return True
        else:
            print("Invalid selection.")
            return False

    def run(self):
        while True:
            print("\nWelcome to the Vending Machine!")
            try:
                amount_inserted = int(
                    input("Please insert cash amount (or 'q' to quit): RM ")
                    )
                if amount_inserted <= 0:
                    print("Invalid amount. Please insert a valid amount.")
                    continue
            except ValueError:
                print("Thank You. Please come again")
                break

            if not self.display_items(amount_inserted):
                continue
            
            choice = input("Enter the desired item's number (or 'q' to quit): ")
            if choice.lower() == 'q':
                print("Thank You. Please come again")
                break
            else:
                if not self.purchase_item(choice, amount_inserted):
                    continue
                repeat = input("Do want to make another purchase? [Y/n]")
                if repeat.lower() == 'y' or repeat == '':
                    continue
                elif repeat.lower() == 'n':
                    print("Thank You. Please come again")
                    break
                
                else:
                    print("Invalid input, exiting...")
                    break


def get_change(balance: int):
    if type(balance) is not int:
        return {'Invalid Value'}
    if balance == 0:
        return {'No Change'}
    currencies = (100, 50, 20, 10, 5, 1)
    change = {}
    for currency in currencies:
        if balance >= currency:
            change[f'RM {currency}'], balance = divmod(balance, currency)
    return change


if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()