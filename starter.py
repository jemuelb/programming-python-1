bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

people = [bob, sue]

for person in people:
    person[2] *= 1.20

people.append(['Tom', 50, 0, None])
