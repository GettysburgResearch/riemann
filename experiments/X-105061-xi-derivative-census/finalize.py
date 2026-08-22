"""Build results.json in the orchestrator schema from completed stage outputs.
Schema: {T0, dps, per_k: {count, zeros, min_sign_margin}, interlacing: {k:
{gaps, extras_total, extra_gaps}}, cross_checks: {...}, incidents: []}.
Also computes min gap per k and the global tightest sign margin vs budget.
Run AFTER: refine_merge, cert3away, cascade, ledger, checks, assemble.
"""
import json, os, sys
import mpmath as mp

LANE = os.environ.get('LANE_DIR', os.path.dirname(os.path.abspath(__file__)))
mp.mp.dps = 35
sys.path.insert(0, LANE)
from xi_eval import xi_block
EPS = mp.mpf(10) ** (-(mp.mp.dps - 5))

def load(n):
    with open(os.path.join(LANE, n)) as f:
        return json.load(f)

zeros, cert3, cascade, ledger, checks, anchors, assembled = (
    load(n) for n in ['zeros.json', 'cert3.json', 'cascade.json', 'ledger.json',
                      'checks.json', 'anchors.json', 'results_assembled.json'])
T0 = mp.mpf(ledger['T0'])
incidents = []

# --- sign margins & incidents from sweep ---
min_margin = {k: None for k in range(5)}   # |v|/(scale*EPS), from log10 data
nudged = []
nrows = 0
with open(os.path.join(LANE, 'sweep.jsonl')) as f:
    for line in f:
        if not line.strip():
            continue
        r = json.loads(line)
        nrows += 1
        for k in range(5):
            marg = 10 ** (r['ml'][k] - r['sl'][k] + (mp.mp.dps - 5))
            if min_margin[k] is None or marg < min_margin[k]:
                min_margin[k] = marg
        if r.get('nudged'):
            nudged.append(r['t'])
if nudged:
    incidents.append({'type': 'sweep_nudges', 'count': len(nudged),
                      'detail': 'grid points landed within sign-margin of a zero; deterministically nudged by 0.0037*h', 't': nudged})

# near-region halvings (h_near below initial hloc/6 means retries happened)
halved = [e for e in cert3['near'] if e['h_near'] < 0.99 * (min(0.06, float(2 * mp.pi / mp.log(max(float(e['z']) if float(e['z']) > 0 else 17.0, 17.08) / (2 * mp.pi)))) / 32) / 6]
away_extra = sum(e['extra_evals'] for e in cert3['away'])
if away_extra:
    incidents.append({'type': 'away_midpoint_insertions', 'total_extra_evals': away_extra,
                      'detail': 'coverage holes filled by certified midpoint evals (normal refinement, no failures)'})

# --- per_k ---
per_k = {}
min_gap = {}
for k in range(4):
    zk_all = [mp.mpf(z['z']) for z in zeros['k%d' % k]]
    zk = [z for z in zk_all if 0 < z <= T0]
    gaps = [float(zk[i + 1] - zk[i]) for i in range(len(zk) - 1)]
    min_gap[k] = min(gaps)
    per_k['k%d' % k] = {
        'count': len(zk),
        'zeros': [mp.nstr(z, 25) for z in zk],
        'min_sign_margin': min_margin[k],
        'min_gap': min_gap[k],
        'max_bracket_width': max(float(mp.mpf(z['w'])) for z in zeros['k%d' % k]),
    }
    assert len(zk) == ledger['R_%d' % k], 'ledger count mismatch k=%d' % k

# --- interlacing / defect ledger ---
interlacing = {}
for k in range(3):
    L = ledger['ledger_k%d' % k]
    extra_gaps = [g for g in L['gaps'] if g['extra'] != 0]
    interlacing['k%d' % k] = {'gaps': L['n_gaps'], 'extras_total': L['X_k'],
                              'extra_gaps': extra_gaps,
                              'below_first': L['below_first'],
                              'above_last_to_T0': L['above_last_to_T0']}
    if extra_gaps:
        incidents.append({'type': 'NONZERO_DEFECT', 'k': k, 'gaps': extra_gaps})

# --- cross-checks (fresh evals where cheap) ---
v0, s0 = xi_block(mp.mpf(0), 3)
xi1_at_0_ok = abs(v0[1]) <= 10 * s0[1] * EPS and abs(v0[3]) <= 10 * s0[3] * EPS
assert xi1_at_0_ok, 'Xi_1(0)/Xi_3(0) oddness FAIL'
th = mp.siegeltheta(T0)
rvm = float(th / mp.pi + 1)
cross = {
    'R0_vs_nzeros_T0': [per_k['k0']['count'], checks['nzeros_T0']],
    'nzeros_200': checks['nzeros_200'], 'nzeros_500': checks['nzeros_500'],
    'rvm_theta_over_pi_plus_1': rvm,
    'S_T0_implied': per_k['k0']['count'] - rvm,
    'zetazero_maxdiff': checks['zetazero_maxdiff'],
    'next_zeta_zero_above_T0': checks['next_zero_above_T0'],
    'xi1_xi3_vanish_at_0_within_budget': xi1_at_0_ok,
    'xi_half_verified': '0.497120778188314109912773739685',
    'anchors': anchors,
}
assert per_k['k0']['count'] == checks['nzeros_T0'], 'R_0 != nzeros(T0)'
assert abs(cross['S_T0_implied']) < 2.5, 'S(T0) out of plausible range'

# --- certificate summary ---
cert_summary = {
    'near_entries': len(cert3['near']), 'near_fails': sum(1 for e in cert3['near'] if not e['ok']),
    'min_near_margin': min(e['margin'] for e in cert3['near'] if e['margin']),
    'away_gaps': len(cert3['away']), 'away_fails': sum(1 for e in cert3['away'] if not e.get('ok', True)),
    'cascade_fails': {('k%d' % k): cascade['k%d' % k]['fails'] for k in [0, 1, 2]},
    'near_halved_entries': len(halved),
}
for nm, cnt in [('near_fails', cert_summary['near_fails']), ('away_fails', cert_summary['away_fails'])]:
    if cnt:
        incidents.append({'type': 'CERT_FAILURE', 'which': nm, 'count': cnt})

res = {
    'T0': float(T0), 'T_cert': float(T0 + 2), 'dps': mp.mp.dps,
    'discipline': assembled['discipline'],
    'per_k': per_k,
    'interlacing': interlacing,
    'cross_checks': cross,
    'certificates': cert_summary,
    'sweep_rows': nrows,
    'incidents': incidents,
    'headline': {
        'R': {k: per_k['k%d' % k]['count'] for k in range(4)},
        'X': {k: interlacing['k%d' % k]['extras_total'] for k in range(3)},
        'min_gap': min_gap,
        'tightest_sweep_sign_margin_vs_budget': min(min_margin[k] for k in range(5)),
    },
}
with open(os.path.join(LANE, 'results.json'), 'w') as f:
    json.dump(res, f, indent=1)
print(json.dumps(res['headline'], indent=1))
print('cert_summary:', json.dumps(cert_summary))
print('incidents:', len(incidents))
print('FINALIZE DONE')
