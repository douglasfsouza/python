from collections import deque

fila = deque(["one, two, three"])

fila.append('four')
fila.append('five')

#print(fila)

fila.popleft()

print(fila[0])