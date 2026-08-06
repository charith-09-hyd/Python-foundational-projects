def display_menu():
    
    print("""
WELCOME TO "ABCD" RESTAURANT 

PLEASE CHOOSE FROM OUR CURATED MENU 

    ::::::::::::::  MENU  :::::::::::::::::

              MAIN COURSES


    1....... VEG BURGER                                  250

    2....... LAMB BURGER                                 400

    3....... CHICKEN BURGER                              350

    4....... GINGER BREAD(4 pieces)                      200

    5....... GRILLED CHICKEN PIZZA                       550

    6....... BELL PEPPER CHICKEN PIZZA                   650

    7....... ROTTISERIE CHICKEN(whole)+ SOUP             900

    8....... BUFFALO SAUCE CHICKEN WINGS                 720

    9....... CHICKEN CAESAR SALAD                        370

    10...... LAMB CHOPS(8 pieces)                        1200

    11...... LAMB RIBS(10 pieces)                        1450

        
            DESSERTS 

    12...... CHOCOLATE MATCHA BURST                       450

    13...... CHOCOLATE ECLAIRS                            250

    14...... CHOCOLATE BISCOFF CAKE                       450

    15...... RED VELVET CAKE SLICE                        300

    16...... CHOCOLATE BROWNIE+ICE CREAM                  550

    17...... NYC CHEESECAKE                               500

    18...... MUD MAN LAVA CAKE                            450

    19...... CHOCOLATE COOKIE(1 piece)                    100

    20...... GINGER COOKIE(1 piece)                       100

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

""")



    display_menu()
    




menu = {
    
    1: ("1 ...... Veg Burger",250),

    2: ("2...... Lamb Burger",400),

    3: ("3...... Chicken Burger",350),

    4: ("4...... Ginger Bread(4 pieces)",200),

    5: ("5...... Grilled Chicken pizza",550),

    6: ("6...... bell pepper Chiken pizza",650),

    7: ("7...... Rottiserie Chicken(whole)+soup",900),

    8: ("8...... Buffalo sauce chicken wings",720),

    9: ("9...... Chicken Caesar Salad",370),

    10: ("10..... Lamb chops (8 pieces)",1200),

    11: ("11..... Lamb Ribs (10 pieces)",1450),

    
    12: ("12..... Chocolate matcha burst",450),

    13: ("13..... Chocolate eclairs",250),

    14: ("14..... Chocolate biscoff cake",450),

    15: ("15..... Red vevlet cake slice",300),

    16: ("16..... Chocolate Brownie + ice cream",550),

    17: ("17..... NYC Cheesecake",500),

    18: ("18..... Mud Man lava Cake",450),
    
    19: ("19..... Chocolate cookie( 1 piece)",100),
    
    20: ("20..... Ginger cookie( 1 piece)",100),


    
}

subtotal = 0 
choice = int(input("ENTER ITEM NUMBERS FROM 1-20: "))
if choice in menu: 
    item_name, price = menu[choice]

    print("ITEM SELECTED:", item_name)

    quantity = int(input("Enter quantity: ")) 

    item_total = price * quantity 

    subtotal += item_total 

    
    print("PRICE IN INR:", price)
    print("QUANTITY: ", quantity)
    print("TOTAL COST: ", item_total)
    print("SUBTOTAL", subtotal )  
     
else:
    print("INVALID ITEM NUMBER SELECT FROM 1-20")


    






