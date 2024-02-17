import re

def is_valid_email(email):
    # Regular expression for basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def get_valid_email():
    while True:
        email = input("Enter your email address: ")
        if is_valid_email(email):
            print("Email is valid. Exiting...")
            break
        else:
            print("Invalid email. Please try again.")

if __name__ == "__main__":
    get_valid_email()
