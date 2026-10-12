# Scoped second review of the causal and Haar classification

**Status:** mathematical content review of the exact source bytes below.
The stated causal classification and probability-model theorems are
accepted at their written scopes. The generalized physical-row moment
and RH remain open.

**Reviewer:** the \(\texttt{/root/signed\_family\_attack}\) AI agent.
This is an AI review, not external human acceptance, integration, or a
proof-assistant certificate.

**Exact reviewed source:**

    standalone/2026-10-13-signed-moment-reassessment/CAUSAL_ORBITS_AND_DENSE_LIFTS.md
    bytes: 44355
    SHA-256: dc8f645731302f2e2059cd115cc70564409af98c08c48a3f30f7d081c917a817

The source was read in full at this hash. A later commit receipt may bind
these same bytes to a frozen mathematical commit. This review does not
authorize a change to those bytes without an updated review identity.

## 1. Independence and conceptual contribution

Two kinds of review occurred and must be distinguished.

1. The original Sections 1--6 and the necessity theorem now numbered
   7.1 were reconstructed independently, before the converse was added.
   The original source had SHA-256
   \(\texttt{c4e25ce7f42f9fc3f2949635a9f7c5cddcc3c38811c6dc74c0bf3e4ab88a87fb}\).
   The reviewer did not supply its causal-measure classification,
   induced-character argument, Kummer count, determinant mean, or
   mean-Mellin necessity proof.
2. During the later converse development, the reviewer independently
   suggested normalizing each local determinant by its expectation,
   using summable local variances, and then shifting the Gaussian
   Mellin integral in a Banach space. The reviewer also suggested the
   all-fixed-\(2k\) extension through the cancellation of linear terms
   in local mixed moments, and confirmed that only fixed-character
   polynomial reciprocal growth is needed. The author supplied the
   complete elementary mixed-tail proof, the written growth adapter,
   and the complete contour-shift proof.

Thus the review below is an independent reconstruction of the original
causal and necessity arguments, and a detailed second reconstruction
of the co-developed all-order sufficiency argument. It must not be
advertised as an independent discovery or a fully independent review
of the converse. The fresh
\(\texttt{/root/determinant\_independent\_review}\) agent supplies
the separate exact-current-source independent review for that purpose.
The historical-review agent supplied conceptual all-order feedback;
no final exact-source all-order receipt from that agent is presumed here.

Two precision suggestions from this reviewer are incorporated in the
final source: the causal measure is explicitly locally finite complex
Radon, and the native sextic set \(S\) explicitly contains primes over
\(6\). Neither suggestion changes the substantive arguments.

## 2. Causal transform and grouped prime coefficients

The Mellin interchange in Lemma 2.1 uses only a line
\(\Re s>\max(1,\sigma_0)\). The Gaussian low-scale bound and
the elementary large-scale bound make that interchange absolutely
integrable. No subcritical weighted integrability of the target sum is
inserted as a premise.

The ratio is forced in the correct direction:

\[
\int t^{-s}\,d\lambda(t)
=\frac{I_u(s)}{I_r(s)}
=\frac{E_u(s)}{E_r(s)}
  \frac{L_K(s,\psi_r)}{L_K(s,\psi_u)}.
\]

Its Dirichlet coefficients are grouped by rational integer norm.
The reviewer specifically checked that an inert rational prime has
no ideal of norm \(p\), so its first rational prime coefficient is zero.
At a split rational prime the two degree-one prime ideals contribute.
Away from the fixed exceptional primes,

\[
c_p
=\sum_{N\mathfrak p=p}\psi_r(\mathfrak p)
 -\sum_{N\mathfrak p=p}\psi_u(\mathfrak p).
\]

This is precisely the difference of the two induced characters on
the rational Frobenius class in the finite Galois closure. It is not
an assertion about one individual prime-ideal coefficient.

The continuous-measure exclusion also checks. After weighting the
difference measure by \(t^{-s_1}\), its pushforward under \(t\mapsto1/t\)
is finite on \([0,1]\). All its polynomial moments vanish, including
the constant moment. Polynomial density annihilates the measure;
removing the weight on compact subsets recovers equality of the
locally finite original measures. There is no unexamined mass at
infinity in this argument.

If the induced traces differ, a nonzero finite conjugacy class gives
a positive-density prime set on which \(|c_p|\) has a fixed positive
lower bound. The divergence of \(\sum |c_p|/p\) contradicts finite
weighted variation at any \(0<\sigma_0\le1\). Restricting equal
induced traces to the index-two subgroup yields equality of the two
multisets of one-dimensional characters. The only possible targets
are therefore \(\psi_r\) and \(\psi_r^c\), with multiplicities covered.

Conversely, field conjugation preserves the grouped \(L\)-function
by conjugating the ideal variable. The remaining finite Euler ratio
has finite weighted coefficient variation at every positive exponent
and gives the required causal identity. The threshold at exponent
one and the fixed-pair lower bounds in (3.7) are consistent with these
facts. No uniformity in a growing conductor is asserted.

## 3. Kummer orbit and physical masks

The residue-character equality criterion follows from the Kummer-Artin
identity and ordinary fixed-extension Chebotarev. In
\(K=\mathbb Q(\sqrt{-3})\), which contains the sixth roots of unity,
agreement outside finitely many primes forces \(u/r\in K^{\times6}\).

For each primitive target, dividing two row characters cancels the
fixed datum \(\nu\); hence its solutions occupy at most one Kummer
class. This gives two classes for linear causal transfers and four
when complex conjugation of the original sum is also permitted.
Field conjugation and conjugation of character values are kept
distinct throughout.

The integral representative and count were checked separately. Reduce
each prime valuation modulo six, retaining the unit. Class number one
gives
\(u=r_0v^6\), with no unnecessary coprimality condition on \(r_0,v\).
A negative valuation of \(v\) cannot produce an integral \(u\).
The sixth power is unchanged by changing the generator of \((v)\),
since every unit has sixth power one. Consequently the rows are in
bijection with integral ideals of norm at most
\((H/Nr_0)^{1/6}\). The asserted \(O(H^{1/6})\) count and the
cardinality exponent in the Hölder discussion follow.

The Euler factors deleted by the physical row remain in \(E_u/E_r\).
The classification does not replace their zero values by units, and
its conclusion is restricted to fixed dilation measures controlled
by weighted total variation.

## 4. Dense determinant family and its mean

The six-fold product in Section 5 retains the principal zero extension
in the \(j=0\) slot. If a prime divides the row, its complete local
determinant is one. This is the correct source mask.

Every member contains the fixed target reciprocal with a finite
nonzero Euler correction. In the open critical strip the other
reciprocal factors cannot have zeros coming from poles of their
finite-order Hecke \(L\)-functions. They therefore cannot cancel a
target pole. The principal pole at \(s=1\) is outside that claim.

The determinant-average calculation follows from the trace of exterior
powers and projection onto invariants. Splitting off the invariant
subspace gives

\[
P_\rho(x)=(1-x)^{m_0}Q_\rho(x),\qquad Q_\rho(0)=1,\quad Q_\rho'(0)=0.
\]

The deletion event changes the mean to
\(q^{-1}+(1-q^{-1})P_\rho(x)\). Dividing by the invariant factor
gives exactly

\[
R_{\rho,q}(x)
=(1-q^{-1})Q_\rho(x)+q^{-1}(1-x)^{-m_0}
=1+O_\rho(q^{-1}|x|+|x|^2).
\]

At \(|x|\le q^{-1/2}\) the last error tends uniformly to zero as
\(q\) grows. Thus one fixed finite deletion makes every remaining
factor nonzero on the entire closed boundary \(\Re s\ge1/2\).
On a smaller closed half-plane \(\Re s\ge1/2+\delta\), the errors
are summable. The resulting infinite product and its reciprocal
are bounded on that half-plane, and the product is holomorphic
and nonzero in the open domain. The finite primitive Euler
correction is also nonzero there.

The reviewer directly expanded the four cyclic-order terms for
\(C_6\) and recovered

\[
P_{\mathrm{reg},C_6}(x)
=1-x+2x^2-4x^3+3x^4-x^5
=(1-x)(1+2x^2-2x^3+x^4).
\]

This supports the displayed reduced-representation polynomial as
well. These are exact finite identities, not numerical evidence for
an arithmetic moment.

## 5. All-order normalized convergence and Gaussian continuation

Theorem 7.2 was checked at every fixed \(k\), without inferring an
unbounded-order statement from a finite computation.

After the fixed small-prime deletion, each mean is nonzero and
\(Z_{\mathfrak p}=1+W_{\mathfrak p}\) satisfies
\(\mathbb EW_{\mathfrak p}=0\) and
\(|W_{\mathfrak p}|\ll_\rho q^{-\Re s}\). For every
\(0\le j,\ell\le k\), the finite binomial expansion therefore gives

\[
\mathbb E Z_{\mathfrak p}^{\,j}\overline Z_{\mathfrak p}^{\,\ell}
=1+O_{\rho,k}(q^{-2\Re s}).
\]

The zero linear terms are essential. Independence makes the
\(2k\)-th norms of finite products uniformly bounded, since
\(\sum q^{-2\alpha}<\infty\) for every \(\alpha>1/2\).
For a tail product \(Y\), expansion of
\((Y-1)^k(\overline Y-1)^k\) cancels the constant contribution
of its mixed moments. The remaining errors give precisely the
Cauchy estimate (7.14). The prefix and tail are independent,
which justifies the factorization used there.

The estimates are uniform in all imaginary parts and on every
closed half-plane \(\Re s\ge\alpha>1/2\). Passing to the limit
in the Banach-valued Cauchy formula supplies holomorphy.
Comparison through unions of prime sets proves exhaustion
independence, and uniqueness in \(L^2\) identifies the limits
for different fixed \(k\). This checks the stated mode of
convergence without an almost-sure assertion.

The fixed-character reciprocal adapter also checks. For a
nonprincipal finite-order Hecke character, complete lattice
residue cells cancel and boundary cells give \(O_{\nu_0}(\sqrt x)\).
For the principal character, the main term in ideal counting
is subtracted and the pole is removed using
\((s-1)\zeta_K(s)/(s+1)\). The resulting function has linear
vertical growth on each fixed right strip. Under the stated
zero-exclusion hypothesis its analytic logarithm exists.
The outer and inner Borel--Carathéodory radii in Lemma 7.3
are strictly separated and remain inside \(\Re s>1/2\).
The bounded Euler-line center value then gives polynomial
reciprocal growth. This uses only the fixed-character
portion of the earlier adapter.

The crucial continuation is

\[
F(s)=\frac{\mathcal H(s)}{L_K(s,\nu_0)^{m_0}}X(s).
\]

It agrees with the original absolutely convergent random
Dirichlet series on \(\Re s>1\). The source does not infer
convergence of its raw finite Euler products below one when
\(m_0>0\). Holomorphy of \(F\) below one is established exactly
under the assumptions used for the subsequent shift.

The Gaussian inverse Mellin integral starts on \(c>1\),
where the coefficient majorant \(\zeta_K(c)^d\) makes
termwise inversion valid. Polynomial vertical growth and
the factor \(e^{-t^2/2}\) make both vertical Bochner
integrals absolutely convergent in \(L^{2k}\); the
horizontal integrals vanish. Shifting to
\(\alpha=1/2+\epsilon/(2k)\) gives
\(\|\mathcal B(D;G)\|_{2k}\ll D^\alpha\), hence the
claimed \(D^{k+\epsilon}\) moment.

When \(m_0=0\), the deterministic factor is already analytic
and bounded in every smaller half-plane, so this conclusion
is unconditional in the model. When \(m_0>0\), any one of
the desired even moments gives the second moment by Hölder.
Jensen then makes the mean's Mellin transform holomorphic
to the right of one half. Its nonzero Gaussian and
\(\mathcal H\) factors rule out a target pole. This proves
the exact equivalence claimed in Theorem 7.4, without
assuming target integrability as part of its necessity proof.

The final rank-one example (7.24) was checked after it was added.
For distinct squarefree ideals a prime occurs on only one side;
its local mean character value is zero. For identical ideals,
the squared modulus contributes precisely
\(\prod_{\mathfrak p\mid\mathfrak n}(1-(N\mathfrak p)^{-1})\).
The fixed character has modulus one outside \(S\), which contains
its conductor. Gaussian absolute convergence justifies expanding
the expectation, and ideal counting bounds the diagonal sum by
\(O_K(D)\). No alias from sixth powers occurs at this squarefree
second-moment calculation. The all-order conclusion uses the
preceding normalized-product theorem, not a false higher-order
diagonal-only assertion.

## 6. Source checks and acceptance boundary

The reviewer read the exact Gaussian source at PR #929,
\(\texttt{97bf40329489992e9384c34d7595af6d01a40774}\), and the
fixed-character lattice/logarithm adapter in Section 8.1 of
FOURTH_MOMENT_ATTACK.md at PR #913,
\(\texttt{6498d6cc2eded03159c7332b25fd224ad07f89c1}\).
Only those stated interfaces are used here; the imported
quasi-Riemann or canonical native moment theorem is not replayed
or invoked by this review.

The exact finite complete-residue identity in
MOBIUS_CRT_TRANSLATION.md was also read at PR #911,
\(\texttt{2f8b6a3898a722d0602a91dea73bac344a3bb7dd}\).
The rank-one source credit is appropriate: that earlier identity
retains all nonunit zeros and explicitly distinguishes its complete
residue measure from a short physical norm ball.

The primary author-hosted sources were opened and the cited
statements checked:

- P. Stevenhagen, *Class Field Theory*, November 7, 2002,
  Theorem 3.1 and Proposition 3.10, at
  <https://websites.math.leidenuniv.nl/algebra/cft.pdf>.
- J. S. Milne, *Class Field Theory*, version 4.03,
  August 6, 2020, V.3.23, VIII.7.4, and the prime-count
  formulation in VIII.7.5, at
  <https://www.jmilne.org/math/CourseNotes/CFT.pdf>.

No effective or conductor-uniform form of Chebotarev is imported.
No zero-free hypothesis is hidden in the causal classification,
the determinant mean formula, or the normalized convergence theorem.
The only target zero-exclusion premise appears explicitly in the
invariant-containing sufficiency direction.

**Acceptance:** the original independent reconstruction and the
later disclosed co-development review both support the exact
source at the hash above. No correction is requested.
The probability measure remains the specified independent local
model. This review supplies no comparison with the growing
physical row ball, no native generalized moment theorem, and
no unconditional zero exclusion.
