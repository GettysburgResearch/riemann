import sympy as sp
import mpmath as mp
mp.mp.dps = 30
t,u,v,y = sp.symbols('t u v y', real=True)
z = sp.I  # y=1 normalized: z = i
# phi'(t) with x=0,y=1: f(u)=2(1-u^2)/(1+u^2)^2 ; check f = -2 Re (u - i)^{-2}
f = 2*(1-u**2)/(1+u**2)**2
chk = sp.simplify(f - (-2*sp.re((u - sp.I)**(-2))))
print("f = -2Re(u-i)^-2 check:", chk)
# second derivative identity: f'' = -12 Re (u-i)^{-4}
chk2 = sp.simplify(sp.diff(f,u,2) - (-12*sp.re((u-sp.I)**(-4))))
# fourth: f'''' = -240 Re (u-i)^{-6}
chk4 = sp.simplify(sp.diff(f,u,4) - (-240*sp.re((u-sp.I)**(-6))))
print("f''=-12Re(u-i)^-4:", chk2, " f''''=-240Re(u-i)^-6:", chk4)
# kappa_4 = max_u (-Re(u+i)^{-4})_+ : known (11+5sqrt5)/64
g4expr = -sp.re((u+sp.I)**(-4))
crit = sp.solve(sp.diff(g4expr,u), u)
vals = [(c, sp.simplify(g4expr.subs(u,c))) for c in crit if c.is_real]
kap4 = sp.simplify(sp.Rational(11,64)+5*sp.sqrt(5)/64)
print("kappa4 exact:", sp.nsimplify(kap4), float(kap4))
print("crit vals lvl4:", [(sp.N(c,15), sp.N(val,15)) for c,val in vals])
# kappa_6 = max_u (-Re(u+i)^{-6})_+
g6expr = sp.simplify(-sp.re((u+sp.I)**(-6)))
d6 = sp.together(sp.diff(g6expr,u))
num6 = sp.numer(sp.simplify(d6))
crit6 = sp.solve(sp.Eq(num6,0), u)
best = []
for c in crit6:
    if c.is_real:
        val = sp.N(g6expr.subs(u,c), 25)
        best.append((sp.N(c,12), val))
best.sort(key=lambda p: -p[1])
print("kappa6 candidates:", best[:4])
