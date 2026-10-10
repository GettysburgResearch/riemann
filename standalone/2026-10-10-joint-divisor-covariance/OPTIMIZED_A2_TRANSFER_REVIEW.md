# Independent review of the optimized mixed A2 transfer

**Reviewer:** /root/moving_auxiliary_attack.

**Reviewed object:** the complete root-authored
OPTIMIZED_A2_TRANSFER.md, 14,739 bytes, SHA-256
d5a87c27959b64e62df7dd3aa2fdd33cc8b42af6e5a64e9bfb20d6b74af0277a.

**Verdict:** pass at the stated conditional scope. The proof transfers
the mixed raw short/long cube envelope to the full arithmetic A2
completion with all nonzero rows and the displayed moving auxiliary
costs. The correction-dependent cutoff produces absolutely convergent
norm sums. The stated numerical row-height ranges follow from the
displayed monomial envelope. No signed centered covariance, full fourth
moment, new zero-free boundary, generalized moment hierarchy, or RH
claim is justified by this review.

**Independence boundary:** I did not author the reviewed proof. I did
author its companion MOVING_AUXILIARY_ADAPTER.md, which supplies the
mixed completed theorem and exact child parameters. In this review I
treat that companion's theorem as a stated input and check its use,
rather than present this as an independent approval of my own theorem.
The companion requires a different review. The imported theta and
angular foundations are also assumptions here, not newly reconstructed
or formally certified by this report.

## 1. Sources and review procedure

I read the whole reviewed proof, PR #918's exact mixed completion and
cube inverse at commit cfa102748b26f840ccc4b963a660711424db0ec3,
standalone/2026-10-10-sextic-joint-core/INTERFACE_COMPARISON.md,
and the all-row raw short/long estimate in PR #923 at
1a1152008706f7e24fa1efe4990588f8f99c5d8d,
standalone/2026-10-10-sextic-separated-cores/ALL_ROW_COMPLETION_AND_RAW_GAIN.md,
Section 6. I also read the proof of the refined all-row sieve,
PR #913 at 6498d6cc2eded03159c7332b25fd224ad07f89c1,
standalone/2026-10-10-sextic-moment-descent/REFINED_ALL_ROW_SIEVE.md,
Theorem 3.4 and its preceding lemmas.

I reconstructed the two exact finite regroupings, every normalization
and mask in the long tail, both orientation inequalities for arbitrary
rectangles, the five correction-label norm exponents, the range of
alternative cutoff exponents, and the two explicit rational regimes.
A separate Python fractions.Fraction calculation reproduced the
five norm exponent pairs and checked all monomial comparisons at both
endpoints of each regime. Because their differences are affine in
\(h=\log_D H\), those exact endpoint comparisons check the stated whole
intervals of the finite exponent optimization.

That calculation is a rational algebra diagnostic only. It does not
compute primitive Gauss sums, replay the theta transformations, test a
global analytic bound, or numerically verify the asymptotic conclusion.

Two presentation issues in the earlier draft were reported and repaired
before this review hash: the denominator of \(X_t\) now explicitly
contains \(E^2\), and the absorption of \(H\) into \(HX\) explicitly
includes nonempty child scales below one. The final bytes also passed
a scan for unintended control characters.

## 2. The mixed raw inverse, including cutoffs below one

The normalization in reviewed (2.1) is correct. On expanding the
completion at length \(B/(Nh)^3\), its further cube variable has weight
\(1/Nb\). Combining it with the inverse coefficient yields \(1/N(hb)\)
and the full multiplicative scalar
\(\lambda(hb)^3\chi_{hb}(k)^3\). No coprimality condition between
\(h\) and \(b\) is required or inserted.

The short part is bounded by weighted Cauchy with weights \(1/Nh\).
Substitution of \(B/(Nh)^3\) in the completed estimate, followed by
\(\min(A,\sqrt B/(Nh)^{3/2})\le\sqrt B/(Nh)^{3/2}\), gives the
\((Nh)^{7/4}\) and \((Nh)^2\) powers in the second and third monomials.
Summing those powers against \(1/Nh\) gives exactly \(U^{7/4}\) and
\(U^2\); the first term costs only reciprocal-norm logarithms.
No scalar Möbius estimate is applied to the sharp cutoff in \(h\).

When \(0<U<1\), the short sum is empty, because nonzero integral ideals
have norm at least one. The short inequality therefore remains valid.
For a cutoff beyond the full physical range, the long sum is empty
and the short estimate is still a legitimate, possibly wasteful, upper
bound. Thus the displayed raw theorem truly holds for every allowed
positive cutoff; it does not require a hidden lower bound of one.

The raw polynomial is symmetric under interchange of its two factors,
their tests, and their scales. The \(q\) mask applies to both factors and
the auxiliary character applies to their product. Choosing the shorter
axis first is therefore exact. The two identities in reviewed (2.4)
show that the non-height monomials are bounded by their product-scale
versions with \(X=\sqrt{AB}\). A fixed finite choice of test orientation
does not affect the uniform seminorm contract.

## 3. The long tail retains the moving masks and all rows

The combined cube index \(d=hb\) yields exactly

\[
c_U(d)=\sum_{\substack{h\mid d\\Nh>U}}\mu_K(h).
\]

Both outer masks, \((a,h)=1\) from inversion and \((a,b)=1\) from the
physical completion, combine to \((a,d)=1\). The physical and inverse
\(qf\) exclusions combine to \((d,qfS)=1\). The remaining squarefree
theta index is permitted to share primes with \(d\). These are the
masks stated in reviewed (2.5).

For \(U<1\), every divisor of \(d\) lies above the cutoff, so
\(c_U(d)=\mathbf1_{d=1}\) exactly. This is consistent with the full raw
family being the entire long part in that range. The identity is
finite: nonempty physical support bounds \(Nd\) by a fixed multiple
of \(B^{1/3}\). The divisor bound on \(c_U\) is consequently absorbed
into the same polynomial reference.

For a fixed \(d\), grouping the two squarefree coprime factors into
their squarefree product gives row-independent divisor-bounded
coefficients at norm \(AB/(Nd)^3\). Their squared mass, divided by that
column scale, is subpower. The \(q,f,d\) masks stay in those coefficients,
and the fixed auxiliary phase has modulus at most one. The all-row
sieve therefore gives reviewed (2.6), with the necessary repeated-row
term \(H^{1/6}AB/(Nd)^3\). Replacing this by a squarefree-row term would
not be justified; the reviewed proof does not do so.

The remaining row factor \(\chi_d(k)^3\) acts as a contraction, including
its zero at rows meeting \(d\). The two tail sums have exponents \(5/2\)
and \(2\), hence their square-root costs are \(U^{-3/2}\) and \(U^{-1}\).
They remain upper bounds for \(U<1\), where the right sides only grow.
The reciprocal-norm height sum is finite and logarithmic. For
nonempty child rectangles, the product scale has a fixed positive
lower bound, so \(H\) is bounded by a fixed multiple of \(HX\). This
proves the long estimate without an auxiliary conductor loss.

## 4. Each A2 child may use its own exact cube cutoff

The A2 correction in reviewed (3.3) has normalized magnitude

\[
\frac1{Nc\,Nd\,(Ne)^{3/2}},
\]

and its row phase has modulus at most one with all original zeros.
The child masks and auxiliary are \(q_t=qcde\), \(f_t=ef\). Since the
correction labels are disjoint from \(qf\), their exact overlap is
retained in

\[
\frac{q_t}{(q_t,f_t)}=\frac q{(q,f)}cd.
\]

Consequently the product scale and the two conductor costs update as

\[
X_t=\frac{X}{(Nc\,Nd)^{3/2}(Ne)^2},\quad
\ell_t=\ell\,Nc\,Nd\,Ne,\quad
m_t=m(Nc\,Nd)^{1/3}(Ne)^{2/3}.
\]

The choice \(U_t=U/(Nc\,Nd)^{1/2}\) is legitimate. Every child possesses
its own finite exact cube identity, and its short/long split can be
made at any positive real cutoff. No identity between different
children requires a common cutoff. Nonempty children and their
cutoffs satisfy the polynomial upper and reciprocal lower ceilings
required by the raw theorem. The separate shorter-axis orientation
does not alter any of these parameters.

Multiplying each square root of a child energy monomial by the
normalized correction magnitude gives the following denominator
exponents:

| Energy term | \(Nc\) and \(Nd\) | \(Ne\) |
|---|---:|---:|
| \(HX\) | \(7/4\) | \(5/2\) |
| \(\ell H^2X^{5/12}U^{7/4}\) | \(5/4\) | \(17/12\) |
| \(mH^{4/3}X^{2/3}U^2\) | \(11/6\) | \(11/6\) |
| \(H^{1/6}X^2U^{-3}\) | \(7/4\) | \(7/2\) |
| \(H^{2/3}X^{4/3}U^{-2}\) | \(3/2\) | \(17/6\) |

I recalculated every entry directly from the preceding child
parameters. Every exponent exceeds one, so the enlarged nonnegative
ideal sums converge absolutely. Coprimality is dropped only after
passing to those accounting sums. The actual correction identities
retain it. Using a smaller preliminary epsilon inside each uniform
child estimate and then squaring the convergent norm sum gives the
claimed final epsilon.

The explanation of the cutoff mechanism is also correct. A common
cutoff would leave \(13/16\) in the second row's first two columns.
For \(U_t=U/(Nc\,Nd)^\eta\), that exponent becomes
\(13/16+7\eta/8\), requiring \(\eta>3/14\). The two long terms require
\(\eta<1\). The other exponents impose no stronger restriction on the
stated open interval.

## 5. The explicit numerical regimes

For \(q=f=1\) and \(A=B=D\), the first cutoff
\(U=D^{4/15}H^{-7/30}\) balances the third and fourth monomials at
\(D^{6/5}H^{13/15}\). The second monomial becomes
\(D^{53/60}H^{191/120}\), and is bounded by that balance exactly when
\(h\le38/87\). The first and fifth terms are smaller throughout the
stated interval \(0\le h\le38/87\).

The second cutoff \(U=D^{1/3}H^{-22/57}\) balances the second and fourth
monomials at \(DH^{151/114}\). The third becomes
\(D^{4/3}H^{32/57}\), which is smaller exactly when \(h\ge38/87\).
The first and fifth are also smaller on the displayed interval.
This cutoff is at least one through \(h=19/22\); the proof correctly
uses that endpoint only for this particular convenient optimization,
not as a restriction on the underlying theorem.

The two envelopes coincide at their junction. Their diagonal-size
range extends to \(h=114/151\). At \(h=1/2\), the cutoff is \(D^{8/57}\)
and the energy exponent is \(379/228\). The difference from the old
classical exponent \(25/12\) is exactly \(8/19\). These are row-height
and positive-energy exponents; the reviewed proof does not confuse
them with a zero-free boundary.

## 6. Scope and smallest load-bearing risk

The genuinely new deduction checked here is the transfer to the full
arithmetic A2 family, through all its moving mixed children, with no
polynomial correction loss. The raw numerical optimization itself
was already present in PR #923.

The smallest analytic failure that would invalidate this transfer is
a failure of the companion mixed completed input for its stated
outer cube mask and moving \(q_t,f_t\), or a failure of its uniform
smooth-scale contract. Conditional on that input and the pinned
all-row sieve, the two finite identities and convergent norm sums
close the transfer. No analytic Weyl functional equation for the A2
series is needed or asserted.

The final boundary paragraph is accurate. Independently corrected
columns reconstruct their original product using \(s_t=c^3d^3e^4\);
the strict first-Poisson off-diagonal retains the comparison of those
reconstructed products and its full outer signed auxiliary sum. The
positive norm does not supply that centered estimate at dual height
\(D^{3-\theta}\). The full fourth moment and the cofinal generalized
moment conclusion remain open.
