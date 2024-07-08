class BankAcct:
    def __init__(self, name, account_number, amount=0.0, interest_rate=0.01):
        """
        Initializes the BankAcct class with the account holder's name, 
        account number, initial amount, and interest rate.
        """
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        """
        Adjusts the interest rate for the account.
        """
        self.interest_rate = new_rate

    def deposit(self, amount):
        """
        Deposits money into the account.
        """
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        """
        if 0 < amount <= self.amount:
            self.amount -= amount
        else:
            print("Invalid withdraw amount. It must be positive and less than or equal to the current balance.")

    def balance(self):
        """
        Returns the current balance of the account.
        """
        return self.amount

    def calculate_interest(self, days):
        """
        Calculates the interest earned based on the number of days.
        """
        daily_rate = self.interest_rate / 365
        interest = self.amount * daily_rate * days
        return interest

    def __str__(self):
        """
        Returns a string representation of the account details.
        """
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Current Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate:.2%}")

# Test function
def test_bank_acct():
    print("Creating a new account for John Doe with account number 123456789.")
    acct = BankAcct(name="John Doe", account_number="123456789", amount=1000.0, interest_rate=0.05)

    print("\nInitial account details:")
    print(acct)

    print("\nDepositing $500...")
    acct.deposit(500)
    print("Balance after deposit:", acct.balance())

    print("\nWithdrawing $200...")
    acct.withdraw(200)
    print("Balance after withdrawal:", acct.balance())

    print("\nAdjusting interest rate to 4%...")
    acct.adjust_interest_rate(0.04)
    print("New interest rate:", acct.interest_rate)

    days = 30
    interest = acct.calculate_interest(days)
    print(f"\nInterest earned over {days} days: ${interest:.2f}")

    print("\nFinal account details:")
    print(acct)

# Execute test function
if __name__ == "__main__":
    test_bank_acct()
