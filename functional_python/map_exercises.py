# Write a Python program to triple all numbers of a given list of integers.
list1 = [1, 2, 3, 4, 5]
def triple(a):
    return a*3
triple_list = list(map(triple, list1))

# 2. Write a Python program to add three given lists using Python map and lambda.

# 3. Write a Python program to listify the list of given strings individually using Python map.
s = ["aaaa", "bbb", "ccc"]
def listify_strings(strings):
    l = []
    for string in strings:
        l.append(string)
    return l
s2 = list(map(listify_strings, s))

# 4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
def raised_to_power(number, power):
    return number ** power

powers = list(map(raised_to_power, list1, range(0, len(list1))))

# 5. Write a Python program to square the elements of a list using map() function.
def square(num):
    return num ** 2
squared = list(map(square, list1))

# 6. Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function.
sequence = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
def converter(s):
    return s.upper(), s.lower()

letters = set(map(converter, sequence))

# 7. Write a Python program to add two given lists and find the difference between lists. Use map() function.
def add(x, y):
    return x + y, x - y
list2 = [0, 2, 4, 6, 8]
added_lists = list(map(add, list1, list2))

# 8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.
tuple = (5, 8, 7, 2, 9)
l_str = list(map(str, tuple))

# 9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer.

# 10. Write a Python program to compute the square of first N Fibonacci numbers, using map function and generate a list of the numbers. Go to the editor
# Click me to see the sample solution

# 11. Write a Python program to compute the sum of elements of an given array of integers, use map() function. Go to the editor
# Click me to see the sample solution

# 12. Write a Python program to find the ration of positive numbers, negative numbers and zeroes in an array of integers. Go to the editor
# Click me to see the sample solution

# 13. Write a Python program to count the same pair in two given lists. use map() function. Go to the editor
# Click me to see the sample solution

# 14. Write a Python program to interleave two given list into another list randomly using map() function. Go to the editor
# Click me to see the sample solution

# 15. Write a Python program to split a given dictionary of lists into list of dictionaries using map function. Go to the editor
# Click me to see the sample solution

# 16. Write a Python program to convert a given list of strings into list of lists using map function. Go to the editor
# Click me to see the sample solution

# 17. Write a Python program to convert a given list of tuples to a list of strings using map function.