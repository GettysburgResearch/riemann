# Variance trapping and exact graph directions for theta moment extension

Status: **proposed native mathematics**. The variance barrier and graph identities
below are proved without the finite theta-20 theorem. Their application to the
theta-20 point is explicitly conditional on that proposed theorem. Numerical
tangent scans and continuations are ordinary Decimal experiments and are not
root certificates. No all-order construction or improved zeta strip is claimed.

The preceding strip packet proves that a finite ferromagnetic Ising observable
`Y=sum_i w_i sigma_i`, with `w_i>=0` and `|h_i|<=b w_i`, has Fourier zeros in
`|Im z|<=b` and obeys

\[
 |\varphi_h(z)|\le \exp\{V_0(b+|\Im z|)^2/2\},
 \qquad V_0=\mathbb E_0Y^2. \tag{1}
\]

Here the subscript zero means the same graph and couplings, after setting every
external field to zero. All statements use the original theta variable unless
standardization is explicitly stated.

## 1. A variance barrier along continuous constructions

### Theorem E1: reference-variance trapping

Let a finite ferromagnetic graph have nonnegative observable weights, arbitrary
real fields satisfying `|h_i|<=b w_i`, and let

\[
 v_h=\mathbb E_hY^2,\qquad V_0=\mathbb E_0Y^2.
\]

The second moment is used; no assumption that the biased law is centered is
needed. Then

\[
 \boxed{\quad v_h\ge V_0\exp(-b^2V_0/2).\quad} \tag{2}
\]

Consequently, suppose a continuous deformation of finite models preserves
`v_h=v>0` and the same band `b`. Assume its reference variance is continuous,
starts at `V_0=v`, and `b^2v/2<1/e`. It stays below the smaller positive solution
`V_-` of

\[
 V\exp(-b^2V/2)=v. \tag{3}
\]

More precisely `V_0<=V_-`. When `b>0`,

\[
 V_-=-\frac{2}{b^2}W_0(-b^2v/2), \tag{4}
\]

where `W_0` is the real principal branch of Lambert's W function. For `b=0`,
every field is zero and `V_0=v` directly.

**Proof.** Write `H=sum_i h_i sigma_i` and `C=E_0 exp(H)`. Global spin
reversal preserves the zero-field law, changes the sign of H and Y, and leaves
Y squared unchanged. Thus

\[
 \mathbb E_0[Y^2e^H]=\mathbb E_0[Y^2\cosh H]\ge V_0. \tag{5}
\]

The nonnegative high-temperature expansion and zero-field Lee--Yang Gaussian
bound, proved in the preceding strip packet, give

\[
 C\le \mathbb E_0 e^{bY}\le e^{b^2V_0/2}. \tag{6}
\]

Divide (5) by C to get (2). The function `g(V)=V exp(-b^2V/2)` increases up to
`2/b^2`, decreases after that point, and its maximum is `2/(e b^2)`. Under the
stated condition, (2) excludes the entire open interval `(V_-,V_+)` between
the two positive roots of (3). The starting value v is below V_-. Continuity
prevents a passage to the upper branch. Equation (4) just solves (3). QED.

Continuity means continuity of the numerical reference variance, and may cross
graph changes realized by zero weights, zero added couplings, or locked-spin
limits. It does not mean that arbitrary models of different orders can be
declared to belong to one path. The needed path is a mathematical premise.

### Corollary E1a: an explicit theta-scale barrier

Take `b=1/3`. Suppose the fixed biased second moment v is the original theta
variance, so the source gives

\[
 0<v<4621/100000=0.04621.
\]

Every continuous, fixed-variance, band-preserving deformation beginning at a
zero-field realization has

\[
 \boxed{\quad V_0<4633/100000=0.04633.\quad} \tag{7}
\]

Indeed, if `r=4633/100000`, the elementary inequality `exp(-x)>=1-x` yields

\[
 r e^{-r/18}\ge r-r^2/18>4621/100000. \tag{8}
\]

The last inequality is exact rational arithmetic: after multiplication by
`18*10^10`, its positive numerator is `135311`. At any first crossing of r,
(2) would contradict (8). This proof does not require computing Lambert W.

### Corollary E1b: compactness for a connected moment construction

Suppose a sequence of symmetric finite ferromagnetic models matches the original
theta moments to unbounded orders and has the fixed band `b=1/3`. Suppose their
construction connects them, by continuous fixed-second-moment deformations, to
a zero-field realization of the same variance. Then the separate uniform
reference-variance condition in the preceding packet's all-order theorem follows
from (7). In particular,

\[
 |\varphi_n(z)|\le
 \exp\{(4633/200000)(1/3+|\Im z|)^2\}. \tag{9}
\]

Moment identification, Montel, and Hurwitz then give the zeta boundary `5/6`.
The cofinal moment construction and the stated connecting paths remain missing.
The corollary removes an independent growth-budget verification from such a
construction; it does not establish the construction.

### Corollary E1c: a large forbidden variance interval

Every individual theta-variance model at band `b=1/3`, whether connected to a
zero-field start or not, satisfies the dichotomy

\[
 V_0<0.04633\quad\hbox{or}\quad V_0>100. \tag{9a}
\]

Indeed, the left endpoint is excluded by (8), and at the right endpoint

\[
 100e^{-100/18}>100e^{-6}>100/3^6>0.04621.
\]

The elementary bound `e<3` suffices. Since `V exp(-V/18)` is unimodal, its
minimum on `[0.04633,100]` occurs at an endpoint, so the full closed interval
is forbidden by (2). In particular, any crude certificate `V_0<=100` upgrades
to the sharp practical bound `V_0<0.04633`. For a finite model, the simple
support estimate `sum_i w_i<=10` is one sufficient such certificate; no pair
correlations need be evaluated. A fixed support bound is not asserted to be
available for a cofinal theta moment construction.

## 2. A domination bound and why continuity cannot be discarded

If the biased observable Y is symmetric, then its law dominates the zero-field
law as measures:

\[
 \mathbb P_h(Y\in A)\ge C^{-1}\mathbb P_0(Y\in A)
 \quad\text{for every Borel set }A. \tag{10}
\]

To see this, replace the indicator by the average of its values at Y and -Y;
symmetry leaves both probabilities unchanged. The averaged indicator is
nonnegative and even, so the same calculation as (5) applies. It follows that

\[
 d_{\rm TV}(\mathcal L_h(Y),\mathcal L_0(Y))
 \le 1-C^{-1}\le1-e^{-b^2V_0/2}. \tag{11}
\]

Total variation here is `sup_A |P(A)-Q(A)|`. In the path class of (7), it is
strictly below `r/18<0.002574`. Thus the permitted field perturbation changes
the observable law by at most about 0.258 percent in total variation. This does
not bound individual high moments by the same absolute amount.

The low branch is a genuine restriction. Fix any `v>0` and `b>0`. Take two
independent spins with observable weights `w/2,w/2` and fields `+bw/2,-bw/2`.
Their sum has characteristic function

\[
 \frac{\cosh(bw)+\cos(wz)}{1+\cosh(bw)}
\]

and biased variance `d_w=w^2/(1+cosh(bw))`, which tends to zero as w increases.
For sufficiently large w, add one independent unbiased spin of weight
`sqrt(v-d_w)`. The full observable has biased variance exactly v, obeys the
same band cap, and has reference variance

\[
 V_{0,w}=w^2/2+v-d_w\longrightarrow\infty. \tag{12}
\]

These are legal nonnegative-coupling finite models. They cannot be connected to
the zero-field starting model by a path preserving v and the same b while the
reference variance stays continuous. A fixed second moment alone therefore
does not prove the compactness needed in the all-order argument.

## 3. Exact vertex splitting without independent Fourier factors

Consider any zero-field finite Ising model with observable Y and a vertex v
having observable weight w>0. Choose `0<a<w`. Replace that vertex's weight by
`w-a`, attach a new spin of weight a by a ferromagnetic edge, and leave the
old graph, old couplings and all fields otherwise unchanged. Write

\[
 \tanh J=1-2\lambda,\qquad 0<\lambda<1/2. \tag{13}
\]

The old marginal is unchanged because summing the new spin gives the constant
`2 cosh J`. Conditional on the old spins, its sign equals the old vertex sign
with probability `1-lambda` and is the opposite sign with probability lambda.
Therefore the new observable has the exact distribution

\[
 \boxed{\quad
 \mathcal L(Y_\lambda)
 =(1-\lambda)\mathcal L(Y)
       +\lambda\mathcal L(Y-2a\sigma_v).
 \quad} \tag{14}
\]

The expression at lambda=0 denotes the locked limit; every positive lambda
below one half uses a positive finite coupling. The graph is interacting, and
(14) is not an independent convolution decomposition. Multiple new leaves
give the equally exact representation

\[
 Y_{\boldsymbol\lambda}
 =Y-2\sigma_v\sum_j a_j B_j,
 \qquad B_j\sim\operatorname{Bernoulli}(\lambda_j)
\]

with the B variables independent of each other and of the old Gibbs model,
provided `a_j>0` and `sum_j a_j<w`. This is a legal finite family with every
configuration retained.

## 4. Exact edge addition and the balanced response polynomial

Add one ferromagnetic edge of coupling J between old vertices u and v. Set
`t=tanh J`. Its Gibbs law is exactly

\[
 \frac{d\mathbb P_t}{d\mathbb P_0}
 =\frac{1+t\sigma_u\sigma_v}
        {1+t\mathbb E_0(\sigma_u\sigma_v)}. \tag{15}
\]

This identity follows directly from
`exp(J sigma_u sigma_v)=cosh J (1+t sigma_u sigma_v)`. It retains all old
configurations and is valid even when adding the edge creates a cycle.

Now let x be N adjustable coordinates of an analytic zero-field family.
Write `p_k= kappa_{2k}/c_{2k}`, where each `c_{2k}` is a fixed nonzero number;
the implementation takes the even cumulants of one fair sign. Assume the
N-by-N Jacobian of `(p_1,...,p_N)` at x0 is invertible. Let

\[
 \ell=(\partial_xp_{N+1})(\partial_x(p_1,\ldots,p_N))^{-1}.
 \tag{16}
\]

The implicit-function theorem retunes x for every sufficiently small added-edge
or splitting parameter so that p_1 through p_N stay fixed. If q denotes the
first derivative of the entire p vector before retuning, the derivative of the
next coordinate afterward is

\[
 S=q_{N+1}-\sum_{k=1}^{N}\ell_kq_k. \tag{17}
\]

This is an exact Schur complement, not a numerical ansatz.

An equivalent formula makes all candidate graph directions cheap to test. Put
`M(s)=E exp(sY)` and define the cumulant influence polynomials by

\[
 A_r(y)=r!\,[s^r]\frac{e^{sy}}{M(s)},\qquad
 G(y)=\frac{A_{2N+2}(y)}{c_{2N+2}}
       -\sum_{k=1}^N\ell_k\frac{A_{2k}(y)}{c_{2k}}. \tag{18}
\]

Here `[s^r]` extracts a Taylor coefficient. Differentiating log M proves that
the variation of `kappa_r` under any signed measure perturbation of total mass
zero is the integral of A_r against that perturbation. Also `E A_r(Y)=0` for
`r>=1`, hence `E G(Y)=0`. Equations (14)--(15) therefore give

\[
 S_{\rm split}(a)=\mathbb E[G(Y-2a\sigma_v)-G(Y)],\qquad
 S_{\rm edge}(u,v)=\mathbb E[G(Y)\sigma_u\sigma_v]. \tag{19}
\]

The split response is an explicit polynomial in a of degree at most `2N+2`.
The added-edge response needs only mixed polynomial moments in the unchanged
old model.

If two legal added directions have opposite nonzero balanced responses, the
attainable next-coordinate set contains an interval around the old value after
enlarging the graph and retuning the first N coordinates. For completeness,
take parameters alpha,beta>=0 with responses `S_alpha>0>S_beta`. Apply the
implicit-function theorem to the N old equations and the old next-coordinate
value, solving for `(x,beta)` as a function of alpha. The enlarged Jacobian is
invertible because its Schur complement is S_beta. At zero,
`beta'(0)=-S_alpha/S_beta>0`; thus for small alpha>0 both new couplings are
strictly positive. At such an interior point, varying beta and retuning x
gives a two-sided interval of next-coordinate values. This is a local
existence theorem only. It supplies neither the interval's size nor a guarantee
that a specific external target lies inside it.

## 5. What the theta-20 scan actually found

The scanner uses the frozen proposed T20D model and its ten active coordinates.
The ordinary 100-digit calculation finds both signs for splitting and edge
addition. For the dominant negative split, dividing the current positive
order-22 residual by the first derivative predicts a splitting probability
above one. This cannot establish a legal root: lambda must be below one half.

Adding a positive edge between the roots of blocks 3 and 8 is substantially
stronger. Its balanced derivative is approximately `-3.2488877892e-15`, while
the source model's next-coordinate residual is approximately `+1.5009965854e-16`.
The resulting first-order predicted edge correlation is approximately `0.0462`.
This motivates a full nonlinear calculation; it is not a proof of a crossing.

The complete evaluator in `explore_added_edge.py` implements (15) using
conditional moments of all old blocks. The unchanged old hub correlations make
`E_0 sigma_u sigma_v=eta^2` for the chosen pair of distinct block roots, so

\[
 \mathbb E_tY^n
 =\frac{\mathbb E_0Y^n+t\mathbb E_0[Y^n\sigma_u\sigma_v]}
        {1+t\eta^2}. \tag{20}
\]

No high-spin truncation, dominant-configuration selection, or omitted-cycle
approximation is used. Positivity of observable weights requires `A>|B|` in
the block coordinates; B itself need not be positive. Numerical nonlinear
continuations are reported in their accompanying JSON records.

## Source lineage and limits

The finite theta source and proposed T20D starting graph are frozen at commit
`c93ca65a510b6acaf167f929b9bf7e67d742b05a`, repository PR #994. The variance and
zero-band inputs are the directly proved S3 theorem of the preceding strip
packet, ultimately using finite multivariate Lee--Yang. E1, (14), (15), and
(17)--(19) are mathematical derivations in this note. The new directed theta
source through order 26 is produced separately by `../source26.py`; its receipt
must not be confused with a root certificate for any finite model.
