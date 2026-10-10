import sys, numpy as np
sys.path.insert(0, '/home/user/riemann/research/exploratory/2026-10-10-quasi-rh-wave/scripts')
import exponent_model as em
def run(label, P, nofloor):
    if nofloor: em.Hfloor = lambda b, l, P: -np.inf
    else:       em.Hfloor = HF0
    B, b, l, det = em.optimise(P)
    print(f"{label:55s} B={B:.6f} at b={b:.4f} l={l:.4f} active={det['active']} class={det['Hmod_class']}")
HF0 = em.Hfloor
base = dict(em.DEFAULT)
ideal = dict(base, alpha=0.0, ck=1.0, cM=1.0)
run("current (Liu)", base, False)
run("current, floor removed (f=1/2 black box)", base, True)
run("ideal counts", ideal, False)
run("ideal counts, floor removed", ideal, True)
run("ideal counts, theta=0", dict(ideal, theta=0.0), False)
run("ideal counts, theta=0, floor removed", dict(ideal, theta=0.0), True)
