from numba import jit
import random
import math
import time
import numpy as np
import pandas as pd
import pandas_datareader as pdr

@jit(nopython=True)
def do_some_math(n):
    z = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        z += math.sqrt(x ** 2 + y ** 2)
    return z

@jit(nopython=True)
def do_some_math_numpy(n):
    z = np.zeros((n, n))
    for i in range(n):
        x = np.random.rand(n, n)
        y = np.random.rand(n, n)
        z += np.sqrt(x ** 2 + y ** 2)
    return z 

def pandas_function(data : pd.DataFrame):
    result = data.sort_values(by=['Volume'])
    result = result.applymap(math.sqrt)
    result += 2
    result = result.applymap(lambda x: x ** 2)
    result = result.T
    return data #result

start = time.time()
#do_some_math(1_000_000_000)
#do_some_math_numpy(1000)
data = pdr.DataReader("AAPL", "yahoo")
print(data)
end = time.time()

print(end - start)