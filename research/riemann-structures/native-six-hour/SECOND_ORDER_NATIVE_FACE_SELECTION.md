# The original kernel resolves the four- and six-prime boundary faces

The leading cluster atlas leaves zero KKT slacks at the four-prime
arithmetic shape and at two inactive coordinates of the six-prime shape.
The actual kernel's next coefficient resolves them. On sufficiently
accurate cofinal arithmetic-log prime clusters, the unique minimizer of
the **full original finite observed energy** activates only the central
two primes at the final stage. Every other activation is exactly zero.

This statement concerns the native squarefree product source with all
2^r factor allocations and the physical factor 1/sqrt(K), for r=4 or6.
It neither deletes the factors containing an early-activated prime nor
claims an amplified full-family bound. Its proof uses the original kernel
with a quantified remainder, rather than replacing that kernel by a
quadratic model.

## 1. The theorem and the stronger prime-window condition

Fix r=4 or6 and a fixed M>0. Suppose actual distinct primes satisfy

\[
 \log p_i=L+\epsilon(i-1)+e_i,
 \qquad |e_i|\le M\epsilon^3,\qquad i=1,\ldots,r,
 \tag{1}
\]

and different cardinality bands are separated by the original kernel's
support as in HIGHER_NATIVE_CLUSTER_ATLAS.md. For all sufficiently small
epsilon, depending only on r and M, the unique minimizing activation has

\[
 q_i=0\quad(i\notin\{r/2,r/2+1\}),\qquad
 q_{r/2}=1/2+O(\epsilon^2),\quad
 q_{r/2+1}=1/2+O(\epsilon^2).
 \tag{2}
\]

In particular (2) has two exact zeros for r=4 and four exact zeros for
r=6. The weaker log-window error O(epsilon^2) from a first-order cluster
argument is not silently sufficient here: it can alter the decisive
order-epsilon inactive gradients. The stronger condition (1) is used.

Each activation is an actual monotone source path: activate the zero-q
primes while at least one central coordinate remains zero, then use the
appropriate power path on the two central coordinates. The original
`2 ds` derivative measure and the source endpoint are unchanged.

## 2. The exact native cubic remainder

The frozen cluster packet derives the five-overlap formula for Gamma on
[0,log2]. Its third derivative is

\[
 \Gamma'''(\delta)=\tfrac18\big((288+192\sqrt2)e^{\delta/2}
                         +(576+192\sqrt2)e^{-\delta/2}\big).
 \tag{3}
\]

This is a convex function; its maximum on the interval is attained at an
endpoint. The two endpoint values are `108+48sqrt2` and `72+72sqrt2`,
both below180. Together with Gamma''(0+)=-72 and evenness, Taylor's
formula therefore gives

\[
 \Gamma(\delta)=\Gamma_0-A|\delta|-36\delta^2+R_3(\delta),
 \qquad |R_3(\delta)|\le30|\delta|^3,
 \quad |\delta|\le\log2,
 \tag{4}
\]

where A=144+64sqrt2. Also |Gamma'|<300 away from zero on this interval,
and the same Lipschitz bound holds across zero. For example
`|Gamma'|<=A+72log2<300` follows from the already proved second-derivative
bound. These are bounds for the authenticated kernel itself.

## 3. The second distance moment and its source normalization

For a shape x and activation q, retain the complete same-cardinality
distance forms

\[
 H_x(q)=\sum_{k,S,T}q(S)q(T)|x(S)-x(T)|,
 \qquad
 J_x(q)=\sum_{k,S,T}q(S)q(T)(x(S)-x(T))^2,
 \tag{5}
\]

where both sums run over all |S|=|T|=k. Dividing the original energy
by its positive source scale and subtracting its constant band mass turns
minimization into maximization of

\[
 \Phi_{\epsilon,x}(q)
 =H_x(q)+\frac{72}{A}\epsilon J_x(q)+\mathcal R_{\epsilon,x}(q).
 \tag{6}
\]

This is an exact definition through the full original energy. If T is
the maximum same-cardinality shape distance and C_r=binom(2r-2,r-1),
(4) implies the uniform coordinate-gradient bound

\[
 \|\nabla\mathcal R_{\epsilon,x}\|_\infty
 \le\frac{240 C_rT^3}{A}\epsilon^2
 \quad(2\epsilon T\le\log2).
 \tag{7}
\]

One may use the homogeneous extensions off the simplex; their common
gradient direction has no effect on constrained KKT comparisons. In
particular the plus sign of the J term in (6) is forced by the negative
quadratic coefficient in (4).

Here is a source-count derivation of the needed moment coefficients.
Write X_q=sum q_i x_i, X2_q=sum q_i x_i^2, S1=sum x_i and S2=sum x_i^2.
In band k put W=binom(r-1,k-1), B=binom(r-2,k-2), C=binom(r-3,k-3),
with out-of-range binomials zero. Counting which indices lie in S gives

\[
\begin{split}
 \sum_{|S|=k}q(S)x(S)&=(W-B)X_q+B S1,\\
 \sum_{|S|=k}q(S)x(S)^2
 &=(W-3B+2C)X2_q+(2B-2C)S1X_q\\
 &\qquad +(B-C)S2+C S1^2.
\end{split}\tag{8}
\]

The k-band contribution to J is twice W times the second expression,
minus twice the square of the first. On reflection-symmetric activations
of the arithmetic shape, X_q is fixed. Thus the coefficient of X2_q in
the whole J is

\[
 2\sum_k W(W-3B+2C)
 =-\frac{2}{r-1}\binom{2r-4}{r-2}.
 \tag{9}
\]

The equality follows from the adjacent-binomial Vandermonde identity.
It is -4 for r=4 and -28 for r=6. No subset or character class is omitted
from this count.

## 4. All inactive gradients, not only a symmetric-path test

First use the ideal comparison shape x=(0,1,...,r-1), and let q0 put
mass1/2 at each central coordinate. Reflection preserves the exact
original energy. Strict convexity makes q0 the exact minimizer when
restricted to the central two-coordinate face, for every sufficiently
small epsilon. This comparison matrix is a function of logarithmic
frequencies; it does not assert that these ideal frequencies are actual
distinct primes in exact geometric progression.

For r=4, the symmetric displacement
`q=(a,1/2-a,1/2-a,a)` increases X2_q by4a. Equations (8)--(9) give
`dJ/da=-16`. Both endpoint gradients are equal by reflection, as are
the active gradients, so each inactive-minus-active J gradient is -8.
Its leading H gradient gap is zero. The exact normalized gaps from (6) are

\[
 (\nabla\Phi)_1-(\nabla\Phi)_2
 =(\nabla\Phi)_4-(\nabla\Phi)_3
 =-\frac{576}{A}\epsilon+O(\epsilon^2)<0.
 \tag{10}
\]

For r=6, the leading atlas gives H-gradient gaps -16 at coordinates1,6
and zero at coordinates2,5. The symmetric displacement putting mass b
at2,5 and removing b from each central coordinate increases X2_q by4b.
Thus `dJ/db=-112`, and each inner inactive-minus-active J gradient is -56.
The complete inactive KKT comparisons are

\[
 \begin{array}{ll}
 i=1,6:&(\nabla\Phi)_i-(\nabla\Phi)_{\rm active}=-16+O(\epsilon),\\
 i=2,5:&(\nabla\Phi)_i-(\nabla\Phi)_{\rm active}
             =-\dfrac{4032}{A}\epsilon+O(\epsilon^2).
 \end{array}\tag{11}
\]

All four are strictly negative. Reflection supplies individual gradient
equalities, rather than treating a negative derivative along one symmetric
direction as sufficient to exclude every inactive coordinate.

Equations (7), (10) and (11), together with the exact active equations,
are the KKT proof for the original kernel in the ideal comparison problem.
The quadratic term is only used to prove signs that the full remainder
cannot overturn.

## 5. Transfer to actual nonsymmetric prime clusters

Condition (1) gives an actual normalized shape x_epsilon with
`||x_epsilon-x_ideal||_infinity<=M epsilon^2`. For two equal-cardinality
subsets, their frequency differences change by at most
`4r epsilon ||x_epsilon-x_ideal||_infinity`. The native Lipschitz bound
following (4) therefore controls the change in the normalized gradient by
O(epsilon^2), uniformly on the simplex. More explicitly, a valid bound is
`1200 r C_r ||x_epsilon-x_ideal||_infinity/A` per coordinate, as long as
the compared frequencies remain in the small-shift interval.

The leading singleton band gives a strictly negative Hessian on the
simplex tangent space, uniformly near this fixed shape. The exact
normalized problem inherits that bound for small epsilon. Consequently
the minimizer on the actual central face differs from q0 by O(epsilon^2),
and both central coordinates remain positive. Evaluating the full
inactive gradients there changes (10)--(11) by only O(epsilon^2).
Their negative order-epsilon or order-one terms survive. The complete
KKT conditions prove (2), with uniqueness from the original Gram norm.

The common physical multiplier1/K changes with the primes but not with q,
so it cannot alter this minimizing face. Distinct physical products remain
distinct; no artificial equality of prime factorizations is used.

## 6. Cofinal actual primes and observable scope

Choose epsilon_j tending to zero. For each fixed j, ordinary PNT supplies
primes in the r disjoint intervals

`[X exp(epsilon_j(i-1)), X exp(epsilon_j(i-1)+min(M,1)*epsilon_j^3)]`

once X is sufficiently large for that fixed j. Choose X_j successively
large and also impose cardinality-band separation. This proves cofinal
actual prime families satisfying (1), without a uniform shrinking-interval
theorem. Their finite original-kernel minimizers have the exact faces (2).

All observed energies are still O(1/K), and their improvements over uniform
activation are O(epsilon/K). The finite bounded certificate distinguishes
the ideal comparison-frequency controls from any separately acquired
literal prime controls. It does not infer a full source moment result,
replace a native diagonal, or identify the complete post-renewal gamma.

## 7. Independent finite original-kernel certificate

The acquisition in `NATIVE_FACE_PRIME_PREREGISTRATION.md` was frozen before
testing any kernel face. It takes the first prime in each of six fixed
windows around `10^8(51/50)^i`, each of half-width100. The resulting primes
are

`99999931, 101999927, 104039917, 106120717, 108243127, 110408003`.

The two prescribed panels use the first four and all six. Every prime is
certified by complete bounded trial division, and the first-prime rule is
replayed. This acquisition does not depend on the kernel test outcome.

For either panel, retain all `2^r` factor allocations. Define the exact
unscaled Gram matrix

\[
 G_{ij}=\sum_{|S|=|T|}1_{i\in S}1_{j\in T}
 \Gamma\!\left(2\log\frac{\prod_{s\in S}p_s}{\prod_{t\in T}p_t}\right).
 \tag{12}
\]

The original energy is `4/(4^r K) q^T G q`. The certificate checks
cardinality-band separation with exact integer inequalities, so the
omitted different-cardinality terms are zero in the actual kernel.
Within each band, it evaluates all nine intersections of the three
literal kernel pieces. It independently compares that expression with
the closed native formula (3), and bounds logarithms by rational series
with rational remainders. The new input cap is explicitly256 bits; the
earlier64-bit helper is preserved unchanged. No quadratic approximation
is used to decide any finite KKT inequality.

The first execution stopped only when an exact interval endpoint exceeded
Python's protected integer-to-string limit. No mathematical input or
decision rule was changed. The bounded output contract now rounds each
lower endpoint down and each upper endpoint up to the dyadic lattice
of spacing2^-512, after an explicit131072-bit arithmetic cap. All signs
and KKT decisions still use the unrounded exact intervals. Serialized
endpoints are checked for outward containment and a2048-bit output cap;
the interpreter's integer conversion protection remains enabled.

Let a,b be the two central indices, and put

\[
 n=G_{bb}-G_{ab},\qquad m=G_{aa}-G_{ab},\qquad d=n+m.
\]

When n,m,d are positive, the restricted central minimizer is
`q_a=n/d,q_b=m/d`. Its full minimum-energy KKT condition at an inactive i
is the sign of the exact expression

\[
 (G_{ia}-G_{aa})n+(G_{ib}-G_{ab})m.\tag{13}
\]

Strict positivity at every inactive index proves the full simplex face,
not merely stationarity along a reflection-symmetric slice. Distinct
physical prime products and positivity of the original Fourier measure
away from isolated zeros make this full Gram form positive definite.
Consequently a certified face is the unique global source-simplex
minimizer. The replay retains a failed sign if one occurs; it does not
modify the acquired primes or discard the failed coordinate.

The final producer also independently enumerates the same-cardinality
integer moments for (8)--(11), including every individual gradient gap,
and checks the actual two-stage source paths on the central face. A zero
activation coordinate does not remove factor allocations containing that
prime. During the first stage the inactive primes are activated while
both active coordinates are zero; their full squarefree monomial
contribution vanishes. During the second stage the active pair follows
positive power paths with all other coordinates already one. The
integrated coefficients are the original `2 ds` coefficients, not a
replacement probability measure.

Both preregistered panels passed the original-kernel KKT test. The
executed discovery is frozen at
`e44e99b59593eacc943ac526193516357d25d34e`; its exact source and artifact
are authenticated by the final producer. Rounded diagnostics are:

| arity | central activations | inactive unscaled half-gradient slacks | original energy gain over uniform |
|---|---|---|---:|
|4|0.4999999946, 0.5000000054|0.193206, 0.193167|6.71757e-34|
|6|0.4999989136, 0.5000010864|77.9347, 1.15790, 1.15740, 77.9342|5.47810e-50|

The certificate uses the exact outward intervals, not these rounded
displays. All inactive signs are strict, while the active coordinates
solve the exact two-coordinate stationarity equations. The r=6 face has
four exact zeros even at this nonsymmetric literal prime tuple. The
gains are absolutely small, as required by the physical1/K factor.
