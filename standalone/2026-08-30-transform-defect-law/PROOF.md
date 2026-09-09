# T-108500 — Exact defect law for pointwise transforms of degree-2 local data

```text
Status:  PROVED for the parts marked Theorem/Lemma below (complete proofs);
         VERIFIED EXACT (machine, m <= 6 symbolic, plus 12 integer
         instantiations per m) for the tabulated defects; CONJECTURED
         where marked
Scope:   local/exact for the generic degree-2 local object over Q(a,b);
         global statements are formal Euler-product identities valid in the
         stated half-planes of absolute convergence, with bad primes
         excluded as stated; nothing global beyond that is claimed
Exact sources or dependencies: core/{exact,symbolic_defect}.py of the pass
         (sympy 1.14.0 for the symbolic layer; all instantiation checks
         stdlib-exact); classical inputs cited inline
What was actually run: matrix/defect_powers_run.py (symbolic + 12 exact
         integer instantiations per transform); replay:
         experiments/X-108500-transform-defects/
Smallest remaining gap: closed form of the FULL defect coefficient list for
         general m (the r=0,1,m-1 coefficients are proved/conjectured as
         stated; middle coefficients are given by the proved u-sum formula
         but not further closed)
RH status: RH and GRH are unproved; this document does not address them.
```

Programme context: issue #764, axes A/B (coefficient and local-parameter
transforms), research mode 1 (transformation and survival atlas), theorem
targets "determine exact defect factors separating scalar transforms from
functorial operations". Novelty position: the m=2 case is the classical
local Rankin-Selberg identity (Shimura-era; imported as known and used as a
correctness oracle); the Cauchy/Hadamard and Jacobi-Trudi identities are
classical symmetric-function theory. Believed new here, subject to the
boundary audit: the uniform *defect law* packaging (exact denominator
minimality for all m, the `a^m - h_m` linear-coefficient law, the
SELF-DUALITY functional equation of the defect, the character-ring EXIT
theorem for m = 3, and the degeneration statement on the supersingular
locus), as survival statements for the #764 ladder. Audit verdict on this
claim family: PARTIAL_OVERLAP — defect extraction per se is classical
(Shimura; Moreno-Shahidi on symmetric-power L-functions; plethysm) and
global survival of Euler products is governed by Estermann/Dahlquist/
Kurokawa theory (see the corrected trichotomy section at the end); the
exact defect tables, the self-duality law, and the m=3 exit statement are
the parts believed new.

## Setting

Generic degree-2 local object: Satake polynomial `D(T) = 1 - aT + bT^2`
over `K = Q(a, b)`, inverse roots `alpha, beta` (so `alpha + beta = a`,
`alpha beta = b`), coefficients `h_k` of `1/D` (complete homogeneous
symmetric functions; `h_k = a h_{k-1} - b h_{k-2}`). For an integer
`m >= 1` write `Sym^m` for the m-th symmetric power of the underlying rank-2
object; `det(1 - Sym^m(A) T) = prod_{j=0}^{m} (1 - w_j T)` with weight
monomials `w_j = alpha^{m-j} beta^j`.

## Theorem 1 (pointwise-power defect law)

For every `m >= 1`, in `K[[T]]`:

```text
sum_{k>=0} h_k^m T^k  =  N_m(T) / det(1 - Sym^m(A) T)
```

where `N_m ∈ Z[a,b][T]` satisfies:

1. `N_m(0) = 1` and `deg_T N_m <= m - 1`;
2. the denominator is EXACT for generic `(a,b)`: `gcd(N_m, det(1 - Sym^m T))
   = 1` away from a proper closed degeneration locus (see Theorem 3);
3. the coefficient of `T^r` in `N_m` equals

   ```text
   c_r  =  sum_{u=0}^{r} (-1)^{r-u} e_{r-u}(Sym^m(A)) h_u^m ,
   ```

   where `e_i(Sym^m(A))` is the i-th elementary symmetric function of the
   weights `w_0..w_m`; in particular `c_0 = 1` and

   ```text
   c_1 = a^m - h_m           (the linear-coefficient law).
   ```

4. **(self-duality of the defect)** for every `m >= 2`,

   ```text
   N_m(T)  =  b^{m(m-1)/2} T^{m-1} N_m( 1 / (b^m T) ) ,
   ```

   equivalently `c_{m-1-r} = b^{m(m-1)/2 - mr} c_r` for
   `0 <= r <= (m-1)/2`. In particular `c_{m-1} = b^{m(m-1)/2}` (take
   `r = 0`). The obstruction to functoriality is itself SELF-DUAL: the
   defect numerator satisfies an exact functional equation of the same
   reflection type as the local data it obstructs.

Machine-verified table (exact symbolic + 12 exact integer instantiations
each; `matrix/defects.json`):

```text
m=2:  N_2 = 1 + b T                                      over det(1 - Sym^2 T)
m=3:  N_3 = 1 + 2ab T + b^3 T^2                          over det(1 - Sym^3 T)
m=4:  N_4 = 1 + b(3a^2-b) T + b^3(3a^2-b) T^2 + b^6 T^3  over det(1 - Sym^4 T)
m=5:  N_5 = 1 + ab(4a^2-3b) T + 2b^3(a^2-b)(3a^2-b) T^2
          + ab^6(4a^2-3b) T^3 + b^10 T^4                 over det(1 - Sym^5 T)
m=6:  see matrix/defects.json (degree 5; same palindrome)
```

Recurring structure worth recording: the factor `a^2 - b = trace(Sym^2 A)`
appears in the higher defects (`c_2` of `N_5`; `c_1, c_4` of `N_6`) — the
same quantity whose non-squareness proves Theorem 2 and whose SIGN decides
the purity stratification of O-108506. All rows are constructed from the
proved coefficient formula, re-verified by symbolic series multiplication,
and cross-checked at 12 exact integer instantiations each
(`matrix/defect_powers_run.py`, `matrix/defects.json`).

### Proof

Write `h_k = (alpha^{k+1} - beta^{k+1}) / (alpha - beta)` (generic
`alpha != beta`). By the binomial theorem,

```text
h_k^m = (alpha-beta)^{-m} sum_{j=0}^m (-1)^j C(m,j) w_j^{k+1},
```

since `alpha^{(m-j)(k+1)} beta^{j(k+1)} = w_j^{k+1}`. Summing the geometric
series `sum_k w_j^{k+1} T^k = w_j / (1 - w_j T)`:

```text
sum_k h_k^m T^k = (alpha-beta)^{-m} sum_j (-1)^j C(m,j) w_j / (1 - w_j T),
```

a rational function with denominator dividing `prod_j (1 - w_j T)
= det(1 - Sym^m(A) T)`. Its numerator over that common denominator is

```text
N_m(T) = (alpha-beta)^{-m} sum_j (-1)^j C(m,j) w_j prod_{i != j} (1 - w_i T).      (*)
```

`N_m(0) = (alpha-beta)^{-m} sum_j (-1)^j C(m,j) w_j = (alpha-beta)^{-m}
(alpha-beta)^m = 1` (the inner sum is the binomial expansion of
`(alpha - beta)^m` in the variables `alpha, beta`). The coefficient of
`T^{m}` in (*) is `(-1)^m (alpha-beta)^{-m} (prod_i w_i) sum_j (-1)^j C(m,j)
= 0` because `sum_j (-1)^j C(m,j) = 0` for `m >= 1`; this kills the top
degree, giving `deg <= m-1`. For the coefficient formula: apply the
standard expansion `e_r(w minus w_j) = sum_{u=0}^r (-1)^u w_j^u e_{r-u}(w)`
inside `[T^r] prod_{i != j}(1 - w_i T) = (-1)^r e_r(w minus w_j)`, exchange
sums, and use

```text
sum_j (-1)^j C(m,j) w_j^{u+1} = (alpha^{u+1} - beta^{u+1})^m
                              = (alpha-beta)^m h_u^m ,
```

which yields `c_r = (-1)^r sum_u (-1)^u e_{r-u}(w) h_u^m` — statement 3
after the sign bookkeeping `(-1)^r(-1)^u = (-1)^{r-u}`. For `r = 1`:

```text
c_1 = (-1)^1 e_1(w) h_0^m + (-1)^0 e_0(w) h_1^m = h_1^m - e_1(w) = a^m - h_m ,
```

since `e_1(w) = sum_j alpha^{m-j} beta^j = h_m` and `h_1 = a`.
Exactness of the denominator: from the second display, the
partial-fraction coefficient of `w_j/(1 - w_j T)` is
`(-1)^j C(m,j) (alpha-beta)^{-m}`, a visibly nonzero element of `K`; a
common factor `(1 - w_j T)` of `N_m` and the denominator would force that
coefficient to vanish. Since all `w_j` are distinct generically, the
reduced denominator is the full product. Membership `N_m ∈ Z[a,b][T]`:
each `c_r` is a symmetric polynomial in `(alpha, beta)` with integer
coefficients (statement 3 exhibits it as such), hence a polynomial in
`(a, b)` over `Z` by the fundamental theorem of symmetric functions.

**Statement 4 (self-duality).** Step 1: reduce to `b = 1`. Each `c_r` is
weighted-homogeneous of degree `mr` for the weights `(1, 2)` on `(a, b)`
(it is homogeneous of degree `mr` in `(alpha, beta)` by statement 3, and
`a, b` have alpha-beta-degrees `1, 2`). Fix `0 <= r <= (m-1)/2` and set
`E(a, b) := c_{m-1-r}(a,b) - b^{m(m-1)/2 - mr} c_r(a,b)`; both terms are
weighted-homogeneous of the same degree `N = m(m-1-r)`. Weighted
homogeneity gives `E(a, b) = b^{N/2} E(a b^{-1/2}, 1)` in `Q(a, b^{1/2})`,
so `E(x, 1) ≡ 0` (all `x`) implies `E ≡ 0` as a polynomial. It therefore
suffices to prove `N_m(T) = T^{m-1} N_m(1/T)` when `b = alpha beta = 1`.

Step 2 (`b = 1`, palindromicity). At `b = 1` the weight multiset satisfies
`1/w_j = w_{m-j}` (inversion-closed). Compute from (*):

```text
T^{m-1} N_m(1/T)
  = (alpha-beta)^{-m} sum_j (-1)^j C(m,j) w_j · T^{-1} prod_{i != j} (T - w_i).
```

Now `prod_{i != j}(T - w_i) = prod_{i != j}(-w_i) · prod_{i != j}(1 - T/w_i)
= (-1)^m (prod_i w_i) w_j^{-1} prod_{i != j}(1 - T w_{m-i})`, and
`prod_i w_i = b^{m(m+1)/2} = 1`. Substituting, the `w_j · w_j^{-1}` cancels;
reindex `i' = m - i` and then `j' = m - j` (using `(-1)^{m-j'} (-1)^m =
(-1)^{j'}`) to get

```text
T^{m-1} N_m(1/T) = T^{-1} M(T),
M(T) := (alpha-beta)^{-m} sum_j (-1)^j C(m,j) prod_{i != j} (1 - w_i T).
```

Finally `M(T) - T N_m(T) = (alpha-beta)^{-m} sum_j (-1)^j C(m,j)
(1 - w_j T) prod_{i != j}(1 - w_i T) = (alpha-beta)^{-m}
[ sum_j (-1)^j C(m,j) ] prod_i (1 - w_i T) = 0`, because the bracketed
binomial sum vanishes for `m >= 1`. Hence `T^{m-1} N_m(1/T) = T^{-1} M(T)
= N_m(T)`. ∎

## Theorem 2 (the m = 3 defect exits the character ring)

`N_3 = 1 + 2ab T + b^3 T^2` is irreducible over `K = Q(a,b)`. Consequently
the m=3 defect is NOT a product of factors `(1 - c T)` with
`c ∈ Q(a,b)` — in particular its inverse roots are not Laurent monomials in
`(alpha, beta)` with rational coefficients, i.e. not virtual-character
weights of the underlying object. The pointwise cube of a degree-2
coefficient system is therefore `Sym^3` times an Euler factor whose roots
generate a nontrivial quadratic extension of the function field of the
local data.

*Proof.* Step 1 (irreducibility over `K = Q(a,b)`): the quadratic
`1 + 2ab T + b^3 T^2` factors over `K` iff its discriminant
`(2ab)^2 - 4 b^3 = 4 b^2 (a^2 - b)` is a square in `K`; `4b^2` is a
square, so this requires `a^2 - b` to be a square in `K`. It is not: a
rational function that is a square and a polynomial is a square
polynomial (in the UFD `Q[a,b]`, `(f/g)^2 = h` with `gcd(f,g)=1` forces
`g` to be a unit), and a square polynomial has even degree in each
variable, while `a^2 - b` has degree 1 in `b`.

Step 2 (the roots are not virtual-character weights — the inference
irreducibility-over-`K` alone does NOT give this, since monomial weights
live in the quadratic extension `Q(alpha, beta)`, and e.g. the Satake
polynomial itself is `K`-irreducible with monomial roots; this gap was
found by the pass's adversarial review, which also supplied the following
repair): if both inverse roots of `N_3` were of the form
`c alpha^i beta^j` with `c ∈ Q`, they would lie in `Q(alpha, beta)`, so
the splitting field of `N_3` over `K` — which by Step 1 and the
discriminant is `K(sqrt(a^2 - b))` — would embed in
`Q(alpha, beta) = K(sqrt(a^2 - 4b))` (the Satake splitting field, degree
2 over `K`). Two quadratic extensions coincide iff the product of their
discriminant classes is a square: this would force `a^2 - b` or
`(a^2 - b)(a^2 - 4b)` to be a square in `K`. Neither is: `a^2 - b` by
Step 1's parity argument, and `(a^2 - b)(a^2 - 4b)` because it is a
product of two non-associate irreducibles of `Q[a,b]` (each of degree 1
in `b`, with distinct `b`-leading data), hence squarefree. So the
inverse roots of `N_3` generate a genuinely different quadratic
extension and are not rational multiples of weight monomials. ∎

Contrast (both classical, machine-verified here as oracles):
- m = 2: `N_2 = 1 + bT = 1 - (-det A) T` — the sign-twisted determinant, a
  character-ring object; globally, for a weight-normalized elliptic datum
  (`b = p` at good `p`), the formal Euler-product identity
  `sum a_n^2 n^{-s} = zeta(s-1) L(Sym^2, s) / zeta(2s-2)` (good primes;
  region of absolute convergence) — the local Rankin-Selberg identity
  (classical; Shimura; imported).
- Hadamard product of two independent degree-2 objects:
  `sum_k h_k(A) h_k(B) T^k = (1 - det A det B T^2) / det(1 - A⊗B T)` —
  the Cauchy identity (classical), machine-verified as an oracle.
- Hankel-minor transform: `h_k h_{k+2} - h_{k+1}^2 = -b^{k+1}` (Jacobi-
  Trudi for the partition `(k+1, k+1)`; classical), machine-verified: the
  one transform in the grammar that lands EXACTLY on a functorial object
  (a determinant twist), with trivial defect.
- Adams relabelling: `sum_k h_{2k} T^k = (1 + bT)/det(1 - psi^2(A) T)`
  (machine-verified exact; elementary).

## Theorem 3 (degeneration on the supersingular locus)

On the locus `a = 0` (trace zero), the generic m=2 identity degenerates by
EXACT cancellation: `N_2 = 1 + bT` divides `det(1 - Sym^2(A) T)
= (1 + bT)^2 (1 - bT)` there, and the reduced local series is

```text
sum_k h_k^2 T^k |_{a=0} = 1 / (1 - b^2 T^2),
```

of denominator degree 2 < 3. (Verified exactly for m=2 in X-108500 check
D2; for m <= 6 the trace-zero instantiation `(a,b) = (0,7)` passes the
cross-multiplied rational-equality checks of `matrix/defect_powers_run.py`,
which is how the degeneration is exercised there — explicit higher-m
degeneration rows are not separately emitted; wording corrected after the
adversarial wave.) Interpretation, stated within its finite
scope: the defect law's SHAPE is generically rigid but its degree can drop
on special fibers; any global consumer of the law must treat the
supersingular-type primes separately. *Proof:* at `a = 0`,
`h_{2j} = (-b)^j`, `h_{2j+1} = 0`, so the squared sequence is `b^{2j}` at
even indices, `0` at odd — the displayed geometric series; the factorization
of the Sym^2 polynomial at `a=0` is direct computation. ∎

## Lemma 4 (L3 is cheap: polynomial transforms never fail local rationality)

Let `D(T) ∈ K[T]` be any degree-`d` local factor with `D(0)=1` over any
field `K` of characteristic 0, `h_k` the coefficients of `1/D`, and
`f ∈ K[x]` any polynomial of degree `m`. Then `sum_k f(h_k) T^k` is a
rational function whose denominator divides
`prod_{j=0}^{m} det(1 - Sym^j(A) T)` (with `Sym^0` contributing `(1-T)`),
of degree at most `sum_{j<=m} C(d+j-1, j)` — a bound UNIFORM in the local
data (hence uniform in `p` for an L-function's local system).

*Proof.* Generic case (distinct nonzero inverse roots `alpha_1..alpha_d`):
`h_k = sum_i c_i alpha_i^k` is an exponential polynomial with frequency set
`{alpha_i}`. Products of exponential polynomials are exponential
polynomials whose frequencies are products of frequencies, so `h_k^j` has
frequencies among the degree-`j` monomials in the `alpha_i` — the weights
of `Sym^j(A)` — and `f(h_k) = sum_j f_j h_k^j` has frequencies among the
weights of `⊕_{j<=m} Sym^j(A)`. A sequence `sum_w gamma_w w^k` is rational
with denominator `prod_w (1 - wT)`; the degree bound is the total number of
weights. Degenerate data (argument tightened after the adversarial wave):
the locus of data with `d` DISTINCT NONZERO inverse roots is the complement
of the hypersurface `{disc x e_d = 0}`, a nonempty Zariski-open — hence
dense — subset of data space over a characteristic-0 field. Now consider

```text
R(T) := ( sum_k f(h_k) T^k ) x prod_{j<=m} det(1 - Sym^j(A) T) .
```

Every coefficient of `R` is a polynomial function of the local data
`(e_1, ..., e_d)` (each `h_k`, hence each `f(h_k)`, is, and so is each
symmetric-power determinant). On the dense generic locus, `R` is a
polynomial of degree `<= B := sum_{j<=m} C(d+j-1, j)` (the generic
computation above: the series is a proper fraction over the product of the
symmetric-power factors). So each coefficient of `R` beyond degree `B`
vanishes on a dense subset, hence identically — i.e. `R` is a polynomial
of degree `<= B` for ALL local data, which gives BOTH the divisibility of
the (reduced) denominator into `prod_{j<=m} det(1 - Sym^j(A) T)` and the
uniform degree bound at once. ∎

**Survival reading (#764 ladder):** every polynomial pointwise transform of
every bounded-degree local system passes L3 with a uniform bound — the
ladder's discriminating power against such transforms begins at L4/L6, and
Theorems 1-2 locate the failure exactly: a nontrivial defect numerator for
every `m >= 2` (by the linear-coefficient law `c_1 = a^m - h_m != 0` for
`m >= 2` generically), with the character-ring exit PROVED at `m = 3`
(Theorem 2) and conjectural for `m >= 4`.

## Survival trichotomy (positioning corrected by the boundary audit)

The boundary audit (BOUNDARY_AUDIT_CONSOLIDATED.md of the pass) rules out
the naive criterion "the transform survives globally iff its defect is
effective": a virtual, non-effective defect can still leave full
meromorphic continuation (e.g. `zeta(s)/zeta(2s)`), and the meromorphy
question for Euler products is governed by KNOWN theory — Estermann's
natural-boundary theorem, Dahlquist's extension, and Kurokawa's meromorphy
theorems (CITATION-NEEDED precision on statements; see the audit file), on
top of the classical identifications of the m=2 case (Shimura;
Rankin-Selberg). For symmetric powers of GL(2) forms the "effective
direction" is now unconditional automorphy (Newton-Thorne 2021).

What this pass therefore records is the exact-local layer feeding that
known global theory, and a THREE-STRATUM survival question rather than an
iff:

```text
S1 (entire/classical-poles completion)   — which defects assemble to shifted
                                           zeta/L-factors in the numerator;
S2 (meromorphic continuation to C)       — governed by Estermann/Dahlquist/
                                           Kurokawa-type criteria applied to
                                           the exact defect;
S3 (natural boundary)                    — the generic expectation for
                                           defects outside the character
                                           ring (Theorem 2), NOT proved here
                                           for any specific m.
```

Proof-sized target deposited (not claimed): classify, for the pointwise
powers `m <= 5` with defects computed exactly here, which stratum each
global defect Euler product `prod_p N_m(p^{-s}; a_p, b_p)` occupies for a
fixed GL(2) source, by applying the Estermann/Dahlquist/Kurokawa machinery
to the exact `N_m` — the pass supplies the exact local inputs; the global
classification is future work on top of known theory.
