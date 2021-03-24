import csv

with open('teachers.csv', 'a') as csvfile:
    fieldnames = ['first_name', 'last_name', 'topic']
    teachwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    teachwriter.writeheader()
    teachwriter.writerow({
        'first_name': 'Kenneth',
        'last_name': 'Love',
        'topic': 'Python'
    })