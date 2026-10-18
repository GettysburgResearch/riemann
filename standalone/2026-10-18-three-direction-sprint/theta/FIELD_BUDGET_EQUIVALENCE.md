# In the ferromagnetic field class, the exterior budget controls reference variance

**Status: PROPOSED complete finite-model inequality and cofinal consumer.**
For the correlated real-field class of repository PR #1001, a uniformly
bounded exponential moment at any one height R>b is equivalent, at the
sequence level, to uniformly bounded zero-field reference variance.
This identifies the exact growth resource required by that class. It does
not construct the resource for actual theta approximants or prove a new
zero-free region.

Let a finite Ising graph have couplings J_e>=0, fields h_i and observable
`Y=sum_i w_i sigma_i`, w_i>=0. Put

\[
 |h_i|\le b w_i,\quad R>b,\quad E_hY=0,\qquad
 M_h(t)=E_he^{tY},\quad V_0=E_0Y^2. \tag{1}
\]

The mean condition holds in particular for every symmetric observable law.
The subscript0 denotes the **same graph, couplings and weights**, with
all fields set to zero. Then

\[
 \boxed{M_h(R)\ge M_h(b)M_0(R-b)\ge M_0(R-b).} \tag{2}
\]

Consequently a budget M_h(R)<=M implies

\[
 \boxed{V_0\le\frac{2(M-1)}{(R-b)^2}.} \tag{3}
\]

A slightly sharper form is V_0<=[arcosh(M)/(R-b)]^2. Thus there is no
sequence in this class having the required uniform exterior exponential
moment while its zero-field reference variance diverges.

## 1. Partition supermultiplicativity, with its correlation proof

Let Z(g) be the partition function with real field vector g. For u,v>=0,

\[
 Z(u+v)Z(0)\ge Z(u)Z(v). \tag{4}
\]

Indeed the mixed derivative of Q(s,t)=log Z(su+tv), for s,t in[0,1], is
`sum_(i,j)u_i v_j Cov_(su+tv)(sigma_i,sigma_j)>=0`. Integration over
the unit square gives (4).

Here is an elementary proof of the nonnegative covariances in precisely
the nonnegative-field regime just used. Take two independent spin
configurations sigma,tau from that law, and write
`p_i=(sigma_i+tau_i)/2`, `q_i=(sigma_i-tau_i)/2`. At each vertex the pair
(p_i,q_i) takes the four values (1,0),(-1,0),(0,1),(0,-1). The doubled
Gibbs weight is proportional to

\[
 \exp\left(2\sum_{ij}J_{ij}(p_ip_j+q_iq_j)
                         +2\sum_i g_i p_i\right). \tag{5}
\]

All coefficients in its absolutely convergent power-series expansion
are nonnegative when J,g>=0. Under the counting measure on the four
vertex values, every monomial in the p_i,q_i has nonnegative sum: a
positive odd exponent gives zero by sign symmetry, simultaneous positive
p and q exponents give zero, and surviving even exponents give positive
values. The same is therefore true after multiplying the expansion (5)
by q_i q_j. Since

\[
 \operatorname{Cov}(\sigma_i,\sigma_j)
       =\tfrac12 E[(\sigma_i-\tau_i)(\sigma_j-\tau_j)]
       =2E(q_iq_j),
\]

the covariance is nonnegative. Absolute convergence permits termwise
summation, since the graph is finite and all p,q are bounded. This is
the needed classical Griffiths/Kelly/Sherman duplication argument,
included to make (4) independent of an unproved correlation assertion.
Historical provenance: Kelly and Sherman, *General Griffiths' Inequalities
on Correlations in Ising Ferromagnets*, J. Math. Phys.9 (1968),466--484,
[DOI](https://doi.org/10.1063/1.1664600).

## 2. The exterior moment bounds the same graph at zero field

In (4) put

\[
 v=h+bw\ge0,\qquad u=(R-b)w\ge0.
\]

Then v+u=h+Rw, and division by Z(h)Z(0) gives the first inequality in
(2). Centering and Jensen give `M_h(b)>=exp(bE_hY)=1`, proving the
second. The zero-field law is symmetric, so

\[
 M_0(R-b)=E_0\cosh((R-b)Y)
       \ge1+\tfrac12(R-b)^2V_0,
\]

which proves (3). For the sharper version, u -> cosh(sqrt(u)) is convex
on u>=0 by its nonnegative-coefficient power series. Jensen therefore
gives `M_0(s)>=cosh(s sqrt(V_0))`.

## 3. The converse and its precise relationship to #1001

The converse sufficient estimate is already present in #1001 at
`f6beb3774ae7ff5eca4cb046786eae10e4f88abc`, strip/PROOF.md, S3b:

\[
 M_h(R)\le\exp\left[\tfrac12 V_0(b+R)^2\right]. \tag{6}
\]

For clarity its ingredients can be seen directly. Zero-field spin
reversal gives Z(h)>=Z(0) by Jensen. The nonnegative zero-field
spin-product expansion gives
`Z(h+Rw)<=Z(|h+Rw|)<=Z((b+R)w)`. The finite zero-field weighted
Lee--Yang theorem and paired Hadamard factorization give
`M_0(s)<=exp(V_0 s^2/2)`: the real-zero product has
`log M_0(s)=sum log(1+s^2/lambda^2)<=s^2 sum lambda^(-2)`, and the
last sum equals V_0/2. A zero-weight vertex is handled by positive-weight
approximation and Hurwitz, as in #1001.

Equations (3) and (6) prove the sequence-level equivalence. The sharp
whole-plane one-point consumer in ONE_POINT_ENTIRE.md applies more
widely, including bounded-support strip models with negative couplings;
this equivalence is restricted to the nonnegative-coupling field class.
For that restricted class, using one exterior MGF budget does not evade
the uniform V_0 requirement supplied by #1001.

## 4. Consequence for completion attempts

Every exact cofinal wall model in COFINAL_WALL_CONSTRUCTION.md has
V_0 tending to infinity. Equation (3) now rules out its exterior budget
without selecting one bad state, and applies to any alternative
ferromagnetic interior graph with the same diverging reference resource.
An actual theta construction in this field class must keep V_0 bounded.
The missing theorem is that growth-controlled construction itself;
unrestricted cofinal moment equality has already been obtained and is
insufficient.
