"""Exact finite diagnostics for the new reflection and moving-mask identities.

All arithmetic below is integer arithmetic. Cyclotomic values are represented
in Z[zeta_6,zeta_p], with zeta_6^2=zeta_6-1 and Phi_p(zeta_p)=0.
These checks cover finite local identities, not a large-sieve estimate,
analytic continuation, an infinite moment bound, or the Riemann hypothesis.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path


def require(condition, context):
    if not condition:
        raise ArithmeticError(context)


class Field:
    def __init__(self, p, root):
        self.p, self.root = p, root
        self.q = p if root is not None else p * p
        self.zero, self.one = (0, 0), (1, 0)
        self.elements = ([(a, 0) for a in range(p)] if root is not None
                         else list(itertools.product(range(p), repeat=2)))
        self.nonzero = self.elements[1:]
        if root is not None:
            require((root * root + root + 1) % p == 0, ("split root", p, root))
        units = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
        self.unit_logs = {self.reduce(u): j for j, u in enumerate(units)}
        require(len(self.unit_logs) == 6, ("distinct sixth roots", p, root))
        self.logs = {x: self.unit_logs[self.power(x, (self.q - 1) // 6)]
                     for x in self.nonzero}
        self.inverses = {x: self.power(x, self.q - 2) for x in self.nonzero}

    def reduce(self, x):
        a, b = x
        if self.root is not None:
            return ((a + self.root * b) % self.p, 0)
        return (a % self.p, b % self.p)

    def mul(self, x, y):
        a, b = x
        c, d = y
        return self.reduce((a * c - b * d, a * d + b * c - b * d))

    def power(self, x, n):
        out = self.one
        while n:
            if n & 1:
                out = self.mul(out, x)
            x = self.mul(x, x)
            n //= 2
        return out

    def neg(self, x):
        return self.reduce((-x[0], -x[1]))

    def trace(self, x):
        return x[0] if self.root is not None else (2 * x[0] - x[1]) % self.p


class Cyclotomic:
    root6 = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]

    def __init__(self, p):
        self.p = p
        self.zero = (0,) * (2 * p)
        self.one = self.term(0, 0)

    def canonical(self, a, b):
        p = self.p
        aa, bb = a[p - 1], b[p - 1]
        return tuple(v - aa for v in a) + tuple(v - bb for v in b)

    def term(self, sixth, additive):
        p = self.p
        a, b = [0] * p, [0] * p
        a[additive % p], b[additive % p] = self.root6[sixth % 6]
        return self.canonical(a, b)

    def add(self, x, y):
        return tuple(a + b for a, b in zip(x, y))

    def scale(self, x, n):
        return tuple(n * a for a in x)

    def monomial_mul(self, x, sixth, additive):
        p = self.p
        c, d = self.root6[sixth % 6]
        a, b = [0] * p, [0] * p
        for i in range(p):
            j = (i + additive) % p
            a[j] = c * x[i] - d * x[p + i]
            b[j] = d * x[i] + (c + d) * x[p + i]
        return self.canonical(a, b)

    def mul(self, x, y):
        p = self.p
        a, b = [0] * p, [0] * p
        for i in range(p):
            for j in range(p):
                z = (i + j) % p
                a[z] += x[i] * y[j] - x[p + i] * y[p + j]
                b[z] += (x[i] * y[p + j] + x[p + i] * y[j]
                         + x[p + i] * y[p + j])
        return self.canonical(a, b)

    def total(self, values):
        out = self.zero
        for value in values:
            out = self.add(out, value)
        return out


def check_field(p, root):
    f, r = Field(p, root), Cyclotomic(p)
    counts = {"gauss_product": 0, "local_reflection": 0,
              "fourier_inversion": 0, "field_multiplication": 0}
    for x in f.nonzero:
        require(f.mul(x, f.inverses[x]) == f.one, ("field inverse", p, root, x))
        for y in f.nonzero:
            require(f.logs[f.mul(x, y)] == (f.logs[x] + f.logs[y]) % 6,
                    ("character multiplicativity", p, root, x, y))
            counts["field_multiplication"] += 1
    gauss = {j: r.total(r.term(j * f.logs[x], f.trace(x))
                        for x in f.nonzero) for j in (1, 2, 3, 4)}
    require(r.mul(gauss[2], gauss[4]) == r.scale(r.one, f.q),
            ("conjugate cubic Gauss product", p, root))
    require(r.mul(gauss[3], gauss[3]) == r.scale(
        r.term(3 * f.logs[f.neg(f.one)], 0), f.q),
        ("quadratic Gauss square", p, root))
    counts["gauss_product"] += 2
    fourier = {
        (j, h): r.total(r.term(j * f.logs[y], f.trace(f.neg(f.mul(h, y))))
                       for y in f.nonzero)
        for j in (1, 4) for h in f.elements
    }  # q times the source's C_{p,j}(h).
    for j in (1, 4):
        for x in f.elements:
            lhs = r.total(r.monomial_mul(fourier[j, h], 0,
                                        f.trace(f.mul(h, x)))
                          for h in f.elements)
            rhs = r.zero if x == f.zero else r.scale(
                r.term(j * f.logs[x], 0), f.q)
            require(lhs == rhs, ("Fourier inversion", p, root, j, x))
            counts["fourier_inversion"] += 1
    epsilons = list(dict.fromkeys(
        [f.one, f.reduce((0, 1)), next(x for x in f.nonzero if f.logs[x] == 1)]))
    sigmas = list(dict.fromkeys([f.one, next(x for x in f.nonzero
                                           if f.logs[x] == 1)]))
    g13 = r.mul(gauss[1], gauss[3])
    for epsilon, sigma, j, x in itertools.product(
            epsilons, sigmas, (1, 4), f.elements):
        lhs = r.total(
            r.monomial_mul(
                fourier[j, h], -2 * f.logs[f.mul(sigma, h)],
                f.trace(f.mul(f.mul(epsilon, f.inverses[h]), x)))
            for h in f.nonzero
        )
        if j == 4:
            rhs = r.scale(r.monomial_mul(gauss[4], -2 * f.logs[sigma], 0),
                          f.q - 1 if x == f.zero else -1)
        elif x == f.zero:
            rhs = r.zero
        else:
            phase = (-2 * f.logs[sigma] + f.logs[f.neg(f.one)]
                     - 3 * f.logs[epsilon] - 3 * f.logs[x])
            rhs = r.monomial_mul(g13, phase, 0)
        require(lhs == rhs, ("Mixed local reflection", p, root, epsilon,
                             sigma, j, x))
        counts["local_reflection"] += 1
    return {"rational_prime": p, "omega_image": root, "residue_norm": f.q,
            "counts": counts}


def check_ramanujan_allocations():
    count = 0
    for q, nval, bval in itertools.product((7, 13, 19, 25), (0, 1), range(4)):
        local = -1 + q * int(nval + bval > 0)
        components = (-1, q * nval, q * int(nval == 0 and bval > 0))
        require(sum(components) == local, ("Ramanujan allocation", q, nval, bval))
        count += 1
        for allocation in range(3):  # g, e, f, respectively.
            if components[allocation] == 0:
                continue
            e, f, g = int(allocation == 1), int(allocation == 2), int(allocation == 0)
            require(nval >= e and bval >= f, ("valid allocation", nval, bval, e, f))
            nprime, bprime = nval - e, bval - f
            for row_divides, quadratic_value in itertools.product((False, True), (-1, 1)):
                lhs = 0 if row_divides else quadratic_value ** (1 + nval + bval)
                remaining = g + nprime + bprime
                rhs = (0 if row_divides and (e + f > 0 or remaining > 0)
                       else quadratic_value ** remaining)
                require(lhs == rhs, ("retained row mask", q, nval, bval,
                                     allocation, row_divides, quadratic_value))
                count += 1
    return count


def check_moving_euler():
    """Convolve the proposed forward correction with product(1-z_i)."""
    count = 0
    for k in range(2, 7):
        for masked in (False, True):
            for exponent in itertools.product(range(4), repeat=k):
                actual = 0
                for delta in itertools.product(*[(0, 1) if e else (0,)
                                                 for e in exponent]):
                    remaining = tuple(e - d for e, d in zip(exponent, delta))
                    support = sum(e > 0 for e in remaining)
                    coefficient = 1 if masked or support == 0 else 1 - support
                    actual += (-1) ** sum(delta) * coefficient
                degree = sum(exponent)
                target = 1 if degree == 0 else (-1 if degree == 1 and not masked else 0)
                require(actual == target, ("Euler correction", k, masked,
                                           exponent, actual, target))
                count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    fixtures = [(7, 2), (7, 4), (13, 3), (13, 9),
                (19, 7), (19, 11), (5, None)]
    fields = [check_field(p, root) for p, root in fixtures]
    result = {
        "status": "PASS",
        "arithmetic": "exact integers in explicitly reduced cyclotomic rings",
        "scope": "finite local identities only; no analytic or asymptotic claim",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "fields": fields,
        "ramanujan_allocation_predicates": check_ramanujan_allocations(),
        "moving_euler_coefficient_predicates": check_moving_euler(),
    }
    result["total_predicates"] = (
        sum(sum(item["counts"].values()) for item in fields)
        + result["ramanujan_allocation_predicates"]
        + result["moving_euler_coefficient_predicates"])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "total_predicates": result["total_predicates"],
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
