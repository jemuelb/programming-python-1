bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

people = [bob, sue]

for person in people:
    person[2] *= 1.20

people.append(['Tom', 50, 0, None])

bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'age': 42,
        'job': ['software', 'writing'],
        'pay': (40000, 50000)}

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')

db = {}
db['bob'] = bob
db['sue'] = sue

if __name__ == '__main__':
    for key in db:
        print(key, '=>', db[key]['name'])

    for key in db:
        print(key, '=>', db[key]['pay'])
