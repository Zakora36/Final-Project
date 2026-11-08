#first two features: one that shows your data and one that adds or updates your data

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

    

while True:
    show_menu()

    menu_option = input("\nSelect Option: ")

    if menu_option == "1":
        show_clients()
    elif menu_option == "2":
        add_hours()

    elif menu_option == "3":
        print("n/c update_rate()")
    elif menu_option == "4":
        print("n/c show_client_entires()")
    elif menu_option == "5":
        print("n/c calc_rate_total()")
    elif menu_option == "6":
        print("n/c calc_month_total()")   
    elif menu_option == "7":
        print("n/c add_month()")   
    elif menu_option == "8":
        print("n/c load_past_month()")  
    elif menu_option == "9":
        print("n/c generate_annual_report()")  
    elif menu_option == "10":
        print("n/c run_simulation()")
    elif menu_option == "11":
        print("Menu Closed")  
        break
    else:
        print("Please enter the commands number(1-11)")