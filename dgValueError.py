def tryAgain(prompt, retries=3, default='y'):
    while True:
        response=input(prompt)
        if response in {'y','ye','yes','yep'}:
            return True
        elif response in {'n', 'no', 'not', 'nop', 'nope'}:
            return False
        else:
            print('Try again')
            retries -= 1
        if retries < 0:
            raise ValueError('No more retries')
            
r = tryAgain('Type y-yes ou n n-no: ')
if r:
    print('You typed YES')
else:
    print('You typed NO')