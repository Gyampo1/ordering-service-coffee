import random
import os

# TABLE SYSTEM: Define the file name
file_name = "orders.txt"

# TABLE SYSTEM: Check if the file already exists.
# If it does NOT exist, create it and write the clean table headers first.
if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write(f"{'ORDER ID':<10} | {'CUSTOMER NAME':<25} | {'COFFEE ITEM':<15} | {'QTY':<5} | {'TOTAL PRICE':<12} | {'COUNTRY':<8} | {'CITY/TOWN':<15} | {'ADDRESS':<25} | {'PHONE NUMBER':<15}\n")
        f.write("-" * 145 + "\n")

# Main program loop to handle multiple orders
while True:
    # OPEN FILE: Open in append mode ('a') to add rows to our table
    f = open(file_name, "a")

    # UNIQUE ID GENERATION: Every new order gets a unique ID
    lower = "bdfghjk"
    numbers = "0123456789"
    string = lower + numbers
    length = 7
    order_id = "".join(random.sample(string, length))

    # WELCOME SCREEN
    print("               \n              \n               \n     ")
    print("                          Welcome to Louis's Coffee Shop")
    print("--------------------\n--------------------")
    print("Hello I am Goodie,\n :Your personal assistance to make an order here at Louis's coffee shop")
    print("--------------------\n--------------------")
    input("[Goodie]: press --enter-- to proceed the ordering process: ")

    # CLEAR SCREEN
    os.system('cls' if os.name == 'nt' else 'clear')

    # USER INFORMATION COLLECTION
    name = input("[Goodie]: what is your firstname?\n : ")
    lastname = input("[Goodie]: What is your lastname?\n : ")
    os.system('cls' if os.name == 'nt' else 'clear')

    # BANNED USERS CHECK
    if name + lastname == "Louis" + "Danso" or name + lastname == "Lincoln" + "Osei":
        print("[Goodie]: You have been banned from this shop, " + name + "!!!\nGoodie: We're so sorry to hear this")
        input("[Goodie]: Press --any key-- to end session")
        f.close()
        exit()
    else:
        print("[Goodie]: Hello " + name + ", thank you so much for joining in today.\n")

    print("-------------------\n-----------------")

    # MENU DISPLAY
    menu = " [*]Black Coffee-$4\n [*]Espresso-$8\n [*]Latte-$5\n [*]Cappuccino-$8\n [*]Frappuccino-$13\n"
    print("[Goodie]: Here is what we are serving.\n" + menu)

    print("[Goodie]Make sure order is on the menu above and is spelt correctly\n [*]NB:Check the capitalization of the words of your order\nIt should be the same as the ones on our menu")
    print("------------------------------------------\n---------------\n------------------------------------------")

    # ITEM SELECTION AND PRICING LOGIC
    order = input("[Goodie]:What would you like, " + name + "?: ")
    if order == "Frappuccino":
        price = 13
    elif order == "Black Coffee":
        price = 4
    elif order == "Latte":
        price = 5
    elif order == "Espresso":
        price = 8
    elif order == "Cappuccino":
        price = 8
    else:
        print("------------------------------------------\n---------------\n------------------------------------------")
        print("[Goodie]: We are sorry we don't have that here... Make sure order is on the menu above and is spelt correctly\n [*]NB:Check the capitalization of the words of your order\nIt should be the same as the ones on our menu")
        input("Thank you!!!\n Press enter to exit and try again later__")
        f.close()
        exit()

    os.system('cls' if os.name == 'nt' else 'clear')

    # QUANTITY INPUT
    number_of_order = int(input("[Goodie]: How many would you like to order?\n : "))
    os.system('cls' if os.name == 'nt' else 'clear')

    # TOTAL CALCULATION & CONFIRMATION
    print("[Goodie]: Sounds good " + name + ", we'll have that " + order + " ready for you in a moment.")
    total = price * number_of_order
    formatted_price = f"${total}.99"
    print("[Goodie]: Your total amount to pay is: " + formatted_price + " (delivery fee included)")

    
    confirmation = int(input("Press 1 to confirm: \n--"))
    if confirmation == 1:
        print("[*]Price Confirmed")
    else:
        print("[Goodie]: Can't continue if you do not confirm")
        input("[Goodie]: Thanks for being with us\nGoodie: press --any key-- to end session")
        f.close()
        exit()

    convert = total * 14
    os.system('cls' if os.name == 'nt' else 'clear')

    # CHECKOUT GATEWAY
    print("--------PAYMENT WOULD BE MADE AFTER CHECKOUT---------")
    checkout = input("Proceed to Checkout: ")
    print("------------------------------------------\n------------------------------------------")
    os.system('cls' if os.name == 'nt' else 'clear')

    # COUNTRY VERIFICATION
    country = input("[Goodie]: Enter country(GH): ")
    print(country)
    if country == "GH":
        print("--" + country + " Confirmed")
    else:
        print("[Goodie]:Make sure country is written as 'GH'")
        input("[Goodie]: Press --any key-- to end session")
        f.close()
        exit()

    os.system('cls' if os.name == 'nt' else 'clear')

    # DELIVERY ADDRESS & CONTACT COLLECTION
    area = input("[Goodie]: City or Town: ")
    print("--" + area + " confirmed")
    house_address = input("[Goodie]: Enter a valid house address: ")
    print("--" + house_address + " confirmed")
    print("[Goodie]: Enter number without country code")
    number = int(input("[Goodie]: Telephone number(+233): "))
    confirm_number = int(input("[Goodie]: Confirm telephone number: "))
    print("-------------------\n--------------------")

    if number == confirm_number:
        print("-- Number verified")
    else:
        print("**Numbers are not the same**")
        print("**Make sure numbers are the same**")
        print("**Thank you so much, " + "and try again next time!!!**")
        input("Press --any key-- to end session")
        f.close()
        exit()

    os.system('cls' if os.name == 'nt' else 'clear')

    # TERMS AND CONDITIONS
    print("------------------\n--------------")
    print("------------------------------------------\n---------------\n------------------------------------------")
    terms_and_conditions = input("*Press --enter-- to see our terms and conditions")
    os.system('cls' if os.name == 'nt' else 'clear')

    print("[Goodie]: Here are our terms and conditions:\n READ THEM CAREFULLY!!!")
    print("Our services are provided to adults over the age of eighteen (18) years.")
    print("By proceeding to purchase through here,")
    print("You acknowledge that you are over 18 years of age and you are accepting our terms and services.")

    proceed = int(input("Press 1 to proceed: "))
    if proceed == 1:
        print("ok")
    else:
        input("could not continue... press --any key-- to end session ")
        f.close()
        exit()

    os.system('cls' if os.name == 'nt' else 'clear')

    print("-----------------------------------------------------------------------")
    Get_order_info = input("*press --enter-- for order info.__ ")
    print("-----------------------------------------------------------------------")
    print("\n \n")

    # COMBINE NAMES AND TELEPHONE FOR CLEAN ROWS
    full_name = f"{lastname} {name}"
    phone_formatted = f"0{number}"

    # TABLE FILE WRITE SYSTEM: Writes fields into spacing blocks so they line up vertically under the table headers
    f.write(f"{order_id:<10} | {full_name:<25} | {order:<15} | {number_of_order:<5} | {formatted_price:<12} | {country:<8} | {area:<15} | {house_address:<25} | {phone_formatted:<15}\n")
    f.close() # Safely close file to save changes permanently

    os.system('cls' if os.name == 'nt' else 'clear')

    # INVOICE DISPLAY OUTPUT
    print("[Goodie]: Here is your order info\n-------\n-------")
    print("[*]ORDER ID:" + order_id)
    print("[*]ORDER status: Pending")
    print("----------\n---------")
    print("[Goodie]: THANK YOU FOR BUYING FROM US\nGoodie: HOPING TO SEE YOU AGAIN!!!")
    print("-----------------------------------------------------------------------")
    print("[Goodie]: CONTACT OUR TOLL FREE NUMBERS: 0507693544 or 0598440737 TO MAKE PAYMENT")
    print("-----------------------------------------------------------------------")
    print("********************************")
    print("********************************")
    print("CALL US BEFORE ENDING SESSION")
    print("********************************")
    print("********************************")
    print("-----------------------------------------------------------------------")

    # LOOP BREAKER TERMINATION CHECK
    again = input("\nAdd another order? y/n: ")
    if again.lower() != 'y':
        print("Thank You, Goodbye!")
        break

exit()
