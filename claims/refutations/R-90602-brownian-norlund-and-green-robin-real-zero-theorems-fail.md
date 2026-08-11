# R-90602 — The logarithmic Nörlund and central-binomial Brownian real-zero proposals fail at high frequency

Claim ID: `R-90602`  
Status: **REFUTATION — DEPENDS ON L-90603/L-90604**  
Created: 2026-08-11  
Targets: BLNRZ in `L-21706/T-21705`; BGRRZ in `T-21704` and PR #296

## 1. Refuted targets

The Brownian programme proposed two positive cutoff mixtures followed by functional-equation symmetrization:

1. logarithmic Nörlund weights
   \[
   \lambda_{N,K}=1/(KH_N);
   \]
2. central-binomial Green weights
   \[
   \lambda_{N,K}=\omega_K/\sum_{J\le N}\omega_J,
   \qquad
   \omega_K=[\binom{2K}{K}/4^K]^2.
   \]

Their closing theorems BLNRZ/BGRRZ asked for an unbounded sequence—more strongly every `N`—on which every zero of

\[
 \mathcal X_N(s)=m_{\lambda,N}(s)+m_{\lambda,N}(1-s)
\]

in `0<Re s<1` lies on `Re s=1/2`.

## 2. Refutation

Both weight families retain top-half mass `>>1/log N`, so `L-90603` applies. For every fixed

\[
 1/2<\beta<1
\]

and every sufficiently large `N`, the one-sided factor has infinitely many high-frequency zeros with real parts tending to `beta`.

`L-90604` proves that functional-equation symmetrization preserves those zeros: the reflected term is smaller by `|t|^(1/2-beta)`, and Rouché gives a nearby zero of `mathcal X_N`.

Therefore, for each of the logarithmic and central-binomial producers and every sufficiently large `N`,

\[
 \boxed{
 \mathcal X_N(s)=0
 \text{ for infinitely many }s\text{ with }\operatorname{Re}s>1/2.
 }
 \tag{R-90602.1}
\]

No unbounded real-zero subsequence exists.

## 3. Disposition

Retained:

- finite Brownian gamma identities;
- positive cutoff mixtures;
- exact functional equation and reflection symmetry;
- quantitative local-uniform convergence to xi;
- Green/occupation formulas;
- one-fiber Robin self-adjointness;
- finite scans as bounded-height reconnaissance.

Refuted:

- BLNRZ;
- BGRRZ;
- all-large or cofinal real-zero stability for either positive mixture;
- the proposed finite-real-zero-to-RH chain based on those producers.

Still logically possible:

- a height-dependent producer `N=N(T)` with a theorem only below height `T`;
- a redesigned, non-Bohr-unstable producer;
- an infinite limiting canonical system constructed directly, rather than via globally real-zero finite Dirichlet approximants.

The Riemann Hypothesis remains unproved.

## 4. Why the earlier evidence was misleading

The violations occur at imaginary heights escaping to infinity for each fixed finite `N`. Consequently:

- local-uniform convergence on compact subsets remains true;
- every fixed-height scan can pass;
- every individual Robin fiber can be self-adjoint;
- positive averaging and exact functional-equation symmetry can both hold;

while the complete finite mixture still has infinitely many off-line zeros much higher up.

The finite real-zero theorem should therefore be removed from the live proof frontier, not left as an unproved final lemma.
