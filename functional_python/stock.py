import json
from copy import copy
from functools import partial, reduce
from operator import attrgetter, itemgetter


class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return str(self)
    
    
def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]


'''
sorted() takes an iterable to sort and returns a new list from it. If you need to customize the sorting, pass a function in as the key argument. There's an optional reverse argument that will cause the results to be reversed before they're returned.

operator.itemgetter()gets items from an object that supports that operation. We use it to get keys from dicts but it has other uses too.

operator.attrgetter() gets attributes from an object.

reversed() takes an iterable and reverses it, returning a new iterable. This new iterable has to be turned into a list/tuple/etc to get items from it by index.
'''
    
BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)

pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])

pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'), reverse=True)
print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)

#important_list = [5, 3, 1, 2, 4]
#important_list.sort()  # Bad idea, sorts list in place
#sorted(important_list) # Sorts a copy of the list
# print(sorted(important_list))
# print(important_list)

# Map applied a function to every item that's iterable
a = [1, 2, 3]
def double(n):
    return n*2
print(list(map(double, a)))

def sales_price(book):
    """Apply a 20% discount to the book's price"""
    book = copy(book)
    book.price = round(book.price-book.price*.2, 2)
    return book

sales_book = list(map(sales_price, BOOKS))
# The same as list comprehension:
sales_book2 = [sales_price(book) for book in BOOKS]
print(sales_book[0].price)
print(BOOKS[0].price)
'''
map() takes a function and an iterable. The function should take a single argument. This function will be applied, in order, to each item in the iterable and the result of that function will be returned to map(). In the end, map() will return a new iterable with the mutated values.

[func(item) for item in iterable] achieves the same result, plus turns the results into a list. For simple, single-serving applications, this is often a better choice since it's often more readable at a glance.
'''

### FILTER ###
def is_long_book(book):
    """Does a book have 600+ pages?"""
    return book.number_of_pages >= 600

long_books = list(filter(is_long_book, BOOKS))
# Tha same as comprehension:
long_books2 = [book for book in BOOKS if book.number_of_pages >= 600] # / if is_long_book(book)

print(len(BOOKS)) # 28
print(len(long_books)) # 12
'''
filter() takes a function and an iterable. The function, like with map(), takes only a single argument and is applied to each item in the iterable. If the function returns a truthy value for the item, the item is sent back to filter() which, ultimately, returns a new iterable of the filtered items.

You can achieve the same effect with [item for item in iterable if func(item)]. Again, like with map(), this can be more quickly readable for small applications.

filterfalse() works just like filter() but only returns things where the filter function gives back a False or non-truthy value.
'''

### CHAINING ###
def has_roland(book):
    return any(["Roland" in subject for subject in book.subjects])

def titlecase(book):
    book = copy(book)
    book.title = book.title.title()
    return book

# print(list(map(titlecase, filter(has_roland, BOOKS))))
def is_good_deal(book):
    return book.price <= 5
# Looks for books that are on sale cheaper than $5 and sorts by price
cheap_books = sorted(
    filter(is_good_deal, map(sales_price, BOOKS)),
    key=attrgetter('price')
)
print(cheap_books[0].price) # 2.8

'''
Since filter(), map(), sorted() all return iterables, we can chain them together. Chained functions resolve, or happen, from the inside out, so the innermost function runs first.

This is another reason why functions usually return a value at the end. It makes it easier to use them all together.

any(iterable) returns True if any of the items in the iterable are truthy. Similar is the function all(). all(iterable) returns True if all of the items in the iterable are truthy.
'''

### REDUCE ###
def product(x, y):
    return x * y

print(reduce(product, [1, 2, 3, 4, 5])) # 120

def add_book_prices(book1, book2):
    return book1 + book2

total = (reduce(add_book_prices, [b.price for b in BOOKS]))
print(total)    # 225.30

'''
functools.reduce() takes a function and an iterable. The function, though, takes two arguments. The first time it runs, the two arguments will be the first two items in the iterable. Every time after that, the first argument will be the result of the last time the function was run. The second argument will be the next value from the iterable. When the iterable is out of items, reduce() will return whatever the function returned last.

Think about adding up all of the numbers in a column. You add the top two, then add the third number to the sum you got from the first two. Then you add the fourth number to the sum of the top three, and so on.

Calling a function over again from within itself is known as recursion and it's what makes reduce() able to do its job.
'''

### LAMBDA ###
total = reduce(lambda x, y: x + y, [b.price for b in BOOKS])
long_books = filter(lambda book: book.number_of_pages >=600, BOOKS)
good_deals = filter(lambda book: book.price <= 6, BOOKS)

'''
lambda, like def, is the keyword that marks a new function. Lambda functions don't have to have a name, though.

Lambdas can't contain new lines (outside of containers) or assignments.
'''

### PARTIALS ###
def mark_down(book, discount):
    book = copy(book)
    book.price = round(book.price - book.price*discount, 2)
    return book

standard = partial(mark_down, discount=.2)
# print(standard(BOOKS[0]).price)
half = partial(mark_down, discount=.5)
half_price_books = map(half, filter(is_long_book, BOOKS))

'''
functools.partial lets you preset some arguments to a function. You can then call the new function with the remaining arguments as needed. This often ends up being really handy when used with map() and filter().
'''