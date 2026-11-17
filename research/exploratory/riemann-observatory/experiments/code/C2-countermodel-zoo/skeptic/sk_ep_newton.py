import sys, time, flint
from flint import acb, arb
from sk_ep_probe import Z
flint.ctx.prec = 80
def newton(z, steps=12):
    for _ in range(steps):
        h = 1e-7
        f0 = complex(Z(acb(z.real, z.imag)))
        f1 = complex(Z(acb(z.real + h, z.imag)))
        d = (f1 - f0) / h
        st = f0 / d
        z = z - st
        if abs(st) < 1e-13: break
    return z, abs(complex(Z(acb(z.real, z.imag))))
for t in [float(x) for x in sys.argv[1:]]:
    best = None
    for s0 in (1.01, 1.0, 0.99, 1.03):
        z, r = newton(complex(s0, t))
        if abs(z.imag - t) < 1 and r < 1e-10:
            best = (z, r); break
    print(t, best, flush=True)
