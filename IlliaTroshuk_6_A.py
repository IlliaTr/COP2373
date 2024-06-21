# Personal information format validator

import re

# Define the validation functions
def validate_phone_number(phone):
    # Validate US phone number format
    pattern = re.compile(r'^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$')
    return pattern.match(phone) is not None

def validate_ssn(ssn):
    # Validate US Social Security number format
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return pattern.match(ssn) is not None

def validate_zip_code(zip_code):
    # Validate US ZIP code format
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return pattern.match(zip_code) is not None

# Main function to get and display input from the user
def main():
    phone = input("Please enter a phone number using this format: 123-456-7890 or (123) 456-7890): ")
    ssn = input("Please enter a Social Security number using this format: 123-45-6789): ")
    zip_code = input("Please enter a ZIP code using this format: 12345 or 12345-6789): ")

    print(f"Phone number valid: {validate_phone_number(phone)}")
    print(f"Social Security number valid: {validate_ssn(ssn)}")
    print(f"ZIP code valid: {validate_zip_code(zip_code)}")

# Run the main function
if __name__ == "__main__":
    main()
