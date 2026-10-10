# Kintali QRH review (bounded): exact checks of Sec. 4.3-4.4 exponents and of the
# Hinz-1976-Satz-A-only variant of R(a). Run: python3 -I kintali_exponent_check.py
from fractions import Fraction as F
import sympy as sp

a, d, e, beta, v = sp.symbols('a d e beta v', real=True)
# (22): outside power at (x_r, w_r, z_r) = (a+16e, 1-a-6e, 17/50)
xr, wr, zr = a + 16*e, 1 - a - 6*e, sp.Rational(17, 50)
outside = sp.expand(xr + zr/2 + wr/2 - sp.Rational(5, 4))
print("(22) outside exponent:", outside, "| claimed:", sp.expand(a/2 - sp.Rational(3,4) + sp.Rational(17,100) + 13*e))
print("(22) U power (num a-1/2 minus z_r):", sp.expand(a - sp.Rational(1,2) - zr), "| claimed a-21/25")
C = lambda r: r - sp.Rational(2, 3)
rel_const = sp.nsimplify(-sp.Rational(3,4) + sp.Rational(17,100) + sp.Rational(2,3))
print("E constant 13/150?", rel_const, rel_const == sp.Rational(13,150))

def E(dd, aa, R):
    return aa/2 - beta + sp.Rational(13,150) + dd*(R + aa - sp.Rational(21,25))
print("E(1/2,a) =", sp.simplify(E(sp.Rational(1,2), a, sp.Symbol('R')) ), "(expect a - beta + R/2 - 1/3)")

# (23) rows
def outp(x, w, z): return sp.expand(x + z/2 + w/2 - sp.Rational(5,4) - C(beta))
print("Ew rel:", outp(beta+e, sp.Rational(3,4), sp.Rational(1,6)+e), "| claimed -1/8+3e/2")
print("Ez rel:", outp(beta+e, sp.Integer(1), sp.Rational(1,8)), "| claimed -1/48+e")
print("Eu rel:", outp(beta+e, sp.Rational(1,2), sp.Rational(17,50)), "| claimed -49/300+e")
print("EU abs:", sp.expand(2 + v/2 + 1 - sp.Rational(5,4)), "| claimed 7/4+v/2")
tot = sp.expand(sp.Rational(7,4) + v/2 + sp.Rational(501,1000)*(1 - v))
print("sum over U>Z^0.501:", tot, "| at v=4000:", tot.subs(v, 4000))

# max_a a + R(a)/2 - 1/3 with Kintali R and with Hinz Satz A only (Q-exponent 6(1-a)/(2-a))
Rk = lambda x: min(F(1), 5*(1-x))
Ra = lambda x: min(F(1), F(6)*(1-x)/(2-x))
grid = [F(51,100) + F(k, 100000) for k in range(0, 49001)]
for name, R in (("Kintali 5(1-a)", Rk), ("Hinz A 6(1-a)/(2-a)", Ra)):
    best = max(grid, key=lambda x: x + R(x)/2 - F(1,3))
    val = best + R(best)/2 - F(1,3)
    mono = min(R(x) + x - F(21,25) for x in grid), max(R(x) + x - F(21,25) for x in grid)
    print(f"{name}: argmax a={best}, max={val} (29/30={F(29,30)}), range of d-slope={mono}")
# derivative check for Hinz A branch on [4/5,1]
f = a + 3*(1-a)/(2-a) - sp.Rational(1,3)
print("f'(a) on [4/5,1] =", sp.simplify(sp.diff(f, a)), "; at 4/5:", sp.diff(f,a).subs(a, sp.Rational(4,5)), "; at 1:", sp.diff(f,a).subs(a,1))
print("47/48 - 29/30 =", F(47,48) - F(29,30))
print("-1/80 + 1/1000 =", F(-1,80) + F(1,1000), "< -1/100:", F(-1,80)+F(1,1000) < F(-1,100))
print("C(b)-delta0-9/32 =", F(47,48) - F(2,3) - F(1,4800) - F(9,32))
print("b - delta0 =", F(47,48) - F(1,4800), "> 11/12:", F(47,48)-F(1,4800) > F(11,12))
# h(sigma)=min(3/(2-s),2/s) max on [1/2,1]
hs = max(min(F(3)/(2-s), F(2)/s) for s in [F(1,2)+F(k,10000) for k in range(5001)])
print("max h =", hs)
# Lemma 6 geometry: disk radius 2-a-2e, heights < T + 1.49 <= 2T for T>=3; R6 > r0
for aa in (F(51,100), F(1)):
    ee = F(1,1000)
    print("a=",aa," R2=",2-aa-2*ee," R6=",2-aa-6*ee, " R6>49/100:", 2-aa-6*ee > F(49,100))
