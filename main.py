

client_hours = {}

def load_cases():
    global case_info
    case_info = {}

    try:
        with open("cases.csv", "r") as file:
            next(file)  # Skip the header

            for line in file:
                line = line.strip()
                case_number, client, court, rate = line.split(",")

                case_info[case_number] = {
                    "Client": client,
                    "Court": court,
                    "Billing Rate": float(rate)
                }

    except FileNotFoundError:
        print("No existing case file found.")

    return case_info


def save_cases():
    with open("cases.csv", "w") as file:

        file.write("Case Number,Client,Court,Billing Rate\n")

        for case_number, details in case_info.items():
            line = (
                case_number + "," +
                details["Client"] + "," +
                details["Court"] + "," +
                str(details["Billing Rate"]) + "\n"
            )

            file.write(line)

    print("Cases saved successfully!")


#Shows the clients info from dictionary
def show_clients():
    print("\n======= CLIENT LIST =======")

    for case_number, details in case_info.items():
        print(f"\nCase Number: {case_number}")
        print(f"Client: {details['Client']}")
        print(f"Court: {details['Court']}")
        print(f"Billing Rate: ${details['Billing Rate']:.2f}")

#Add the units of hours to specified clients
def add_hours():
    print("\n======= ADD CLIENT HOURS =======")

    case_number = input("Enter Case Number: ")

    if case_number not in case_info:
        print(f"Case number({case_number}) not found.")
        return

    try:
        hours = float(input("Enter Hours Worked: "))

    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if case_number not in client_hours:
        client_hours[case_number] = []

    client_hours[case_number].append(hours)
    print()
    print(f"Added {hours} hours to {case_number}.")
    print(f"Client: {case_info[case_number]['Client']}")

#Display the menu options to user    
def show_menu():
    print("\n======= LAW FIRM BILLING SYSTEM =======")
    print("1. Show Client List")
    print("2. Add Hours")
    print("3. Record or Update Billing Rate")
    print("4. Show Client Hour Entries")
    print("5. Show Total Hours by Billing Rate")
    print("6. Show Monthly Gross Income")
    print("7. Start New Month")
    print("8. View Previous Month")
    print("9. Show Annual Billing Report")
    print("10. Run 30-Day Billing Simulation")
    print("11. Save and Exit")

    
load_cases()

while True:
    show_menu()

    menu_option = input("\nSelect Option: ")

    if menu_option == "1":
        show_clients()
    elif menu_option == "2":
        add_hours()
        
    elif menu_option == "3":
        print("Coming soon")
    elif menu_option == "4":
        print("Coming soon")
    elif menu_option == "5":
        print("Coming soon")
    elif menu_option == "6":
        print("Coming soon")   
    elif menu_option == "7":
        print("Coming soon")   
    elif menu_option == "8":
        print("Coming soon")  
    elif menu_option == "9":
        print("Coming soon")  
    elif menu_option == "10":
        print("Coming soon")
    elif menu_option == "11":
        print("Menu Closed")  
        save_cases()
        break
    else:
        print("Please enter the commands number(1-11)")