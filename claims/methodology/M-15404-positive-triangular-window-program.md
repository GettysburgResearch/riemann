# M-15404 — Positive proof programme for the triangular prime window

Claim ID: `M-15404`  
Title: Preserve the complete critical cancellation through renewal, pair energy, or screw positivity  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15409`--`L-15413`, `T-15406`  
Scope: positive route only  
Related counterexample candidates: none

## Objective

For `h=log 4`, prove either

\[
 \sup_{x\ge x_0}|Q_h(x)|<\infty
 \tag{M-15404.1}
\]

or

\[
 \sup_{X\ge1}\frac1X
 \int_{x_0}^{x_0+X}|Q_h(x)|^2dx<\infty.
 \tag{M-15404.2}
\]

`T-15406` then gives RH.

The triangular window is preferred for theorem development because it is finite,
piecewise linear, and has two independent exact prime-side representations.
The smoother notched windows remain useful for numerical reconnaissance and
finite moat construction.

## Four equivalent positive targets

### A. Critical Hardy estimate

Prove

\[
 \sup_{\sigma>0}\frac{\sigma}{2\pi}
 \int_{\mathbb R}
 \left|
 \widehat G_{h,L}(\sigma+it)
 \frac{\zeta'}{\zeta}(1/2+\sigma+it)
 \right|^2dt<\infty.
 \tag{M-15404.3}
\]

This is the clean analytic target. It permits simple boundary poles at critical
zeros but excludes every interior pole.

### B. Positive renewal square function

For the positive primitive

\[
 A_h=\mu*H_h,
 \]

prove

\[
 \sup_X\frac1X
 \int_{x_0}^{x_0+X}e^x|A_h'(x)|^2dx<\infty.
 \tag{M-15404.4}
\]

Use the exact renewal equation

\[
 A_h*\nu=x(\nu*H_h)-\nu*(uH_h)
 \]

and preserve the critical deconvolution correlation. A fixed positive-weight
contraction is insufficient; the estimate must reach the boundary
`Re z=-1/2` in the renewal variable.

### C. Signed prime-pair energy

Prove

\[
 \sum_{m,n}
 \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}
 \mathcal K_X(\log m,\log n)=O(X),
 \tag{M-15404.5}
\]

with the exact triangular autocorrelation kernel. `L-15411` shows that the
off-diagonal portion must cancel

\[
 \frac4{3h}X^2+O(X).
 \]

The proof must retain signs and correlations. Absolute values, diagonal
estimates, and termwise majorants are disallowed as main steps.

### D. Screw/infinite-divisibility route

Use

\[
 Q_h=\mathcal D_hg_\zeta+O(e^{-5x/2})
 \]

from `L-15410`. Prove conditional negative definiteness of `g_zeta`, or a
weaker finite-difference energy theorem sufficient to bound `mathcal D_hg_zeta`.
The full CND statement is already RH-equivalent; a successful proof must derive
it from the prime-side cancellation rather than assume a zero representation.

## Markov-chain formulation

Let `pi_x` be the moving integer law of `L-15413`, and let

\[
 p_h(x)=\mathbb P_{\pi_x}(N_1=1).
 \]

Then

\[
 Q_h(x)=e^{x/2}
 \bigl[Z_h'(x)p_h(x)+Z_h(x)p_h'(x)\bigr].
 \tag{M-15404.6}
\]

A positive probabilistic proof must construct a compensated martingale or
flow identity in which the two polynomial-size terms cancel before applying
Cauchy--Schwarz. Bounding the score and mass derivatives separately cannot
reach the target.

### Candidate Markov deliverables

1. An exact carré-du-champ formula for the upward/downward adjoint pair under an
   invariant von Mangoldt weight.
2. A representation of (M-15404.6) as one compensated boundary flux.
3. A uniform quadratic-variation bound on each interval of logarithmic length
   `X`.
4. A comparison between the chain energy and the triangular prime-pair kernel.
5. An exact finite-state truncation with a complement estimate uniform in the
   truncation.

## Selberg-symmetry subprogramme

Let

\[
 d\Sigma=t\,d\mu+d\mu*d\mu.
 \]

Its Laplace transform is

\[
 \widehat\Sigma_L(z)=\frac{\zeta''}{\zeta}(1+z),
 \]

and its arithmetic coefficients

\[
 \frac{\Lambda(n)\log n+(\Lambda*\Lambda)(n)}n
 \]

are nonnegative. Convolving the exact Selberg identity against `H_h` produces
a nonlinear positive equation for `A_h`.

The research target is not another PNT proof. It is a **signed energy identity**
whose quadratic term equals the off-diagonal cancellation in `L-15411` and
whose remaining arithmetic error is `O(X)`. The classical `O(x)` Selberg
remainder, used termwise, is far too large after critical rescaling.

## Fail-fast tests for proposed proofs

A proposed proof is rejected if it uses any of the following as the final
cofinal step:

- positivity and convergence of `A_h` without a critical derivative estimate;
- Markov invariance without a boundary square-function theorem;
- a prime number theorem error weaker than square-root scale;
- a zero-density theorem that permits even one off-line zero;
- an upper bound formed by discarding the prime-pair cross terms;
- a finite support ladder or fitted power law;
- conditional negative definiteness imported from RH;
- a fixed `sigma_0>0` Hardy estimate that does not approach `sigma=0`.

## Proof-producing finite programme

While the analytic identity is pursued, build exact controls:

1. directed triangular-window values using the complete ratio-64 prime-power
   annulus;
2. independent hinge replay through four cumulative values;
3. exact partition and polynomial integration of finite mean-square blocks;
4. exact diagonal/off-diagonal ledgers verifying `L-15411` numerically;
5. finite Markov absorption ledgers verifying `L-15413`;
6. comparison with the screw finite difference and elementary correction;
7. increasing-precision and independent-backend overlap.

These calculations can falsify a proposed inequality or reveal the right
compensator. No finite passing set is promoted to RH.

## Current boundary

The positive route has been reduced to one finite exact statistic and three
mathematically equivalent energy mechanisms. None of the critical cancellation
estimates is currently proved. The programme has removed window complexity and
hidden asymptotic terms, but not the RH-strength boundary estimate itself.
