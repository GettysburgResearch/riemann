from fractions import Fraction
import numpy as np

T = 10
idx = list(range(2, T+1))
B = [[Fraction(0)]*(T-1) for _ in range(T-1)]
for i, n in enumerate(idx):
    for j, q in enumerate(idx[:i+1]):
        B[i][j] = Fraction((n//q)*(q-1-(n % q)), n+1)

# float eigenvector -> rational witness
Bf = np.array([[float(x) for x in row] for row in B])
w, V = np.linalg.eigh((Bf+Bf.T)/2)
v = V[:, 0]
r = [Fraction(int(round(1000*x)), 1000) for x in v]
# exact f^T sym(B) f = f^T B f (since f^T B f = f^T B^T f)
val = sum(r[i]*B[i][j]*r[j] for i in range(T-1) for j in range(T-1))
n2 = sum(x*x for x in r)
print("exact witness r =", [str(x) for x in r])
print("exact f^T B f =", val, "=", float(val), " ||f||^2 =", float(n2))
print("Rayleigh quotient =", float(val/n2))
assert val < 0
print("PROVED: sym(B_10) (and by congruence sym(K_10)) is NOT PSD.")
