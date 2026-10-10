# Directed critical-pair existence certificates

Status: **PROPOSED directed interval certificate; independent review requested.**

Scope: sixteen disjoint low critical-line intervals, used as anchors by the
compact Pick theorem in `../heights/PROOF.md`. This is an existence certificate,
with no assertion that the zeros are simple or constitute a complete census.

Exact dependency: `python-flint==0.9.0`, which wraps Arb/FLINT ball arithmetic.
The mathematical inference uses the classical zeta functional equation.

For real t define

\[
\theta(t)=\operatorname{Im}\log\Gamma(1/4+it/2)-(t/2)\log\pi,
\qquad Z(t)=e^{i\theta(t)}\zeta(1/2+it).
\]

The log-Gamma branch is analytic on the right half-plane and real on the
positive real axis. The functional equation makes Z real and continuous
on the real axis. The script starts from exact integers and half-integers,
and computes enclosing complex balls for log-Gamma, pi, exp,
and zeta. Each real enclosure excludes zero with the reported sign. The
imaginary enclosure containing zero is a consistency check; reality itself
comes from the functional equation, not from a numerical smallness test.

Opposite signs at 14/15, 21/22, 25/26, 30/31, 32/33, 37/38, 40/41, 43/44,
48/49, 49.5/50, 52/53, 56/57, 59/60, 60.5/61, 65/66, and 67/68 prove at
least one zero in each respective open interval by the intermediate value
theorem. Therefore sixteen distinct critical pairs exist. The first nine
have squared ordinates in `[196,225]`, `[441,484]`, `[625,676]`, `[900,961]`,
`[1024,1089]`, `[1369,1444]`, `[1600,1681]`, `[1849,1936]`, `[2304,2401]`.
All sixteen exact squared intervals are emitted in the receipt. Half-integer
endpoints start from `Fraction` and are stored as rational strings in JSON;
binary floating-point inputs are never used.

The same script also certifies `xi(1/2)>1/4` from the exact expression
`s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/2` at `s=1/2`. This supplies the
nonzero central value used in the independent Jensen zero-count estimate;
it makes no claim about any other central-point normalization.

What ran:

```sh
python certify_hardy_z.py --output hardy_z_certificate.json
python -O certify_hardy_z.py --precision 128
```

Both checks use explicit exceptions, so Python optimization cannot remove
the sign contracts. The saved receipt is at 256-bit precision. Independent
replay should run the code rather than trusting rounded text in the receipt.

Smallest remaining gap: these anchors supply only the finite positive Gram
part of the compact-domain theorem; all-height source and tail assumptions
must still be bound to their exact imported theorems.
