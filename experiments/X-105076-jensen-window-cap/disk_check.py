# B2: Jensen window cap (Theorem B2) verified on the adversarial configs that
# broke the pointwise 0-2-4 method (L-105067 Prop T-3 / sec 3b families) and on
# the 600-config residual generator of X-105067 t2_capscan_bracket.py.
import numpy as np, random, collections
random.seed(7); rng = np.random.default_rng(7)
R4 = 2 + np.sqrt(3)
H = 8.0; RHO = np.sqrt(4 + H*H); RR = 2.4*RHO
TH_BG = 0.0070026908
C_PAIR, C_REAL, C_AMP = 5.81288, 2.84992, 0.83845

def f0(s, y): return 2*(y*y - s*s)/(s*s + y*y)**2
def f2(s, y): return -12*(s**4 - 6*s*s*y*y + y**4)/(s*s + y*y)**4
def f4(s, y): return -240*(s*s-y*y)*(s*s-4*s*y+y*y)*(s*s+4*s*y+y*y)/(s*s+y*y)**6

def zeros_list(reals, pairs):
    Z = [(complex(c, 0.0), m) for (c, m) in reals]
    for (x, y, m) in pairs: Z += [(complex(x, y), m), (complex(x, -y), m)]
    return Z

def hprime_c(t, Z):   # complex t (scalar or array); h' = -sum m/(t-w)^2
    v = np.zeros_like(np.asarray(t, dtype=complex))
    for (w, m) in Z: v -= m/(np.asarray(t, dtype=complex) - w)**2
    return v

def hprime_r(t, reals, pairs):
    v = np.zeros_like(t)
    for (c, m) in reals: v -= m/(t - c)**2
    for (x, y, m) in pairs: v += m*f0(t - x, y)
    return v

def absterms(t, reals, pairs):
    v = np.zeros_like(t)
    for (c, m) in reals: v += m/(t - c)**2
    for (x, y, m) in pairs: v += np.abs(m*f0(t - x, y))
    return v

def count_zeros(lo, hi, reals, pairs, N=400001):
    t = np.linspace(lo + 1e-9*(hi-lo), hi - 1e-9*(hi-lo), N)
    v = hprime_r(t, reals, pairs); A = absterms(t, reals, pairs)
    mask = np.abs(v) > 1e-11*A
    sv = np.sign(v)[mask]
    return int(np.count_nonzero(sv[1:]*sv[:-1] < 0))

def clusters_of(deep):
    iv = sorted(range(len(deep)), key=lambda j: deep[j][0])
    comps, cur, hi = [], [], None
    for j in iv:
        x, y, m = deep[j]
        lo2, hi2 = x - R4*y, x + R4*y
        if cur and lo2 <= hi: cur.append(j); hi = max(hi, hi2)
        else:
            if cur: comps.append(cur)
            cur, hi = [j], hi2
    if cur: comps.append(cur)
    return comps

def triple_nonempty(sub, lo, hi, N=200001):
    t = np.linspace(lo, hi, N)
    L0 = sum(m*f0(t-x, y) for (x, y, m) in sub)
    L2 = sum(m*f2(t-x, y) for (x, y, m) in sub)
    L4 = sum(m*f4(t-x, y) for (x, y, m) in sub)
    return bool(((L0 > 0) & (L2 > 0) & (L4 > 0)).any())

def window_bound(cluster, reals, pairs, verbose=False):
    """Stopping recursion; returns dict with terminal window data + bounds."""
    Z = zeros_list(reals, pairs)
    allpts = [(w, m) for (w, m) in Z]
    S = set()
    for (x, y, m) in cluster: S.add((x, y)); S.add((x, -y))
    span_lo = min(x - R4*y for (x, y, m) in cluster)
    span_hi = max(x + R4*y for (x, y, m) in cluster)
    for it in range(40):
        xs = [w.real for (w, m) in allpts if (w.real, w.imag) in S]
        ys = [abs(w.imag) for (w, m) in allpts if (w.real, w.imag) in S]
        c = 0.5*(min(xs) + max(xs))
        L = max(0.5*(max(xs) - min(xs)), 4*max(ys), 1e-300,
                0.5*max(span_hi - c, c - span_lo))
        tstar = complex(c, H*L)
        need = set()
        for (w, m) in allpts:
            if (w.real, w.imag) in S: continue
            if abs(w - tstar) <= RR*L*(1 + 1e-12): need.add((w.real, w.imag))
        if need:
            S |= need; S |= {(x, -y) for (x, y) in need}  # conjugation-close
            continue
        # (A2) is enforced by choice of c, L. (DOM):
        NS = sum(m for (w, m) in allpts if (w.real, w.imag) in S)
        bg = sum(m/max(abs(w - tstar) - RR*L, 1e-300)**2
                 for (w, m) in allpts if (w.real, w.imag) not in S)
        if bg <= TH_BG*NS/L**2 or len(S) == len(allpts):
            break
        # inflate: swallow nearest outside zero
        wbest = min(((w, m) for (w, m) in allpts if (w.real, w.imag) not in S),
                    key=lambda wm: abs(wm[0] - tstar))
        S.add((wbest[0].real, wbest[0].imag)); S.add((wbest[0].real, -wbest[0].imag))
    pS = len({(x, abs(y)) for (x, y) in S if y != 0})
    nuS = len({x for (x, y) in S if y == 0})
    thm = C_PAIR*pS + C_REAL*nuS + C_AMP
    # numeric Jensen ratio (achieved): log|g| = log|h'| + sum 2 log|t-w| over S-members
    Smem = [(complex(x, y), 1) for (x, y) in S]   # factor per DISTINCT zero, squared
    def logg(t):
        lg = np.log(np.abs(hprime_c(t, Z)))
        for (w, _m) in Smem: lg += 2*np.log(np.abs(np.asarray(t, dtype=complex) - w))
        return lg
    th = np.linspace(0, 2*np.pi, 4096, endpoint=False)
    circ = tstar + RR*L*np.exp(1j*th)
    Mmax = float(np.max(logg(circ))); ctr = float(logg(np.array([tstar]))[0])
    ach = (Mmax - ctr)/np.log(2.4)
    # Lemma B2.1 check
    NS = sum(m for (w, m) in allpts if (w.real, w.imag) in S)
    cone_ok = abs(hprime_c(np.array([tstar]), Z)[0]) >= 0.0070026*NS/L**2
    return dict(pS=pS, nuS=nuS, thm=thm, ach=ach, cone_ok=bool(cone_ok),
                c=c, L=L, iters=it, span=(span_lo, span_hi),
                terminal=(len(S) == len(allpts)))

def run_config(name, a, b, reals, deep, other, out):
    comps = clusters_of(deep)
    tot_thm = 0.0; rows = []
    for comp in comps:
        cl = [deep[j] for j in comp]
        wb = window_bound(cl, reals, deep + other)
        lo = max(a, wb['span'][0]); hi = min(b, wb['span'][1])
        ztrue = count_zeros(lo, hi, reals, deep + other) if hi > lo else 0
        tne = triple_nonempty(cl, wb['span'][0], wb['span'][1])
        m = len(cl); M = sum(mm for (_, _, mm) in cl)
        ok = ztrue <= int(wb['thm'])
        rows.append((tne, m, M, ztrue, wb, ok))
        tot_thm += wb['thm']
    zG = count_zeros(a, b, reals, deep + other)
    for (tne, m, M, ztrue, wb, ok) in rows:
        out.write("%s  T%s m=%d M=%d  Ztrue=%d  thmB2=%.2f (p=%d,nu=%d,it=%d,term=%d) "
                  "achJ=%.2f cone=%d %s\n" % (name, "NE" if tne else "E", m, M,
                  ztrue, wb['thm'], wb['pS'], wb['nuS'], wb['iters'],
                  wb['terminal'], wb['ach'], wb['cone_ok'],
                  "OK" if ok else "**VIOL**"))
    return rows, zG, tot_thm

if __name__ == "__main__":
    import sys, io
    out = io.StringIO()
    # ---------- PART A: the exact families that broke the pointwise method ----
    out.write("== PART A: L-105067 sec 3b adversarial families (T_K nonempty) ==\n")
    fams = []
    # A1 equal-scale mult-ratio (integer mults 1:3 and 2:7 ~ mu=3.5), offset 0.7
    fams.append(("A1a-mu3", [(0.0, 1.0, 1), (0.7, 1.0, 3)]))
    fams.append(("A1b-mu3.5", [(0.0, 1.0, 2), (0.7, 1.0, 7)]))
    # A2 edge injector, unit mults
    fams.append(("A2-edge", [(0.0, 0.8, 1), (0.05, 1.0, 1)]))
    # A3 13-pair near-common scale
    offs = [1.05, 1.08, 1.11, 1.14, 1.17, 1.20]
    p13 = [(0.0, 1/1.3, 1)] + [(s*o, 1.0, 1) for o in offs for s in (1, -1)]
    fams.append(("A3-13pair", p13))
    for g in (8.0, 32.0, 128.0):
        a, b = -g/2, g/2
        for (nm, cl) in fams:
            reals = [(a, 1), (b, 1)]
            run_config("%s g=%g" % (nm, g), a, b, reals, cl, [], out)
    # A4: endpoint-hugging variant (cluster near a, extra real zeros outside)
    g = 16.0; a, b = -g/2, g/2
    cl = [(a + 1.6, 1.0, 1), (a + 2.3, 1.0, 3)]
    reals = [(a, 1), (b, 1), (a - 0.7, 2), (a - 2.5, 1), (b + 1.0, 1)]
    run_config("A4-hug g=16", a, b, reals, cl, [], out)
    # ---------- PART B: rerun the 600-config generator, apply the disk bound --
    out.write("\n== PART B: X-105067 t2 generator rerun, disk bound per cluster ==\n")
    NC = 0; viol = 0; nne = 0; ne_ok = 0
    stats = collections.Counter(); ratios = []
    def budgets_ok(a, b, reals, others):
        gg = b - a; W = V1 = V2 = 0.0; ML4 = MR4 = ML6 = MR6 = 0.0
        c8, c12 = 1 + np.sqrt(2), 2 + np.sqrt(3)
        for (x, y, mm) in others:
            ov = (x - y < b) and (x + y > a)
            if ov and y >= gg/2:
                w = (gg/(2*y))**2; W += mm*w; V1 += mm*w*w; V2 += mm*w**3
            elif not ov:
                if x + y <= a:
                    if a - x < c8*y: ML4 += mm
                    if a - x < c12*y: ML6 += mm
                elif x - y >= b:
                    if x - b < c8*y: MR4 += mm
                    if x - b < c12*y: MR6 += mm
        kap = (11 + 5*np.sqrt(5))/64
        return (W < 1) and (kap*V1 + 0.022543*(ML4 + MR4) < 1) and \
               (V2 + 0.04631627*(ML6 + MR6) < 1)
    for trial in range(600):
        g = random.choice([1.0, 4.0, 16.0]); a, b = -g/2, g/2
        reals = [(a, random.choice([1, 1, 2])), (b, random.choice([1, 1, 3]))]
        for extra in range(random.randint(0, 3)):
            side = random.choice([-1, 1]); d = 10**rng.uniform(-2, 1)
            reals.append(((b if side > 0 else a) + side*d, random.randint(1, 3)))
        m = random.randint(1, 5); deep = []
        for j in range(m):
            y = 10**rng.uniform(np.log10(g*1e-4), np.log10(g*0.49))
            x = rng.uniform(a - 0.5*y, b + 0.5*y)
            deep.append((x, y, random.randint(1, 4)))
        other = []
        for k in range(random.randint(0, 3)):
            kind = random.choice(['sh', 'nonov'])
            if kind == 'sh':
                y = g/2*10**rng.uniform(0, 0.3); x = rng.uniform(a, b); mm = 1
                if (g/(2*y))**2*mm < 0.3: other.append((x, y, mm))
            else:
                y = 10**rng.uniform(-2, 0); side = random.choice([-1, 1])
                x = (b if side > 0 else a) + side*(y + 10**rng.uniform(-2, 0)*y)
                other.append((x, y, 1))
        if not budgets_ok(a, b, reals, other): continue
        NC += 1
        sink = io.StringIO()
        rows, zG, tot = run_config("t%d" % trial, a, b, reals, deep, other, sink)
        for (tne, mm, M, zt, wb, ok) in rows:
            stats['NE' if tne else 'E'] += 1
            if tne:
                nne += 1
                if ok: ne_ok += 1
            if not ok:
                viol += 1; out.write("VIOL " + sink.getvalue())
            if M > 0: ratios.append((wb['thm']/max(M, 1), tne, wb['terminal']))
        if trial % 150 == 0: sys.stderr.write("trial %d\n" % trial)
    out.write("configs used: %d  clusters: %s\n" % (NC, dict(stats)))
    out.write("T-nonempty clusters: %d, certified OK: %d, violations: %d\n"
              % (nne, ne_ok, viol))
    rt = [r for (r, tne, term) in ratios]
    out.write("bound/M ratio: min %.2f med %.2f max %.2f;  terminal-window "
              "fraction %.3f\n" % (min(rt), sorted(rt)[len(rt)//2], max(rt),
              sum(1 for (_, _, t) in ratios if t)/len(ratios)))
    print(out.getvalue())
    open("disk_check_out.txt", "w").write(out.getvalue())
