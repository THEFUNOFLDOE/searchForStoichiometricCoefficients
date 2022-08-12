import sys
from equation import equation

# start program from there
for i in sys.stdin:
    if i.strip() == 'quit':
        break

    print(equation(i.strip()))
    print('-'*100)
