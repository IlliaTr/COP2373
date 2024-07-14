from decimal import Decimal

class Money(Decimal):
    # Initialization
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
    
    # Subtraction method
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

# Test function
def test_money_operations():
    m1 = Money('10.50', 'USD')
    m2 = Money('5.25', 'USD')
    m3 = Money('15.75', 'EUR')

    print("Initial Values:")
    print(f"m1: {m1}")
    print(f"m2: {m2}")
    print(f"m3: {m3}")

    # Test addition
    result_add = m1 + m2
    print("\nAddition:")
    print(f"{m1} + {m2} = {result_add}")

    try:
        result_add_diff_units = m1 + m3
    except TypeError as e:
        print("\nAddition with different units:")
        print(f"Error: {e}")

    # Test subtraction
    result_sub = m1 - m2
    print("\nSubtraction:")
    print(f"{m1} - {m2} = {result_sub}")

    try:
        result_sub_diff_units = m1 - m3
    except TypeError as e:
        print("\nSubtraction with different units:")
        print(f"Error: {e}")

    # Test multiplication
    result_mul = m1 * 2.5
    print("\nMultiplication:")
    print(f"{m1} * 2.5 = {result_mul}")

if __name__ == "__main__":
    test_money_operations()
