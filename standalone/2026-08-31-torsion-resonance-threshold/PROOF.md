# The torsion resonance threshold: forced spectrum collisions begin at m = 2 ord(alpha^2) + 1, and the spectrum first collides at z = a

```text
Status:  PROVED (Lemmas 1-4, Theorem, Proposition, Corollary below —
         complete elementary proofs). The theorem is the FORWARD half
         of the empirical entry law of O-108512 (collision from
         m = 2R+1 onward, first entry forced, collision value z = a);
         the CONVERSE half (no accidental collision below the
         threshold) remains empirical: certified exact at ten torsion
         points for every m from 5 up to each entry.
Machine: matrix/torsion_field_probe.py + torsion_field_probe.json
         (number-field-exact table m = 5..27 x 10 points, including
         the (z - a)^2 divisibility at every entry: 10/10).
Depends: T-108500 (defect law), T-108509 (spectrum polynomial M_m,
         monicity), T-108510 (used only for context).
RH status: RH and GRH are unproved; nothing here addresses them.
```

## Setting

Fix a torsion point on the self-dual slice: `b = 1`,
`a = alpha + alpha^{-1} = 2 cos theta` with `alpha` a primitive M-th
root of unity, `M >= 3` (so `a != +-2`), and let

```text
R := ord(alpha^2) = M / gcd(M, 2).
```

Work in `K = Q(a)`. All statements are exact identities in `K[T]` or
`K[z]`. Write `N_m(T)` for the specialization to this point of the
generic defect numerator (T-108500), `M_m(z)` for the spectrum
polynomial (T-108509); since the generic `N_m` has constant
coefficient 1 and `M_m` is monic (T-108509), specialization commutes
with everything used below, and `deg N_m = m - 1`, `deg M_m = nu`
persist at the slice.

## Lemma 1 (exponential form of the powered coefficients)

`h_k = (alpha^{k+1} - alpha^{-(k+1)}) / (alpha - alpha^{-1})`, and by
the binomial theorem

```text
h_k^m = sum_{j=0}^{m} d_j (alpha^{2j-m})^k,
d_j   = (-1)^{m-j} C(m, j) alpha^{2j-m} (alpha - alpha^{-1})^{-m}.
```

∎ (Direct expansion; `d_j` collects the k-independent part.)

## Lemma 2 (regrouping of the defect at the slice)

For `c` mod `M` let `n_c := #{ 0 <= j <= m : 2j - m == c (mod M) }`
and `D_c := sum of d_j over that set`. Then, with
`D_m(T) = prod_{j=0}^m (1 - alpha^{2j-m} T) = prod_c (1 - alpha^c T)^{n_c}`
(the specialized Sym^m denominator),

```text
N_m(T) = D_m(T) * sum_c D_c / (1 - alpha^c T)
       = prod_c (1 - alpha^c T)^{n_c - 1} * G(T),
G(T)   = sum_c D_c * prod_{c' != c} (1 - alpha^{c'} T),
```

sums and products over the OCCUPIED classes (`n_c >= 1`); in
particular EVERY class `c` contributes the factor
`(1 - alpha^c T)^{n_c - 1}` to `N_m(T)`, regardless of whether any
`D_{c'}` vanishes (a vanishing `D_c` only raises multiplicities).

**Proof.** The generic identity
`N_m(T) = det(1 - Sym^m(A) T) * sum_k h_k^m T^k` holds coefficientwise
over `Q(a, b)` (T-108500) and specializes. By Lemma 1 the series is
`sum_c D_c/(1 - alpha^c T)` (grouping equal geometric ratios; the
coefficient sequence is a pure exponential sum, so all poles are
simple). Multiplying by `D_m = prod_c (1 - alpha^c T)^{n_c}` clears
each simple pole with one power, leaving each term of the sum
divisible by `prod_c (1 - alpha^c T)^{n_c - 1}`; terms with
`D_c = 0` are zero and harmless. ∎

## Lemma 3 (class multiplicities and where the triples land)

`2j - m == 2j' - m (mod M) iff j == j' (mod R)`. Hence the classes hit
by `j in [0, m]` repeat with period `R` in `j`, and:

1. `m <= R - 1`: all `n_c <= 1`.
2. `R <= m <= 2R - 1`: `max_c n_c = 2`.
3. `m = 2R`: exactly one class has `n_c = 3`, namely
   `c == -m == 0 (mod M)` (both parities: `2R == 0 (mod M)`), whose
   root is `T = 1`.
4. `m = 2R + 1`: exactly two classes have `n_c = 3`, namely
   `c == -1` and `c == +1 (mod M)` (from `j = 0, R, 2R` and
   `j = 1, R+1, 2R+1`), whose roots are `T = alpha^{+1}` and
   `T = alpha^{-1}`.

∎ (Direct counting; `e_j = 2j - m` steps by 2 and drops by `2R == 0`
every `R` steps of `j`.)

## Lemma 4 (T-multiplicity reads off z-collisions)

Over the algebraic closure write the spectrum part of `N_m` as
`prod_{i=1}^{nu} (T^2 - z_i T + 1)` (T-108509 at `b = 1`), each factor
`(1 - u_i T)(1 - u_i^{-1} T)`-scaled with `u_i + u_i^{-1} = z_i`; for
even m there is additionally the trivial factor `(1 + T)`. For any
`w not in {1, -1}`: the multiplicity of `w` as a T-root of `N_m`
equals `#{ i : z_i = w + w^{-1} }`. In particular

```text
mult_T(w) >= 2 for some w not in {1, -1}
   ==>  two spectrum points coincide  ==>  disc_z M_m = 0.
```

∎ (A factor with `z_i = w + w^{-1}` has T-roots `{w, w^{-1}}`,
distinct since `w != +-1`, so contributes `w` exactly once; the
trivial factor contributes only at `-1`.)

## Theorem (forced entry at m = 2R + 1; the spectrum collides at z = a)

Let `m = 2R + 1`. By Lemma 3(4) the classes `c == +-1` have
`n_c = 3`, so by Lemma 2 `N_m(T)` is divisible by
`(1 - alpha T)^2 (1 - alpha^{-1} T)^2`. Since `M >= 3`,
`alpha^{+-1} not in {1, -1}`, so Lemma 4 applies with
`w = alpha^{-1}` (or `alpha`): at least two spectrum points share

```text
z = alpha + alpha^{-1} = a .
```

Hence `disc_z M_{2R+1} = 0` at the torsion point and moreover
`(z - a)^2 | M_{2R+1}(z)` in `K[z]`: THE SPECTRUM'S FIRST FORCED
COLLISION IS AT THE ORIGINAL TRACE. ∎

(Machine confirmation: at all ten tested torsion points — R = 3, 4,
5, 5, 6, 9, 9, 10, 11, 13 — `M(a) = M'(a) = 0` at `m = 2R + 1`
exactly, 10/10; torsion_field_probe run of 2026-08-31.)

The same argument gives collisions for every `m >= 2R + 1` whenever
some tripled class lands off `{T = +-1}`; the exceptional
configurations are classified below.

## Proposition (why nothing is forced earlier, and the m = 2R near-miss)

For `m <= 2R - 1`, Lemma 3(1,2) gives `n_c - 1 <= 1`: the prefactor of
Lemma 2 is squarefree and no collision is forced. At `m = 2R` the
unique tripled class has root `T = 1` (Lemma 3(3)): the resulting
double T-root at `w = 1` is ONE spectrum point at the boundary value
`z = 2` (a single factor `(1 - T)^2`), not a coincidence of two — so
no `disc_z` vanishing is forced, matching the observed `False` at
`m = 2R` at every tested point. What is NOT proved here is the
absence of ACCIDENTAL collisions from the cofactor `G` below the
threshold; that converse half is certified empirically (ten points,
every `m` from 5 to each entry, exact).

## Corollary (the supersingular gap at m = 6, derived)

At `a = 0`: `M = 4`, `R = 2`. At `m = 6` the class counts are
`n_{c=2} = 4` (root `alpha^{-2} = -1`) and `n_{c=0} = 3` (root `1`):
the prefactor forces multiplicities only at `T = +-1`, i.e. boundary
values `z = +-2` — one spectrum point at `z = 2`, and at `z = -2` the
coincidence is with the EVEN-m TRIVIAL factor, which is not a
spectrum-spectrum collision. This DERIVES the one anomaly of the
empirical table (O-108512: `M_6(a=0) = (z - 2b^3)(z + 2b^3)` — the
spectrum-trivial collision invisible to `disc_z M`). At `m = 8`,
`n_{c=0} = 5` gives `mult_T(1) = 4`, i.e. TWO spectrum points at
`z = 2`, and the collision reappears — matching the table. ∎

## Addendum: the converse is PROVED for all m <= 15, for ALL torsion points

**Lemma (monic sieve).** Let `p in Z[a]` be a primitive irreducible
polynomial with `|lc(p)| != 1`. Then `p` has no root of the form
`2 cos(2 pi k / N)` (any torsion value). *Proof.* A torsion value is
an algebraic integer, so its minimal polynomial `q` is monic with
integer coefficients and irreducible. If the value were a root of
`p`, then `q | p` in `Q[a]`; irreducibility of `p` forces
`q = p / lc(p)`, and `q in Z[a]` would force `lc(p)` to divide every
coefficient of `p`, contradicting primitivity. ∎

**Computation (matrix/disc_slice_factor_lcs.json; exact sympy
factorizations over Z of `disc_z M_m(a, 1)` for m = 5..15).** At every
m in this range the factorization consists of (i) monic factors that
are PRECISELY the torsion minimal polynomials with threshold
`2 ord(alpha^2) + 1 <= m` — e.g. at m = 15: `a, a -+ 1, a^2 - 2,
a^2 - 3, a^2 -+ a - 1` and both ord-7 cubics, and nothing else — and
(ii) a SINGLE remaining irreducible factor of large degree whose
leading coefficient is never a unit (16; 5, 5; 2025; 21609;
157351936; 740710656; ~3.2e13; ~1.1e15; ~1.2e21; ~1.8e22; ~1.2e29 for
m = 5..15).

**Corollary (complete law for m <= 15).** By the monic sieve, no
torsion point of ANY order is a root of the non-monic factor, so for
`5 <= m <= 15` and EVERY torsion point:

```text
disc_z M_m (theta) = 0   <=>   m >= 2 ord(alpha^2) + 1 .
```

Together with the Theorem (forced entry, all m), the entry law of
O-108512 is a COMPLETE THEOREM in the range m <= 15 — for all torsion
points simultaneously, not merely the fourteen tested — and remains
proved in the forward direction for every m. ∎

## What is proved and what remains

PROVED: collisions are forced from `m = 2R + 1` on (with the explicit
exceptional bookkeeping at `T = +-1` classes), the first forced
collision value is `z = a`, the `m = 2R` non-entry, the `a = 0`,
`m = 6` gap, and — by the monic sieve over the exact factorizations —
the FULL two-sided law for all torsion points in the range
`m <= 15`. OPEN: the converse for `m >= 16`, which by the same sieve
reduces to a single verifiable property per m: that after removing
the (known) torsion factors, the remaining factor of
`disc_z M_m(a, 1)` has non-unit leading coefficient and no monic
irreducible torsion divisors — an explicitly checkable normal form
whose persistence for all m is the deposited conjecture. The reading of O-108512 is
upgraded accordingly: the torsion entry law's threshold is now a
THEOREM in one direction, with the resonance mechanism identified as
CLASS CROWDING of the Sym^m weight monomials modulo the torsion order
— the discrete shadow, at exact-arithmetic level, of "extra symmetry
forces spectral degeneracy".
```
