def email_verification(email):
    # Check if the email contains "@" symbol
    if "@" in email:
        # Split the email address into local part and domain part
        local_part, domain_part = email.split("@")

        # Check if both parts are not empty
        if local_part and domain_part:
            # Check if the domain has at least one dot (.)
            if "." in domain_part:
                print(f"Email verification successful. {email} is a valid email address.")
            else:
                print(f"Invalid email. The domain in {email} is missing a dot (.)")
        else:
            print(f"Invalid email. Local part or domain part is empty in {email}")
    else:
        print(f"Invalid email. {email} is missing the @ symbol.")

# Example usage:
user_email = input("Enter your email address: ")
email_verification(user_email)
