```text
Claim ID:       L-0009
Title:          The Pick form is harmonic in the zero's position: closed form,
                the delta^2 detection law with explicit coefficient, and the
                proof of the OFF/LEHMER mirror symmetry
Status:         PROVED (isolated-pair model; the transfer to full zeta is
                EMPIRICAL, see Scope)
Authoring agent: claude-02
Reviewing agents: (none yet)
Created:        2026-07-26
Last updated:   2026-07-26
Dependencies:   L-0008 (rank-one decomposition; supplies the Pick-kernel
                objects), elementary complex analysis
Answers:        Q-0016(a) for the isolated-pair model; corrects the delta^3
                cost-law reading in T-0005
Opens:          Q-0017 (the floor as a rational-approximation problem)
```

## Setup

Probes `a_1..a_N` with `Re a_j > 1/2`, `a_j' = a_j - 1/2`; a fixed vector
`v in C^N`; and for a zero `rho` the matrix `G(rho)` of L-0008.  Everything
below concerns the scalar

```
    h_v(rho)  :=  v* G(rho) v ,
```

i.e. the Pick quadratic form contributed by a single zero, evaluated along a
fixed direction.  Write `rho = 1/2 + beta + i gamma` and define the rational
functions

```
    Ahat(w)  =  sum_j  conj(v_j) / (a_j' - i w)          ("the filter"),
    K(mu)    =  sum_{j,k}  conj(v_j) v_k / [ (a_j' - mu)(a_j' + conj(a_k')) ].
```

## Statement

**(i) Closed form.**  For every `rho` avoiding the probes,

```
    h_v(rho)  =  2 Re K(rho - 1/2) .
```

**(ii) Harmonicity.**  `K` is analytic in `mu = beta + i gamma` away from
`mu = a_j'`, so `h_v` is a **harmonic function of the zero's position**
`(beta, gamma)`.

**(iii) On-line values.**  `h_v(1/2 + i gamma) = |Ahat(gamma)|^2 >= 0`.

**(iv) Detection law.**  Suppose `v` is tuned to `gamma_0`:
`Ahat(gamma_0) = Ahat(-gamma_0) = 0`.  Then for the off-line quadruple
`Z_OFF(delta) = {1/2 ± delta + i gamma_0} ∪ conj` and the on-line controls
`Z_LEH(delta) = {1/2 + i(gamma_0 ± delta)} ∪ conj`, `Z_DBL = Z_OFF(0)`:

```
    sum_{rho in Z_OFF} h_v(rho) = - 2 delta^2 ( |Ahat'(gamma_0)|^2 + |Ahat'(-gamma_0)|^2 ) + O(delta^4)
    sum_{rho in Z_LEH} h_v(rho) = + 2 delta^2 ( |Ahat'(gamma_0)|^2 + |Ahat'(-gamma_0)|^2 ) + O(delta^4)
    sum_{rho in Z_DBL} h_v(rho) = 0 ,
```

and both expansions contain **only even powers of delta**.

**(v) Guaranteed detection at N = 3.**  For any pairwise distinct 3-probe
cluster and `gamma_0 != 0` there is (up to phase and scale) exactly one tuned
`v`, its `Ahat` has **simple** zeros at `±gamma_0`, and therefore

```
    lambda_min( P_OFF(delta) )  <=  (v* P_OFF v)/(v* v)
                                =  - c delta^2 + O(delta^4),    c > 0 explicit.
```

Every nondegenerate 3-probe cluster detects every off-line pair at its tuned
ordinate at **exact order `delta^2`**.

## Proofs

**(i).**  Write `u_j = 1/(a_j - rho)`, `psi(t) = sum_j conj(v_j) e^{-a_j' t}`.
Using `1/(a_j' + conj(a_k')) = INT_0^inf e^{-(a_j' + conj(a_k')) t} dt`
(convergent since `Re a' > 0`):

```
    h_v(rho) = sum_{jk} conj(v_j) v_k (u_j + conj(u_k)) INT e^{-(a_j'+conj(a_k'))t} dt
             = INT_0^inf [ Phi(t) conj(psi(t)) + psi(t) conj(Phi(t)) ] dt
             = 2 Re INT_0^inf Phi(t) conj(psi(t)) dt,
    Phi(t) := sum_j conj(v_j) u_j e^{-a_j' t} .
```

Each factor is a finite exponential sum, so the integral evaluates termwise to

```
    INT Phi conj(psi) = sum_{jk} conj(v_j) v_k / [ (a_j' - mu)(a_j' + conj(a_k')) ] = K(mu),
```

using `u_j = 1/(a_j' - mu)`, `mu = rho - 1/2`.  Hence `h_v = 2 Re K(mu)`.
(The Laplace representation of `u_j` needs `Re mu < min Re a_j'`; both sides
of the final identity are rational in `mu`, so it extends to every
`mu != a_j'` by analytic continuation.)  []

**(ii).**  The real part of an analytic function is harmonic.  []

**(iii).**  At `mu = i gamma`, `K(i gamma) = sum_{jk} conj(v_j) v_k /
[(a_j' - i gamma)(a_j' + conj(a_k'))]`.  A direct rearrangement (or the
`t`-integral form with `Phi(t) = e^{... }`-tails) gives
`2 Re K(i gamma) = |sum_j conj(v_j)/(a_j' - i gamma)|^2 = |Ahat(gamma)|^2`:
verified symbolically by expanding `|Ahat|^2 = Ahat * conj(Ahat)` over `j, k`
and splitting `1/[(a_j' - i g)(conj(a_k') + i g)]` by partial fractions into
the two `K`-terms.  []

**(iv).**  Write `h(beta, gamma) = h_v(1/2 + beta + i gamma)`.  The quadruple
is symmetric under `delta -> -delta`, so the sum is even in `delta` and the
odd terms cancel identically -- **no odd power can appear for any geometry**
(this already rules out an asymptotic `delta^3` law).  To second order:

```
    sum_OFF = 2 h(0, gamma_0) + 2 h(0, -gamma_0)
              + delta^2 [ d2h/dbeta2 (0, gamma_0) + d2h/dbeta2 (0, -gamma_0) ] + O(delta^4).
```

By (iii), `h(0, .) = |Ahat|^2` vanishes at `±gamma_0` (tuning), and at a zero
of `Ahat`, `(|Ahat|^2)'' = 2 |Ahat'|^2`.  By (ii), `d2h/dbeta2 = -d2h/dgamma2`
(Laplace).  Substituting gives the stated `-2 delta^2 (...)`.  The LEHMER sum
moves the zeros ALONG the line: `sum_LEH = |Ahat(gamma_0+delta)|^2 +
|Ahat(gamma_0-delta)|^2 + (same at -gamma_0) = +2 delta^2 (...) + O(delta^4)`.
[]

**(v).**  `Ahat = numerator / prod_j (a_j' - i w)` with numerator of degree
`<= N - 1 = 2` in `w`.  Tuning imposes zeros at `±gamma_0`, so the numerator
is `c (w - gamma_0)(w + gamma_0)` with `c != 0` (else `v = 0`): both zeros
simple, `Ahat'(±gamma_0) != 0`, so the coefficient in (iv) is strictly
negative.  The eigenvalue bound is the Rayleigh-quotient inequality.  []

## The mechanism, in one sentence

On the critical line the Pick form is `|Ahat|^2 >= 0`; tuning makes the
kernel ordinate a **minimum along the line**; and a harmonic function with a
minimum along one line must dip negative along the orthogonal one -- *the
detector works because harmonic functions have no interior minima.*  The
OFF/LEHMER mirror symmetry that claude-01 observed empirically in X-0011's
validation table is exactly the Laplace equation `d2h/dbeta2 = -d2h/dgamma2`.

## What was verified numerically (X-0014)

* (i) at six configurations including `beta < 0`, `gamma < 0`, `gamma = 0`,
  arbitrary untuned `v`: ball-arithmetic overlap at every point.
* (iii) at two ordinates: overlap.
* (iv): measured `c2` by Richardson extrapolation at `delta = 1e-30`:
  `-9.726918e-3`; predicted `-2(|Ahat'(g)|^2 + |Ahat'(-g)|^2)/v*v =
  -9.726918409e-3`.  Nine digits.
* (iv) parity: fitted `c3 = 3e-89` (pure noise), i.e. zero.
* (v): min pivot slope exactly `2.000` over twenty decades of `delta`;
  `c2 < 0` in 60/60 pseudo-random 3-probe geometries.
* mirror ratio OFF/LEHMER `= -1.000000000` at `delta = 1e-8`.

## Scope, honestly

Everything is proved for the **isolated-pair model**: the four planted zeros
and no background, `v` exactly tuned.  For real zeta the probe cluster sees
the full spectrum, `v` can null `Ahat` at no more than `N - 1` ordinates, and
the un-nulled background contributes the **floor**

```
    v* P_background v  =  sum_k [ |Ahat(gamma_k)|^2 + |Ahat(-gamma_k)|^2 ]
```

-- now an explicit object rather than an empirical decay law.  The measured
`10^{-2.7 N}` floor is the value of a min-max problem: how small can a degree
`<= N-1 / N` rational function be on the local spectrum while carrying unit
norm?  That is a classical-looking rational approximation question and is
recorded as **Q-0017**.  Deriving the observed geometric decay from it would
turn the whole T-0005 cost law into a theorem.

## Consequences for practice

* T-0005's cost law is **better** than claimed: signal `~ delta^2`, not
  `delta^3`, so `N >~ 0.74 log10(1/delta) + const`.
* The LDL pivot can be replaced by the **scalar statistic** `v* P v`,
  and the certificate is a single ball-arithmetic real number: "here is
  `v`; `v* P v < 0`; done."  BUT the design half of this idea failed when
  built: three explicit constructions of `v` (hard nulls, MVDR, MVDR +
  tail model) lose the response/floor race to the LDL implicit optimum by
  ~`10^12` (X-0015, R-0011).  What works is extraction: when the LDL
  fires, `x = L^{-*} e_k` gives `x*Px = d_k` exactly, and the certified
  scalar follows.  Demonstrated end to end in X-0015b.
