from fractions import Fraction
from mpmath import mp, mpf, sqrt, nstr
mp.dps = 30
PRIMES61 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

# full lattice of P_61 divisors, sorted: check global min of A_t = sum mu/d
divs = [(1,1)]
for p in PRIMES61:
    divs += [(d*p, -mu) for d,mu in divs]
divs.sort()
print("full lattice size:", len(divs))
run = Fraction(0); Amin = Fraction(10); argA = None
for d,mu in divs:
    run += Fraction(mu,d)
    if run < Amin: Amin = run; argA = d
print("global min A_t over ALL t | P_61:", Amin, float(Amin), "at t =", argA)
print("A_inf = prod(1-1/p) =", float(run))

# B_13 high precision
B13 = sum(mu/sqrt(mpf(d)) for d,mu in divs if d<=13)
print("B_13 =", nstr(B13,25))
c1 = 4*(Fraction(1,67)-Fraction(-2323,30030))
print("c1 = 4(1/67 - A_13) =", c1, "=", nstr(mpf(c1.numerator)/c1.denominator, 20))
c0 = 3*(B13 - 1/sqrt(mpf(67)))
print("c0 = 3(B_13 - 67^{-1/2}) =", nstr(c0,20))

# violated pure-root thresholds at X=61841: t with F0(t)<0
def T(u): return 4*sqrt(u)-3 if u>=1 else mpf(0)
X = 61841
run = mpf(0); neg = []
runA = Fraction(0)
for d,mu in divs:
    if d > X: break
    run += mu*T(mpf(X)/d)/sqrt(mpf(d))
    if run < 0: neg.append(d)
print(f"X={X}: #violated root thresholds = {len(neg)}; first 25: {neg[:25]}")
print(f"   ranges: min={neg[0]} max={neg[-1]}")

# closed-form fit across ladder
fam = [(71,13),(71,11),(73,13),(79,17),(83,19),(89,23),(101,29),(151,43),(211,61),(331,53)]
c1f = mpf(c1.numerator)/c1.denominator
print("\n(q,y)      X        sqrt(X)      V* computed        c1*sqrt(X)+c0      diff")
computed = {61841:'88.5349841231', 52327:'81.1792188383', 63583:'89.8188724047',
            89981:'107.467361152',105659:'116.726492333',137149:'133.44197816',
            196243:'160.261483481',435031:'240.205028032',862357:'339.523012631',
            1175381:'396.92869681'}
for q,y in fam:
    Xv = 67*q*y
    pred = c1f*sqrt(mpf(Xv)) + c0
    print(f"({q},{y})  {Xv}  {nstr(sqrt(mpf(Xv)),10)}  {computed[Xv]}   {nstr(pred,12)}")
