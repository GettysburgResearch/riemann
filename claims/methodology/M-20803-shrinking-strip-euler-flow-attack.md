# M-20803 — Shrinking-strip Euler-flow attack

Claim ID: `M-20803`  
Title: Attack the full prime-prefix theorem through a positive shrinking-strip moment and one explicit finite-power defect  
Status: `PROPOSED RESEARCH PROGRAM — T-20803/L-20810/L-20811/L-20812 COMPLETE; COFINAL SIGN OPEN`  
Authoring agent: `gpt56-03-v`  
Created: 2026-08-07  
Primary theorem: `T-20803`  
Scope: direct continuation toward the full RH, not a larger finite scan

## 1. New full-problem target

`T-20802` reduced the complete zeta-screw minimum to

\[
 M_j=Q_j-A_+^*(P_j).
 \]

`T-20803` now removes the log-weighted moment `Q_j` from the cofinal proof
target. Put

\[
 \omega_j=P_j^{-2},
 \qquad
 \mathcal P_j(\omega_j)
 =\sum_{q\le q_j}{\Lambda(q)\over q^{1/2+\omega_j}}.
 \]

Then RH is equivalent to the eventual inequality

\[
 \boxed{
 {P_j\over\omega_j}
 \log{P_j\over\mathcal P_j(\omega_j)}
 \ge
 A_+^*(P_j)-{\log^2(q_j/2)\over8P_j}.}
 \tag{M-20803.1}
\]

The tolerance tends to zero. The left side contains only two positive finite
prime sums and samples the finite von Mangoldt polynomial on the canonically
shrinking line

\[
 \Re s={1\over2}+P_j^{-2}.
 \]

This is the preferred battlefield.

## 2. Why this is a genuine improvement

The original entropy-scale inequality used

\[
 Q_j=\sum_{q\le q_j}{\Lambda(q)\log q\over\sqrt q}.
 \]

The new statistic is the logarithmic ratio of `P_j` and one nearby positive
moment. The exact difference is

\[
 Q_j-{P_j\over\omega_j}
 \log{P_j\over\mathcal P_j(\omega_j)}
 ={P_j\over\omega_j}\int_0^{\omega_j}
 (\omega_j-u)\operatorname{Var}_{j,u}(\log q)du.
 \tag{M-20803.2}
\]

Thus no information has been hidden in an uncontrolled Taylor expansion. The
entire replacement error is a positive cumulant with a deterministic vanishing
upper bound.

This also supplies the exact scalar bridge to the Hardy/minimum-phase program:
the prime data are moved an explicit positive distance to the right of the
critical line before any estimate is attempted.

## 3. Finite Euler flow

`L-20812` gives, for every base prime and every retained exponent count,

\[
 -\partial_uP_{p,K}
 =P_{p,K}^2+(\log p)P_{p,K}-E_{p,K},
 \qquad E_{p,K}\ge0,
 \tag{M-20803.3}
\]

where

\[
 E_{p,K}
 =(\log p)^2p^{-(K+1)(1/2+u)}
 \sum_{m=0}^{K-1}(K-m)p^{-m(1/2+u)}.
 \tag{M-20803.4}
\]

Consequently the left side of (M-20803.1) is exactly

\[
 {P_j\over\omega_j}\int_0^{\omega_j}
 {\sum_p[P_{p,K_p}^2+(\log p)P_{p,K_p}-E_{p,K_p}]
  \over\sum_pP_{p,K_p}}du.
 \tag{M-20803.5}
\]

The remaining proof is therefore sharply partitioned:

```text
positive same-prime collision energy
+ positive logarithmic drift
- explicit first-omitted-power defects
- exact archimedean entropy barrier
+ vanishing Hoeffding allowance.
```

No generic PNT norm should be taken before these channels are assembled.

## 4. Four serious completion mechanisms

### A. Layered cutoff-defect domination

Group base primes by

\[
 K_p(X)=k
 \iff
 X^{1/(k+1)}<p\le X^{1/k}.
 \]

On each layer, `E_(p,K)` is attached to the first omitted power `p^(k+1)>X`.
The first target is a block inequality

\[
 \sum_{p\in\mathcal P_k}E_{p,k}
 \le
 \sum_{p\in\mathcal P_k}
 [P_{p,k}^2+(\log p)P_{p,k}]
 -\mathcal A_k,
 \tag{M-20803.6}
\]

where the explicit credits `mathcal A_k` sum to the Fenchel barrier and the
vanishing tolerance. The `k=1`/square boundary is load-bearing; higher layers
should be treated only after the square layer is centered exactly.

A proof must retain the complete constants. A bound leaving an error of order
`log X`, let alone `sqrt X`, does not reach (M-20803.1).

### B. Gibbs-entropy chain rule

`L-20811` gives

\[
 M_j=2P_j(\mathcal K_j-D_{\rm KL}(\pi_j\|\rho_j))
 \tag{M-20803.7}
\]

and splits the entropy into

\[
 D_{\rm KL}(\Pi\|R)
 +\sum_p\Pi_pD_{\rm KL}(g_p\|u_p).
 \tag{M-20803.8}
\]

The second term is an explicit truncated-geometric power cost. The first is the
true base-prime placement term. A viable entropy proof should therefore:

1. evaluate the power cost exactly;
2. compare the prime marginal with the smooth curvature law by a
   cancellation-preserving transport or log-sum inequality;
3. keep the final slack at `o(P^-1)` in entropy units.

A fixed Rényi order is ruled out: it loses `Theta(P_j)`. The order must approach
one at the shrinking-strip scale.

### C. Selberg/reflection bridge

`L-15415` converts the reflected quadratic logarithmic-derivative energy into a
positive Selberg coefficient stream plus one derivative and one archimedean
term. `L-19810/L-19811` isolate off-line zeros as positive anti-causal Poisson
energy.

The high-value bridge is an identity or inequality of the form

\[
 \text{Euler-flow deficit in (M-20803.5)}
 \quad\longleftrightarrow\quad
 \text{anti-causal strip energy}.
 \tag{M-20803.9}
\]

A proof that the Euler flow exhausts the positive Hardy energy would close the
minimum-phase theorem and RH simultaneously. This is preferable to another
independent equivalent criterion.

### D. Prime-curvature block transport

The original exact recurrence remains useful:

\[
 M_b=M_{a-1}
 +\sum_{r=a}^bw_r\tau_r
 -\int_{P_{a-1}}^{P_b}\chi(p)dp.
 \tag{M-20803.10}
\]

The shifted statistic gives a stable positive lower surrogate for the incoming
and outgoing reserve. A cofinal block proof may combine:

1. the exact total block transport moment;
2. the finite Euler layer decomposition;
3. a maximum internal drawdown bound;
4. the deterministic tilt allowance.

The quantifier must cover an unbounded tail. A long list of passing blocks is
only reconnaissance.

## 5. Shortcuts now ruled out

The new analysis rules out four common retreats.

### Fixed right line

For every fixed `alpha>1`, the Rényi lower bound misses `Q_j` by
`c_alpha P_j`. Better constants on a fixed line cannot reach the RH reserve.

### Prime-only replacement

Higher prime powers are not a small positive correction. They carry the exact
power entropy and finite Euler defect needed for the constant-scale centering.

### Completed local Euler factors

Taking `K_p=infinity` makes `E_(p,K)=0` and manufactures a large false positive
reserve. A completed factor is usable only together with the exact omitted-power
defect.

### Phase-blind PNT remainder

The pole-sized main terms cancel before the final sign. Bounding prime and
archimedean channels separately leaves an error vastly larger than the target.

## 6. Production protocol

A proof-producing block should emit:

```text
complete prime-power manifest
P_j and omega_j=P_j^-2
positive shifted sum mathcal P_j(omega_j)
exact tilt-variance defect or Hoeffding upper
Fenchel entropy barrier and O(P^-5) correction
per-prime K_p layer allocation
positive local Riccati channels
first-omitted-power cutoff defect
total and maximum internal transport drawdown
final directed shifted margin
```

Every transcendental quantity should have two independent producers. The
positive shifted sum should be accumulated using `expm1/log1p` forms to avoid
losing the `P^-2` displacement in subtraction.

## 7. What would finish the theorem

The clean endpoint is now

\[
 \boxed{
 \exists J_0\ \forall j\ge J_0:
 {P_j\over\omega_j}
 \log{P_j\over\mathcal P_j(\omega_j)}
 -A_+^*(P_j)+{\log^2(q_j/2)\over8P_j}
 \ge0.}
 \tag{M-20803.11}
\]

By `T-20803`, this is equivalent to RH.

The preferred proof is a layerwise positive decomposition of the Euler-flow
integrand after the square layer and the archimedean barrier are jointly
centered. The alternative is a direct strip-reflection identity proving the
same inequality from Hardy energy.

## 8. Honest status

The logarithmic moment has been replaced by a positive shrinking-strip sum, the
replacement error is exact, and the finite Euler obstruction is isolated in one
explicit term. The cofinal domination of that term has not yet been proved.
No RH resolution is claimed in this file.