#!/usr/bin/env python3
"""Exact finite Ising/cloning/cluster controls, not an RH or analytic proof."""
from fractions import Fraction as F
from itertools import product
from math import comb, prod
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'PROOF.md', 'README.md', 'REVIEW.md', 'SOURCES.json', 'VALIDATION.md',
         'check.py', 'test_check.py', 'result.json', 'SHA256SUMS'}
PARENT = '7ff754c7347d6ee9d59608e562e469351b3d37e7'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def spin_distribution(n, edges):
    need(type(n) is int and n > 0, 'invalid vertex count')
    for i, j, r in edges:
        need(0 <= i < j < n and F(0) < r <= F(1), 'invalid edge')
    need(len({(i, j) for i, j, _ in edges}) == len(edges), 'duplicate edge')
    out = {}
    for s in product((-1, 1), repeat=n):
        weight = prod((r for i, j, r in edges if s[i] != s[j]), start=F(1))
        out[s] = weight
    z = sum(out.values(), F(0))
    need(z > 0, 'partition')
    return {s: w / z for s, w in out.items()}


def observable_moments(law, weights, order=6):
    return [sum((p * sum((a * x for a, x in zip(weights, s)), F(0)) ** k
                 for s, p in law.items()), F(0)) for k in range(order + 1)]


def components(n, edges):
    # Explicit graph traversal, independent of the RC disjoint-set implementation.
    adjacency = [set() for _ in range(n)]
    for i, j, _ in edges:
        adjacency[i].add(j)
        adjacency[j].add(i)
    unseen = set(range(n))
    groups = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack = [start]
        group = []
        while stack:
            i = stack.pop()
            group.append(i)
            for j in adjacency[i] & unseen:
                unseen.remove(j)
                stack.append(j)
        groups.append(sorted(group))
    return groups, adjacency


def clone_graph(n, edges, weights, delta, wire=F(1, 2**20), bridge=F(999, 1000)):
    degree = [0] * n
    for i, j, _ in edges:
        degree[i] += 1
        degree[j] += 1
    # Rational ceiling, never float rounding.
    counts = [max(degree[i] + 2, (a / delta).__ceil__()) for i, a in enumerate(weights)]
    modules, at = [], 0
    for k in counts:
        modules.append(list(range(at, at + k)))
        at += k
    full = []
    for module in modules:
        full.extend((i, j, wire) for i, j in zip(module, module[1:]))
    used = [0] * n
    for i, j, r in edges:
        a, b = modules[i][used[i]], modules[j][used[j]]
        used[i] += 1
        used[j] += 1
        full.append((min(a, b), max(a, b), r))
    groups, _ = components(n, edges)
    chosen = [group[0] for group in groups]
    original_bridges = []
    for i, j in zip(chosen, chosen[1:]):
        a, b = modules[i][-1], modules[j][-1]
        full.append((min(a, b), max(a, b), bridge))
        original_bridges.append((min(i, j), max(i, j), bridge))
    return counts, modules, full, original_bridges


def rc_statistics(n, edges, weights):
    totals = {k: F(0) for k in ('one', 'V', 'V2', 'V3', 'W', 'VW', 'U')}
    for active in product((False, True), repeat=len(edges)):
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        factor = F(1)
        for on, (i, j, r) in zip(active, edges):
            factor *= (1-r) if on else r
            if on:
                parent[find(i)] = find(j)
        amplitude = {}
        for i, a in enumerate(weights):
            root = find(i)
            amplitude[root] = amplitude.get(root, F(0)) + a
        cluster_factor = 2 ** len(amplitude)
        weight = factor * cluster_factor
        V = sum((a*a for a in amplitude.values()), F(0))
        W = sum((a**4 for a in amplitude.values()), F(0))
        U = sum((a**6 for a in amplitude.values()), F(0))
        vals = dict(one=F(1), V=V, V2=V*V, V3=V**3, W=W, VW=V*W, U=U)
        for k, value in vals.items():
            totals[k] += weight * value
    z = totals['one']
    need(z > 0, 'RC partition')
    return {k: value/z for k, value in totals.items()}


def reconstruct():
    records = []
    clone_cases = [
        (2, [(0, 1, F(1, 3))], [F(1, 2), F(1)], F(1, 4)),
        (2, [(0, 1, F(2, 5))], [F(1, 2), F(1)], F(1, 8)),
        (3, [(0, 1, F(1, 2))], [F(0), F(1, 2), F(1, 4)], F(1, 4)),
        (3, [(0, 1, F(2, 3)), (1, 2, F(1, 3))], [F(1, 2)]*3, F(1, 4)),
        (3, [], [F(1, 4), F(1, 2), F(3, 4)], F(1, 2)),
    ]
    clone_states = 0
    for n, edges, weights, delta in clone_cases:
        old = spin_distribution(n, edges)
        counts, modules, full, bridges = clone_graph(n, edges, weights, delta)
        N, K = sum(counts), 2*len(edges)+2*n
        groups, adj = components(N, full)
        need(len(groups) == 1 and max(map(len, adj)) <= 3, 'connected degree-three')
        A, B0 = sum(weights, F(0)), sum(weights, F(0))+K*delta
        need(N <= A/delta+K, 'clone size')
        need(sum((abs(delta*k-a) for k, a in zip(counts, weights)), F(0)) <= K*delta,
             'weight rounding')
        law = spin_distribution(N, full)
        clone_states += len(law)
        aligned = {}
        for s, p in law.items():
            if all(len({s[v] for v in module}) == 1 for module in modules):
                reps = tuple(s[module[0]] for module in modules)
                aligned[reps] = aligned.get(reps, F(0))+p
        good = sum(aligned.values(), F(0))
        need(good > 0, 'alignment probability')
        aligned = {s: p/good for s, p in aligned.items()}
        need(aligned == spin_distribution(n, edges+bridges), 'exact conditioned source')
        eta = F(2**(N-1), 2**20)
        need(1-good <= eta, 'all-plus defect bound')
        bridge_ratio = 1/prod((r for _, _, r in bridges), start=F(1))
        after = observable_moments(law, [delta]*N)
        before = observable_moments(old, weights)
        for k in range(1, 7):
            bound = k*B0**(k-1)*K*delta + 2*B0**k*(eta+bridge_ratio-1)
            need(abs(after[k]-before[k]) <= bound, 'complete clone moment bound')
        need(all(after[k] == before[k] == 0 for k in (1, 3, 5)), 'spin-flip symmetry')
        records.append(['clone', n, N, str(good), str(after[2])])

    graph_cases = [
        (1, [], [F(1)]),
        (2, [(0, 1, F(3, 5))], [F(1), F(1)]),
        (3, [(0, 1, F(1, 3)), (1, 2, F(2, 3))], [F(1, 2), F(1), F(0)]),
        (3, [(0, 1, F(1, 2)), (0, 2, F(2, 5)), (1, 2, F(3, 4))], [F(1)]*3),
        (4, [(0, 1, F(1, 2)), (1, 2, F(1, 3)), (2, 3, F(1, 4)), (0, 3, F(2, 3))],
         [F(1, 3), F(2, 3), F(1), F(4, 3)]),
        (5, [(0, i, F(i, i+1)) for i in range(1, 5)], [F(1)]*5),
        (6, [(i, j, F(1, 2)) for i in range(3) for j in range(3, 6)], [F(1, 2)]*6),
    ]
    rc_configs = spin_configs = 0
    for n, edges, weights in graph_cases:
        law = spin_distribution(n, edges)
        mu = observable_moments(law, weights)
        st = rc_statistics(n, edges, weights)
        rc_configs += 2**len(edges)
        spin_configs += 2**n
        need(mu[2] == st['V'], 'RC variance')
        need(mu[4] == 3*st['V2']-2*st['W'], 'RC fourth moment')
        need(mu[6] == 15*st['V3']-30*st['VW']+16*st['U'], 'RC sixth moment')
        k4 = mu[4]-3*mu[2]**2
        k6 = mu[6]-15*mu[4]*mu[2]+30*mu[2]**3
        need(k4 == 3*(st['V2']-st['V']**2)-2*st['W'], 'RC fourth cumulant')
        need(k6 == 15*(st['V3']-3*st['V2']*st['V']+2*st['V']**3)
             -30*(st['VW']-st['V']*st['W'])+16*st['U'], 'RC sixth cumulant')
        need(mu[4] <= 3*mu[2]**2, 'finite fourth-moment domination')
        need(law[(1,)*n] >= F(1, 2**n) and law[(-1,)*n] >= F(1, 2**n),
             'extreme probability')
        records.append(['RC', n, str(k4), str(k6)])

    bath_cases = 0
    for L in range(1, 33):
        for r in range(1, min(L, 6)+1):
            moment = sum((F(comb(L, k)*(2*k-L)**(2*r), 2**L)
                          for k in range(L+1)), F(0))
            df = prod(range(1, 2*r, 2))
            falling = prod(range(L-r+1, L+1))
            need(moment >= df*falling, 'bath paired-index lower bound')
            need(moment <= df*L**r, 'finite bath Gaussian upper bound')
            if r >= 2 and L >= r*(r-1):
                need(F(falling, L**r) >= F(1, 2), 'full falling-factorial bound')
            bath_cases += 1
            records.append(['bath', L, r, str(moment), falling])

    jet_cases = 0
    for L in (8, 64, 4096):
        for c2 in (F(1), F(3, 2), F(2)):
            for d in (F(1), F(2)):
                t = F(1, 3)
                gamma = 1-c2*t
                A = d*t*t + 2*gamma*gamma/L
                D = d+2*c2*c2/L
                root = D*t-2*c2/L
                need(root > 0 and gamma > 0, 'formal jet interior')
                need(D*A-2*d/L == root*root, 'exact normalization radical')
                need(-2*d*t+4*c2*gamma/L == -2*root, 'implicit derivative sign')
                jet_cases += 1
    # Two-spin lattice polynomial has exact unit-circle roots for Pythagorean rates.
    lattice_cases = 0
    for r, b in ((F(3,5), F(4,5)), (F(5,13), F(12,13)), (F(8,17), F(15,17))):
        need(r*r+b*b == 1, 'unit root')
        # u=-r+ib; 1+2r*u+u^2=0, checked in real and imaginary parts.
        need(1-2*r*r+r*r-b*b == 0 and 2*r*b-2*r*b == 0, 'lattice root polynomial')
        law = spin_distribution(2, [(0, 1, r)])
        weights = {s: sum((p for v,p in law.items() if sum(v)==s), F(0)) for s in (-2,0,2)}
        need(weights[-2] == weights[2] == 1/(2*(1+r))
             and weights[0] == r/(1+r), 'lattice polynomial is actual Ising source')
        lattice_cases += 1

    variance_cases = 0
    for k in range(2, 33):
        variances = [F(j, k*k) for j in range(1,k+1)]
        V = sum(variances, F(0))
        need(V <= 1 and sum((v*v for v in variances), F(0)) <= V*max(variances),
             'infinitesimal cloud variance budget')
        variance_cases += 1

    digest = hashlib.sha256(json.dumps(records, separators=(',', ':')).encode()).hexdigest()
    return {'schema': 1, 'status': 'PROPOSED_COMPONENTS_NOT_RH', 'parent_commit': PARENT,
            'rh_proved': False, 'all_order_realization_proved': False,
            'new_theta_integrals_executed': 0, 'actual_zeta_zeros_computed': 0,
            'cases': {'clone_graphs': len(clone_cases), 'clone_spin_configurations': clone_states,
                      'random_cluster_graphs': len(graph_cases), 'RC_edge_subsets': rc_configs,
                      'RC_comparison_spin_configurations': spin_configs,
                      'finite_bath_moments': bath_cases, 'formal_seed_jet_panels': jet_cases,
                      'lattice_polynomials': lattice_cases, 'cloud_variance_panels': variance_cases},
            'mathematical_fingerprint': digest,
            'analytic_arguments_machine_proved': False}


def strict_load(path):
    def pairs(items):
        out = {}
        for k,v in items:
            need(k not in out, 'duplicate JSON key')
            out[k] = v
        return out
    def bad(_):
        raise ValueError('non-integer JSON numeric literal')
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=pairs,
                      parse_float=bad, parse_constant=bad)


def authenticate():
    need({p.name for p in ROOT.iterdir()} == FILES, 'inventory differs')
    need(all((ROOT/n).is_file() and not (ROOT/n).is_symlink() for n in FILES), 'nonregular file')
    entries = {}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        h,n = line.split('  ',1)
        need(n not in entries and n in FILES-{'SHA256SUMS'} and len(h)==64, 'bad manifest')
        entries[n] = h
    need(set(entries) == FILES-{'SHA256SUMS'}, 'incomplete manifest')
    for n,h in entries.items():
        need(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h, 'hash mismatch: '+n)
    source = strict_load(ROOT/'SOURCES.json')
    need(source['parent_commit']==PARENT, 'source drift')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--emit', action='store_true', help='producer mode; no authentication')
    group.add_argument('--check', type=Path)
    args = ap.parse_args()
    if args.check:
        authenticate()
    expected = reconstruct()
    if args.check:
        actual = strict_load(args.check)
        need(json.dumps(actual, sort_keys=True, separators=(',',':')) ==
             json.dumps(expected, sort_keys=True, separators=(',',':')), 'result mismatch')
    print(json.dumps(expected, sort_keys=True, indent=2))


if __name__=='__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print('REJECT: '+str(exc), file=sys.stderr)
        sys.exit(1)
