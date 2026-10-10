# Continuing the complete reunited series by conditioning on divisors

**Status:** proposed source-conditional analytic theorem. The complete
standard-face series, including its cube factor, has the normally
convergent divisor representation and continuation domain proved below.
The proof does not use an angular zero-free theorem for this complete
object. A separate corollary for the uncompleted Gauss series uses the
companion 11/12 angular result. Neither statement proves a higher moment.

**Scope:** fixed finite ray characters, the standard infinity-cusp face,
and every squarefree quadratic row k outside the fixed bad-prime set S.
All moving zero masks are retained. This is a theorem for an infinite
Dirichlet series, not an extrapolation from a finite calculation.

**Exact dependencies:** the definitions in PR #915 at
9959364671f89b86f3992ec5ed5e19f804eb607b,
REUNITED_RAMANUJAN_EULER_PRODUCT.md and
NEGATIVE_BRANCH_DIRICHLET_SERIES.md; the theta automorphy, Fourier
support, coefficient bounds, and finite local reflection identities in
the October 5 paper2.tex imported from OpenAI/math commit
adc7f1241b42e322a6451854ab7e4b4c146bf78a; and the pure plus derivative
adapter in Sections 1–2 of
[HIGHER_ANGULAR_SECOND_MOMENT.md](HIGHER_ANGULAR_SECOND_MOMENT.md).
The relevant imported interfaces are eq:T, eq:theta-local-factors,
eq:theta-support, eq:theta-mellin-functional-equation, and the absolutely
convergent dual cusp Mellin series. This proof uses those theta
interfaces, not the canonical mean-square theorem or its finite
induction. The independent review must check their stated application.

## 1. The complete object and its conditioned theta series

Use the notation of [EULER_DOMAIN_EXTENSION.md](EULER_DOMAIN_EXTENSION.md).
Thus k is squarefree, Q=Nk, and

\[
\chi^-_k=\eta\overline\alpha^3\chi_k^3,\qquad
\chi^+_k=\rho^3\alpha^3\chi_k^3,\qquad
\kappa_k=\eta\rho^3\mathbf1_{(\,\cdot\,,kS)=1}.
\tag{1.1}
\]

Let vartheta be the fixed cubic ray character in the standard cusp
coefficient, so vartheta cubed is one outside S. Define the squarefree
Gauss coefficient

\[
\mathfrak a_k(n)
 =\gamma_2(n)\rho(n)\vartheta(n)\alpha(n)\chi_k(n)^3,
\tag{1.2}
\]

with zero extension at S and k. Its absolute value is at most one, and
the exact inherited CRT identity is

\[
\mathfrak a_k(dm)
 =\mathfrak a_k(d)\mathfrak a_k(m)\chi_m(d)^4
\qquad ((d,m)=1).
\tag{1.3}
\]

For a squarefree d coprime to kS, put

\[
G_{k,d}(s)
 =\sum_m^*\frac{\mathfrak a_k(m)\chi_m(d)^4}{(Nm)^s}.
\tag{1.4}
\]

The character in (1.4) is zero when m meets d. Define the exact completed
series

\[
\begin{aligned}
\mathcal T_{k,d}(s)
 &=G_{k,d}(s)\,
   L_{S,kd}(3s-\tfrac12,\chi^+_k),\\
L_{S,kd}(r,\chi^+_k)
 &=L_{S,k}(r,\chi^+_k)
   \prod_{p\mid d}(1-\chi^+_k(p)(Np)^{-r}).
\end{aligned}
\tag{1.5}
\]

Initially these are equalities for Re(s)>1. The first line is literally
the imported definition of the completed theta series with

\[
\Psi_{k,d}(n)=
 \alpha(n)^2\rho(n)\vartheta(n)\chi_k(n)^3\chi_n(d)^4.
\tag{1.6}
\]

Indeed its squarefree coefficient is (1.2) times chi_m(d)^4, while the
cube coefficient is alpha cubed times rho cubed times chi_k cubed,
with the additional mask at d. This last assertion uses
chi_b(d) to the twelfth power as a zero mask; it is not set equal to one
when b meets d. The angular parameter of (1.6) is +2, so its theta
realization uses one plus horizontal derivative and is entire.

Every d sum below runs over squarefree d coprime to kS, where G_(k,d)
and T_(k,d) have just been defined. This is the exact restriction forced
by a_k(d), not the removal of a nonzero term.

Set

\[
r=3s-\tfrac12,\qquad v=w+3s-\tfrac32.
\tag{1.7}
\]

The complete reunited standard-face object is

\[
\mathscr R_k(w,s)
 =\sum_n^*\frac{\mathfrak a_k(n)}{(Nn)^s}
                  \mathcal F_{k,n}(w,3s-\tfrac12),
\tag{1.8}
\]

where mathcal F is the full Ramanujan allocation from the frozen source.
Equation (1.8) is initially absolutely convergent for Re(w)>1,
Re(s)>1.

## 2. A uniform bound for the conditioned completed series

### Lemma 2.1

Let

\[
A(\sigma)=\max\{0,1-\sigma,1-2\sigma\},\qquad
B(\sigma)=\max\{0,(1-\sigma)/2,1/2-2\sigma\}.
\tag{2.1}
\]

On each fixed bounded real strip, for every epsilon>0,

\[
\boxed{
|\mathcal T_{k,d}(\sigma+it)|
 \ll Q^{A(\sigma)+\epsilon}
       (Nd)^{B(\sigma)+\epsilon}(2+|t|)^M.}
\tag{2.2}
\]

Here M is finite, and the implied constant and M depend only on the
strip, epsilon, the fixed ray data, and S. In particular no k or d is
hidden in the constant. For 0<=sigma<=1 this is

\[
|\mathcal T_{k,d}(\sigma+it)|
 \ll Q^{1-\sigma+\epsilon}
       (Nd)^{(1-\sigma)/2+\epsilon}(2+|t|)^M.
\tag{2.3}
\]

**Proof.** The plus derivative realization in (1.6) gives an entire
function, with the same gamma parameters as a first horizontal
derivative. At each prime of k the finite local exponent is j=3; at
each prime of d it is j=4. These sets are disjoint. All their primes
are active. Thus the transformed denominator is c=c_0kd, where c_0
belongs to a fixed finite bad-ray family. There is no extra growing
sum over active subsets.

Cubic reciprocity identifies chi_n(d)^4 with chi_d(n)^4, because the
source's reciprocity factor has fourth power one. The exact local
factors are

\[
|B_{p,3}(\ell)|\le1,\qquad
B_{p,4}(\ell)
 =(Np)^{-1/2}\bigl(Np\,\mathbf1_{p\mid\ell}-1\bigr).
\tag{2.4}
\]

The possible unit phases in the first formula, the fixed additive
characters, and the plus derivative scalar have modulus at most one.
The scalar contributed by the cusp denominator has norm
(Nc) to the power 1-2s. The plus derivative changes its angular phase
to alpha(c) squared; it does not change that norm exponent.

Fix eta>0 and consider Re(s)=-eta. The dual series is absolutely
convergent at u=1+eta. The inherited coefficient support is
ell=unit times lambda to the m times n b cubed, with n squarefree,
and its absolute coefficient is bounded by a fixed constant times
3 to the m/6 times (Nb) to the 1/2. The ramified m sum is convergent
and contributes a fixed constant on this line.

For a good prime of norm q, the unweighted n,b majorant has local sum

\[
S_p(u)=\frac{1+q^{-u}}{1-q^{1/2-3u}}.
\tag{2.5}
\]

If p divides d, taking the absolute value in (2.4) changes its local
sum exactly to

\[
q^{-1/2}\bigl[1+(q-1)(S_p(u)-1)\bigr]
 =q^{-1/2}\bigl[1+O_\eta(q^{-\eta})
                       +O_\eta(q^{-3/2-3\eta})\bigr].
\tag{2.6}
\]

The constant term in this local sum corresponds to p not dividing nb;
all other terms correspond to p dividing nb. In particular the
positive Ramanujan branch does not cost a bare factor q.

The product of the bracketed factors at the primes of d is
O_eta,epsilon((Nd)^epsilon): separate the finitely many small prime
norms, then bound each remaining bracket by q to an arbitrarily small
positive power. The unrestricted Euler majorant at the other primes
converges for u>1. The k factors only remove terms from it.
Consequently the complete dual series on this line is

\[
\ll_{\eta,\epsilon}(Nd)^{-1/2+\epsilon}.
\tag{2.7}
\]

The theta functional equation, including its gamma ratio, now gives

\[
|\mathcal T_{k,d}(-\eta+it)|
 \ll_{\eta,\epsilon}
 Q^{1+2\eta}(Nd)^{1/2+2\eta+\epsilon}(2+|t|)^{M_\eta}.
\tag{2.8}
\]

On Re(s)=1+eta the defining Dirichlet series is bounded uniformly in
k,d,t by its absolute majorant. The Mellin realization gives finite
order in each intervening strip. The three-lines argument after a
fixed polynomial weight in t therefore applies uniformly to (2.8)
and that right-hand bound. For 0<=sigma<=1 the interpolation weight
of the left line is (1+eta-sigma)/(1+2eta). Its Q exponent is
1+eta-sigma, and its d exponent is

\[
\frac{(1/2+2\eta)(1+\eta-\sigma)}{1+2\eta}.
\]

Choosing eta sufficiently small in terms of the requested epsilon
proves (2.3), with polynomial vertical growth. No limiting
interchange in the indices k,d is needed.

On a closed left half-strip the functional equation directly gives
the exponents 1-2sigma and 1/2-2sigma; the preceding interpolation
absorbs an arbitrarily small neighborhood of sigma=0 into epsilon.
To the right of one use the absolute Dirichlet series, treating a
small neighborhood of one in the same way. These observations prove
(2.2) on every fixed bounded real strip. QED.

## 3. The exact divisor expansion and cube cancellation

At a prime p put q=Np and

\[
x=\chi^-_k(p)q^{-w},\qquad
y=\chi^+_k(p)q^{-r},\qquad
z=qxy=\kappa_k(p)q^{-v}.
\tag{3.1}
\]

Work first with Re(w)>1, Re(v)>1. Then
|x|+|z|<1, so 1-x+z has no zero. This explicit domain is important:
division by that local expression was not permitted throughout the
larger fixed-index domain of the companion Euler note.

For the old, normally convergent remainder mathcal E, the exact ratio
of its n-prime and n-free local factors is

\[
\frac{1+(q-1)x}{1-x+z}
 =1+h(p),\qquad
h(p)=\frac{qx-z}{1-x+z}
     =\frac{qx(1-y)}{1-x+z}.
\tag{3.2}
\]

Extend h multiplicatively to squarefree ideals. Since E_(k,1) is
nonzero on this domain, finite multiplication gives

\[
\mathcal E_{k,n}(w,v)
 =\mathcal E_{k,1}(w,v)\sum_{d\mid n}h(d).
\tag{3.3}
\]

For the complete object (1.8), substitute the inherited factorization
mathcal F=L(r,chi+)L(v,kappa_k)mathcal E/L(w,chi-), expand (3.3), and
write n=dm. Equations (1.3)–(1.5) then give, initially in the common
absolute-convergence region,

\[
\begin{aligned}
\mathscr R_k(w,s)
 &=\frac{L_{S,k}(v,\kappa_k)}{L_{S,k}(w,\chi^-_k)}
   \mathcal E_{k,1}(w,v)\\
 &\quad\times
 \sum_{d}^{*}
 \frac{\mathfrak a_k(d)h(d)}{(Nd)^s}
 \mathcal T_{k,d}(s)
 \frac{L_{S,k}(r,\chi^+_k)}{L_{S,kd}(r,\chi^+_k)}.
\end{aligned}
\tag{3.4}
\]

Terms with d meeting kS vanish exactly. The quotient in the last line
is initially

\[
\prod_{p\mid d}(1-y_p)^{-1}.
\tag{3.5}
\]

Combining (3.2) and (3.5) prime by prime cancels the factor 1-y:

\[
\boxed{j(p):=\frac{h(p)}{1-y_p}
                  =\frac{q x_p}{1-x_p+z_p}.}
\tag{3.6}
\]

Define j by the rightmost expression, which does not divide by 1-y.
The cancellation is an identity proved on the initial domain, so
zeros of 1-y encountered elsewhere create no exceptional rule.
The resulting exact representation is

\[
\boxed{
\mathscr R_k(w,s)
 =\frac{L_{S,k}(v,\kappa_k)}{L_{S,k}(w,\chi^-_k)}
   \mathcal E_{k,1}(w,v)
 \sum_d^*\frac{\mathfrak a_k(d)j(d)}{(Nd)^s}
                     \mathcal T_{k,d}(s).}
\tag{3.7}
\]

The cube reciprocal has disappeared from the complete object.
The reciprocal still displayed is on Re(w)>1, where its ordinary
Euler product suffices.

At a deleted prime x=y=z=0, all original local factors equal one and
h(p)=j(p)=0. Equations (3.3)–(3.7) therefore preserve the literal mask,
including every d–k and m–d exclusion.

## 4. Continuation of the full infinite series

### Theorem 4.1

Write omega=Re(w), sigma=Re(s), and v=w+3s-3/2. Define the connected
tube domain

\[
\begin{split}
\mathfrak D=\{(w,s):\;&\omega>1,\quad
                    \omega+\sigma>2,\\
                   &\omega+\tfrac32\sigma>\tfrac52,\quad
                    \omega+3\sigma>\tfrac52\}.
\end{split}
\tag{4.1}
\]

Then (3.7) is a normally convergent holomorphic representation of the
analytic continuation of (1.8) throughout mathfrak D. On every closed
subtube with bounded real parts and positive margins from the
displayed boundaries, for every epsilon>0,

\[
\boxed{
|\mathscr R_k(w,s)|
 \ll Q^{A(\sigma)+\epsilon}(2+|\Im s|)^M.}
\tag{4.2}
\]

The bound is uniform in both imaginary parts, in k, and in every
divisor index used in the proof. The constant and finite M may
depend on the closed subtube, epsilon, and the fixed ray data.

**Proof.** The last inequality in (4.1) says Re(v)>1. Therefore all
local denominators in (3.6) are nonzero. On any specified closed
subtube,

\[
|j(p)|\ll q^{1-\omega},\qquad
|j(d)|\ll_\epsilon (Nd)^{1-\omega+\epsilon}.
\tag{4.3}
\]

The first bound follows from |x|+|z|<1 with a uniform margin. The
second uses the fixed-small-prime argument and squarefreeness.
Both are uniform in the imaginary parts.

Lemma 2.1 bounds the absolute value of the d summand in (3.7) by

\[
Q^{A(\sigma)+\epsilon}(2+|\Im s|)^M
 (Nd)^{1-\omega-\sigma+B(\sigma)+2\epsilon}.
\tag{4.4}
\]

All nonzero integral ideals have a convergent norm Dirichlet sum
with exponent greater than one. Thus this majorant is summable
provided

\[
\omega+\sigma>2+B(\sigma).
\tag{4.5}
\]

By the definition (2.1) of B, (4.5) is exactly the last three
inequalities of (4.1). Choosing the intermediate epsilon smaller
than the positive margins proves normal convergence and the
uniform bound for the divisor series.

The product E_(k,1) is uniformly bounded on the present domain by
its absolutely convergent Euler majorant. L(v,kappa_k) and
1/L(w,chi-_k) are also uniformly bounded by their absolute Euler
products because Re(v),Re(w)>1. None of these bounds removes the
k mask. This proves holomorphy and (4.2).

The domain is an intersection of open real half-spaces, hence
connected, and contains Re(w)>1, Re(s)>1. The representation agrees
with (1.8) on that initial open domain. It is therefore the analytic
continuation of that same complete object. QED.

### 4.1 The actual improvement in the domain

The direct coefficient majorant in the frozen packet required
Re(s)>1 when Re(w)>1, forcing Re(v)>5/2. Theorem 4.1 passes below
that limitation.

For 0<=sigma<=1 its effective condition is

\[
\omega+\tfrac32\sigma>\tfrac52,
\qquad\text{or}\qquad
\Re v>1+\tfrac32\sigma.
\tag{4.6}
\]

For sigma<=0 it is exactly

\[
\boxed{\Re v>1.}
\tag{4.7}
\]

In the latter case omega>1 follows automatically from (4.7).
For example, sigma=-1/12, Re(v)=1+delta, and
omega=11/4+delta lie in mathfrak D for every delta>0.
This example concerns an infinite normally convergent divisor
representation, not a finite-data observation.

The theta weight has its first left Mellin pole at t=-5/6, while
t=s-1/2. Hence the range -1/3<sigma<=0 is also before that first
kernel pole. Any actual double-contour deformation must still
include its smooth transforms and fixed-ray components; the
theorem supplies the full series and vertical growth required on
these contours. It does not move across v=1.

## 5. What remains for the uncompleted Gauss series

For clarity, define the different object

\[
\mathscr G_k(w,s)
 =\sum_n^*\frac{\mathfrak a_k(n)\mathcal E_{k,n}(w,v)}
                         {(Nn)^s}.
\tag{5.1}
\]

Without its global cube factor the cancellation in (3.6) is not
available. The companion angular reciprocal theorem, at boundary
beta=11/12, does nevertheless give

\[
G_{k,d}(s)
 =\frac{\mathcal T_{k,d}(s)}
        {L_{S,kd}(3s-\tfrac12,\chi^+_k)}
\tag{5.2}
\]

as a holomorphic function for

\[
\Re s>\frac{\beta+1/2}{3}=\frac{17}{36}.
\tag{5.3}
\]

The modulus of the literal denominator, including its d mask, has
norm at most a fixed multiple of QNd. The conductor-uniform
reciprocal bound therefore preserves (2.3) with epsilon losses,
on a fixed interior of (5.3). In particular smooth Mellin inversion
gives the useful individual Gauss bound

\[
\sum_m^*\mathfrak a_k(m)\chi_m(d)^4 W(Nm/X)
 \ll Q^{1-\sigma+\epsilon}(Nd)^{(1-\sigma)/2+\epsilon}
       X^\sigma\|W\|_{C^J}
\tag{5.4}
\]

for 17/36<sigma<1 and W supported in a fixed compact interval.
The vertical bound in Lemma 2.1 and the companion reciprocal
theorem require only a finite J. This is uniform in the moving
conductors; it is not a fixed-row constant disguised as uniformity.

Equations (3.2)–(3.3), before cancelling the cube factor, now continue
(5.1) normally when 17/36<sigma<1 and
omega+(3/2)sigma>5/2. This approaches Re(v)=41/24 from the right as
sigma approaches 17/36. That smaller domain is the domain of the
uncompleted object obtained by this argument. It must not be
confused with Theorem 4.1 for the complete object.

## 6. The remaining boundary and the conductor comparison

Theorem 4.1 reaches the right of the finite-order divisor v=1. It
does not cross it. For sigma<=0, its d-series majorant at the
boundary is precisely a norm power with exponent one. Normal
convergence at that boundary therefore needs an additional
cancellation or summation theorem. The pole of L(v,kappa_k), when
kappa is principal, cannot be assigned a residue independently of
that unsummed boundary series.

There is also a precise limit to the current conductor bound.
The scalar in the literal double Mellin integral is

\[
A^{v-1}\left(\frac{Q^2}{cAB}\right)^{s-1/2}.
\tag{6.1}
\]

On sigma<=0, multiply its absolute value by the Q exponent
Q^(1-2sigma) in (4.2). The Q powers cancel exactly:

\[
\boxed{
A^{\Re v-1}(cAB)^{1/2-\sigma}\,Q^\epsilon.}
\tag{6.2}
\]

For A=B=D the D exponent is Re(v)-2sigma. In the chamber
0<sigma<1 the corresponding comparison is

\[
D^{\Re v-2\sigma}Q^{\sigma+\epsilon},
\qquad \Re v>1+\tfrac32\sigma.
\tag{6.3}
\]

In the long row range Q of order D cubed, (6.3) becomes worse as
sigma increases from zero. Equation (6.2) supplies no negative
power of Q either. Thus this new continuation does not itself
remove the long-row loss needed for the generalized moment.

One possible next arithmetic direction is explicit in (3.7):

\[
\mathfrak a_k(d)j(d)(Nd)^{-s}
 =
\frac{\gamma_2(d)\eta(d)\rho(d)\vartheta(d)
                 \alpha(d)^{-2}}
     {(Nd)^{s+w-1}}
\prod_{p\mid d}(1-x_p+z_p)^{-1},
\tag{6.4}
\]

with the retained mask at kS. The two quadratic row factors cancel
to that mask. The leading d coefficient has canonical angular
parameter -1. Its remaining dependence through T_(k,d)(s) is a
cubic twist and a cube mask, however, so it is not a product of
independent one-variable Gauss series. On Re(w),Re(v)>1 the
residual local product in (6.4) has an absolutely summable
divisor perturbation, since its error is
O(q^(-Re(w))+q^(-Re(v))). A genuine two-variable reflection or
signed d-average estimate for the remaining correlated family is
still needed to pass v=1 or obtain a conductor saving. The current
proof does not assume such a theorem.
