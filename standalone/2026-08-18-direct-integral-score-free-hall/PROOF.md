# A self-contained proof candidate for RH by score-free Hall, direct integration, and factor-67 recursion

## Abstract

We construct, for every sufficiently large `X`, one nonnegative finite row whose ordinary and radix-four carry responses lie under the exact native capacities and whose literal entropy score is at least `4sqrt(X)-O(log X)`. The proof uses only the compact `P_61` Hall problem, a two-sort separation of target source and row bonus, an exact residual-only causal identity, positive direct endpoint integration, a single scalar safety thinning, and a subcritical actual-mass recursion. The formerly used false identity equating the complete parabolic score loss with radix-four slack is rejected. The endpoint conclusion follows from the direct score lower bound.

This document is written as a complete proof candidate. It is not an accepted proof and should be read adversarially.

## 1. Definitions

The definitions and full theorem statements are in `L-99020` through `L-99025`. The details below close the interfaces most likely to hide a normalization or ownership error.

### 1.1 Parabolic component row

For real `Y>=1` define

\[
S_Y(n)=\sum_{m\ge n,\,m\le Y}\frac1{\sqrt m}\log\frac Ym
\]

and

\[
Q_Y(j)=(j+1)\Delta_j^2\left[\frac{S_Y(j)}{j-1}\right],
\qquad j\ge2.
\]

Expanding the second difference gives

\[
Q_Y(j)=
\frac{j+1}{j-1}[h_Y(j)-h_Y(j+1)]
+
\frac{2(j+1)}{j(j-1)}h_Y(j+1)
+
\frac2{j(j-1)}\sum_{m\ge j+2}h_Y(m),
\]

where `h_Y(m)=m^{-1/2}log(Y/m)` on `m<=Y` and zero otherwise. Every term is nonnegative. Differentiation on an activation cell proves `Q_Y(j)` is nondecreasing in `Y`.

The ordinary response is

\[
C_Y(q)=q^{-1/2}H(Y/q),
\qquad
H(Z)=\sum_{m\le Z}m^{-1/2}\log(Z/m),
\]

and the detail response

\[
\Theta_Y(q)=q^{-1/2}[H(Y/q)-H(Y/(4q))]
\]

is nonnegative and nondecreasing in `Y` because

\[
\frac d{dZ}[H(Z)-H(Z/4)]
=Z^{-1}\sum_{Z/4<m\le Z}m^{-1/2}\ge0.
\]

### 1.2 Compact Hall

The proof of `L-99020` is finite. The checker evaluates the active odd thresholds and the normalized-row gates with outward rational enclosures. The analytic tail of the profile derivative follows from the displayed lattice-ramp lower bound. Hall's theorem then gives the flow. Equation `L-99020.4` is obtained by substituting `T_e=u_e+sum_o t(o,e)` and `T_o=sum_e t(o,e)`.

The score ratio is decreasing, so declared score is retained only on the residual-source sort. The row profile is increasing, so the row edge term is nonnegative. This is the precise type separation that removes the PR #499 contradiction.

### 1.3 Causal identity and literal score

Equation `L-99021.1` follows by collecting the parent coefficient and each child coefficient. Since every physical row coordinate is linear, the identity holds simultaneously in literal entropy. No source-declared score is substituted for literal entropy.

For the backup inequality `L-99021.5`, put

\[
A_N=\sum_{2\le m\le N}\frac{\log m}{\sqrt m}.
\]

On joint activation cells, differentiation gives

\[
D_p'(Y)=
\frac{A_{\lfloor Y\rfloor}-p^{-1/2}A_{\lfloor Y/p\rfloor}}Y
-
\frac5{2\sqrt Y}(1-p^{-1}).
\]

Because `p>=67`, the first numerator contains the complete interval `Y/4<m<=Y`. Since `log(t)/sqrt(t)` decreases for `t>=e^2`,

\[
A_{\lfloor Y\rfloor}-A_{\lfloor Y/p\rfloor}
\ge(3Y/4-1)\frac{\log Y}{\sqrt Y}.
\]

Thus `D_p'(Y)>0` for `Y>=67`. At `Y=p`,

\[
D_p(p)=E(p)-5\sqrt p+3+2p^{-1/2}.
\]

On each cell its derivative is positive for `N>=67`; the directed base enclosure in the checker gives `D_67(67)>1.52`. This proves the backup inequality.

### 1.4 Positive direct integration and finite compression

For fixed `X`, every physical row has support in `2<=j<=X`; every ordinary and detail vector has support in `2<=q<=X`; and only finitely many rough-prime and boundary labels are active. Hence the complete feature map is finite dimensional. Coordinatewise integration of nonnegative row vectors gives a nonnegative row directly.

Normalize the finite measure to a probability measure. Its feature average lies in the compact convex hull of the feature range. The convex Caratheodory theorem gives a representation by at most `D+1` atoms in `R^D`; multiplying the weights by the total mass recovers the original integral. Adding one indicator coordinate per discrete label class preserves every label mass. Thus optional finite compression is exact and introduces no B-spline collar or interpolation error.

### 1.5 All-column estimate

The adjacent error estimate follows from the exact factor-67 Euler remainder constant

\[
C_{67}=\sum_{k\le67}\frac{|\mu(k)|}{\sqrt k}
\left(1+\frac12\log\frac{67}k\right)<19.
\]

Summing `n^{-3/2}` over the multiples of `q` beginning at `K` gives `L-99023.2`. Division by the exact detail target gives `L-99023.3`. The single thinning then leaves strict reserve. The terminal derivative calculation uses only the possible quotients `1,2,3`; integrating the omitted width `10000` gives the stated lower response. With no B-spline collar, the only terminal adverse term is the finite Euler mismatch.

### 1.6 All-depth sourcewise score telescope

Before safety operations, Hall and causal splitting are exact physical-row identities. Direct integration and optional convex compression are exact. The only arithmetic score-realization issue occurs when a fixed `P_61` source coefficient reaches its terminal quotient below `67`.

For each `d|P_61`, the quotients `X/(d67^j)` have one and only one terminal layer. Every nonterminal literal entropy difference dominates the matching declared-score difference. The complete debt therefore telescopes to the single terminal layer. The terminal debt is at most twice its target. Summing over the fixed Euler support gives

\[
2(4\sqrt{67}-3)\prod_{p\le61}(1+p^{-1/2})<3600.
\]

The direct-integral construction has no quantization score loss. The common thinning costs less than `96sqrt(67)`, and the fixed top/base packets cost one absolute constant. Consequently

\[
\mathcal H(d_X)\ge4\sqrt X-C_*.
\]

The one-eighth child-mass theorem guarantees convergence and source ownership; it is not used as a proxy for signed loss.

### 1.7 Parabolic score and endpoint theorem

Monotonicity of `f_X=b_X/x`, followed by the elementary logarithmic remainder bound, gives

\[
J_\Lambda(X)<4\sqrt X+4\log X.
\]

Feasibility gives `H(d)<=P_Lambda`, so `F_Lambda<=J-H`. The prime-square asymptotic follows by isolating `p^2`, applying ordinary partial summation and the prime number theorem, and bounding powers `p^r`, `r>=3`, absolutely. The constant is `(-1-zeta(1/2))/4>0`.

Finally, finite Fubini gives the Mellin transform of the prime endpoint. Every off-line zero gives a nonreal pole, and the compact numerator is nonzero there. Landau's theorem says an eventually nonnegative function cannot have its first singularity only off the real axis. Eventual negativity of the prime endpoint therefore excludes every off-line zero. The functional equation completes RH.

## 2. No-RH-input audit

The construction uses no RH, GRH, square-root Mertens estimate, power-saving PNT error, CPBD, generic large-sieve alignment, zero-density theorem, or `J_Lambda-4sqrt(X)=O(log X)` assumption. The only PNT use is the classical qualitative theorem in the proper-prime-power asymptotic.

## 3. Status

This is a complete proof candidate. Every named lemma is stated and argued in the packet, and every finite compact gate is replayable. Because the result would settle RH, the correct status before hostile independent reconstruction is **proposed, not accepted**.
