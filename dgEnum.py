from enum import Enum

class Color(Enum):
    RED = 'red'
    BLUE = 'blue'
    
c = Color(input('Escolha uma cor: red ou blue: '))

print (f'entered: {c}')

if c == Color.RED:
    print ('You choosed red')
elif c == Color.BLUE:
    print ('You choosed blue')
else:
   print ("Invalid color!!")

#match c:
#    case Color.RED:
#        print ('You choosed red')
