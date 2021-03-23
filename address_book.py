import re

# Opens a file in Python. This won't contain the content of the file, it just points to it in memory.
names_file = open("names.txt", encoding="utf-8") 
# .read() - Reads the entire contents of the file object it's called on.
data = names_file.read()
# .close() - Closes the file object it's called on. This clears the file out of Python's memory.
names_file.close()

# r'string' - A raw string that makes writing regular expressions easier.
# re.match(pattern, text, flags) - Tries to match a pattern against the beginning of the text.
print(re.match(r'Love', data)) 
# re.search(pattern, text, flags) - Tries to match a pattern anywhere in the text. Returns the first match.
print(re.search(r'Kenneth', data))

'''
If you don't know the size of a file, it's better to read it a chunk at a time and close it automatically. The following snippet does that:

with open("some_file.txt") as open_file:
    data = open_file.read()
'''
# Tries to match pattern of phone number (999) 999-9999
print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
print(re.search(r'\w+, \w+', data))
print(re.findall(r'\w*, \w+', data))

'''
\w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character. In "new-releases-204", \w would match each of the letters in "new" and "releases" and the numbers 2, 0, and 4. It wouldn't match the hyphens.
\W - is the opposite to \w and matches anything that isn't an Unicode word character. In "new-releases-204", \W would only match the hyphens.
\s - matches whitespace, so spaces, tabs, newlines, etc.
\S - matches everything that isn't whitespace.
\d - is how we match any number from 0 to 9
\D - matches anything that isn't a number.
\b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
\B - matches anything that isn't the edges of a word.


\w{3} - matches any three word characters in a row
\w{,3} - matches 0, 1, 2, or 3 word characters in a row.
\w{3,} - matches 3 or more word characters in a row. There's no upper limit.
\w{3, 5} - matches 3, 4, or 5 word characters in a row.
\w? - matches 0 or 1 word characters.
\w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.
\w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.
.findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.


[abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.
[a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.
[0-9] - range that'll match any number from 0 to 9. You can change the ends to restrict the set.


'''

# find all email addresses
print(re.findall(r'[-\w\d+.]+@[-\w\d+.]+', data))
# find words 'treehouse' 
# re.I == re.IGNORECASE
print(re.findall(r'\b[trehous]{9}\b', data, re.I))

'''

    [^abc] - a set that will not match, and, in fact, exclude, the letters 'a', 'b', and 'c'.
    re.IGNORECASE or re.I - flag to make a search case-insensitive. re.match('A', 'apple', re.I) would find the 'a' in 'apple'.
    re.VERBOSE or re.X - flag that allows regular expressions to span multiple lines and contain (ignored) whitespace and comments.
'''
# Find all email addresses without gov
print(re.findall(r'''
    \b@[-\w\d.]*    # First a word boundary, an @, and then any number of characters
    [^gov\t]+       # Ignore 1+ instances of the letters 'g', 'o' or 'v' and a tab
    \b              # Match another word boundary
''', data, re.VERBOSE|re.I))

# Find job and company
print(re.findall(r'''
    \b@[-\w]*,    # First a word boundary, an @, and then any number of characters
    \s            # Find 1 whitespace
    [-\w ]+       # 1+ hyphens and charactes and explicit spaces
    [^\t\n]       # Ignore tabs and newlines
''', data, re.X))

'''

([abc]) - creates a group that contains a set for the letters 'a', 'b', and 'c'. This could be later accessed from the Match object as .group(1)
(?P<name>[abc]) - creates a named group that contains a set for the letters 'a', 'b', and 'c'. This could later be accessed from the Match object as .group('name').
.groups() - method to show all of the groups on a Match object.
re.MULTILINE or re.M - flag to make a pattern regard lines in your text as the beginning or end of a string.
^ - specifies, in a pattern, the beginning of the string.
$ - specifies, in a pattern, the end of the string.

'''

print(re.search(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t  #Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  #Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  #Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t ? #Job and company
    (?P<twitter>@[\w\d]+)?$  #Twitter
''', data, re.X|re.M))

'''

re.compile(pattern, flags) - method to pre-compile and save a regular expression pattern, and any associated flags, for later use.
.groupdict() - method to generate a dictionary from a Match object's groups. The keys will be the group names. The values will be the results of the patterns in the group.
re.finditer() - method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.
.group() - method to access the content of a group. 0 or none is the entire match. 1 through how ever many groups you have will get that group. Or use a group's name to get it if you're using named groups.

'''

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  #Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  #Emailp
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  #Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t ? #Job and company
    (?P<twitter>@[\w\d]+)?$  #Twitter
''', re.X|re.M)

# print(line.search(data).groupdict())

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))