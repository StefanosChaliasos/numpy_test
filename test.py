import numpy as np
from pandac import computations


n = computations.mul(12, 2)
a = np.arange(n)
a.ndim

# now reshape it
b = a.reshape(2, 4, 3)
print(b)
# b is having three dimensions
