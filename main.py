import sys
from equation import equation

for i in sys.stdin:
    print(equation(i.strip()))
    print('-'*100)
