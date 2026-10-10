from fractions import Fraction
from math import gcd
from mpmath import mp, mpf, sqrt, nstr, iv

mp.dps = 40
iv.prec = 250

# squarefree n <= 13 with mobius signs (integer = P61-lattice version since all prime factors <= 13 <= 61)
sf13 = [(1,1),(2,-1),(3,-1),(5,-1),(6,1),(7,-1),(10,1),(11,-1),(13,-1)]
evens = [d for d,mu in sf13 if mu==1]
odds  = [d for d,mu in sf13 if mu==-1]
print("squarefree d<=13 mu=+1:", evens, "  mu=-1:", odds)

A13 = sum(Fraction(mu,d) for d,mu in sf13)
print("A_13 =", A13, "; equals -2323/30030:", A13 == Fraction(-2323,30030), "; 2323 =", 23*101)

c1 = 4*(Fraction(1,67) - A13)
print("c1 = 4(1/67 - A_13) =", c1, "; equals 371342/1006005:", c1 == Fraction(371342,1006005),
      "; gcd:", gcd(371342,1006005), "; decimal:", nstr(mpf(c1.numerator)/c1.denominator, 25))

fourA = 4*abs(A13)
print("4|A_13| =", fourA, "; 9292/30030 reduces to", Fraction(9292,30030), "; equal:", fourA == Fraction(9292,30030))

# B_13 (high precision and interval)
B13 = sum(mu/sqrt(mpf(d)) for d,mu in sf13)
B13i = sum(mu/iv.sqrt(iv.mpf(d)) for d,mu in sf13)
print("B_13 =", nstr(B13, 25), " interval [", nstr(B13i.a,25), ",", nstr(B13i.b,25), "]")

c0 = 3*(B13 - 1/sqrt(mpf(67)))
c0i = 3*(B13i - 1/iv.sqrt(iv.mpf(67)))
print("c0 = 3(B_13 - 67^{-1/2}) =", nstr(c0, 25), " interval [", nstr(c0i.a,25), ",", nstr(c0i.b,25), "]")
print("3|B_13| =", nstr(-3*B13, 25))

c1f = mpf(c1.numerator)/c1.denominator
c1iv = iv.mpf(c1.numerator)/c1.denominator
X0 = (abs(c0)/c1f)**2
X0i = (abs(c0i)/c1iv)**2
print("X_0 = (|c0|/c1)^2 =", nstr(X0, 25), " interval [", nstr(X0i.a,25), ",", nstr(X0i.b,25), "]")
# certify 77 < X0 < 78 and c1*sqrt(78)+c0 > 0
v78 = c1iv*iv.sqrt(iv.mpf(78)) + c0i
v77 = c1iv*iv.sqrt(iv.mpf(77)) + c0i
print("c1*sqrt(78)+c0 interval [", nstr(v78.a,20), ",", nstr(v78.b,20), "] > 0:", v78.a > 0)
print("c1*sqrt(77)+c0 interval [", nstr(v77.a,20), ",", nstr(v77.b,20), "] < 0:", v77.b < 0)

# root-only threshold C* = (3|B13|/(4|A13|))^2 = (45045 |B13| / 4646)^2
Cstar = (3*abs(B13)/ (4*abs(mpf(A13.numerator))/A13.denominator))**2
Cstar2 = (mpf(45045)*abs(B13)/4646)**2
print("C* =", nstr(Cstar, 25), "=", nstr(Cstar2, 25))

# base witness checks
X = 61841
def T(u): return 4*sqrt(u)-3 if u >= 1 else mpf(0)
F013 = 4*sqrt(mpf(X))*mpf(A13.numerator)/A13.denominator - 3*B13
F013_direct = sum(mu*T(mpf(X)/d)/sqrt(mpf(d)) for d,mu in sf13)
print("F0(13) closed form:", nstr(F013,20), " direct sum:", nstr(F013_direct,20), " diff:", nstr(F013-F013_direct,5))
head67 = T(mpf(X)/67)/sqrt(mpf(67))
print("head A_1 = 67^{-1/2} T(923):", nstr(head67, 20))
Vstar = -F013 + head67
print("V*(61841) = -F0(13)+head =", nstr(Vstar, 20), " vs c1*sqrt(X)+c0 =", nstr(c1f*sqrt(mpf(X))+c0, 20))
# escape constant at base witness
print("-F0(13) = (9292/30030)sqrtX - 3|B13| =", nstr(-F013,20), "=", nstr(mpf(9292)/30030*sqrt(mpf(X))+3*B13,20))

# ladder cross-check: closed form vs reproduced slacks (from circulation.py run)
computed = {61841:'88.5349841231', 52327:'81.1792188383', 63583:'89.8188724047',
            89981:'107.467361152',105659:'116.726492333',137149:'133.44197816',
            196243:'160.261483481',435031:'240.205028032',862357:'339.523012631',
            1175381:'396.92869681'}
fam = [(71,13),(71,11),(73,13),(79,17),(83,19),(89,23),(101,29),(151,43),(211,61),(331,53)]
print("\n  X        computed slack     c1*sqrt(X)+c0        -F0(13)+head67      rel.diff")
maxrel = mpf(0)
for q,y in fam:
    Xv = 67*q*y
    pred = c1f*sqrt(mpf(Xv)) + c0
    mine = -(4*sqrt(mpf(Xv))*mpf(A13.numerator)/A13.denominator - 3*B13) + T(mpf(Xv)/67)/sqrt(mpf(67))
    rel = abs(pred - mpf(computed[Xv]))/pred
    maxrel = max(maxrel, rel)
    print(f"  {Xv:8d}  {computed[Xv]:16s}  {nstr(pred,15):20s} {nstr(mine,15):20s} {nstr(rel,3)}")
print("max relative diff closed-form vs computed:", nstr(maxrel,3))
