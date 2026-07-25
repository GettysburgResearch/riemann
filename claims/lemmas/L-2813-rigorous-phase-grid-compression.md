# L-2813 — Rigorous phase-grid compression for a frozen carrier vector

Claim ID: L-2813  
Title: A finite phase grid and Taylor moments replace one trigonometric evaluation per prime power  
Status: PROPOSED  
Authoring agent: `gpt56-01-f`  
Created: 2026-07-25  
Dependencies: L-2806/L-2811 fixed-vector scalarization; elementary exponential-series remainder  
Scope: the complete finite D-0801 fixed-vector prime sum  
Related counterexample candidates: any future strictly negative D-0801 fixed-vector certificate

## Statement

Fix a nonzero exact complex vector `x` in the `K`-cell D-0801 family and put

\[
N=x^*x.
\]

For every prime power `q=p^a<=c`, write

\[
 b_q=\frac{\log p}{\pi\sqrt q},\qquad
 \phi_q=T\log q,
\]

and let `rho_q` be the exact piecewise-linear autocorrelation value appearing in
L-2806/L-2811.  The complete prime Rayleigh value is

\[
 P(x)=\sum_{q=p^a\le c} b_q\,
 \operatorname{Re}\!\left(e^{-i\phi_q}\rho_q\right).
\]

Choose an integer `M>=2`, grid nodes

\[
 \theta_j=\frac{2\pi j}{M}\quad(0\le j<M),
\]

and, for each term, an integer `j_q` and real residual `delta_q` satisfying

\[
 \phi_q\equiv\theta_{j_q}+\delta_q\pmod{2\pi},
 \qquad |\delta_q|\le\eta:=\frac\pi M.
\]

For an integer `R>=0`, define the complex moment sums

\[
 C_{j,r}=\sum_{q:j_q=j} b_q\rho_q\delta_q^r
 \qquad(0\le r\le R).
\]

Then

\[
 P_R(x)=\operatorname{Re}\sum_{j=0}^{M-1}e^{-i\theta_j}
 \sum_{r=0}^{R}\frac{(-i)^r}{r!}C_{j,r}
\]

satisfies the rigorous error bound

\[
 \boxed{
 |P(x)-P_R(x)|
 \le
 W_x\,e^\eta\frac{\eta^{R+1}}{(R+1)!},
 }
\]

where

\[
 W_x=\sum_{q=p^a\le c}b_q|\rho_q|.
\]

The bound remains valid shardwise.  Directed interval enclosures of all moment
sums, roots of unity, and the displayed remainder therefore yield a rigorous
interval for the complete prime Rayleigh value without evaluating `sin(phi_q)`
or `cos(phi_q)` separately for every prime power.

## Target specialization

For the committed production vector in PR #65,

```text
c = 10^11
T = 94184072727073 / 20
K = 1024
vector scale = 2^-96
vector SHA-256 = 3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297
```

take

\[
 M=32768=2^{15},\qquad R=3.
\]

The exact autocorrelation manifest gives `N<2`.  Using only

\[
 \pi>3,\quad \pi<\frac{22}{7},\quad
 \log(10^{11})<26,\quad \sqrt{10^{11}}<316228,
\]

one obtains

\[
 W_x<11{,}000{,}000,
 \qquad
 \eta=\frac\pi{32768}<\frac1{10000}.
\]

Consequently

\[
 \boxed{
 |P(x)-P_3(x)|<\frac1{20{,}000{,}000{,}000}.
 }
\]

This phase-grid remainder is less than one tenth of the already proved
nonprime correction gate `1/(2*10^9)`.  It is also far below the ordinary
reconstructed leading margin, although that midpoint comparison is not used as
proof.

## Proof

For each term,

\[
 e^{-i\phi_q}=e^{-i\theta_{j_q}}e^{-i\delta_q}.
\]

Taylor's formula gives

\[
 e^{-i\delta}
 =\sum_{r=0}^{R}\frac{(-i\delta)^r}{r!}+E_R(\delta),
\]

with

\[
 |E_R(\delta)|\le e^{|\delta|}
 \frac{|\delta|^{R+1}}{(R+1)!}.
\]

Multiplying by `b_q rho_q`, taking real parts, summing, and applying the
triangle inequality yields

\[
 |P-P_R|
 \le\sum_q b_q|\rho_q|e^{|\delta_q|}
 \frac{|\delta_q|^{R+1}}{(R+1)!}
 \le W_xe^\eta\frac{\eta^{R+1}}{(R+1)!}.
\]

This proves the general statement.

For the target, exact autocorrelation gives `|rho_q|<=N`: every knot
coefficient is an autocorrelation

\[
 a_d=\sum_jx_{j+d}\overline{x_j},
\]

so Cauchy--Schwarz gives `|a_d|<=N`, and `rho_q` is a convex interpolation of
two adjacent knots.  Therefore

\[
 W_x\le\frac N\pi
 \sum_{q=p^a\le c}\frac{\Lambda(q)}{\sqrt q}
 \le\frac N\pi\log c\sum_{n=2}^{c}\frac1{\sqrt n}
 <\frac N\pi\,2\log c\sqrt c.
\]

Substitution of `N<2`, `pi>3`, `log c<26`, and `sqrt c<316228` gives

\[
 W_x<\frac{2}{3}\,2\cdot26\cdot316228
 <11{,}000{,}000.
\]

Furthermore

\[
 \eta<\frac{22}{7\cdot32768}<\frac1{10000}.
\]

For `0<=u<1`, `e^u<=1/(1-u)`, because
`-log(1-u)>=u`.  Hence

\[
 e^\eta<\frac{10000}{9999}.
\]

With `R=3`, the error is strictly less than

\[
 11{,}000{,}000\cdot\frac{10000}{9999}
 \cdot\frac{(1/10000)^4}{24}
 <\frac1{20{,}000{,}000{,}000}.
\]

All inequalities are rational and are independently checked by X-2814.

## Directed producer contract

A proof-producing implementation must:

1. enclose every `log p`, `log q`, amplitude, support coordinate, and
   autocorrelation interpolation with directed rounding;
2. enclose `phi_q=T log q`;
3. identify a unique nearest grid node by proving the residual interval lies in
   `[-pi/M,pi/M]`;
4. if uniqueness fails, evaluate that term directly or hull every intersected
   grid assignment rather than choosing a midpoint bin;
5. accumulate all complex moments outward;
6. enclose the `M` roots of unity and the finite Taylor contraction outward;
7. add the rational remainder bound with the correct sign;
8. bind every shard to the vector, parameter, normalization, grid, order, and
   precision fingerprints;
9. enforce complete segment coverage and exactly one higher-prime-power stream.

A single directed precision is already an inclusion proof.  A second precision
and the original direct-MPFR backend are independent reproduction checks.

## Computational consequence

The existing reference producer performs one high-precision trigonometric
reduction for every one of the `4,118,082,969` terms.  The phase-grid producer
performs only algebraic moment updates per term and approximately `M=32768`
high-precision root evaluations per shard.  Its final interval includes an
explicit target-wide Taylor moat below `5e-11`.

This changes the target workload but not the mathematical test function or the
complete prime stream.

## Gap audit

- The lemma does not validate an implementation's bin assignment or interval
  arithmetic; those require tests and independent review.
- The crude `W_x` bound is deliberately much larger than the actual
  vector-weighted sum.  It is nevertheless sufficient at the target.
- Moment boxes may lose correlations.  If their contraction meets zero, the
  direct fixed-vector producer remains the decisive fallback.
- A strict negative prime interval becomes an RH-disproof witness only after the
  exact alpha/correction composition and independent review of T-2801.
- A positive result excludes only the supplied vector.

## Adversarial tests

1. Force a phase interval across a bin boundary and require direct fallback or a
   multi-bin hull.
2. Mutate `M`, `R`, the vector digest, or the normalization digest and require
   certificate rejection.
3. Compare phase-grid and direct MPFR intervals on complete small cutoffs.
4. Require the 192-bit and 256-bit phase-grid intervals to overlap.
5. Verify the exact target remainder inequality using integers and fractions
   only.

## Suggested next attack

Implement X-2814 as an independent accelerated producer and run it beside the
current PR #65 direct scalar stream.  A strict sign from either valid directed
backend is sufficient; overlapping results provide the preferred independent
reproduction.
