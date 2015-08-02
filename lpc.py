#!/usr/bin/python
from pprint import pprint
import numpy as np
import math as ms

#data = open('data.txt').read().split('\n')
data = [
    170,
    180,
    180,
    160,
    180,
    160,
    170,
    170,
    160,
]

N = len(data)
x = 0
r = np.zeros(N)
data.extend(np.zeros(N-1))

for k in range(N-1):
    for i in range(N-1):
        x += data[i]*data[i+k]
    r[k] = x/N

Q = np.zeros(N)
Q[0] = r[0]
alpha = np.zeros((N, N))
k = np.zeros(N)

k[1] = r[1]/Q[0]
alpha[1][1] = k[1]
Q[1] = (1-ms.pow(k[1], 2))*Q[0]

for n in range(2, N):
    tmp = 0
    for j in range(1, n-1):
        tmp += alpha[j][n-1]*r[n-j]
    k[n] = -(r[n]+tmp)/Q[n-1]
    alpha[n][n] = k[n]
    Q[n] = (1-ms.pow(k[n], 2))*Q[n-1]

    for j in range(1, n-1):
        if (n-j) <= 0:
            break
        alpha[j][n] = alpha[j][n-1] + k[n]*alpha[n-j][n-1]

a = np.zeros(N)
for j in range(1, N):
    a[j] = alpha[j][N-1]

xhat = 0
for n in range(1, N-1):
    xhat += a[n]*data[n]

xhat = xhat * (-1)

#pprint(k)
#pprint(Q)
#pprint(r)
#pprint(alpha)
#pprint(a)
print(xhat)
