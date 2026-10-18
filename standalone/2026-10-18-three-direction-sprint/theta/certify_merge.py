"""Fresh complete-theta interval contraction for one tree merge (remove a hub edge and insert a positive cross edge).

Only exact rational inputs and the pinned outward integer backend enter the
acceptance calculation.  A fixed finite preconditioner need not be an exact
center inverse: the checked norm below one independently proves invertibility.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import sys
import time
import merge_model as model

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'theta'))
sys.path.insert(0, str(ROOT/'theta/inherited'))
import pr886_primitive as b
import source_extended
from certify_nonnegative_obstruction import load
I, SCALE = b.I, b.SCALE


def certify(parameters):
    primitive = ROOT/'theta/inherited/pr886_primitive.py'
    b.require(hashlib.sha256(primitive.read_bytes()).hexdigest() ==
              '2eba75b7fc82617342c20f6a06270462b6d82f1e7162f66847c029e7e5a9fa55',
              'pinned outward backend identity')
    p = load(parameters)
    b.require(p['schema'] == 'TS.merge.parameters.v1', 'merged-tree parameter schema')
    degree, counts, active = p['degree'], p['counts'], p['active']
    c, eta, radius = list(map(F, p['centers'])), F(p['hub_correlation']), F(p['radius'])
    types = p['merge_types']
    b.require(len(p['merge_ends']) == 2 and all(type(v) is int and v in (0,1) for v in p['merge_ends']), 'two legal merge endpoint flags')
    vertices = ['root' if v == 0 else 'child' for v in p['merge_ends']]
    b.require(type(degree) is int and 2 <= degree <= 32 and degree % 2 == 0,
              'complete even source degree')
    n = degree//2
    b.require(len(counts) >= 2 and all(type(x) is int and x > 0 for x in counts),
              'all component multiplicities positive integers')
    b.require(len(c) == 3*len(counts)+1 and c[1] == 0 and c[2] == 1,
              'complete model and fair-sign coordinates')
    b.require(len(active) == n and len(set(active)) == n and
              all(type(k) is int and 0 <= k < len(c) and k not in (1, 2) for k in active),
              'complete distinct square active chart')
    b.require(len(types) == 2 and all(type(k) is int for k in types) and
              0 <= types[0] <= types[1] < len(counts) and
              (types[0] != types[1] or counts[types[0]] >= 2),
              'cross edge joins distinct component copies')
    b.require(len(vertices) == 2 and all(v in ('root', 'child') for v in vertices) and
              all(k != 0 or v == 'root' for k, v in zip(types, vertices)),
              'cross edge endpoints exist')
    b.require(eta == F(1, 10**10) and 0 < radius <= F(1, 10**20),
              'fixed positive hub and small rational cube')
    box = [I(I.coerce(x-(radius if k in active else 0)).lo,
             I.coerce(x+(radius if k in active else 0)).hi) for k, x in enumerate(c)]
    b.require(box[0].lo > 0, 'positive singleton weight on cube')
    biases = [I.coerce(eta), box[-1]]
    for k in range(1, len(counts)):
        A, B, prob = box[3*k:3*k+3]
        b.require((A+B).lo > 0 and (A-B).lo > 0, 'all physical weights positive on cube')
        b.require(prob.lo > I.rat(1, 2).hi and prob.hi < SCALE,
                  'all dimer couplings positive and finite')
        biases.append(2*prob-1)
    b.require(all(q.lo > I.rat(1, 10**11).hi and
                  q.hi < I.rat(999999999, 10**9).lo for q in biases),
              'every edge bias strictly inside (0,1)')
    support = sum((counts[k]*box[3*k] for k in range(len(counts))), I.coerce(0))
    b.require(support.hi < I.coerce(12).lo, 'complete observable support below twelve')
    # A tree cluster normalized through its single hub attachment has total mass1.
    normalizer = I.coerce(1)
    print('TS_MERGE_FRESH_COMPLETE_THETA_SOURCE', degree, flush=True)
    src = source_extended.reconstruct(degree)
    target = [I(*record) for record in src['standardized_cumulant_ratios']]
    b.require(len(target) == n and len(src['standardized_moments']) == degree+1,
              'all source moments and complete tails present')
    R = [[F(v) for v in row] for row in p['rational_preconditioner']]
    b.require(len(R) == n and all(len(row) == n for row in R), 'fixed square rational witness')
    value, _ = model.evaluate([I.coerce(x) for x in c], counts, types, p['merge_ends'], eta, degree)
    residual = [value[k]-target[k] for k in range(n)]
    beta = F(max(b.absup(sum((R[i][k]*residual[k] for k in range(n)), I.coerce(0)))
                 for i in range(n)), SCALE)
    print('TS_MERGE_WHOLE_CUBE_JACOBIAN', flush=True)
    _, J, raw = model.jet(box, counts, types, p['merge_ends'], eta, degree, active)
    L = F(max(sum(b.absup(I.coerce(int(i == j))-
                         sum((R[i][k]*J[k][j] for k in range(n)), I.coerce(0)))
                  for j in range(n)) for i in range(n)), SCALE)
    margin = radius-beta-L*radius
    print('TS_MERGE_BOUNDS', 'beta', float(beta), 'L', float(L), 'radius', float(radius), flush=True)
    b.require(L < F(1, 1000), 'strict contraction throughout the entire cube')
    b.require(beta < radius/100, 'fresh complete-source center displacement below one percent of radius')
    b.require(margin > F(99, 100)*radius, 'strict cube invariance')
    b.require(all(raw[k].lo <= src['standardized_moments'][k][1] and
                  raw[k].hi >= src['standardized_moments'][k][0] for k in range(degree+1)),
              'diagnostic raw source and model enclosure overlap at every order')
    observed = counts[0]+2*sum(counts[1:])
    edges = sum(counts)+sum(counts[1:])
    b.require(edges == observed, 'connected merged graph remains a tree')
    names = ['theta/merge_model.py', 'theta/model.py', 'theta/certify_merge.py', 'theta/source_extended.py',
             'theta/certify_nonnegative_obstruction.py', 'theta/inherited/pr886_primitive.py']
    return {'schema': 'TS.merge.certificate.v1',
            'status': 'PROPOSED_COMPUTER_ASSISTED_FINITE_THEOREM', 'rh_proved': False,
            'degree': degree, 'vertices': observed+1, 'observed_vertices': observed,
            'edges': edges, 'positive_edges': edges, 'cycle_rank': 0,
            'counts': counts, 'active': active, 'parameters': p,
            'radius': str(radius), 'beta_upper': str(beta), 'contraction_upper': str(L),
            'invariance_margin': str(margin), 'support_interval': support.record(),
            'conditional_normalizer_interval': normalizer.record(),
            'edge_bias_types': [q.record() for q in biases], 'complete_theta_source': src,
            'parameter_sha256': hashlib.sha256(parameters.read_bytes()).hexdigest(),
            'input_hashes': {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in names}}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--parameters', type=Path, required=True)
    ap.add_argument('--emit', type=Path)
    ap.add_argument('--check', type=Path)
    args = ap.parse_args()
    b.require(bool(args.emit) != bool(args.check), 'choose exactly one of emit and check')
    began = time.monotonic()
    result = certify(args.parameters)
    text = json.dumps(result, sort_keys=True, separators=(',', ':'))+'\n'
    if args.emit: args.emit.write_text(text)
    if args.check: b.require(load(args.check) == result, 'fresh certificate equality')
    print('TS_MERGE_CERTIFICATE_PASS', hashlib.sha256(text.encode()).hexdigest(),
          'seconds', time.monotonic()-began, flush=True)
