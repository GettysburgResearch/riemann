# Hardy translation and physical-inner band bounds

Status: NEW NATIVE PROOF AND BOUNDED EXACT CONTROLS; EXACT-SHA REVIEW REQUIRED.

Scope: finite exponential-polynomial denominator spaces on L^2(0,infinity),
arbitrary phases and confluence, and multiplication by a FINITE Blaschke
numerator. No infinite-inner approximation theorem or actual Xi degree bound.

Exact sources: thirteen immutable repository bindings in the source manifest,
including the earlier coarse packet at 8ef225b8753e2cd1f9c031fbb8038d1321c7f308.
That packet is preserved, not rewritten. This is a separate strengthening.

What was actually run: exact Gaussian-rational Gram/generator and rational
inner-isometry controls, polynomial identities, source authentication, and
resource/type/coverage tests. No numerical Xi, transcendental quadrature,
eigenvalue approximation, or formal analytic proof verification.

Smallest remaining gap: finite-inner degree/approximation control in the
actual mesoscopic cofinal exhaustion, followed by the source/free-energy
comparison. A small accepted-band mass is not a small total Pick charge.

## 1. Native half-line theorem

Let M be an N-dimensional space of continuous functions on [0,infinity),
contained in L^2(0,infinity), with S_h M subset M for every h>=0, where
(S_h f)(t)=f(t+h). Let k_M(t)=K_M(t,t) be its evaluation-kernel diagonal:
\[
 k_M(t)=\sup_{\|f\|_2=1,\ f\in M}|f(t)|^2
       =\sum_{\ell=1}^N|\psi_\ell(t)|^2
\]
for any orthonormal basis. Finite dimension makes evaluation bounded.
Because
\[
 \|S_hf\|_2^2=\int_h^\infty|f(u)|^2du\le\|f\|_2^2,\qquad
 {\rm ev}_{t+h}={\rm ev}_t S_h,
\]
we have k_M(t+h)<=k_M(t). Thus k_M is nonnegative and nonincreasing.
Its integral is N by orthonormality. Consequently
\[
 \boxed{t\,k_M(t)\le\int_0^t k_M(u)du\le N,\qquad t>0.}
\tag{HT1}
\]
There is no commutation with frequency projection and no removal of phases.

For distinct z_j=y_j+ia_j, with y_j>0 and positive integers q_j, take
\[
 M=\operatorname{span}\{t^k e^{-z_jt}:0\le k<q_j\},\qquad N=\sum_jq_j.
\tag{HT2}
\]
These functions are linearly independent (apply the usual constant-coefficient
differential annihilators, isolating one exponential-polynomial block).
Translation preserves each block and all functions are square integrable.
Hence (HT1) holds for arbitrary horizontal phases, heights, spacings, and
multiplicities. In particular the earlier confluent q^2 bound improves to q.
The numerical constant 1 in (HT1) is not claimed optimal.

For 0<A<B, monotonicity also gives the sharper interval estimate
\[
 \boxed{\int_A^B k_M(t)dt\le N\frac{B-A}{B}
                         \le N\log(B/A).}
\tag{HT3}
\]
Indeed the average over [A,B] is no greater than the average over [0,B].
Equivalently, if J=integral_A^B k_M, then
integral_0^A k_M >= A J/(B-A), so N>=B J/(B-A).
The logarithmic comparison follows by integrating 1/t>=1/B.
For a measurable set I, the alternative bound
integral_I k_M<=N integral_I dt/t is available when the latter is finite.

## 2. A second native proof and an exact matrix identity

Use the row basis
\[
 w(t)=(t^{r-1}e^{-zt}/(r-1)!)_{(z,r)},\quad 1\le r\le q_z,\qquad
 G=\int_0^\infty w(t)^*w(t)dt.
\]
For basis indices (z,r),(v,s),
\[
 G_{(z,r),(v,s)}
 =\frac{(r+s-2)!}{(r-1)!(s-1)!(\bar z+v)^{r+s-1}}.
\tag{HT4}
\]
This is positive definite. Write w'=wA: A has -z on each block diagonal
and 1 on its superdiagonal. With c=w(0), integration of (w^*w)' gives
\[
 A^*G+GA=-c^*c,\qquad
 AG^{-1}+G^{-1}A^*=-G^{-1}c^*cG^{-1}.
\tag{HT5}
\]
All terms at infinity vanish; the value at zero is c^*c. Therefore
\[
 \boxed{k_M'(t)
 =w(t)(AG^{-1}+G^{-1}A^*)w(t)^*
 =-|w(t)G^{-1}c^*|^2\le0.}
\tag{HT6}
\]
No modulus is moved through an oscillatory sum. As a normalization control,
taking the trace of (HT5) after multiplication by G^{-1} gives
k_M(0)=2 sum_j q_j Re(z_j). Also integral k_M=tr(G^{-1}G)=N.
These identities include near-collisions without a condition-number assumption.

## 3. Physical inner multiplication by inclusion, not commutation

Use the unitary Hardy Fourier convention
F(x)=(2pi)^(-1/2)integral_0^infinity f(t)e^{ixt}dt. Let
K_B=H^2(C_+) minus B H^2(C_+) orthogonally.

Let B_-^s be a FINITE denominator subfactor of degree n>=1, and let B_+ be a
FINITE Blaschke product of degree m>=0 (a unimodular constant is allowed).
Set d=m+n. The numerator is the actual full numerator factor for this finite
statement, not merely a selected numerator subfactor.

The elementary orthogonal decomposition is
\[
 \boxed{K_{B_+B_-^s}=K_{B_+}\oplus B_+K_{B_-^s}.}
\tag{HT7}
\]
To prove it, split H^2=K_{B_+} plus B_+H^2, then split the second summand
as B_+K_{B_-^s} plus B_+B_-^s H^2. Multiplication by B_+ is an isometry
because its boundary modulus is one.

A finite Blaschke model space has dimension equal to its degree and is the
span of the derivative kernels at its zeros with their multiplicities.
Under the Fourier map these are precisely the exponential-polynomial spaces
(HT2). One can see the finite-dimensional description by iterating (HT7):
a single-factor model space is its one-dimensional Cauchy-kernel span;
the resulting rational functions have exactly the permitted lower-half-plane
poles and partial fractions give the derivative kernels. No simplicity is used.

Let E synthesize any basis of the denominator space, G=E^*E, and define the
PHYSICAL band Gram
\[
 G_{I,B_+}=E^*M_{B_+}^*\Pi_I M_{B_+}E.
\]
The Fourier image W of B_+K_{B_-^s} lies in the d-dimensional product model
space. Projection-kernel domination gives k_W<=k_{product}. Equations
(HT1)--(HT3) imply, for I=[A,B],
\[
 \boxed{\operatorname{tr}(G^{-1}G_{I,B_+})
 \le\min\{n,\ d(B-A)/B\},}
\tag{HT8}
\]
\[
 \boxed{G_{I,B_+}\le\epsilon_d G,\qquad
 \epsilon_d=\min\{1,\ d(B-A)/B\}.}
\tag{HT9}
\]
Here the trace is the band trace of the n-dimensional physical image W,
and the Loewner estimate follows from positivity and its trace bound.
It is NOT necessary for W itself to be shift invariant.

For comparison, without physical multiplication, a denominator space of
degree n obeys the same formulas with d=n. All bounds are uniform in
locations, separations and confluence at fixed declared degrees.

## 4. Literal source and actual-Xi application

Retain L-106671 and CB1--CB6 of the frozen coarse packet:
N=OB_+, D=OB_-, R=N-D, and on the selected denominator jets
\[
 C=J_O,\quad V=J_{B_+},\quad J_R=CV=VC,\quad G_O=C^*GC.
\]
O is holomorphic and nonzero at retained nodes, so C is invertible.
For any Hermitian band weight H, the exact source convention gives
\[
 \operatorname{tr}(G_O^{-1}J_R^*H J_R)
 =\operatorname{tr}(G^{-1}V^*H V).
\tag{HT10}
\]
In particular (HT9) yields
\[
 \boxed{\operatorname{tr}(G_O^{-1}J_R^*G_{I,B_+}J_R)
 \le\epsilon_d\operatorname{tr}(G_O^{-1}J_R^*GJ_R).}
\tag{HT11}
\]
No freedom to choose the literal Xi source jets is assumed. If the total
on the right is zero, the left is zero; no ratio with zero is formed.
This controls the physical-inner band Gram that CB26 left open, but only
under the finite-Blaschke hypotheses and with total degree paid.
Physical multiplication by the OUTER factor or the analytic gauge has not
been commuted with Pi_I; they remain encoded by the actual source metric.

For every fixed positive odd K and fixed M>0, the actual-Xi uniform
accepted-set envelope proved in CB18--CB20 satisfies, for lambda=2/X,
\[
 S_X=\{\xi\in[X/2,2X]:|\rho_{K,2/X}(\xi)|\le M\}\subset[A_X,B_X],
\]
\[
 A_X=X+(1/(4\pi)-KM/(2\pi)-r_X)e^{-X}/X,\quad
 B_X=X+(1/(4\pi)+KM/(2\pi)+r_X)e^{-X}/X,\qquad r_X\to0.
\]
Thus
\[
 \frac{B_X-A_X}{B_X}
 =\left(\frac{KM}{\pi}+o(1)\right)e^{-X}/X^2.
\tag{HT12}
\]
The envelope is uniform by the frozen tail bootstrap, not inversion of a
pointwise limit. It does not claim S_X is an interval or that rho is monotone
in xi. K,M are fixed; the error does not depend on model-space degree or nodes.

Consequently physical band traces, unit-vector masses, and the relative
literal source-band energy in (HT11) tend to zero whenever
\[
 \boxed{d(X)=m(X)+n(X)=o(X^2e^X).}
\tag{HT13}
\]
The unweighted conclusion needs only n(X)=o(X^2e^X), including a single
confluent multiplicity q(X). This is stronger than the earlier sufficient
q=o(Xe^{X/2}) cutoff, without contradicting the dense-union countercontrol.

This is a localization obstruction to a strategy requiring concentration in
the accepted scalar band, not a proof of small total physical charge.
The forced topological factor of L-106674 remains. The actual frontier
T-106620 explicitly retains cofinal-exhaustion and boundary ledgers. It gives
a height SUM, which does not bound the number of arbitrarily shallow zeros.
No bound d=O(T log T) for native companion factors is inferred from the
Riemann zero count. No substitution X~log T into (HT13) is made.

If the actual numerator is an infinite inner function, (HT7) still exists
abstractly but the product model space has infinite dimension and the finite
d-bound does not apply. A finite-inner approximation plus quantitative error
and compatible degree control would be needed. Those hypotheses are not
supplied by the pinned sources. Neither the full physical-scale transfer nor
the free-energy target is proved here.

## 5. Countercontrols and why the degree hypotheses matter

The physical image need not have a monotone kernel. For one denominator
kernel f(t)=sqrt(2)e^{-t} and B(x)=(x-i)/(x+i), its Fourier-side image is
sqrt(2)(1-2t)e^{-t}. The rank-one image kernel vanishes at t=1/2 and is
positive at t=1. Applying the shift-invariant theorem directly to that image
would be invalid; (HT7) is the reason the bound works.

The numerator degree cannot be omitted uniformly, even with denominator
degree n=1 at FIXED height. Fix L>0. For each T>0 let a_m=2m/T and
\[
 B_{m,T}(x)=\left[-\frac{x-ia_m}{x+ia_m}\right]^m.
\tag{HT14}
\]
These are finite Blaschke products of degree m. For each real x,
B_{m,T}(x)->exp(iTx) as m->infinity, since
log((1+ix/a_m)/(1-ix/a_m))=2ix/a_m+O_x(a_m^{-3}).
For the fixed Hardy transform F of sqrt(2)e^{-t}, dominated convergence,
using |B_{m,T}-exp(iTx)|<=2, and Plancherel give strong L^2 convergence to
sqrt(2)e^{-(t-T)}1_{t>=T}. Its mass on [T,T+L] is 1-exp(-2L)>0.
Hence for every T one can choose a finite m sufficiently large to retain,
say, half that mass. Letting T->infinity makes (B-A)/B=L/(T+L)->0.

Therefore no bound depending only on the rank n=1 and vanishing with relative
band width can hold uniformly over finite numerator degree. The order of
choices is fixed L, then T, then sufficiently large m. This uses actual
finite inner functions and a fixed-height denominator, but is not Xi data
and provides no quantitative necessity converse to (HT13).
For an unrestricted singular inner exp(iTx), the same shift is exact;
finite Blaschke approximation explains why finite DEGREE must still be paid.

## 6. Prior art and exact replay contract

The dimension/evaluation/translation mechanism is classical. A close primary
reference is Borwein and Erdelyi, *Nikolskii-type inequalities for shift
invariant function spaces*, Proc. Amer. Math. Soc. 134 (2006), 3243--3246:
[author's four-page paper](https://people.tamu.edu/~terdelyi/papers-online/shift_sub.pdf).
Its finite-interval theorem and proof use evaluation-kernel dimension averaging
and translation. Here one-sided L^2 contractivity makes the diagonal monotone
and yields the direct half-line coefficient N. No novelty claim is made.

The product decomposition is explicitly recorded in Fricain, Hartmann and
Ross, *Multipliers between model spaces*, [arXiv v2](https://arxiv.org/pdf/1605.07418v2),
equation (2.12), p.8; finite Blaschke model spaces are described in (2.18)--(2.19),
p.9. Section 2 also identifies the upper-half-plane version. We gave the
elementary Hilbert-space proof rather than importing a multiplier theorem.

The exact producer uses Gaussian rationals (pairs of Fractions), not binary
complex floating point. In the basis of (HT4), it rebuilds G,A,c and checks
both identities (HT5), all Hermitian LDL pivots, the origin constant
2 sum Re z, and total dimension. Predeclared examples include separated
complex phases, repeated nodes, mixed confluence, and a zero-degree numerator.

For physical controls it multiplies each Laplace basis element
1/(s+z)^r by the finite numerator product
prod_c (s-bar c)/(s+c). Exact partial fractions give an inclusion matrix J
into the product model basis. It checks the FULL rational-function identity
by cross-multiplied polynomial coefficients and independently checks
J^*G_product J=G_denominator. Finite point sampling does not substitute for
the rational identity. This exercises collisions between numerator and
denominator nodes as well as separate complex poles.

A held-out complex confluent pair C,V commutes in the jet algebra but neither
commutes with G or an exact positive weight H. The control proves
0<H<G/2 by exact Hermitian LDL pivots, verifies (HT10)--(HT11), and shows
that dropping the outer from the denominator metric changes the trace.
This H is an abstract positive weight, not a claim to have constructed an
actual Xi band Gram. The physical-band conclusion is the native proof above.

Interval factors d(B-A)/B and all caps are rational. The nonmonotone image
control uses its exact polynomial and exact zero at t=1/2; positivity at 1
and the delay limit are analytic statements proved above, with exponentials
left symbolic. The checker does not machine-certify limits or arbitrary
continuous-frequency inequalities.

The fixed panel and public hard caps are recorded in the fixture. A total
degree cap is enforced BEFORE matrix or polynomial allocation; raw values
reject bool, float and nonrational inputs. Gaussian-rational arithmetic also
has an intermediate bit cap. Every result-bearing predicate survives -O.
Every frozen repository input is authenticated by exact commit, Git blob,
and LF-normalized SHA-256 before the report is built. The fixture binds the
note, producer, tests and manifest, and is accepted only by complete typed
canonical-JSON equality to a fresh rebuild. External formula contracts are
metadata-authenticated, not remote-byte authenticated.

Replay commands:
```text
python research/exploratory/hardy_translation_physical_band_bound.py --check
python -O research/exploratory/hardy_translation_physical_band_bound.py --check
python -m unittest discover -s tests -p test_hardy_translation_physical_band_bound.py
python -O -m unittest discover -s tests -p test_hardy_translation_physical_band_bound.py
```

Author replay: both producer modes and all 33 new tests passed. The adjacent
confluent-source (23), actual-kernel (15), and near-adapted-scale (23) tests
also passed in both modes: 61 adjacent tests per mode. Ruff and diff checks
passed. These are bounded algebra/source replay results, not machine proofs
of the analytic statements.

An independent frozen-code and proof audit is required. The load-bearing new
steps are evaluation contractivity, the finite product-model inclusion, and
faithful finite-degree scope. No height/count, cofinal, free-energy, critical-line
percentage, RH, GRH, or novelty conclusion is asserted.
