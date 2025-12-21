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

# Tuple of values
tuples = (1, 2.0, "Hi", True, False)

tuples = (1, 2.0, "Hi", True, True)

# {Key: Value}
dictionary = {"iphone1" : "Benjamin", "Samung": "Adrian"}

print(dictionary["iphone1"])

print(array[0])

students = [
    {"name": "Benjamin", "age": 20},
    {"name": "Adrian", "age": 20},
    {"name": "Arnold", "age": 20}
]

for student in students:
    pass
   # print(f"My name is {student['name']} and I am {student['age']} years old")

# Queue example i.e. First in first out
#0,1,2,3....
array = [{"weight":1, "name": "Benjamin", "age": 20}, {"weight":1, "name": "Adrian", "age": 20}, {"weight":2, "name": "Arnold", "age": 20}]

array2 = [{"weight":"second", "name": "Benjamin", "age": 20}, {"weight":"first", "name": "Adrian", "age": 20}, {"weight":"second", "name": "Arnold", "age": 20}]
print("Before...")
print(array2)
# Adding to Queue


for va in array2:
    if va["weight"] == "first":
        array2.remove(va)
    else:
        pass

print("After...")
print(array2)



