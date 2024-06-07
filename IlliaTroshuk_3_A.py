# Monthly Expenses Analyzer

import functools

def main():

    # Initialize a list
    expenses = []

    # Display instructions for the user
    print("Please enter your monthly expenses one by one. Type 'f' to finish")

    # Continue to ask the user about their expenses until they are finished
    while True:
        expense_type = input("Enter the type of expenses: ")
        if expense_type.lower() == 'f':
            break
        amount = float(input("Enter the amount: "))
        expenses.append((expense_type, amount))

    # Calculate total expense
    total_expense = functools.reduce(lambda x, y,: x + y[1], expenses, 0)

    # Find highest expense
    highest_expense = functools.reduce(lambda x, y: x if x[1] > y[1] else y, expenses)

    # Find lowest expense
    lowest_expense = functools.reduce(lambda x, y: x if x[1] < y[1] else y, expenses)

    # Display the results
    print(f"Total Monthly Expense: ${total_expense:.2f}")
    print(f"Highest Monthly Expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest Monthly Expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

if __name__ == "__main__":
    main()