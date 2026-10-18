# Exact cofinal strip models exist, but their growth budget fails

**Status: PROPOSED complete analytic construction and obstruction. No new
zeta zero-free region or proof of RH follows.** The target is the actual
original theta law, not a synthetic replacement. The construction explains
why unrestricted finite moment climbing in the real-field strip class is
insufficient: that class already permits exact matching at every finite
order, for every positive band, while an explicit rare sector destroys
complex compactness.

The imported input is the finite multivariate Lee--Yang band theorem,
proved for this field/weight formulation in repository PR #1001 at
`f6beb3774ae7ff5eca4cb046786eae10e4f88abc`,
`standalone/2026-10-18-zeta-specific-family-and-strip/strip/PROOF.md`,
Theorem S3. Gaussian quadrature and the implicit-function argument are
proved below in the forms actually used. Domain-wall coding is elementary;
no novelty claim about its general use in probability is intended.

## 1. The exact cofinal theorem

Let`T` be the actual symmetric theta random variable with
`E exp(izT)=Xi(z)/Xi(0)`. Fix any`b>0`. For every integer`n>=1`, there is a
finite **connected ferromagnetic chain**, with strictly positive
observable weights`w_i`, finite positive couplings`J_i`, and real fields
satisfying

\[
 |h_i|\le b w_i,
\]

whose symmetric observable`Y_n=sum_i w_i sigma_i` satisfies

\[
 E Y_n^{2r}=E T^{2r}\qquad(1\le r\le n). \tag{1}
\]

Every finite characteristic function has all its zeros in`|Im z|<=b`.
Nevertheless the models can be chosen with

\[
 E e^{R Y_n}\longrightarrow\infty
 \quad\text{for every }R\ge b, \tag{2}
\]

and their same-graph zero-field reference variances tend to infinity.
Thus neither the growth premise of #1001 nor the one-point premise in
ONE_POINT_ENTIRE.md is furnished by this exact cofinal feasibility result.

The same argument works for any symmetric probability law whose squared
variable has all moments and a positive density on`(0,infinity)`. The theta
density satisfies these hypotheses: it is strictly positive, and its full
tails decay faster than every exponential, as described in SOURCE_DEEP.md
and HERMITE_ARCHITECTURE.md.

## 2. A finite quadrature point with an invertible moment map

Put`U=T^2`. Let`P_(n+1)` be its monic orthogonal polynomial of degree`n+1`.
The moment Gram matrix is strictly positive definite, so this polynomial
exists. It has`n+1` distinct positive zeros`u_1,...,u_(n+1)`: if it had at
most`n` sign-changing positive roots, multiplying it by their product would
give a polynomial of degree at most`n` whose inner product with
`P_(n+1)` has a fixed nonzero sign, contradicting orthogonality.

Let`ell_j` be the Lagrange polynomial of degree`n` on those nodes, and set
`alpha_j=E ell_j(U)`. Polynomial division by`P_(n+1)` shows that

\[
 E Q(U)=\sum_{j=1}^{n+1}\alpha_j Q(u_j)
 \quad(\deg Q\le2n+1).
\]

Indeed the quotient has degree at most`n`, so its product with
`P_(n+1)` integrates to zero. Applying this identity to`ell_j^2` proves
`alpha_j=E ell_j(U)^2>0`; applying it to1 gives`sum alpha_j=1`.

The symmetric atomic law with masses`alpha_j/2` at`+-sqrt(u_j)` therefore
matches the theta even moments required in (1). Keep its positive nodes
fixed and vary the first`n` probabilities, with
`alpha_(n+1)=1-sum_(j<=n) alpha_j`. The Jacobian of its first`n` even
moments is

\[
 A_{rj}=u_j^r-u_{n+1}^r,\qquad1\le r,j\le n. \tag{3}
\]

This matrix is invertible. A linear dependence of its rows would give a
polynomial of degree at most`n` vanishing at all`n+1` distinct nodes;
the polynomial is zero, hence so are all coefficients. The starting
probability vector lies strictly inside the positive simplex.

## 3. Encode the atomic law by a single domain wall

List the`2n+2` symmetric support points in increasing order as
`v_0<...<v_K`, with`K=2n+1`, `v_0=-A`, `v_K=A`. Let their probabilities
be`p_0,...,p_K`, so`p_k=p_(K-k)>0` and`sum p_k=1`.

Use spins`0,...,K+1` on a chain. For each interior spin`1<=i<=K`, set

\[
 w_i=\frac{v_i-v_{i-1}}2>0,
 \qquad\sum_{i=1}^K w_i=A.
\]

Choose a large finite`L>1` and put

\[
 J_k=L-\frac12\log p_k>0\quad(0\le k\le K),\qquad
 H=2L,\qquad B=H/b.
\]

The two endpoint observable weights are`w_0=w_(K+1)=B`; their fields are
`h_0=H`, `h_(K+1)=-H`. Every interior field is zero. In particular
`|h_i|<=b w_i` holds at every vertex, with equality at the endpoints.
All couplings and weights are finite and strictly positive.

The Gibbs probability is proportional to

\[
 \exp\left(\sum_{k=0}^K J_k\sigma_k\sigma_{k+1}
                  +H\sigma_0-H\sigma_{K+1}\right).
\]

Reflection of the chain followed by global spin reversal preserves this
law and reverses the observable. Thus`Y` is symmetric.

If the endpoints are`+,-` and exactly one domain wall occurs, at bond`k`,
the endpoint observable contributions cancel and

\[
 Y=2\sum_{i\le k}w_i-A=v_k.
\]

Its relative weight is`exp(-2J_k)=exp(-2L)p_k`. Conditional on this
one-wall sector the observable has exactly the desired atomic law.
The reversed endpoint orientation gives its reflection, the same law.

## 4. Exact complete-sector bounds

Let`a=exp(-2L)`. A configuration is determined by its first spin and the
set`S` of domain-wall bonds. Apart from a common factor, its coupling
weight is`a^|S| product_(k in S) p_k`. Write

\[
 E=\sum_{m\text{ even}}a^m e_m(p),\qquad
 O=\sum_{m\text{ odd}}a^m e_m(p),
\]

where`e_m` is the elementary symmetric polynomial. The full partition
function is

\[
 Z=2e^{\sum J_k}\{E+\cosh(2H)O\}. \tag{4}
\]

No configuration is discarded. Since`e_m(p)<=1/m!` and`e_1(p)=1`,

\[
 E\le e,\qquad a\le O\le ea,\qquad O-a\le ea^3.
\]

The probability of aligned endpoints, corresponding to an even wall
count, and the probability of at least three walls with opposite
endpoints therefore obey

\[
 P_{\rm even}\le2e\,e^{2L-2H},\qquad
 P_{\rm odd,\ge3}\le e\,e^{-4L}. \tag{5}
\]

On the remaining one-wall sector the law is the prescribed atomic law.
The total observable is bounded by`2B+A`. Consequently every fixed moment
converges to its atomic value as`L` tends to infinity, since`B=2L/b` and
the probabilities in (5) decay exponentially.

## 5. Retune to exact theta moments at every finite order

Fix`n` and the quadrature nodes from Section2. Use the`n` independent
probability coordinates there in a small closed ball strictly inside the
positive simplex. The chain's first`n` even moment map`F_L(alpha)` is
real analytic in these coordinates. In fact, after extracting the common
coupling factor as in (4), every configuration weight is a polynomial
in the`p_k`, and the remaining normalization is strictly positive.

On this ball the estimates in (5), and their first derivatives in the
probabilities, are uniform. There are finitely many configurations for
the fixed`n`, every probability is bounded away from zero, and
differentiating a wall product only changes its finite constant bound.
Thus the moment maps converge in`C^1` to the atomic moment map:

\[
 F_L\longrightarrow F_\infty,
 \qquad DF_L\longrightarrow A.
 \tag{6}
\]

For moments through`2n`, the error is bounded by a constant depending on
the fixed nodes, probability ball,`n,b`, times
`(1+L)^(2n) exp(-2L)`. This includes both sectors in (5), all their
normalization terms, and all first probability derivatives.

For completeness, apply the map

\[
 G_L(\alpha)=\alpha-A^{-1}
       \{F_L(\alpha)-(E T^2,...,E T^{2n})\}.
\]

At the positive quadrature vector`alpha_0`, (6) gives
`G_L(alpha_0)-alpha_0->0`, and uniformly on a small ball
`DG_L=I-A^(-1)DF_L->0`. For every sufficiently large finite`L`, this is
a strict contraction mapping that ball into itself. Banach's theorem
therefore supplies an interior positive vector`alpha_L` with the exact
theta moments (1).

This proves finite existence for every`n`, without any assumption about
theta zeros. Choose one sufficiently large`L_n>=n` for each`n`.
The resulting sequence has exact cofinal moment matching and, in
particular, its **actual variance is exactly`Var(T)`** at every stage.

## 6. The exact completion estimate fails in a specified sector

The all-positive spin configuration has probability

\[
 P(\sigma_i=+1\ \forall i)
   =\frac1{2(E+\cosh(2H)O)}
   \ge\frac1{4e}e^{-2H+2L}, \tag{7}
\]

using`O<=ea`, `E<=e`, and`a cosh(2H)>1` for`H=2L,L>1`.
Its observable is`2B+A`. Hence for every`R>0`,

\[
 \boxed{E e^{RY}\ge\frac1{4e}
 \exp\{2H(R/b-1)+2L+RA\}.} \tag{8}
\]

In particular (8) tends to infinity for every`R>=b`, also after the
probabilities are retuned in Section5. The bound is uniform over the
whole positive simplex; it does not rely on the exact quadrature vector.
This proves (2). The rare aligned sector has vanishing contribution to
every fixed moment while making every useful exterior exponential-moment
budget diverge.

In the same graph with all fields removed, ferromagnetic correlations
are nonnegative. Thus its reference variance satisfies

\[
 V_0=E_0Y^2\ge\sum_iw_i^2\ge2B^2\longrightarrow\infty. \tag{9}
\]

Neither the zero-field-variance consumer in #1001 nor the sharper actual
one-point consumer in ONE_POINT_ENTIRE.md can complete this construction.
The failed estimate is explicit: the all-positive sector alone forces
the lower bound (8), so no better bound on the other sectors can repair it.

## 7. An explicit approximate sequence for the actual theta law

There is also a version requiring no quadrature or retuning. Let`X_N` be
`T` rounded to mesh`1/N` and clipped to`[-N,N]`. It has symmetric positive
probabilities`p_k` on`v_k=-N+k/N`, `0<=k<=2N^2`. Use`K=2N^2` interior
spins, all weights`1/(2N)`, and the same chain formulas with

\[
 L_N=N^2,\qquad H_N=N^4,\qquad B_N=H_N/b.
\]

The one-wall law is exactly`X_N`. Bounds (5) imply convergence of every
fixed moment to the actual theta moment. For each fixed`r<b`, the
contribution of the unwanted sectors to the Fourier transform on
`|Im z|<=r` is bounded by

\[
 2e\,e^{-4N^2+rN}
 +4e\,e^{-2N^4(1-r/b)+2N^2+rN}\longrightarrow0.
\]

The rounded/clipped theta transforms converge locally uniformly on the
whole plane, by dominated convergence and the theta exponential moments.
Thus the graph transforms converge locally uniformly to`Xi/Xi(0)` on
the open strip`|Im z|<b`. At every`iR` with`R>=b`, (8) diverges instead.
This gives a completely specified actual-target realization of the
compactness failure, beyond a synthetic rare-jump example.

## 8. Consequence for the research programme

The real-field class from #1001 is sufficiently flexible that **exact
cofinal theta moment feasibility is already unconditional** when no
uniform growth resource is imposed. The necessary new theorem is a
cofinal construction with a bounded reference variance or one bounded
actual exponential moment at a point`R>b`. The chain construction proves
that this resource does not follow from exact moments, fixed actual
variance, positivity, ferromagnetic coupling, or a fixed zero band.

This rules out one explicit universal coding attempt as a route to a new
zero-free region. It does not rule out other correlated real-field
constructions with controlled resources. No computational residual,
finite moment count, or zero-free conclusion is substituted for that
missing completion estimate.
