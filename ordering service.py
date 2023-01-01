import random

f = open("orders.txt", "w")

lower = "bdfghjk"
numbers = "0123456789"
string = lower + numbers
length = 7
order_id = "".join(random.sample(string, length))

print("               \n              \n               \n     ")
print("                          Welcome to Louis's Coffee Shop")
print("--------------------\n--------------------")
print("Hello I am Goodie,\n :Your personal assistance to make an order here at Louis's coffee shop")
print("--------------------\n--------------------")
input("[Goodie]: press --enter-- to proceed the ordering process: ")
name = input("[Goodie]: what is your firstname?\n : ")
lastname = input("[Goodie]: What is your lastname?\n :")

if name + lastname == "Louis" + "Danso" or name + lastname =="Lincoln" + "Osei":
    print("[Goodie]: You have been banned from this shop, " + name + "!!!\nGoodie: We're so sorry to hear this")
    print(input("[Goodie]: Press --any key-- to end session"))
    exit()
else:
    print("[Goodie]: Hello " + name + ", thank you so much for joining in today.\n")
print("-------------------\n-----------------")
menu = " [*]Black coffee-$4\n [*]Espresso-$8\n [*]Latte-$5\n [*]Cappuccino-$8\n [*]Frappuccino-$13\n"
#price = 8
print("[Goodie]: Here is what we are serving.\n" + menu)

print("[Goodie]Make sure order is on the menu above and is spelt correctly\n [*]NB:Check the capitalization of the words of your order\nIt should be the same as the ones on our menu")
print("------------------------------------------\n---------------\n------------------------------------------")
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
    print(
        "[Goodie]: We are sorry we don't have that here... Make sure order is on the menu above and is spelt correctly\n [*]NB:Check the capitalization of the words of your order\nIt should be the same as the ones on our menu")
    print(input("Thank you!!!\n Press 1 to exit and try again later__"))
    exit()


number_of_order = int(input("[Goodie]: How many would you like to order?\n : "))
print("[Goodie]: Sounds good " + name + ", we'll have that " + order + " ready for you in a moment.")
total = price * number_of_order
print("[Goodie]: Your total amount to pay is: $" + str(total) + ".99" + " (delivery fee included)")
confirmation = int(input("Press 1 to confirm: \n--"))
if confirmation == int(1):
    print("[*]Price Confirmed")
else:
    print("[Goodie]: Can't continue if you do not confirm")
    print(input("[Goodie]: Thanks for being with us\nGoodie: press --any key-- to end session"))
    exit()
convert = total * 14
print("--------PAYMENT WOULD BE MADE AFTER CHECKOUT---------")
checkout = input("Proceed to Checkout: ")
print("------------------------------------------\n------------------------------------------")
country = (input("[Goodie]: Enter country(GH): "))
print(country)
if country == "GH":
    print("--" + country + " Confirmed")
else:
    print("[Goodie]:Make sure country is written as 'GH'")
    print("[Goodie]: Press --any key-- to end session")
    exit()

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
    print(input("Press --any key-- to end session"))
    exit()
print("------------------\n--------------")
print("------------------------------------------\n---------------\n------------------------------------------")
terms_and_conditions = input("*Press --enter-- to see our terms and conditions")

print("[Goodie]: Here are our terms and conditions:\n READ THEM CAREFULLY!!!")
print("Our services are provided to adults over the age of eighteen (18) years.")
print("By proceeding to purchase through here,")
print("You acknowledge that you are over 18 years of age and you are accepting our terms and services.")
proceed = int(input("Press 1 to proceed: "))
if proceed == 1:
    print("ok")
else:
    print(input("could not continue... press --any key-- to end session "))
    exit()
print("-----------------------------------------------------------------------")
Get_order_info = input("*press --enter-- for order info.__ ")
print("-----------------------------------------------------------------------")
print("\n \n")


# makes or opens a file called orders.py
f.write("*Order ID: " + str(order_id ) + "\n\n")
f.write("*Name: " + str(lastname) + " " + str(name) + "\n\n")
f.write("*Type of coffee ordered: " + str(order) + "\n\n")
f.write("*Number of coffee ordered: " + str(number_of_order) + "\n\n")
f.write("*Price to be paid: " + "$" + str(total) + ".99\n\n")
f.write("*Country: " + str(country) + "\n\n")
f.write("*Area: " + str(area) + "\n\n")
f.write("*Address: " + str(house_address) + "\n\n")
f.write("*Number: " +str(0) + str(number) + "\n\n")

f.close()

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
print(input("Press ---any key--- to end session: "))

import turtle

t = turtle.Turtle()

t.speed(100)
turtle.bgcolor("black")

for i in range(240):
    t.color("cyan")
    t.circle(i)
    t.left(5)

turtle.done()


exit()
