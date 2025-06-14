#define the menu of resturant
menu = {
    'pizza': 299,   'burger': 99,
    'pasta': 149,
    'coldcoffee': 49,
    'chickenwings': 399,
    'momos': 80 
}

  

# greet
print("WELCOME TO OUR CAFE")
print(" pizza: RS299\n burger: Rs99\n pasta: Rs149\n coldcoffee: Rs49\n chickenwings: Rs399\n momos: Rs80")

order_total = 0
item_1 = input("Please Enter the name of item you want to order =")
if item_1 in menu: 
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else :
    print("Please order something that is in our menu")
    
another_order =   input("Do you want to add something else ? (Yes/No)")
if another_order == "Yes":
     item_2 = input("please enter the name of second item = ")
     if item_2 in menu:
         order_total += menu[item_2]
         print(f"item {item_2} has been added")
     else :
      print("Please order something that is in our menu")
      
print(f"Total amount to pay is {order_total}")
        
 