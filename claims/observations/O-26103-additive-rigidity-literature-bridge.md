# O-26103 — Literature bridge to additive-function logarithm rigidity

Observation ID: `O-26103`  
Title: The transverse part of the Annular Dual Frame theorem is a finite quantitative Erdős logarithm-rigidity problem  
Status: **LITERATURE CONNECTION / PROPOSED ADAPTATION — NOT A PROOF OF `ADF`**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #261  
Depends on: `O-26102`, `L-26107`

## 1. Classical qualitative theorem

Erdős proved in

> P. Erdős, *On the distribution function of additive functions*, Ann. of Math. 47 (1946), 1–20,

that a real-valued additive arithmetic function satisfying

\[
 f(n+1)-f(n)\longrightarrow0
\]

must be

\[
 f(n)=c\log n
\]

for one real constant `c`.

Kátai and Wirsing later weakened the gap hypotheses, including averaged formulations. Mauclaire's 1999 characterization paper gives a concise historical account and further arithmetic-progression variants.

This is exactly the qualitative rigidity suggested by the annular dual denominator.

## 2. Quantitative modern input

A. P. Mangerel,

> *Additive functions in short intervals, gaps and a conjecture of Erdős*, Ramanujan J. 59 (2022), 1023–1090; arXiv:2108.12351,

proves quantitative local-to-global results for additive functions. Relevant features include:

1. savings in first or second moments of consecutive gaps force savings in corresponding centred moments;
2. under stated regularity hypotheses, almost-everywhere monotonicity makes an additive function close to a slowly varying multiple of `log n`;
3. the approximation is expressed in a prime-power coefficient metric, the same natural metric in which the annular source vector `lambda_(p^a)` lives.

The paper builds on earlier gap and rigidity work of Elliott, Hildebrand, Kátai, Wirsing, and Ruzsa.

## 3. Exact match to the repository coordinate

For

\[
 L_\lambda(n)=\sum_{p^a\mid n}\lambda_{p^a},
\]

`L-26105/O-26102` give

\[
 (A_X^*\lambda)_j
 =2L_\lambda(j)-L_\lambda(j-1)-L_\lambda(j+1).
\]

`L-26107` converts this second-difference energy into:

- an `L^2` bound for the consecutive gaps;
- exact dyadic and triadic scaling identities;
- the characteristic relations `h(n) approximately 2h(2n)` and `h(n) approximately 3h(3n)`.

Thus the transverse `ADF` problem has the same geometry as quantitative logarithm rigidity, but in a finite, source-dependent annulus.

## 4. Why the published theorems do not close `ADF` automatically

The existing results do not directly provide the required inequality because:

1. `L_lambda` depends on `X`;
2. only one fixed annulus is controlled, not all integers up to `X`;
3. the available norm is a second-difference norm, not initially a first-gap norm;
4. `ADF` needs a source-pairing estimate with an explicit `X^(o(1))` constant;
5. the logarithmic component is RH-bearing and must remain signed rather than be bounded by an absolute centred moment.

A valid adaptation must therefore be quantitative and finite-scale. It should use `L-26107` to enter the gap-rigidity machinery, extract

\[
 \lambda=c\Lambda+\lambda^\perp,
\]

and control only the transverse source pairing by curvature. The scalar `c Lambda` component must be sent to the factor-two recurrence rather than absorbed into a generic rigidity estimate.

## 5. Proposed adaptation target

The desired finite theorem is:

\[
\boxed{
 |\langle\lambda^\perp,r_X\rangle|
 \le X^{o(1)}\|A_X^*\lambda\|_2,
}
\]

where `lambda^perp` is the prime-power coefficient error after subtracting the optimal nonnegative multiple of `Lambda`.

The classical rigidity theorems strongly suggest that `Lambda` is the only genuine near-null direction. `L-26107` supplies the exact extra dilation identities that a finite quantitative proof can exploit.

## 6. Proof boundary

This observation identifies a mature literature and a concrete adaptation route. It does not claim that the hypotheses or constants of any cited theorem already imply `ADF`, the scalar recurrence, or RH.