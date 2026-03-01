# Basic Python Functions
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))

# Simple addition function


def add(a, b):
    return a + b


print("2 + 3 =", add(2, 3))

# Factorial function (recursive)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("Factorial of 5 is", factorial(5))

# Fibonacci function (recursive)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci of 10 is", fibonacci(10))

# Check if a number is prime


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


print("Is 17 prime?", is_prime(17))

# Reverse a string


def reverse_string(s):
    return s[::-1]


print("Reversed 'Hello' is", reverse_string("Hello"))

# Count words in a string


def count_words(s):
    return len(s.split())


print("Number of words in 'Hello World' is", count_words("Hello World"))

# Square function


def square(n):
    return n * n


print("Square of 4 is", square(4))

# Cube function


def cube(n):
    return n * n * n


print("Cube of 3 is", cube(3))

# Power function


def power(base, exponent):
    return base ** exponent


print("2 raised to the power of 3 is", power(2, 3))

# Greatest Common Divisor (GCD)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print("GCD of 48 and 18 is", gcd(48, 18))

# Least Common Multiple (LCM)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


print("LCM of 4 and 6 is", lcm(4, 6))

# Check if a string is a palindrome


def is_palindrome(s):
    return s == s[::-1]


print("Is 'racecar' a palindrome?",
      is_palindrome("racecar"))

# Count vowels


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


print("Number of vowels in 'Hello World' is", count_vowels("Hello World"))

# Count consonants


def count_consonants(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char.isalpha() and char not in vowels)


print("Number of consonants in 'Hello World' is",
      count_consonants("Hello World"))

# Anagram check


def is_anagram(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())


print("Are 'listen' and 'silent' anagrams?", is_anagram("listen", "silent"))

# Iterative version of Fibonacci


def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print("Fibonacci of 10 (iterative) is", fibonacci_iterative(10))

# Additional functions


def calculate_total_price(prices, tax_rate):
    total = sum(prices)
    total_with_tax = total * (1 + tax_rate)
    return total_with_tax


print("Total price with tax is", calculate_total_price([10, 20, 30], 0.07))

# global variable example
counter = 0


def increment_counter():
    global counter
    counter += 1
    return counter


print("Counter after incrementing:", increment_counter())

# double a number


def double(n):
    return n * 2


print("Double of 5 is", double(5))

# store in a variable
result = double(5)

print("Result stored in variable is", result)

# use in conditional statement
if double(5) > 10:
    print("Double of 5 is greater than 10")
else:
    print("Double of 5 is not greater than 10")
