# Conductor averages, rational incidence, and joint continuation

**Status:** proposed standalone research, stacked on PR #925 at
506e3808d2f1e86a31a6d1f70cc7da58367c9918.
This pass proves source-dependent bounds for additional positive
portions of every fixed even moment, a larger continuation domain
for the exact reflected function, and an elementary Gaussian
sampling criterion. The full generalized moment and RH remain open.

The arithmetic advance is to average the cubic characters created
by primes that occur twice in a Hermitian tuple. Counting the
rational primes behind singleton ideals then strengthens that
average. The spectral advance exchanges two physical axes only
after an exact split has resolved the one-sided cube mask.

## 1. The target and the four proof notes

In the inherited Eisenstein normalization, the target is
\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\]
\[
\sum_{0<Nu\le D^h}|A_u(D;W)|^{2k}
\ll_{k,h,W,\nu,S,\epsilon}D^{h+k+\epsilon},
\qquad h=1+\vartheta,\quad\vartheta>0,
\tag{1.1}
\]
for each fixed integer order \(k\ge2\), each permitted fixed test and character
datum, every sufficiently large real \(D\), and every
\(\epsilon>0\). Constants need not be uniform in \(k\).
Every physical element row is present.

| Note | Proved advance | Retained limitation |
|---|---|---|
| [Cubic conductor average](CUBIC_CONDUCTOR_AVERAGE.md) | A conductor-uniform mean over the double-prime cubic family; \(\mathcal Q_L^\Phi\ll D^{k+\epsilon}H^{1/2}L^{3/4}\), plus its size-sensitive refinement | Imports de Faveri's Proposition 8.1; the large-singleton complement is not controlled |
| [Rational-prime incidence](RATIONAL_PRIME_INCIDENCE.md) | A native rational-radical count, split/inert conductor branches, and the stronger composed region \(v(g_1)^3w(g_1)^2\le H^2\) | Positive accounting for specified regions; its analytic branches retain their stated imported inputs |
| [Joint continuation](JOINT_CONTINUATION.md) | Holomorphic continuation to \(a,b>1/2,\ 6a+8b>11\), and square-root row means in larger regions | Uses the pinned theta foundation; canonical rows are squarefree; no improvement of the physical moment envelope |
| [Gaussian sampled moments](GAUSSIAN_SAMPLED_MOMENTS.md) | Full moving-height and maximal recovery from \(O(\log X/\log\log X)\) prescribed scales, with exact finite truncation and conditional zero extraction | The arithmetic sampled moment estimate remains unproved |

The first two notes permit arbitrary bounded column coefficients,
not only the native Möbius coefficients, within their stated fixed
compact support. This quantifier is useful because their positive
accounting estimates survive arbitrary additional tuple selectors.
The spectral note instead requires the exact coherent smooth
divisor coefficients; it does not inherit an arbitrary divisor
weight quantifier.

## 2. The averaged conductor estimate

For a tuple
\(\mathbf t=(n_1,\ldots,n_k;m_1,\ldots,m_k)\), let \(g_m\)
be the product of its nonprincipal prime ideals occurring exactly
\(m\) times. Let \(S_{\mathbf t}^{\Phi}(H)\) be its exact complete
smooth row kernel, including all residual-zero principal masks.
For \(Ng_1\asymp L\), define
\[
\mathcal Q_L^\Phi
=\sum_{\mathbf t:\,Ng_1\asymp L,\ f\ne1}
|c(\mathbf t)|\,|S_{\mathbf t}^{\Phi}(H)|.
\tag{2.1}
\]
Every double-prime conductor and every higher multiplicity is summed.

A multiplicity-two nonprincipal prime occurs twice on one
Hermitian side, so its sextic exponent is \(2\) or \(4\). Split
these primes into the two cubic labels \(a,b\). The new uniform
mean, with background conductor norm \(R\), is
\[
\begin{aligned}
\sum_{a\sim A,\ b\sim B}^{*}
|L(1/2+it,\psi\xi_{ab^2})|^2
&\ll (RAB)^\epsilon(2+|t|)^C AB\\
&\quad\times
\left[1+R^{1/2}(M/N)^{1/6}+(R/M)^{1/3}\right],
\end{aligned}
\tag{2.2}
\]
where \(M=\min(A,B)\), \(N=\max(A,B)\), and the literal
coprimality restrictions of the proof are imposed.

The dependence on \(R\) is proved from the arbitrary-coefficient
polynomial inequality in de Faveri's
[arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1),
Proposition 8.1. It is not inferred from the fixed-twist constant
in that paper's Theorem 1.2. The proof treats the two approximate
functional equation halves, primitive local values at the bad
primes, the finite unit/ray correction, and every moving exclusion.

The principal-mask count has weight \((Nab)^{-1}\). Cauchy–Schwarz
in (2.2) produces \(ABR^{1/4}\), cancelling that weight after
dyadic localization. All remaining multiplicity-\(m\) sums,
\(m\ge3\), converge strictly. This proves
\[
\boxed{\mathcal Q_L^\Phi
\ll D^{k+\epsilon}H^{1/2}L^{3/4}.}
\tag{2.3}
\]
Consequently the complete region \(Ng_1\le H^{2/3}\) has the
desired total size \(HD^{k+\epsilon}\).

The sharper dependence on the two cubic sizes gives
\[
\mathcal Q_{L;A,B}^\Phi
\ll D^{k+\epsilon}H^{1/2}
\left[L^{1/2}+L^{3/4}(M/N)^{1/12}
+L^{2/3}M^{-1/6}\right].
\tag{2.4}
\]
The corresponding three explicit inequalities are in Corollary
4.3 of the proof.

## 3. Count conjugate and inert primes once

The elementary count depends on
\[
\rho(\mathbf t)=
\operatorname{rad}_{\mathbb Z}\!\left(\prod_i Nn_i\,Nm_i\right).
\]
There are \(O(D^\epsilon R)\) supported tuples with
\(\rho(\mathbf t)\le R\): each rational prime determines only a
fixed number of incidence choices at the fixed order. Therefore
the entire region \(\rho(\mathbf t)\le(BD)^k\), including every
squarefull total norm product, has size \(HD^{k+\epsilon}\) by
counting alone. This includes tuples whose column ideals are
pairwise coprime but contain paired conjugate primes.

For the stronger combination with (2.3), uniquely write
\[
Ng_1=v(g_1)w(g_1)^2.
\tag{3.1}
\]
The squarefree integer \(v(g_1)\) contains rational primes with
exactly one split prime ideal in \(g_1\). The squarefree integer
\(w(g_1)\) contains paired split primes and inert prime ideals
in \(g_1\). These are data of the singleton ideal, not occurrence
counts in the whole tuple.

On \(v(g_1)\asymp V,\ w(g_1)\asymp W\), the new composition gives
\[
\boxed{\mathcal Q_{V,W}^{\Phi}
\ll D^{k+\epsilon}H^{1/2}V^{3/4}W^{1/2}.}
\tag{3.2}
\]
Hence
\[
\boxed{v(g_1)^3w(g_1)^2\le H^2}
\tag{3.3}
\]
is another complete region at the desired size. It contains
\(Ng_1\le H^{2/3}\) and can be strictly larger.

The note also gives four-parameter rational-incidence branches
from classical completion, Wu's subconvexity bound, and the
divisor-sensitive bound already pinned in PR #925. The native
radical count uses none of those analytic inputs.

### What the strict examples compare

At \(H=D^{21/20}\), an explicit fourth-moment configuration has
\[
Ng_1\asymp D^{4/5},\quad Ng_2\asymp D,\quad
v(g_1)\asymp D^{3/5},\quad w(g_1)\asymp D^{1/10}.
\]
The composed bound is \(HD^{2-1/40+\epsilon}\).
The unrefined cubic estimate has excess \(3/40\), and the
rational pointwise Wu branch has excess \(351/2560\).
The proofs give all column factors and verify their feasible scales.

These are improvements in **tuplewise absolute accounting** over
the explicitly compared branches. They are not claims that every
earlier signed method fails on the complete block. In particular,
PR #926 already has stronger estimates for some corresponding
complete smooth signed blocks. Those estimates do not control
arbitrary subsets or the sum of the individual absolute kernels.
Both proof notes and the independent reviews preserve this distinction.

## 4. A larger continuation domain for the exact reflected series

Write \(u=v-s,\ t=1-s,\ a=\Re u,\ b=\Re t\).
The [spectral proof](JOINT_CONTINUATION.md) retains the exact local
cube correction
\[
\Theta_k(d;u,t)=\prod_{p\mid d}\frac{1-A_p}{1-z_p}.
\]
It then splits the possible intersection of the squarefree
inner index with the physical cube index before exchanging the
raw axes. The common moving auxiliary and global masks are
computed explicitly; no coprimality condition is inserted.

For the exact canonical series and the actual reunion of all
three cusps, the resulting holomorphic tube is
\[
\boxed{a>1/2,\qquad b>1/2,\qquad 6a+8b>11.}
\tag{4.1}
\]
This is normal convergence of coherent smooth dyadic blocks and
continuation of the original function from an absolute chamber.
It is not a claim about arbitrary sharp rearrangements.

For squarefree primary rows \(Nk\asymp Q\), the norm is
\(O(Q^{1+\epsilon})\) on compact real substrips of (4.1).
It improves to \(O(Q^{1/2+\epsilon})\) in the following regions,
with fixed vertical polynomial factors understood:

| Inputs in addition to the pinned theta foundation | Region |
|---|---|
| Classical sextic sieve and scalar counting | \(a>5/8,\ b>1\) |
| De Faveri's Theorem 1.1 and the inherited \(11/12\) angular input | \(a>73/120,\ b>1\) |

The proof also retains the \(4/7<a<1,\ b>(6-a)/5\) region under
the latter inputs. Every monomial comparison is proved analytically.
No numerical linear program substitutes for those inequalities.

The scalar \(73/120\) is **not a zero-free exponent**. Its
candidate physical energy \(QD^{73/60+\epsilon}\) is still
weaker than the existing positive envelope
\(QD^{29/24+\epsilon}\), by \(1/120\) in the column exponent.
The note proves this comparison explicitly.

## 5. A smaller exact arithmetic sampling target

Fix once and for all
\[
G(y)=(2\pi)^{-1/2}e^{-(\log y)^2/2},\qquad
\widehat G(s)=e^{s^2/2}.
\tag{5.1}
\]
The Gaussian sum is entire in logarithmic scale with a
row-uniform growth bound. Write \(M_{2k}(D,H;G)\) for its full
element-row moment up to norm \(H\). For fixed \(e\ge0\), quantitative
interpolation shows that the actual moment bound for this fixed test follows from
\[
\frac1{n_X}\sum_{j=0}^{n_X-1}
M_{2k}(Xe^{t_j},(Xe^{t_j})^h;G)
\ll_\epsilon X^{h+k+e+\epsilon}
\tag{5.2}
\]
on every sufficiently large dyadic \(X\), where
\[
n_X=\left\lceil\frac{8\log(e^eX)}{\log\log(e^eX)}\right\rceil,
\qquad t_j=\frac{j\log2}{n_X-1}.
\]
The recovered result even bounds the row sum of the maximum on
the preceding dyadic interval. That choice keeps every moving
row endpoint covered.

An alternative requires an integrated bound on any measurable
aperture of relative measure \(\gamma_X\) satisfying
\(\log(1/\gamma_X)=o(\log\log X)\). No local distribution
condition is needed. Finite sums with norm window
\[
D\exp\!\left(\pm2\sqrt{(A+1)\log D}\right)
\]
approximate the Gaussian values with uniform error \(O(D^{-A})\).
Interpolation applies to the entire sum, not to moving finite
cutoffs.

The exact sixth-power replicas and causal inversion then give
the conditional zero-free boundary
\[
\Re s>\frac12+\frac{5h}{12k}+\frac e{2k}.
\tag{5.3}
\]
For \(k=2,\ h\downarrow1,\ e=0\), this approaches \(17/24\);
an appropriate unbounded hierarchy would approach \(1/2\).
Neither hierarchy nor even the required fourth-moment premise
is proved. Estimates for a different compact test are not silently
transferred to this Gaussian test.

## 6. What remains open

The arithmetic notes remove their controlled regions from the
exact signed remainder at a justified positive cost. The
complement still contains tuples with many unrelated singleton
primes. For \(2k\) mutually coprime column ideals at scale \(D\),
\(Ng_1\asymp D^{2k}\); in the absence of rational pairings,
neither (2.3) nor (3.2) approaches the full target at \(H\) near
\(D\).

The missing assertion is cancellation in that actual signed
large-singleton average, at all required scales and orders.
The Gaussian criterion identifies fewer scale observations
that would suffice, but supplies no arithmetic upper bound for
them. The joint continuation theorem is not a substitute for
that signed estimate.

The pass also investigates
[direct singleton-sieve averaging](EXPLORATION_SINGLETON_SIEVE.md).
Its coarse size reduction returns to the classical condition
\(L\sqrt G\le H\), so it is not promoted as a new diagonal
region. The separately labeled exploration records the retained
sign-size question for a later proof attempt.

## 7. Sources, independent review, and finite diagnostics

[SOURCE_LOCK.json](SOURCE_LOCK.json) records the exact repository
input commits and hashes and the versioned external theorem.
The packet was compared against PR #924's stronger physical
A2 estimates and PR #926's sampled and signed-block results;
those earlier gains are not claimed again here.

The content reviews are:

- [Cubic conductor average](REVIEW_CUBIC_CONDUCTOR_AVERAGE.md).
- [Rational incidence and a second cubic audit](REVIEW_RATIONAL_PRIME_INCIDENCE.md).
- [Joint continuation](REVIEW_JOINT_CONTINUATION.md).
- [Gaussian criterion](REVIEW_GAUSSIAN_SAMPLED_MOMENTS.md) and
  [a second independent Gaussian audit](REVIEW_GAUSSIAN_SECOND.md).

The exact committed-source bindings and final verification are
recorded in [VALIDATION.md](VALIDATION.md). AI-agent review is not
human external acceptance or Lean verification. The imported
analytic theorems have not been independently reproved here.

Run the exact finite diagnostic with:

~~~bash
python standalone/2026-10-10-conductor-averages/check_conductor_exponents.py
~~~

Its [saved output](conductor_exponent_report.json) records rational
exponent identities, the comparison fixtures, and 15,600 aggregated
local multiplicity assignments for \(k=1,\ldots,8\). It verifies
that finite algebra, not the analytic proofs, all orders by
enumeration, any full moment, or any zero-free region.
