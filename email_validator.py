def email_verification(email):
    j,d,k=0,0,0    
    if len(email)>=6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@")==1):
                if(email[-4]==".") ^ (email[-3:]=="."):
                    for i in email:
                        if i==i.isspace():
                            k=1
                        elif i.isalpha():
                            if i==i.upper():
                                j=1
                        elif i.isdigit():
                            continue
                        elif i =="_" or i =="." or i =="@":
                            continue
                        else:
                            d=1
                    if k==1 or j==1 or d==1:
                        print("wrong email")   
                    else:
                        print(f"Your email {email} is correct!!")         

                else:
                    print(f'Email must end with ".com" or ".org" or ".in".')
            else:
                print("wrong email")
    else:
        print("wrong email")
user_email = input("Enter your email address: ")
email_verification(user_email)
