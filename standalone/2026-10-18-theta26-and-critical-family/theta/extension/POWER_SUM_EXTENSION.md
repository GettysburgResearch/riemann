# Exact power-sum extension, collision coordinates, and all-order consumers

**Status.** The results proved below are finite-dimensional identities,
quantitative conditional extension lemmas, and conditional all-order consumers.
They do not establish a cofinal family for theta, RH, or a new zeta strip.
Ordinary-Decimal continuation records are exploratory producers. The separately
directed degree-22/24/26 certificates are described in `../PROOF_GAUSSIAN.md`.

The use of Stieltjes moments to detect real zeros belongs to the classical
Grommer/moment-criterion tradition; no novelty is claimed for that criterion.
The new purpose here is to make the construction freedoms and their exact
acceptance tests explicit in the repository's normalization.

## 1. Normalization and removal of the Gaussian-reserve condition

Let H be an even real entire target with H(0)=1 and H''(0)=-1. Near zero write

\[
 \log H(z)=-\frac{z^2}{2}-\sum_{r\ge2}\frac{q_r}{r}z^{2r}.
 \tag{P1}
\]

For the standardized theta observable, these numbers are

\[
 q_r=\frac{(-1)^{r+1}r\,\kappa_{2r}}{(2r)!}.
 \tag{P2}
\]

For any finite collection of nonzero complex numbers b_j, closed under
conjugation, put

\[
 P(z)=\exp\!\left[-\left(\frac12-\sum_jb_j\right)z^2\right]
       \prod_j(1-b_jz^2)
     =e^{-z^2/2}\prod_j (1-b_jz^2)e^{b_jz^2}.
 \tag{P3}
\]

Thus matching coefficients through degree 2n is precisely

\[
 \sum_j b_j^r=q_r,\qquad 2\le r\le n.
 \tag{P4}
\]

The Gaussian coefficient a=1/2-sum b_j is real but need not be nonnegative.
Indeed, for every complex w,

\[
 |(1-w)e^w|^2=(1-2\Re w+|w|^2)e^{2\Re w}
          \le e^{|w|^2},
 \tag{P5}
\]

using 1+t<=e^t. Consequently

\[
 \boxed{\quad |P(z)|\le
   \exp\!\left(\frac{|z|^2}{2}+
                    \frac{|z|^4}{2}\sum_j|b_j|^2\right).\quad}
 \tag{P6}
\]

For positive real b_j, the sum in (P6) is exactly the already matched q_2.
It is therefore unnecessary to keep sum b_j bounded, keep a nonnegative,
or represent P as the Fourier transform of a positive law.

**Cofinal real-root consumer.** If finite positive real node sets satisfying
(P4) exist for unbounded n, the associated P converge locally uniformly to H,
and every zero of H is real. To prove this, (P6) gives a common bound on every
compact set. Any subsequential entire limit has all Taylor coefficients of H,
hence equals H. The normal-family argument then gives convergence of the full
sequence. Hurwitz on each disk disjoint from the real axis gives the zero
claim, since H(0)=1 excludes the identically zero limit.

This is a conditional consumer. Neither the existence of one finite model nor
positive Hankel matrices at a finite list of orders proves its hypothesis.
The companion `../WEIGHTED_CANONICAL.md` proves a stronger half-plane consumer
which permits arbitrary positive weights, by keeping the fractional factors
holomorphic on each open half-plane and proving convergence on the imaginary
axis directly. The unit-node constructions below remain useful because their
finite approximants are entire and have a global zero-location theorem.

## 2. An exact moving-anchor flow

Suppose a finite positive real node set matches powers 2 through m+1, and
choose m distinct active nodes alpha_1,...,alpha_m>0. All other nodes are held
fixed. Add L identical new nodes x, with L a positive integer, and retune the
active nodes beta_i(x) so that

\[
 \sum_{i=1}^m\beta_i(x)^r+Lx^r
       =\sum_{i=1}^m\alpha_i^r,
 \qquad r=2,\ldots,m+1,\qquad \beta_i(0)=\alpha_i.
 \tag{P7}
\]

At x=0, the Jacobian is a nonzero diagonal multiple of a Vandermonde matrix,
so there is a unique local analytic branch. Define its Lagrange cardinal
polynomials

\[
 \ell_i(t)=\prod_{j\ne i}\frac{t-\beta_j}{\beta_i-\beta_j}.
 \tag{P8}
\]

As long as the beta_i remain distinct and positive, the exact ODE is

\[
 \boxed{\quad \beta_i'(x)=-\frac{Lx}{\beta_i(x)}\ell_i(x).\quad}
 \tag{P9}
\]

**Proof.** Differentiate (P7), divide its r-th row by r, and insert (P9).
The required identity is
sum_i beta_i^(r-2) ell_i(x)=x^(r-2), which is Lagrange interpolation of a
polynomial of degree at most m-1. Conversely, the derivative system has a
unique solution while its Vandermonde determinant is nonzero. QED.

Define the gain in the next power and the retuned Gaussian coefficient by

\[
 \begin{split}
 A(x)&=Lx^{m+2}+\sum_i\beta_i(x)^{m+2}-\sum_i\alpha_i^{m+2},\\
 a(x)&=a(0)-Lx-\sum_i(\beta_i(x)-\alpha_i).
 \end{split}
 \tag{P10}
\]

They have the exact derivatives

\[
 \boxed{\quad A'(x)=L(m+2)x\prod_i(x-\beta_i(x)),\qquad
 a'(x)=-L\prod_i\left(1-\frac{x}{\beta_i(x)}\right).\quad}
 \tag{P11}
\]

For the first identity, the interpolation error for t^m is
t^m-sum_i beta_i^m ell_i(t)=prod_i(t-beta_i). For the second, the polynomial
1-t sum_i ell_i(t)/beta_i has value one at zero and vanishes at every beta_i;
it therefore equals prod_i(1-t/beta_i).

While 0<x<min beta_i(x), the next-power gain is strictly monotone with sign
(-1)^m, and

\[
 a(0)-Lx\le a(x)\le a(0).
 \tag{P12}
\]

Equation (P12) is useful accounting, although Section 1 removes any need for
a(x)>=0. Where x>0, the exact gain per decrease in a is

\[
 \frac{dA}{d(-a)}=(-1)^m(m+2)x\prod_i\beta_i(x).
 \tag{P13}
\]

The nodes have unit multiplicities throughout; L is an integer. No fractional
power of a polynomial has been introduced.

## 3. A quantitative acceptance test

Choose delta>0 with

\[
 \delta<\tfrac14\min_i\alpha_i,\qquad
 2\delta<\min_{i\ne j}|\alpha_i-\alpha_j|.
 \tag{P14}
\]

For m=1 the second condition and all empty products are omitted. Put

\[
 K_i=\prod_{j\ne i}
       \frac{\alpha_j+\delta}{|\alpha_i-\alpha_j|-2\delta}.
 \tag{P15}
\]

Let tau be any positive number satisfying

\[
 \tau<\min_i(\alpha_i-\delta),\qquad
 \frac{L\tau^2K_i}{2(\alpha_i-\delta)}<\delta
 \quad\hbox{for every }i.
 \tag{P16}
\]

Then the branch (P7) exists on the whole interval [0,tau], stays in
|beta_i-alpha_i|<delta, and

\[
 (-1)^m A(\tau)\ge
 C:=\frac{L(m+2)\tau^2}{2}
      \prod_i(\alpha_i-\delta-\tau)>0.
 \tag{P17}
\]

Consequently, every next-power deficit Delta with

\[
 0<(-1)^m\Delta\le C
 \tag{P18}
\]

is filled at a unique x in (0,tau], while preserving all old matched powers
and retaining positive real nodes. If a positive Gaussian coefficient is
separately wanted, adding the optional constraint Ltau<a(0) guarantees it.

**Proof.** Until the first exit from the delta box, all beta_i stay positive
and separated. For 0<=x<=tau, x<beta_j, so
|x-beta_j|<=alpha_j+delta, and hence |ell_i(x)|<=K_i. Equation (P9) gives

\[
 |\beta_i(x)-\alpha_i|
 \le\frac{Lx^2K_i}{2(\alpha_i-\delta)}<\delta.
 \tag{P19}
\]

This rules out the first exit. The ODE has a smooth bounded vector field on
a compact neighborhood of this box, so continuation cannot fail before tau.
Every factor beta_i(x)-x is at least alpha_i-delta-tau. Integrating the
signed version of (P11) proves (P17); strict monotonicity and the intermediate
value theorem give (P18). QED.

These inequalities can be checked with rational intervals enclosing a
certified starting root. If they fail, no mathematical impossibility follows:
they are deliberately sufficient bounds for a chosen chart. A sharper
interval continuation or changing active anchors can produce a larger range.

## 4. Passing a real-root collision through conjugate coordinates

Replace two selected nodes by

\[
 b_\pm=u\pm\sqrt d,\qquad u>0,
 \qquad C_r(u,d)=b_+^r+b_-^r
     =2\sum_{k=0}^{\lfloor r/2\rfloor}
           {r\choose2k}u^{r-2k}d^k.
 \tag{P20}
\]

Every C_r is a real polynomial. A collision is d=0; negative d represents
the conjugate pair u+i sqrt(-d), u-i sqrt(-d). Equivalently, with s=2u and
p=u^2-d, one can use C_0=2, C_1=s, and C_r=sC_(r-1)-pC_(r-2).

**Collision chart lemma.** Suppose the other m-2 selected nodes gamma_j are
positive, mutually distinct, and different from u>0. The Jacobian of powers
r=2,...,m+1 in the coordinates gamma_1,...,gamma_(m-2),u,d is invertible at
d=0. Thus the exact power constraints have a real analytic local continuation
through that collision. A continuation with d<0 has exactly the conjugate
pair specified in (P20); no root location claim beyond this is automatic.

**Proof.** At d=0 the pair columns in row r are
2r u^(r-1) and r(r-1)u^(r-2). Divide row r by r. From the d column subtract
1/(2u) times the u column, then factor out 2u from the latter column, u from
the former, and gamma_j from each simple-node column. The remaining matrix is
the confluent Vandermonde matrix on the simple nodes gamma_j and the double
node u, with powers 0 through m-1. Up to the ordering sign its determinant is

\[
 2u^2\!\left(\prod_{r=2}^{m+1}r\right)
 \left(\prod_j\gamma_j\right)
 \left(\prod_{i<j}(\gamma_j-\gamma_i)\right)
 \left(\prod_j(u-\gamma_j)^2\right),
 \tag{P21}
\]

which is nonzero. The analytic implicit-function theorem proves the claim.
QED.

The next-power derivative (P11) remains valid, with the two pair factors
replaced by ((x-u)^2-d). This follows first away from the collision by the
same polynomial interpolation argument, then at the collision by continuity.
For d<0 that factor is positive. If all other selected nodes exceed x, the
same parity sign is retained.

### Exact physical strip cost

Let v be the unstandardized theta variance, so that physical xi coordinates
are z_phys=z_std/sqrt(v). For d<0 put r=|b_+|=sqrt(u^2-d). The four zeros
associated with the pair have

\[
 |\Im z_{\rm std}|^2=\frac{r-u}{2r^2},\qquad
 |\Im z_{\rm phys}|^2=\frac{r-u}{2vr^2}.
 \tag{P22}
\]

Thus a physical half-width B is equivalent to r-u<=2vB^2r^2. In the (s,p)
coordinates this is 2sqrt(p)-s<=4vB^2p. If u>0, it can also be certified
without square roots by

\[
 p\le (u+2vB^2p)^2,\qquad p=u^2-d>0.
 \tag{P23}
\]

The pair contributes 2r^2 to T=sum_j |b_j|^2 and 2(u^2+d) to sum_j b_j^2.
Their difference is exactly -4d=4(Im b_+)^2. Equation (P6) therefore remains
an explicit normality bound throughout such a continuation.

## 5. An automatic normality barrier for strip-preserving collisions

Consider any finite collection of positive real nodes and conjugate pairs,
with real Gaussian coefficient as in (P3). Suppose all pair zeros lie in the
fixed physical strip of half-width B, and put

\[
 T=\sum_j|b_j|^2,\qquad q=\sum_j b_j^2=q_2>0,
 \qquad c=vB^2.
 \tag{P24}
\]

For a pair b=u+iy, r=|b|, (P22) gives r-u<=2cr^2. Hence
y^2=(r-u)(r+u)<=4cr^3, and

\[
 T-q=4\sum_{\rm pairs}y^2
 \le16c\sum_{\rm pairs}r^3
 \le4\sqrt2\,c\,T^{3/2}.
 \tag{P25}
\]

The last step uses sum r^3 <= (sum r^2)^(3/2) and 2sum r^2<=T.
No unproved variance or first-power estimate is used.

Consequently, if a continuous strip-preserving path starts with all nodes
real, fixes q, and if R>q satisfies

\[
 R-4\sqrt2\,cR^{3/2}>q,
 \tag{P26}
\]

then T<R everywhere on the path. Otherwise its first passage through R
contradicts (P25). Adding zero nodes and passing between real/conjugate pair
coordinates is allowed when T remains continuous.

For the directed theta source, v<4621/100000 and q_2<17409/1000000. With
B=1/3, take R=7/400. Since 4sqrt(2)<6 and sqrt(R)<133/1000,

\[
 R-6\left(\frac{4621}{900000}\right)
       R\left(\frac{133}{1000}\right)
       -\frac{17409}{1000000}
 =\frac{1157849}{60000000000}>0.
 \tag{P27}
\]

Every such path from the certified real-node model therefore has T<7/400,
and its entire functions obey the uniform bound

\[
 |P(z)|\le\exp\left(\frac{|z|^2}{2}+\frac{7|z|^4}{800}\right).
 \tag{P28}
\]

A cofinal collection of exact theta matches on these paths would imply
physical zero confinement to |Im z_phys|<=1/3, hence the zeta boundary 5/6.
The cofinal construction and its strip-preserving continuation are open;
the barrier supplies normality only after those hypotheses hold.

## 6. Positive moment weights: a valid all-order consumer and a finite pitfall

There is a second all-order route which does not require unit root
multiplicities. Set s_k=q_(k+2). Assume both finite matrices

\[
 (s_{i+j})_{i,j=0}^N\succeq0,\qquad
 (s_{i+j+1})_{i,j=0}^N\succeq0
 \quad\hbox{for every }N\ge0.
 \tag{P29}
\]

The classical Stieltjes moment theorem supplies a positive measure nu on
[0,infinity) with s_k=int t^k dnu(t). One primary proof, including degenerate
cases, is Zagorodnyuk, Theorem 2, cited below.

**All-order log-derivative consumer.** Under (P29), an even entire H with
(P1) has only real zeros.

**Proof.** Define the entire function F(w) by H(z)=F(z^2). Since F(0)=1,
its logarithmic derivative is analytic in some disk about zero. Cauchy's
coefficient estimate in that disk bounds |s_k|<=C M^k for finite constants
C,M. The representing measure is compactly supported: any positive mass on
[M+epsilon,infinity) would contradict that estimate as k tends to infinity.
Enlarging M if necessary causes no problem.

For sufficiently small w, the power series and geometric expansion give

\[
 -\frac{F'(w)}{F(w)}
   =\frac12+w\int_{[0,M]}\frac{d\nu(t)}{1-tw}.
 \tag{P30}
\]

The right side is analytic on the slit domain C minus [1/M,infinity),
interpreting M=0 separately. It agrees there with the left side as a
meromorphic function, by the identity theorem. A zero of F in that domain
would create a pole of -F'/F, which is impossible. Thus every zero of F is
positive real, and every zero of H is real. When M=0 the right side is a
polynomial and F is zero-free; the conclusion remains valid. QED.

Entireness is essential in this argument. It is what makes the logarithmic
derivative meromorphic with residues equal to negative integer zero
multiplicities. Directly exponentiating an arbitrary finite positive-weight
measure need not give an entire function, so it is not a substitute for
checking the entire target's all-order condition (P29).

### Why finite Hankel positivity does not produce unit nodes

For unit positive nodes, p_2=sum b_j^2 and p_3=sum b_j^3 necessarily satisfy

\[
 p_3\le p_2^{3/2}.
 \tag{P31}
\]

Indeed b_j<=sqrt(p_2) for every j. But take the positive measure equal to
one half of the uniform probability law on [9/20,11/20]. Its moments are

\[
 p_1=\frac14,\quad p_2=\frac{301}{2400},\quad
 p_3=\frac{101}{1600},\quad
 p_3^2-p_2^3=\frac{27814499}{13824000000}>0.
 \tag{P32}
\]

Every finite Hankel matrix of this measure, including shifted matrices and
the usual interval interior localizers, is strictly positive definite: its
quadratic form is the integral of a nonzero polynomial squared against a
strictly positive density on an interval. Nevertheless even its p_2,p_3
cannot be represented by unit nodes. Its p_1 also leaves positive reserve
under the normalization 1/2, so reserve is not the obstruction.

Nor can finite Hankel positivity force the parity sign in (P18). At m+1
distinct positive nodes, the matrix of powers 2 through m+1 has a
one-dimensional nullspace in its weights, and the next-power row does not
vanish on that nullspace, by the Vandermonde determinant. Perturb weights
1+epsilon v_j with either sign of sufficiently small epsilon. All weights
remain positive, all old powers are fixed, and the next power moves in
opposite directions. For any specified finite matrix order, sufficiently
many distinct support points make the relevant matrices strictly positive.
Thus a missing residual-sign theorem must use information beyond those
finite positivity conditions and that choice of starting model.

Normalized equal-weight quadrature results have a related bookkeeping
limitation: a quadrature with n equal weights for a measure of mass M has
weights M/n. Root multiplicities in (P3) must be integers. A common rescaling
of nodes cannot absorb M/n simultaneously in multiple powers. Peled's
quadrature and inverse-mapping results are relevant tools, but do not by
themselves remove this integrality constraint in a direct finite product.
This limitation does not invalidate the different all-order consumer (P30).

## 7. Experiment status and reproducibility

`extend_power_sums.py` follows (P7) by 150-digit Decimal Newton correction,
changes active anchors when a chart approaches collision, and applies a
safeguarded square Newton refinement after observing a scalar crossing.
Its default input is the final sibling `../gaussian_parameters.json`, rather
than an optimizer history. NumPy/SciPy are used only for exploratory active
chart selection; the two finite algebra checkers are standard-library Python.

The first-stage target deficit is approximately +5.46785696955e-23, in the
permitted direction because m=10. With at most 30 anchor changes, clouds of
one, four, eight, twelve, and sixteen roots close approximately 11.4, 43.3,
64.2, 76.5, and 94.5 percent of that deficit. Those runs stop at selected-chart
collisions or the chosen switch budget. Their stopping points do not prove
infeasibility. Allowing further chart changes and larger integer clouds
produces completed endpoints:

| Stage | Initial nodes / degree | Added equal roots | Final nodes / degree | Anchor changes | Gaussian coefficient a |
| --- | --- | --- | --- | --- | --- |
| First extension | 64 / 22 | 20 | 84 / 24 | 35 | 0.06523527090 |
| First extension, alternative | 64 / 22 | 24 | 88 / 24 | 27 | 0.06383584250 |
| First extension, alternative | 64 / 22 | 32 | 96 / 24 | 21 | 0.06135387248 |
| Second extension | 84 / 24 | 20 | 104 / 26 | 20 | 0.05779857340 |
| Second extension, alternative | 84 / 24 | 64 | 148 / 26 | 16 | 0.04946766286 |

The next deficit at the 84-node producer is approximately
-1.18908833328e-25, again in the permitted direction, now because m=11.
Thus the numerical experiment supplies an actual two-step chain
64/degree22 -> 84/degree24 -> 104/degree26, adding twenty factors at each step.
The complete curated endpoints are `power_extension_candidates.json` and
`power_extension26_candidates.json`; these files contain source/input hashes,
the crossing summaries, all nodes, and independently recomputed midpoint
residuals. The relative residuals of the chosen 84- and 104-node centers are
below 1.3e-148 and 8.6e-134, respectively.

The trajectory remains numerical. The separate sibling `check_incremental.py`
uses directed arithmetic to certify the endpoint existence statements; a
successful endpoint certificate does not certify every intermediate flow
segment or establish the all-order hypotheses. In particular, the 104-node
producer starts from the numerical 84-node center. Exact degree-24 existence
near that center is a separate statement and is not silently substituted
for a certified connecting path.

`continue_conjugate_pair.py` replaces the closest active pair by (u,d) and
continues the same complete power system across d=0, recording physical strip
width and T. The one- and four-root paths do pass through a conjugate collision
while preserving the old powers numerically, but hit the physical 1/3 strip
budget with deficits still about 4.84235e-23 and 3.09544e-23. The permitted
complex continuation gives only a small extra gain for these pairs; it does
not finish either degree-24 match. These records are ordinary-Decimal
experiments, not interval certificates. Their compact endpoints and failure
boundaries are retained in `extension_experiments.json`.

`check_power_extension.py` uses exact rational arithmetic to check the
interpolation identities on explicit rational charts, the confluent
Jacobian formula, the counterexample arithmetic, and the source-qualified
rational normality barrier. Its certificate does not establish an exact
theta root or all-order construction. The proofs above supply the general
algebraic arguments beyond the finite rational examples.

From the packet's `theta` directory, immutable-receipt replays are:

```sh
python -S extension/check_power_extension.py --output /tmp/power_identity_replay.json
python -O -S extension/check_power_extension.py --output /tmp/power_identity_optimized_replay.json
python -S extension/check_extension.py --output /tmp/graph_identity_replay.json
python -O -S extension/check_extension.py --output /tmp/graph_identity_optimized_replay.json
```

The numerical two-step producer can be rerun separately with NumPy and SciPy:

```sh
python extension/extend_power_sums.py --degree 22 --nodes 64 --cloud 20 --switch-anchors --max-switches 90 --output /tmp/degree24_cloud20.json
python extension/extend_power_sums.py --degree 24 --nodes 84 --cloud 20 --switch-anchors --max-switches 100 --parameters extension/power_extension_candidates.json --output /tmp/degree26_cloud20.json
```

Those commands produce independently checkable rational centers; they do not
prove the trajectory or promise byte-for-byte reproduction of an optimizer's
historical log on different numerical-library builds. The curated log hashes
record the actual historical inputs from which the shipped centers were
extracted. The directed endpoint checker is the mathematical acceptance gate.

### Primary references

1. J. Grommer, *Ganze transzendente Funktionen mit lauter reellen Nullstellen*,
   Journal fuer die reine und angewandte Mathematik 144 (1914), 114–166.
   [Archival record](https://geodesic.mathdoc.fr/item/JRAM_1914__144_149420/),
   DOI [10.1515/crll.1914.144.114](https://doi.org/10.1515/crll.1914.144.114).
   Historical real-zero/moment-criterion context; (P30) is proved directly here.
2. Sergey M. Zagorodnyuk, *The matrix Stieltjes moment problem: a description
   of all solutions*, New York J. Math. 18 (2012), 479–497, Theorem 2.
   [Primary paper](https://nyjm.albany.edu/j/2012/18-27p.pdf).
3. Ron Peled, *Simple universal bounds for Chebyshev-type quadratures*,
   [arXiv:0903.4625](https://arxiv.org/abs/0903.4625), especially Theorem 1.1
   and Proposition 2.5. The quantitative root-flow lemma above has its own
   proof and does not import a unit-multiplicity conclusion from that paper.
