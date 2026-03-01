from abc import ABC, abstractmethod


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Alice", 30)
person1.greet()


"""
inheritance example
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def greet(self):
        print(f"{self.name} says Hello!")


class Cat(Animal):  # Inherits from Animal
    def speak(self):
        print(f"{self.name} says Meow!")


cat1 = Cat("Whiskers")
cat1.speak()  # Output: Whiskers says Meow!
cat1.greet()  # Output: Whiskers says Hello!


# Polymorphism example
class Dog(Animal):  # Inherits from Animal
    def speak(self):
        print(f"{self.name} says Woof!")


dog1 = Dog("Buddy")
dog1.speak()  # Output: Buddy says Woof!
dog1.greet()  # Output: Buddy says Hello!


# Encapsulation example
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance


account1 = BankAccount("Alice", 1000)
account1.deposit(500)  # Output: 500 deposited. New balance: 1500
account1.withdraw(200)  # Output: 200 withdrawn. New balance: 1300
# Output: Current balance: 1300
print(f"Current balance: {account1.get_balance()}")


# Abstraction example


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


circle1 = Circle(5)
# Output: Area of the circle: 78.5
print(f"Area of the circle: {circle1.area()}")

# Output: Hello world
print("Hello world")


# Dictionary example
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# Output: Alice
print(my_dict["name"])
# Output: 30
print(my_dict["age"])
# Output: New York
print(my_dict["city"])
# add a new key-value pair to the dictionary
my_dict["country"] = "USA"
# Output: USA
print(my_dict["country"])
# get all keys in the dictionary
print(my_dict.keys())
# get all values in the dictionary
print(my_dict.values())
# get all items in the dictionary
print(my_dict.items())
# update a value in the dictionary
my_dict["age"] = 31
# Output: 31
print(my_dict["age"])
# check if a key exists in the dictionary
if "name" in my_dict:
    print("Name key exists in the dictionary.")
# Output: Name key exists in the dictionary.
# remove a key-value pair from the dictionary
del my_dict["city"]
# Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}
print(my_dict)

# nested dictionary example
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
# Output: Alice
print(nested_dict["person1"]["name"])
# Output: 25
print(nested_dict["person2"]["age"])
# add a new key-value pair to the nested dictionary
nested_dict["person3"] = {"name": "Charlie", "age": 35}
# Output: {'name': 'Charlie', 'age': 35}
print(nested_dict["person3"])
# Output: {'person1': {'name': 'Alice', 'age': 30}, 'person2': {'name': 'Bob', 'age': 25}, 'person3': {'name': 'Charlie', 'age': 35}}
print(nested_dict)
# update a value in the nested dictionary
nested_dict["person1"]["age"] = 31
# Output: 31
print(nested_dict["person1"]["age"])
# remove a key-value pair from the nested dictionary
del nested_dict["person2"]
# Output: {'person1': {'name': 'Alice', 'age': 31},
# 'person3': {'name': 'Charlie', 'age': 35}}
print(nested_dict)


# List example
my_list = [1, 2, 3, 4, 5]
# Output: 1
print(my_list[0])
# Output: 5
print(my_list[4])

# Tuple example
my_tuple = (1, 2, 3, 4, 5)
# Output: 1
print(my_tuple[0])
# Output: 5
print(my_tuple[4])
# Output: (1, 2, 3, 4, 5)
print(my_tuple)
# get the length of the tuple
# Output: 5
print(len(my_tuple))
# get the index of a value in the tuple
# Output: 2
print(my_tuple.index(3))
# update a value in the tuple (this will raise an error because tuples are immutable)
# my_tuple[0] = 10  # This will raise a TypeError: 'tuple' object does not support item assignment
# delete a value in the tuple (this will raise an error because tuples are immutable)
# del my_tuple[0]  # This will raise a TypeError: 'tuple'
# slice the tuple
# Output: (2, 3, 4)
print(my_tuple[1:4])
# add a new value to the tuple (this will create a new tuple because tuples are immutable)
new_tuple = my_tuple + (6,)
# Output: (1, 2, 3, 4, 5, 6)
print(new_tuple)
# check the duplicate values in the tuple
my_tuple_with_duplicates = (1, 2, 3, 4, 5, 1, 2, 3)
# Output: (1, 2, 3, 4, 5, 1, 2, 3)
print(my_tuple_with_duplicates)
# convert the tuple to a set to remove duplicates
unique_values = set(my_tuple_with_duplicates)
# Output: {1, 2, 3, 4, 5}
print(unique_values)


# Set example
my_set = {1, 2, 3, 4, 5}
# Output: {1, 2, 3, 4, 5}
print(my_set)
# add a new value to the set
my_set.add(6)
# Output: {1, 2, 3, 4, 5, 6}
print(my_set)
# remove a value from the set
my_set.remove(3)
# Output: {1, 2, 4, 5, 6}
print(my_set)
# check if a value exists in the set
if 2 in my_set:
    print("2 exists in the set.")
# Output: 2 exists in the set.
# get the length of the set
# Output: 5
print(len(my_set))
# delete the set
del my_set
# clear the set (this will raise an error because the set has been deleted)
# my_set.clear()  # This will raise a NameError: name 'my_set' is not defined


# for loop example
for i in range(5):
    # Output: 0, 1, 2, 3, 4
    print(i)

# while loop example
count = 0
while count < 5:
    # Output: 0, 1, 2, 3, 4
    print(count)
    count += 1
