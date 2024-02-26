i = 5
def f(a=i):
    print(f'a={a}'.format(a))

i=6
f()
print("Os argumentos sao definidos no momento de definicao da funcao")