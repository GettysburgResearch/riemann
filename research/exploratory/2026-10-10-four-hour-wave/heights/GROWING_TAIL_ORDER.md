# The complete high-height source has cofinally growing Pick order

Status: analytic consequence of the reviewed annular frame, with the same
explicitly imported classical source and published argument-count inputs.
No critical-line census is used in this tail theorem. RH remains unproved.

## 1. Statement

Set `H0=3*10^12`. For `T>=H0`, define the complete height-tail kernel

\[
 K_{>T}(x,y)=\sum_{b_\alpha>T}
 w_\alpha\frac{s_\alpha+xy}{(x^2+s_\alpha)(y^2+s_\alpha)}.
 \tag{G1}
\]

The source conventions are those of
[ANNULAR_GLOBAL_PICK.md](ANNULAR_GLOBAL_PICK.md): a critical pair contributes
`s=b^2,w=2m`; an off-line quartet contributes the two conjugate squared poles
`s=b^2-a^2 +/- 2iab`, each with `w=2m`. The classical strip gives
`0<=a<=1/2`. The condition `b>T` includes or excludes whole conjugate groups.
The locally normal source identity and absolute entrywise convergence are
imported classical facts, not established by finite arithmetic here.

For every even integer `n>=256` satisfying

\[
                     14n^3\le T, \tag{G2}
\]

the matrix `[K_{>T}(x_i,x_j)]` is positive definite at every set of `n`
distinct positive nodes. It is positive semidefinite through order `n` when
nodes may repeat. In particular, if

\[
 n(T)=\max\{n\in 2\mathbb N:14n^3\le T\},
 \tag{G3}
\]

then the certified tail order is cofinal, with
`n(T)=(T/14)^(1/3)+O(1)`.

This theorem constrains the complete source above increasing heights. It does
not certify growing order for the full kernel: the source below `T` must
also be controlled to draw that conclusion. In particular no RH deduction
follows by sending `T` to infinity in different tail kernels.

## 2. Count input and endpoint conventions

The only published quantitative input needed here is the Trudgian (2014)
argument bound, as source-qualified in the preceding packet. Together with
the elementary explicit theta/Stirling estimate, it gives

\[
 |N_+(u)-\mathcal M(u)|<\tfrac14\log u\quad(u\ge H_0),
 \qquad \mathcal M'(u)=\frac1{2\pi}\log\frac{u}{2\pi}. \tag{G4}
\]

`N_+(u)` is the right-continuous count of all upper-half-plane zeros through
height `u`, with multiplicity. The bound at zero ordinates means the bound
obtained from one-sided nonzero-ordinate limits. Stieltjes measures therefore
count exactly `(L,rL]`, including any atom at the right endpoint and excluding
any atom at the left endpoint. The error bound is applied to those same
one-sided values in integration by parts. `H0` is merely a convenient numeric
threshold for the logarithmic estimates in this theorem. The published
verified critical-line height is not an input to (G1)--(G3).

## 3. Uniform annular reduction

For a fixed `n` satisfying (G2), put

\[
 r=1+\frac1{2n},\qquad L_k=Tr^k,\qquad
 h=\frac1{2n}+\frac1{8n^2}.
\]

The disjoint annuli `(L_k,rL_k]` partition the entire source in (G1).
On each one `n^3/L_k<=1/14` and `L_k>=H0`. Use the exact arbitrary-node
congruence from the preceding packet, normalized with
`rho_i=x_i^2/L_k^2` and

\[
 \phi(z)=\frac{\prod_i(1+\rho_i)}{\prod_i(\rho_i+z)},
 \qquad\psi_j(z)=z^j\phi(z),\quad j=0,1.
\]

The two blocks have polynomial degree at most `d=n/2-1` and quadratic forms
`sum w psi_j(s/L_k^2) P(s/L_k^2)^2`. Their real-height reference uses
`v=b^2/L_k^2 in [1,r^2]` and exactly the measure `2 dN_+(b)`.
The actual displacement is `z-v=-a^2/L_k^2+2iab/L_k^2`.

The Legendre derivative identity and two-endpoint Gram calculation of
[L2_FRAME_REFINEMENT.md](L2_FRAME_REFINEMENT.md), section 2, hold for every
degree. Thus its annular domination proof applies whenever the scalar
guards below hold; it has no inherent restriction `n<=6000`.

## 4. Guards for all orders, without a finite-range extrapolation

Write `u=1/n`, so `0<u<=1/256`. The normalized weighted variation coefficient
is exactly the positive-coefficient polynomial

\[
 (1+u/2)^2\left(\frac38+\frac u4+\frac{u^2}2
                         +\frac{5u^3}8+\frac{u^4}8\right).
 \tag{G5}
\]

It is increasing in `u`, and its value at `u=1/256` is less than `49/128`.
Consequently the correlated endpoint-plus-variation bound is valid at every
`n>=256`. The unweighted bound `3/8+1/(4n)<=49/128` is smaller.
The real weight lower bound `psi_j>4/11` holds for every positive `n`, since
`r^(2n)<e<11/4`.

All the remaining guards have explicit monotone worst cases:

\[
\begin{split}
 &\frac16+\frac{441}{1024}\frac{n^3}{L}
       \le\frac16+\frac{441}{14336}<\frac15,\\
 &D_P\le n^3/4,\quad
   D_P|z-v|\le\frac{5n^3}{16L}\le\frac5{224}<\frac1{32},\\
 &nA^2/L^2\le\frac1{56\cdot256^2H_0}<\frac1{17},\\
 &r^2+5/(4L)\le(1+1/512)^2+5/(4H_0)<4/3,\\
 &2(1+1/n)(17/16)\le2(1+1/256)(17/16)<3,\\
 &2(1+1/n)(1+2/n)(17/16)^2
       \le2(1+1/256)(1+2/256)(17/16)^2<4,\\
 &4/n^4+3/n^2+1/2\le4/256^4+3/256^2+1/2<9/16.
\end{split} \tag{G6}
\]

Here `A<=1/2`, `L>=T`, and the third line follows from
`n/L^2=(n^3/L)/(n^2L)`. The elementary exponential rounding
`exp(1/32)<32/31<17/16` and count-density inequality
`6400/57568>1/9` are the same as in the reviewed frame. These guards retain
the sampling constant `1/5`, the complex Taylor constant `17/16`, and
`|psi|<=2, |psi'|<=3n, |psi''|<=4n^2` uniformly in arbitrary node scales.

## 5. Strict domination and complete summation

The reviewed frame proof gives a main reserve
`(4/99)Lh logL Q`, `Q=int[-1,1] R(t)^2 dt>0`, and bounds its relative
quadrature plus strip losses by

\[
 \mathcal R_*(n,A,L)=
 \frac{43659}{4096}\frac{n^3}{L}
 +\frac{1287495}{131072}A^2\frac{n^6}{L^2}
 +\frac{99}{20}A^2\frac{n^3+3n}{L^2}. \tag{G7}
\]

Under (G2), its uniform upper bound is

\[
 \mathcal R_*
 \le\frac{43659}{57344}
   +\frac{1287495}{102760448}
   +\frac{99}{1120H_0}\left(1+\frac3{256^2}\right)
 <\frac45. \tag{G8}
\]

The middle denominator is `131072*4*14^2`. The replay verifies (G8) as an
exact rational inequality. Every nonzero polynomial quadratic form in both
moment blocks is therefore strictly positive on every complete annulus.
The exact invertible node congruence proves annular positive definiteness.

Absolute entrywise convergence passes the positive semidefinite inequalities
from finite annular sums to the complete tail. The first annulus is already
positive definite, so the complete sum is positive definite at distinct
nodes. For fewer distinct nodes, append positive nodes to reach size `n` and
take a principal submatrix. Repeated nodes are obtained by continuity.
This proves (G1)--(G3).

## 6. Replay scope

[verify_growing_tail.py](verify_growing_tail.py) checks the exact worst-case
inequalities (G5)--(G8), checks positivity of the coefficients establishing
the monotone variation bound, and gives sample integer orders from (G3).
These are uniform algebraic guards, rather than a finite loop promoted to an
all-order proof. The published count input, classical source identities,
analytic congruence, and analytic Taylor/Legendre estimates remain imported
or proven in the cited packet; the checker does not rerun a zero census.
