from datetime import datetime

# Greet the user based on the current time
def greet_user():
    name = input("Enter Your Name: ")
    hour = datetime.now().hour
    if hour < 12:
        print(f"Good Morning {name}!")
    elif 12 <= hour < 18:
        print(f"Good Afternoon {name}!")
    else:
        print(f"Good Evening {name}!")
    print("Welcome to Help Centre!")

# Reusable function to handle choices
def get_choice(options):
    for key, value in options.items():
        print(f"{key}. {value}")
    choice = int(input("Enter your choice: "))
    return choice

# Define all help functions
def myorder():
    options = {
        1: "Current Products",
        2: "Previous Order",
        3: "Canceled Order"
    }
    choice = get_choice(options)
    if choice == 1:
        print("Current Product: Samsung S25 Ultra")
    elif choice == 2:
        print("Previous Order: Java Book")
    elif choice == 3:
        print("Canceled Order: Toy Car")
    else:
        print("Invalid option in My Orders.")

def myaccount():
    options = {
        1: "Change the number",
        2: "Change my email"
    }
    choice = get_choice(options)
    if choice == 1:
        ph_num = int(input("Enter new 10-digit number: "))
        print(f"Successfully changed to {ph_num}")
    elif choice == 2:
        email = input("Enter new email: ")
        print(f"Successfully changed to {email}")
    else:
        print("Invalid option in My Account.")

def ret():
    options = {
        1: "Payment and refunds",
        2: "Issue with order"
    }
    choice = get_choice(options)
    if choice == 1:
        print("Refund options: Cash on delivery / Prepaid")
    elif choice == 2:
        issue = input("Enter issue with your order: ")
        print(f"Your issue has been recorded: {issue}")
    else:
        print("Invalid option in Return.")

def payment():
    options = {
        1: "Where do I get refund?",
        2: "Amount debited but order not confirmed"
    }
    choice = get_choice(options)
    if choice == 1:
        print("Refunds are processed within 5–7 business days.")
    elif choice == 2:
        print("If the amount was debited but the order isn't confirmed, please wait or contact support.")
    else:
        print("Invalid option in Payments.")

def question():
    question = input("Your question: ")
    print(f"Thank you! We'll get back to you shortly regarding: {question}")

def somethingelse():
    message = input("Please describe your issue: ")
    print("Thank you for contacting us. Your message has been received.")

# Main menu loop
def main():
    greet_user()

    menu_options = {
        1: "My Orders",
        2: "My Account",
        3: "Return",
        4: "Payments",
        5: "Product Question",
        6: "Something else",
        7: "Exit"
    }

    while True:
        print("\n--- Help Centre Menu ---")
        choice = get_choice(menu_options)

        if choice == 1:
            myorder()
        elif choice == 2:
            myaccount()
        elif choice == 3:
            ret()
        elif choice == 4:
            payment()
        elif choice == 5:
            question()
        elif choice == 6:
            somethingelse()
        elif choice == 7:
            print("Thank you for visiting the Help Centre!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
