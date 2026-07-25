# L-5603 — The archimedean block by endpoint expansion, at any carrier

Claim ID: L-5603
Title: Every L-4201 archimedean coefficient is an explicit finite sum in
`1/omega` determined by `k` and its derivatives at three knots, with an
elementary remainder
Status: PROPOSED
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: L-4201; L-4202 (for the `alpha_0` identity only); L-5601 (for the
huge-phase evaluation of the knot exponentials)
Scope: the D-0801 archimedean block at any carrier `T > 0`
Related counterexample candidates: none

## Motivation

O-5603 showed that past the C-5601 barrier the binding constraint is the
archimedean bound, not the prime side: the L-4202 envelope `B_A` grows like `K`
and shrinks only like `1/T`, while the margin it must resolve falls like
`K^{-2}`.  Direct quadrature of the L-4201 integrals removes the pessimism but
needs `O(omega b)` panels per lag, which at the production carrier is
`10^{11}` panels — impossible.  This lemma computes the same coefficients in
`O(1)` work per lag, with accuracy that *improves* as `T` grows.

## Statement

Use L-4201: `b = 2L/K`, `omega = T/2`, `k(t) = e^{-t/4}/(1-e^{-t})`,
`tau_d(r) = (1-|r-d|)_+`, and

\[
 z_d=-\frac1{2\pi}\int_0^{2L}k(t)e^{-i\omega t}\tau_d(t/b)\,dt .
\]

### (a) Lags `d >= 2`

For every `n >= 1`,

\[
 \boxed{\;
 z_d=-\frac1{2\pi}\sum_{m=1}^{n}\frac{m}{b\,(i\omega)^{m+1}}D_d^{(m-1)}
 \;+\;R_{d,n},\;}
\]

\[
 D_d^{(j)}
 =k^{(j)}\!\big((d\!-\!1)b\big)e^{-i\omega(d-1)b}
 -2k^{(j)}(db)e^{-i\omega db}
 +k^{(j)}\!\big((d\!+\!1)b\big)e^{-i\omega(d+1)b},
\]

with

\[
 |R_{d,n}|\le\frac1{2\pi\,\omega^{\,n+1}}
 \int_{(d-1)b}^{(d+1)b}\left|\varphi_d^{(n+1)}(t)\right|dt,
 \qquad \varphi_d=k\cdot\tau_d(\cdot/b),
\]

and the convenient enlargement
`int |phi_d^{(n+1)}| <= 2b\max|k^{(n+1)}| + 2(n+1)\max|k^{(n)}|` over the
support.

In particular the series starts at `omega^{-2}`:

\[
 \boxed{\;
 z_d=\frac{1}{2\pi\omega^2 b}
 \left[k((d\!-\!1)b)e^{-i\omega(d-1)b}-2k(db)e^{-i\omega db}
       +k((d\!+\!1)b)e^{-i\omega(d+1)b}\right]+O(\omega^{-3}) . }
\]

**The off-diagonal archimedean coefficients are `O(1/T^2)`, not `O(1/T)`.**
L-4202 bounds them by `2k((d-1)b)/(\pi T)`; the true size is smaller by a
factor of order `omega b = TL/K`.

### (b) Lag `d = 1`

Its support reaches `t = 0`, where `k` has a simple pole that the hat factor
cancels.  With `g(t) = t\,k(t)`, analytic at `0` with `g(0) = 1`,

\[
 \boxed{\;
 z_1=-\frac1{2\pi}\sum_{m=0}^{n}\frac1{(i\omega)^{m+1}}
 \left[\frac{g^{(m)}(0)}{b}
 -\frac{2m\,k^{(m-1)}(b)}{b}e^{-i\omega b}
 +\frac{m\,k^{(m-1)}(2b)}{b}e^{-2i\omega b}\right]+R_{1,n}. }
\]

Its `m = 0` term is `-1/(2\pi i\omega b)`, of modulus `1/(2\pi\omega b)`.  This
is the **only** `O(1/T)` piece of the entire archimedean block.

### (c) Diagonal

From the L-4202 identity
`alpha_0 = ell_T + (1/2\pi)[-\mathrm{Ci}(\omega b)+\int_0^b q_b(t)\cos(\omega t)dt]`
with `q_b(t) = 1/t - k(t)(1-t/b)` (removable at `0`, value `1/b - 1/4`),

\[
 \alpha_0-\ell_T=\frac1{2\pi}\left[
 -\frac{\sin\psi}{\psi}+\frac{\cos\psi}{\psi^2}+\frac{2\sin\psi}{\psi^3}
 +\frac{q_b(b)\sin\psi}{\omega}
 -\frac{q_b'(0)-q_b'(b)\cos\psi}{\omega^2}\right]+O(\omega^{-3}),
\]

where `psi = omega b`.

### (d) Consequence

Every knot exponential is `e^{-i\omega m b} = e^{-iTLm/K}`, a huge phase that is
evaluated once per lag with MPFR exactly as in L-5601.  So the complete block
`A_K` costs `O(K)` high-precision evaluations, independently of `T`, and the
truncation error decreases as `T` grows.

## Proof

For a function `psi` that is `C^{n+1}` on `[a,c]`, repeated integration by parts
gives

\[
 \int_a^c\psi(t)e^{-i\omega t}dt
 =\sum_{m=0}^{n}\frac{\psi^{(m)}(a)e^{-i\omega a}-\psi^{(m)}(c)e^{-i\omega c}}
   {(i\omega)^{m+1}}
 +\frac1{(i\omega)^{n+1}}\int_a^c\psi^{(n+1)}(t)e^{-i\omega t}dt,
\]

which also bounds the remainder by `\omega^{-(n+1)}\int|\psi^{(n+1)}|`.

Split the support of `varphi_d` at the kink `t = db`.  On each half
`varphi_d = k\,u` with `u` affine, so `u'' = 0` and

\[
 \varphi_d^{(m)}=k^{(m)}u+m\,k^{(m-1)}u',\qquad u'=\pm\frac1b .
\]

For `d >= 2` the outer endpoints have `u = 0`, so
`\varphi_d^{(m)} = m k^{(m-1)}(\cdot)u'` there; at the kink `u = 1` from both
sides, so the two `k^{(m)}` terms cancel in the difference and only
`-2m k^{(m-1)}(db)/b` survives.  Collecting the four boundary contributions
(two outer, two at the kink) gives exactly `(m/b)D_d^{(m-1)}` with the signs as
displayed, and the `m = 0` terms vanish because `varphi_d` is continuous and
vanishes at the outer endpoints.  Multiplying by `-1/2\pi` gives (a).

For `d = 1` the left endpoint is `t = 0`, where `k` is singular but
`varphi_1 = g(t)/b` on `[0,b]` with `g = tk` analytic.  Applying the same
identity with `\psi = g/b` on `[0,b]` and `\psi = k\,u` on `[b,2b]`, and using
`g^{(m)}(b)/b = k^{(m)}(b) + m k^{(m-1)}(b)/b` so that the kink difference is
again `-2m k^{(m-1)}(b)/b`, gives (b).  Part (c) is the standard asymptotic of
`Ci` together with two integrations by parts of `\int_0^b q_b\cos(\omega t)dt`,
legitimate because `q_b \in C^\infty[0,b]` after its removable singularity is
filled in.  ∎

## Executed validation

`experiments/X-5601-rigorous-carrier-stream/archimedean_asymptotic.py`, checked
against the direct quadrature of `archimedean_block.py` at
`c = 10^9`, `K = 1024`, `T = 6283.185307` (`omega b = 127.16`), `n = 3`:

```text
sum_{d>=2} |z_d|   expansion   1.1925597e-4
                   quadrature  1.1925588e-4
max_d |difference|             1.134e-10        (remainder bound 5.84e-8)
sum_d |difference|             1.230e-10        (remainder bound 6.19e-8)
alpha_0 - ell_T    expansion   8.333665e-7
                   quadrature  8.302582e-7
```

At the production parameters `c = 10^11`, `K = 1024`,
`T = 94184072727073/20` (`omega b = 1.1648e11`), where direct quadrature would
need `10^{11}` panels per lag:

```text
alpha_0 - ell_T                2.1924e-24
|z_1|                          1.3664e-12
sum_{d>=2} |z_d|               1.2006e-22
assembled row sum              1.3664e-12
expansion remainder bound      2.1924e-36
L-4202 uniform bound B_A       1.6566e-10        -> 121x larger
runtime                        1.5 s
```

So at the production carrier the entire archimedean block is, to 10 significant
figures, the single number `z_1 \approx 1/(2\pi\omega b) = K/(2\pi T\log c)`.

## Effect on the production certificate

Reassembling `Q = A_K + R_K - S_K` with the computed blocks instead of the
L-4202/L-4203 envelopes (`exact_certificate.py`) gives at `c = 10^{11}`:

```text
lambda_min(Q)          floating  2.671872230e-4
lambda_min(Q)          lower     2.671861467e-4
total enclosure half-width       7.633e-11
  Gram residual + rounding       7.348e-11     <-- now dominant
  L-5601 stream enclosure        2.830e-12
  archimedean expansion remainder 2.192e-36
  pole (assembled, norm)         5.962e-18
```

The bottleneck has moved a third time: it is now the binary64 Gram factorization
residual, an artifact of the linear algebra rather than of the mathematics, and
is removable by factoring in higher precision.

## Analytic domain audit

- `k` is real-analytic on `(0, \infty)` with a simple pole at `0`; all
  derivatives are evaluated at `t = mb > 0` for `d >= 2`, and the `d = 1` case
  uses `g = tk`, analytic at `0`.
- `q_b` is `C^\infty` on `[0,b]` once its removable singularity at `0` is
  filled in with `1/b - 1/4`.
- The integration-by-parts identity needs only piecewise `C^{n+1}` regularity
  and is applied on each smooth half separately.
- `Ci` is used at the positive real argument `\omega b`.
- No branch of any multivalued function occurs.

## Dependency audit

- L-4201 supplies the coefficients being computed and the `1/2` convention on
  the upper diagonal.
- L-4202 is used only for its exact `Ci`/`q_b` decomposition of `alpha_0`
  (its step 1), not for its bound.
- L-5601 supplies the huge-phase machinery for `e^{-iTLm/K}`; here it is done
  with MPFR at 60 digits because there are only `K` of them.

## Gap audit

1. The expansion is asymptotic, not convergent.  The remainder bound is what
   makes it usable, and it must be evaluated, not assumed.  It is only small
   when `\omega(d-1)b \gg n`, which fails for the first few lags at small `T`;
   `d = 1` is treated separately and `d = 2,3` should be checked against
   quadrature whenever `\omega b` is not large.
2. The implementation is ordinary floating point.  It is **not** an interval
   computation, so certificates built on it are `PROPOSED`, not certified.
   Making it directed is `Q-5604` and is now the last analytic gap in the chain.
3. `k^{(j)}` is obtained by numerical differentiation in mpmath; a symbolic
   closed form would be preferable for an interval version.
4. The bound `int|\varphi^{(n+1)}| <= 2b\max|k^{(n+1)}| + 2(n+1)\max|k^{(n)}|`
   uses the maximum over the support, which for the `1/t`-like `k` is attained
   at the left endpoint `(d-1)b`; that is what the implementation evaluates.
5. Nothing here touches the prime side, the normalization, or RH.

## Adversarial tests

1. Agreement with direct quadrature at several `(c, K, T)` with `omega b` from
   `10` to `10^5`, requiring the difference to sit inside the remainder bound.
   Implemented as `test_asymptotic_matches_quadrature`.
2. Increase `n` and require the value to move by less than the previous
   remainder bound.
3. Set `k \equiv 1` artificially: the expansion must reproduce the exact
   elementary integral of a hat against `e^{-i\omega t}`.
4. Take `omega b` small (a few units) and require the expansion to *fail* the
   quadrature comparison, confirming the remainder bound is not vacuous.
5. Compare the assembled `A_K` against the L-4202 envelope and require
   `||A_K - ell_T I|| <= B_A`; a violation would refute one of the two.

## Remaining uncertainty

The integration-by-parts algebra is elementary and I checked the boundary
bookkeeping twice, in both directions, against the quadrature.  What I am not
confident about is the *implementation* of the derivative evaluations at
higher `n` and small `d`, where `k^{(j)}((d-1)b)` grows like `j!/((d-1)b)^{j+1}`
and cancellation between the three knot terms becomes severe.  The executed
runs stay far from that regime, but an interval version must handle it.

## Suggested next attack

`Q-5604`: make this directed.  The pieces needed are an interval evaluation of
`k^{(j)}` at the knots (a closed form in terms of the Eulerian-like numbers of
`e^{-t/4}/(1-e^{-t})` would be ideal), an interval knot phase from L-5601, and
an outward evaluation of the displayed remainder.  Nothing in the structure
resists it; it is bookkeeping.
