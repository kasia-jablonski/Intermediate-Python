nums = range(5, 101)
halves = []
for num in nums:
    halves.append(num/2)

halves = [num/2 for num in nums]

rows = range(4) 
cols = range(10)
[(x, y) for y in rows for x in cols]
# [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3)]

[(letter, number) for number in range(1, 5) for letter in 'abc']
# [('a', 1), ('b', 1), ('c', 1), ('a', 2), ('b', 2), ('c', 2), ('a', 3), ('b', 3), ('c', 3), ('a', 4), ('b', 4), ('c', 4)]

{number: letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))}
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

{student: points for student, points in zip(['Kenneth', 'Dave', 'Joy'], [123, 456, 789])}
# {'Kenneth': 123, 'Dave': 456, 'Joy': 789}

total_nums = range(1, 101)
fizzbuzzes = {
    'fizz': [n for n in total_nums if n % 3 == 0],
    'buzz' : [n for n in total_nums if n % 7 == 0] 
}
fizzbuzzes = {key: set(value) for key, value in fizzbuzzes.items()}
# {'fizz': {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99}, 'buzz': {98, 35, 70, 7, 42, 77, 14, 49, 84, 21, 56, 91, 28, 63}}

fizzbuzzes['fizzbuzz'] = {n for n in fizzbuzzes['fizz'].intersection(fizzbuzzes['buzz'])}
fizzbuzzes['fizzbuzz']
# {42, 84, 21, 63}