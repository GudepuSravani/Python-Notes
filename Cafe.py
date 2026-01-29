menu = {
    "coffee":125,"Tea" :20,"samosa":16,"puff":12,"Biscuit":15,"cake":50,
}

print("Welcome to our Order cafe")

print("coffee:125\nTea:20\nsamosa:16\npuff:12\nBiscuit:15\ncake:50")

order_item = input("enter your item:")
order_total = 0

if order_item in menu:
        order_total+=menu[order_item]
        order = input('Do you want anything else (Yes/No)?')

        if order == "yes":
             order_item2 = input("Enter your second item:")

             if order_item2 in menu:
                    order_total += menu[order_item2]
                    print(f'your order value:{order_total}')

             else:
                   print("you entered a wrong item")
   