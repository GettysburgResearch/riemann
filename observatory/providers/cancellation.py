"""Full finite signed-source comparisons, spectral witnesses, and held-out sweeps.

Nothing here estimates an infinite operator or accepts an RH certificate.
Every displayed difference is derived from the two complete finite matrices.
"""
from __future__ import annotations
import hashlib
import math
import random
import numpy as np
from .contracts import CancellationSpec

SOURCE_NOTES = {
    'mobius': 'Literal integer Möbius values μ(n).',
    'magnitude': '|μ(n)|: same squarefree support and magnitudes, all nonnegative.',
    'random_signs': 'Synthetic deterministic hash-derived signs on |μ(n)| support; SHA-256(seed,n), first-byte parity.',
    'shuffled': 'Synthetic seeded Fisher–Yates permutation of μ on this finite window; multiset preserved, arithmetic positions changed.',
    'liouville': 'Literal λ(n)=(-1)^Ω(n), including nonsquarefree integers; support differs from μ.',
    'alternating': 'Synthetic (-1)^n on |μ(n)| support.',
}

def digest(obj):
    from identity import content_id
    return content_id(obj)

def source(name, start, n, seed):
    from engine import sieve
    _, mu = sieve(start+n-1)
    values = mu[start:start+n]
    if name == 'magnitude':
        values = [abs(v) for v in values]
    elif name == 'random_signs':
        values = [abs(v) * (1 if hashlib.sha256(f'{seed}:{i}'.encode()).digest()[0] & 1 else -1)
                  for i, v in zip(range(start, start+n), values)]
    elif name == 'shuffled':
        values = list(values)
        # Explicit algorithm; Random's integer generator is recorded by Python version.
        rng = random.Random(seed)
        for i in range(n-1, 0, -1):
            j = rng.randrange(i+1)
            values[i], values[j] = values[j], values[i]
    elif name == 'alternating':
        values = [abs(v) * (-1 if i % 2 else 1) for i, v in zip(range(start, start+n), values)]
    elif name == 'liouville':
        primes, _ = sieve(start+n-1)
        values = []
        for i in range(start, start+n):
            r, sign = i, 1
            for p in primes:
                if p*p > r:
                    break
                while r % p == 0:
                    r //= p
                    sign = -sign
            if r > 1:
                sign = -sign
            values.append(sign)
    elif name != 'mobius':
        raise ValueError('Unknown arithmetic source')
    return np.array(values, dtype=np.int64)

def kernel(start, n, width):
    indices = np.arange(start, start+n, dtype=np.int64)
    logs = np.log(indices.astype(float))
    return indices, logs, np.exp(-0.5 * ((logs[:, None]-logs[None, :])/width)**2)

def decomposition(matrix, split):
    total = math.fsum(matrix.ravel().tolist())
    aa = math.fsum(matrix[:split, :split].ravel().tolist())
    bb = math.fsum(matrix[split:, split:].ravel().tolist())
    cross = 2*math.fsum(matrix[:split, split:].ravel().tolist())
    diagonal = math.fsum(np.diag(matrix).tolist())
    return {'A': aa, 'B': bb, 'cross': cross, 'total': total,
            'diagonal': diagonal, 'off_diagonal': total-diagonal,
            'identity_residual': total-math.fsum([aa, bb, cross])}

def experiment(q, side, K, indices):
    name, seed = getattr(q, 'source_'+side), getattr(q, 'seed_'+side)
    coefficients = source(name, q.start, q.n, seed)
    weights = coefficients / indices.astype(float)**q.exponent
    matrix = weights[:, None]*K*weights[None, :]
    rows = [math.fsum(row.tolist()) for row in matrix]
    # Prefix energies include both orientations of each newly added off-diagonal term.
    increments = [matrix[i, i]+2*math.fsum(matrix[i, :i].tolist()) for i in range(q.n)]
    prefix = [math.fsum(increments[:i+1]) for i in range(q.n)]
    data = {'request': {'source': name, 'seed': seed, 'start': q.start, 'n': q.n,
                        'split': q.split, 'width': q.width, 'exponent': q.exponent},
            'definition': SOURCE_NOTES[name], 'coefficients': coefficients.tolist(),
            'weights': weights.tolist(), 'matrix': matrix.ravel().tolist(),
            'rows': rows, 'prefix_energy': prefix, 'energy': decomposition(matrix, q.split)}
    data['experiment_id'] = digest(data)
    return data

def cancellation(q, ctx=None, spectral=True):
    from engine import series
    indices, logs, K = kernel(q.start, q.n, q.width)
    A, B = experiment(q, 'a', K, indices), experiment(q, 'b', K, indices)
    difference = np.array(B['matrix']).reshape(q.n, q.n)-np.array(A['matrix']).reshape(q.n, q.n)
    result = {
        'experiments': {'a': A, 'b': B}, 'indices': indices.tolist(),
        'grid': {'kind': 'interaction', 'n': q.n, 'x': indices.tolist(), 'y': indices.tolist(),
                 'values': difference.ravel().tolist()},
        'series': [series(label, indices.tolist(), values, q.n) for label, values in [
            ('A: full-prefix energy', A['prefix_energy']), ('B: full-prefix energy', B['prefix_energy']),
            ('A: signed row contribution', A['rows']), ('B: signed row contribution', B['rows']),
            ('B − A: row discrepancy', (np.array(B['rows'])-A['rows']).tolist())]],
        'metrics': {'A_energy': A['energy']['total'], 'B_energy': B['energy']['total'],
                    'B_minus_A': B['energy']['total']-A['energy']['total'],
                    'split_after_integer': int(indices[q.split-1]),
                    'difference_trace_sum': math.fsum(difference.ravel().tolist())},
        'events': [],
        'formula': 'a_n=c_n/n^α; K_mn=exp(-(log m−log n)²/(2h²)); Q=aᵀKa=Q_A+Q_B+2C_AB. Difference is control B minus source A, term by term.',
        'warnings': [f'Complete finite window {q.start}..{q.start+q.n-1}; both blocks and all cross terms retained. No infinite-prefix or RH conclusion.',
                     'Kernel, eigensystem and energies are binary64 numerical scouts. Magnitude control changes signs, not the kernel.',
                     'The Gaussian kernel is positive semidefinite by construction; finite positive energy is not evidence for a special arithmetic positivity mechanism.']}
    if spectral:
        eigenvalues, vectors = np.linalg.eigh(K)
        # Fix sign for replay; clustered eigenvalues still permit arbitrary rotations.
        for j in range(q.n):
            if vectors[np.argmax(np.abs(vectors[:, j])), j] < 0:
                vectors[:, j] *= -1
        projections_a, projections_b = vectors.T @ A['weights'], vectors.T @ B['weights']
        eigen_residual = float(np.linalg.norm(K@vectors-vectors*eigenvalues, ord='fro'))
        threshold = np.finfo(float).eps*q.n*max(float(abs(eigenvalues[-1])), 1)
        reliable = eigenvalues[eigenvalues > threshold]
        result['spectrum'] = {'eigenvalues': eigenvalues.tolist(), 'vectors': vectors.T.tolist(),
                              'projection_a': projections_a.tolist(), 'projection_b': projections_b.tolist(),
                              'mode_energy_a': (eigenvalues*projections_a**2).tolist(),
                              'mode_energy_b': (eigenvalues*projections_b**2).tolist(),
                              'residual_frobenius': eigen_residual,
                              'numerical_rank_threshold': threshold,
                              'numerical_rank': int(len(reliable)),
                              'resolved_condition_ratio': float(reliable[-1]/reliable[0]) if len(reliable) else None,
                              'note': 'Vectors are columns of an orthonormal eigensystem, serialized by mode. Tiny/clustered modes are numerically unstable. No negative eigenvalue is clipped.'}
        result['metrics']['spectral_energy_residual_A'] = float(np.sum(eigenvalues*projections_a**2)-A['energy']['total'])
        # The selected mode is a kernel section f(u)=Σv_n K(u,log n), not an RH detector.
        result['kernel'] = {'logs': logs.tolist(), 'width': q.width}
    return result

def sweep(q, ctx=None):
    from engine import series
    widths = np.geomspace(q.width_min, q.width_max, q.width_steps).tolist()
    splits = sorted(set(np.round(np.linspace(1, q.n-1, q.split_steps)).astype(int).tolist()))
    trials = []
    for width in widths:
        # No holdout input is accessed during selection.
        p = CancellationSpec(n=q.n, start=q.train_start, split=splits[0], width=width,
                             exponent=q.exponent, source_a=q.source_a, source_b=q.source_b,
                             seed_a=q.seed_a, seed_b=q.seed_b)
        indices, _, K = kernel(p.start, p.n, width)
        A, B = experiment(p, 'a', K, indices), experiment(p, 'b', K, indices)
        ma, mb = np.array(A['matrix']).reshape(q.n, q.n), np.array(B['matrix']).reshape(q.n, q.n)
        denom = A['energy']['diagonal']+B['energy']['diagonal']
        for split in splits:
            ca, cb = decomposition(ma, split)['cross'], decomposition(mb, split)['cross']
            score = abs(cb-ca)/denom if denom else 0.0
            trials.append({'width': width, 'split': split, 'cross_a': ca, 'cross_b': cb,
                           'signed_difference': cb-ca, 'score': score, 'normalizer': denom})
    winner_index = max(range(len(trials)), key=lambda i: trials[i]['score'])
    winner = trials[winner_index]
    detector = {'version': 1, 'metric': '|cross_B-cross_A|/(diagonal_A+diagonal_B); zero if denominator is zero',
                'train_start': q.train_start, 'n': q.n, 'exponent': q.exponent,
                'width': winner['width'], 'split': winner['split'],
                'source_a': q.source_a, 'source_b': q.source_b, 'seed_a': q.seed_a, 'seed_b': q.seed_b}
    detector['detector_id'] = digest(detector)
    p = CancellationSpec(n=q.n, start=q.holdout_start, split=winner['split'], width=winner['width'],
                         exponent=q.exponent, source_a=q.source_a, source_b=q.source_b,
                         seed_a=q.seed_a, seed_b=q.seed_b)
    held = cancellation(p, spectral=False)
    ae, be = held['experiments']['a']['energy'], held['experiments']['b']['energy']
    denom = ae['diagonal']+be['diagonal']
    held_score = abs(be['cross']-ae['cross'])/denom if denom else 0.0
    return {'series': [series('Best training score at each width', widths,
                    [max(t['score'] for t in trials if t['width']==w) for w in widths], len(widths))],
            'events': [], 'trials': trials, 'widths': widths, 'splits': splits,
            'winner_index': winner_index, 'detector': detector,
            'holdout': {'request': p.model_dump(), 'score': held_score, 'signed_difference': be['cross']-ae['cross'],
                        'experiments': held['experiments'], 'grid': held['grid']},
            'metrics': {'training_trials': len(trials), 'training_best_score': winner['score'],
                        'frozen_holdout_score': held_score, 'holdout_evaluations': 1},
            'formula': detector['metric'],
            'warnings': ['Selection uses the declared training window only. The winning width and split are frozen before ONE evaluation on the disjoint held-out window.',
                         'This is exploratory effect size, not a p-value or statistical significance claim. Repeated human retuning can consume the holdout.',
                         'A click on another training trial creates a new investigation; it does not inherit the frozen winner’s held-out result. All training trials, including failures, are exported.']}
