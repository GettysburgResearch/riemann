# Shrinking-strip Euler-flow continuation

Agent: `gpt56-03-v`  
Date: 2026-08-07  
Repository: `gfreund123/riemann`  
Branch: `agent/gpt56-03-r/207-directed-d0001-frame`  
PR: #208  
Classification: exact new RH-equivalent tilted-prime criterion and proof-facing Euler decomposition; RH not proved

## Executive result

The previous pass reduced the global zeta-screw minimum to the prime-prefix
reserve

\[
 M_j=Q_j-A_+^*(P_j).
\]

This pass moves the theorem further. The logarithmically weighted moment

\[
 Q_j=\sum_{q\le q_j}{\Lambda(q)\log q\over\sqrt q}
\]

is replaced by one positive finite von Mangoldt sum on the shrinking line

\[
 \Re s={1\over2}+P_j^{-2}.
\]

Put

\[
 \omega_j=P_j^{-2},
 \qquad
 \mathcal P_j(\omega_j)
 =\sum_{q\le q_j}{\Lambda(q)\over q^{1/2+\omega_j}},
\]

and

\[
 \widetilde M_j
 ={P_j\over\omega_j}
  \log{P_j\over\mathcal P_j(\omega_j)}
 -A_+^*(P_j).
\]

`T-20803` proves the exact sandwich

\[
 \widetilde M_j\le M_j\le\widetilde M_j+\eta_j,
 \qquad
 \eta_j={\log^2(q_j/2)\over8P_j}\to0.
\]

Together with the square-sampling/Landau transfer, it proves

\[
 \boxed{
 RH
 \iff
 \widetilde M_j\ge-\eta_j
 \text{ for every sufficiently large prime-power prefix}.}
\]

This is a genuine change of attack surface. The left side now consists of two
positive finite prime sums and an explicit logarithm. No zero data, derivative
with respect to the prime exponent, matrix, support mesh, or Schur complement
remains.

## Exact cumulant identity

For the Gibbs law

\[
 \pi_{j,u}(q)
 ={\Lambda(q)q^{-1/2-u}\over\mathcal P_j(u)},
\]

the replacement defect is not estimated heuristically. It is exactly

\[
 M_j-\widetilde M_j
 ={P_j\over\omega_j}\int_0^{\omega_j}
 (\omega_j-u)\operatorname{Var}_{j,u}(\log q)du.
\]

Popoviciu's variance bound gives `eta_j`. Therefore a future proof can replace
the inexpensive range bound by the exact directed variance integral without
changing the theorem.

## Compound-Poisson interpretation

`L-20810` defines the finite arithmetic Lévy measure

\[
 \nu_j=\sum_{q=p^k\le q_j}{1\over k\sqrt q}\delta_{\log q}.
\]

The associated compound-Poisson law has

\[
 \mathbb E X_j=P_j,
 \qquad
 \operatorname{Var}(X_j)=Q_j.
\]

The Fenchel curvature generates an explicit reference compound-Poisson law of
the same mean and variance

\[
 A_+^*(P_j)+A(\log2).
\]

Hence

\[
 M_j=A(\log2)
 +\operatorname{Var}(X_j)-\operatorname{Var}(Y_{P_j}).
\]

An equivalent stop-loss formula expresses the reserve as the integrated
difference of two positive call transforms. This connects the prime-transport
criterion to the infinitely-divisible zeta program without importing RH.

## Entropy interpretation

`L-20811` uses the probability laws

\[
 \pi(q)={\Lambda(q)q^{-1/2}\over P_j},
 \qquad
 \rho(q)={\Lambda(q)\over\psi(q_j)}.
\]

It proves

\[
 D_{KL}(\pi\|\rho)
 =\log{\psi(q_j)\over P_j}-{Q_j\over2P_j},
\]

so

\[
 M_j=2P_j(\mathcal K_j-D_{KL}(\pi\|\rho)).
\]

The entropy chain rule separates the base-prime marginal from the explicit
truncated-geometric power entropy. A Rényi hierarchy approaches the target from
right-shifted positive prime sums.

A fixed Rényi order cannot close the theorem: for `1<alpha<2` its generic loss
is `c_alpha P_j`. The order must approach one at a shrinking-strip scale. This
explains rather than merely observes why a fixed vertical line remains too
coarse.

## Finite Euler Riccati flow

`L-20812` gives the exact local identity

\[
 -\partial_uP_{p,K}
 =P_{p,K}^2+(\log p)P_{p,K}-E_{p,K},
\]

where

\[
 E_{p,K}
 =(\log p)^2p^{-(K+1)(1/2+u)}
 \sum_{m=0}^{K-1}(K-m)p^{-m(1/2+u)}\ge0.
\]

The full shifted statistic is therefore

\[
 {P_j\over\omega_j}\int_0^{\omega_j}
 {\sum_p[P_{p,K_p}^2+(\log p)P_{p,K_p}-E_{p,K_p}]
  \over\sum_pP_{p,K_p}}du.
\]

The exact remaining arithmetic composition is now visible:

```text
positive same-prime collision energy
+ positive logarithmic drift
- positive first-omitted-power cutoff defect
- archimedean entropy barrier
+ vanishing tilt allowance.
```

Completing local Euler factors sets `E=0` and manufactures a false reserve.
Dropping higher prime powers removes the same load-bearing channel in a
different coordinate system. Both shortcuts are now formally excluded.

## Exact regression

`X-20807` is a standard-library Fraction checker. It verifies a synthetic Lévy
reserve

```text
arithmetic mean       6
arithmetic variance  26
reference variance   24
initial reserve        1
Fenchel barrier       23
final reserve          3
```

and the finite Euler identity

```text
P_local             45/16
Q_local             117/8
cutoff defect       441/256
Riccati reconstruction 117/8.
```

Verdict:

```text
PASS_EXACT_L20810_L20812_IDENTITIES
```

## Indicative Riemann computation

At the global record-low prefix found through `10^7`, ending at `q=3089`, the
80-decimal-place replay gives

```text
exact Fenchel reserve M
0.0275205733536208048204145750691337826974942559163525421663039...

shrinking-strip margin tilde M
0.0155668761738849273126544785831975853434439859791034637044906...

exact positive tilt-variance defect
0.0119536971797358775077600964859361973540502699372490784618133...

universal Hoeffding tolerance
0.0620164700643069875665941071430353127006195359710194328168290...
```

The stronger strict shifted test is positive at the hardest known finite prefix.
At the final prefix through `10^7`, the ordinary extended-precision tilt defect
has fallen below `3.1e-4`.

These are calibration values only. They are not directed and not cofinal.

## Exact remaining theorem

The new finish line is

\[
 \boxed{
 \exists J_0\ \forall j\ge J_0:
 {P_j\over\omega_j}
 \log{P_j\over\mathcal P_j(\omega_j)}
 \ge A_+^*(P_j)-{\log^2(q_j/2)\over8P_j}.}
\]

A proof may now attack:

1. layerwise domination of the first-omitted-power defects;
2. the exact prime/power entropy chain rule;
3. a Selberg/reflection identity for the finite Euler flow; or
4. block transport with the shifted statistic as a stable incoming reserve.

The most attractive route is to center the square layer and archimedean barrier
jointly, then factor the remaining Euler-flow integrand into a positive
convolution plus a summable layer defect.

## SERIOUS RESOLUTION PATH

Yes. The route is now:

```text
finite positive shifted von Mangoldt sum
-> exact finite Euler Riccati flow
-> layerwise positive domination of the cutoff defect
-> tolerant cofinal shifted inequality
-> square-sampling/Landau transfer
-> RH.
```

The missing layerwise domination has not been proved in this pass. RH is not
claimed solved.

## Files

```text
claims/theorems/T-20803-shrinking-strip-tilted-prime-criterion.md
claims/lemmas/L-20810-prime-prefix-levy-cumulant-transport.md
claims/lemmas/L-20811-gibbs-entropy-prime-power-chain.md
claims/lemmas/L-20812-finite-euler-riccati-strip-flow.md
claims/methodology/M-20803-shrinking-strip-euler-flow-attack.md
claims/observations/O-20806-shrinking-strip-tilt-recon.md
claims/experiments/X-20807-levy-euler-flow-verifier.md
experiments/X-20807-levy-euler-flow/
```