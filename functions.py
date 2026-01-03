from datetime import datetime

def greeter(name:str):
    if datetime.now().hour < 12:
        print(f"Good morning, {name}")
    elif datetime.now().hour < 17:
        print(f"Good afternoon, {name}")
    elif datetime.now().hour < 22:
        print(f"Good evening, {name}")
    else:
        print(f"Good night, {name}")


data = {
    "bottles": 500,
    "shirts": 200,
    "pens": 100
}


def pricing_for_labelling(item_name:str, quantity:int):
    if item_name not in data.keys():
        print("Item not registered!")
        return
    
    price = data[item_name]
    total_amount = price * quantity

    return total_amount
    
    