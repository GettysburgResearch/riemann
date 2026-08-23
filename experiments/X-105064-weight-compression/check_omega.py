import random, json
random.seed(105064)

def omega_pair(zeros, x, y):
    """zeros: sorted list of distinct real zeros; pair (x,y). Return (omega, mu, r)."""
    lo, hi = x - y, x + y
    zs = sorted(zeros)
    # gaps = (zs[i], zs[i+1]); overhang iff open intervals intersect
    om, gmax, r = 0.0, 0.0, 0
    for i in range(len(zs) - 1):
        a, b = zs[i], zs[i+1]
        if a < hi and b > lo and a < b:   # G cap I_p nonempty (open)
            g = b - a
            om += min(1.0, g*g/(4*y*y))
            gmax = max(gmax, g); r += 1
    mu = min(1.0, gmax/(2*y))
    return om, mu, r

viol = 0; worst = 0.0; trials = 200000
for _ in range(trials):
    n = random.randint(2, 40)
    zs = sorted(random.uniform(-10, 10) for _ in range(n))
    x = random.uniform(-11, 11); y = random.choice([random.uniform(1e-4, 0.5), random.uniform(1e-3, 3)])
    # note: y>1/2 violates strip but the lemma is pure combinatorics; test anyway
    om, mu, r = omega_pair(zs, x, y)
    bound = mu + 2*mu*mu
    if om > bound + 1e-12: viol += 1
    if bound > 0: worst = max(worst, om/bound)
print("random trials:", trials, "violations:", viol, "worst omega/(mu+2mu^2):", round(worst, 6))

# adversarial family: sup 3
res = []
for eps in [0.1, 0.01, 1e-4, 1e-8]:
    y = 0.4; x = 0.0; L = 2.0
    zs = [x-y-L, x-y+eps, x+y-eps, x+y+L]
    om, mu, r = omega_pair(zs, x, y)
    res.append((eps, round(om, 8), mu, r))
print("sup-3 family (eps, omega, mu, r):", res)

# giant gap
zs = [-5.0, 5.0]; om, mu, r = omega_pair(zs, 0.0, 0.3)
print("giant gap: omega", om, "mu", mu, "r", r)

# tiny-gap cluster: n equal contained gaps of length g, plus 2 protruding of length g
def cluster(n):
    y = 0.5; g = 2*y/n
    zs = [-y - g] + [-y + i*g for i in range(n+1)] + [y + g]
    om, mu, r = omega_pair(zs, 0.0, y)
    return round(om,6), round(mu + 2*mu*mu,6), round(om/(mu+2*mu*mu),4)
print("cluster n=4,20,200 (omega, bound, ratio):", [cluster(n) for n in (4,20,200)])

# sharpness small-mu: ratio -> 1?
print("cluster n=2000:", cluster(2000))
