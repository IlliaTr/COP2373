# Spam Email Evaluation

import re
import time

def make_timer(func):
    def wrapper():
        t1 = time.time()
        ret_val = func()
        t2 = time.time()
        print('Time elapsed was', t2 - t1, 'seconds.')
        return ret_val
    return wrapper

@make_timer
def main():
    # Create a list of 30 common spam/scam words
    spam_keywords = [
        "free", "win", "winner", "click here", "subscribe", "buy now", "claim now",
        "discount", "limited time", "offer expires", "act now", "urgent", "congratulations",
        "check here", "risk-free", "money-back guarantee", "earn", "extra cash",
        "cheap", "no cost", "prize", "money", "billion", "million", "click here",
        "chance", "100% free", "trial", "special promotion", "guaranteed"
    ]
    
    # Ask user to paste email content and convert it to lower case
    email_message = input("Enter your email message: ").lower()

    # Delay to simulate processing
    time.sleep(2) 
    
    # Initialize variables
    spam_score = 0
    spam_words_found = []
    likelihood = ""
    
    # Iterate over each word in email, check for spam keyword, and update the variables
    for keyword in spam_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', email_message):
            spam_score += 1
            spam_words_found.append(keyword)
    
    # Determine spam likelihood based on the spam score
    if spam_score > 6:
        likelihood = "High"
    elif 3 < spam_score <= 6:
        likelihood = "Moderate"
    else:
        likelihood = "Low"

    # Display the results
    print("\nSpam Score:", spam_score)
    print("Likelihood of being spam:", likelihood)
    print("Keywords found:", ', '.join(spam_words_found))

# Run the application
if __name__ == "__main__":
    main()