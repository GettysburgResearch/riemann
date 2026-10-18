"""Independent finite spin enumeration for the one-cross-edge moment map."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from decimal import Decimal as D, localcontext
import hashlib
import json
import sys
import time

import cyclic_model as model


def enumeration(zq, counts, eta, degree, types, vertices):
    zero, one = zq[0]*0, zq[0]*0+1
    components, weights, edges, k = [], [], [], 0
    for i, count in enumerate(counts):
        A, B, p = zq[3*i:3*i+3]
        for copy in range(count):
            root = k
            if i == 0:
                weights.append(A)
                components.append((i, root, None))
                k += 1
            else:
                weights.extend([(A+B)/2, (A-B)/2])
                edges.append((k, k+1, 2*p-one))
                components.append((i, k, k+1))
                k += 2
    chosen = []
    for kind, vertex in zip(types, vertices):
        row = next(row for row in components if row[0] == kind and row not in chosen)
        chosen.append(row)
    v0 = chosen[0][1 if vertices[0] == 'root' else 2]
    v1 = chosen[1][1 if vertices[1] == 'root' else 2]
    raw, norm = [zero]*(degree+1), zero
    for spins in product((-1, 1), repeat=k):
        mass = one
        for _, root, _ in components:
            mass *= (one+eta*spins[root])/2
        for a, b, correlation in edges:
            mass *= (one+correlation*spins[a]*spins[b])/2
        mass *= one+zq[-1]*spins[v0]*spins[v1]
        total = sum((w*s for w, s in zip(weights, spins)), zero)
        norm += mass
        for n in range(degree+1):
            raw[n] += mass*(one if n == 0 else total**n)
    return [x/norm if n % 2 == 0 else zero for n, x in enumerate(raw)]


def main():
    began = time.monotonic()
    degree, counts, eta = 10, [1, 2, 1], F(1, 7)
    z = [F(1, 5), F(0), F(1), F(3, 5), F(-1, 4), F(4, 5),
         F(1, 2), F(1, 6), F(2, 3), F(2, 7)]
    fixtures, checks = [], 0
    for types, vertices in [((0, 1), ('root', 'root')),
                            ((1, 2), ('child', 'root')),
                            ((1, 1), ('root', 'child'))]:
        active = [0, 3, 4, 5, len(z)-1]
        _, J, raw = model.jet(z, counts, eta, degree, active, types, vertices)
        zz = [model.Dual(x, [F(j == k) for k in active]) for j, x in enumerate(z)]
        direct = enumeration(zz, counts, eta, degree, types, vertices)
        kap, unit = model.cumulants(direct), model.unit_cumulants(degree)
        for n, (a, b) in enumerate(zip(raw, direct)):
            assert a == b.v, ('raw', types, vertices, n)
            checks += 1
        for r, row in enumerate(J, 1):
            for a, b in zip(row, kap[2*r].d):
                assert a == b/unit[2*r], ('derivative', types, vertices, r)
                checks += 1
        fixtures.append({'types': types, 'vertices': vertices, 'spins': 7,
                         'configurations': 128, 'degree': degree})
    packet = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(packet/'theta'))
    import model as frozen_tree
    with localcontext() as ctx:
        ctx.prec = 100
        p = json.loads((packet/'theta/parameters22.json').read_text())
        def dec(s):
            q = F(s)
            return D(q.numerator)/D(q.denominator)
        zz = list(map(dec, p['centers']))
        values, raw = model.evaluate(zz+[D(0)], p['counts'], dec(p['hub_correlation']),
                                     24, (3, 6))
        old, old_raw = frozen_tree.evaluate(zz, p['counts'], dec(p['hub_correlation']), 24)
        assert max(abs(a-b) for a, b in zip(raw, old_raw)) < D('1e-75')
        assert max(abs(a-b) for a, b in zip(values, old)) < D('1e-75')
        checks += 2
    receipt = {'status': 'PASS_EXACT_FINITE_CONTROLS', 'checks': checks,
               'fixtures': fixtures, 'complete_tree_boundary_degree': 24,
               'model_sha256': hashlib.sha256(Path(model.__file__).read_bytes()).hexdigest(),
               'elapsed_seconds': time.monotonic()-began,
               'moment_matching_existence_proved': False}
    Path(__file__).with_name('CYCLIC_MODEL_CONTROLS.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt), flush=True)


if __name__ == '__main__':
    main()
