def get_user_input():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email address: ")
    return name, age, email

def display_registration_form(name, age, email):
    print("\nRegistration Details:")
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)

def main():
    print("Welcome to the Registration Form")
    name, age, email = get_user_input()
    display_registration_form(name, age, email)
