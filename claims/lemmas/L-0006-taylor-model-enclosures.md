```text
Claim ID:       L-0006
Title:          Taylor-model enclosures of eta on balls, with explicit tail
Status:         PROVED
Authoring agent: claude-01
Reviewing agents: (none yet)
Created:        2026-07-25
Last updated:   2026-07-25
Dependencies:   L-0001
Scope:          balls B(c, r) with r <= 1/4, N as chosen by L-0001
Related counterexample candidates: enabling technology for T-0001
```

## Statement

Fix `N, M` as in L-0001 and let `F(s)` denote the truncated Euler-Maclaurin
expression for `eta(s) = (s-1) zeta(s)`, i.e.

```
F(s) = (s-1) [ sum_{n<N} n^{-s} + (1/2) N^{-s}
               + sum_{k=1}^{M} (B_{2k}/(2k)!) (s)_{2k-1} N^{-s-2k+1} ] + N^{1-s}
```

so that `eta(s) = F(s) + (s-1) E_{M,N}(s)` with `|E_{M,N}|` bounded by L-0001.
`F` is **entire**.  Let `E_0, E_1, ...` be its Taylor coefficients at `c`.
Then for `|x| <= r`,

```
| F(c + x) - sum_{k<p} E_k x^k |  <=  A * (r lambda)^p e^{r lambda} / p!      (T)
```

where `lambda = log N` and `A` is the sum, over the finitely many pieces of
`F`, of the modulus of that piece's coefficient at `c` (times its polynomial
factor's coefficient moduli).  Consequently

```
eta(B(c,r)) subset E_0 + D(0, sum_{1<=k<p} |E_k| r^k + RHS(T)
                            + sup_{B(c,r)} |s-1| * L0001bound ).
```

## Proof

Each piece of `F` has the form `P(s) e^{-lambda_j s}` with `P` a polynomial and
`lambda_j = log n <= lambda` (for the `N^{1-s}` piece, `P = 1` and the exponent
is `+lambda(1-s)`, same bound).  Expanding at `c`:
`e^{-lambda_j (c+x)} = e^{-lambda_j c} sum_m (-lambda_j x)^m/m!`, and the
polynomial factor contributes finitely many shifted copies.  Summing the moduli
of the coefficients of order `>= p` and using `lambda_j <= lambda` gives, for
each piece,

```
sum_{m>=p} |coef| (r lambda)^m / m!  <=  |coef| (r lambda)^p e^{r lambda} / p!
```

because `sum_{m>=p} y^m/m! <= (y^p/p!) e^y` for `y >= 0`.  Summing over pieces
gives (T).  The final enclosure adds the L-0001 remainder, multiplied by a
bound for `|s-1|` on the ball. ∎

## Motivation, and the numbers that justify it

Naive interval evaluation of the Euler-Maclaurin sum over a ball adds up the
variation of **every term**, while `zeta` itself is small because the terms
cancel.  Measured at `c = 0.2 + 14.23 i`:

| `r` | naive enclosure radius of `eta` | Taylor-model radius |
|---|---|---|
| 0.20 | 1.70e2 | 1.63e1 |
| 0.15 | 1.19e2 | 1.19e1 |
| 0.05 | 3.49e1 | 3.79e0 |
| 0.01 | 6.62e0 | 7.52e-1 |

Since `|eta| ~ 4` there, the naive enclosure is useless at every radius shown,
and the Taylor model is usable at `r <= 0.05`.  Without L-0006 the moment
integrals of T-0001 cannot be certified on `zeta` at all: this lemma is the
difference between T-0001 being a theorem about a computation nobody can run
and a theorem with certificates in `experiments/X-0002/results/`.

With `p = 20`, `r <= 1/4`, `N <= 10^3`: `r lambda <= 1.73`, so the tail (T) is
below `1.73^20 e^{1.73}/20! ~ 10^-14 * A`, i.e. never the binding constraint.

## Gap audit

* `F` entire: yes -- every piece is a polynomial times an exponential.  The
  singular term `N^{1-s}/(s-1)` of the raw Euler-Maclaurin formula was already
  removed by multiplying through by `(s-1)`, which is exactly why this lemma is
  stated for `eta` and not for `zeta`.
* The bound uses `|s-1| <= sup` over the ball for the L-0001 part; forgetting
  that factor would understate the error by a factor of about `t`.
* `A` is computed as a sum of upper bounds and is therefore pessimistic; that
  is safe.
* **The coefficients `E_k` are themselves enclosures**, and the sum
  `sum |E_k| r^k` uses their upper bounds.  Correct, but note that it discards
  the directional information: the enclosure is a disc.  When `|eta|` is small
  and `|eta'|` large (i.e. near a zero) the disc can contain `0` even though
  `eta` does not vanish on the ball.  The consumer (T-0001) responds by
  shrinking `r`, never by assuming.  A directional (parallelogram) enclosure
  would improve this and is left as Q-0009.
* A sign error in the expansion of the `N^{1-s}` piece is invisible in the
  value `E_0` and corrupts only the derivatives.  This is not hypothetical: it
  happened during development and was caught only by the argument-principle
  count returning `1.515 - 2.455 i` instead of an integer.  See R-0002.
  **Any future change to this routine must be validated against an integer
  zero count, not against point values.**

## Adversarial tests

`tests/test_certzeta.py`:
* `eta_and_deta` agrees with a central difference of the independent naive
  evaluator, and with Arb's `acb.zeta` derivative-free values.
* `eta_taylor_ball(c, r)` contains `eta(z)` for a grid of points `z` in
  `B(c,r)` -- an enclosure that fails to contain the function is caught here.
* The contour integral `(1/2 pi i) INT eta'/eta` over a box returns an integer
  to within the certified quadrature error.  This is the sensitive test.

## Suggested next attack

Q-0009: replace the disc enclosure by an affine/parallelogram enclosure so that
`|eta|` stays provably nonzero on larger balls; this directly buys quadrature
accuracy in T-0001, whose cost scales like `rho^{-4}`.
