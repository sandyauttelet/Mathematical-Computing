"""
Created on Mon Jul  3 12:57:29 2023

@author: sandy
"""

import numpy as np

def f(x):
    if x % 2 == 0:
        return x/2
    if x % 2 == 1:
        return 3*x+1
    
def C(n):
    if n == 1:
        return 0
    fun = f(n)
    for i in range(1,1000): #1000 was an arbitrary choice. Is there a max_iter?
        if fun == 1:        #I only broke it by too large of n, never got iter > 1000
            return i
        fun = f(fun)
        
A = [[C(6),C(2),C(3)],[C(4),C(11),C(6)],[C(7),C(8),C(16)]]
B = np.reshape(range(1,10),(3,3))
np.fill_diagonal(B, [6,11,16])
B = np.vectorize(C)(B)
assert np.allclose(B, A)
b = [14,-4,17]

x = np.linalg.solve(A,b)

A_bonus =[[C(7),C(2),C(3),C(4),C(5)],[C(6),C(27),C(8),C(9),C(10)],\
          [C(11),C(12),C(55),C(14),C(15)],[C(16),C(17),C(18),C(62),C(20)],\
              [C(21),C(22),C(23),C(24),C(102)]]
B_bonus = np.reshape(range(1,26),(5,5)) #Curtis found pattern and built A faster
np.fill_diagonal(B_bonus,[7,27,55,62,102])
B_bonus = np.vectorize(C)(B_bonus)
assert np.allclose(B_bonus, A_bonus)

b_bonus = [72,345,521,551,247]

x_bonus = np.linalg.solve(A_bonus,b_bonus)
