import sys, flint
sys.path.insert(0, "/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C1-detection-horizons/skeptic")
src = open("/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C1-detection-horizons/skeptic/sk_jensen_exact.py").read()
ns = {}
exec(src.split("res = []")[0], ns)
from flint import arb, acb, acb_poly
flint.ctx.prec = 6000
a = arb(5)*arb.pi()/2; b = arb(7)*arb.pi()/2
X = ns["coeffs_X"](10, a, b, 70, 6000)
for d in (118, 119, 120):
    co = ns["R_poly"](X, d)
    flint.ctx.prec = 3000
    rts = acb_poly([acb(c) for c in co]).roots()
    r = sorted([(float(x.real.mid()), float(x.imag.mid())) for x in rts])
    gaps = [(r[i+1][0]-r[i][0], r[i][0]) for i in range(len(r)-1)]
    mg = min(gaps)
    print(d, "smallest gap between consecutive root real parts (u):", mg, "rel:", mg[0]/mg[1], "max |imag|:", max(abs(y) for _, y in r))
    flint.ctx.prec = 6000
