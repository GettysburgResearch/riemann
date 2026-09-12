# Correlated Ising realization: a serious route assessment and a new degree-eight construction

Assessment completed 12 September 2026 against the cited pinned PRs;
packaged as a proposed research contribution on 13 September. **RH remains open.**

The strongest feature of this route is that its final analytic implication is
already complete: an admissible family converging to the actual theta law
would prove RH. Its weakness is the unproved existence of that family. The
latest papers solve increasingly substantial finite inverse problems and
construct complete infinite laws, but none proves an extension mechanism at
unbounded moment order.

This pass did produce a concrete improvement. By using a compensated
ferromagnetic edge instead of changing every edge uniformly, I obtained a
directed full-source certificate for an infinite model matching theta through
degree eight and retaining all three real-field growth coefficients. An
analytic continuation then makes the entire infinite chain connected. Its
tenth moment has a certified error, so it is explicitly not theta. The full
proof and reproducible arithmetic are in [ising-computation/PROOF.md](ising-computation/PROOF.md).

## 1. What must actually be completed

Fix the unchanged normalized theta probability density

\[
w(t)=\frac{\phi(t)}{\int_{\mathbb R}\phi},\qquad
\phi(t)=\sum_{n\ge1}(4\pi^2n^4e^{9t/2}-6\pi n^2e^{5t/2})e^{-\pi n^2e^{2t}}
\quad(t\ge0),
\]

extended evenly by the Jacobi identity. Its characteristic function is
\(\Phi(z)=\Xi(z)/\Xi(0)\). A finite admissible model has zero-field probability
proportional to \(\exp(\sum_{i<j}J_{ij}\sigma_i\sigma_j)\), where
\(J_{ij}\ge0\), and observable \(X=\sum_i a_i\sigma_i\) with \(a_i\ge0\).

The sufficient target is to construct models \(X_m\) such that

\[
\left|E X_m^{2r}-\mu_{2r}\right|\le2^{-m},\qquad 1\le r\le m,
\quad \mu_{2r}=\int t^{2r}w(t)dt.
\tag{I}
\]

An unbounded subsequence of orders is sufficient. Exact matching is convenient
for certificates but unnecessary for the final implication. A single fixed
graph, one prescribed graph class, explicit convergence rates in graph size,
and simple zeros of Xi are all unnecessary extra requirements.

For a finite model the paired Lee--Yang product gives

\[
\frac{E X^{2r}}{(2r)!}\le\frac{(\operatorname{Var}X/2)^r}{r!},
\qquad |E e^{izX}|\le e^{\operatorname{Var}X|z|^2/2}.
\tag{2}
\]

The variance match in (I) bounds the entire Taylor tails uniformly. Moment
convergence therefore gives locally uniform convergence to \(\Phi\), and
Hurwitz transfers the real-zero property. There is no remaining complex-tail
or normalization problem once (I) is established. Weak convergence of the
actual laws is another sufficient formulation, by the classical closure
theorem; one need not force an unnecessarily rigid topology.

The precise literature scope is important. The finite weighted statement
appears after equation (21) of [Newman--Wu](https://arxiv.org/abs/1901.06596);
its Theorem 16 establishes weak closure of the relevant symmetric Lee--Yang
probability class. Neither statement constructs Ising approximants to an
arbitrary real-zero probability law. The abstract construction target is a
Griffiths--Simon type membership problem, not a converse supplied by Lee--Yang.

## 2. Does this merely restate RH, or demand more?

For the actual theta law, having only real Fourier zeros is exactly RH.
Membership in the weak closure of finite pair-ferromagnetic magnetizations
implies that property. No theorem identifying the two classes was found in
the papers inspected here. Consequently the unrestricted Ising construction
is a sufficient route; it should not be advertised as an established
equivalent reformulation.

Several narrower proposals impose additional restrictions:

- **Fixed-k weight-adapted stars:** #867 proves a strictly increasing real
  phase for its nondegenerate limiting companion, so a successful exact
  realization in that fixed class would also prove simplicity of all Xi zeros.
  Simplicity is not part of RH and is not supplied by the general closure
  argument. This is a reason to retain general graphs as the ultimate target.
- **Uniform hidden-spin attachments and quartic visible scaling:** #842
  proves that even their weak closure misses theta. This is an actual excluded
  architecture, not a missing technical estimate.
- **Independent signs, Gaussian dust and bounded persistent components:**
  their structural restrictions can survive limits. Adding more parameters
  without escaping the forbidden architecture cannot solve the problem.
- **Fixed homogeneous chains with a prescribed harmonic tail:** they are
  valid productive model classes, but no universality theorem places theta
  inside them, even assuming RH.

The historical correlation-inequality connection is substantial. Newman's
[1991 paper](https://doi.org/10.1007/BF01888165) proves convexity of the derivative
of the theta density's negative logarithm and discusses its GHS relevance.
Thus positive-source geometry and Ising inequalities have been connected to
RH for decades. Such inequalities are useful tests; they do not by themselves
establish the inverse representation needed here.

## 3. What the actual PRs contribute

The table distinguishes matched order from the global properties of the law.
All finite existence claims retain their written analytic and interval-proof
dependencies; running a checker is not formal verification.

| Work | Actual mathematical advance | Still missing |
|---|---|---|
| #863, `0640c9c59be0bf20c18258460a7517fb09728e82` | A finite 272-spin model matches through degree 14; its degree-16 defect is positive, approximately between .20 and .21 in the standardized convention. It also restricts persistent bounded lattice components in a putative theta limit. | Reachability of the next native target, then an unbounded-order family. |
| [#867](https://github.com/GettysburgResearch/riemann/pull/867), `4c7898432546814812b2be8c72fc199e294354d1` | A connected 96-spin heterogeneous star matches through 14 with negative degree-16 defect; an actual infinite star preserves those moments and the leading theta real-MGF growth. Homogeneous stars are excluded. | The positive and negative degree-16 seeds are not connected by a demonstrated admissible lower-moment fiber; mixtures are not automatically admissible. |
| [#869](https://github.com/GettysburgResearch/riemann/pull/869), `6603f8b04f9a2d073123a328ac0298a498c93a96` | Exact edge-merger and annihilator formulas, and directed favorable local graft derivatives at the #863 seed; a separate quantitative finite spectral-occupancy obstruction. | The favorable grafts do not reach degree 16; the occupancy obstruction is synthetic, not a theta obstruction. |
| [#871](https://github.com/GettysburgResearch/riemann/pull/871), `43a9eea85e20202370cae4b6ffa1a2c30fc3cfc3` | A locally finite connected chain with fixed positive correlation, analytic density, explicit complex cutoff and all three real-field growth coefficients; exact moments 2 and 4. | Its sixth moment is provably wrong. |
| [#875](https://github.com/GettysburgResearch/riemann/pull/875), `be149104721ae7b65b624c100118edfd7b76b69b` | A calibrated independent seed and analytic continuation to connected infinite chains matching moments 2, 4 and 6. | No explicit positive-correlation radius; eighth moment remains wrong throughout a small neighborhood. |
| **This pass** | A five-parameter certified dimer/head seed and analytic continuation to connected infinite chains matching 2, 4, 6 and 8, preserving all three growth coefficients. | No explicit positive-correlation radius; tenth moment is wrong; no order-uniform extension theorem. |

The new #842 material must be read at its actual head,
`aa281cc871637f287ff91457e5608b5b5f694c25`, rather than its stale PR body.
Its cumulant spectral-index theorem and arbitrary finite-theta-jet
countermodels are consequential, but neither is a higher-order Ising fit.

## 4. Restrictions that genuinely change the research plan

**Independent-factor obstruction.** For uniformly bounded-variance independent
sign sums, the inequality
\(|\chi(3t)|\le e^{2Vt^2}|\chi(t)|\) passes to limits. Hence every real zero
brings its triple. The source-specific zero/nonzero-triple certificate excludes
theta. A fair-sign product is therefore not a viable exact all-order target.
The #867 homogeneous-star argument forces its common bias to zero under a
theta-limit assumption, reducing to this obstruction.

**Persistent bounded components.** The bounded-component restrictions in #863
prevent treating a successful finite dimer module as an all-order recipe. A
whole infinite chain evades that restriction because its component is genuinely
unbounded. The fact that the couplings in one local existence theorem can be
small does not imply that sending them to zero along increasing orders will
produce theta.

**Hidden quartic closure.** In #842's hidden-spin class,
\(\rho(x)\propto e^{-ax^4-bx^2}M_B(x)\), let
\(g(u)=-\log\rho(\sqrt u)\). The Lee--Yang product gives
\(g'''(u)=-2\sum_j(u+y_j^2)^{-3}\le0\). A log-concave compactness argument
passes the corresponding third finite-difference sign through weak limits.
The actual theta source has the opposite eventual sign. This excludes that
whole class, even with unboundedly many hidden spins; it does not exclude
general pair graphs. The same paper gives a connected four-spin counterexample
to extending its uniform-attachment inequality to general graphs.

**Finite jets do not determine the spectrum.** The latest #842 construction
keeps arbitrarily many exact theta moments, positivity, the full real divisor,
reflection and endpoints, while adding prescribed nonreal zeros at large
height. It changes the source and lacks the native arithmetic identity.
Its polynomial multiplier also changes the logarithmic real-MGF growth term,
so it does not preserve every condition imposed by the calibrated chains.
The calibrated chains' own next-moment mismatches already show that their
correct growth and finite matches do not identify theta.

These are reasons to use source-specific constraints and test precise
architectures. They are not evidence that the full Ising route is impossible.

## 5. Why cumulant positivity is not the inverse-Ising theorem

For an even LP characteristic function one has

\[
\Phi(z)=e^{-\gamma z^2}\prod_j(1-\lambda_jz^2),
\quad \gamma\ge0,\quad\lambda_j>0,
\]

with zeros repeated according to **integer** analytic multiplicity. Its local
logarithmic coefficients satisfy
\(q_1=\gamma+\sum\lambda_j\) and \(q_n=\sum\lambda_j^n\) for \(n\ge2\).
For the unchanged theta source, #842's complete spectral-index proof makes
positivity of all the specified shifted Hankel forms equivalent to RH. A
proof of that entire source-specific sign family would finish the analytic
problem without constructing any Ising graph.

At finite order, positive Hankel forms give a positive quadrature for the
logarithmic derivative. Integrating it need not give an entire characteristic
function: the pole residues need not be integers. Nor is every entire LP
function a probability characteristic function. Finite cumulant positivity
does not suffice for an entire LP probability lift. Even after obtaining such
a lift, the sources inspected here do not provide a theorem that constructs
pair-Ising approximants from it.

#869 makes the first failure quantitative. Put
\(b=q_1^2/q_2\), \(\delta=q_1q_3/q_2^2-1\). Every even LP lift with
\(q_2>0\) necessarily satisfies

\[
\operatorname{dist}(b,\mathbb Z_{\ge0})
\le b(4\delta+2\sqrt\delta).
\]

Its explicit positive symmetric six-atomic probability source has strictly
positive finite cumulant matrices but \(b=10.5\), \(\delta=10^{-6}\), violating
this condition robustly. This is a useful preliminary veto for an inverse
problem, not a result about theta's own feasibility.

## 6. The new work performed in this pass

The starting point was #875's four head groups of multiplicities
\((25,4,1,1)\), with their total mass fixed by the full three-term growth
calibration. At its independent seed, adding an edge between weights \(u,v\)
has the exact log-MGF derivative

\[
\partial_J\log M(h)|_{J=0}=\tanh(uh)\tanh(vh).
\]

I differentiated its four even Taylor coefficients, compensated the lower
moments and the head mass by the head Jacobian, and found a favorable edge
between two of the four \(b\)-spins. Several other edges have the opposite
sign: ferromagnetic coupling is not automatically favorable after constraints
are imposed. This is the relevant sensitivity, rather than the unconstrained
increase of the variance.

A high-precision exploratory solve then found a positive one-dimer root of
all five equations. It was followed by an accepting calculation using freshly
reconstructed complete theta moments and full harmonic-tail bounds. In a
radius-\(10^{-12}\) box the residual after exact rational preconditioning is
below \(7.63\cdot10^{-22}\), while the whole-box contraction constant is below
\(1.252\cdot10^{-7}\). All 50 inverse identities and positivity constraints
pass. Two native integration meshes certify the same root box.

The analytic extension is not left to numerical intuition. A new useful lemma
shows that any fixed joint Markov cumulant is a polynomial divisible by every
distinct-site gap correlation. Consequently it is bounded by a constant times
\(r_*^{\text{span}}\) when all edge correlations have modulus at most
\(r_*<1\). Holder and geometric gap summation give normal holomorphic
convergence of every fixed observable cumulant. This pays the infinite-chain
implicit-function theorem at order eight and higher without presupposing
order-specific formulas.

The special edge's exact probability-density ratio to the homogeneous chain
is bounded above and below independently of the real field. Thus it preserves
all three growth coefficients. This is why the new adjustment is compatible
with the calibration. The resulting connected models have a complete
standardized degree-ten mismatch between .03321148056 and .03321163717 at
the seed, persisting with a slightly wider bound at small positive background
correlation. The construction has made one additional native target exactly
reachable; it has not established an induction.

## 7. What I would pursue next, and the actual completion criterion

The productive object is the constrained response map. For constraints
\(C(\theta,\eta)=c\), an adjustable head \(\theta\), and a new positive edge
parameter \(\eta\), the next observable has derivative

\[
\partial_\eta K_{\rm next}
-D_\theta K_{\rm next}(D_\theta C)^{-1}\partial_\eta C.
\tag{3}
\]

For a family of possible edges, the signs and cone generated by these
compensated derivatives say which next-moment motions are locally admissible.
The new eighth-moment construction demonstrates that this calculation can
choose a successful target correction while preserving the growth constraint.
It is more informative than another unstructured parameter fit.

A completion needs a theorem ensuring an unbounded sequence of admissible
corrections: enough right-inverse control, adequate target displacement before
the boundary or singular Jacobian, and positive weights/couplings. There is
currently no order-uniform estimate of this kind. Local full rank cannot
replace it. Conversely, a useful negative result would identify a persistent
invariant of a proposed architecture that the native theta source violates;
the hidden-quartic and homogeneous-star results show how decisive such an
invariant can be.

My assessment is that correlated Ising remains a serious constructive option,
and the present pass gives it an actual additional finite step. I still place
the exact native gamma-defect route slightly ahead for completion prospects:
that route already identifies its approximating sources with theta and needs
a sign/budget theorem, whereas the Ising approach may be asking for additional
representation structure. This ordering is a research judgment, not a
probability estimate. Repeated finite successes can improve confidence in an
architecture, but they do not shrink the all-order quantifier automatically.

## 8. Review and validation boundaries

Sources read directly include #875 ISING.md, NUMERICS.md, END_TO_END.md and
primitive code; #871's full proof and inverse programme; #867's full star
proof; #842's hidden-spin, cumulant spectral-index and finite-jet proofs; and
#869's finite occupancy proof and the earlier edge-graft work. The written
new proof uses the pinned source/calibration dependencies explicitly.

The root agent independently read the new proof, certificate code, pinned
source routines and #875's numerical remainder argument. It found no defect
in gap divisibility with repeated sites, the normal-convergence/IFT argument,
the finite-edge growth comparison, or the normalization of the degree-ten
mismatch. This is a second analytic review within the same agent session;
it is not formal verification or a second numerical backend.

New accepting computations: two complete-source integration meshes and four
independent finite algebra tests. The scout is explicitly labeled nondirected;
only the subsequent outward interval result supports existence. The initial
exact-inverse check caught an integer-row coercion before any accepting result;
the row was changed to exact rationals and the full calculation rerun.
The initial assessment changed no repository files or PRs. This publication
adds its separately labeled proposed packet to PR #869.
