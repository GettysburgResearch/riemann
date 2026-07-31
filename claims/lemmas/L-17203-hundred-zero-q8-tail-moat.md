# L-17203 — A hundred-zero directed refinement of the `q=8` raw moat

Claim ID: `L-17203`  
Title: The exact ten-notch `q=8` filter has raw RH moat `3.5*10^-26` for `x>=18`  
Status: `PROPOSED`  
Authoring agent: `gpt56-172n-01/hundred_zero_refine`  
Reviewing agents: independent adversarial subagent audit completed; repository review pending  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: `L-17201`, `L-17202`, the raw smoothed von Mangoldt explicit formula in `T-15404`, the Hadamard product for `xi`, and Arb/FLINT certified zero counts  
Certificate: `X-17204`  
Scope: issue #172, negative route  
Related counterexample candidates: none

## Statement

Let `G_0` be the exact rational ten-notch filter of `L-17201` and let

\[
 G_8=(I-\tfrac18\tau_{(6/5)\log2})
     (I-\tfrac18\tau_{(2/3)\log2})G_0
\tag{L-17203.1}
\]

be the two-trivial-zero-annihilator filter of `L-17202`.  For

\[
 Q_{G_8}(x)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                   G_8(x-\log n),
\tag{L-17203.2}
\]

RH and the inherited explicit-formula normalization imply

\[
 \boxed{|Q_{G_8}(x)|<3.5\,10^{-26}\qquad(x\ge18).}
\tag{L-17203.3}
\]

This is a directed tail-domain constant for the raw statistic.  It is not an
all-real startup bound and no violating support is asserted.

## Exact transform and inherited safety

With

\[
 B_r(z)=\frac{1-e^{-rz}}{rz},\qquad
 \mathcal R=\{1/2,1/4,1/8,1/16,r_1,\ldots,r_{10}\},
\]

where the `r_j` are the exact decimal rationals in `L-17201`, put

\[
 \Phi(z)=e^{-z}\prod_{r\in\mathcal R}B_r(z),
\]

\[
 \widehat G_8(z)=\Phi(z)^2(1-2e^{-(\log4)z})
 \left(1-\tfrac18e^{-((6/5)\log2)z}\right)
 \left(1-\tfrac18e^{-((2/3)\log2)z}\right).
\tag{L-17203.4}
\]

The dependency hashes in `X-17204` freeze those rational widths and the two
annihilators.  The strip-safety, pole cancellation, support bound

\[
 b_8:=\sup\operatorname{supp}G_8<\frac{6499}{600},
 \qquad \|G_8\|_1\le\frac{243}{64},
\tag{L-17203.5}
\]

and exact annihilation at `-5/2` and `-9/2` are inherited from `L-17202`.

## Certified first-hundred census

At 320-bit precision, Arb constructed `zeta_zero(j)` for every
`1<=j<=100`.  For the full ordinate ball `Gamma_j`, `X-17204` formed

\[
 I_j=\Gamma_j+[-10^{-70},10^{-70}]
\]

and certified that the cumulative positive-ordinate count at the lower and
upper endpoints of `I_j` is respectively `j-1` and `j`.  The intervals are
strictly ordered and disjoint.  It also certified

\[
 N(237)=100.
\tag{L-17203.6}
\]

Thus the balls give a multiplicity-exact census of every positive ordinate
below 237.  The verifier directly ball-evaluated (L-17203.4), without replacing
any ordinate by a floating midpoint, and obtained

\[
 L_{100}:=2\sum_{j=1}^{100}|\widehat G_8(i\gamma_j)|
 \in 3.47779083534058809995433344924\,10^{-26}
      \;\mathbin{+/-}\;2.08\,10^{-117}.
\tag{L-17203.7}
\]

The factor two includes the conjugate ordinates.

## Positive Hadamard remainder and the unlisted line tail

Under RH, the Hadamard identity used in `L-17201` becomes the positive sum

\[
 C_\xi:=2+\gamma_{\rm Euler}-\log(4\pi)
       =\sum_\rho\frac1{\gamma^2+1/4}.
\tag{L-17203.8}
\]

As recorded in `L-17201`, `zeta(s)<0` for `0<s<1`; hence there is no
nontrivial zero with `gamma=0`, so the positive conjugate-pair partition used
here exhausts (L-17203.8).

Arb subtracted the first hundred certified conjugate-pair masses from the
ball for `C_xi`, giving

\[
 R_{100}:=C_\xi-
   2\sum_{j=1}^{100}\frac1{\gamma_j^2+1/4}
 \in 0.00622171312439445702801959536094
      \;\mathbin{+/-}\;5.24\,10^{-95}.
\tag{L-17203.9}
\]

Write `P=product_(r in R) r`.  For real `t` with `|t|>=237`, all fourteen
box power bounds are active.  Equation (L-17202.9) therefore gives

\[
 |\widehat G_8(it)|\le
 C_8|t|^{-28},\qquad
 C_8=\frac{81}{64}\frac{3\,4^{14}}{P^2}.
\tag{L-17203.10}
\]

For `|gamma|>=237`,

\[
 \gamma^{-2}\le
 \left(1+\frac1{4\cdot237^2}\right)
 \frac1{\gamma^2+1/4}.
\]

Consequently the entire unlisted nontrivial-zero contribution is at most

\[
 C_8\,237^{-26}
 \left(1+\frac1{4\cdot237^2}\right)R_{100}
 \in 1.83517205593595053987711040773\,10^{-35}
      \;\mathbin{+/-}\;5.81\,10^{-128}.
\tag{L-17203.11}
\]

Combining (L-17203.7) and (L-17203.11), Arb encloses the complete nontrivial
line sum by

\[
 B_{\rm line}
 \in 3.47779083717576015589028398911\,10^{-26}
      \;\mathbin{+/-}\;6.40\,10^{-118}
 <3.49\,10^{-26}.
\tag{L-17203.12}
\]

## Directed trivial-zero remainder at `x=18`

Let `lambda_m=2m+1/2`.  The first two terms vanish exactly.  Arb directly
evaluated the next three fixed terms at `x=18`:

| `m` | `lambda_m` | enclosure of `e^(-18 lambda_m)|G8hat(-lambda_m)|` |
|---:|---:|---:|
| 3 | `13/2` | `3.47981964764107646742799907111e-30 +/- 9.19e-124` |
| 4 | `17/2` | `4.18532449004541060243350941316e-38 +/- 1.25e-131` |
| 5 | `21/2` | `5.78226324973072658768279118034e-46 +/- 4.56e-139` |

Their sum is enclosed by

\[
 B_{3:5}(18)\in
 3.47981968949432194610843006852\,10^{-30}
 \;\mathbin{+/-}\;7.45\,10^{-124}.
\tag{L-17203.13}
\]

For `x>=18`, (L-17203.5) gives `x-b_8>4301/600`.  Hence the remaining
trivial zeros satisfy

\[
\begin{aligned}
 B_{\ge6}(x)
 &\le \frac{243}{64}
 \frac{\exp(-(25/2)(4301/600))}
      {1-\exp(-2(4301/600))}\\
 &\in 4.62201572436467770041296842849\,10^{-39}
      \;\mathbin{+/-}\;7.47\,10^{-133}.
\end{aligned}
\tag{L-17203.14}
\]

The three direct terms and this geometric majorant decrease with `x`.
For `x>b_8`, the inherited explicit formula has no endpoint term, its pole
term is canceled, and only the nontrivial and trivial-zero sums remain.
Equations (L-17203.12)--(L-17203.14) give the retained complete enclosure

\[
 |Q_{G_8}(x)|\le
 3.47813881914517178965733129989\,10^{-26}
 \;\mathbin{+/-}\;8.66\,10^{-118}
 <3.5\,10^{-26},
\]

which proves (L-17203.3), conditional on the stated dependencies.

## Certification boundary

- All one hundred zero balls, all one hundred count jumps, `N(237)=100`, and
  every displayed analytic ball were produced by one Arb/FLINT backend.
- Exact rational checks freeze the inherited certificates and replay the
  support, `L1`, line-factor, and tail constants before Arb is loaded.
- The raw smoothed explicit-formula normalization remains the source-level
  dependency identified in `L-17201/T-15404`.
- This claim is therefore `PROPOSED`, not independently reproduced.
- No exact sign-separated prime support and no RH contradiction are claimed.
