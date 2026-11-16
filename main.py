
transactions = []
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

def load_transactions():
    global transactions
    transactions = []

    try:
        with open("transactions.csv", "r") as file:
            next(file)  # Skip the header

            for line in file:
                line = line.strip()

                case_number, date, hours, description, amount = line.split(",")

                transactions.append({
                    "Case Number": case_number,
                    "Date": date,
                    "Hours": float(hours),
                    "Description": description,
                    "Amount": float(amount)
                })

    except FileNotFoundError:
        print("No existing transaction file found.")

    return transactions

def record_transaction():

    case_number = input("Enter the case number: ")

    # Check if the case exists
    if case_number not in case_info:
        print("Error: Case number does not exist.")
        return

    date = input("Enter the date (YYYY-MM-DD): ")

    try:
        hours = float(input("Enter hours worked: "))

        if hours <= 0:
            print("Error: Hours must be greater than zero.")
            return

    except ValueError:
        print("Error: Please enter a valid number of hours.")
        return

    description = input("Enter a description of the work: ")

    # Calculate the billing amount
    rate = case_info[case_number]["Billing Rate"]
    amount = hours * rate

    # Create the transaction dictionary
    transaction = {
        "Case Number": case_number,
        "Date": date,
        "Hours": hours,
        "Description": description,
        "Amount": amount
    }

    # Add transaction to the list
    transactions.append(transaction)

    print("Transaction recorded successfully!")
    print(f"Total amount billed: ${amount:.2f}")



def view_transactions():

    if not transactions:
        print("No transactions have been recorded.")
        return

    for transaction in transactions:
        print("-------------------------")
        print("Case:", transaction["Case Number"])
        print("Date:", transaction["Date"])
        print("Hours:", transaction["Hours"])
        print("Description:", transaction["Description"])
        print(f"Amount: ${transaction['Amount']:.2f}")



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



def save_transactions():
    with open("transactions.csv", "w") as file:

        file.write("Case Number,Date,Hours,Description,Amount\n")

        for transaction in transactions:

            line = (
                transaction["Case Number"] + "," +
                transaction["Date"] + "," +
                str(transaction["Hours"]) + "," +
                transaction["Description"] + "," +
                str(transaction["Amount"]) + "\n"
            )

            file.write(line)

    print("Transactions saved successfully!")

#Shows the clients info from dictionary
def show_clients():
    print("\n======= CLIENT LIST =======")

    for case_number, details in case_info.items():
        print(f"\nCase Number: {case_number}")
        print(f"Client: {details['Client']}")
        print(f"Court: {details['Court']}")
        print(f"Billing Rate: ${details['Billing Rate']:.2f}")



#Display the menu options to user    
def show_menu():
    print("\n======= LAW FIRM BILLING SYSTEM =======")
    print("1. Show Client List")
    print("2. Record Transactions")
    print("3. Record or Update Billing Rate")
    print("4. Show Client Transactions")
    print("5. Show Total Hours by Billing Rate")
    print("6. Show Monthly Gross Income")
    print("7. Start New Month")
    print("8. View Previous Month")
    print("9. Show Annual Billing Report")
    print("10. Run 30-Day Billing Simulation")
    print("11. Save and Exit")

    
load_cases()
load_transactions()

while True:
    show_menu()

    menu_option = input("\nSelect Option: ")

    if menu_option == "1":
        show_clients()
    elif menu_option == "2":
        record_transaction()

    elif menu_option == "3":
        print("Coming soon")
    elif menu_option == "4":
        view_transactions()
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
        save_transactions()
        break
    else:
        print("Please enter the commands number(1-11)")