from decimal import Decimal

class Money(Decimal):
    # Initialization method
    def __new__(cls, v, units='USD'):
        return super(Money, cls).__new__(cls, v)
    
    def __init__(self, v, units='USD'):
        self.units = units

    # Addition method
    def __add__(self, other):
        if isinstance(other, Money) and self.units == other.units:
            return Money(super().__add__(other), self.units)
        else:
            raise TypeError("Both Money objects must have the same currency units for addition.")
    
    # Subtration method
    def __sub__(self, other):
        if isinstance(other, Money) and self.units == other.units:
            return Money(super().__sub__(other), self.units)
        else:
            raise TypeError("Both Money objects must have the same currency units for subtraction.")
    
    # Multiplication method
    def __mul__(self, multiplier):
        if isinstance(multiplier, (int, float, Decimal)):
            return Money(super().__mul__(Decimal(multiplier)), self.units)
        else:
            raise TypeError("Multiplier must be an integer, float, or Decimal.")
    
    # String method
    def __str__(self):
        return f"{super().__str__()} {self.units}"

class BankAcct:
    def __init__(self, name, account_number, amount=0.0, interest_rate=0.01):
        """
        Initializes the BankAcct class with the account holder's name, 
        account number, initial amount, and interest rate.
        """
        self.name = name
        self.account_number = account_number
        self.amount = Money(amount, 'USD')
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
        deposit_amount = Money(amount, self.amount.units)
        if amount > 0:
            self.amount += deposit_amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        """
        withdraw_amount = Money(amount, self.amount.units)
        if 0 < amount <= self.amount:
            self.amount -= withdraw_amount
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
        daily_rate = Decimal(self.interest_rate) / 365
        interest = self.amount * daily_rate * days
        return Money(interest, self.amount.units)

    def __str__(self):
        """
        Returns a string representation of the account details.
        """
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Current Balance: {self.amount}\n"
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
    print(f"\nInterest earned over {days} days: {interest}")

    print("\nFinal account details:")
    print(acct)

# Execute test function
if __name__ == "__main__":
    test_bank_acct()
