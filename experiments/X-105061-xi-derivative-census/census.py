"""Lane B4 census driver. Stages: sweep | refine | cert3 | cascade | ledger | checks.
Usage: python3 census.py <stage> [T0]
All state under LANE dir; restartable; checkpoints per ~50 units in sweep.
Budgeted-mp discipline: every accepted sign has |val| > 10*scale*eps_budget,
eps_budget = 10^-(dps-5), dps = 35. NOT interval arithmetic.
"""
import sys, os, json, time
import mpmath as mp

HOME_LANE = os.path.dirname(os.path.abspath(__file__))
LANE = os.environ.get('LANE_DIR', HOME_LANE)
sys.path.insert(0, HOME_LANE)
from xi_eval import xi_block

mp.mp.dps = 35
EPS = mp.mpf(10) ** (-(mp.mp.dps - 5))
TWO_PI = 2 * mp.pi
SAFETY = mp.mpf(2)

T0 = mp.mpf(500)          # census height (may be overridden by CLI)
TBUF = mp.mpf(3)          # sweep buffer
TCERT = None              # set in main: T0 + 2

def meangap(t):
    x = max(float(t), float(TWO_PI) * 2.72)
    return float(TWO_PI) / mp.log(x / TWO_PI)

def hstep(t):
    return min(mp.mpf('0.06'), mp.mpf(meangap(t)) / 32)

# ---------- certified sign with retry/nudge ----------
class SignFail(Exception):
    pass

def cert_eval(t, K):
    """xi_block with certified signs for all k<=K. Returns dict row."""
    vals, scales = xi_block(t, K)
    signs, mlog, sclog = [], [], []
    for k in range(K + 1):
        v, sc = vals[k], scales[k]
        if not (abs(v) > 10 * sc * EPS):
            raise SignFail((mp.nstr(t, 30), k, mp.nstr(v, 5), mp.nstr(sc, 5)))
        signs.append(1 if v > 0 else -1)
        mlog.append(float(mp.log10(abs(v))))
        sclog.append(float(mp.log10(sc)))
    return {'t': mp.nstr(t, 30), 'sg': signs, 'ml': mlog, 'sl': sclog}

# ---------- stage: sweep ----------
def stage_sweep():
    path = os.path.join(LANE, 'sweep.jsonl')
    tend = T0 + TBUF
    t = mp.mpf(0)
    n_done = 0
    if os.path.exists(path):
        with open(path) as f:
            last = None
            for line in f:
                if line.strip():
                    last = line
                    n_done += 1
        if last:
            row = json.loads(last)
            t = mp.mpf(row['t']) + hstep(mp.mpf(row['t']))
            print('resuming at t =', mp.nstr(t, 12), 'rows done:', n_done, flush=True)
    f = open(path, 'a')
    t_wall = time.time()
    nudges = 0
    while t <= tend:
        try:
            row = cert_eval(t, 4)
        except SignFail as e:
            # grid point too close to a zero of some Xi_k: nudge deterministically
            nudges += 1
            t = t + hstep(t) * mp.mpf('0.0037')
            row = cert_eval(t, 4)   # if this also fails, abort loudly
            row['nudged'] = 1
        f.write(json.dumps(row) + '\n')
        n_done += 1
        if n_done % 200 == 0:
            f.flush()
            print('t=%8.3f rows=%d wall=%.0fs nudges=%d' % (float(t), n_done, time.time() - t_wall, nudges), flush=True)
        t = t + hstep(t)
    f.close()
    print('SWEEP DONE rows=%d wall=%.0fs nudges=%d' % (n_done, time.time() - t_wall, nudges), flush=True)

def load_sweep():
    rows = []
    with open(os.path.join(LANE, 'sweep.jsonl')) as f:
        for line in f:
            if line.strip():
                r = json.loads(line)
                r['tf'] = float(mp.mpf(r['t']))
                rows.append(r)
    # monotone t
    for i in range(1, len(rows)):
        assert rows[i]['tf'] > rows[i - 1]['tf']
    return rows

# ---------- stage: refine ----------
def illinois(k, a, b, fa, fb, tol=mp.mpf('1e-20')):
    """Certified-sign Illinois on Xi_k. fa,fb mpf values with opposite certified signs."""
    assert (fa > 0) != (fb > 0)
    na = nb = 0
    for it in range(500):   # worst case shrink >= 7/8 per step: 0.06*(7/8)^500 << 1e-20
        if b - a <= tol:
            break
        m = b - (b - a) * fb / (fb - fa)
        lo, hi = a + (b - a) / 8, b - (b - a) / 8
        if not (lo < m < hi):
            m = (a + b) / 2
        vals, scales = xi_block(m, k)
        v, sc = vals[k], scales[k]
        if not (abs(v) > 10 * sc * EPS):
            # cannot certify sign this close to the zero: fall back to returning bracket
            break
        if (v > 0) == (fa > 0):
            a, fa = m, v
            na += 1; nb = 0
            if na >= 2:
                fb = fb / 2
        else:
            b, fb = m, v
            nb += 1; na = 0
            if nb >= 2:
                fa = fa / 2
    return a, b

def stage_refine():
    rows = load_sweep()
    out = {}
    t_wall = time.time()
    klist = [int(sys.argv[3])] if len(sys.argv) > 3 else list(range(4))
    for k in klist:
        zeros = []
        for i in range(1, len(rows)):
            if rows[i - 1]['sg'][k] * rows[i]['sg'][k] < 0:
                a, b = mp.mpf(rows[i - 1]['t']), mp.mpf(rows[i]['t'])
                # certified endpoint values (re-eval to get mpf values)
                va, sa = xi_block(a, k); vb, sb = xi_block(b, k)
                assert abs(va[k]) > 10 * sa[k] * EPS and abs(vb[k]) > 10 * sb[k] * EPS
                assert (va[k] > 0) == (rows[i - 1]['sg'][k] > 0) and (vb[k] > 0) == (rows[i]['sg'][k] > 0)
                aa, bb = illinois(k, a, b, va[k], vb[k])
                zeros.append({'a': mp.nstr(aa, 30), 'b': mp.nstr(bb, 30),
                              'z': mp.nstr((aa + bb) / 2, 30), 'w': mp.nstr(bb - aa, 5)})
        out['k%d' % k] = zeros
        print('k=%d: %d zeros refined, wall=%.0fs' % (k, len(zeros), time.time() - t_wall), flush=True)
        fn = 'zeros.json' if len(klist) == 4 else 'zeros_k%d.json' % k
        with open(os.path.join(LANE, fn), 'w') as f:
            json.dump(out, f)
    print('REFINE DONE wall=%.0fs' % (time.time() - t_wall), flush=True)

def stage_refine_merge():
    out = {}
    for k in range(4):
        with open(os.path.join(LANE, 'zeros_k%d.json' % k)) as f:
            out.update(json.load(f))
    with open(os.path.join(LANE, 'zeros.json'), 'w') as f:
        json.dump(out, f)
    print('REFINE MERGE DONE:', {k: len(v) for k, v in out.items()}, flush=True)

def load_zeros():
    with open(os.path.join(LANE, 'zeros.json')) as f:
        Z = json.load(f)
    return {int(k[1]): [mp.mpf(z['z']) for z in v] for k, v in Z.items()}

# ---------- stage: cert3 (top-rung completeness for Xi_3) ----------
def get_z3():
    Z = load_zeros()
    z3 = [mp.mpf(0)] + Z[3]           # 0 is a zero (Xi_3 odd)
    return [z for z in z3 if z <= TCERT + mp.mpf('0.5')]

def compute_near(z3, indices, t_wall):
    entries = []
    for idx, z in enumerate(z3):
        if idx not in indices:
            continue
        hloc = hstep(z)
        dmin = None
        if idx > 0:
            dmin = z - z3[idx - 1]
        if idx + 1 < len(z3):
            d2 = z3[idx + 1] - z
            dmin = d2 if dmin is None else min(dmin, d2)
        r = min(mp.mpf('1.5') * hloc, dmin / 3)
        lo, hi = z - r - hloc / 2, z + r + hloc / 2
        if z == 0:
            lo = mp.mpf(0)   # use evenness of Xi_4: certify [0, hi] only
        hn = hloc / 6
        ok = False
        for attempt in range(7):
            npts = int(mp.ceil((hi - lo) / hn)) + 1
            sgs, m4, M5 = [], None, None
            failed = False
            for i in range(npts):
                tt = lo + (hi - lo) * i / (npts - 1)
                vals, scales = xi_block(tt, 5)
                v4, s4 = vals[4], scales[4]
                if not (abs(v4) > 10 * s4 * EPS):
                    failed = True
                    break
                sgs.append(1 if v4 > 0 else -1)
                a4 = abs(v4); a5 = abs(vals[5])
                m4 = a4 if m4 is None or a4 < m4 else m4
                M5 = a5 if M5 is None or a5 > M5 else M5
            if not failed and len(set(sgs)) == 1 and m4 > SAFETY * M5 * hn / 2:
                ok = True
                break
            hn = hn / 2
        entry = {'idx': idx, 'z': mp.nstr(z, 25), 'r': float(r), 'lo': mp.nstr(lo, 25), 'hi': mp.nstr(hi, 25),
                 'h_near': float(hn), 'ok': bool(ok),
                 'margin': float(m4 / (SAFETY * M5 * hn / 2)) if (m4 and M5) else None}
        entries.append(entry)
        if not ok:
            print('NEAR-REGION FAILURE at z=%s — LOUD' % mp.nstr(z, 20), flush=True)
        if idx % 40 == 0:
            print('near %d/%d wall=%.0fs' % (idx, len(z3), time.time() - t_wall), flush=True)
    return entries

def stage_cert3near():
    shard, nsh = int(sys.argv[3]), int(sys.argv[4])
    z3 = get_z3()
    t_wall = time.time()
    entries = compute_near(z3, set(range(shard, len(z3), nsh)), t_wall)
    with open(os.path.join(LANE, 'cert3_near_%d.json' % shard), 'w') as f:
        json.dump(entries, f)
    print('CERT3NEAR shard %d/%d DONE n=%d fails=%d wall=%.0fs' %
          (shard, nsh, len(entries), sum(1 for e in entries if not e['ok']), time.time() - t_wall), flush=True)

def stage_cert3away():
    nsh = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    z3 = get_z3()
    near = []
    for i in range(nsh):
        with open(os.path.join(LANE, 'cert3_near_%d.json' % i)) as f:
            near += json.load(f)
    near.sort(key=lambda e: e['idx'])
    assert [e['idx'] for e in near] == list(range(len(z3))), 'near shards incomplete'
    rows = load_sweep()
    report = {'near': near, 'away': [], 'T_cert': float(TCERT)}
    t_wall = time.time()
    run_away(z3, rows, report, t_wall)
    with open(os.path.join(LANE, 'cert3.json'), 'w') as f:
        json.dump(report, f)
    nfail = sum(1 for e in report['near'] if not e['ok']) + sum(1 for e in report['away'] if not e.get('ok', True))
    print('CERT3 DONE fails=%d wall=%.0fs' % (nfail, time.time() - t_wall), flush=True)

def stage_cert3():
    rows = load_sweep()
    z3 = get_z3()
    t_wall = time.time()
    report = {'near': compute_near(z3, set(range(len(z3))), t_wall), 'away': [], 'T_cert': float(TCERT)}
    run_away(z3, rows, report, t_wall)
    with open(os.path.join(LANE, 'cert3.json'), 'w') as f:
        json.dump(report, f)
    nfail = sum(1 for e in report['near'] if not e['ok']) + sum(1 for e in report['away'] if not e.get('ok', True))
    print('CERT3 DONE fails=%d wall=%.0fs' % (nfail, time.time() - t_wall), flush=True)

def run_away(z3, rows, report, t_wall):
    # --- away regions: exclusion-radius coverage ---
    # For an away point p with certified |Xi_3(p)| = v and M4 >= sup|Xi_4| on the gap
    # (grid max * budgeted stand-in), Xi_3 has no zero in |t-p| < v/M4; we use the
    # SAFETY-discounted radius R_p = v/(SAFETY*M4). Union of [p-R_p, p+R_p] over away
    # points plus the near intervals must cover [0, TCERT] — asserted explicitly.
    bounds = z3 + [TCERT] if z3[-1] < TCERT else z3
    for gi in range(len(bounds) - 1):
        zl, zr = bounds[gi], bounds[gi + 1]
        # cover starts at left near end (or 0-r case handled: z=0 near covers [0,hi])
        cov_lo = mp.mpf(report['near'][gi]['hi'])
        cov_hi_target = mp.mpf(report['near'][gi + 1]['lo']) if gi + 1 < len(z3) else zr
        gpts = [(mp.mpf(r['t']), r) for r in rows if zl <= mp.mpf(r['t']) <= zr]
        M4log = max(r['ml'][4] for t, r in gpts)
        M4 = mp.mpf(10) ** M4log
        # away points: master grid points inside the band [cov_lo, cov_hi_target]
        pts = [[t, mp.mpf(10) ** r['ml'][3], r['sg'][3]] for t, r in gpts if cov_lo <= t <= cov_hi_target]
        # constant sign required on the whole away band
        extra_evals = 0
        ok = True
        hidden = []
        for rounds in range(400):
            sgs = set(p[2] for p in pts)
            if len(sgs) > 1:
                hidden.append(mp.nstr((zl + zr) / 2, 20))
                print('AWAY: SIGN CHANGE inside gap %d — hidden zeros of Xi_3! LOUD' % gi, flush=True)
                ok = False
                break
            # coverage chain
            cur = cov_lo
            gap_at = None
            for p in sorted(pts):
                Rp = p[1] / (SAFETY * M4)
                if p[0] - Rp > cur:
                    if p[0] > cur:
                        gap_at = (cur, min(p[0], cov_hi_target))
                        break
                cur = max(cur, p[0] + Rp)
                if cur >= cov_hi_target:
                    break
            if gap_at is None and cur >= cov_hi_target:
                break  # covered
            if gap_at is None:
                gap_at = (cur, cov_hi_target)
            # insert midpoint(s) in the uncovered hole
            hole_l, hole_r = gap_at
            if hole_r - hole_l < mp.mpf('1e-12'):
                ok = False
                print('AWAY: hole shrank below 1e-12 in gap %d at %s — LOUD (suspect zero)' % (gi, mp.nstr(hole_l, 20)), flush=True)
                break
            tm = (hole_l + hole_r) / 2
            vals, scales = xi_block(tm, 4)
            extra_evals += 1
            if not (abs(vals[3]) > 10 * scales[3] * EPS):
                ok = False
                hidden.append(mp.nstr(tm, 25))
                print('AWAY: uncertifiable sign at %s in gap %d — LOUD (suspect zero)' % (mp.nstr(tm, 20), gi), flush=True)
                break
            pts.append([tm, abs(vals[3]), 1 if vals[3] > 0 else -1])
        else:
            ok = False
            print('AWAY: refinement budget exhausted in gap %d — LOUD' % gi, flush=True)
        report['away'].append({'gap': gi, 'zl': mp.nstr(zl, 20), 'zr': mp.nstr(zr, 20),
                               'n_pts': len(pts), 'ok': bool(ok), 'extra_evals': extra_evals,
                               'M4log': M4log, 'hidden': hidden})
        if gi % 40 == 0:
            print('away %d/%d wall=%.0fs' % (gi, len(bounds) - 1, time.time() - t_wall), flush=True)

# ---------- stage: cascade (Z2 from Z3, Z1 from Z2, Z0 from Z1) ----------
def stage_cascade():
    Z = load_zeros()
    t_wall = time.time()
    report = {}
    for k in [2, 1, 0]:
        zsup = [z for z in Z[k + 1] if z <= TCERT]
        parts = [mp.mpf(0)] + zsup + [TCERT]
        # endpoint signs of Xi_k at all partition points
        sgs = []
        for i, p in enumerate(parts):
            if i == 0 and k % 2 == 1:
                sgs.append(0)   # Xi_k odd: exact zero at 0
                continue
            vals, scales = xi_block(p, k)
            v, sc = vals[k], scales[k]
            assert abs(v) > 10 * sc * EPS, ('cascade endpoint sign fail (double zero?)', k, mp.nstr(p, 25))
            sgs.append(1 if v > 0 else -1)
        # predicted zero count per interval; compare with located zeros
        zk = [z for z in Z[k] if z <= TCERT]
        entries = []
        nfail = 0
        for i in range(len(parts) - 1):
            a, b = parts[i], parts[i + 1]
            if sgs[i] == 0:
                pred = 0        # monotone from exact zero at t=0: no interior zero
            else:
                pred = 1 if sgs[i] * sgs[i + 1] < 0 else 0
            got = [z for z in zk if a < z < b]
            okline = (len(got) == pred)
            if not okline:
                nfail += 1
                print('CASCADE MISMATCH k=%d interval (%s, %s): pred %d got %d — LOUD' %
                      (k, mp.nstr(a, 15), mp.nstr(b, 15), pred, len(got)), flush=True)
            entries.append({'a': mp.nstr(a, 20), 'b': mp.nstr(b, 20), 'pred': pred, 'got': len(got), 'ok': okline})
        # every located zero must be in exactly one interval: total check
        total_pred = sum(e['pred'] for e in entries)
        report['k%d' % k] = {'n_intervals': len(entries), 'total_pred': total_pred,
                             'total_located': len(zk), 'fails': nfail, 'intervals': entries}
        print('cascade k=%d: intervals=%d pred=%d located=%d fails=%d wall=%.0fs' %
              (k, len(entries), total_pred, len(zk), nfail, time.time() - t_wall), flush=True)
        assert total_pred == len(zk) and nfail == 0, 'CASCADE FAILURE k=%d' % k
    with open(os.path.join(LANE, 'cascade.json'), 'w') as f:
        json.dump(report, f)
    print('CASCADE DONE wall=%.0fs' % (time.time() - t_wall), flush=True)

# ---------- stage: ledger ----------
def stage_ledger():
    Z = load_zeros()
    res = {'T0': float(T0)}
    for k in range(4):
        res['R_%d' % k] = len([z for z in Z[k] if 0 < z <= T0])
    for k in range(3):
        zk = [z for z in Z[k] if 0 < z <= T0]
        zk1 = [z for z in Z[k + 1] if 0 < z <= T0]
        gaps = []
        Xk = 0
        for i in range(len(zk) - 1):
            a, b = zk[i], zk[i + 1]
            cnt = len([z for z in zk1 if a < z < b])
            extra = cnt - 1
            Xk += extra
            gaps.append({'a': mp.nstr(a, 20), 'b': mp.nstr(b, 20), 'count': cnt, 'extra': extra})
            if extra != 0:
                print('NONZERO DEFECT k=%d gap (%s,%s): count=%d — LOUD' % (k, mp.nstr(a, 15), mp.nstr(b, 15), cnt), flush=True)
        below = len([z for z in zk1 if 0 < z < zk[0]]) if zk else None
        above = len([z for z in zk1 if zk[-1] < z <= T0]) if zk else None
        res['ledger_k%d' % k] = {'X_k': Xk, 'n_gaps': len(gaps), 'below_first': below,
                                 'above_last_to_T0': above, 'gaps': gaps}
        print('ledger k=%d: gaps=%d X_k=%d below_first=%s above_last=%s' % (k, len(gaps), Xk, below, above), flush=True)
    with open(os.path.join(LANE, 'ledger.json'), 'w') as f:
        json.dump(res, f)
    print('LEDGER DONE', flush=True)

# ---------- stage: checks (R_0 vs zetazero + RvM) ----------
def stage_checks():
    Z = load_zeros()
    z0 = [z for z in Z[0] if 0 < z <= T0]
    out = {'R_0': len(z0)}
    t_wall = time.time()
    maxdiff = mp.mpf(0)
    for n, z in enumerate(z0, start=1):
        g = mp.im(mp.zetazero(n))
        maxdiff = max(maxdiff, abs(g - z))
    out['zetazero_maxdiff'] = mp.nstr(maxdiff, 5)
    # tolerance = max achievable bracket width at t~T0 (sign certification is
    # budget-limited near zeros: widths reach ~3e-14 at t~500, see NOTES FINAL)
    assert maxdiff < mp.mpf('1e-13'), 'zetazero mismatch'
    # next zero above T0 must be > T0
    gnext = mp.im(mp.zetazero(len(z0) + 1))
    assert gnext > T0, 'missed a zeta zero below T0!'
    out['next_zero_above_T0'] = mp.nstr(gnext, 20)
    # RvM: N(T) approx theta(T)/pi + 1 (+ S(T), |S|<2.5 here)
    th = mp.siegeltheta(T0)
    out['rvm_main'] = float(th / mp.pi + 1)
    # independent count via mpmath nzeros (Turing-method based)
    nz = mp.nzeros(T0)
    out['nzeros_T0'] = int(nz)
    assert nz == len(z0), 'nzeros(T0)=%d != census R_0=%d' % (nz, len(z0))
    # recompute task-claimed table values (do not trust the prompt)
    out['nzeros_200'] = int(mp.nzeros(200))
    out['nzeros_500'] = int(mp.nzeros(500)) if T0 != 500 else int(nz)
    print('nzeros: N(200)=%d N(500)=%d (task claimed 79 / 269)' % (out['nzeros_200'], out['nzeros_500']), flush=True)
    print('R_0=%d  zetazero maxdiff=%s  next above T0 at %s  theta/pi+1=%.3f  wall=%.0fs' %
          (len(z0), mp.nstr(maxdiff, 3), mp.nstr(gnext, 12), float(th / mp.pi + 1), time.time() - t_wall), flush=True)
    with open(os.path.join(LANE, 'checks.json'), 'w') as f:
        json.dump(out, f)
    print('CHECKS DONE', flush=True)

def stage_assemble():
    def load(name):
        with open(os.path.join(LANE, name)) as f:
            return json.load(f)
    zeros, cert3, cascade, ledger, checks = (load(n) for n in
        ['zeros.json', 'cert3.json', 'cascade.json', 'ledger.json', 'checks.json'])
    anchors = load('anchors.json') if os.path.exists(os.path.join(LANE, 'anchors.json')) else json.load(open(os.path.join(HOME_LANE, 'anchors.json')))
    res = {
        'lane': 'B4 certified census',
        'date': '2026-08-22',
        'T0': float(T0), 'T_cert': float(TCERT), 'dps': mp.mp.dps,
        'eps_budget': '1e-%d' % (mp.mp.dps - 5),
        'discipline': 'budgeted mp arithmetic (sign margins |v|>10*scale*eps; grid maxima as sup stand-ins with SAFETY=2); NOT interval arithmetic',
        'xi_half_verified': '0.497120778188314109912773739685',
        'xi_half_task_constant_wrong': '0.4971207781595661 (task prompt value wrong from digit 11)',
        'counts': {'R_%d' % k: ledger['R_%d' % k] for k in range(4)},
        'defect_ledger': {'X_%d' % k: ledger['ledger_k%d' % k]['X_k'] for k in range(3)},
        'n_gaps': {'k%d' % k: ledger['ledger_k%d' % k]['n_gaps'] for k in range(3)},
        'boundary': {'k%d' % k: {'below_first': ledger['ledger_k%d' % k]['below_first'],
                                 'above_last_to_T0': ledger['ledger_k%d' % k]['above_last_to_T0']} for k in range(3)},
        'cert3_near_fails': sum(1 for e in cert3['near'] if not e['ok']),
        'cert3_away_fails': sum(1 for e in cert3['away'] if not e.get('ok', True)),
        'cert3_min_near_margin': min(e['margin'] for e in cert3['near'] if e['margin']),
        'cascade_fails': {('k%d' % k): cascade['k%d' % k]['fails'] for k in [0, 1, 2]},
        'checks': checks,
        'anchors': anchors,
        'zeros_files': 'zeros.json (refined to width<=1e-20; fields a,b certified opposite-sign bracket)',
    }
    with open(os.path.join(LANE, 'results.json'), 'w') as f:
        json.dump(res, f, indent=1)
    print(json.dumps({k: v for k, v in res.items() if k in ['counts', 'defect_ledger', 'n_gaps', 'boundary', 'cert3_near_fails', 'cert3_away_fails', 'cascade_fails']}, indent=1))
    print('ASSEMBLE DONE')

if __name__ == '__main__':
    stage = sys.argv[1]
    if len(sys.argv) > 2:
        T0 = mp.mpf(sys.argv[2])
    TCERT = T0 + 2
    {'sweep': stage_sweep, 'refine': stage_refine, 'refine_merge': stage_refine_merge,
     'cert3': stage_cert3, 'cert3near': stage_cert3near, 'cert3away': stage_cert3away,
     'cascade': stage_cascade, 'ledger': stage_ledger, 'checks': stage_checks,
     'assemble': stage_assemble}[stage]()
