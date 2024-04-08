import yaml


def return_change(balance: int):
    if type(balance) is not int:
        return {'Invalid Value'}
    if balance == 0:
        return {'No Change'}
    currencies = (100, 50, 20, 10, 5, 1)
    change = {}
    for currency in currencies:
        if balance < currency:
            next
        else:
            change[f'RM {currency}'], balance = divmod(balance, currency)
    return change


if __name__ == "__main__":
    change = return_change(186)
    # print(change)
    print(yaml.dump(change, width=1,  sort_keys=False))
