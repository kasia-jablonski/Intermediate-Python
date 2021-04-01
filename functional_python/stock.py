import json
from copy import copy
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