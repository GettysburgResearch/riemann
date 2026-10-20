# A quantitative interface for retaining the resonant theta residue

Date: 20 October 2026.

Status: proved elementary weighted-row bound and conditional analytic
adapter. The all-field residue premise below is **not proved here**.
This note identifies an input sufficient to remove the two resonant
unitary exceptions in the inverse estimates without improving Liu's
numerical comparison system. The companion
[EISENSTEIN_SPHERICAL_REFLECTION.md](EISENSTEIN_SPHERICAL_REFLECTION.md)
now proves the residue premise over \(E\), for all fixed finite data and
moving punctures. Its insertion into the full source marked induction
is in [EISENSTEIN_UNITARY_INVERSE.md](EISENSTEIN_UNITARY_INVERSE.md).

Exact dependencies: the normalized inverse family and margin in Liu,
[arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1),
Section 10.2, equations (10.4)--(10.5), and the selected family of Section
11.2. The actual Eisenstein-field residue and its native filter laws are
proved, from the published residue formula, in
[RESONANT_RESIDUE_MEAN.md](RESONANT_RESIDUE_MEAN.md).

This interface does not use the conditional marked saving in Section 3
of that companion note. Thus no zero-free hypothesis is used to establish
the preliminary inverse moment in this proposed route.

## 1. A uniform weighted-row lemma, including arbitrary labels

Let \(F\) be a fixed number field and \(S\) a fixed finite set of primes.
For exterior ideals \(k,f\), put

\[
 j_p(k,f)\equiv v_p(k)+4v_p(f)\pmod6,\qquad 0\le j_p<6.
\]

Define the nonnegative arithmetic majorant

\[
 b_f(k)=
 \begin{cases}
 \displaystyle\prod_{\substack{p\\j_p(k,f)\in\{2,4\}}}q_p^{-1/3},
       &j_p(k,f)\in\{0,2,4\}\text{ at every }p,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{1.1}
\]

The product includes primes of \(f\) even if they do not divide \(k\).

**Lemma 1.1.** For every \(\epsilon>0\) and \(H\ge1\),

\[
 \boxed{\sum_{q_k\le H}b_f(k)
         \ll_{F,S,\epsilon}H^{1/3+\epsilon}q_f^\epsilon.}
 \tag{1.2}
\]

The implied constant is independent of the label, including its number
of primes and its valuations.

**Proof.** Take \(\sigma>1/3\). At a prime outside \(f\), the local
Dirichlet series in \(k\) is

\[
 B_0(q,\sigma)=
 \frac{1+q^{-1/3}(q^{-2\sigma}+q^{-4\sigma})}
      {1-q^{-6\sigma}}.
 \tag{1.3}
\]

The product over all exterior primes converges, since
\(2\sigma+1/3>1\) and \(6\sigma>1\).
At a prime of \(f\), the even shift \(4v_p(f)\) merely permutes the
three allowed residues \(0,2,4\). Each numerator term has magnitude at
most one, and \(B_0(q,\sigma)\ge(1-q^{-6\sigma})^{-1}\). Its replacement
factor is therefore at most \(3B_0(q,\sigma)\). Consequently

\[
 \sum_k b_f(k)q_k^{-\sigma}
       \ll_{F,S,\sigma}3^{\omega(f)}
       \ll_{F,S,\sigma,\epsilon}q_f^\epsilon.
 \tag{1.4}
\]

The last estimate follows by putting all primes with \(q_p^\epsilon<3\)
into one fixed finite constant. Rankin's bound
\(1_{q_k\le H}\le(H/q_k)^\sigma\), and a sufficiently small
\(\sigma-1/3>0\), prove (1.2). No cancellation or sieve theorem is
used. \(\square\)

If a fixed source orientation has only digits \(0,4\), replace (1.1)
by that smaller support. Its exterior local factor is
\((1+q^{-1/3-4\sigma})/(1-q^{-6\sigma})\). The same proof gives the
stronger \(H^{1/6+\epsilon}q_f^\epsilon\). The weaker symmetric bound
(1.2) is enough below and allows either whole orientation.

## 2. The missing source premise, stated with all of its interfaces

For a fixed finite coefficient/profile family, consider the resonant
completed theta sum in the exact source normalization. Its original
column parameter is \(X\), its row is \(k\), and its label is \(f\).
The proposed premise is the following.

**Residue interface R.**

1. After the compact-test theta reflection is continued meromorphically,
   the extra spherical term is
   \[
   X^{1/3}\widehat W(5/6)\,\mathfrak r(k,f;\rho,\upsilon)
   \tag{2.1}
   \]
   for the centrally normalized coefficient sum; harmless fixed
   profile constants and a finite list of such terms are allowed.
   There is no additional pole to the right of the reflected contour.

2. The actual finite-place, unit-sector, and coprimality data satisfy
   \[
   |\mathfrak r(k,f;\rho,\upsilon)|^2
        \ll C\,b_f(k).
   \tag{2.2}
   \]
   The constant can depend on the fixed field, coefficient family,
   finite \(S\)-data and profile, but not on moving \(k,f,\rho\).
   Common-prime zeros and all active digit-zero filters are retained.
   Divisor-bounded factors can be allowed with a declared
   \((q_kq_f)^\epsilon\) loss.

3. Full-index prime divisibility marks have residue multiplier
   \(1/q_p\), while full-index coprimality filters have multiplier
   \(1-1/q_p\), at an exterior prime not already forced to zero.
   Products and priority assignments respect these identities.
   Equivalently, each surviving selected prime position has absolute
   residue mass bounded by \(\sum_{p\in\mathcal P_i}O(1)/q_p=O(1)\).

4. The subtracted reflection has the same coefficient transformations,
   finite profile family, and bounds
   \(\min(x^{a_0},x^{-A})\), \(0<a_0<1/3\), as the nonresonant
   reflection. All statements use finite test seminorms and polynomial
   norm-height costs before a common Fourier measure is taken.

These four clauses are a source statement, not an arbitrary majorant
substitution. The companion theorem proves the residue size and filter
law for the explicit Eisenstein cubic twists \(G_r\) and their completed
theta index. It does **not** identify every all-field coefficient,
Jacquet constituent, finite \(S\)-profile, or pole in R.

## 3. Why this residue would fit the existing inverse induction

The source normalized theta family is

\[
 \mathcal E=Z^{-N-V}
   \sum_{\substack{f\ {\rm sf}\\q_f\asymp Z^V}}w(f)
   \sum_{0<q_k\ll Z^M}
   \left|\sum_{n\ {\rm sf}}
       a_0(n)\nu(n)\rho(n)\chi_n(k)\chi_n(f)^4
                           W(q_n/Z^N)\right|^2,
 \tag{3.1}
\]

where \(w(f)\) is nonnegative and divisor-bounded. Put \(F=N+V\);
the required margin is \(F-M-Q\ge c>0\), with \(Q\ge0\) the
coprimality charge.

Assume R. By (2.1)--(2.2) and Lemma 1.1, the residue part of (3.1) is

\[
 \mathcal E_{\rm res}
       \ll Z^{(2N+M)/3+\epsilon}.
 \tag{3.2}
\]

To check normalization directly: dividing the inner sum by \(Z^{N/2}\)
makes its residue \(Z^{N/3}\mathfrak r\); squaring gives \(Z^{2N/3}\).
The label count \(Z^{V+\epsilon}\) cancels the prefactor \(Z^{-V}\).
The row estimate is \(Z^{M/3+\epsilon}\). Thus no factor of \(Z^V\)
or \(Z^N\) has been silently dropped.

The source margin now implies the strict gap

\[
 F-\frac{2N+M}{3}
      =\frac{N+3V-M}{3}
      \ge\frac{2V+Q+c}{3}\ge c/3.
 \tag{3.3}
\]

Hence the spherical term is \(O(Z^{F-c/3+\epsilon})\).
This remains true for selected primes under the source's stronger
margin \(F-M-Q-z_0\ge c\), since R.3 introduces no prime-length
power into the residue bound. The second selected margin remains
available for the existing dual term.

For the short cube-completion divisor \(h\), the source coefficient
has magnitude at most \(q_h^{-1}\), and its theta scale is
\(X=Z^N/q_h^3\). The residue therefore gains another \(q_h^{-1}\):

\[
 q_h^{-1}X^{1/3}=Z^{N/3}q_h^{-2}.
 \tag{3.4}
\]

The sum of this absolute divisor mass converges. Fixed norm modes
have modulus one. If a selected prime is assigned to \(h\) rather
than the surviving theta index, the mass at that prime is
\(O(q_p^{-2})\); otherwise it is \(O(q_p^{-1})\) by R.3. Summing
either over a fixed-ratio prime annulus costs \(O(1)\). Thus the
source's priority assignment causes no new positive scale exponent
in the residue term.

Splitting a terminal reflection into its dual sum and its residue costs
only a fixed factor in the positive squared norm. A finite-depth
induction absorbs this factor in its constants; the strict source
margins and the new \(c/3\) residue margin absorb the subsidiary mesh
losses. The nonterminal two-Poisson identities and the ordinary
product-moment recursion do not change.

This proves the following **conditional adapter**, not R itself:
if R is established for the entire finite family encountered by the
source inverse induction, that induction and its selected version
extend to the resonant unitary coefficients. The existing sixth-power
amplification then supplies the noncircular \(11/12\) starting bound;
the already available angular/radial product adapter supplies the
ordinary product interface. A refined \(B_\flat\) conclusion still
requires control of the spherical residue in the actual direct
compensated comparison. The inverse-terminal calculation here does not
by itself establish that different estimate.

No claim at a smaller numerical boundary follows. In particular, even
a complete proof of R expands the family available to the inverse
method, not prove RH.

## 4. Source work still required

Over a general field, the next concrete task is to compute the weighted global constant term
of the actual digit-averaged spherical theta vector, including its
fixed finite \(S\)-profiles. One must identify its local digit support,
the pole locations and multiplicities, the residue coefficient, and
the compatibility of full-index marks with that coefficient.
The pointwise \(q_r^{-1/6}\) conductor decay, the \(1/q_p\) marked
residue law, the complete fixed-conductor support, and the absence of
additional poles are now proved over \(E\) in the spherical companion.

Local pole powers \(1/3,2/3\) alone do not prove R.2. A local
annihilating differential operator alone does not prove R.4: its
Mellin zeros can restore the missing residue during deconvolution.
The source-specific global residue, rather than disappearance of its
formal constant term, is the remaining analytic object.
