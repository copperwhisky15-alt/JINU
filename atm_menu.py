balance = 0
correct_pin = 2403
attempt = 3

while attempt > 0:
    pin = int(input("Enter UPI pin:"))
    if pin == correct_pin:
        print("\nAccess granted ✔️✔️")
        while True:
            print("\n 💳 ATM menu")
            print("\n 1. 💰 CHECK BALANCE")
            print("\n 2. 💵 DEPOSIT")
            print("\n 3. 💸 WITHDRAW")
            print("\n 4. 🚪 EXIT")
            choice = int(input("\nEnter The option:"))
            if option == 1:
                print("Your current balance is: ₹560 💰")
            if option == 2:
                print("Depositing Rupees ₹ 💵")
            if option == 3:
                print("Withdrawing ₹'s 💸")
            else:
                print("Invalid option ❌")
