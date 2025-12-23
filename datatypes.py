# These are strings
string = "Hello world!sdvs 23e2dewdc"
string1 = 'Hsdvds'

# Integer
integer = 1

# Float
float_number = 1.0

# False = 0 True = 1
boolean_value: bool = False

# List of values
arrays = [1, 2.0, "Hi", True, False]

# no of elements = nth

arrays[0] = 2

# Tuple of values
tuples = (1, 2.0, "Hi", True, False)

tuples = (1, 3, "Hi", True, False)

tuples = (1, 2.0, "Hi", True, True)

# {Key: Value}
dictionary = {"Ssali": "Benjamin", "Samung": "Adrian"}

print(dictionary["Samung"])

print(arrays[0])

students = [
    {"name": "Benjamin", "age": 20},
    {"name": "Adrian", "age": 20},
    {"name": "Arnold", "age": 20}
]

for student in students:
    pass
   # print(f"My name is {student['name']} and I am {student['age']} years old")

# Queue example i.e. First in first out
# Stack
# Linked list
#0,1,2,3....
array = [{"weight":1, "name": "Benjamin", "age": 20}, {"weight":1, "name": "Adrian", "age": 20}, {"weight":2, "name": "Arnold", "age": 20}]

array2 = [{"weight":"second", "name": "Benjamin", "age": 20}, {"weight":"first", "name": "Adrian", "age": 20}, {"weight":"second", "name": "Arnold", "age": 20}]

print("Before...")
print(array)

# Processing
array.pop(0)

print("After")
print(array)

## Adding to our queue 
array.append({"weight":1, "name": "Arnold", "age": 20})

print("After adding to queue")
print(array)




