# Root mathematical review of the new component proofs

**Outcome: PASS within the exact stated component scopes and named analytic premises.** This report records the root agent's independent reconstruction of the companion proofs authored by other agents. The root authored the moving-mask, original A2 and stratified two-scalar A2 notes, so its checks of those notes are not described as independent review. Separate agents review each of them; the new combined theorem has two scoped manuscript reviewers, with their development contributions disclosed.

This is an internal mathematical audit. It is not external peer review, formal verification, or a new proof of the whole imported canonical theorem. The proof files retain their source-qualified status.

## 1. Frozen targets

| File | Reviewed SHA-256 |
|---|---|
| SIGNED_AUXILIARY_REUNION.md | 6b8277e64adb1121704fbf7dc4553aeda31b598c65e0279d80316a35d66d38bf |
| HIGHER_CUBIC_POOLS.md | 622cf846a961aed28ac0363f91766045f328c99700931621f123c17347c6bc23 |
| HYBRID_CUBE_INVERSE.md | d4c5dad1b5c719043ac7118c5f468b3d5c398e2bbd5c4470a1983f64139f066a |
| ALL_ROW_SPECTRAL_MEAN.md | 204e448b92e4a0d4087e0ccf8e99cb20fcfef26114a95622af2c47c965cdb651 |
| MIXED_CUBIC_REPLICATION.md | fb32d3a63704950be1d30228ec03a0ee1f157f23d1c7b24a8793886160fbb30b |
| SMALL_W_CORE_AUDIT.md | c0d07ccc7ed2fc1490a631c73db47044df256b7ca6f946ecacd5c735e457f9d9 |
| SMALL_W_POSITIVE_CUTOFFS.md | 52a4d27a5f518feabfb8ecb6c87eee5172a6ce3f2cf6a5aa5630c00ff9346461 |

The final signed proof includes a one-sentence endpoint qualification found by its other reviewer: the strict comparison between its two smooth-block alternatives requires beta<1. At beta=1 the alternatives coincide. The formulas and hypotheses did not change. The final hybrid proof explicitly includes fixed smooth two-variable tests and uses the separately proved moving-mask block. The final spectral proof directly applies that local adapter at outer scale one with counting. Those changes were read before this review was frozen.

## 2. Exact signed reunion and second Poisson

I reconstructed the changes of variables from the pinned PR #914 formula before taking any absolute value. A nonzero coefficient forces b,f,d,z1,z2 to be pairwise coprime, with m_i=d z_i and d=(m1,m2). It does not force the original row to avoid f. The two original row symbols impose (k,d)=1. The Gauss CRT contributes the fourth-power d phases, which combine with f to give the invariant w=fd. Every divisor f of w has a valid inverse reconstruction.

The remaining divisor dependence is exactly
\[
\sum_{f\mid w}\mu(f)\mathbf1_{(k,w/f)=1}
=\prod_{p\mid w}(\mathbf1_{p\nmid k}-1)
=\mu(w)\mathbf1_{w\mid k}.
\]
Consequently k=wh and the character phase is the fifth power in w. A new coprimality condition on h and w would remove valid repeated-row terms. The product weights depend only on bwz_i, so the identity retains the full original coupled smoothing.

The radial norm scale before the second Poisson is T=Nw N(z1z2)/H. The primitive character is chi_z1 times the conjugate of chi_z2. Its conductor is exactly z1z2 because the columns are disjoint and the local powers one and five are nonprincipal at every conductor prime. Excluding the unit pair is therefore precisely what removes the zero row on both sides. The Poisson factor Nw sqrt(N(z1z2))/H cancels the preceding H/(L Nw sqrt(N(z1z2))). The final prefactor is 1/L, and the row test is Phi(Nw Nr/H).

I checked the finite-ray cancellation against the source arithmetic identities. The first column combines a_xi(z1) with gamma_1(z1); the second combines its conjugate with gamma_-1(z2), including chi_z2(-1). The CRT reciprocity bicharacter and that sign are required by the quotient identity. The product is the actual finite-ray G(z1 z2^-1), with no angular factor remaining. Expanding this fixed function uses finitely many fixed characters, not a growing ray group.

For the quantitative tail I independently obtained the k-by-k allocation of g=bw and the 2k residual singleton scales. Their product on each side is L/Ng. The pointwise tensor correction is
\[
(1-\textstyle\sum_i t_i)/\prod_i(1-t_i),
\]
whose nonconstant coefficient is 1 minus support size and whose absolute local error is O((Np)^(-2 beta)). The stated beta>1/2 gives convergence. This preserves the native coefficients and moving exclusions. Counting the selected all-row Schwartz sum gives H/Nw, including stronger decay when Nw>H. The remaining ideal sums are
\[
H L^{2\beta-1}\sum_b(Nb)^{-2\beta}
\sum_{Nw\ge R}(Nw)^{-2\beta-1},
\]
and give the claimed R^(-2 beta). The sharp cutoff is on the frozen invariant w; no sharp inverse-sum estimate is used. Arbitrarily large row annuli are handled by enlarging the reference parameter and retaining Schwartz decay.

The proof therefore establishes the stated signed component tail for the actual smooth convolution. It does not establish the leading b=w=1 contribution or transfer the native second moment to a shorter row range with an unproved moving twist.

## 3. Physical higher cubic norms and mixed coprimality

The primary squarefree cubic sieve was read in Blomer–Goldmakher–Louvel, arXiv:1112.1650v1, Theorem 1.3. The root independently fetched the pinned #917 all-row proof and checked the representation u=epsilon v^3 a b^2. The fixed cube factor contributes its literal column mask. Freezing v and the smaller of a,b, then using the larger component as the squarefree row, gives the three all-row terms H, H^(1/3)L and (HL)^(2/3). Every unit and bad-prime component is accounted for. No squarefree-row theorem was used on arbitrary rows without this argument.

For a physical product of cubic polynomials, repeated incidence ideals are frozen before the remaining squarefree singleton product is grouped into the column of that sieve. The grouped coefficient has squared mass O(D^epsilon R(c)) by a fixed-order divisor bound and the actual tuple count. The three norm powers are R(c)^(1/2), R(c), and R(c)^(5/6). Pair repetitions are harmonic in the first term; every other correction sum is convergent. This proves the product lemma for a fixed number of physical copies and therefore the stated integer higher norms.

The pair ideals have prime sign +1, whereas singleton inverse ideals have sign -1. I independently expanded
\[
\frac{1+\sum_j s_j z_j}{\prod_j(1+s_j z_j)}.
\]
The nonconstant coefficient is (1-|supp e|) product_j(-s_j)^(e_j). A one-axis term vanishes outside the moving mask. At critical norm weights 1/2 the proof correctly regularizes only a finite supported horizon by adding a small positive weight; it does not claim convergence of the unregularized infinite Euler product.

The exact coupled tests can be Mellin separated after fixed singleton cutoffs are inserted. Hard pair dyads require only sup norms in the classical cubic estimate; singleton inverse tests remain smooth with uniform finite seminorms. Each shortened correction scale receives the same fixed character, sign, and zero mask before its norm is estimated.

For the hybrid, the selected native factor uses p=2q/(q-1). Its scale exponent is 1/2+(2b-1)/(2q). The cubic product uses 2q, giving reciprocal-exponent sum 1/2. Every correction weight is at least 1/2, including each separate monomial from the cubic norm. Normalization by R^2 X T=D^k gives the stated rho_q formula. The integer q is fixed independently of D.

I recomputed the complete triangle bounds at h=21/20, r=5/24 and b=7/8. The excesses are 181/240 for q=1 and 119/160 for q=2. The latter improves the same complete #923 triangle by 35/288. At counting, the diagonal cutoff is 23/60 rather than 33/80. The root fetched #923's exact source and checked that this is the same polynomial portion and normalization.

The higher-ideal norm sum converges because |I|/2>1 for |I|>=3; the number of pair dyads has a fixed logarithmic power. This validates the complete peripheral selector. The separate Hermitian statement spends one full native L2 norm, one interpolated native norm, and a cubic norm; its Holder reciprocals sum to one. It does not promote a positive side norm to an absolute estimate for an arbitrary signed subset.

## 4. Smooth hybrid inverse and its all-row tail

I compared the three short-block monomials with the frozen #921 CUBE_INVERSE and ARBITRARY_ROW_MOMENTS factorization. Keeping both inverse scalar sums gives the exact powers G^(2 beta-2) Z^(2 beta-2) before the block is optimized. The support G^2 Z^3≪B is imposed on the complete reunited sum first. The smooth extra cutoff in Z has uniformly rescaled derivatives through the common-divisor changes of variables.

The three balanced short terms are consequently
\[
HD,\quad JH^2D^{\beta-1/2}R^{5/2-\beta},\quad
KH^{4/3}D^{2/3}R^{2\beta}.
\]
The common-divisor norm costs are d1^(-beta-1/2), d2^(-beta-1/2), and ell^(-2 beta), all summable. The remaining positive variable is allowed to meet ell.

For the long part, expanding the physical cube and grouping d=hb gives a single divisor-bounded coefficient c_R(d). The outer condition is (a,d)=1; the squarefree n may meet d. The character at a repeated d prime retains its nonunit zero. The moving auxiliary and original exclusion are row-independent bounded factors inside the squarefree product coefficient used by the classical sieve. Thus the long estimate has no J,K penalty. Its norm weights are d^-1 for the H term, d^-5/2 and d^-2 for the two length terms, yielding the stated harmonic loss and R^-3,R^-2 energy tails.

The general ordered-axis formulas follow by using G<=sqrt(M) Z^-3/2, even if this is weaker than the outer-axis bound. Swapping axes transposes the fixed test without changing the raw polynomial. The final two-variable Mellin argument and fixed-R row-profile passage cover the child tests and row domains required by the root A2 theorem.

The root separately reconstructed the exponent optimization and reproduced the exact diagnostic. At beta=11/12, H=sqrt(D), the balance gives R=D^(8/55) and energy D^(1087/660+epsilon). The D^2 range is H<=D^(342/451)J^(-216/451) with K<=J^(2/3). These are bounds for the literal normalized polynomial. They do not control its original long signed covariance.

## 5. All-row canonical spectral mean

I read the actual imported Proposition R. It states the completed mean for all nonzero element rows with independently polynomially bounded H,X,Nf. The separate later cube-reduction lemma has a Sigma condition; that condition is not imposed on Proposition R. The spectral proof therefore uses the source proposition on its stated domain.

The completed block is normalized by X^-1/2 and its cube summand has amplitude sqrt(Nb). Freezing b produces the normalized squarefree block at X/(Nb)^3 with exterior weight 1/Nb. The all-row classical bound sums with harmonic or convergent weights and gives H+H^(1/6)X+(HX)^(2/3). The fixed auxiliary is a bounded coefficient in this use of the sieve.

Mellin reconstruction uses X^(1/2-u), so the cube Dirichlet exponent is exactly 3u-1/2. The completed dyadic series converges normally on every compact subset of Re(u)>1/2 at a fixed finite row set. The cube reciprocal is absolutely convergent there, uniformly in the omitted primes. Thus dividing by it needs no new zero-free input.

I recomputed both crossovers. The all-row linear-column term meets the completed bound at X=H^(11/12)F^(1/2), with norm cost H^(1-11a/12)F^((1-a)/2). This is below the desired H^(1/2)F^((1-a)/2) when a>6/11. The cubic cross term has crossover H^(4/5)F^(3/5) and requires a>5/8. The latter remains dominant. Uniformity across a=5/6 is handled with a logarithm rather than a singular constant.

For the new original-column exclusion, the final proof invokes the independently reviewed moving-mask adapter at outer scale one and beta=1. Only the primary unit ideal is selected, giving the literal one-variable completion and its cube mask. The third energy term is absorbed by H+H^2J0/X using K0<=J0^(2/3). The exact multiplier is J0=Nd N(q0/(q0,d)). Hence the spectral corollary is an actual composition with the local adapter, retaining the named theta inputs but no added angular reciprocal assumption.

This proves the advertised canonical-family mean and its row/exclusion extension. It does not identify every coefficient of the separate arbitrary-row full-cusp reflected series or improve the 5/8 sufficient threshold.

## 6. Evidence and retained boundary

The finite diagnostics identified in VALIDATION.md were reproduced from their executable sources under ordinary and optimized Python. Their scopes are stated in VALIDATION.md. Genuine small split-prime Eisenstein symbols occur in the mask and triangle diagnostics. The signed-reunion Gauss factors are formal CRT-compatible cyclotomic data, not numerically evaluated primitive Gauss sums. Exact rational balances are diagnostics of the written continuous arguments, not sampled substitutes for them.

No new analytic claim is inferred from those finite tests. The imported canonical proof was not rebuilt; the native-M2, finite-order pointwise, angular scalar, theta and classical-sieve dependencies remain exactly those named in the proof being used. No full fourth moment, cofinal hierarchy, new zeta zero-free boundary, or RH conclusion passes this review.


## 7. Mixed integer cubic replications

I read the entire frozen addendum, including its general cyclic theorem,
unequal shortened scales, comparison class, Hermitian formula and weighted
row extension. The identity underlying the additional rational exponent is
literal: with three degree-five exponent vectors (1,2,2), (2,1,2), (2,2,1),
the product of the physical monomials is the fifth power of the original
three-factor product. Hölder therefore gives its L^(10/3) norm from the
three ordinary L2 norms. All monomials have a fixed integer number of
actual factors, so the parent classical cubic-product lemma applies.

For s cyclic products of common total degree d, every original pair axis
has total replication degree d. If the t-th physical cubic norm term has
length weight alpha_t in {1/2,1,5/6}, the exact correction weight on pair
axis j is sum_t m_(j+t) alpha_t/d, at least 1/2. This is true before any
original equal-scale specialization. The selected native singleton has
weight 1/2+(2 beta-1)s/(2d), and all other singletons have weight beta.
Consequently the mixed mu/mu-squared correction is legitimate for each of
the finitely many norm monomials, including moving excluded primes and
literal nonunit zeros. No fractional physical inverse power is introduced.

At s=3,d=5, the native factor uses L5 and contributes height exponent1/5
and singleton weight29/40 when beta=7/8. I recomputed all27 combinations
and their81 pair weights using the supplied exact producer. The maximum
excess is863/1200, with the all-cross-term cubic choice. The normalized
formula independently gives21/16−7/40−251/600=863/1200. Its savings are
59/2400 over119/160 and263/1800 over623/720.

I also independently derived the restricted comparison in Section5.
Let t_e be the Hölder weight of a degree-n integer physical monomial.
At equal original pair and singleton scales, the complete power cost is
7/8+sum_e t_e(7/16+delta_n), where delta_n is the physical rho exponent.
The pair budgets give sum_e n t_e<=3. Hence the cost is the stated convex
combination of E_n and the counting remainder7/8. The piecewise E_n has
its integer minimum at n=5. This proves optimality only within that
explicit direct-monomial Hölder class. It does not certify the formal
real-q value23/32 or exclude other analytic arguments.

The Hermitian exponents sum to one, and its correction weights retain
at least1/2 on every varying axis. The squared height exponent in the
Schwartz expansion is at most one. Both extensions therefore have the
claimed scope. The leading all-singleton core remains unchanged.

## 8. Final native reconstruction and cutoff-qualified method diagnosis

I checked the final change of variables g=bw,s=wr against the frozen signed
formula. For fixed g,s all primitive coefficients, fixed-ray phases,
column exclusions and the profile Phi(Ns/H) are independent of the chosen
divisor w. The complete sum over w gives 1_((s,g)=1). This statement would
fail for a truncated w sum, and the proof correctly does not make it there.
Expanding the fixed finite G and writing n1=gz1,n2=gz2 reconstructs the
product-column native energy with B_(nu,v) carrying conjugate(nu). Equality
of product columns is exactly the primitive unit pair. The subtraction is
the full displayed Delta_v, including its original row mask and the factor
G(1) after the finite Fourier sum. There is no positivity assumption on
its scalar Fourier coefficients or on Phi.

The additional adapter keeps the ambient row height H after s=wr. The two
largest original singleton axes have product at least Z^(2/k), up to fixed
support constants. Native M2 and row Cauchy on those two, pointwise on the
others, yield H Z^(1+(2 beta-1)(1-1/k)) before counting b,w and dividing
by L. The count is O(BW), and BW=L/Z, so the displayed normalized power is
H Z^((2 beta-1)(1-1/k)). Its shifted correction uses two weights1/2 and
remaining weights beta; selecting the axes before their shifts is crucial.
This does not assert M2 for a first-power twist at height H/Nw.

The old hybrid audit is explicitly restricted to its pinned R,T>=1
inequalities. The later positive-cutoff addendum now includes all R>0 and
the actual empty-short thresholds. I verified its elementary optimization:
inf_R max{A R^p,R^-3}=A^(3/(p+3)). At the balanced residual scales its A
is D² Z^(7/4+kappa/2)/H². On nonempty dual support it is at least a fixed
multiple of D² H^(-9/8+kappa/4), which has a positive D exponent for the
specified1<h<2 and kappa>1/2. At kappa11/12, the new power is36/55.

This is a diagnosis of the displayed positive envelopes only. The final
addendum explicitly allows exact pruning of empty short strata and does
not infer a lower bound for arithmetic energy. Its independent classical
benchmark at b=w=1 gives exponents2,(5h+4)/6,2+h/3 after the exact outer
normalization; the last is largest for1<h<2 and exceeds the target h.
The bounded-dual-height large-b endpoints are explicitly outside that
failure claim. These qualifications are necessary and are present in the
final reviewed hash.

## 9. New adjacent source and authorship boundary

During this pass PR #924 appeared at725b2d25ab47e57500049d93985560098c7ef3fa.
Its exact sixth-power stratification and full-A2 length-adapted source
were read and pinned. The root combined them with the existing two-scalar
block, using tau=(3−2 beta)/(5−2 beta) and a dilated smooth cutoff. The
resulting STRATIFIED_TWO_SCALAR_A2.md is root-authored and therefore relies
on the separate signed and higher agents' hash-bound reviews, not on a
self-described independent root review. Its89/55 result supersedes the
positive unstratified exponents in the earlier frozen proofs.

The preserved5/8 spectral baseline likewise is not advertised as the
latest threshold: PR #924 separately derives4/7 using the newly credited
de Faveri external large sieve. That primary statement and the adjacent
adapter were read. The new stratified89/55 result does not require that
additional external theorem.
