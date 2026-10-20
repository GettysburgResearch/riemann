"""Exact finite-field replay of the positive cubic reflection.

For q=7,13,19, use Z[omega,zeta_q] with omega^2+omega+1=0 and
1+zeta_q+...+zeta_q^(q-1)=0.  These checks falsify incorrect local
orientations; the written general Gauss-sum argument remains the proof.
No floating point, optional dependencies, or removable assertions.
"""

import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


class Ring:
    def __init__(self, q):
        self.q = q
        self.width = q - 1
        self.dim = 2 * self.width

    def zero(self):
        return [0] * self.dim

    def add_term(self, out, omega_power, zeta_power, value=1):
        a = omega_power % 3
        k = zeta_power % self.q
        a_terms = ((a, 1),) if a < 2 else ((0, -1), (1, -1))
        k_terms = ((k, 1),) if k < self.width else (
            (j, -1) for j in range(self.width)
        )
        k_terms = tuple(k_terms)
        for aa, av in a_terms:
            for kk, kv in k_terms:
                out[aa * self.width + kk] += value * av * kv

    def monomial(self, a=0, k=0, value=1):
        out = self.zero()
        self.add_term(out, a, k, value)
        return out

    def shift(self, vector, a=0, k=0):
        out = self.zero()
        for index, value in enumerate(vector):
            if value:
                aa, kk = divmod(index, self.width)
                self.add_term(out, aa + a, kk + k, value)
        return out

    def add_to(self, target, vector):
        for index, value in enumerate(vector):
            target[index] += value


def primitive_root(q):
    for g in range(2, q):
        if len({pow(g, e, q) for e in range(q - 1)}) == q - 1:
            return g
    raise RuntimeError("No primitive root found")


def check_field(q):
    ring = Ring(q)
    g = primitive_root(q)
    logarithms = {pow(g, e, q): e for e in range(q - 1)}
    checks = 0
    negative_controls = 0
    for orientation in (1, 2):
        digits = {x: orientation * logarithms[x] % 3 for x in range(1, q)}
        require(digits[q - 1] == 0, "A cubic character must be trivial at -1")
        checks += 1

        fourier = []
        for d in range(q):
            value = ring.zero()
            for x in range(1, q):
                ring.add_term(value, digits[x], d * x)
            fourier.append(value)
        tau = fourier[1]
        for d in range(q):
            expected = ring.zero() if d == 0 else ring.shift(tau, -digits[d])
            require(fourier[d] == expected, f"Primitive Fourier identity q={q},d={d}")
            checks += 1

        product = ring.zero()
        for x in range(1, q):
            for y in range(1, q):
                ring.add_term(product, digits[x] - digits[y], x + y)
        require(product == ring.monomial(value=q), f"Gauss product q={q}")
        checks += 1

        # The DR local inverse substitution has d=v/a, where v is
        # a fixed unit determined by lambda and CRT conventions.
        # First Fourier transform, then Kubota chi(a), then e(ua).
        for v in range(1, q):
            for u in range(q):
                transformed = ring.zero()
                for a in range(1, q):
                    d = v * pow(a, q - 2, q) % q
                    ring.add_to(
                        transformed,
                        ring.shift(fourier[d], digits[a], u * a),
                    )
                expected = ring.zero() if u == 0 else ring.monomial(
                    -digits[v] + digits[u], value=q
                )
                require(
                    transformed == expected,
                    f"Positive cubic self-reflection q={q},v={v},u={u}",
                )
                checks += 1
                if u and digits[u]:
                    wrong_orientation = ring.monomial(
                        -digits[v] - digits[u], value=q
                    )
                    require(
                        transformed != wrong_orientation,
                        f"Wrong conjugated-output control q={q},v={v},u={u}",
                    )
                    negative_controls += 1
    return checks, negative_controls


def main():
    checks = 0
    controls = 0
    results = []
    for q in (7, 13, 19):
        passed, rejected = check_field(q)
        checks += passed
        controls += rejected
        results.append({"q": q, "checks": passed, "negativecontrols": rejected})
    print(json.dumps({
        "status": "pass",
        "scope": "Exact positive cubic finite Fourier identities; no analytic certification",
        "fieldresults": results,
        "totalchecks": checks,
        "negativecontrols": controls,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
