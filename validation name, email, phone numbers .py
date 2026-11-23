
# Ask for Name .Name validation 
user_name=input("Enter your name. ").strip()
if user_name[0].isalpha() and user_name.isalnum():
    print("You enetred name successfully. ")
else:
    print("The name is incorrect. Name should be start from Alpabets. ")
print(user_name)

# Ask for Email. Email validation
email = input("Enter your Email: ")
if email.endswith("@gmail.com"):
    print("You entered email successfully.")
else:
    print("Please enter a valid email.")
print(email)

# Ask for Phone number.Phone number validation
phone_number = input("Enter your Phone numbers: ").strip()
if phone_number.isdigit():
    print("You entered your number successfully.")
else:
    print("Please enter a correct phone number.")
print(phone_number)






