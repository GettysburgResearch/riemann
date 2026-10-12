# Optimized count primitive and strip-aware displacement payment

Status: proposed complete-source corollary of the separately frozen
DOUBLE_COUNT_PICK.md, pending independent review. No original packet is changed.
Scope: global complete xi Pick positivity on arbitrary distinct positive
nodes through order 1,414,000 using the classical strip. With the additional
uniform strip hypothesis `|Re rho_s-1/2|<=3/8` for all nontrivial zeta zeros,
the same proof gives order 1,480,000. Both remain finite-order results;
RH is open.
Exact dependencies: [DOUBLE_COUNT_PICK.md](../DOUBLE_COUNT_PICK.md), exact
SHA-256 `23e67ff10510aa7b27b497cd58e7e8a6f1a874c1fe3a9099ba5b7651df7a74b0`;
its complete node/source/rational-class, Gamma, Turing-integral, good-cutoff,
density and published critical-line census inputs remain unchanged. The
optional `3/8` strip can be supplied by the separately imported September
30 quasi-RH theorem identified at its frozen source in
[PRIMARY_SOURCES.md](../../literature/PRIMARY_SOURCES.md); its analytic proof
and formal solution closure are not rebuilt here. The classical-strip
result has no quasi-RH theorem dependency.
What was run: exact rational controls for the sharper count-primitive
coefficient, uniform arbitrary-displacement amplification and full-source
gaps in verify_optimized_double_count.py, normal and optimized Python.
Smallest remaining gap: independent review of this new composition.

## ODC1. The accumulated theta term fits inside the existing constant

Keep `H0=3000000000000`, the node-independent good cutoff `T>=H0` with
`Delta(T)=0`, and `A_T(t)=integral_T^t Delta(u)du`. From B1–B8 of the
frozen packet, for `t>=T`,

\[
 |A_T(t)|\le a+b\log t+d\log(t/T),
 \quad a=2067/1000,\ b=59/1000,\ d=1/141.
\tag{ODC1}
\]

Let `L=28729/1000<log H0` and `c0=a/L=2067/28729`.
The exact inequality `d<c0` gives

\[
 a+d\log(t/T)<c_0\log T+c_0\log(t/T)=c_0\log t.
\tag{ODC2}
\]

The first comparison is strict since `a<c0*log T`; the second is valid
because `log(t/T)>=0`. Thus, uniformly at every such T and t,

\[
 \boxed{|A_T(t)|<c_A'\log t,
 \quad c_A'=59/1000+2067/28729=3762011/28729000.}
\tag{ODC3}
\]

This bound includes `t=T`, where the primitive is zero. It pays the
accumulated theta error from the constant allowance already present in
ODC1, without adding `1/141` to the logarithmic coefficient. Equivalently,
dividing ODC1 by `log t` writes the two terms after b as a convex combination
of `a/log T` and d; both are below c0.

The native Gamma remainder, including its explicit `-1/(360z^3)` term,
is exactly the frozen B1–B6 proof. No stronger Stirling expansion or new
external count estimate is assumed.

## ODC2. Twice-integrated quadrature and a supplied strip depth

Keep every complete-source convention and unshifted derivative norm in
B7–B11, with

\[
 q=n^2/T,\quad n\ge850000,\quad d_0=3191/5000,
 \quad C_1=6383/10000,\quad C_2=2037/5000,
 \quad C=C_2+C_1^2.
\]

Twice integrating by parts at the good cutoff gives the same vanishing
endpoint terms. Replacing only the primitive coefficient in B11 yields

\[
 \left|2\int_{(T,\infty)} |R|^2d\Delta\right|
 <J' q^2B_R,\qquad
 \boxed{J'=4c_A'C=306538772327579/718225000000000.}
\tag{ODC4}
\]

This holds for every original complex proper rational numerator. With the
unchanged density constants

`m*=(113/355)(1-1838/28729)` and `U*=106/333`,

the complete real-height reserve is `(m*-J'q^2)B_R` and the sampling upper
bound is `(U*+J'q^2)B_R`. The original convergence and count conventions,
including the cutoff atom in the below-or-at-T part, remain essential.

Now let the complete source have independently varying actual vertical
rational displacements `|a_b|<=A<=1/2`. Retain the strip depth in the V5
amplification bound rather than substituting 1/2 early:

\[
 \kappa>\exp[2A(d_0+2/n)q].
\tag{ODC5}
\]

The original prefactor control and discrete Minkowski series prove this
uniformly in the independently chosen paths `tau*a_b`. The original
bounds for `B`, `DB`, `R'` and `R''` remain valid because `A<=1/2`.
The complete product-rule bound is therefore

\[
 \sum w_\alpha |(R_+R_-)''(b_\alpha+i a_\alpha)|
 \le2C\kappa^2q^2(U_*+J'q^2)B.
\tag{ODC6}
\]

Conjugate source groups cancel the first imaginary Taylor term. Its
integral remainder contributes the factor `A^2/2`, so the full loss is
`A^2 C kappa^2 q^2(U*+J'q^2)B`. All source multiplicities, both signed-pole
classes and both reflected upper members of each nonreal quartet remain
included. Constant displacement, finite root selection and a truncated
Taylor series are not hypotheses.

Consequently the complete-source quadratic form is strictly positive if

\[
 G_A(q)=m_*-J'q^2
       -A^2C\kappa^2q^2(U_*+J'q^2)>0.
\tag{ODC7}
\]

For fixed A and kappa, this decreases with `q>=0`. The endpoint gap pays
every allowed q. The following two exact choices satisfy ODC5 and ODC7
uniformly for `n>=850000`:

| Complete displacement bound A | q0 | kappa | Exponent upper | Exact endpoint gap |
| --- | --- | --- | --- | --- |
| 1/2 | 667/1000 | 1531/1000 | 4257/10000 | 762345376598329967484512648703103327298527 / 6792397470000000000000000000000000000000000000 |
| 3/8 | 731/1000 | 71/50 | 7/20 | 73091897928132099409751855017013608382087 / 30188433200000000000000000000000000000000000 |

The exponent upper bounds are strict; rational exponential Taylor sums
with complete geometric tails prove `exp(exponent upper)<kappa`.
The positive endpoint gaps are approximately `0.0001122351` and
`0.0024211889`, respectively. Only their exact rational values are guards.

## ODC3. Finite global and selectable-cutoff consequences

At any node-independent good cutoff `T>=H0`, the complete tail is strictly
positive on any even `n>=850000` distinct positive nodes satisfying

\[
 1000n^2\le667T\quad(A=1/2),\qquad
 1000n^2\le731T\quad(A\le3/8).
\tag{ODC8}
\]

Principal submatrices cover all smaller sizes. Cofinal good-cutoff
existence supplies selectable tail orders
`sqrt(667T/1000)+O(1)` or, with the narrower complete strip,
`sqrt(731T/1000)+O(1)`. These concern changing tail kernels.

For the full global kernel, the frozen cutoff theorem gives one common
`T* in [H0,H0+20]`, independent of all nodes. The imported published
critical-line verification reaches `3000175332800>H0+20`, so the complete
below-or-at-T* source is nonnegative. The exact inequalities

`1000*(1414000)^2<667*H0` and
`1000*(1480000)^2<731*H0`

pay the two global headline orders. At H0, the largest even orders under
ODC8 are respectively **1,414,566** and **1,480,878**. The classical result
is unconditional relative to the same explicitly named classical/published
imports as DOUBLE_COUNT_PICK.md. The second also needs an independently
supplied complete `3/8` displacement bound. Supplying a finite census or an
average zero-density statement would not supply that uniform strip.

This corollary has no all-order full-kernel conclusion and no RH conclusion.
A future integration would require its own exact-commit review.
