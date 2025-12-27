arr = [1,2,3,4,5,6,7,8,9,10]

# If statements are used to check for boolean values and perform conditional operations
# For statement these are used to iterate over values of a list

names = [{"name":"Ben", "paid_status":True}, {"name":"John", "paid_status":False},{"name":"Claus", "paid_status":False},{"name":"Marvin", "paid_status":True},{"name":"Alex", "paid_status":False}]

# Range is a function that returns a list of number for (i, k). i.e. range(i,k) i optional 

# for i in range(4, 10, 2):
#     print(i)

print(f"Number of items in names list is {len(names)}")


for i in range(len(names)):
    print("Hi my name is "+ names[i]["name"])

# for value in arr:
#     if value % 2 != 0:
#         print(value);    

for name in names:
    if name["paid_status"] == False:
        print(f"Please {name['name']}, please clear your debt before the 24th of this month!")
    else:
        print(f"{name['name']}, thank so much for clearing the debt.")

arr = [1,2,3,4,5]

while len(arr) > 0:
    print(arr.pop())


