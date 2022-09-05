posInt = int(input('enter a positive integer: '))
guess = posInt / 2
print('guess 0 =', guess)
for i in range(1, 10):
    guess = (guess + posInt / guess) / 2
    print('guess', i, '=', guess)