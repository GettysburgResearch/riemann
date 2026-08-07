# Shrinking-strip Euler-flow continuation

Agent: `gpt56-03-v`  
Date: 2026-08-07  
Repository: `gfreund123/riemann`  
Branch: `agent/gpt56-03-r/207-directed-d0001-frame`  
PR: #208  
Classification: exact RH-equivalent tilted-prime criterion and positive Euler-flow decomposition; RH not proved

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

The left side now consists of two positive finite prime sums and an explicit
logarithm. No zero data, matrix, support mesh, or Schur complement remains.

## Exact cumulant identity

For the Gibbs law

\[
 \pi_{j,u}(q)
 ={\Lambda(q)q^{-1/2-u}\over\mathcal P_j(u)},
\]

the replacement defect is exactly

\[
 M_j-\widetilde M_j
 ={P_j\over\omega_j}\int_0^{\omega_j}
 (\omega_j-u)\operatorname{Var}_{j,u}(\log q)du.
\]

Popoviciu's variance bound gives `eta_j`. A proof object may replace the cheap
range bound by the exact directed variance integral without changing the
logical theorem.

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
difference of two positive call transforms.

## Entropy interpretation

`L-20811` uses

\[
 \pi(q)={\Lambda(q)q^{-1/2}\over P_j},
 \qquad
 \rho(q)={\Lambda(q)\over\psi(q_j)}
\]

and proves

\[
 D_{KL}(\pi\|\rho)
 =\log{\psi(q_j)\over P_j}-{Q_j\over2P_j},
\]

so

\[
 M_j=2P_j(\mathcal K_j-D_{KL}(\pi\|\rho)).
\]

The entropy chain rule separates the base-prime marginal from the explicit
truncated-geometric power entropy. A fixed Rényi order loses `Theta(P_j)`; the
order must approach one on a shrinking strip.

## Finite Euler flow and the second breakthrough

`L-20812` gives

\[
 -\partial_uP_{p,K}
 =P_{p,K}^2+(\log p)P_{p,K}-E_{p,K},
 \qquad E_{p,K}\ge0.
\]

The first interpretation treated `E_(p,K)` as the remaining local negative
channel. `L-20813` proves that this is false: the collision square pays it
exactly.

\[
 \boxed{
 P_{p,K}^2-E_{p,K}
 =(\log p)^2
  \sum_{\ell=2}^K(\ell-1)p^{-\ell(1/2+u)}
 \ge0.}
\]

Equivalently, the right side is the sum over ordered retained power pairs
`m+n<=K`. Therefore

\[
 \boxed{
 -\partial_uP_{p,K}
 =(\log p)P_{p,K}
 +(\log p)^2
  \sum_{\ell=2}^K(\ell-1)p^{-\ell(1/2+u)}.}
\]

The global shifted statistic is now

\[
 {P_j\over\omega_j}\int_0^{\omega_j}
 {\mathcal B_j(u)+\mathcal C_j(u)
  \over\mathcal P_j(u)}du,
\]

where both channels are positive and

\[
 \mathcal C_j(u)
 =\sum_{\substack{p^\ell\le q_j\\\ell\ge2}}
 { (\Lambda*\Lambda)(p^\ell)
  \over p^{\ell(1/2+u)}}.
\]

Thus the trusted finite Euler flow has **no internal negative arithmetic
channel**. The cutoff defect is exactly the part of the completed collision
square lying outside the retained exponent triangle.

## Square-layer centering

At `u=0`, the diagonal Selberg channel satisfies

\[
 \mathcal C_j(0)
 ={1\over8}\log^2q_j+C_{\rm diag}+o(1).
\]

The square layer supplies the only divergent term. Every exponent layer
`ell>=3` is absolutely summable. Therefore the higher-power channel can be
centered to `o(1)` unconditionally.

The remaining RH-sensitive object is the correlated comparison

```text
positive base-prime drift
+ centered diagonal Selberg channel
versus
nonlinear archimedean entropy barrier.
```

The next proof should not return to bounding `E_(p,K)` separately; that problem
is closed.

## Exact regression

`X-20807` is a standard-library Fraction checker. It verifies

```text
arithmetic mean       6
arithmetic variance  26
reference variance   24
initial reserve        1
Fenchel barrier       23
final reserve          3
```

and

```text
P_local                    45/16
Q_local                    117/8
cutoff defect              441/256
triangular retained power    99/16
```

with both local reconstructions equal to `117/8`. Verdict:

```text
PASS_EXACT_L20810_L20812_L20813_IDENTITIES
```

## Indicative Riemann computation

At the global record-low prefix through `10^7`, ending at `q=3089`, the
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
is below `3.1e-4`. These are calibration values only: not directed and not
cofinal.

## Exact remaining theorem

The finish line is

\[
 \boxed{
 \exists J_0\ \forall j\ge J_0:
 {P_j\over\omega_j}
 \int_0^{\omega_j}
 {\mathcal B_j(u)+\mathcal C_j(u)
  \over\mathcal P_j(u)}du
 \ge A_+^*(P_j)-{\log^2(q_j/2)\over8P_j}.}
\]

The leading completion routes are:

1. a centered Selberg/reflection square after the square-layer constant and
   archimedean barrier are assembled jointly;
2. the exact prime/power entropy chain rule at `o(P^-1)` entropy scale;
3. an identity between the centered positive Euler flow and the anti-causal
   Poisson energy of `L-19810/L-19811`;
4. a cofinal block-transport theorem using the shifted statistic as a stable
   lower reserve.

## SERIOUS RESOLUTION PATH

Yes. The route is now:

```text
finite positive shifted von Mangoldt sum
-> exact cumulant sandwich
-> wholly positive triangular Euler/Selberg flow
-> centered arithmetic-versus-archimedean inequality
-> square-sampling/Landau transfer
-> RH.
```

The centered comparison has not been proved in this pass. RH is not claimed
solved.

## Files

```text
claims/theorems/T-20803-shrinking-strip-tilted-prime-criterion.md
claims/lemmas/L-20810-prime-prefix-levy-cumulant-transport.md
claims/lemmas/L-20811-gibbs-entropy-prime-power-chain.md
claims/lemmas/L-20812-finite-euler-riccati-strip-flow.md
claims/lemmas/L-20813-triangular-retained-power-convolution.md
claims/methodology/M-20803-shrinking-strip-euler-flow-attack.md
claims/observations/O-20806-shrinking-strip-tilt-recon.md
claims/experiments/X-20807-levy-euler-flow-verifier.md
experiments/X-20807-levy-euler-flow/
integration/gpt56-03-v-208-shrinking-strip-euler-flow.md
```