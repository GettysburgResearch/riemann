# Signed graph sectors, joint Gauss continuation, and centered cube inversion

**Status: proposed standalone research, with explicit source qualifications.**
This packet is stacked on PR #924 at
`725b2d25ab47e57500049d93985560098c7ef3fa`. It combines that packet with
the exact #922 reunion and the newer #925/#926 branches. It proves new
conditional whole-sector bounds, a larger holomorphic domain for the
actual reunited theta object, and elementary principal-kernel and
joint-correction estimates. It does not prove a full fourth moment,
`17/24`, the cofinal moment hierarchy, or RH.

The proposed source-conditional zeta boundary remains
`139999/160000`. The original imported theta foundation has not been
independently reconstructed or certified by this continuation.

## 1. The new results

| Result | Exact output | Proof and scope |
| --- | --- | --- |
| Entire cross-gcd graph sectors | A bounded selector on all shared incidence ideals can stay inside a signed native core. Forest rank controls whole overlapping graph unions at every fixed moment order. | [ARBITRARY_GRAPH_SECTORS.md](ARBITRARY_GRAPH_SECTORS.md), under the stated `NM2` and `PW_b` premises |
| Full fourth-moment cross-gcd union | `|U_C(D/R)| <= H D^(2+epsilon) R^(2b-1)` now holds for all `1 <= R <= D`. At `b=7/8`, the previous upper range was `D^(4/5)`. | The same proof, including all intersections, arbitrary within-side gcd cuts, and the endpoint `R=D` |
| Dense cross-gcd sector | At every fixed `k>=3`, `|S| <= H D^(1+epsilon) R^(2b(k-1))`, for `k/(2(k-1)) <= b <= 1`. It is diagonal-size for `R <= D^(1/(2b))`. | [DENSE_CROSS_GCD_SECTORS.md](DENSE_CROSS_GCD_SECTORS.md), with a complete induced-subset inequality proof |
| Joint Gauss continuation | The actual reunited three-cusp `Y_k(s,v)` is holomorphic for `Re s<1/2`, `Re(v-s)>1/2`, `Re(v-2s)>3/5`, with squarefree-row energy `H^(10/7+epsilon)`. | [JOINT_GAUSS_REUNION_CONTINUATION.md](JOINT_GAUSS_REUNION_CONTINUATION.md), using the counting theta/inverse inputs; no angular reciprocal estimate is needed |
| Principal cube tails and strict covariance pruning | The actual long cube inverse has complete-residue principal energy `O(D^epsilon/R)`. A specified region of the exact strict A2 comparison has rapid decay after complete smooth row cancellation. | [CENTERED_COVARIANCE_AND_CUBE_ALIASES.md](CENTERED_COVARIANCE_AND_CUBE_ALIASES.md), with exact masks, two independent corrections, and the reconstructed product diagonal |
| Short and long principal blocks | Above a fixed sixth-root ratio of the physical product supports, the four centered principal blocks are exactly `[[T,-T],[-T,T]]`, with `|T| <= D^epsilon/sqrt(R_1 R_2)`. | [PRINCIPAL_SHORT_LONG_COVARIANCE.md](PRINCIPAL_SHORT_LONG_COVARIANCE.md), for the squarefree raw columns and their exact cube inverses; independent exterior A2 shifts require a new calculation |

Each result is about its specified object. In particular, a bound for
`Y_k` is not automatically a bound for the original Möbius moment, and a
principal-energy bound is not a full finite-height energy bound.

## 2. How the graph argument keeps the signs

For a Hermitian `2k`-tuple, decompose every column into the primes unique
to that column and the primes shared by each exact subset of positions.
The native row height is `H=D^h` for a fixed admissible `h>1`, under the
stated `NM2` and `PW_b` hypotheses. The examples with `b=7/8` require the
separately stated uniform `PW_(7/8)` input.
Freeze all shared incidence ideals first. Every condition on the gcd
graph, including its missing edges and any overlaps between matchings,
is then constant while the singleton columns are summed.

An exact finite Euler correction removes coprimality between the free
singleton columns. Native row Cauchy on two columns gives exponent
`1/2` on those axes, and the existing pointwise premise gives exponent
`b` on the others. A charge placed on a large-gcd edge converts its
threshold into a saving. The sufficient condition is explicit:

\[
 \sum_{e\subseteq I}w_e\le\sum_{v\in I}\gamma_v-1
 \qquad(|I|\ge2),
\]

where two `gamma_v` equal `1/2` and all others equal `b`. It leaves every
shared-ideal sum with exponent at least one, hence only a fixed
logarithmic loss. The cancellation in the singleton sums is used before
the positive accounting over shared labels.

For the graph whose edges mean `N gcd(n_i,m_j)>=D/R`, let `r` be its
spanning-forest rank and `z` its number of isolated vertices. Set

\[
 \tau=r-1+\min(1,z/2),\qquad a=2b-1.
\]

Any permitted selector supported on `tau>=tau_0` satisfies

\[
 |S|\ll HD^{k+a(k-1-\tau_0)+\epsilon}R^{a\tau_0}.
\]

This controls the entire union of near-perfect matchings, the larger
rank-at-least-`k-1` region, and all connected graphs. The connected
region is diagonal-size for `R<=D^(1/2)`. Fractional charges give an
additional four-cycle improvement.

For a complete cross graph, a denser charge reaches

\[
 |S|\ll HD^{1+\epsilon}R^{2b(k-1)}.
\]

At `b=7/8`, this is diagonal-size through `R<=D^(4/7)`, equivalently
when every cross gcd is at least `D^(3/7)`. This `4/7` is an arithmetic
gcd-cutoff exponent, distinct from the earlier spectral threshold
`Re u>4/7`. Neither is a zeta zero-free constant.

The result still has two important quantifiers: the order `k` is fixed,
and a selector cannot depend on the free singleton ideals. At `R=D`,
every edge condition is automatic and the theorem returns the original
two-axis bound; no saving is claimed at that endpoint.

## 3. What joint Gauss summation changes

The #922 cube reunion produces two coupled squarefree Gauss factors.
Keeping them together gives the exact Dirichlet family

\[
 \mathcal B_{k,f}(t,u)=
 \sum_{ab\,\mathrm{squarefree}}
 \frac{a_\xi(ab)\omega(b)\chi_{ab}(k)\chi_{ab}(f)^4}
 {(Na)^t(Nb)^u}.
\]

The all-row anisotropic inverse, with the shorter factor chosen as the
outer axis, bounds its normalized physical block by

\[
 \sum_{k\asymp H}|P_{k,f}(A,B)|^2
 \ll (2HFAB)^\epsilon H^{10/7}F^{2/3}\min(A,B)^{6/5}.
\]

Joint dyadic Mellin summation therefore converges normally when

\[
 \Re t>\tfrac12,\quad\Re u>\tfrac12,
 \quad\Re(t+u)>\tfrac85.
\]

After the exact cube identity, the residual correction is a convergent
sum over an auxiliary `z` with denominator `(Nz)^(t+w)`. Its phase,
mask and fourth-power twist are specified in the proof. The full bad
prime, ramified and cusp expansion remains summable on this domain.
With `t=1-s` and `u=v-s`, this gives the new tube for the same `Y_k`.
It crosses `v=1` for every `Re s<1/5`, extending the old crossing
`Re s<0`.

The stronger continuation pays row energy `H^(10/7+epsilon)`. The
previous `H^(1+epsilon)` mean remains available on its smaller domain.
The proof explicitly checks that the new scalar contour envelope is
dominated by existing completed bounds. Thus this analytic-domain
advance is not reported as a physical moment improvement.

## 4. The two-column inverse and its exact principal subtraction

The full A2 product support has prime exponents `0,1,3,4`. Distinct
products on this support yield nonprincipal row characters. Unrestricted
theta cubes change this: products `m d^3` and `m (d')^3` have a principal
complete-residue correlation when `d/d'` is a square, even if the products
differ. Their literal zero masks can still differ.

The exact principal kernel is

\[
 \Pi(n,n')=
 \mathbf1_{v_p(n)\equiv v_p(n')\ (6)\ \forall p}
 \prod_{p\mid nn'}(1-(Np)^{-1}).
\]

Full Möbius inversion cancels the extra cube terms before any row norm
is taken. A truncated inverse need not cancel them. The new proof groups
`d=sj^2`, retains the common zero masks and obtains

\[
 \|L_R\|_{\mathrm{pr}}^2\ll D^\epsilon/R,
 \qquad
 |\langle L_R,L'_{R'}\rangle_{\mathrm{pr}}|
 \ll D^\epsilon/\sqrt{RR'}.
\]

This is the complete-residue principal part. The ordinary product
diagonal has the same upper bound. A second exact identity turns the
joint cutoff `N lcm(h,h')<=R` into one Möbius divisor sum over
`rad(dd')`; finite witnesses show why it has no automatic positivity
or advantage over a rectangular cutoff.

There is a sharper consequence for comparable fixed physical product
supports. Write each raw squarefree column as `P_j=S_j+T_j`, its short
and long inverse parts. Principal pairing of a raw product with a long
cube product forces the latter to have the form `m j^6`. A nonzero
long inverse coefficient requires a squarefree divisor of `j` above
the cutoff. Therefore a cutoff at least the sixth root of the cross
support ratio makes both raw/long principal cross terms exactly zero.
The four centered principal blocks are consequently

\[
 \begin{pmatrix}\mathcal T&-\mathcal T\\-\mathcal T&\mathcal T\end{pmatrix},
 \qquad |\mathcal T|\ll D^\epsilon/\sqrt{R_1R_2}.
\]

For the original balanced first-Poisson normalization, the full signed
`b,f` accounting gives `O(D^epsilon L/R)` for each off-product
zero-frequency block, where `L=AB` is the original product scale.
Their sum is exactly zero. These are
bounds for the principal artifacts of truncation; the remaining
nonzero frequencies are not estimated by this identity.

Before unrestricted cubes are inserted, complete smooth row Poisson
gives rapid decay for a strict reconstructed A2 pair whenever

\[
 \Lambda=
 \frac{F^2\Delta(N)\Delta(N')\,
 N\gcd(\operatorname{rad}N,\operatorname{rad}N')}
 {H_{\mathrm{orig}}}
 \ge D^\delta,
 \qquad
 \Delta(N)=\frac{\mathrm N(N)}{\mathrm N(\operatorname{rad}N)}.
\]

For two correction triples with products `C,C'`, one sufficient
condition is `F N(C) N(C')>=H_orig^(1/2)D^(delta/2)`. The exact original
diagonal, both corrected auxiliaries, and every prescribed A2 row phase
must be retained. An extra row twist that changes the reconstructed
character is not covered by this pruning theorem.

## 5. The remaining attack and the connection to 17/24

The graph result removes a previous obstruction to combining many
overlapping signed sectors. It can be composed with #926's sharper
within-side Möbius tail and with the positively accounted conductor
regions of #914/#925, using the exact subtraction stated in the graph
proof. Restricting a below-diagonal signed estimate to a hard conductor
region can add back a diagonal-size error; that cost is retained.

The far-separated singleton region remains. When `R<D`, pairwise
coprime columns give no graph edge and the present two-axis argument
still has the excess `(2b-1)(k-1)`. It is linear in `k` for fixed
`b>1/2`. The new covariance pruning also leaves the all-unit, coprime
core, where `Lambda=1/H_orig`.

Two routes have now been ruled out as automatic fixes. Fixed logarithmic
scale averaging alone does not remove the balanced tuple shell (#926),
and principal-alias subtraction alone cannot remove the reflected
long-column `U` term: the new note gives a centered arbitrary-vector
witness with no cubes or aliases at all. The missing input must use the
literal arithmetic coefficients or their signed coupled row kernel.

The concrete next target remains the original strictly off-product-
diagonal first-Poisson expression from #914, with its signed auxiliary
sum and coupled kernel. The new joint Gauss identity and the single-
divisor joint inverse can be inserted into that expression with their
phases and masks now specified; a useful cancellation estimate after
that insertion has not been proved.

The existing cofinal extraction of #919 reads

\[
 \sigma>\frac12+\frac{5h}{12k}+\frac{\lambda}{2k}
\]

for the source's stated signed dyadic moment bound at row height `D^h`
and whole-moment excess exponent `lambda`. In #919's signed-remainder
criterion this is `lambda=max(e,(2b-1)q)`, including the controlled
regions as well as the remaining signed average with excess `e`.
A full fourth moment with `lambda=0`
and `h` approaching one would give `17/24`. A suitably covered cofinal
family with `h_k,lambda_k=o(k)` would reach the critical line
qualitatively, retaining the source's coverage of the fixed primitive
twist and its contragredient. These required whole-moment estimates
remain open. The arithmetic row height, the spectral variables `s,v`, and a zeta zero's
ordinate are separate quantities throughout this packet.

## 6. Sources, review, and reproduction

[SOURCE_LOCK.json](SOURCE_LOCK.json) binds every load-bearing and
comparison source to its original commit, Git blob, byte size and
SHA-256. The six newly used adjacent source files are copied exactly;
previously retained sources are referenced at their existing locations.
No earlier proof packet is edited.

[VALIDATION.md](VALIDATION.md) records the independently rerun finite
checks, exact manuscript review bindings and limitations. The analytic
proofs are in the five notes above. The checks concern finite
arithmetic, rational exponent identities, graph constraints and source
integrity; they do not test infinite moments or establish the imported
analytic premises. Reviews are scoped independent AI-agent reviews,
not human peer review or proof-assistant certification.
