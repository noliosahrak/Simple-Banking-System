import random


class Account:
    uniqueness_guard = []

    @staticmethod
    def unique_ending(cls):
        ending = str(random.randint(0, 10000000000))
        if ending in cls.uniqueness_guard:
            ending = cls.unique_ending()
        cls.uniqueness_guard.append(ending)
        return ending

    def __init__(self, cls):
        ending = cls.unique_ending
        if len(ending) < 10:
            ending = "0" * (10 - len(ending)) + ending
        self.number = "400000" + ending
        self.pin = str(random.randint(0, 10000))
        if len(self.pin) < 4:
            self.pin = "0" * (4 - len(self.pin)) + self.pin
        self.balance = 0


def create_account():
    new_account = Account(Account)
    print("Your card has been created")
    print("Your card number:")
    print(new_account.number)
    print("Your card PIN:")
    print(new_account.pin)
    print()
    accounts.append(new_account)


def log_menu(account):
    while True:
        print("1. Balance")
        print("2. Logout")
        print("0. Exit")
        choice = int(input())
        print()
        if choice == 0:
            print("Bye!")
            return False
        if choice == 1:
            print("Balance: " + str(account.balance))
            print()
        if choice == 2:
            print("You have successfully logged out!")
            print()
            return True


def login():
    print("Enter your card number:")
    card_number = input()
    print("Enter your PIN:")
    card_pin = input()
    print()
    for i in accounts:
        if card_number == i.number and card_pin == i.pin:
            print("You have successfully logged in!")
            return log_menu(i)
        else:
            print("Wrong card number or PIN")
            print()
            return True


def start():
    menu = True
    while menu:
        print("1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        choice = int(input())
        print()
        if choice == 0:
            print("Bye!")
            menu = False
        if choice == 1:
            create_account()
        if choice == 2:
            menu = login()


accounts = []
start()
