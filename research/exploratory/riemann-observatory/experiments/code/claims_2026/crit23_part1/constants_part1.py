"""CRIT23 Level-2 audit, part 1: headline constants recomputed from the stated formulas (independent of the
earlier ./checks/ scripts).  mpmath at 40 digits; sympy for exact values.
  AF Lemma 5.6 (5.13): R(psi) = (int psi^2 + iint |u-v| psi(u)psi(v)) / (int psi)^2  on [-1/2,1/2]
  Theorem A: (i) 2 - R(psi), (ii) (3 - R(psi))/2;  R(psi0) = 4/3, R(psiMT) = 1/2 + cot(1/sqrt2)/sqrt2
  LZ (1.1): C0 = 3/2 - cot(1/sqrt2)/sqrt2, C1 = (C0+1)/2
  AF App. A Lean form: cMT = sqrt2 tan(1/sqrt2) / (1 + tan(1/sqrt2)/sqrt2), constants 2 - 1/cMT and 3/2 - 1/(2 cMT)
  AF App. B.4 intermediate (Cauchy-Schwarz) certificate: 2/R - 1  (claimed 1/2 flat, 0.5066 MT)
  AF Rem. 6.1: H(lambda) = 2 - 1/lambda - lambda/3
Run: python3 -I constants_part1.py"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 40
out = []


def R_of(psi):
    I1 = mp.quad(psi, [-0.5, 0.5])
    I2 = mp.quad(lambda u: psi(u) ** 2, [-0.5, 0.5])
    # iint |u-v| psi(u) psi(v) = 2 * int_{u>v} (u-v) psi(u) psi(v)
    I3 = 2 * mp.quad(lambda u: psi(u) * mp.quad(lambda v: (u - v) * psi(v), [-0.5, u]), [-0.5, 0.5])
    return (I2 + I3) / I1 ** 2, I1, I2, I3


psi0 = lambda u: mp.mpf(1)
psiMT = lambda u: mp.cos(mp.sqrt(2) * u)
R0, *_ = R_of(psi0)
RMT, I1, I2, I3 = R_of(psiMT)
CMT = mp.mpf(1) / 2 + mp.cot(1 / mp.sqrt(2)) / mp.sqrt(2)
out.append(f"R(psi0) by quadrature        = {mp.nstr(R0, 30)}   (exact 4/3: diff {mp.nstr(R0 - mp.mpf(4)/3, 3)})")
out.append(f"R(psiMT) by quadrature       = {mp.nstr(RMT, 30)}")
out.append(f"C_MT = 1/2 + cot(1/v2)/v2    = {mp.nstr(CMT, 30)}   diff {mp.nstr(RMT - CMT, 3)}")
# exact flat window with sympy
u, v = sp.symbols("u v", real=True)
I3_exact = sp.integrate(sp.integrate(sp.Abs(u - v), (v, -sp.Rational(1, 2), sp.Rational(1, 2))), (u, -sp.Rational(1, 2), sp.Rational(1, 2)))
out.append(f"sympy: iint_[-1/2,1/2]^2 |u-v| = {sp.nsimplify(I3_exact)}  =>  R(psi0) = 1 + 1/3 = {1 + sp.nsimplify(I3_exact)}")
out.append("")
out.append(f"Theorem A(i)  flat: 2 - 4/3        = {sp.Rational(2) - sp.Rational(4, 3)}")
out.append(f"Theorem A(ii) flat: (3 - 4/3)/2    = {(sp.Rational(3) - sp.Rational(4, 3)) / 2}")
out.append(f"Theorem A(i)  MT  : 2 - C_MT       = {mp.nstr(2 - CMT, 25)}   (stated 0.67250...)")
out.append(f"Theorem A(ii) MT  : (3 - C_MT)/2   = {mp.nstr((3 - CMT) / 2, 25)}   (stated 0.83625...; abstract rounds to 0.8362)")
C0 = mp.mpf(3) / 2 - mp.cot(1 / mp.sqrt(2)) / mp.sqrt(2)
out.append(f"LZ C0 = 3/2 - cot(1/v2)/v2     = {mp.nstr(C0, 25)};  LZ C1 = (C0+1)/2 = {mp.nstr((C0 + 1) / 2, 25)}")
t = mp.tan(1 / mp.sqrt(2))
cMT_lean = mp.sqrt(2) * t / (1 + t / mp.sqrt(2))
out.append(f"AF Lean cMT = v2 tan(1/v2)/(1+tan(1/v2)/v2) = {mp.nstr(cMT_lean, 25)};  1/cMT - C_MT = {mp.nstr(1 / cMT_lean - CMT, 3)}")
out.append(f"   Lean constants: 2 - 1/cMT = {mp.nstr(2 - 1 / cMT_lean, 20)};  3/2 - 1/(2 cMT) = {mp.nstr(mp.mpf(3)/2 - 1 / (2 * cMT_lean), 20)}")
out.append("")
# stationarity of MT window: G(u) = psi(u) + int |u-v| psi(v) dv constant on [-1/2,1/2]
for uu in (0, 0.17, 0.33, 0.5):
    G = psiMT(uu) + mp.quad(lambda vv: abs(uu - vv) * psiMT(vv), [-0.5, uu, 0.5])
    out.append(f"MT stationarity G({uu}) = {mp.nstr(G, 20)}")
out.append(f"   G(0) predicted cos(1/v2) + sin(1/v2)/v2 = {mp.nstr(mp.cos(1/mp.sqrt(2)) + mp.sin(1/mp.sqrt(2))/mp.sqrt(2), 20)};  "
           f"int psiMT = v2 sin(1/v2) = {mp.nstr(mp.sqrt(2)*mp.sin(1/mp.sqrt(2)), 20)} (quad {mp.nstr(I1, 20)})")
out.append("")
out.append(f"App. B.4 Cauchy-Schwarz stage: 2/R - 1:  flat {mp.nstr(2 / R0 - 1, 15)} (claimed 1/2),  MT {mp.nstr(2 / CMT - 1, 15)} (claimed 0.5066)")
lam = sp.symbols("lambda", positive=True)
H = 2 - 1 / lam - lam / 3
out.append(f"Rem. 6.1: H(lambda) = 2 - 1/lambda - lambda/3; H'(lambda) = {sp.simplify(sp.diff(H, lam))} > 0 on (0,1]; H(1) = {H.subs(lam, 1)}")
# Montgomery-type R_lambda(psi0) = 1/lambda + lambda/3 from F(alpha) = |alpha| + delta-mass 1 (support lambda, Fejer weight)
a_ = sp.symbols("a", positive=True)
Rl = (lam * 1 + 2 * sp.integrate((lam - a_) * a_, (a_, 0, lam))) / lam ** 2
out.append(f"   check R_lambda(psi0) via (1/lambda^2)[lambda + 2 int_0^lambda (lambda-a) a da] = {sp.simplify(Rl)}")
print("\n".join(out))
