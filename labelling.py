from functions import pricing_for_labelling

while True:
    item_name = input("Input item you want to label: \n")
    quantity = input("Input Quantity of item: \n")

    try:
        if int(quantity) <= 0:
            print("Please enter a valid quantity.")
            raise Exception()
        
        if bool(item_name) == False:
            print("Please enter actual item name.")
            raise Exception()
        
        total = pricing_for_labelling(item_name, int(quantity))
        print(f"Total cost for labelling {item_name} will be {total}.")

    except Exception:
        print("Dont enter string in quantity.")





