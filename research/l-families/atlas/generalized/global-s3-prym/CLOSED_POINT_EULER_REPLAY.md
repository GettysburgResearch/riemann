# Closed-point Euler products, independently of extension trace aggregation

Status: proposed finite source authentication extending, not rewriting,
`23ad35cc8010f72cf1df54f09eccb4dcba108879`.
Scope: every closed point of P1 of degree at most four for the six frozen
F5/F7 sources. This finite replay does not prove an all-degree Euler identity.

The first packet reconstructs Frobenius polynomials from complete point
counts in four extensions. This extension instead visits the closed places,
forms each genuine local determinant on inertia invariants, and multiplies
their inverse power series. It tests the distinction between Frobenius at a
closed point and powers of that Frobenius after extension of constants.

## Complete closed-point enumeration

For each n=1,2,3,4 construct F_(p^n) using the frozen field model. Partition
all its elements into orbits under `a -> a^p`. Keep exactly those orbits of
length n. Each retained orbit is one affine closed point of degree n, and
its minimal polynomial is the product of `(X-a)` over the orbit. The product
must have all coefficients in F_p and be a monic irreducible degree-n
polynomial. Its code identifies the closed place without choosing a
compatible embedding between different field models.

Coverage is checked in two ways: every element belongs to exactly one
Frobenius orbit, and the number of length-n orbits is

    (1/n) sum_(d|n) mu(n/d) p^d.

This formula follows from counting roots of `X^(p^n)-X`: every monic
irreducible of degree dividing n contributes exactly its degree many
distinct roots. Möbius inversion gives the displayed number. The single
point at infinity is included separately, with local determinant one for
both augmentation sheaves in this packet.

## Local factors and truncation

At a retained closed place, evaluate the cubic over its actual residue
field. Away from the discriminant, its number of rational roots determines
the permutation type: zero roots gives a three-cycle, one a transposition,
and three the identity. The rank-two standard denominators in a local
variable z are respectively

    1+z+z^2, 1-z^2, (1-z)^2.

At a simple discriminant zero the denominator is `1-z`; on the cyclic
stratum a triple-root ramified fibre has denominator one. For the Kummer
twist at a nonzero residue t, substitute `chi_(F_(p^n))(t)*z` in that local
denominator. At t=0 the twisted invariant space is zero, so its denominator
is one. This is not the same as extending a residue-field character to an
unrelated larger field: a negative sign becomes positive after an even
extension, and the closed-place calculation retains the original sign.

Substitute `z=T^n` and invert each denominator as a formal integer power
series, truncating after T^4. Every omitted closed point has degree greater
than four and hence contributes `1+O(T^5)`. Therefore the product of this
finite complete census is exactly the degree-four truncation of the full
Euler product. No approximation or analytic convergence is involved.

For comparison, read the frozen primitive point-count artifact and demand
that the standard product equal its elliptic numerator padded through
degree four, and that the twisted product equal its independent four-step
Newton Prym numerator. The Euler multiplication itself uses no extension
trace sums or Newton recurrence.

## Acceptance and remaining boundary

`closed_euler.py` authenticates its predecessor directly against the frozen
Git objects before importing its field implementation. It regenerates all
Frobenius orbits, minimal polynomials, residue-field factors, and products.
The artifact records a compact factor census and a digest of the complete
ordered closed-place records for each extension. The predecessor's field
implementation remains a dependency; independent direct polynomial divisor
checks and model changes were tested in that frozen packet.

New tests prescribe a negative Kummer branch over F7 and show that its
residue-field sign changes under a quadratic extension. They also compare
degree-two closed-place enumeration against direct monic-polynomial
enumeration, and reject omitted factors, wrong local degrees, forged
numeric types, and out-of-range coverage. These checks establish the
declared finite computation, not the global curve weight theorem.

Run from this directory:

```powershell
python -B -m unittest -v test_closed_euler.py
python -B closed_euler.py --write
python -B closed_euler.py --check
python -O -B -m unittest -v test_closed_euler.py
python -O -B closed_euler.py --check
```

The exact source, producer, tests and proof are content-bound in a separate
manifest. The first packet's seven frozen files are unchanged.
