"""Count distinct small-conductor cyclotomic fields with a certified low zero."""
from hashlib import sha256
from math import gcd

from flint import arb, ctx, dirichlet_char


def witness(modulus):
    for label in range(2, modulus):
        if gcd(modulus, label) != 1:
            continue
        character = dirichlet_char(modulus, label)
        if not character.is_primitive():
            continue
        left = character.hardy_z(arb(0)).real
        right = character.hardy_z(arb(1) / 2).real
        if left * right < 0:
            return label
    return None


def main():
    ctx.prec = 70
    conductor_cap = 400_000
    covered = bytearray(conductor_cap + 1)
    evidence = []
    for modulus in range(3, 1001):
        if modulus % 4 == 2 or covered[modulus]:
            continue
        label = witness(modulus)
        if label is None:
            continue
        evidence.append(f"{modulus} {label}\n")
        covered[modulus::modulus] = bytes([1]) * (conductor_cap // modulus)

    count = sum(covered[q] for q in range(1, conductor_cap + 1) if q % 4 != 2)
    print(f"{len(evidence)} witness conductors, {count} distinct cyclotomic fields")
    print(sha256("".join(evidence).encode()).hexdigest())


if __name__ == "__main__":
    main()
