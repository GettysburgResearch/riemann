"""pipeline_table.py -- combine lab_core (truth) and dual_energy (dual mean square) outputs.

All inputs are exact integers; ratios are printed as floats.  Rows: all u in V_M (deg u <= m = M-1),
columns: monic squarefree n of degree d.  Monic-row sums are multiplied by (q-1) where needed;
ratios below are independent of that factor except where stated.
  Diag      = sum_u #{n : (n,u)=1}                                   (primal diagonal)
  Off       = M2 - Diag                                               (the signed quantity; equals the
                                                                       signed dual exactly, ledger.py)
  P         = q^{M-d} * E(K),  K = 2d - M,  E(K) = sum_{h in V_K} |B_h|^2   (after positivity: the full
                                                                       dual mean square in primal units)
  Pdiag     = q^{M-d} * DD(K)                                         (its dual diagonal)
Printed: rho = m/d, Off/Diag, P/Diag (= cost of positivity + mean square), E/DD (is the dual
diagonal-sized?), predicted q^{d-M} (the D^{1-rho} law), and the signed-dual saving exponent
kappa = log(P/|Off|) / log(q^d)  (how much the signed dual saves over the positive bound, in units of d).
Usage: python3 pipeline_table.py core.txt de.txt [de2.txt ...]
"""
import sys
import math
import json


def read_core(p):
    rows = {}
    q = None
    for line in open(p):
        if line.startswith('#'):
            q = int(line.split()[1].split('=')[1])
            continue
        t = line.split()
        rows[(int(t[0]), int(t[1]))] = (int(t[3]), int(t[4]))
    return q, rows


def read_de(p):
    q = d = None
    E = {}
    for line in open(p):
        if line.startswith('#'):
            t = line.split()
            q = int(t[1].split('=')[1]); d = int(t[2].split('=')[1])
            continue
        if line.startswith('q='):
            continue
        t = line.split()
        E[int(t[0])] = (int(t[2]), int(t[3]))
    return q, d, E


def main():
    qc, core = read_core(sys.argv[1])
    out = []
    for p in sys.argv[2:]:
        q, d, E = read_de(p)
        assert q == qc
        mmax = max(k for _, k in core)
        print(f'\n### q = {q}, d = {d} (columns: {sum(1 for _ in [0])} squarefree n of degree {d})')
        print('| M | m | rho=m/d | dual rows deg h < K | Off/Diag (truth) | P/Diag (after positivity) | q^(d-M) | E/DD (dual vs its diagonal) | kappa |')
        print('|---|---|---|---|---|---|---|---|---|')
        for M in range(1, 2 * d + 1):
            m = M - 1
            K = 2 * d - M
            if m > mmax or (K - 1) > max(E) or K < 0:
                continue
            M2 = sum(core[(d, k)][0] for k in range(m + 1))
            Dg = sum(core[(d, k)][1] for k in range(m + 1))
            EK = sum(E[k][0] for k in range(K))
            DDK = sum(E[k][1] for k in range(K))
            Off = M2 - Dg
            P = (q ** (M - d)) * EK if M >= d else EK / q ** (d - M)
            r_off = Off / Dg
            r_P = P / Dg
            ed = EK / DDK if DDK else float('nan')
            kappa = math.log(P / abs(Off)) / math.log(q ** d) if Off != 0 and P > 0 else float('nan')
            out.append(dict(q=q, d=d, M=M, m=m, rho=m / d, Off_over_Diag=r_off, P_over_Diag=r_P,
                            q_pow=q ** (d - M), E_over_DD=ed, kappa=kappa, M2=str(M2), Diag=str(Dg),
                            E=str(EK), DD=str(DDK)))
            print(f'| {M} | {m} | {m/d:.2f} | {K} | {r_off:+.4f} | {r_P:.3f} | {q**(d-M):.3g} | {ed:.4f} | {kappa:.3f} |')
    json.dump(out, sys.stdout if False else open('results/pipeline_table_q%d.json' % qc, 'w'), indent=1)


if __name__ == '__main__':
    main()
