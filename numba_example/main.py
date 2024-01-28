from numba import jit
import random
import math
import time

@jit(nopython=True)
def do_some_math(n):
    z = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        z += math.sqrt(x ** 2 + y ** 2)
    return z

start = time.time()
do_some_math(1_000_000_000)
end = time.time()

print(end - start)