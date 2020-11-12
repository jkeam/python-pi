from decouple import config
from decimal import Decimal, getcontext

getcontext().prec=100
times = config('TIMES', default=20, cast=int)

if __name__ == "__main__":
    while True:
        for i in range(times):
            pi = 0
            for k in range(100):
              # https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
              pi = pi + (1/Decimal(16)**k * (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6)))
            print(f"{i + 1}: {pi}")
