# L-15608 — Weighted-deficit trace-tail identity

Claim ID: `L-15608`  
Title: The scalar leverage deficit is exactly the uncaptured trace of a positive localization operator  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-d`  
Created: 2026-07-31  
Dependencies: `L-15607`; trace-class localization operators; Ky Fan principle  
Scope: optimal packet construction for the scalar capacity certificate

## Deficit operator

Use the setting of `L-15607`.  Fix a real level `G` and put

\[
 w_G(\xi)=(G-s(\xi))_+.
 \tag{L-15608.1}
\]

Assume `w_G` is integrable, or use a finite directed cover plus a separately
certified zero tail.  Define the positive trace-class operator

\[
 T_G
 =P_I\mathcal F^{-1}w_G\mathcal F P_I
 \tag{L-15608.2}
\]

with the Fourier normalization of `L-15607`.

Let `L` be a finite-dimensional packet with orthogonal projection `P_L`.

## Exact trace identity

The leverage deficit of `L-15607` satisfies

\[
 \boxed{
 \mathfrak D_L(G)
 =\operatorname{Tr}\bigl((I-P_L)T_G\bigr).}
 \tag{L-15608.3}
\]

### Proof

For each frequency, the rank-one plane-wave kernel gives

\[
 \operatorname{Tr}T_G
 =\frac1{2\pi}\int_I\int_{\mathbb R}w_G(\xi)\,d\xi\,dx
 =\int\frac{|I|}{2\pi}w_G(\xi)\,d\xi.
\]

For any orthonormal basis `k_1,...,k_d` of `L`,

\[
 \operatorname{Tr}(P_LT_G)
 =\sum_{j=1}^d\langle T_Gk_j,k_j\rangle
 =\int\frac1{2\pi}
   \sum_{j=1}^d|\widehat{k_j}(\xi)|^2w_G(\xi)\,d\xi.
\]

Subtracting and using the orthonormal form of the leverage function proves
(L-15608.3).  The general-basis identity follows from the exact Gram formula.
QED.

## Optimal unconstrained packet

Let

\[
 \theta_1\ge\theta_2\ge\cdots\ge0
 \tag{L-15608.4}
\]

be the eigenvalues of `T_G`, repeated with multiplicity.  Among all
`d`-dimensional packets,

\[
 \boxed{
 \inf_{\dim L=d}\mathfrak D_L(G)
 =\sum_{n>d}\theta_n.}
 \tag{L-15608.5}
\]

The optimum is attained by the span of the first `d` eigenvectors.

This is the Ky Fan maximum principle applied to

\[
 \operatorname{Tr}(P_LT_G).
\]

Consequently, an unconstrained `d`-packet can prove the saturation floor
`Gamma` whenever

\[
 \boxed{
 \sum_{n>d}\theta_n\le G-\Gamma.}
 \tag{L-15608.6}
\]

## Exact source constraints

Let `P_N` be the span of the first `N` eigenvectors of `T_G`, and impose `r`
linear source constraints.  Their common kernel inside `P_N` has dimension at
least

\[
 d=N-r.
\]

For any such kernel packet `L`,

\[
 \boxed{
 \mathfrak D_L(G)
 \le
 \sum_{n=1}^r\theta_n
 +\sum_{n>N}\theta_n.}
 \tag{L-15608.7}
\]

### Proof

The omitted subspace inside `P_N` has dimension at most `r`.  Its `T_G` trace is
at most the sum of the largest `r` eigenvalues.  The complete complement of
`P_N` contributes the tail sum.  Apply (L-15608.3).  QED.

This is a worst-case source-repair bound.  The actual constrained trace is
usually sharper and can be certified directly from a rational nullspace and the
finite matrix of `T_G`.

## Constraint-aware optimum

Let `Lambda:P_N->C^r` be the exact source-constraint map and let

\[
 L=\ker\Lambda.
\]

If `J` is any exact basis of this kernel and `M=J^*J`, then the captured deficit
trace is

\[
 \operatorname{Tr}
 \left(M^{-1}J^*T_GJ\right).
 \tag{L-15608.8}
\]

Therefore

\[
 \boxed{
 \mathfrak D_L(G)
 =\operatorname{Tr}T_G
 -\operatorname{Tr}
  \left(M^{-1}J^*T_GJ\right).}
 \tag{L-15608.9}
\]

Directed rational Loewner bounds for the two finite matrices give a proof-grade
constraint-aware deficit without relying on the worst-case top-`r` charge.

## Relationship to concentration and plunge counts

`T_G` is a weighted localization operator whose frequency weight is the actual
arithmetic symbol deficit, not merely an indicator of a bad set.  Indicator
majorants recover the multiband concentration operators of `L-14311` and the
plunge-width count of `L-15606`.

The weighted eigenvalue tail is strictly more informative:

- shallow deficit cells contribute proportionally less;
- deep cells determine the leading eigenvectors automatically;
- isolated narrow phase alignments have small trace cost;
- the scalar saturation condition is exactly a tail-sum inequality.

Recent trace and plunge estimates for localization operators may therefore be
applied directly once the arithmetic weight is enclosed by an admissible finite
union or layer-cake representation.

## Cofinal completion target

A sufficient scalar cofinal theorem is the existence of exact repaired packets
`L_j` and levels `G_j,Gamma_j` such that

\[
 \boxed{
 \operatorname{Tr}((I-P_{L_j})T_{G_j})
 \le G_j-\Gamma_j}
 \tag{L-15608.10}
\]

and the near-radical rates of `T-15602` hold.

Then `L-15607` proves exact count saturation, `T-15602` gives `F_j->0-`, and
RH follows.

The theorem isolates a genuine scalar object.  No production asymptotic bound
for (L-15608.10) is currently known.

## Proof boundary

- The trace identities and Ky Fan optimization are exact functional analysis.
- Exact source packets need not coincide with the unconstrained optimal
  eigenvectors.
- The worst-case source charge in (L-15608.7) may be too large; it is an upper
  bound, not an asymptotic claim.
- Applying recent localization trace theorems requires matching their geometry,
  normalization, and regularity assumptions.
- No RH proof is claimed without the cofinal weighted-tail estimate.
