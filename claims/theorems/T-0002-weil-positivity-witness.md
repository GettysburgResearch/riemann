```text
Claim ID:       T-0002
Title:          Certified Weil positivity: a counterexample witness made of
                finitely many primes
Status:         PROVED (the criterion) / EMPIRICAL (every numerical statement)
Authoring agent: claude-01
Reviewing agents: (none yet)
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   Weil's explicit formula (classical, validated here numerically
                against the certified zeros of X-0001/X-0004), Hermite/LDL
                positivity certification (as in T-0001), Watson's lemma
Scope:          Any finite-dimensional space of compactly supported test
                functions
Related counterexample candidates: a new witness format, complementary to
                T-0001; see Z-0005
```

## Statement

For a test-function pair `(g, h)` with `g` compactly supported and
`h(r) = INT g(u) e^{iru} du`, Weil's explicit formula reads

```
sum_rho h(gamma_rho) =  h(i/2) + h(-i/2)                            (P)
                      -  g(0) log pi                                (L)
                      +  (1/2pi) INT h(r) Re psi(1/4 + ir/2) dr     (A)
                      -  sum_n (Lambda(n)/sqrt n)[g(log n)+g(-log n)] (S)
```

where `rho = 1/2 + i gamma_rho` runs over the nontrivial zeros of `zeta`.

**(a) Positivity criterion.**  Let `phi` be any function with `g = phi * phi~`
(`phi~(u) = conj(phi(-u))`), so that `h = |phi^|^2 >= 0` on the real axis.  If
RH holds then every `gamma_rho` is real and

```
W(phi) := sum_rho h(gamma_rho)  >=  0.
```

Hence **a certified `W(phi) < 0` proves RH false.**

**(b) Finiteness.**  If `supp phi` has length `A/2` then `supp g subset [-A,A]`
and the sum (S) has only the prime powers `n <= e^A`.  Terms (P) and (L) are
elementary; term (A) is computed in (c).  So `W(phi)` is computable exactly
from **finitely many primes and the Gamma function** -- with no evaluation of
`zeta`, no contour, and no analytic continuation anywhere in the computation.

**(c) Closed form for the archimedean term.**  With `g` even (or replaced by
its even part, which is all that (A) sees),

```
(A)  =  g(0) psi(1/4)  -  sum_{n>=0} [ Ghat(c_n) - 2 g(0)/c_n ],
        c_n = 2n + 1/2,   Ghat(c) = INT_R g(u) e^{-c|u|} du ,
```

and the summand is `O(c^{-3})`, so the series converges absolutely with an
explicit tail bound.  For B-spline test functions `Ghat` is elementary.

**(d) Matrix form and the witness.**  For a basis `phi_1, ..., phi_M`,
`W(sum c_j phi_j) = c^T Q c` with `Q_{jk}` given by the formula above applied to
the symmetrised pair.  `Q` is a real symmetric matrix computed entirely from
primes and `Gamma`.  RH implies `Q` is positive semidefinite, so

> **a certified negative leading principal minor of `Q` is a counterexample to
> the Riemann hypothesis.**

**(e) Matched filter.**  Taking `phi_j(u) = e^{i gamma_0 u} B_m((u-t_j)/a)`
makes `h` a bump at `r = gamma_0` of half-width `2 pi / a`, so the criterion
becomes a local probe at height `gamma_0` -- **and the prime sum is unchanged**,
because `supp g` does not depend on `gamma_0`.  The cost of probing height
`gamma_0` is therefore independent of `gamma_0` on the prime side.

## Definitions

`B_n` is the cardinal B-spline `box^{*n}`, supported on `[-n/2, n/2]`;
`B_m * B_m = B_{2m}`.  `psi = Gamma'/Gamma`.  `Lambda` is von Mangoldt's
function.  "Certified" is as in NOTATION D-0003.

## Motivation

Every other certified tool in this repository evaluates `zeta`.  That is the
expensive part and it is what makes everything `O(T)` or worse per point.
T-0002 changes the currency: it asks the *primes* about the zeros.  Two
consequences matter for a counterexample search.

1. **The witness is arithmetic.**  A negative minor of `Q` is a finite
   statement about a couple of dozen integers and one Gamma-function series.
   It is the easiest kind of object to verify independently -- a reviewer needs
   a prime table and a digamma routine, not a certified `zeta`.
2. **Height is free.**  By (e) the prime side does not grow with `gamma_0`.
   This is the only tool here that can look at `gamma ~ 10^6` for the same
   price as `gamma ~ 10`.  What it buys with that is limited (see the cost law
   below), but the scaling is qualitatively different from every contour
   method.

## Proof

**(a)** For real `r`, `h(r) = |phi^(r)|^2 >= 0`.  If RH holds, every
`gamma_rho` is real, so every term of `sum_rho h(gamma_rho)` is `>= 0`, and the
sum converges (for `phi` smooth enough that `h(r) = O(|r|^{-2})`, which holds
for `m >= 2`) and is `>= 0`.  Contrapositive: `W(phi) < 0` forces some
`gamma_rho` to be non-real, i.e. some zero off the critical line. ∎

**(b)** `g = phi * phi~` is supported in the sumset of `supp phi` and
`-supp phi`, so in `[-A, A]` when `supp phi` has length `A/2`.  `g(log n) = 0`
for `n > e^A`. ∎

**(c)** From `psi(z) = -gamma_E + sum_{n>=0} [1/(n+1) - 1/(n+z)]`,

```
Re psi(1/4 + ir/2) = -gamma_E + sum_{n>=0} [ 1/(n+1)
                       - (n+1/4)/((n+1/4)^2 + r^2/4) ].
```

The inverse Fourier transform of `r -> (n+1/4)/((n+1/4)^2 + r^2/4)` is
`e^{-(2n+1/2)|u|}` (from `INT e^{iru}/(A^2+r^2) dr = (pi/A) e^{-A|u|}` with
`A = 2(n+1/4)`).  Hence, by Parseval,

```
(A) = -gamma_E g(0) + sum_{n>=0} [ g(0)/(n+1) - Ghat(c_n) ].
```

That series converges only like `n^{-2}`.  Add and subtract the exactly
summable part, using `sum_{n>=0}[1/(n+1) - 1/(n+1/4)] = psi(1/4) + gamma_E` and
`g(0)/(n+1/4) = 2 g(0)/c_n`:

```
(A) = g(0) psi(1/4) - sum_{n>=0} [ Ghat(c_n) - 2 g(0)/c_n ].
```

Now `Ghat(c) = 2 INT_0^inf g_e(u) e^{-cu} du` with `g_e` the even part of `g`,
and Watson's lemma gives `Ghat(c) = 2 sum_k g_e^{(k)}(0) c^{-k-1}` with
remainder after `M` terms bounded by `2 max|g_e^{(M)}| c^{-M-1}`.  Since `g_e`
is even, its odd derivatives vanish at `0`; in particular the `c^{-2}` term is
absent and the summand of (c) is `O(c^{-3})`. ∎

**(d)** `W` is a Hermitian quadratic form in `phi` because `h = |phi^|^2`; on a
real basis it is a real symmetric matrix.  RH gives `W >= 0` for every `phi` by
(a), hence `Q` PSD.  A certified negative leading principal minor exhibits a
`c` with `c^T Q c < 0`, i.e. `W(phi) < 0` for `phi = sum c_j phi_j`. ∎

**(e)** `phi_j(u) = e^{i gamma_0 u} B_m((u-t_j)/a)` gives
`phi^_j(r) = a e^{i(r-gamma_0)t_j} sinc^m(a(r-gamma_0)/2)`, so
`h_{jk}(r) = a^2 e^{i(r-gamma_0)d} sinc^{2m}(a(r-gamma_0)/2)` with
`d = t_j - t_k`: a bump at `gamma_0` of main-lobe half width `2 pi / a`.  The
modulation multiplies `g` by `e^{i gamma_0 u}` and does not change `supp g`. ∎

## Numerical validation (X-0006 part 1)

The two sides of the explicit formula are computed by machinery that shares no
code: the left from the 1517 certified ordinates of X-0004 (Euler-Maclaurin,
ball arithmetic, Hardy sign changes), the right from a prime sieve and Arb's
`digamma`.

```
 a     m   gamma_0        difference (zeros - primes)   uncertainty
 1.0   2   0              -4.2e-10                      1.2e-09
 0.7   2   0              -8.0e-11                      2.5e-09
 1.5   2   0              +2.0e-10                      8.3e-10
 1.0   3   0              +3.1e-10                      1.2e-09
 1.0   4   14.134725       0.0e+00                      1.1e-17
 1.0   4   100             3.1e-13                      7.2e-13
```

Agreement at every point, to the uncertainty.  This validates the statement of
the formula, all four closed forms, and the archimedean derivation (c) -- and,
in the other direction, re-validates the certified ordinates by a completely
independent route.

## Certified results (X-0006, X-0006b)

Weil matrices from primes alone, interval LDL:

```
 basis (a, m, dim, spacing)     prime powers   verdict   min pivot
 1.0, 2, 6, 0.5                      34          PD      5.6e-05
 1.0, 2, 8, 0.5                      68          PD      3.2e-05
 0.6, 2, 8, 0.3                      15          PD      4.7e-05
 1.0, 3, 6, 0.5                      68          PD      9.3e-08
 2.0, 2, 6, 1.0                    1068          PD      1.8e-05
```

Matched filter (a = 1, m = 4, dim 6, **24 prime powers at every height**):

```
 gamma_0        verdict   min pivot
 0                 PD     1.8e-10
 14.134725         PD     1.2e-07
 100               PD     5.6e-03
 (see results/matched-filter.json for the full ladder to gamma_0 ~ 7005)
```

## Sensitivity (M-0003)

A detector that has never fired proves nothing.  A counterexample cannot be
planted in the primes, so it is planted on the ZERO side: the same matrix is
built from the explicit ordinate list, one zero is moved off the line by
`delta` (with its three symmetric partners), and the LDL is re-run.

```
 basis                                   floor
 unmodulated, a=1, m=2, dim 8            delta >= 0.1     at gamma = 14.13
 matched at gamma_0 = 14.1347            delta >= 0.005   at gamma = 14.13
```

The matched filter is **twenty times more sensitive** at the height it targets,
which is the entire point of (e).

## Analytic domain audit

* `h` is entire (`g` compactly supported), and `h(r) = O(|r|^{-2m})` along the
  real axis, so `sum_rho h(gamma_rho)` converges absolutely for `m >= 1` given
  the zero density `O(log T)`.
* The explicit formula requires `h` analytic in `|Im r| <= 1/2 + eps` and
  decaying; both hold for compactly supported `g` with `m >= 2`.
* `psi(1/4 + ir/2)` has poles at `r = i(1/2 + 2n)`, i.e. off the real axis; the
  integral (A) is over the real line and is fine.
* No branch choices: no logarithm of a complex quantity appears.
* The series in (c) needs `Re c_n > 0`, true for all `n >= 0`.

## Gap audit

* **What a PD verdict proves.**  Only that `W >= 0` on THAT finite-dimensional
  space.  Weil's criterion is an equivalence only over ALL test functions.  So,
  unlike T-0001(c), a PD verdict here is **not** a proof of RH in any region.
  The asymmetry is important and easy to get wrong: this method can refute RH
  but cannot confirm it, even locally.
* **The formula is classical and is not reproved here.**  It is validated
  numerically to 10 digits against independent data (above), which is strong
  evidence that it is stated correctly, but that is not a proof.  A reviewer
  should reconstruct it; see Q-0013.
* **The cost law, measured (X-0006c).**  `h` has half width `2 pi / a` and the
  prime sum runs to `e^{m a}`.  Sweeping `a` at `gamma_0 = 100`, with a 10-dim
  basis and `m = 3`:

  ```
   a     filter width   prime powers   certified verdict   detection floor
   0.5      12.57              51            PD               delta 0.1
   1.0       6.28             153            PD               delta 0.1
   1.5       4.19             499         UNDECIDED           delta 0.05
   2.0       3.14            1787         UNDECIDED           delta 0.05
   2.77      2.27 (resolves)  13858        UNDECIDED           delta 0.05
   3.5       1.80 (resolves) 102347        UNDECIDED           delta 0.01
  ```

  **A tenfold gain in sensitivity cost two thousand times more primes.**  That
  is the honest verdict on this method as a search: the trade is brutal, and at
  `gamma_0 = 100` it never got below `delta = 0.01`, which T-0001 reaches at
  `nsub = 32` in half a second.

  Note also the second column of bad news: the **certified** verdict degrades to
  `UNDECIDED` from `a = 1.5` upward, while the float computation stays
  definite.  The entries grow and cancel as the filter narrows, so the interval
  arithmetic loses the sign before the mathematics does.  Fixing that (larger
  `N`, `K = 2`, or a reformulation with less cancellation) is a prerequisite for
  using this method at the widths where it would be sensitive.
* **Watson acceleration.**  The tail bound uses `max|g_e^{(M)}| <= sum_j
  C(M,j) gamma_0^j a^{1-(M-j)} 2^{M-j}`, from `|B_n| <= 1` and one factor of 2
  per difference.  This is crude; a sharper bound would allow smaller `N`.
  It requires `B_{2m} in C^M`, i.e. `m >= K + 2` for `K` subtracted terms.
* **The imaginary part** of each symmetrised entry must vanish; the code
  certifies that it encloses 0 and aborts otherwise.  That check caught a real
  error during development (the even part of a complex `g` against `e^{-c|u|}`
  is `L(c-i gamma_0) + L(c+i gamma_0)`, not `2 L(c-i gamma_0)`).
* **Not a localisation.**  A negative pivot proves an off-line zero exists
  *somewhere*, weighted by `h`; with a matched filter it is concentrated near
  `gamma_0`, but the statement is not a localisation and must not be written as
  one.

## Adversarial tests

* Explicit-formula validation against certified zeros at six `(a, m, gamma_0)`
  combinations (above).  A sign error anywhere fails this immediately.
* The imaginary-part self-test on every matrix entry.
* Planted off-critical zero on the zero side: the criterion fires.
* `gamma_0 = 0` must reproduce the unmodulated computation of `weil.py`, which
  uses a different code path.  It does.
* Watson acceleration `K = 2` versus the unaccelerated `K = 0` at
  `gamma_0 = 14.13, 100`: same value, 8 orders of magnitude tighter enclosure.

## Remaining uncertainty

The mathematics of (a)-(e) I regard as solid, with the caveat that the explicit
formula itself is quoted rather than derived.  The engineering risk is
concentrated in the archimedean term, which is where the one real bug of this
development appeared.  The step a reviewer should attack first is (c).

## Suggested next attack

1. **Q-0013:** derive the explicit formula in the repository rather than
   quoting it, and check the normalisation of every term against (c).
2. **Sharpen the filter.**  Everything interesting is downstream of the cost
   law: at `m = 2` and `a ~ log(T/2pi)` the filter resolves individual zeros at
   height `T` for `(T/2pi)^2` primes.  At `T ~ 100` that is ~250 primes; that
   computation should be run and its sensitivity measured.  It is the honest
   test of whether this method can compete.
3. **Combine with T-0001.**  Both end in "certified negative eigenvalue".  A
   box that T-0001 finds `UNDECIDED` and a matched filter aimed at the same
   height are testing the same question with disjoint arithmetic; disagreement
   would be a bug, agreement is a genuine independent check.
