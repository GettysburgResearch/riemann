# A usable strip class, and an obstruction to elementary cosine products

Status: **PROPOSED native mathematics, with explicit imported inputs. No new
zero-free boundary for zeta and no proof of RH are claimed.**

Scope: an unconditional obstruction to the elementary product suggested in the
research prompt; a uniform entire-function bound for a larger ferromagnetic
class with external fields; an all-order conditional strip theorem; and a
source-bound finite example with genuinely nonreal zeros.

Exact sources: the classical theta identity and finite multivariate Lee--Yang
theorem, as described in Newman--Wu [NW]; Li--Radziwill's unconditional
arithmetic-progression nonvanishing theorem [LR]; the theta primitive and source
reconstruction from repository PR #994 at
`c93ca65a510b6acaf167f929b9bf7e67d742b05a`. The mathematical theorem T20D in that
PR is a proposed finite theorem, not an integrated or independently approved
theorem. Only Section 7 below uses T20D as an explicitly stated premise.

What was actually run: `check_strip.py` reconstructs the complete theta source
using the frozen inherited arithmetic, then checks the finite example with
directed integer intervals and separately verifies a rational small-graph
high-temperature expansion by full spin enumeration. The finite example matches
only moments 2 and 4. The global theorems below are proved on paper.

Smallest remaining gap toward an improved zeta strip: construct models in
Theorem S4 at unbounded moment orders while keeping the same field/weight band
and a uniform zero-field reference variance. No such cofinal construction is
provided. Theorem S1 rules out using only independent elementary cosine factors
for that construction.

## 1. Normalization

Write

\[
 F_\theta(z)=\frac{\xi(1/2+iz)}{\xi(1/2)}
             =\mathbb E e^{izT},\qquad v=\mathbb E T^2.
 \tag{1}
\]

The symmetric theta variable T is the original, undeformed variable with
density proportional to

\[
 \Phi(t)=\sum_{n\ge1}
 (4\pi^2n^4e^{9t/2}-6\pi n^2e^{5t/2})e^{-\pi n^2e^{2t}}
 \quad(t\ge0),
 \tag{2}
\]

extended evenly. This density is positive and has every exponential moment.
The reconstruction gives

\[
 0.04620998<v<0.04621000,\qquad
 0.2088970< -\kappa_4(T)/v^2 <0.2088973.
 \tag{3}
\]

Every zero of F_theta in |Im z|<=b corresponds to a zeta zero in
`1/2-b <= Re s <= 1/2+b`. A standardized variable Y=T/sqrt(v) has characteristic
function F_theta(z/sqrt(v)); its zero-band parameter is `b*sqrt(v)`, not b.
All field/weight bands in this note use the original variable unless stated
otherwise.

## 2. The elementary product cannot converge to theta

For a>=0 and w>0 define

\[
 f_{a,w}(z)=\frac{a+\cos(wz)}{a+1}.
 \tag{4}
\]

It is the characteristic function of a symmetric variable supported on
`{-w,0,w}` with probabilities `1/[2(a+1)], a/(a+1), 1/[2(a+1)]`.

### Theorem S1: obstruction to elementary product approximation

There is **no** sequence of the form

\[
 P_n(z)=e^{-g_nz^2/2}\prod_{j=1}^{m_n} f_{a_{nj},w_{nj}}(z),
 \qquad g_n\ge0,\quad a_{nj}\ge0,\quad w_{nj}>0,
 \tag{5}
\]

that converges locally uniformly on the whole complex plane to F_theta.
There is no restriction on the factor count, widths, masses, Gaussian variance,
or zero-band widths in this theorem.

**Proof.** It is classical and unconditional that F_theta has a positive real
zero; fix one and call it gamma. No numerical zero census or RH premise is
needed. If (5) converged, Rouche's theorem on shrinking circles about gamma
would give zeros z_n of P_n with z_n -> gamma. A Gaussian has no zeros, so choose
one elementary factor f_n responsible for z_n.

Write its parameters as a_n,w_n and z_n=x_n+iy_n. If 0<=a_n<=1, every zero is
real and

\[
 w_nx_n=\pm\arccos(-a_n)+2\pi k.
\]

If a_n>1, then

\[
 w_nx_n=(2k+1)\pi,\qquad
 a_n=\cosh(w_n|y_n|).
 \tag{6}
\]

Consequently `w_n |x_n| >= pi/2` in either case. Since x_n -> gamma, w_n is
bounded below by a strictly positive constant.

There is also an upper bound. Fix R>0. For large n, |y_n|<R/2. Every symmetric
factor in (5) is at least 1 at iR, including the Gaussian. Hence

\[
 f_n(iR)\le P_n(iR)\le C_R
 \tag{7}
\]

for a finite C_R. If a_n<=1, the left side is at least `exp(R w_n)/4`. If
a_n>1, (6) gives

\[
 f_n(iR)\ge
 \frac{\cosh(Rw_n)}{1+\cosh(w_n|y_n|)}
 \ge\frac14 e^{w_n(R-|y_n|)}.
 \tag{8}
\]

Equations (7)--(8) bound w_n above. After passage to a subsequence,
`w_n -> w_*>0` and `a_n -> a_*` with 0<=a_*<=1; the last assertion follows
from (6) and y_n -> 0 whenever a_n>1.

The factors converge locally uniformly to f_{a_*,w_*}. Every zero r of this
limiting factor is approached by zeros r_n of f_n, by Rouche's theorem, including
when a_*=1 and the limiting zero is double. Since P_n(r_n)=0 and P_n converges
locally uniformly, F_theta(r)=0. In particular, the entire progression

\[
 r_k=\frac{\arccos(-a_*)+2\pi k}{w_*},\qquad k\in\mathbb Z,
 \tag{9}
\]

consists of zeros of F_theta.

But [LR, Theorem 4] states unconditionally that, for every alpha>0 and real
beta, the lower asymptotic proportion of integers l in [X,2X] with
`zeta(1/2+i(alpha*l+beta)) != 0` is at least 1/3. Apply it with
`alpha=2*pi/w_*` and `beta=arccos(-a_*)/w_*`. This contradicts (9). QED.

**Meaning.** The obstruction does not say that a finite cosine product cannot
match many theta moments. It says that such products cannot form the required
entire approximation sequence, even if the permitted band is widened. Adding
Gaussian factors does not fix the obstruction. A product containing arbitrary
correlated Lee--Yang factors is outside Theorem S1; no obstruction for that
larger class is being asserted.

### Corollary: a bounded-parameter finite-order obstruction must exist

Fix 0<=A<infinity. There cannot be a model (5) matching all theta moments through
degree 2N for every N with every a_nj<=A. To prove this, exact matching of the
second moment bounds the total variance by v. Since

\[
 f_{a,w}(it)\le\cosh(wt)\le e^{w^2t^2/2},\qquad
 w^2=(a+1)\operatorname{Var}(X)\le(A+1)\operatorname{Var}(X),
\]

the resulting products form a normal family on the entire plane. Any
subsequential limit has every theta derivative at zero and therefore equals
F_theta, contradicting S1. Thus some finite order is infeasible in this bounded
class. The proof does not give the first infeasible order.

## 3. A concrete failure of strip-only compactness

Fix b>0 and let `a_w=cosh(bw)` as w -> infinity. The zeros of f_{a_w,w} are

\[
 \frac{(2k+1)\pi}{w}\pm ib.
 \tag{10}
\]

All fixed positive moments tend to zero, since

\[
 \mathbb E X_w^{2k}=\frac{w^{2k}}{1+\cosh(bw)}\longrightarrow0.
 \tag{11}
\]

The characteristic functions converge to 1 uniformly on compact subsets of
`|Im z|<b`. At every iR with R>b they diverge to infinity, by (8). Even
convergence of every moment together with a fixed zero band therefore fails to
give whole-plane normality. This is an exact counterexample, not a numerical
warning. Its limiting distribution is the point mass at zero.

For comparison, there is an exact elementary sub-Gaussian cutoff:

### Lemma S2

For 0<=a<=2,

\[
 f_{a,w}(it)\le
 \exp\!\left(\frac{w^2t^2}{2(a+1)}\right)
 \quad(t\in\mathbb R).
 \tag{12}
\]

For a>2, this variance-sharp inequality fails for all sufficiently small
nonzero t.

**Proof.** Put h(x)=log[(a+cosh x)/(a+1)] and y=cosh x>=1. Then

\[
 h''(x)=\frac{a y+1}{(a+y)^2}\le\frac1{a+1},
\]

because the difference between the two sides after multiplying by the positive
denominators is

\[
 (a+y)^2-(a+1)(ay+1)
 =(y-1)(y+1+a-a^2)\ge0
 \quad(0\le a\le2).
\]

Integrate twice using h(0)=h'(0)=0. Conversely, the fourth cumulant is
`w^4(a-2)/(a+1)^2`, which is positive for a>2. Its Taylor contribution makes
the logarithm exceed its quadratic term near zero. QED.

This repairs compactness for an elementary class, but Theorem S1 still rules
that class out as an all-order theta approximation scheme. The next theorem
retains the useful compactness while allowing interacting models.

## 4. A larger class with external fields and a uniform entire bound

Let G be any finite graph. Take ferromagnetic couplings J_ij>=0, real fields
h_i, and observable weights w_i>=0. Put

\[
 Z(g)=\sum_{\sigma\in\{-1,1\}^{V(G)}}
 \exp\left(\sum_{ij}J_{ij}\sigma_i\sigma_j+\sum_i g_i\sigma_i\right),
 \quad Y=\sum_i w_i\sigma_i,
 \quad \varphi_h(z)=\frac{Z(h+izw)}{Z(h)}.
 \tag{13}
\]

Let `V_0=E_0 Y^2` be the variance in the **same graph with the fields set to
zero**. V_0 is not silently identified with the variance in the biased model.

### Theorem S3: field/weight strip and normality estimate

Suppose

\[
 |h_i|\le b w_i\quad\text{for every vertex},\qquad b\ge0.
 \tag{14}
\]

Then every zero of varphi_h satisfies `|Im z|<=b`, and

\[
 |\varphi_h(z)|\le
 \exp\!\left[\frac{V_0}{2}(b+|\Im z|)^2\right]
 \qquad(z\in\mathbb C).
 \tag{15}
\]

In particular a uniform bound on V_0 gives a normal family on the **entire
plane** with no bound required on the number of spins, total support,
sum |h_i|, or largest coupling.

**Proof of the strip.** The finite multivariate Lee--Yang theorem [NW] says
Z(g) is nonzero if all Re g_i are strictly positive, or all strictly negative,
for J_ij>=0. If every w_i>0 and Im z>b, then
`Re(h_i+izw_i)=h_i-w_i Im z<0` at every vertex. The other half-plane follows
with the opposite sign. If some w_i=0, (14) forces h_i=0 there. Give those
vertices temporary positive weights epsilon, with unchanged fields. Their
characteristic functions are nonzero outside the same band and converge locally
uniformly as epsilon -> 0. The value at zero stays 1, so Hurwitz's theorem
preserves zero-freeness in each open exterior half-plane.

**Proof of the bound.** First, for the zero-field observable,

\[
 M_0(u):=Z(uw)/Z(0)\le e^{V_0u^2/2}\quad(u\in\mathbb R).
 \tag{16}
\]

Here is the standard entire-function proof, to specify the input precisely.
The finite zero-field characteristic function is even, of exponential type,
normalized to 1, and by Lee--Yang has only real zeros. Hadamard factorization,
with opposite zeros paired, gives
`varphi_0(z)=prod_k(1-z^2/r_k^2)`, counting positive zeros with multiplicity and
with `sum_k r_k^-2<infinity`. Evenness removes a linear exponential factor;
exponential type excludes a quadratic one. Its second derivative at zero gives
`V_0=2 sum_k r_k^-2`. Substituting z=iu and using log(1+x)<=x proves (16).
The constant case is immediate. The temporary-weight limit handles zero
weights as above.

Second, the zero-field spin correlations are nonnegative. One can verify this
without a correlation-inequality black box: expand each edge Boltzmann factor
as `cosh(J_e)(1+sigma_i sigma_j tanh(J_e))`. The correlation of a spin set S is
the sum of nonnegative products over edge sets with odd boundary S, divided by
the analogous sum with empty odd boundary. Therefore

\[
 \frac{Z(g)}{Z(0)}
 =\sum_{S\subseteq V}\mathbb E_0\sigma_S
      \prod_{i\in S}\sinh(g_i)\prod_{i\notin S}\cosh(g_i)
 \le\frac{Z(c)}{Z(0)}
 \tag{17}
\]

whenever g is real and `|g_i|<=c_i` with c_i>=0. Indeed, replacing each sinh by
its absolute value first increases the sum, and every resulting term is
coordinatewise increasing in |g_i|.

Third, zero-field spin reversal implies `E_0 sum h_i sigma_i=0`. Jensen's
inequality gives `Z(h)/Z(0)>=1`. For real t, (14), (16), and (17) imply

\[
 M_h(t)=\frac{Z(h+tw)}{Z(h)}
 \le\frac{Z((b+|t|)w)}{Z(0)}
 \le e^{V_0(b+|t|)^2/2}.
 \tag{18}
\]

Finally `|E_h exp(izY)|<=E_h exp(-Im(z)Y)` proves (15). QED.

### An exact symmetry condition

If an involution tau of the vertex set preserves the graph, its couplings and
its weights, and `h_tau(i)=-h_i`, then Y is symmetric under the biased Gibbs
law. The map `sigma_i -> -sigma_tau(i)` preserves the Gibbs weight and changes
Y to -Y. Fields on vertices fixed by tau are necessarily zero. This gives an
even characteristic function without forming an independent reflected product.

The involution is a sufficient condition, not a claimed necessary one.

### Computing the variance resource

For a tree with q_e=tanh(J_e), the zero-field identity is

\[
 V_0=\sum_iw_i^2+
       2\sum_{i<j}w_iw_j\prod_{e\in\operatorname{path}(i,j)}q_e.
 \tag{19}
\]

It follows by choosing one fair root spin and independent edge-product signs.
Equation (19) is exact, and is a rational check if all weights and correlations
are rational. An arbitrary graph can instead use the full nonnegative
high-temperature expansions in (17), or a rigorous upper bound on their ratio.

## 5. All-order conditional strip theorem with a finite approximation bound

### Theorem S4

Fix b>=0 and V<infinity. Suppose, for arbitrarily large integers N, there is a
finite Ising model as in S3 with symmetric Y_N, field/weight band b, and
zero-field reference variance V_0,N<=V, such that

\[
 \mathbb E Y_N^{2k}=\mathbb E T^{2k}\quad(1\le k\le N).
 \tag{20}
\]

Then F_theta has no zero with |Im z|>b. Thus every nontrivial zeta zero has
`Re s<=1/2+b`; for b=1/3 this gives the boundary 5/6.

The same conclusion holds if, along such a sequence, each fixed moment tends
to the corresponding theta moment, with the same uniform b and V.

**Proof.** Bound (15) gives a uniform bound on each compact set. Montel's
theorem gives a locally uniformly convergent subsequence from any subsequence.
Derivative convergence and (20) identify every derivative at zero with
F_theta. The target is entire, so the identity theorem identifies the entire
limit. Every subsequential limit is the same, proving full locally uniform
convergence. The value at zero is 1. Hurwitz's theorem in the two open exterior
half-planes transfers the zero exclusion from S3. QED.

The field/weight and variance premises are explicit constructive requirements.
Neither the fact that each individual model has finite variance nor finite
moment matching proves their uniform cofinal form.

### A quantitative consequence at each finite order

Suppose (20) holds through 2N and write P for that finite model. For 0<R<r,

\[
 \sup_{|z|\le R}|P(z)-F_\theta(z)|
 \le
 \left(e^{V_0(b+r)^2/2}+F_\theta(ir)\right)
 \frac{(R/r)^{2N+2}}{1-(R/r)^2}.
 \tag{21}
\]

To see this, use (15) and `|F_theta(z)|<=F_theta(ir)` on the circle |z|=r,
apply the Cauchy coefficient bound to the difference, and sum its even Taylor
tail beginning at degree 2N+2. F_theta(ir) is a positive real exponential
moment, directly computable from (2). No unproved zero statement is involved.

If the S4 hypotheses hold, they additionally imply
`F_theta(ir)<=exp[V(b+r)^2/2]`, so the prefactor can be replaced by twice this
quantity. Ignoring the rational denominator in (21), the minimizing radius is
the positive solution of `r(r+b)=2(N+1)/V`, whenever it exceeds R. This explains
how to convert a finite moment result into a certified complex approximation
on an explicitly chosen domain. A root count or a global zero statement still
requires its separate complete domain argument.

## 6. An exact finite example that really has nonreal zeros

This example demonstrates that S3 is strictly larger than the real-zero class,
while retaining the correct theta scale and a small variance resource. It is
not an improvement on the degree-20 moment count.

Take one dimer with equal observable weights w/2, positive coupling J, and
opposite real fields +h,-h. Its exact characteristic function is f_{a,w}, where

\[
 q=\tanh J=\frac1{10000},\quad r=\tanh h=\frac1{32},\quad
 a=e^{-2J}\cosh(2h)
 =\frac{1-q}{1+q}\frac{1+r^2}{1-r^2}>1.
 \tag{22}
\]

Add 16 independent fair spins of equal weight u. This is a finite
ferromagnetic model with 18 observed spins and one positive edge. The involution
swaps the two dimer vertices and fixes the fair spins.

Put k=-kappa_4(T)/v^2 and define

\[
 c=2-a,\quad d=\frac18,\quad
 t=\frac{d+\sqrt{(c+d)k-cd}}{c+d},\quad
 w=\sqrt{(a+1)vt},\quad
 u=\sqrt{\frac{v(1-t)}{16}}.
 \tag{23}
\]

The complete theta intervals prove `0<t<1`, so all the weights are positive.
The dimer contributes variance vt and fourth cumulant `-c v^2t^2`. The 16
fair spins contribute variance v(1-t) and fourth cumulant
`-v^2(1-t)^2/8`. The quadratic equation in (23) gives

\[
 \mathbb E Y^2=v,\qquad \kappa_4(Y)=\kappa_4(T),
 \quad\text{hence }\mathbb E Y^4=\mathbb E T^4.
 \tag{24}
\]

The directed checker proves `h<(1/3)(w/2)` using the rational bound
`atanh(r)<r/(1-r^2)`; therefore the whole model satisfies the actual band
b=1/3. It also proves

\[
 V_0=\frac{w^2(1+q)}2+16u^2<\frac1{20}.
 \tag{25}
\]

Because a>1, this model has nonreal zeros at
`[(2j+1)pi +/- i arcosh(a)]/w`, with no cancellation by the extra cosine factors.
The checker additionally encloses their imaginary height strictly between
3/10 and 31/100 by comparing cosh(3w/10) and cosh(31w/100) against a. It checks
the lower comparison with directed exponentials. For the upper comparison it
can already use `cosh(x)>=1+x^2/2`. Thus the example has explicitly nonreal
zeros inside the desired band, not just a vacuous nonzero-field parameter.

No theta moment beyond degree 4 is claimed. Theorem S1 explains why simply
repeating these independent blocks cannot solve the full approximation task.

## 7. A local continuation of the existing degree-20 construction

This is a **conditional corollary of the proposed T20D theorem in PR #994**,
not a replay or independent approval of its 305-spin root certificate.

Assume T20D and its asserted invertible 10-by-10 active moment Jacobian.
Choose two of its 256 identical fair leaves attached to the zero-weight hub.
Give them fields `+epsilon A_0` and `-epsilon A_0`, where A_0 denotes the retuned
active weight coordinate, leaving the other fields zero. The graph and all
weights have the required swapping involution. For
epsilon sufficiently small, the analytic implicit function theorem retunes the
same ten active coordinates to keep all ten theta moments through degree 20
exact. Indeed, the finite-spin moment map is real analytic in the parameters
and fields, its Jacobian at epsilon=0 is the T20D invertible Jacobian, and all
strict positivity inequalities persist in an open neighborhood.

In standardized coordinates the field/weight ratio is exactly |epsilon|; in
the original theta coordinates it is |epsilon|/sqrt(v). The zero-field
reference variance is continuous and equals 1 in standardized coordinates at
epsilon=0, so it stays, for example, below 2 in a sufficiently small interval.

This shows that the proposed finite degree-20 realization is not confined to a
single zero-field slice. It does **not** establish that the continuation reaches
epsilon=sqrt(v)/3, any larger moment order, or an unbounded sequence of graphs.
No positive numerical radius for this local continuation is certified here.

## 8. Consequences for the next construction

The elementary product proposed in the prompt fails for an exact reason that
is independent of numerical fitting: a real zero forces a persistent periodic
factor. It should not be the main all-order model class.

External fields on an interacting ferromagnetic graph give a legitimate
replacement. The finite search can optimize three concrete quantities
together: matched theta moments, `max_i |h_i|/w_i`, and the zero-field reference
variance V_0. Symmetry can be enforced by graph involutions without doubling
the model into an independent reflected product. Theorem S3 controls the
complex growth that strip-only moment fitting misses. The remaining hard task
is a cofinal construction in this larger class; neither this note nor the
existing finite degree-20 theorem supplies it.

## References

[LR] Xiannan Li and Maksym Radziwill, *The Riemann zeta function on vertical
arithmetic progressions*, arXiv:1208.2684v1, Theorem 4 (page 3):
https://arxiv.org/pdf/1208.2684 . The theorem covers every alpha>0 and beta real;
it is unconditional. It is used only to exclude a full progression on the
critical line.

[NW] Charles M. Newman and Wei Wu, *Constants of de Bruijn--Newman type in
analytic number theory and statistical physics*, arXiv:1901.06596v2, Sections
2.1 and 2.5: https://arxiv.org/html/1901.06596v2 . The multivariate finite
ferromagnetic Lee--Yang statement and the theta Fourier normalization are the
imported inputs. The enlarged strip-class compactness theorem in this note is
proved directly; it is not inferred by applying a real-zero closure theorem to
a different class.

[T20] Repository PR #994, frozen source
`c93ca65a510b6acaf167f929b9bf7e67d742b05a`,
`standalone/2026-10-18-theta20-and-native-cancellation/theta/PROOF20.md` and
`theta_source.py`, `pr886_primitive.py`:
https://github.com/GettysburgResearch/riemann/tree/c93ca65a510b6acaf167f929b9bf7e67d742b05a/standalone/2026-10-18-theta20-and-native-cancellation/theta .
The source primitive is reused unchanged; no fresh independence of the
transcendental arithmetic backend is claimed.
