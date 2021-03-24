import json

with open('148.json') as artfile:
    art = json.load(artfile)
    print(art['description'])

kenneth = {'first_name': 'Kenneth', 'last_name': 'Love', 'topic': 'Python'}
#json.dumps(kenneth)
craig  = {'first_name': 'Craig', 'last_name': 'Dennis', 'topic': 'Java'}

with open('teachers.json', 'a') as teacherfile:
    json.dump([kenneth, craig], teacherfile)
