from decouple import config
from decimal import Decimal, getcontext

getcontext().prec=100
times = config('TIMES', default=500, cast=int)

if __name__ == "__main__":
    i = 1
    places = 500
    print(f"Every number printed represents {times} times pi is calculated {places} places.")
    while True:
        for j in range(times):
            pi = 0
            for k in range(places):
              # https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
              pi = pi + (1/Decimal(16)**k * (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6)))
        print(i)
        i += 1
