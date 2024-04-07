def addFounds(founds):
    done = 0
    while done == 0:
        print()
        add = input("Choose between 5, 10, 50, 100 or 200 to add to your founds: ")
        print()
        if add == "5" or add == "10" or add == "50" or add == "100" or add == "200":
            add = int(add)
            founds = founds + add
            done = 1
            print("Founds were added succesfully!")
            print()
        else:
            done = 0
    return founds

def menu(menu_q,menu_items,founds):
    buyed = 0
    validationCode = False
    if founds >= 5:
        for i in range(len(menu_items)):
            print(f"Q: {menu_q[i]} / P: {menu_items[i]} / Code = {i+1} / Price = $10")
        while buyed == 0:
            print()
            while validationCode == False:
                code = int(input("Please select 1 item to retire."))
                print("Checking stock and verifications...")
                if code > 0 and code < 11 and menu_q[code-1] > 0 and founds >= 10:
                    menu_q[code-1] = menu_q[code-1] - 1
                    founds = founds - 10
                    validationCode = True
                    buyed = 1
                else:
                    print("Out of stock.")
                    validationCode = True
                    buyed = 1
    else:
        print()
        print("Not enough founds.")
        print()
    return menu_q,menu_items,founds
    
                                    
            
                
    

def main():
    founds = 0
    menuQuantities = [10,10,10,10,10,10,10,10,10,10]
    menu_items = ["Potato Chips","Chocolate Bar","Bottled Water","Granola Bar","Pretzels","Fruit Snacks","Soda (Regular)","Energy Drink","Mixed Nuts","Gum"]
    while True:
        print("Welcome to our vending machine!!")
        print("Please, select one of the options below to continue:")
        print()
        print("1. Add founds.")
        print("2. Consult your founds.")
        print("3. Go to the Vending Menu.")
        print("4. Exit.")
        print()
        choose = input("Go to: ")
        if choose == "1":
            founds = addFounds(founds)
        elif choose == "2":
            print()
            print(f"Your actual founds are: {founds}")
            print()
        elif choose == "3":
            menuQuantities,menu_items,founds = menu(menuQuantities,menu_items,founds)
        elif choose == "4":
            return print("Bye Bye!")
        else:
            print()
            print("Invalid option.")
            print()
main()