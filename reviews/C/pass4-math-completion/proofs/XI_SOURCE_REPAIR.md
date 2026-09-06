# C4-X: source-complete repair of the actual-Xi order-three mathematics

Status: complete proposed mathematical repair; source-level review, **not a compiled
replacement and not independent acceptance of this newly authored repair**.
Base: `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Sources: SRC-X0--SRC-X5 and SRC-U0 in `../SOURCES.tsv`.
The original formal files and their historical conditional theorems are unchanged.

<a id="X1"></a>
## X1. Correct the entire function, not just one node value

The pinned Mathlib declaration, not its inconsistent overview comment, says

\[
 \Lambda(s)=\Lambda_0(s)-1/s-1/(1-s),
 \qquad \Lambda_0\text{ entire},\qquad\Lambda_0(1-s)=\Lambda_0(s).
\]

The overview line has the opposite signs in its informal description of
Lambda0. The declaration `completedRiemannZeta_eq` and the definition's own
docstring agree with the displayed equation above. A source lock must point
to the declaration/body, not inherit the erroneous overview sign.

Define

\[
 \boxed{\xi_{\rm ent}(s)=\tfrac12+	frac12s(s-1)\Lambda_0(s).}
\tag{X1.1}
\]

For s not 0 or 1, multiplying the pinned identity by s(s-1)/2 gives

\[
 \tfrac12s(s-1)\Lambda(s)
 =\tfrac12s(s-1)\Lambda_0(s)-\tfrac12(s-1)+\tfrac12s
 =\xi_{\rm ent}(s).
\]

The replacement is entire, has values 1/2 at 0 and 1, and satisfies the
functional equation. Its centered function F(z)=xi_ent(1/2+z) is even. Equality
with the raw product holds on open neighborhoods disjoint from {0,1}, so all
derivatives agree there, not just the values.

By contrast the deposited total product is zero at 0 and 1, regardless of
Mathlib's total assignments to Lambda there. Its centered node at x=1/2 is
zero because division by zero in the total field is zero. The input field
`diagonalPositive inputs.grouped (1/2)` requires strict positivity. The old
input type is therefore empty. This confirms the prior C finding; it does not
refute the informal theorem or indicate kernel inconsistency.

`../lean/EntireXiRepair.lean` is a candidate implementation of the function-level
repair and the old point-value regression. It is deliberately outside trusted
imports and marked NOT_COMPILED. No arbitrary value is assigned directly to the
node function, and no positivity is assumed to prove the normalization.

<a id="X2"></a>
## X2. Cardinality and completeness are separate requirements

The deposited `offLineEnumeration : Nat -> ReflectedOffLineOrbit` forces a
nonempty off-line spectrum. Its injectivity forces an infinite one. Correcting
xi's removable values cannot repair that independent exclusion of RH and finite
exceptional spectra.

The membership equivalences in `GroupedActualXiC2Expansion` are not by themselves
a complete multiplicity-preserving spectrum specification. In particular:

* they compare selected lists with other selected lists, rather than asserting
  that every actual orbit occurs;
* no injectivity of the mixed `orbits` sequence is stated;
* the other-critical list is not explicitly forbidden from containing the selected
  reserve; its completeness field only addresses orbits different from that reserve.

These are observations about individual fields. They are **not** a constructed
countermodel to the full old package: its convergence-to-actual-Xi fields can
impose further restrictions, and the full input is already empty by X1. They
explain why simply replacing Nat by Option cannot authenticate the source.

A sufficient replacement is an arbitrary countable index set for each of:
(1) the selected critical orbit, recorded exactly once with multiplicity m0;
(2) all other distinct critical locations, disjoint from the selected one;
(3) all distinct right-upper off-line representatives. Membership must be
bijective onto the actual location sets and the stored multiplicity must equal
the analytic zero order. Empty and finite index sets are allowed.

An injective coding *from each index set into Nat* gives the finite exhaustion
I_N={i:code(i)<N}. This is the opposite direction from the problematic map.
Alternatively use Nat -> Option Orbit, require every orbit occurs exactly once
at a `some` entry, and give `none` the zero jet. The labels' multiplicity is a
weight, not a license to list one location repeatedly. Every finite exhaustion
must be of the same fixed source; it may not change after a hypothetical zero.

<a id="X3"></a>
## X3. Explicit spectral hypotheses for the repaired theorem

Fix H>=1024. The following are the only spectral data used below.

A selected critical location has 0<gamma0<=H/2 and integer multiplicity m0>=1;
write r0=gamma0^2. Other critical locations have gamma_j>0 and integer m_j>=1.
Off-line representatives have 0<a_i<1/2, b_i>H, integer m_i>=1. Put

\[
 c_i=b_i^2-a_i^2,\qquad B_i=2a_ib_i,
 \qquad R(t)=\frac2{t+r_0},\qquad
 q_i(t)=\frac{4m_i(t+c_i)}{(t+c_i)^2+B_i^2}.
\]

Assume the summability and global off-line budget

\[
 \sum_j\frac{m_j}{\gamma_j^2}<\infty,
 \qquad
 \sum_i\frac{m_i}{b_i^2}\le\frac{2(\log H+1)}H.
\tag{X3.1}
\]

The other-critical sum excludes the selected orbit. Define

\[
 p(t)=m_0R(t)+\sum_j\frac{2m_j}{t+\gamma_j^2}+\sum_i q_i(t).
\tag{X3.2}
\]

These are spectral hypotheses, not a zero table generated in this pass. X4
explains the exact entire-function source identification. For actual xi, the
finite-height theorem, existence of the low reserve, the coarse zero-count
bound, and classical entire growth/zero correspondence must be bound to their
own reviewed sources. None is proved by a metadata string or by the finite
checks accompanying this report.

### The tail budget has a simple independent analytic derivation

If N_+(T), counting the relevant upper zeros with multiplicity, satisfies
N_+(T)<=T log T for T>=H, then Stieltjes partial summation gives

\[
 \sum_{b_i>H}\frac{m_i}{b_i^2}
 \le -\frac{N_+(H)}{H^2}
       +2\int_H^\infty\frac{N_+(u)}{u^3}du
 \le\frac{2(\log H+1)}H.
\]

The first inequality uses that the chosen off-line representatives are a
subset of the upper zeros. For a finite cutoff T the upper boundary term
N_+(T)/T^2 tends to zero. No finite zero census substitutes for the all-height
count estimate.

The scalar budget need not remain a numerical black box. For x>=1,
log x<=sqrt x: the difference has its minimum at x=4, where it is positive
because log2<1. Hence

\[
 \frac{18(\log H+1)}H
 \le\frac{18}{\sqrt H}+\frac{18}{H}
 \le\frac{297}{512}<1\quad(H\ge1024).
\tag{X3.3}
\]

The actual pinned height 3000175332800 satisfies this elementary sufficient
condition. This proves the arithmetic inequality, not the external height theorem.

<a id="X4"></a>
## X4. Complete C2 source expansion on t>0, not only t>1/4

**Theorem X4.** The series (X3.2) and its first two derivatives converge locally
uniformly for t>=0. If an even real entire F of order strictly less than 2,
with F(0) nonzero, has exactly the multiplicity-labelled zeros

\[
 \pm i\gamma_j\quad\text{and}\quad\pm a_i\pm ib_i
\]

including the selected pair, with no omitted zeros, then

\[
 p(t)=\frac{F'(\sqrt t)}{\sqrt t\,F(\sqrt t)}\quad(t>0).
\tag{X4.1}
\]

This includes t=1/4 by the correctly defined entire F. No analytic continuation
of a sign from (1/4,infinity) to (0,infinity) is invoked.

**Proof of convergence.** Write U=t+c_i. Since H>=1024, c_i>=b_i^2/2. The
partial-fraction representation

\[
 q_i(t)=\frac{2m_i}{t+c_i+iB_i}+\frac{2m_i}{t+c_i-iB_i}
\]

gives, for j=0,1,2 and t>=0,

\[
 |q_i^{(j)}(t)|\le 2^{j+3}j!\,m_i/b_i^{2j+2}.
\]

The critical derivatives are bounded by 2j!m_j/gamma_j^{2j+2}. Summability of
m_j/gamma_j^2 implies only finitely many gamma_j<1; handle them separately.
The remaining derivatives are dominated by constants times the summable
zeroth tail. The Weierstrass M-test and differentiated-series theorem prove
C2 convergence. In fact the argument gives every fixed derivative order.
Absolute convergence makes all fixed countable reindexings legitimate.

**Proof of source identity.** Evenness gives F(z)=G(z^2) for an entire G by
its power series. Its order is less than 1. Hadamard factorization therefore
has genus zero and no nonconstant exponential factor. The product for G is

\[
 \frac{G(t)}{G(0)}=
 \prod_{\rm critical}(1+t/\gamma^2)^m
 \prod_{\rm off}
   \bigl[(1+t/(c+iB))(1+t/(c-iB))\bigr]^m.
\]

All products count locations and analytic multiplicities exactly once. The
summability just proved permits logarithmic differentiation away from the
zeros. On t>=0 all denominators are nonzero. Twice G'/G is exactly (X3.2),
and F'(sqrt t)/(sqrt t F(sqrt t))=2G'/G. The derivative limits agree with the
actual derivatives, by the same locally uniform bounds. QED.

This step is conditional on complete actual zero correspondence and growth;
matching two incomplete enumerations is not a substitute. The classical
Hadamard theorem is an explicit imported analytic tool, not a Lean build.

<a id="X5"></a>
## X5. The existing one-orbit payment extends to every t>=0

Let d_i=c_i-r0, kappa_i=B_i^2/d_i^2 and

\[
 \epsilon_i=\frac{2m_i\kappa_i}{1-\kappa_i}.
\]

These shares are **independent of t**. Their derivatives introduce no omitted
terms when jets are combined. The source geometry gives

\[
 d_i\ge\frac23b_i^2>0,\qquad B_i^2<b_i^2,
 \qquad0\le\kappa_i\le\frac9{4b_i^2}<\frac12,
 \qquad0\le\epsilon_i\le\frac{9m_i}{b_i^2}.
\tag{X5.1}
\]

Indeed d_i>=b_i^2-1/4-H^2/4>3b_i^2/4-1/4>=2b_i^2/3 since b_i^2>3.
The B and kappa estimates follow immediately; 1/(1-kappa)<=2 proves the
share bound. For U=t+c_i and s=d_i/U, t>=0 implies U>0 and 0<s<1 because
U-d_i=t+r0>0. Thus the original domain calculation does not intrinsically
require t>1/4. This is a new domain-strengthened repair, not a relabeling of
the old formal theorem's hypotheses.

For a positive C2 function write E(f)=ff''-2(f')^2, and put
cross(f,g)=fg''+gf''-4f'g'. Direct differentiation gives

\[
 E(q_i)=-\frac{32m_i^2B_i^2}{(U^2+B_i^2)^3},\qquad E(R)=0,
\]

\[
 \operatorname{cross}(q_i,R)=
 \frac{16m_i s^2 Q_{\kappa_i}(s)}
 {U^4(1+\kappa_i s^2)^3(1-s)^3},
\]

\[
 Q_\kappa(s)=1-\kappa+3\kappa s(2-s)+\kappa^2s^2(3-2s)
 \ge1-\kappa.
\]

Using B_i^2=kappa_i s^2 U^2 and (1-s)^3<=1 shows

\[
 -E(q_i)\le\epsilon_i\operatorname{cross}(q_i,R).
\]

Since E(q_i+epsilon_i R)=E(q_i)+epsilon_i cross(q_i,R)+epsilon_i^2 E(R),

\[
 \boxed{q_i+\epsilon_iR>0,\qquad E(q_i+\epsilon_iR)\ge0\quad(t\ge0).}
\tag{X5.2}
\]

This reconstructs the source-specific local calculation at its actual
normalization and extends its legitimate domain. Multiplicities remain m_i,
not one unit per distinct zero. The finite symbolic checker verifies these
rational identities; the inequalities above are the proof for all parameters.

<a id="X6"></a>
## X6. Positivity of every paid prefix is derivable

For positive functions f_1,...,f_n, let A=sum f_i and u_i=f_i'/f_i.
The exact identity is

\[
 \boxed{E(A)=A\sum_i\frac{E(f_i)}{f_i}
       +2\sum_{i<j}f_if_j(u_i-u_j)^2.}
\tag{X6.1}
\]

It follows by writing f_i''=E(f_i)/f_i+2f_i u_i^2 and expanding. Thus a finite
sum of positive reciprocal-concave functions remains reciprocal-concave.
A zero-weight component can simply be omitted; no division by its zero value
is performed. This is also a direct n-term reconstruction of the two-jet
`cross_square_certificate` in the inspected source.

Choose arbitrary finite exhaustions I_N and J_N of the fixed off-line and
other-critical sets. By (X3.1), (X3.3) and (X5.1),

\[
 \ell_N=1-\sum_{i\in I_N}\epsilon_i\ge\frac{215}{512}>0.
\]

The paid prefix is

\[
 p_N=\ell_NR+(m_0-1)R+
       \sum_{i\in I_N}(q_i+\epsilon_iR)
       +\sum_{j\in J_N}\frac{2m_j}{t+\gamma_j^2}.
\tag{X6.2}
\]

Every nonzero summand is positive and has nonnegative E by X5 or direct
calculation. Therefore E(p_N)>=0 by (X6.1). At the same time the one-use
identity cancels all allocated shares **at every finite N**, yielding

\[
 p_N=m_0R+\sum_{i\in I_N}q_i+
                 \sum_{j\in J_N}\frac{2m_j}{t+\gamma_j^2}.
\tag{X6.3}
\]

It is an exact value/first/second-derivative identity because shares and leftover
are constant in t. X4 proves C2 convergence to the full p; the polynomial map
(v,d,e)->ve-2d^2 is continuous. Hence

\[
 \boxed{p(t)>0,\qquad p(t)p''(t)-2p'(t)^2\ge0\quad(t\ge0).}
\tag{X6.4}
\]

Thus, in a source-complete repaired API, the separate
`prefixEnergyNonnegative` and paid C2 approximation premises can be constructed
from the one-orbit calculation, the strict total budget and the genuine full
source expansion. They are not new RH-strength assumptions. In the deposited
API they remain supplied fields; this report does not change its code or
pretend its impossible input is inhabited.

<a id="X7"></a>
## X7. The other scalar premises also follow from the corrected source

For a critical term r_j(t)=2m_j/(t+gamma_j^2),

\[
 r_j'<0,\quad (tr_j)'>0,\quad (tr_j)''<0.
\]

For an off-line term q=4mU/(U^2+B^2), c=b^2-a^2>|B| at H>=1024, and

\[
 q'=\frac{4m(B^2-U^2)}{(U^2+B^2)^2}<0,
\]

\[
 (tq)'=\frac{4m[cU^2+(2t+c)B^2]}{(U^2+B^2)^2}>0,
\]

\[
 (tq)''=-\frac{8m[cU^3+3tUB^2-B^4]}{(U^2+B^2)^3}<0.
\tag{X7.1}
\]

For the last sign, U>=c and t>=0 give a numerator at least c^4-B^4>0.
Termwise derivatives are valid by X4. The selected positive critical term
makes the inequalities strict even if the off-line set is empty. We obtain

\[
 p'<0,\qquad (tp)'>0,\qquad (tp)''<0,
 \qquad (1/p)''=-E(p)/p^3\le0.
\tag{X7.2}
\]

Concavity on the **whole connected interval (0,infinity)** makes every second
divided difference of 1/p and tp nonpositive. A source expansion only on
(1/4,infinity) would not justify triples crossing 1/4; X4 is the required
source argument for that domain extension.

<a id="X8"></a>
## X8. The finite Pick algebra and all repeated-node cases

For x_i>0 put t_i=x_i^2, p_i=p(t_i), and

\[
 K_{ij}=\frac{x_ip_i+x_jp_j}{x_i+x_j}.
\]

In particular K_ii=p_i>0. For x<y the exact determinant is

\[
 \det K_{\{x,y\}}=
 \frac{(p(x^2)-p(y^2))(y^2p(y^2)-x^2p(x^2))}{(x+y)^2}>0.
\tag{X8.1}
\]

For three distinct nodes, direct algebra gives the deposited factorization

\[
 \det K=
 \frac{p_1p_2p_3\Delta(t)^2}
 {(x_1+x_2)^2(x_1+x_3)^2(x_2+x_3)^2}
 [t_1,t_2,t_3](1/p)\,[t_1,t_2,t_3](tp),
\tag{X8.2}
\]

where Delta(t)=(t2-t1)(t3-t1)(t3-t2). The prefactor is nonnegative and both
divided differences are nonpositive, so det K>=0. A positive first diagonal
and positive two-node leading pivot give a positive definite 2x2 corner;
its scalar Schur complement equals det K divided by that pivot. Completing
the square gives K positive semidefinite. No invalid rule using only arbitrary
nonnegative leading minors is invoked.

When nodes repeat, K is the pullback of its distinct-node matrix under the
linear map that sums coefficients belonging to equal nodes. Positivity
therefore follows from the one- or two-node case. This is exact duplicate-node
reduction, **not** an unproved assertion about confluent derivative kernels.

Combining X1--X8 proves a complete mathematical order-three theorem for the
correctly normalized entire source under X3--X4's explicit spectral inputs.
It derives the diagonal, strict pair, companion-curvature and reciprocal-
curvature fields instead of installing them as unexplained final-shape inputs.
It proves no statement at order four, and does not prove RH.

<a id="X9"></a>
## X9. Nonvacuity controls and an explicit obstruction to overclaiming

Let H=1024, gamma0=1, m0=1. With no off-line or other critical atoms,
F(z)=1+z^2 is an allowed model. With one off-line representative
(a,b,m)=(1/4,1025,1), put c=b^2-a^2, B=2ab and

\[
 F(z)=(1+z^2)\frac{(z^2+c)^2+B^2}{c^2+B^2}.
\]

It has the required real coefficients, evenness, finite growth and exact
critical/off-line zero locations. The budget follows even from the stronger
simple estimate 1/b^2<1/(9H). The repaired source theorem applies, yet F has
the off-line quartet. Thus PSD through three is not RH in a generic source
class, and the corrected enumeration has not smuggled in an empty spectrum.
The exact checker evaluates this model on triples including x<1/2, x=1/2,
x>1/2, and repeated nodes, retaining all principal minors.

For an infinite off-line model take a_j=1/4, b_j=H 2^(j+1), m_j=1, j>=0,
and the same selected critical factor. The paired genus-zero product converges
locally uniformly since sum b_j^(-2)=1/(3H^2). Its zero counting grows only
logarithmically and it has order zero (the logarithm of its maximum modulus
is O((log R)^2)). It too satisfies the small-share condition. This analytic
model validates admissibility of an infinite index class; the finite tests do
not claim to run an infinite product.

None of these models is claimed to be actual xi, and no actual off-line zero is
asserted. They test the logical scope and cardinality contract of the replacement.

<a id="X10"></a>
## X10. What may now be extracted, and what remains

Proposed new identities: `REVIEW.C4.XI.ENTIRE_NORMALIZATION`,
`REVIEW.C4.XI.COUNTABLE_SOURCE`, `REVIEW.C4.XI.ALL_POSITIVE_C2`,
`REVIEW.C4.XI.PAID_PREFIX`, and `REVIEW.C4.XI.PICK3_REPAIR`.
Do not reuse or rewrite the old source identities.

The following mathematical obligations are reconstructed here: function-level
removable normalization; finite/empty/infinite spectrum admissibility; exact
multiplicity and reserve accounting; local payment at every t>=0; finite
positive-sum closure; complete C2 passage; scalar monotonicity and both
curvatures; the strict-pivot PSD argument; and exact repeated-node reduction.

For actual xi the external finite-height proof, existence of the selected low
critical orbit, classical entire growth/Hadamard zero correspondence and the
all-height counting estimate remain **explicit source inputs**. The repair
is conditional on them. No original zero-verification computation was rerun.
A separate integrator must accept the new argument, implement it in shared
ChallengeDeps and consumers together, regenerate source locks and registry
entries, then compile and compare the exact types and axioms. The full input
construction in Lean has not been produced in this pass. Scientific positivity
through three and a kernel-clean theorem are different completion gates.
