import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s6_zw import *
random.seed(1)
bad = 0; n = 0
for _ in range(4000):
    y = (random.randint(-60, 60), random.randint(-60, 60))
    if is_zero(y) or divides(LAM, y): continue
    x = (random.randint(-300, 300), random.randint(-300, 300))
    a = cubic_symbol(x, y); b = cubic_jacobi(x, y); n += 1
    if a != b: bad += 1
print("cubic_jacobi vs factorization-based symbol:", n, "cases,", bad, "mismatches")
