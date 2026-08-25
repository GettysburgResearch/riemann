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

## Exact control adjacent to Target D — genus-one modular moment tower

This is a benchmark, not a new conjectural target. For monic squarefree cubics
`D` over any odd `F_q`, uniform models are the normalized elliptic-stack
measure. If `P_m(a,q)` is the `Sym^m H^1` trace, the standard level-one modular
trace formula gives

\[
\sum_{[E]/\mathbb F_q}\frac{P_m(a_E,q)}{|\operatorname{Aut}(E)|}
=q\ (m=0),\quad 0\ (m\text{ odd}),\quad
-1-\Theta_{m+2}(q)\ (m>0\text{ even}).
\]

After the elementary `SU(2)` tensor decomposition, every even raw moment is

\[
W_{2n}(q)=C_nq^{n+1}
-\sum_{j=1}^n
\left(\binom{2n}{n-j}-\binom{2n}{n-j-1}\right)
q^{n-j}\bigl(1+\Theta_{2j+2}(q)\bigr).
\]

The first cuspidal term is `-Theta_12(q)` in the tenth moment. This is the
model to imitate in higher genus: identify the compact-group multiplicity,
the boundary term, and the automorphic/cohomological trace separately, rather
than fitting a rational function to small fields. It also supplies a quotient
warning. The full affine branch quotient identifies quadratic twists and does
not carry a signed trace; the square-affine quotient is the elliptic
isomorphism quotient and does.

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
of order one. The cleanest theorem target remains
`mean(H)=O(q^{-2})`. A new exact triangularization isolates the three missing
raw moments:

```text
R3  = chi_(0,3)                         <-> b_D^3
R22 = chi_(0,3)+chi_(2,2)              <-> a_D^2 b_D^2
R4  = chi_(0,4)+3chi_(2,2)+4chi_(0,3)  <-> b_D^4.
```

A bounded generator finds 23 cubic signatures and proves that their primitive
coefficient terms do not cancel type by type. The next lemma must therefore
evaluate genuine marked trace averages. The current sparse conjecture is

\[
\langle\chi_{0,3}\rangle_q\stackrel{?}{=}\frac{q^4-2q-1}{q^6},\quad
\langle\chi_{2,2}\rangle_q\stackrel{?}{=}
\frac{2q^3-q^2-2q-2}{q^6},\quad
\langle\chi_{0,4}\rangle_q\stackrel{?}{=}-\frac{2q^2+1}{q^7}.
\]

It matches only `q=3,5,7`. If proved, it gives

\[
\langle H\rangle_q=
2q^{-2}+2q^{-3}-q^{-4}-8q^{-5}-4q^{-6}-q^{-7}
\]

and hence `q^2 mean(H)->2`. This replaces the earlier visual `9/4` cluster as
the preferred structured conjecture; neither constant has evidence beyond the
same three fields. There is only one sample with `chi_q(-1)=+1`, so the target
must still allow a reciprocity-dependent lower term until the trace calculation
rules it out.

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

The weighting itself is now exact for every odd `q`:

\[
\sum_{[D]}|\operatorname{Stab}(D)|^{-1}=q^3,\qquad
N_q=q^3+q-1+2\mathbf1_{4\mid q-1}+4\mathbf1_{5\mid q-1}
+\mathbf1_{\operatorname{char}F_q=5}.
\]

The first identity is the uniform equation/marked-stack measure; `N_q` is the
coarse presentation count. A geometric proof must identify which of these is
the measure on its chosen local-system stack rather than using “one curve, one
vote” implicitly. The general degree-`2g+1` affine Burnside formula shows that
the relative orbit-count excess begins at `q^{-g}`, universally from affine
involutions.

The stronger all-degree record should guide any change of presentation. With
`S_q(u)=(1-qu^2)/(1-qu)` and `A_q(u)=S_q(u)/(1+u)`, the exact coarse-orbit
series is

\[
\sum_{n\ge0}O_{q,n}u^n=
\frac{S_q(u)+q\sum_{\substack{d\mid q-1\\d\ge2}}
\varphi(d)(1+u)A_q(u^d)+(q-1)S_q(u^p)}{q(q-1)}.
\]

Thus a proposed trace formula should expect separate automorphism strata in
degree classes `0,1 mod d` for multiplicative order `d`, and in degrees
divisible by `p` for translations. These resonances count presentations only;
their correlation with `R_6`, `H`, or another Frobenius statistic remains an
arithmetic-geometric target.

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

It also no longer distinguishes genus two: dual Jacobi--Trudi gives
`e_(g-1)e_(g+1)-e_g^2=-s_(2^g)` in every rank, and the fixed-depth
`e_1^2-e_2^2` is minus an honest character for every `g>=2`. A sharper
arithmetic subtarget is therefore the balanced virtual control

\[
B=2e_1^2-e_2^2=\chi_{2\omega_1}-\chi_{2\omega_2}.
\]

Its odd Haar moments vanish, its even moments are

\[
\operatorname{Haar}(B^{2r})=\frac1{r+1}\binom{2r}{r}^2,
\]

and its exact Haar law is the product of independent arcsine and semicircle
variables on `[-2,2]`. In particular its Haar sign is exactly `1/2`--`1/2`.
The finite quintic family already has the exact nonzero mean

\[
\langle B_D\rangle_q=q^{-1}+q^{-3}-q^{-4}+q^{-5}.
\]

The independently enumerated `q=3,5,7` member ledger now source-locks the
complete joint coefficient law and the raw sums needed by the high-weight
packet. Exact `C_2` reduction gives

\[
B^3=6B-2\chi_{0,3}+R_6,
\qquad
R_6=2\chi_{2,3}+3\chi_{6,0}-3\chi_{4,2}
+\chi_{2,4}-\chi_{0,6}.
\]

Therefore the next clean arithmetic lemma is the explicit formula or a
power-saving bound for `mean(R_6)` in

\[
\langle B_D^3\rangle_q=
6(q^{-1}+q^{-3}-q^{-4}+q^{-5})
-2\langle\chi_{0,3}\rangle_q+\langle R_6\rangle_q.
\]

The `chi_(0,3)` term is independently recoverable from the source-locked
`sum b_D^3`. Unlike the original alternating sign, any odd bias here is not
preinstalled by the compact group. The frozen values of `mean(R_6)` at three
fields are regression controls, not an all-`q` formula.

There is a separate low-dimensional powered target. For the balanced controls
`B_r` formed from `r`-th Frobenius powers, every `r>=3` is already determined
pointwise by `(B_1,B_2)` through an order-four recurrence. Higher echoes are
therefore resonance amplifiers, not new detector coordinates. Their exact Haar
law has pairwise orthogonality and the distinct mixed-cubic resonance

\[
\langle B_rB_sB_t\rangle=
-2\ \text{if }r+s=t,r=1;\qquad
-4\ \text{if }r+s=t,r\ge2;\qquad 0\ \text{otherwise}.
\]

The three frozen fields suggest, but do not prove,

\[
\langle B_2\rangle_q\stackrel{?}{=}
-\frac{(q-1)(q^5+q^2-q+1)}{q^7}.
\]

This is a useful secondary target because Newton identities reduce it to one
explicit fourth-degree coefficient-moment calculation. It must be proved by a
family trace calculation or refuted with a non-heavy method; further brute
force on this machine is not the proposed route.

The representation-theoretic search space is now better typed. In the raw
coefficient-square span `(e_1^2,e_2^2,e_1e_3)`, the entire integer null lattice
is

\[
\mathbb Z(2,-1,0)+\mathbb Z(-1,0,1),
\]

and the second generator is only the reciprocity relation
`e_1e_3-e_1^2=0`. Thus `B` is the unique primitive direction in that quotient
and the only noncentral survivor in three declared low-weight boxes. This
justifies prioritizing its arithmetic odd moments.

It does **not** justify a global uniqueness claim. Exact residue support proves
that

\[
B\,\mathbb Z[u^2+v^2,u^2v^2],
\qquad u=x_1^2+x_1^{-2},\quad v=x_2^2+x_2^{-2},
\]

is an infinite module of symmetric virtual-character laws, and the center-odd
graded sector supplies another mechanism. A later detector search should
therefore quotient tautological relations and central parity first, then ask
for arithmetic bias on a finite set of primitive residue-module generators.
Blindly enlarging a coefficient box would mostly rediscover these exact
compact-group symmetries.

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
stabilizer orders `1,2,1`. An unweighted orbit-representative average would
erase exactly the multiplicities that matter most.

Quantitatively, each single minimum orbit contributes more than half of the
frozen twelfth moment (`58.3993%`, `61.9548%`, `73.4068%`). A useful tail lemma
should therefore separate the extreme orbit/automorphism strata before
applying generic monodromy estimates to the bulk.

The symplectic trace discriminant `(x_1-x_2)^2` on the three minimum orbits is
exactly `4/3,0,5/7`. Their Frobenius types are nevertheless split nonisotypic,
repeated isotypic, and `F_7`-simple with real trace field `Q(sqrt(5))`.
Moreover the realized repeated-angle atom at `q=7` supplies only `2.39209%` of
the twelfth absolute moment, versus `73.40684%` from the simple minimum. A tail
lemma must isolate the nonregular collision wall before using regular
semisimple estimates, but it must also control simple off-wall classes rather
than treating automorphisms or repeated angles as the entire tail.

The deepest admissible integral coefficient pairs in the `USp(4)` region have
`K=-117,-356,-821` at `q=3,5,7`, and none is realized in the marked quintic
supports. This nominates a separate realization theorem near
`Delta=Gamma=0`: classify which split nonisotypic, split isotypic, and simple
real-quadratic Weil classes contain Jacobians with a rational marked
Weierstrass point.

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

### Symmetric-cube recognition target: separate compact image from arithmetic origin

The elliptic symmetric-cube packet supplies a necessary compact coefficient
identity

\[
F(x,y)=-x^4+x^2y+x^2+y^3-2y^2=0
\]

and a generic inverse `t_0=x(y-1)/(x^2-y)`. This is not sufficient for
arithmetic origin over `F_q`: the node `(0,0)` would require `t^2=2q`, which
has no integral solution for odd `q`. A useful local recognition theorem
should classify the integral points on the scaled curve subject to the Hasse
bound and determine exactly which arise from elliptic traces. It must treat
the three nodal fibers separately.

The bounded cross-family test is now complete. Among 251 frozen genus-two
coefficient atoms, exactly 7 lie on the curve: 4 independently
source-witnessed shapes carrying 53 members and 3 `(0,0)` ghost atoms carrying
398 members. The exact odd-prime candidate lemma leaves only `t=0` for
`p>=5`, and \(t=0,\pm3\) for `p=3`. The next theorem target is the corresponding
classification for every odd prime power, including the valuation conditions
for `q|t^3`, the three nodal fibers, and a proof of which candidate shapes can
occur in the marked genus-two family. It must keep coefficient-shape
intersection separate from equality of differently weighted local factors.

On the statistical side, prove effective versions of the exact stack laws for
geometrically linked elliptic subfamilies. The thin compact targets
`E(x^4)=4`, `E(y^3)=5`, and `E(x^2y^2)=7` already differ from generic `USp(4)`
at `3,4,5`; the first `Theta_12` multiplicities identify which lower-order
cohomological terms a proof must preserve.

### Symmetric-fourth recognition target: arithmetic on the principal `SO(3)` slice

The elliptic symmetric-fourth factor occupies

\[
d^2+yd-y^2-y^3=0,
\qquad y=w^2+w-1,\quad d=wy,\quad w=t^2/q-2.
\]

The node `(0,0)` has no rational arithmetic preimage because it would force
`w^2+w-1=0`. The first remaining recognition problem is therefore not node
incidence but a classification of rational and integral points on the smooth
arithmetic image, together with the minimum coefficient data needed to
recover `t^2`. In particular, trace alone can alias distinct elliptic traces,
whereas the second coefficient can resolve at least the first explicit
aliases. A useful theorem should decide this recovery problem uniformly in
odd `q`, then compare the resulting thin `SO(3)` family with the primitive
genus-two `SO(5)` factor without identifying their monodromy or motives.

### Symmetric-power alias target: lift scalar recovery to full local factors

The scalar problem now has a sharp answer for every odd `q`:

\[
\begin{array}{c|c}
m\bmod6 & \text{integral recovery from }\operatorname{Tr}(\operatorname{Sym}^m)\\
\hline
1,3 & t\text{ exactly}\\
2 & t\text{ up to sign}\\
4,5,0 & \text{uniform recovery fails.}
\end{array}
\]

The minimum initial coefficient problem is now solved completely for `m=5`,
over `Q` and every fixed `q!=0`: `(E_5,c_2)` leaves only the sign fibers
`t^2=q,3q`, while `(E_5,c_2,c_3)` removes the first and is equivalent to
equality of the full reciprocal factor. The positive-rank general collision
curve is therefore invisible only to the first scalar coefficient, not to
the first two.

The complete-factor part of the uniform `m` theorem is now solved.  For every
`m>=1` and fixed rational `q!=0`, equality of the full factors forces
`x^2=y^2`.  Even `m` is always invariant under the central sign.  For odd
`m`, the only rational nontrivial sign strata are

\[
 x^2=2q,\quad4\mid m+1,
 \qquad\text{and}\qquad
 x^2=3q,\quad6\mid m+1.
\]

On an odd-prime-power integral trace lattice, the second is the only nonzero
case and is exactly `m=5 mod 6`, `q=3^(2k+1)`,
`t=+/-3^(k+1)`.  The proof uses the quotient group intrinsic to the complete
root multiset and a multiplicity-sensitive consecutive-residue lemma, rather
than extrapolation from `m=5`.

The algebraic boundary is also exact for odd root order.  If `zeta` is
primitive of odd order `N`, the complete spectra attached to `zeta` and
`zeta^a` agree precisely when `a=+/-1 mod N` or
`m=-2,-1,0 mod N`.  At the exceptional powers every primitive class shares
one of the three universal cyclotomic factors.  This is vacuous at `N=3` and
gives genuine non-sign aliases for every odd `N>=5`.

The next uniform recovery target is therefore finer: determine, as a
function of `m`, the least initial coefficient prefix that already recovers
the rational trace up to these unavoidable full-factor aliases.  In parallel,
extend the cyclotomic stabilizer analysis to even root order and then to
traces over a fixed number field `K`, where the available torsion orders are
constrained by `[K:Q]`.  Any theorem must distinguish a local algebraic trace
from an elliptic trace and a compatible global family.

The `m=5` collision curve is now understood at the rational level:

\[
z^2=x^4+5x^3y+9x^2y^2+5xy^3+y^4.
\]

It is birational to

\[
\mathcal E:\quad Y^2=X^3-6X+5,
\]

and the explicit point `Q=(-2,3)` is nontorsion. Multiples `2Q`, `3Q`,
and `7Q` produce three rigorously certified prime-field collisions; a
complete Hasse-lattice census through `q=2000` finds no other primitive
general orbit in that range. Waterhouse realizes the three base-prime trace
pairs by ordinary elliptic curves, but rules out their nontrivially scaled
odd-exponent towers as elliptic traces.

The next theorem target is therefore an `S`-integral/descent analysis of the
rational maps from `\mathcal E` to `(x,y,z,q)`. Determine the Mordell--Weil
group, classify primitive integral collision rays, and isolate the terms for
which `q` is a prime power. Infinitude of rational points is already proved;
infinitude of integral points, primitive prime values, or globally compatible
elliptic families is not. The prime-power condition and Waterhouse
realizability must remain separate filters.

### Plethysm-ladder target: propagate coefficient maps beyond `Sym^3`

The first nontrivial square now closes exactly:

\[
 \bigwedge^2\operatorname{Sym}^3V
 =(\det V)^3\oplus(\operatorname{Sym}^4V\otimes\det V),
 \qquad R_{q^3}(T)=P_{\operatorname{Sym}^4}(qT),
\]

and its normalized curve map satisfies
`F_4(y-1,x^2-y)=-F_3(x,y)`. The next target is the full odd ladder

\[
 \bigwedge^2\operatorname{Sym}^mV
 \simeq
 \bigoplus_{\substack{1\le i\le m\\ i\text{ odd}}}
 \operatorname{Sym}^{2m-2i}V\otimes(\det V)^i.
\]

For `m=5`, the first two rungs now give
`c_2=qE_8+q^3E_4+q^5` and
`-c_3=q^3E_9+q^5E_5+q^6E_3`, with all 15 and 20 weights checked directly.
The next step is to derive the full normalized coefficient maps of the
primitive summands for general odd `m`, their discriminant and singular loci,
and their pullbacks to the existing locked coefficient supports. The theorem
must separate representation-theoretic identities from arithmetic
realization: matching a transformed local polynomial or coefficient point
does not by itself identify motives, compatible systems, or global Euler
products.

### Elliptic-pair target: detect geometry inside the `SO(4)` product law

For independent elliptic-form factors, the normalized tensor coefficients are

\[
x=uv,\qquad y=u^2+v^2-2.
\]

The exact compact image is the two-dimensional `SO(4)` region obtained by
reconstructing `p=u^2,r=v^2\in[0,4]`. Its reciprocal-quartic discriminant
splits into two mechanisms:

\[
\operatorname{Disc}_Z(P)
=\bigl((y+2)^2-4x^2\bigr)
 \bigl(x^2-4(y-2)\bigr)^2
=(p-r)^2(p-4)^2(r-4)^2.
\]

The independent product law is now exact, including all-odd-prime-power low
moments and locked fold/endpoint masses. Its intersection with the elliptic
`Sym^3` curve is also exact: four signed doubling graphs, no integral points
at nonsquare odd prime powers, and `16p^floor(k/2)-4` Hasse points at
`q=p^(2k)`. Waterhouse collapses simultaneous elliptic realization to the
repeated-root endpoint, unit, and zero-endpoint strata; the remaining square-
field points are explicit arithmetic ghosts.

The next arithmetic target is therefore to replace independent draws by
geometrically linked elliptic pairs: isogenous curves, quadratic twists,
shared covers, or fibers in one surface. Compute the first failure of product
moment factorization and determine whether any family can enforce one signed
doubling graph coherently across primes. A one-place spectral dilation or
Waterhouse existence result is not such a correspondence.

Trace moments alone are provably lossy here: standard `SO(4)` and
`Sym^3(SU(2))` agree through order four and first split at order six
(`25` versus `34`). A useful recognition theorem should combine the
two-dimensional coefficient region, at least the sixth trace moment, and
cross-prime compatibility. It must not infer an isogeny or twist from
`A=\pm B` at one field.

### Adjacent higher-variety target: distinguish tensor lifts inside `SO(8)`

For independent genus-one and genus-two factors, the primitive weight-two
local system

\[
H^1(E)\otimes H^1(C)
\]

has compact tensor image `(USp(2) x USp(4))/diag(-I,-I)` in `SO(8)`. If
`u,v,w,h` are its first four normalized coefficients, every member obeys the
proved hypersurface equation

\[
\boxed{u^2h-u^4+2u^2v+u^2-2uw-w^2=0.}
\]

The first compact-group trace fingerprint is

\[
\mathbb E_{\rm product}(\operatorname{Tr}^4)=6,
\qquad
\mathbb E_{SO(8)}(\operatorname{Tr}^4)=3,
\]

and the same representation degree gives
`(E(h),E(uw))=(1,1)` on the product image versus `(0,0)` on generic `SO(8)`.
The independent marked-model family already has exact all-`q` first
corrections for `v`, `h`, and `uw` from the locked marginal theorems.

This creates three precise next steps that require no undirected large scan:

1. prove all-`q` variances and covariance for `h-1` and `uw-1`, then identify
   their first automorphic character channels;
2. test the hypersurface defect on an independently sourced orthogonal family
   as a certificate against hidden tensor-lift monodromy; and
3. replace the independent Cartesian family by geometrically linked pairs
   `(E,C)` sharing a cover, isogeny, or correspondence, and measure the first
   failure of marginal moment factorization.

The sign bridge `A=-t_E` from the genus-one trace fixture is source-locked, and
the declared measure is the product of ordered marked-model/curve-stack laws.
No uniform coarse product-variety law or generic `SO(8)` equidistribution is
being inferred.

### Exterior-square target: compensate a universal moving local eigenline

For the primitive five-dimensional factor

\[
R(T)=1+(q-b)T+q(a^2-b)T^2-q^2(a^2-b)T^3+q^3(b-q)T^4-q^5T^5,
\]

every good local polynomial has the exact divisor `(1-qT)`. On an individual
finite-field fiber this is a genuine Frobenius-stable line. The ambient
`SO(5)` standard representation has no common invariant vector, but the actual
family monodromy is unproved and may be smaller; an endoscopic splitting
visibly contributes an anti-diagonal second Tate line to the primitive factor.
The first theorem target is therefore to determine the family-wide and
cross-prime status of

\[
Q_{\rm local}(T)=R(T)/(1-qT).
\]

One should prove one of the following sharply separated outcomes:

1. the quartics form an independently natural compatible or automorphic
   system, with the required bad-factor and analytic data; or
2. they do not, and the formal zeta factor extracted from good Euler factors
   is globally compensated by an explicit zero or failure of compatibility.

The adjacent finite-family target is the orientation moment. With
`s=b/q-1`, exact `SO(5)` Haar measure gives

\[
E_{SO(5)}(s^5)=1,
\]

whereas all three frozen family means are negative. Evaluate `E_q(s^5)` for
all odd `q`, or obtain a power-saving comparison with the `SO(5)` target, and
identify the cohomological channel carrying the volume-tensor invariant. The
three signs alone are not an asymptotic conjecture.

### Integral-factor target: count the `+q` elliptic-form locus for all `q`

The exact finite predicate is

\[
\Delta=a^2-4b+8q=d^2,\qquad d\equiv a\pmod2,
\]

equivalently
`P(T)=(1-rT+qT^2)(1-sT+qT^2)` with integral `r,s`. Determine its
member-weighted and stack-weighted multiplicities in the monic squarefree
quintic family for every odd prime power, separating repeated from distinct
factors. The frozen fractions `1/6,141/500,85/343` are census values only and
must not be interpolated.

A second stage may import Honda--Tate/Tate and polarization theorems explicitly
to ask which polynomial rows give product isogeny classes and which principal
polarizations occur on Jacobians. The complement of the displayed predicate
must not be renamed “irreducible over `Z`,” and ground-field failure must not be
renamed geometric simplicity.

### Tensor-singular target: explain arithmetic incidence with the pinch line

The containing tensor coefficient hypersurface has normal form

\[
r^2=u^2\lambda,\qquad r=u+w,\quad
\lambda=h+2v+2-u^2,
\]

and transverse rank-drop pullback

\[
(A=0,b=2q)\ \cup\ (a=0,b=2q-A^2).
\]

The coefficient mechanism is now exact:

\[
q^2(h+2v+2)=(A^2+b-2q)^2+(Aa)^2.
\]

Thus real/integer rank drop is precisely the displayed union, both branches
lie in the integral `+q` split locus, and the converse is explicitly false.
Scheme-theoretically the pullback `(Aa,R^2)` doubles the transverse direction;
only its reduced arithmetic support is being called split. The bounded census
counts all incidences exactly but does not explain their arithmetic geometry.
A useful next theorem should compute their all-`q`
model/stack masses, their first character moments, and their intersection,
then determine—using explicitly imported arithmetic geometry—which strata
correspond to extra endomorphisms, supersingularity, or accidental trace-zero
without conflating the singularity of a containing coefficient hypersurface
with a singular source variety—or asserting that this hypersurface equals the
full coefficient image.

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
