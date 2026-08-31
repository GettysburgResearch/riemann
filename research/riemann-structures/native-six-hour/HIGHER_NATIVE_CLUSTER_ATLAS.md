# Higher native activation: a concave band limit and the complete four-prime atlas

This extends the actual L-102707 activation source and the original
L-102880 ratio observation to every fixed squarefree arity. Its leading
cluster problem is a strictly concave, piecewise quadratic optimization
on the source simplex. For four primes the complete solution is explicit:
the middle two coordinates carry all limiting mass on one shape wall;
away from that wall all four coordinates are positive. The middle gap
changes the energy but not the optimizer. A five-prime calculation gives
strict inactive slacks and hence a stable face for the actual finite kernel.

The wall is a limiting shape, not an equality of products of distinct
physical primes. All statements retain the physical factor 1/sqrt(K),
all source factor allocations and the original measure nu. These are
selection results on the stated squarefree product, not an amplified
full-family estimate or one path optimized simultaneously at every product.

## 1. The complete source and cardinality bands

Let p1<...<pr be distinct primes, K their product, and write

\[
 \log p_i=L+\epsilon x_i,
 \qquad x_1<\cdots<x_r,\quad\epsilon>0.
 \tag{1}
\]

For a native monotone path from zero to one, put
`q_i=int u_i'(s) product_(j!=i)u_j(s) ds`. These coefficients are
nonnegative and sum to one. For S subset {1,...,r}, let q(S)=sum_(i in S)q_i
and x(S)=sum_(i in S)x_i. The actual `2 ds` source coefficient is

\[
 v_S=(-1)^r2^{1-r}q(S).
 \tag{2}
\]

The empty factor is zero; every other factor is retained and carries the
common physical multiplier 1/sqrt(K). Every simplex point is source
realizable. Positive points use the power paths u_i=s^(a_i), with
q_i=a_i/sum a_j. For a face, activate the zero-q coordinates first while
one positive-q coordinate is still zero, then use power paths on the
positive group. This can be done by monotone piecewise smooth paths with
the same endpoints and the actual derivative measure.

Suppose different cardinality bands are separated: for every k<r the
smallest product of k+1 primes divided by the largest product of k primes
exceeds sqrt8. The bands are then orthogonal in nu because the kernel
autocorrelation Gamma is supported on [-log8,log8]. Within one band the
frequency difference is 2epsilon[x(S)-x(T)]. Thus the exact full energy is

\[
 E_\epsilon(q)=\frac{4^{1-r}}K
 \sum_{k=1}^r\sum_{|S|=|T|=k}
 q(S)q(T)\Gamma(2\epsilon[x(S)-x(T)]).
 \tag{3}
\]

The total k-band coefficient mass is
`W_k=sum_(|S|=k)q(S)=binom(r-1,k-1)`, independent of q. In particular,

\[
 C_r=\sum_{k=1}^rW_k^2=\binom{2r-2}{r-1}.
 \tag{4}
\]

No variable band mass or deleted mean mode is hidden in (4).

## 2. HCA-1: the original-kernel cluster objective and a uniform remainder

The preceding cluster packet derives directly from the native kernel

\[
 \Gamma(\delta)=\Gamma_0-A|\delta|+O(\delta^2),
 \quad A=144+64\sqrt2,
 \quad |O(\delta^2)|\le36\delta^2
 \quad(|\delta|\le\log2).
 \tag{5}
\]

Define the source-owned distance objective

\[
 H_x(q)=\sum_{k=1}^r\sum_{|S|=|T|=k}
          q(S)q(T)|x(S)-x(T)|.
 \tag{6}
\]

Let T_x be the largest same-cardinality subset-sum distance. Whenever
2epsilon T_x<=log2, equations (3)--(5) give

\[
 E_\epsilon(q)=\frac{4^{1-r}\Gamma_0 C_r}{K}
 -\frac{8A\epsilon}{4^rK}H_x(q)+R_\epsilon(q),
 \qquad
 |R_\epsilon(q)|\le
 \frac{144\,4^{1-r}C_rT_x^2\epsilon^2}{K}.
 \tag{7}
\]

This proves the physical normalization of the optimization: maximize H,
not a replacement scalar spectral model. The bound is uniform on the
whole simplex, including its faces.

For each cardinality k, order the distinct locations x(S). If Delta is
a consecutive gap and m(q) is the cumulative coefficient mass to its
left, its contribution to (6) is

\[
 2\Delta\,m(q)\{W_k-m(q)\}.
 \tag{8}
\]

Equal subset-sum locations are grouped before making cuts. Since m(q)
is linear and W_k is constant, every term in (8) is concave. The first
band makes the entire objective strictly concave. In fact, on a
zero-sum displacement z, with Z_j=z1+...+zj and
delta=min_j(x_(j+1)-x_j)>0, the first-band quadratic form is

\[
 -2\sum_{j=1}^{r-1}(x_{j+1}-x_j)Z_j^2
 \le-\frac\delta2\|z\|_2^2.
 \tag{9}
\]

Here `||z||^2<=4 sum Z_j^2`; every other band has a nonpositive quadratic
form because its displacement has total mass zero. Hence H has a unique
simplex maximizer, even when some higher-band locations collide.

The true finite-kernel energy is strictly convex: its singleton band is
the Gram form of distinct exponentials in the nonzero absolutely
continuous original measure. Let q_epsilon minimize (3), and let q_x
maximize (6). A useful quantitative consequence, including face optima, is

\[
 \|q_\epsilon-q_x\|_2
 \le\frac{144\sqrt r\,C_rT_x^2}{A\delta}\,\epsilon.
 \tag{10}
\]

Indeed, divide (7) by its positive leading scale after subtracting the
constant. Each coordinate of the normalized error gradient is bounded by
`144 C_r T_x^2 epsilon/A`: differentiating a band introduces total mass
2W_k^2. Apply the two constrained variational inequalities and the
strong concavity (9). No interior-point assumption or false uniform
conditioning claim at vanishing singleton gaps is needed.

## 3. HCA-2: the entire four-source shape atlas

Write the four ordered coordinates, up to translation, as

\[
 x=(0,a,a+b,a+b+c),\qquad a,b,c>0,
\]

and put u=q1, v=q4, Q=q1+q2. The source simplex constraints are
`u,v>=0` and `u<=Q<=1-v`. If c>=a, the two-element subset order is

```
12, 13, 23, 14, 24, 34,
```

with successive gaps `b,a,c-a,a,b` and cumulative masses
`Q, 1+u-v, 2-2v, 2+u-v, 2+Q`. Using (8) and adding the singleton
and triple bands gives the exact polynomial

\[
\begin{split}
 H_x(q)={}&8(a+b+c)+8bQ(1-Q)\
 &-8au^2+8auv-4(3c-a)v^2+4(c-a)v.
\end{split}\tag{11}
\]

At c=a the middle gap is zero, so either adjacent order produces the
same polynomial. For c<a reflect the prime indices and exchange a,c.

The unique maximizer is therefore

\[
 \boxed{
 c\ge a:\quad
 v=\frac{c-a}{3(2c-a)},\quad u=\frac v2,\quad
 q_x=(u,1/2-u,1/2-v,v).
 }
 \tag{12}
\]

For a>=c use
`u=(a-c)/(3(2a-c)), v=u/2` in the same vector. To verify the KKT
conditions, first Q=1/2 maximizes its independent strict quadratic;
then the stationary equations give u=v/2 and the displayed v. These
coordinates satisfy all simplex constraints: u<=1/12 and v<=1/6 when
c>=a, with the reflected bounds in the other chamber. Thus no additional
active-face chamber is missing.

The middle gap b has disappeared from (12), although it still changes
the energy and conditioning. The two chambers meet in the limiting face

\[
 a=c:\qquad q_x=(0,1/2,1/2,0).
 \tag{13}
\]

For c>=a the exact optimum value is

\[
 H_x(q_x)=8(a+b+c)+2b+
          \frac{2(c-a)^2}{3(2c-a)}.
 \tag{14}
\]

Its gain over uniform activation is

\[
 H_x(q_x)-H_x(1/4,1/4,1/4,1/4)
 =\frac{2c^2+5ac-a^2}{12(2c-a)}>0,
 \tag{15}
\]

and reflection supplies the other case. At arithmetic spacing a=b=c=1,
the optimum is 26 and the gain is 1/2. The source path realizing (13)
first activates primes 1 and 4 while the two middle coordinates remain
zero, then activates the middle coordinates together. This is an actual
endpoint-preserving source path; deleting endpoint atoms is not its definition.

For example x=(0,1,2,4) has
`q_x=(1/18,4/9,7/18,1/9)`. The shape (0,1,4,6) has the same outer gaps
and the same optimizer, while reflection gives the corresponding reversed
weights. These predictions precede the exact discovery run.

## 4. HCA-3: a stable finite-source face at five primes

The five-source arithmetic shape yields a stronger boundary conclusion.
This calculation was derived from the cut formulas before inspecting the
held-out discovery answer. For x=(0,1,2,3,4), reflection and uniqueness
force the maximizer to have the form

\[
 q=(a,b,1-2a-2b,b,a),\qquad a,b\ge0,\quad a+b\le1/2.
\]

Writing z=a+b, the singleton and four-element bands contribute
`28+4b-8a^2-8z^2`. The pair and triple bands have pair locations
1,...,7 with cumulative subset counts `1,2,4,6,8,9` and cumulative
coefficient masses `z,1-b,2-z,2+z,3+b,4-z`. Formula (8), applied to
the pair weights and their complements, gives
`100+8b+8z-16z^2-8b^2`. Thus the exact objective on the symmetric simplex is

\[
 H(q)=128+8a+20b-32a^2-48ab-32b^2.
 \tag{16}
\]

Its unique constrained maximum is

\[
 \boxed{q_*=(0,5/16,3/8,5/16,0)},\qquad
 H(q_*)=1049/8,
 \quad H(q_*)-H(1/5,\ldots,1/5)=401/200.
 \tag{17}
\]

At this point the a-derivative is -7 and the b-derivative is zero.
In the full KKT convention `Bq=lambda` on active coordinates, where
H=q^TBq, each inactive endpoint has strict slack
`lambda-(Bq)_endpoint=7/4`. Reflection supplies equality of the two
endpoint slacks and of the two other active gradients. Hence (17)
solves the full simplex problem, not only a restricted symmetric problem.

Unlike the four-source wall, this face is stable under small shape and
original-kernel perturbations. For actual prime clusters with
`log p_i=log X+epsilon*(i-1)+O(epsilon^2)`, equation (10) and the
Lipschitz dependence of B on the shape give q_epsilon=q_*+O(epsilon).
The middle three coordinates stay positive, and the two strict inactive
gradient gaps stay positive. The KKT equations therefore force

\[
 (q_\epsilon)_1=(q_\epsilon)_5=0
 \quad\text{for every sufficiently small epsilon}.
 \tag{18}
\]

This is an exact active-face statement for the original finite observed
energy on cofinal actual prime clusters. No equality of distinct prime
products is needed. A zero activation means the corresponding prime is
activated before the active group; it does not delete every factor atom
containing that prime. All 32 source allocations remain in (3).

The leading gain over the uniform path is
`401*A*epsilon/(25600*K)`. It is positive and absolutely small, consistent
with the physical normalization throughout this packet.

## 5. Physical prime realization and what the wall does not mean

For distinct physical primes, exact equality of the two middle pair
frequencies would require p1*p4=p2*p3, which is impossible. Thus the wall
(13) must not be advertised as an exact prime-product collision. It is a
limiting rational shape that can be approached by actual primes.

For each fixed small epsilon and target ordered shape x, ordinary PNT
supplies primes in disjoint intervals with endpoints
`X exp(epsilon x_i)` and `X exp(epsilon x_i+epsilon^2)` once X is
sufficiently large for that fixed epsilon. Choose successive X values
after choosing a sequence epsilon tending to zero. Then

\[
 \log p_i=\log X+\epsilon x_i+O(\epsilon^2),
\]

and all cardinality bands separate for large X. This uses a diagonal
sequence of fixed-relative-interval consequences of PNT, not a uniform
shrinking-interval theorem. The source matrix is Lipschitz in the shape;
(9)--(10) therefore show that the actual minimizing activations converge
to (12), including (13). At the wall their endpoint coordinates are
O(epsilon); no claim is made that the finite optimizer has exactly zero
end coordinates.

For every fixed arity and shape, all these energies are O(1/K) and the
strict leading improvements are O(epsilon/K). No growing native principal
moment conclusion follows. The finite global-horizon experiment is a
separate test of a single path acting on many physical products at once.

## 6. HCA-4: the held-out six-source result and its precise limitation

The preregistered exact discovery is frozen at
`0eb242a5ae1f0e29ab725587fc63a973ff6354c1`. It agrees with all four-source
predictions and with the independently derived five-source result. For the
held-out shape x=(0,1,2,3,4,5), the complete source matrix B in H=q^TBq is

```
472 542 594 640 684 730
542 576 612 638 662 684
594 612 616 634 638 640
640 638 634 616 612 594
684 662 638 612 576 542
730 684 640 594 542 472
```

The cumulative-distance construction (8) independently reproduces this
matrix. Its exact KKT solution is

\[
 q_*=(0,0,1/2,1/2,0,0),\quad H(q_*)=625,
 \quad H(q_*)-H(1/6,\ldots,1/6)=70/9.
 \tag{19}
\]

The inactive-slack vector in the Bq convention is `(8,0,0,0,0,8)`.
Strict concavity proves uniqueness despite the zero slacks at coordinates
2 and 5. Thus small original-kernel and shape perturbations preserve the
two extreme zero activations, but this leading calculation alone does
**not** prove that all four limiting zeros persist at finite epsilon.
The middle inactive directions require a higher-order analysis.

For an independent short reduction, reflection writes
`q=(a,b,1/2-a-b,1/2-a-b,b,a)`. Direct substitution gives
`H=625-32a-32a^2-32ab-24b^2`, whose unique constrained maximum is a=b=0.
The absence of a linear b-term exhibits the unresolved finite-order issue.

## 7. Exact discovery rather than extrapolation

HIGHER_CLUSTER_PREREGISTRATION.md fixes the shape panels and hard caps.
The bounded producer builds the matrix in (6) from all ordered subset
pairs and independently from (8). It enumerates every nonempty active
support and solves its rational KKT system. For r<=6 this is at most
64 source subsets, 63 active supports and a seven-dimensional linear
system. The four-source predictions above are checked. Arithmetic r=5 and
r=6 were preregistered held-out panels without prescribed answers; the
five-source answer was subsequently derived analytically before its
computed answer was inspected, while (19) was first read from the exact
discovery and then proved by its source matrix and KKT certificate.

The all-arity limit and the four-source atlas are proved above, not inferred
from those finite panels. The replay does not stand in for the original
kernel remainder or assert that a rational shape wall is an exact native
prime equality.
