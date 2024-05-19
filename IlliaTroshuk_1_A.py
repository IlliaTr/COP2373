# Cinema Tickets Pre-Sale

def pre_sell_tickets():

    # Initialize the variables
    total_tickets = 20
    max_tickets_per_buyer = 4
    total_buyers = 0

    # Loop until all tickets are sold
    while total_tickets > 0:
        try:

            # Display tickets and prompt the user for purchase
            print(f"Tickets remaining: {total_tickets}")
            tickets_requested = int(input("How many tickets would you like to buy (max 4 per buyer)? "))

            # Check if there are enough tickets for the user to purchase
            if tickets_requested < 1 or tickets_requested > max_tickets_per_buyer:
                print(f"You can only buy between 1 and {max_tickets_per_buyer} tickets.")
                continue

            if tickets_requested > total_tickets:
                print(f"Only {total_tickets} tickets remaining. Please enter a valid number of tickets.")
                continue

            # Calculate current number of tickets and buyers
            total_tickets -= tickets_requested
            total_buyers += 1

            # Display the result
            print(f"Thank you for purchasing {tickets_requested} tickets!")
            print(f"Tickets remaining: {total_tickets}")

        # Handle the case where the user input is not a valid integer
        except ValueError:
            print("Please enter a valid number.")

    # Display the results when tickets sold out
    print("All tickets have been sold!")
    print(f"Total number of buyers: {total_buyers}")


# Execute the function
if __name__ == "__main__":
    pre_sell_tickets()
