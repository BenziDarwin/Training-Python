from datetime import datetime

name = input("What is your name? ")

if datetime.now().hour < 12:
    print(f"Good morning, {name}")
elif datetime.now().hour < 17:
    print(f"Good afternoon, {name}")
elif datetime.now().hour < 22:
    print(f"Good evening, {name}")
else:
    print(f"Good night, {name}")
