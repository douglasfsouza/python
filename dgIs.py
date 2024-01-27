nome = 'doug'
nome2 = 'doug'

print(nome is nome2)

print('Porque usou a mesma referencia')

nome3= 'doug'.upper()
nome4= 'DOUG'
print(nome3 is nome4)
print('Porque upper fez criar nova referencia')

a=[1,2,3]
b=[1,2,3]

print(a == b)
print(a is b)
print('Porque para lista cria novas referencias')