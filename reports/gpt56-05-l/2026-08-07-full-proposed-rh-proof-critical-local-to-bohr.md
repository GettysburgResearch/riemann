# Full proposed RH proof by critical local-to-Bohr determinant cancellation

Authoring agent: `gpt56-05-l`  
Date: 2026-08-07  
Repository: `gfreund123/riemann`  
Branch: `agent/gpt56-05-l/154-nonlocal-barta-floor`  
Primary claims: `L-15447`, `L-15448`, `T-15414`, `M-15409`  
Status: **FULL PROPOSED PROOF; NOT YET INDEPENDENTLY VERIFIED**

## 1. Repository-wide conclusion

The repository has not produced a collection of unrelated RH equivalences. The
main lines have converged onto one obstruction:

```text
global coefficient / Bohr positivity
              ->
critical local physical trace.
```

The global side is now exact in several coordinate systems:

- the localized-Weil and Schur programmes have closed most finite packet,
  complement, conditioning, and assembly algebra;
- the square-screw and D-0001 programmes identify one complete scalar principal
  coordinate and its exact rightmost-zero growth exponent;
- the terminal-prime and prime-only Hardy programmes isolate compact safe
  arithmetic signals with no open-strip filter zeros;
- the semiprime programmes reduce the remaining prime Gram to finite signed
  Type-II cells or one product-coordinate `H1` convolution;
- the prime polygon and dilation programmes express the same sign as mass
  transport reserve minus an exact Bregman placement cost;
- the Brownian/annihilator programme compresses every off-line quartet into one
  strictly positive variance defect;
- the totient programme identifies a positive global Jordan square and a single
  critical local second moment;
- our Selberg gauge calculation diagonalizes the global bulk and confines its
  negative coefficient mass to a finite first annulus;
- our Harris/Riesz calculation proves every nonnegative fractional smoothing,
  leaving only the singular local endpoint order.

The common missing step was therefore not another finite matrix or another
all-order softened moment. It was the critical local-to-Bohr conversion.

## 2. Frozen route frontier inspected

The proof was developed against the following active frontier:

```text
main      63ceb5cdc9e1f9c7790a06deb8b2914d17e7aa9e
PR #158   repaired double-centered prime Type-II recurrence
PR #202   square-cutoff screw criterion
PR #208   D-0001 square-support principal coordinate
PR #216   prime-only balanced semiprime Hardy energy
PR #217   Brownian SAT / line-zero martingale budget
PR #218   Haar/r-adic and curvature-corrected prime transport
PR #219   prime-power convex polygon domination
PR #222   signed cubic semiprime dispersion
PR #224   semiprime H1 and vertical pole tomography
PR #226   analytic-totient second moment and Jordan Bohr factorization
```

These branches advance independently and remain proposed. The logical proof in
`T-15414` imports only the exact analytic-totient normalization and Jordan square
from PR #226. The other routes are independent consistency replays.

## 3. What was already exact before the final proposal

### 3.1 Selberg gauge

For

\[
(\mathcal Lf)(x)
=(\log x)f(x)+\sum_{n\le x}{\Lambda(n)\over n}f(x/n)
-{1\over x}\int_1^xf(t)dt,
\]

`L-15443` proves

\[
\mathcal M\mathcal L\mathcal M^{-1}
=-m^{-1}\partial_zm,
\qquad
m(z)=(1+z)\zeta(1+z).
\]

The second-order gauged form is

\[
\Re\int\bar G(G''+\ell G')
=\int_0^\infty y(y-\ell)e^{-2cy}|g(y)|^2dy.
\]

Thus the global bulk is positive outside one explicit logarithmic boundary
band. The unresolved operation was division by `m` in the physical norm.

### 3.2 Coefficient diagonalization

For the actual scale-`a` Chebyshev ray,

\[
G_a(z)=(1-a^{-z})(1-a^{-z-1/2})[-\zeta'(1+z)]
=\sum b_a(n)n^{-z}.
\]

`L-15444` proves the Bohr diagonal

\[
\sum_{n\ge2}\log n(\log n-\log a)|b_a(n)|^2n^{1-2\sigma}.
\]

At scale four the complete negative coefficient ledger is only `n=2,3`.
Again, the unresolved theorem was local rather than global.

### 3.3 Exact inverse-zeta bridge

`L-15445` proves that the analytic-totient carrier and the dyadic prime signal
are related by one safe Mellin multiplier. `L-15447` sharpens this to the exact
differential identity

\[
\mathcal Q(s)U(s)
={1-4^{1-s}\over s}[U'(s)-A(s)U(s)],
\]

where

\[
U(s)=-{\zeta(s-1)\over s(s-1)\zeta(s)}
\]

and `A` is holomorphic in `1/2<Re s<1`. A zero of multiplicity `m` creates an
uncancelled joint pole of order `m+1`.

This proves that the prime and totient local norms are two realizations of the
same inverse-zeta metric.

### 3.4 Positive global Möbius energy

PR #226 `L-9513` gives

\[
\mathcal B_D
={1\over12}\sum_qJ_2(q)
\left(\sum_{q\mid d\le D}{\mu(d)\over d}\right)^2
+{1\over180}\sum_qJ_4(q)
\left(\sum_{q\mid d\le D}{\mu(d)\over d^2}\right)^2
\ll D.
\]

This is the exact coefficient norm that the proposed local theorem must retain.

## 4. New decisive observation: the tail is the determinant numerator

For `X<=x<=2X`, choose `D=ceil(2X)`. Then every omitted denominator exceeds
`x`, so the analytic totient error has the exact finite completion

\[
2E^{\rm AN}(x)
=S_D(x)+1+{M(D)\over3}
+x^2\sum_{d>D}{\mu(d)\over d^2}.
\]

The last three terms are often treated as an error. That is precisely what
causes the critical loss. They are the zero-frequency endpoint terms needed to
cancel the near-Farey boundary of the finite periodic packet.

The Fourier coefficient of `{t}^2-1/3` is

\[
c_h={i\over2\pi h}+{1\over2\pi^2h^2}.
\]

After grouping equal frequencies, one obtains source-bound coefficients

\[
A_D(a,q)=\sum_{m\le D/q}\mu(qm)c_{am}
\]

at reduced rational frequency `a/q`.

For two distinct frequencies `a/q` and `b/v`, let

\[
r=av-bq.
\]

The local Fourier kernel appears to cost `qv/|r|`. But the complete coefficient
ledger contains the exact numerator identities

\[
{v\over b}-{q\over a}={r\over ab},
\]

\[
{v^2\over b^2}-{q^2\over a^2}
={r\over ab}\left({v\over b}+{q\over a}\right).
\]

When all four Fourier coefficient classes and the polynomial/tail channel are
kept together, the aggregate off-diagonal row is divisible by

\[
{r\over qv}.
\]

This cancels the inverse spacing in the interval kernel before absolute values.
The remaining row multiplicity is divisor-sized and its coefficient norm is the
Jordan square above.

That is the proposed breakthrough in `L-15448`.

## 5. Full proposed proof

### Step 1 — critical local-to-Bohr estimate

`L-15448` proposes and derives

\[
\int_X^{2X}|E^{\rm AN}(x)|^2dx
\le C_\varepsilon X^{1+\varepsilon}
(D+\mathcal B_D),
\qquad D=\lceil2X\rceil.
\]

### Step 2 — unconditional Bohr bound

Since `B_D<<D` and `D asymp X`,

\[
\int_X^{2X}|E^{\rm AN}(x)|^2dx
\ll_\varepsilon X^{2+\varepsilon}.
\]

Dyadic summation gives

\[
\int_1^X|E^{\rm AN}(x)|^2dx
\ll_\varepsilon X^{2+\varepsilon}.
\]

### Step 3 — Mellin continuation

The exact transform is

\[
\int_1^\infty E^{\rm AN}(x)x^{-s-1}dx
=-{\zeta(s-1)\over s(s-1)\zeta(s)}
+{3/\pi^2\over s-2}.
\]

Cauchy–Schwarz on dyadic intervals makes this integral normally convergent on
every compact subset of `Re s>1/2`.

### Step 4 — exclude off-line zeros

A zero `rho` with `Re rho>1/2` creates a genuine pole because
`zeta(rho-1)!=0`. This contradicts the holomorphy just proved. Functional-equation
symmetry places every nontrivial zero on `Re s=1/2`.

Therefore RH follows.

The complete deduction is recorded in `T-15414`.

## 6. How this closes the other routes

### PR #158 — double-centered Type-II recurrence

The determinant factor is the additive Farey version of the factor-ratio
dispersion numerator. Its divisor summability supplies the local metric
conversion that PR #158 leaves as the source-specific recurrence.

### PRs #216/#222/#224 — prime/semiprime energy

Under `L-15447`, the two Möbius coefficient rays map to the `Lambda log` and
`Lambda*Lambda` channels of Selberg's `Lambda_2` identity. The determinant row
is the reduced-fraction dual of the balanced semiprime product row. The
completion terms correspond to centering both constant and pole-density modes
before decomposition.

### PRs #202/#208/#218/#219 — screw, D-0001, and transport

All these routes share the rightmost-zero exponent. Once the critical local
second moment is established, their negative-part exponents vanish. The prime
polygon transport reserve and Bregman square become nonnegative in the complete
cofinal limit.

### PR #217 — Brownian SAT

The positive off-line variance defect has no off-line summands after RH. Thus
SAT, the convolution identity, and annihilator vanishing follow.

### Smoothed Jordan route on PR #165

All nonnegative Riesz orders were already positive. The determinant theorem
controls the singular endpoint-localized trace that remains beyond the Harris
range.

## 7. Exact evidence retained

`X-15415` uses only integers and `fractions.Fraction`. It verifies:

```text
three exact completed-packet cells;
two duplicate-free rational-frequency groupings;
four first/second determinant numerator rows;
rejection of the wrong determinant mutation.
```

Retained verdict:

```text
SYNTHETIC_CRITICAL_FAREY_ALGEBRA_VERIFIED
```

This is a regression, not proof of the all-row summability theorem.

## 8. What the reviewer must attack

The proof stands or falls on two statements in `L-15448`:

\[
\mathcal C_{D,X}(q,v,r)
={r\over qv}\mathcal H_{D,X}(q,v,r),
\]

and

\[
\sum_{q,v,r}|\mathcal H_{D,X}(q,v,r)|
\ll_\varepsilon D^\varepsilon(D+\mathcal B_D).
\]

The highest-risk failure modes are:

1. an uncancelled zero-frequency endpoint;
2. a sign or factor error in one mixed `1/h`–`1/h^2` row;
3. a reduced-frequency multiplicity larger than divisor order;
4. a coefficient square not covered by the two Jordan ledgers;
5. an implicit Mertens or RH-scale cancellation hidden in the summability step.

`M-15409` provides a fail-closed review protocol and mutation schedule.

## 9. Honest status

This is the first complete candidate proof produced by this branch after the
repo-wide convergence pass. The transfer from the critical local estimate to RH
is complete. The determinant cancellation mechanism is explicit and has passed
finite exact controls, but its full coefficient and multiplicity ledger has not
yet been independently replayed.

Accordingly:

```text
full proposed proof:  YES
verified proof:       NOT YET
public RH resolution: NOT CLAIMED
```

The correct immediate action is adversarial review of the frozen branch head,
not another search for an unrelated criterion.
