#!/usr/bin/env python3
"""Lane S part 2: true per-fibre Hall feasibility via LP/max-flow,
independent of the prefix-reduction argument; dual extraction."""
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix, csr_matrix

N = 520
mu = [1]*(N+1); mu[0] = 0
primes = []; is_comp = [False]*(N+1)
for i in range(2, N+1):
    if not is_comp[i]:
        primes.append(i); mu[i] = -1
    for p in primes:
        if i*p > N: break
        is_comp[i*p] = True
        if i % p == 0:
            mu[i*p] = 0; break
        else:
            mu[i*p] = -mu[i]
smooth = [False]*(N+1)
for n in range(1, N+1):
    m0 = n
    for p in primes:
        if p > 61: break
        while m0 % p == 0: m0 //= p
    smooth[n] = (m0 == 1)

def fibre_system(x, smooth_only=False):
    ks = [k for k in range(1, int(np.floor(x))+1) if mu[k] != 0 and (smooth[k] or not smooth_only)]
    E = [k for k in ks if mu[k] == 1]
    O = [k for k in ks if mu[k] == -1]
    T = {k: (4*np.sqrt(x/k) - 3)/np.sqrt(k) for k in ks}
    return E, O, T

def prefix_deficit(x, smooth_only=False):
    E, O, T = fibre_system(x, smooth_only)
    ks = sorted(E+O)
    acc = 0.0; worst = (0.0, None)  # (violation, t)
    for k in ks:
        acc += mu[k]*T[k]
        if mu[k] == -1 and -acc > worst[0]:
            worst = (-acc, k)
    return worst  # (max positive violation = deficit, argmax t) ; 0 if feasible

def lp_maxflow(x, smooth_only=False):
    E, O, T = fibre_system(x, smooth_only)
    edges = [(oi, ei) for oi, o in enumerate(O) for ei, e in enumerate(E) if e <= o]
    nv = len(edges); nO = len(O); nE = len(E)
    A = lil_matrix((nO+nE, nv))
    for j, (oi, ei) in enumerate(edges):
        A[oi, j] = 1.0
        A[nO+ei, j] = 1.0
    b = np.array([T[o] for o in O] + [T[e] for e in E])
    c = -np.ones(nv)
    res = linprog(c, A_ub=csr_matrix(A), b_ub=b, bounds=(0, None), method='highs')
    assert res.status == 0, res.message
    flow = -res.fun
    D = sum(T[o] for o in O)
    deficit = D - flow
    marg = res.ineqlin.marginals  # <=0 shadow prices; dual y = -marg
    y_o = -marg[:nO]; z_e = -marg[nO:]
    return dict(E=E, O=O, T=T, flow=flow, D=D, deficit=deficit, y_o=y_o, z_e=z_e)

def lp_feasibility(x, smooth_only=False):
    E, O, T = fibre_system(x, smooth_only)
    edges = [(oi, ei) for oi, o in enumerate(O) for ei, e in enumerate(E) if e <= o]
    nv = len(edges); nO = len(O); nE = len(E)
    Aeq = lil_matrix((nO, nv)); Aub = lil_matrix((nE, nv))
    for j, (oi, ei) in enumerate(edges):
        Aeq[oi, j] = 1.0; Aub[ei, j] = 1.0
    res = linprog(np.zeros(nv), A_eq=csr_matrix(Aeq), b_eq=np.array([T[o] for o in O]),
                  A_ub=csr_matrix(Aub), b_ub=np.array([T[e] for e in E]),
                  bounds=(0, None), method='highs')
    return res.status  # 0 feasible/optimal, 2 infeasible

print("== sweep x=2..120: LP max-flow deficit vs prefix-Hall prediction ==")
maxerr = 0.0; mism = []
for x in list(range(2, 121)) + [148, 149, 210, 211, 306, 307, 400]:
    viol, t_arg = prefix_deficit(float(x))
    r = lp_maxflow(float(x))
    err = abs(r['deficit'] - viol)
    maxerr = max(maxerr, err)
    if err > 1e-7: mism.append((x, r['deficit'], viol))
print(f"max |LP deficit - max_t(-H_t)^+| over sweep = {maxerr:.3e}; mismatches: {mism}")

print("\n== per-C boundary fibres: LP status, deficit, dual violator ==")
eps = 1e-6
tests = [(67.0-eps, 'C=67 boundary'), (71.0-eps, 'C=71 boundary'),
         (87.0, 'x=87'), (87.35, 'x=87.35 (near crossing, FLAG margin)'),
         (88.0, 'x=88 first integer infeasible'),
         (89.0-eps, 'C=89 boundary'), (101.0-eps, 'C=101 boundary'),
         (149.0-eps, 'C=149 boundary'), (211.0-eps, 'C=211 boundary'),
         (307.0-eps, 'C=307 boundary'), (401.0-eps, 'C=401 boundary')]
for x, label in tests:
    r = lp_maxflow(x)
    viol, t_arg = prefix_deficit(x)
    st = lp_feasibility(x)
    # dual extraction: violator odds = {o : y_o ~ 0}, cut evens = {e : z_e ~ 1}
    O = r['O']; E = r['E']
    vio_o = [o for o, y in zip(O, r['y_o']) if y < 0.5]
    cut_e = [e for e, z in zip(E, r['z_e']) if z > 0.5]
    feas = 'FEASIBLE' if r['deficit'] < 1e-9 else 'INFEASIBLE'
    print(f"{label:38s} x={x:<12.6f} lp_feas_status={st} {feas:10s} deficit={r['deficit']:.9f} "
          f"prefix_pred={viol:.9f} argmax_t={t_arg}")
    if r['deficit'] > 1e-9:
        print(f"   dual min-cut: violator odds (y=0) = {vio_o}")
        print(f"                 saturated evens (z=1) = {cut_e}")

print("\n== smooth-support variant B at key fibres ==")
for x in (88.0, 89.0-eps, 401.0-eps):
    r = lp_maxflow(x, smooth_only=True)
    viol, t_arg = prefix_deficit(x, smooth_only=True)
    O = r['O']; E = r['E']
    vio_o = [o for o, y in zip(O, r['y_o']) if y < 0.5]
    cut_e = [e for e, z in zip(E, r['z_e']) if z > 0.5]
    print(f"x={x:<12.6f} deficit={r['deficit']:.9f} prefix_pred={viol:.9f} argmax_t={t_arg} "
          f"violator={vio_o if r['deficit']>1e-9 else '-'} cut_evens={cut_e if r['deficit']>1e-9 else '-'}")

print("\n== near-tight FEASIBLE fibre duals (x=87, x=87.35): bottleneck structure ==")
for x in (87.0, 87.35):
    r = lp_maxflow(x)
    tight_e = [(e, round(z,4)) for e, z in zip(r['E'], r['z_e']) if z > 1e-6]
    slack_o = [(o, round(y,4)) for o, y in zip(r['O'], r['y_o']) if y < 1-1e-6]
    print(f"x={x}: deficit={r['deficit']:.2e}; capacity duals>0: {tight_e[:12]}")
    print(f"     demand duals<1: {slack_o[:12]}")

print("\n== min slack per feasible C and violation growth per infeasible C ==")
for C in (71, 89, 101, 149, 211, 307, 401):
    x = C - eps
    viol, t_arg = prefix_deficit(x)
    # min slack over ALL prefixes at boundary fibre
    E, O, T = fibre_system(x)
    ks = sorted(E+O); acc = 0.0; mn = (1e9, None)
    for k in ks:
        acc += mu[k]*T[k]
        if mu[k] == -1 and acc < mn[0]: mn = (acc, k)
    print(f"C={C}: min_t H_t(C^-) = {mn[0]:+.6f} at t={mn[1]}; deficit={max(viol,0):.6f}")

print("\n== infeasible fibre census per C (integer fibres) ==")
for C in (71, 89, 101, 149, 211, 307, 401):
    bad = []
    for x in range(2, C):
        viol, t_arg = prefix_deficit(float(x))
        if viol > 1e-9: bad.append(x)
    frac_cont = max(0.0, (C - 87.35893176924588)/C)
    print(f"C={C}: infeasible integer fibres = {len(bad)} "
          f"({bad[:5]}{'...' if len(bad)>5 else ''}); continuous-fibre infeasible fraction = {frac_cont:.3f}")
