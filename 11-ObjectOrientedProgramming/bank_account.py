class Bank_account:
    def __init__(self, bank_account):
       self.bank_account = str(bank_account)
       self.balance = 0.0

    def deposit(self, dep):
        self.balance += dep
    
    def withdraw(self, wit):
        if wit<=self.balance:
            self.balance -= wit
        else:
            print(f'Insufficient funds on the account ({wit})')
    
    def show_status(self):
        balancef = f'{self.balance:.2f}'.replace('.',',')
        if len(self.bank_account) == 26 or len(self.bank_account) == 32:
            return f'Bank Account No: {self.bank_account}\n Balance: PLN {balancef}'
        else:
            return 'Wrong bank account no. (no 26 digits), maybe try without spaces:)'
def main():
    my_acc = Bank_account('12 3456 5555 9090 1111 0000 7722')
    print(my_acc.show_status())
    my_acc.deposit(25.30)
    print(my_acc.show_status())
    my_acc.withdraw(31.70)
    print(my_acc.show_status())
    my_acc.withdraw(14)
    print(my_acc.show_status())

if __name__ == '__main__':
    main()

        


    