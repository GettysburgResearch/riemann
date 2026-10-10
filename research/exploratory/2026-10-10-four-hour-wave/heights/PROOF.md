# Height, strip width, and finite safe-axis order

Status: proposed mathematics, independently reviewable; not an integrated claim.

Scope: (i) finitely many alternating derivative signs on the complete positive
squared axis; (ii) a uniform compact-node Pick theorem of arbitrary declared
finite even order under an explicit inequality; (iii) a synthetic obstruction
to extending the existing single-reserve order-three argument to order four.

Dependencies: the explicit complete zero-orbit expansion used in
`reviews/C/pass4-math-completion/proofs/XI_SOURCE_REPAIR.md`; for an application
to xi, the published finite-height theorem and a source-bound all-height zero
count, plus certified existence of the stated critical pairs. Numerical zero
verification is not rerun here. No assumption of RH is used in the lemmas.

## 1. Source and normalization

Let an even real entire function have critical pairs `+/- i gamma` and
off-line quartets `+/- a +/- i b`, with analytic multiplicities. Write

\[
p(t)=\sum_{\rm critical}\frac{2m}{t+\gamma^2}
       +\sum_{\rm off}\frac{4m(t+b^2-a^2)}{(t+b^2-a^2)^2+4a^2b^2},
\quad F(x)=xp(x^2),\quad K(x,y)=\frac{F(x)+F(y)}{x+y}.
\]

The source identity `F=E'/E` is an explicit hypothesis, or is obtained from
the complete genus-zero expansion in the cited repair. It requires complete
zero correspondence and growth, not a finite zero table. Suppose every
off-line representative satisfies `0<a<=A`, `b>H>A`, and

\[
N_+(T)\le T\log T\quad(T\ge H),
\]

where `N_+` counts all upper-half-plane zeros with multiplicity. The selected
off-line representatives are a subset, so Stieltjes partial summation gives

\[
S_4:=\sum_{\rm off}\frac{m}{b^4}
\le\frac{4(3\log H+1)}{9H^3}.                         \tag{1}
\]

Indeed the boundary term at infinity vanishes, the term at H is nonpositive,
and `4 integral_H^infty log(u)/u^4 du` is the displayed expression.

## 2. A sharp height-to-derivative sign lemma

For one quartet put `c=b^2-a^2`, `B=2ab`. For every integer `k>=0`,

\[
(-1)^kq^{(k)}(t)
=4m k!((t+c)^2+B^2)^{-(k+1)/2}
 \cos\bigl((k+1)\arctan(B/(t+c))\bigr).               \tag{2}
\]

Since `arctan(B/c)=2 arctan(a/b)` when `a<b`, the right side is strictly
positive at every `t>=0` whenever

\[
2(k+1)\arctan(A/H)\le\pi/2.                         \tag{3}
\]

Strict positivity holds even at equality in (3), since `b>H`. Termwise
differentiation follows from the same fixed-order locally uniform convergence
as the source repair. Every critical term has all alternating signs strictly
positive. Thus the complete source has all signs through any integer `k`
satisfying (3), provided at least one source atom is present.

This threshold is sharp for a *single* quartet on the complete `t>=0` axis:
if `(k+1) arctan(B/c)>pi/2`, its angle varies continuously from that value
down to zero, and intersects an interval where cosine is negative. This is
true even when the angle at zero lies beyond a whole period.

For `H=3*10^12`, the strip `A<=3/8` improves the elementary sufficient
derivative-order range by a factor 4/3 over `A<=1/2`. Neither finite
alternating derivative signs nor all scalar derivative signs alone imply a
finite Pick matrix is positive; the following theorem uses an actual Gram
lower bound.

More explicitly, `arctan(v)<v` and `pi>3` prove every alternating derivative
sign for `0<=k<=6*10^12-1` with A=3/8, or
`0<=k<=45*10^11-1` with the classical A=1/2. These are finite analytic
conclusions from (2), not numerical evaluations of such enormous derivatives.

## 3. A signed-shadow estimate that survives node collisions

Replace every off-line quartet `(a,b,m)` by the critical pair at `b` with
multiplicity `2m`. Its kernel is positive semidefinite. Call the difference
between the true and shadow kernels `D_{a,b,m}(x,y)`.

The odd logarithmic derivative of the quartet is

\[
F_{a,b,m}(z)=m\sum_{\epsilon,\eta=\pm1}
                  \frac1{z-\epsilon a-\eta ib}.
\]

For real `z`, every denominator has modulus at least `b`. A central second
difference in `a`, with its integral remainder, gives for `k>=1`

\[
|F_{a,b,m}^{(k)}(z)-F_{0,b,m}^{(k)}(z)|
\le \frac{2ma^2(k+2)!}{b^{k+3}}.                    \tag{4}
\]

Here `F_{0,b,m}` contains the four terms at a=0, hence is the logarithmic
derivative of the multiplicity-2m critical shadow. For example k=1 has the
constant 12, without a lost factor from the two conjugate poles.

Oddness removes the apparent singularity at x+y=0:

\[
D_{a,b,m}(x,y)=\int_0^1
   (F_{a,b,m}'-F_{0,b,m}')(\theta x-(1-\theta)y)\,d\theta.
\]

Differentiating i times in x and j times in y, applying (4), and using
`integral theta^i(1-theta)^j = i!j!/(i+j+1)!`, gives

\[
\frac{|\partial_x^i\partial_y^jD_{a,b,m}(x,y)|}{i!j!}
\le\frac{2ma^2(i+j+3)(i+j+2)}{b^{i+j+4}}.             \tag{5}
\]

The same bound holds for mixed divided differences on arbitrary real nodes,
including their continuous confluent limits, by the integral formula for
divided differences. This is a signed-source estimate: the discarded part
is the exact difference from a positive shadow, not an unrelated source.

## 4. Uniform finite-order compact Pick positivity

Fix `M>=1`, `n=2M`, and M distinct critical pairs. Write their squared
ordinates as `0<r_1<...<r_M` and use just one coefficient unit of each pair.
Let `X>0`, `0<x_i<=X`, and let `S>0` with `H>=2S`. Define

\[
\begin{split}
T&=4\sum_{j=1}^M\sum_{i=0}^{n-1}\frac{S^{2i}}{r_j^{i+1}},\\
d&=\frac{2^nS^{n(n-1)}\prod_jr_j
                     \prod_{j<k}(r_k-r_j)^4}
             {\prod_j(X^2+r_j)^{2n}},\\
\eta&=12n A^2 S_4.
\end{split}                                                        \tag{6}
\]

**Theorem.** If

\[
\boxed{\frac{(n-1)^{n-1}d}{T^{n-1}}>\eta,}             \tag{7}
\]

then every n-node kernel K on `[0,X]` is positive definite at distinct
nodes. Packets of size at most n, including repeated nodes, are PSD. The
statement concerns this compact interval, not the unbounded axis.

**Proof.** For distinct nodes, apply the invertible Newton divided-difference
congruence: row i takes the divided difference on the first i+1 nodes, then
is multiplied by `S^i`. Each selected critical pair contributes the Gram
kernel of the two functions

\[
\sqrt2\frac{\sqrt{r_j}}{x^2+r_j},\qquad
\sqrt2\frac{x}{x^2+r_j}.
\]

Their i-th derivatives divided by i! have modulus at most
`sqrt(2)*r_j^{-(i+1)/2}`, as follows directly from partial fractions at
`+/- i sqrt(r_j)`. Thus the trace of the transformed selected-anchor Gram
matrix is at most T.

The untransformed anchor determinant is exactly

\[
\det G=
\frac{2^n\prod_jr_j\prod_{j<k}(r_k-r_j)^4
              \prod_{i<k}(x_k-x_i)^2}
     {\prod_i\prod_j(x_i^2+r_j)^2}.                  \tag{8}
\]

To check (8), multiply row i of the feature matrix by
`prod_j(x_i^2+r_j)`. Its columns become the even and odd polynomials
`sqrt(r_j) prod_{k!=j}(x^2+r_k)` and
`x prod_{k!=j}(x^2+r_k)`. Their coefficient determinant has square
`prod_j r_j prod_{j<k}(r_k-r_j)^4`; the ordinary monomial evaluation
determinant is the Vandermonde. Include the factor `2^n` from the Gram
normalization. The Newton congruence removes exactly the Vandermonde square;
the S scaling supplies `S^{n(n-1)}`. Therefore the transformed determinant
is at least d.

If its eigenvalues are `0<lambda_1<=...<=lambda_n`, AM-GM gives
`lambda_2...lambda_n <= (T/(n-1))^(n-1)`, hence
`lambda_1 >= (n-1)^(n-1)d/T^(n-1)`.

For k=i+j, (5) after S scaling is bounded by

`2ma^2 (k+3)(k+2)(S/b)^k/b^4 <=12ma^2/b^4`.

The last inequality holds for every integer k>=0 when S/b<=1/2: the ratio
`(k+3)(k+2)/2^k` is at most 6 (equal at k=0,1 and decreasing afterwards).
Summing the complete off-line source bounds every transformed error entry
by `12A^2S_4`; the operator norm is at most n times that quantity. All
unused actual critical pairs and all shadows remain PSD under the same
congruence. Inequality (7) now proves strict positivity.

For smaller packets, append distinct nodes in `[0,X]` and restrict. Repeated
nodes follow by the exact coefficient-summing congruence, not by identifying
duplicate evaluations with derivatives. QED.

For interval anchor enclosures `r_j in [l_j,u_j]` with `u_j<l_{j+1}`, replace
the numerator of d by `prod l_j prod(l_k-u_j)^4`, its denominator by
`prod(X^2+u_j)^(2n)`, and r_j in T by l_j. This is a deliberately conservative
exact rational sufficient inequality.

## 5. Why the original single reserve cannot simply extend to order four

Take one critical pair of squared ordinate r and multiplicity e, and one
quartet of multiplicity m. Write c=b^2-a^2 and h=4a^2b^2. Its moments are

\[
\mu_0=2e+4m,\quad \mu_1=2er+4mc,\quad
\mu_2=2er^2+4m(c^2-h),\quad
\mu_3=2er^3+4m(c^3-3ch).
\]

For any four distinct fixed positive `u_i`,

\[
\det K(Lu_i,Lu_j)=
\frac{(\mu_0\mu_2-\mu_1^2)(\mu_1\mu_3-\mu_2^2)
              \Delta(1/u)^2}
     {L^{20}\prod_i u_i^2}+O(L^{-22}).               \tag{9}
\]

Proof: set z=1/x. After extracting row and column factors z, the analytic
kernel starts with the coefficient matrix on monomials 1,z,z^2,z^3

\[
\begin{pmatrix}
\mu_0&0&-\mu_1&0\\0&\mu_1&0&-\mu_2\\
-\mu_1&0&\mu_2&0\\0&-\mu_2&0&\mu_3
\end{pmatrix}.
\]

Its determinant is the product in (9). Antisymmetry supplies the two
Vandermonde factors. The next homogeneous degree is two larger, because
the kernel is even under simultaneous (z,w) sign reversal.

The factors satisfy

\[
\begin{split}
D_0&=8m\{e[(c-r)^2-h]-2mh\},\\
D_1&=8m\{er[c(c-r)^2-h(3c-2r)]-2mh(c^2+h)\}.
\end{split}                                                       \tag{10}
\]

For fixed a,r,m and b tending to infinity, positivity of D1 requires
asymptotically `e>=8ma^2/r`. This cost does not decay with b. The earlier
order-three reciprocal-curvature share costs only `O(ma^2/b^2)`.
Therefore its summable fixed-reserve ledger is insufficient at order four.

An exact countermodel satisfying the repaired source conditions has

`H=1024, r=200, e=1, a=3/8, b=1025, m=256`.

The even polynomial is

\[
E(z)=(1+z^2/200)
 \left(\frac{(z^2+c)^2+h}{c^2+h}\right)^{256}.
\]

It has exact prescribed multiplicities, no omitted zeros, order zero,
and nonzero value at zero. Its off-line budget is
`256/1050625<2/H<2(log H+1)/H`. Its complete upper-zero count is at most
513, hence `N_+(T)<=T log T` for every T>=1024. It obeys the narrower
quasi-RH-compatible horizontal strip `a<=3/8`. Yet

`D_0=4518253421430481/2>0`,

`D_1=-3346984876045740972698225/16<0`.

At `x=(10250,20500,30750,41000)` its exact four-node determinant is
negative, while every principal minor of size at most three is positive.
Equation (9) also gives an entire cofinal family of negative packets.
This is a synthetic counterexample to an inference from the listed source
hypotheses, never a claim about an actual xi zero or actual negative xi matrix.

## 6. Current remaining gaps

The compact theorem needs an independent audit of the signed-shadow
normalization and determinant formula. Its actual-xi specialization needs
directed critical-pair existence certificates and explicit binding to the
finite-height/counting sources. Increasing n or X requires checking (7),
not extrapolating a table. It does not transport compact positivity to all
orders or the complete positive axis.
