# Four theorem nominations from the L-function detector atlas

All statements below are **proposed targets**, not results. They are written to
make the missing arithmetic input explicit and to prevent a finite experiment
from being mistaken for a theorem.

## Target A — function-field trace individualization

Nomination: `FF-XD-TRACE-INDIVIDUALIZATION`
Programmes: #737 and #741.

Let `q` be an odd prime power and give the complete hyperelliptic family
`H_{2g+1}(q)` the uniform measure on monic squarefree polynomials of degree
`2g+1`. Work in the regime of fixed `g` and fixed kernel `K` as `q` tends to
infinity. Derive from one declared reciprocal-L degree kernel a finite
Hermitian statistic

\[
X_D(K)=\sum_{m,n=0}^{2g}K_{mn}H_D(m)\overline{H_D(n)},
\qquad H_D(n)=q^{-n/2}B_D(n),
\]

where `K=K^*` and `K` is the genuine function-field adapter for a selected canonical
`XD` or `HCNC` detector, not the toy lag-one probe.

For `U in USp(2g)`, let `H_U(n)` denote the coefficient of `t^n` in
`det(I-tU)^{-1}` and define

\[
X_U(K)=\sum_{m,n=0}^{2g}K_{mn}H_U(m)\overline{H_U(n)}.
\]

Prove an effective monodromy trace and variance theorem

\[
\frac1{|H_{2g+1}(q)|}\sum_D X_D(K)
=\int_{USp(2g)}X_U(K)\,dU+E_1(q,g,K),
\]

\[
\operatorname{Var}_{D\in H_{2g+1}(q)}X_D(K)
=\operatorname{Var}_{U\in USp(2g)}X_U(K)+E_2(q,g,K),
\]

with explicit errors strong enough to decide whether the required one-sided
bound is density-one or only averaged. Mean and variance control do not imply a
memberwise bound without an additional discrete gap or a pointwise estimate.
Before invoking monodromy, first determine whether the genuine kernel has a
deterministic sign on the `USp(2g)` character image; if it does not, the Haar
model may refute rather than support density-one positivity.

Why this target: the exhaustive `q=5,g=1` result proves that purity plus mean
cancellation cannot perform individualization. The exhaustive `q=3,g=2` result
shows that exact purity and the palindromic functional equation still allow all
three signs for a parity-even toy minor. The missing input must therefore
control the actual kernel's fluctuation or exceptional members, plausibly
through monodromy/sheaf estimates.

Number-field handoff: formulate the corresponding trace/exponential-sum bound
for the same coefficient kernel over integers; do not transfer the conclusion
merely from function-field RH.

## Target B — quadratic-twist excess-rank second moment

Nomination: `TWIST-EXCESS-RANK-L2`
Programmes: #738 and #741.

Fix a source-locked primitive self-dual GL(2) form `f`. For fundamental
discriminants in one explicitly defined root-number subfamily
`D_epsilon(X)`, let

\[
r_d=\operatorname{ord}_{s=1/2}\Lambda(f\otimes\chi_d,s),
\qquad
e_d=r_d-\frac{1-\varepsilon}{2}\in2\mathbf Z_{\ge0}.
\]

First prove the bounded second moment

\[
\sum_{d\in D_\varepsilon(X)}e_d^2
\ll_f |D_\varepsilon(X)|.
\]

The stronger minimalist-rank target is

\[
\frac1{|D_\varepsilon(X)|}\sum_{d\in D_\varepsilon(X)}e_d^2=o(1).
\]

For any fixed positive centered node packet this is exactly equivalent to the
same bound for the average squared parity/full detector correction:

\[
\frac1{|D_\varepsilon(X)|}\sum_d
\|M_d^{\rm parity}-M_d^{\rm full}\|_F^2
=\left(\sum_i x_i^{-2}\right)^2
\frac1{|D_\varepsilon(X)|}\sum_de_d^2.
\]

Why this target: it isolates legitimate rank contamination without depending
on the Loewner/Pick sign convention. It also controls the high-rank tail, which
a mere density-one nonvanishing statement need not do.

## Target C — root-number-split reciprocal-prime wavelet moment

Nomination: `TWIST-RECIPROCAL-PRIME-M2`
Programmes: #738 and #741, with a handoff to #737.

Fix the same `f`, one root-number subfamily, and a compact real prime weight
`w_p(P)` obtained from a declared reciprocal-L wavelet adapter. At good primes
define

\[
W_d(P)=\sum_{p\le P}
w_p(P)\frac{a_p(f)\chi_d(p)}{\sqrt p}.
\]

Prove, uniformly in a nontrivial range `P<=X^theta`, an exact diagonal main term
with a power-saving or otherwise summable off-diagonal error:

\[
\delta_{\varepsilon,X}(p)
=\frac1{|D_\varepsilon(X)|}
\sum_{d\in D_\varepsilon(X)}\chi_d(p)^2,
\]

\[
\frac1{|D_\varepsilon(X)|}\sum_{d\in D_\varepsilon(X)}W_d(P)^2
=\sum_{p\le P}w_p(P)^2\frac{a_p(f)^2}{p}
\delta_{\varepsilon,X}(p)
+O_{f,w}(E(X,P)),
\]

where bad primes, the fundamental-discriminant condition, and the root-number
restriction are all explicit. Away from special primes the unconditioned local
density is asymptotic to `p/(p+1)`, not `1`; the root-number restriction may
change it and must be computed. The error `E(X,P)` must be strong enough for the
intended compact detector limit.

Why this target: the Phase-0 table shows that raw GL(1) unit amplitude does not
survive degree two. This moment uses the correct unitary GL(2) coefficient and
asks quadratic-character orthogonality to supply the family law. The analogous
function-field theorem should be attacked first by exact character sums and
monodromy, providing a formula—not a transfer claim—for the number-field target.

The exact conductor-coprime precursor now computes the complete raw Gram and
centered covariance matrices for the fixed `11.a2` prime packet at
`X=256,512,1024,2048`, both pooled and in the sourced root-number cohorts
`epsilon_d=sign(d)*(d/11)`. The root-sign counts at the largest window are
568/574. Its pooled weighted radical correction to `E(W_d^2)` is nonmonotone,
and the root-cohort second-moment difference also changes sign across the four
windows. The off-diagonal root-cohort Gram-contrast RMS decreases from
`0.108858` to `0.039862`, but `sqrt(N)` times that RMS stays of order one and
the maximizing pair moves. The separate 13-prime character-mean contrast has
RMS `0.129637,0.097490,0.068315,0.044893`, while its `sqrt(N)`-scaled values
remain between `1.517080` and `1.645824`; the local-density contrast is smaller
and also nonmonotone after scaling. This is why the target asks for weighted,
uniform off-diagonal and marginal estimates rather than extrapolating an
unweighted finite RMS or fitted rate.

## Target D — genus-two higher moments and effective USp(4) equidistribution

Nomination: `FF-GENUS2-TOY-MINOR-HIGHER-MOMENTS`
Programmes: #737 and #741.

For odd prime powers `q`, let `H_5(q)` be the uniform family of monic
squarefree quintics and write

\[
P_D(u)=1+a_Du+b_Du^2+qa_Du^3+q^2u^4,
\qquad
\frac1{P_D(u)}=\sum_{n\ge0}B_D(n)u^n.
\]

The exact algebraic lemma

\[
B_D(1)B_D(3)-B_D(2)^2=qa_D^2-b_D^2
\]

and the following first-moment formula are now proved in the bound DRAFT
research note:

\[
\frac1{|H_5(q)|}\sum_{D\in H_5(q)}
\frac{qa_D^2-b_D^2}{q^2}
=-\left(1-\frac1q\right)^2+\frac{q+1}{q^5}
\longrightarrow-1.
\]

Combining this identity with the exact compact-group range
`-20<=F<=4/3` also proves, for
`P(q)=q^5-2q^4+q^3-q-1`,

\[
\rho_-(q):=\frac{|\{D:qa_D^2-b_D^2<0\}|}{|H_5(q)|}
\ge\frac{P(q)}{20q^5},
\qquad \liminf\rho_-(q)\ge\frac1{20}.
\]

Thus negative-member existence and a uniform asymptotic density floor no longer
need nomination. The bound is one-sided and does not determine the sign law.

The remaining target begins at moment two. One of its three coefficient pieces
is now exact: reweighting the linear-only rows of the proved quartic table gives

\[
\sum_Da_D^4
=q(q-1)(q+1)(3q^4-10q^3+15q^2-3q-11),
\]

so

\[
\mathbb E[(a_D/\sqrt q)^4]
=3-\frac7q+\frac5{q^2}+\frac{12}{q^3}
-\frac{14}{q^4}-\frac{11}{q^5}\longrightarrow3.
\]

A separate three-row degree-two calculation now also proves

\[
\mathbb E[b_D]=q-1+\frac{q^2-1}{q^3}.
\]

A seven-type quartic reweighting further proves

\[
\mathbb E[a_D^2b_D]
=\frac{(q+1)(q^2-2q+3)(2q^2-2q-1)}{q^3}.
\]

Together with the proved `a_D^2` and `b_D^2` formulas, this isolates the exact
low-weight character means

\[
\langle\chi_{0,1}\rangle_q=-q^{-1}+q^{-2}-q^{-4},\qquad
\langle\chi_{2,0}\rangle_q=q^{-3}-q^{-4},\qquad
\langle\chi_{0,2}\rangle_q=-q^{-1}-q^{-5},
\]

\[
\langle\chi_{2,1}\rangle_q=2q^{-3}-q^{-4}-2q^{-5},\qquad
\langle\chi_{4,0}\rangle_q=-3q^{-5}.
\]

A higher-moment proof should preserve this unequal decay: treating all
nontrivial characters as a single generic `O(q^{-1})` error discards the exact
`q^{-3}` suppression in the `chi_(2,0)` and `chi_(2,1)` channels and the
`q^{-5}` suppression in `chi_(4,0)`.

Writing

\[
A_4=\sum_Da_D^4,\qquad
M_{22}=\sum_Da_D^2b_D^2,\qquad B_4=\sum_Db_D^4,
\]

the exact reduction is

\[
\sum_DK_D^2=q^2A_4-2qM_{22}+B_4.
\]

The remaining arithmetic is finite but not elementary bookkeeping: the same
squarefree sieve reduces it to 20 degree-six signatures for `M_22` and 54
degree-eight signatures for `B_4`. Their new inputs are six marked
quadratic-character coefficient families (`p_1` in conductor degree four;
`p_1,p_2` in degree six; and `p_1,p_2,p_3` in degree eight), sometimes with
deletion-character factors. Principal and collision strata are polynomial;
reciprocity may create a `chi_q(-1)` branch, while surviving coefficient
averages may be genuine Frobenius-trace terms. A polynomial or two-branch fit
must therefore be proved rather than inferred from `q=3,5,7`.

The exact radical-degree census further localizes the work. The generic
degree-six part of `M22` has only three signatures, with leading mixture
`(1,2,1)/4`; the generic degree-eight part of `B4` has only five, with leading
mixture `(1,4,6,4,1)/16`. Every collision or even-exponent stratum has lower
type-count degree. A practical first lemma should therefore aggregate these
eight generic conductor types before estimating them individually, then prove
the cancellation of the next collision layers needed for the conjectural
`O(q^{-2})` high-weight average.

There is an equivalent, especially compact representation-theoretic target.
Put

\[
F(U)=(\operatorname{Tr}U)^2-e_2(U)^2,
\qquad U\in USp(4).
\]

For `chi_(a,b)` denoting highest weight `a*omega_1+b*omega_2`, exact `C_2`
decomposition gives

\[
\begin{aligned}
F^2={}&3+4\chi_{0,1}+2\chi_{2,0}+4\chi_{0,2}+2\chi_{2,1}
+\chi_{4,0}+2\chi_{0,3}+\chi_{2,2}+\chi_{0,4},\\
(\operatorname{Tr}U)^4={}&3+5\chi_{0,1}+6\chi_{2,0}+2\chi_{0,2}
+3\chi_{2,1}+\chi_{4,0}.
\end{aligned}
\]

Since the normalized trace fourth moment is exact, the entire second-moment
limit first reduces to the displayed virtual character. The new exact
`a_D^2b_D` formula resolves its last two low-weight channels. Writing

\[
H=\chi_{0,4}+\chi_{2,2}+2\chi_{0,3},
\]

the complementary low-weight part has the exact average

\[
-q^{-1}-q^{-2}-6q^{-3}+6q^{-4}.
\]

Therefore the target is now the honest high-weight assertion
`mean(H)->0`, equivalent to the desired second-moment limit. The frozen exact
values provide regression controls only:

\[
\mathbb E[(K_D/q^2)^2]
=\frac{2408}{3^7},\quad\frac{131504}{5^7},\quad
\frac{1645440}{7^7}.
\]

The corresponding exact means of `H` are

\[
\frac{536}{2187},\qquad\frac{7154}{78125},\qquad
\frac{37652}{823543}.
\]

Their `q^2` rescalings are `536/243`, `7154/3125`, and `37652/16807`, all
near `9/4`. The cleanest sharpened target is therefore first to prove
`mean(H)=O(q^{-2})`; a secondary conjecture is

\[
q^2\langle H\rangle_q\longrightarrow\frac94.
\]

The constant is a three-field nomination, not an interpolation theorem. A
cohomological calculation should decide whether `9/4` is genuine, replaced by
a congruence-dependent main term, or merely a small-field coincidence.
Indeed, the exact deviations of `q^2 mean(H)` from `9/4` have signs
`-,+,-`, matching `chi_q(-1)` on the three frozen fields. There is only one
sample in the positive branch, so the target should allow an
`eta_q=chi_q(-1)` lower-order term until reciprocity rules it out.

The exact affine action

\[
D(T)\longmapsto \alpha^{-5}D(\alpha T+\beta)
\]

fixes `K_D` and partitions the frozen `q=3,5,7` families into 29, 132, and
349 weighted orbits. A proof may exploit this quotient, but it must retain
orbit-size weights and separate automorphism strata; in characteristic five,
`T^5-T` is fixed by the entire affine group. Burnside or stack-weighted trace
formulas are therefore more faithful than an unweighted representative sum.
The same action with a nonsquare scaling proves every joint moment odd in
`a_D` vanishes exactly; a correlation calculation may discard those strata
before doing any character-sum work.

For each fixed `m>=2`, prove an effective formula

\[
\frac1{|H_5(q)|}\sum_{D\in H_5(q)}
\left(\frac{qa_D^2-b_D^2}{q^2}\right)^m
=\int_{USp(4)}F(U)^m\,dU+E_m(q),
\qquad E_m(q)\longrightarrow0,
\]

uniformly for `m` in any range needed by the chosen detector. Ideally expose
the conductor and representation dependence in an explicit square-root-scale
or better error, or derive exact rational functions in `q` for the first few
fixed moments. The normalization uses `P_D(t/sqrt(q))=det(I-tU)`, so
`a_D/sqrt(q)=-Tr(U)` and `b_D/q=e_2(U)`. Since
`Lambda^2 Std` is `1 + V_(omega_2)`, character orthogonality gives the proved
first Haar mean `-1`. Exact `C_2` Weyl constant terms give the next five targets

```text
m=2,3,4,5,6: 3, -11, 56, -374, 3117.
```

More structurally,
`F=-(1+chi_(0,1)+chi_(0,2))` is minus the character of an honest
20-dimensional representation containing the trivial summand. Hence every
Haar moment, at every order, is a nonzero integer with sign `(-1)^m`; the six
displayed values are the first tensor-invariant multiplicities. This exact
all-order sign theorem concerns the compact group and does not imply the
corresponding finite-family limits.

There is now a finite-moment payoff strictly between the unconditional
`1/20` floor and full sign equidistribution. For

\[
R(x)=1+\frac{5405x+264x^2-23x^3}{12023},
\]

the exact support bound gives `1_{x>=0}<=R(x)^2`, and the six Haar moments give

\[
\mathbb E_{\mathrm{Haar}}R(F)^2=\frac{7663}{12023},
\qquad
\mu_{\mathrm{Haar}}(F<0)\ge\frac{4360}{12023}.
\]

An exact support-adapted majorant improves that baseline. With
`t=(3x+28)/32`, set

\[
p(t)=\frac{(t+1)(20t-13)^2(40t-7)^2(2927-2792t)}{14407470}.
\]

Its factorization proves `p>=0` on `[-1,1]`; the identity
`p(t)-1=(t-7/8)(1-t)Q(t)` and five positive Bernstein coefficients for `Q`
prove `p>=1` on `[7/8,1]`. Exact moment substitution gives

\[
\mathbb E_{\mathrm{Haar}}p\!\left(\frac{3F+28}{32}\right)
=\frac{3879608783}{6358302720}.
\]

Consequently, proving convergence for moments `m=2,...,6` already yields the
stronger conditional conclusion

\[
\liminf_{q\to\infty}\rho_-(q)
\ge\frac{2478693937}{6358302720}\approx0.389836,
\]

without needing full weak convergence or control of mass near `F=0`. This is a
certified lower bound, not the exact Haar sign probability or a claimed optimal
degree-six bound. It makes the six fixed-moment formulas a useful standalone
theorem target even if an effective sign-law rate remains out of reach.

There is now a stronger twelve-moment rung. Exact `C_2` constant terms give

```text
m=7,...,12: -30321, 327688, -3815668, 46998100, -605231862, 8084025096.
```

A separately replayed factorized degree-twelve majorant, certified by a
positive quadratic square-completion remainder and ten positive rational
Bernstein coefficients, proves

\[
\mu_{\mathrm{Haar}}(F<0)\ge
\frac{153081644970674178368978470022738347661743507912075314789490808683}
{318454738700269877013669525120657835305950388794994707229994647552}
\approx0.480701.
\]

Thus formulas through `m=12` would upgrade the conditional finite-family
liminf from `0.389836` to `0.480701`. The polynomial was discovered
numerically but is accepted by exact rational algebra; neither it nor the
degree-six predecessor is claimed optimal. This creates two useful stopping
points for a proof: moments through six already give a substantial density
theorem, while moments through twelve give a materially stronger one.

The finite histogram supports at `q=3,5,7` are exactly
`[-8/3,8/9]`, `[-116/25,29/25]`, and `[-282/49,59/49]`. Their positive edges
move near the Haar endpoint `4/3`, but their negative edges remain far from
`-20`. Any effective high-moment argument must therefore control the rare
far-negative Frobenius classes rather than treating the discrepancy as
uniform smoothing across the support.

The minimum is one affine orbit in each frozen field: sizes `6,10,42`, with
stabilizer orders `1,2,1`. This makes a stack-weighted analysis of the extreme
automorphism strata a plausible route to the high-moment tail; an unweighted
orbit-representative average would erase exactly the multiplicities that
matter most.

Quantitatively, each single minimum orbit contributes more than half of the
frozen twelfth moment (`58.3993%`, `61.9548%`, `73.4068%`). A useful tail lemma
should therefore separate the extreme orbit/automorphism strata before
applying generic monodromy estimates to the bulk.

The symplectic trace discriminant `(x_1-x_2)^2` on the three minimum orbits is
exactly `4/3,0,5/7`. In particular the characteristic-five orbit lies on the
repeated-angle diagonal and has the extra involution already seen in its
stabilizer. The tail lemma should isolate this near-diagonal/endoscopic locus
before invoking estimates valid only on the regular semisimple bulk.

The bounded shifted-grid Weyl quadrature additionally nominates

\[
\mu_{\mathrm{Haar}}\{U:F(U)<0\}\approx0.738,
\]

while the exact finite proportions at `q=3,5,7` are respectively
`17/27, 33/50, 33/49`. The boundary `F=0` is the zero set of a nonzero
polynomial in the two trace coordinates and therefore has Haar measure zero.
Consequently weak convergence to Haar already implies convergence of the sign
proportions; an effective rate for this discontinuous indicator needs
quantitative boundary control. The displayed probability is numerical, not a
certified interval or a premise of the target.

Using only that display value, the three quantities
`sqrt(q)*(mu_Haar-rho_-(q))` are `0.187442, 0.174076, 0.170333`. Their tight
clustering nominates the concrete effective target

\[
\rho_-(q)=\mu_{\mathrm{Haar}}(F<0)+O(q^{-1/2}).
\]

A secondary numerical possibility is a one-sided leading correction of size
about `0.17/sqrt(q)`. The bound, not that constant, is the responsible theorem
target: three fields and a non-rigorous quadrature value cannot determine an
asymptotic coefficient.

Why this target: the first moment no longer needs nomination. Its exact
squarefree-sieve proof shows that low moments can expose structure more sharply
than a three-field fit. The higher moments now test whether the full
hyperelliptic family approaches the compact-group law, not merely whether one
average has the right limit. A proof should decompose `F^m` into `USp(4)`
characters or evaluate the corresponding finite-field correlations, with an
effective error. This target remains about a toy coefficient minor; it does
not rename that minor as `XD`, `HCNC`, or a Pick/Loewner theorem.

## Falsification and promotion rules

For each nomination, a future computation should retain:

- the exact family definition and root-number split;
- the completed and local normalization fingerprints;
- a frozen detector contract before the final scan;
- explicit exceptional members and negative controls;
- source/coverage hashes and a compact replay;
- separate labels for memberwise, family-average, and density-one conclusions.

No target becomes a theorem node from numerical fit alone.
