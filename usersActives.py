users = {'Doug':'Active', 'And':'Inactive', 'Nico':'Active'}
print('Users:')
for user, status in users.copy().items():
    print(user + ' ' + status)
    if status == 'Inactive':
        del users[user]

actives = {}
for user, status in users.items():
    if (status == 'Active'):
        actives[user] = status

print("Actives:")

for user, status in actives.copy().items():
    print(user + ' ' + status)