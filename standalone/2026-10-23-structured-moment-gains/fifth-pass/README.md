# A sextic A+B moment, its resonant term, and amplified cubic components

24 October 2026. Proposed source-dependent extensions of the frozen
fourth-pass mathematics at
[8c88fd2](https://github.com/GettysburgResearch/riemann/commit/8c88fd23300bba093ce2f78295c4e27dbd60147d).
The new sextic coefficient theorem uses the pinned large sieve and
ordinary Hecke functional equation, with no zero-free hypothesis.
The cubic radical-range and amplified-component results retain the
explicit \(\mathrm{ZF}_\beta\) premise. These are distinct coefficient
families and distinct deductions.

No smaller global zero-free boundary is proved. The complete inverse
or signed numerator consumer is still required. The new results are
stated below with the coefficients, orientations, and remaining
application requirements explicit.

The fourth-pass mathematical files and their exact-commit review are
preserved. This directory is a separate mathematical object.

## 1. A complete sextic moment with a phase-canceling coefficient

Let \(\gamma_j(n)\) be the normalized Gauss sum of the \(j\)-th power
of the sextic character \(\chi_n\), with the exact additive convention
in the proof. Put \(\alpha(n)=n/|n|\) for the primary generator and
fix \(\theta(n)=\alpha(n)^\ell\nu(n)\), with fixed finite-ray data
\(\nu\) and fixed integer \(\ell\). For a nonnegative radial annular
row weight \(W\) and norm-annular column weight \(V\), define

\[
J_{6,\theta}(A,B)=\frac1B\sum_{a\equiv1\ (3)}W(a/\sqrt A)
\left|\sum_n\mu(n)\theta(n)\gamma_2(n)
                       V(Nn/B)\chi_n(a)\right|^2.
\]

The primary rows are unrestricted. The column ideals lie outside the
fixed omitted set \(S\) of the theorem, retain their original zeros
on nonunits, and are squarefree because of \(\mu\). The sextic
character has the **positive orientation displayed above**.

For every \(A,B\ge1\) and every \(\epsilon>0\), the new theorem and
its companion give

\[
\boxed{J_{6,\theta}(A,B)\ll(AB)^\epsilon
\left\{A+B+\mathbf1_{\ell=-1}A^{5/6}B^{1/3}\right\}.}
\]

Thus every fixed nonresonant angular type \(\ell\ne-1\) has the
\(A+B\) bound. The assertion allows fixed finite linear combinations
of ray characters of the same angular type and bounded smooth test
families. It does not insert a moving conductor into \(\theta\), and
it does not extend the coefficient to \(\mu d_K\gamma_2\).

The improvement comes from an exact arithmetic cancellation. The
pinned identity

\[
\gamma_1(n)\gamma_2(n)=\mu(n)\alpha(n)G(n)
\]

turns the column after pair Poisson into
\(\mu^2(n)\alpha(n)G(n)\theta(n)\). Here \(G\) is a fixed finite-ray
function. After expanding the squarefree restriction, the resulting
full character sums can be reflected by the ordinary Hecke functional
equation. No zero-free region is used.

The proof retains every common divisor, original zero, and nonzero
Fourier frequency. In its notation, the ordinary moving phase is
\(v=f^2/m\), equivalently \(f^2m^5\) on the retained support. Its
complete conductor-times-redundant-radical budget is \(KF\), where
\(F=Nf\). The extra coprimality divisor \(l\) is removed before
reflection; it contributes no extra factor to that phase budget.
The complete nonprincipal ledger sums to \(B(AB)^\epsilon\), and
the genuine pair diagonal contributes \(A(AB)^\epsilon\).

At \(\ell=-1\), principal inducing characters are separated before
reflection. Their good frequencies satisfy

\[
k_{\rm good}=f^4m q^6.
\]

Counting that set with the actual Fourier tail, including subunit
nominal widths, gives the additional
\(A^{5/6}B^{1/3}\) term. At \(A=B\) it is \(B^{7/6}\). This prices
the resonance explicitly. In particular it includes the resonant
coefficient \(\overline{\gamma_1}\), obtained by taking
\(\theta=\alpha^{-1}\overline G\) and expanding its finite-ray part.

Read the complete proof in
[SEXTIC_ROW_PHASE_CANCELLATION.md](SEXTIC_ROW_PHASE_CANCELLATION.md)
and the angular completion in
[SEXTIC_RESONANT_ANGLE_COMPLETION.md](SEXTIC_RESONANT_ANGLE_COMPLETION.md).

This sextic statement and the cubic theorem in Section 2 concern
different character orientations and coefficients. The cubic
divisor-weight adapter cannot be used to insert \(d_6\) into the
new sextic theorem.

## 2. The moving radical may approach the column length

Fix an integer \(K\ge1\), the angular type, the initial arithmetic data, and
\(0<\sigma<1\). Let \(J_{K,R}(A,B)\) be the all-row normalized cubic
moment with the actual coefficient
\(\mu(n)d_K(n)\theta_R(n)G_3(n)\), as defined in the fourth pass.
Here \(G_3\) denotes the normalized cubic Gauss coefficient called
\(G\) in that theorem. Section 1 uses \(G\) for its finite-ray phase.
The natural presentation is common to the row mean. Its squarefree
radical \(R\) includes every moving good conductor prime and every
moving good redundant zero.

The new theorem replaces the earlier restriction \(NR\le B^{2/3}\)
by

\[
\boxed{NR\le B^{1-\sigma}.}
\]

For some \(\eta=\eta(\sigma,K,\beta)>0\),

\[
J_{K,R}(A,B)
\ll(AB)^\epsilon\{A+(AB)^{2/3-\eta}\},
\qquad A\ge B\ge2 .
\]

When \(1\le A\le B\), set \(C\asymp(B/A)^{1/3}\), with the stated
fixed endpoint adjustment. The sufficient restriction
\(NR\le(B/C)^{1-\sigma}\) gives

\[
J_{K,R}(A,B)
\ll(AB)^\epsilon
\{A^{1/3}B^{2/3}+A^{1/3}B^{1-2\eta}\}.
\]

For example, the fixed choice \(\sigma=1/10\) permits radicals
through \(B^{9/10}\) in the first range. There is no claim at
\(\sigma=0\), no uniform saving as \(\sigma\) tends to zero with the
lengths, and no assertion for \(B/\log B\).

The proof revisits the exceptional full-factor budget. With auxiliary
slack \(\lambda>0\), conductor plus height contributes the exponent
\(1-3\lambda/4<1\). The two endpoint estimates then have strict gaps
\(\lambda/2\) and \(3\lambda/4\). The fixed-factor argument, powerful
correction series, original diagonal, common-divisor tails, and all
frequencies are retained. The proof gives explicit choices transferring
the new gap through every outer cutoff.

See
[NATURAL_PRESENTATION_RANGE_WITH_FIXED_POWER_GAP.md](NATURAL_PRESENTATION_RANGE_WITH_FIXED_POWER_GAP.md).

In the frozen unamplified fourth-moment variables, the legal conductor
range becomes

\[
T\le U^{4(1-\sigma)/(7-\sigma)}
       X^{(1-\sigma)/(7-\sigma)}.
\]

At \(X\asymp U^2\), the choice \(\sigma=1/10\) gives
\(T\le U^{18/23}\), with the required strict margins. Its exponent
approaches \(6/7\) as a fixed \(\sigma\) is chosen small. This is the
range where the estimate can be applied; its size still increases
with \(T\), so it does not eliminate the large-core problem.

## 3. Keep the actual prime amplifier in the fourth-moment component

This result applies to squarefree good physical rows
\(Nu\asymp U\), fixed initial arithmetic data, and the actual product
of disjoint smooth prime slots

\[
\mathcal Q_u=\prod_i\left(P_i^{-1/2}
\sum_{p\ {\rm prime}}a_i(p)\psi_u(p)W_i(Np/P_i)\right),
\qquad L=\prod_iP_i.
\]

The coefficient and zero-extension conventions are the source's
ones. The result handles both the reflected pair of plain witnesses
and the fourth-power AFE. Its root-number coefficient is the actual
\(\mu(u)\overline{\gamma_2(u)}\), with fixed angular/ray factors.

The important identity retains all coincidences. Let \(D\) be the
coincident prime product and \(P,Q\) the unmatched products. For
\(n=t h^2\), split

\[
P=ac,\quad Q=bd,\quad t=sab,\qquad v=scd,\quad k=ad^2h .
\]

Then, including zeros on nonunits,

\[
1_{(u,D)=1}\chi_{6,u}(th^2)\chi_{6,u}(P)
\overline{\chi_{6,u}(Q)}
=1_{(u,Db)=1}\chi_{6,u}(v)\chi_{3,u}(k).
\]

The complete common moving radical is
\(\operatorname{rad}(vDb)\). The canceled prime phase at \(b\)
retains its zero; the prime \(a\) remains in the cubic row.

For \(Nn\asymp X\), \(Nv\asymp T\), and \(1\le X\le U^2\), the
coefficient-energy calculation cancels the apparent power cost from
counting prime pairs. In the short-row branch it gives

\[
|\mathcal C_{X,T}|
\ll (UXL)^\epsilon
U^{1-\eta}X^{-1/6}T^{2/3}
\]

under the exact conductor condition in the proof. The long-row branch
has its own displayed bound. Together they imply the following:
for every fixed \(\delta>0\), if

\[
L\le U^{1/12-\delta},
\]

the sum of the specified signed components

\[
T\le X^{1/4}U^{3\eta/4}
\]

is \(\ll U^{1-\eta/3}\), after choosing the positive saving and
subsidiary losses as stated. The proof includes the profile tails,
a sufficiently small growing common height range, all prime
coincidence patterns, and square-core overlaps.

The existing selected-prime capacity \(2m+6\kappa z\le1\), with
\(L=U^z\), gives \(z\le1/(18\kappa)<1/12\) when
\(m\ge1/3\) and \(\kappa>2/3\). Thus the component estimate retains
the actual prime product in that range without a pointwise prime
charge.

See
[PRIME_AMPLIFIED_FOURTH_MOMENT_CORE.md](PRIME_AMPLIFIED_FOURTH_MOMENT_CORE.md).
This proof uses the already frozen \(2/3\) natural-presentation
theorem; its validity does not depend on silently importing the
larger range in Section 2.

## 4. What remains to reach the zero-free consumer

The amplified result controls a signed part of the original moment.
It does not bound a detected class, the nonsquarefree physical rows,
or the remaining combined cores
\(Nv>X^{1/4}U^{3\eta/4}\).

In the generic disjoint-prime case, a squarefree index \(n\) coprime
to \(PQ\) produces \(v=nPQ\). At the main scale its norm can be
\(U^2L^2\). Trivial common supports do not force this term into the
controlled range. The exact remaining phase and sparse coefficient
conditions are displayed in the component proof.

The fourth-pass complete cubic inverse target also remains open:
the example boundary \(131/150\) would need, already in its
unit-divisor core, \(J(D^{22/25},D)\ll D^{1+\epsilon}\).
Neither the larger radical range nor the amplified component proves
that estimate. No numerical global boundary is promoted here.

The new sextic theorem supplies a stronger estimate for its stated
coefficient family, but the sixth-power dual has
\(\mu d_6\gamma_2\) after whole-sum conjugation. That divisor weight
is outside the theorem. There is also a separate signed-consumer
problem: at the actual scales \(H=U^2\), \(B=U^3\), even the
hypothetical bound \(J_6(H,B)\ll H+B\) would cost \(U^2\) under
the direct Cauchy step. Merely reflecting the corresponding linear
sum returns the original approximate functional equation. These
calculations are included in the sextic proof, rather than leaving
its global application implicit.

The six-full-factor continuation and its exact missing induction
closure are recorded in
[MANY_PLAIN_FACTOR_INDUCTION_CHECK.md](MANY_PLAIN_FACTOR_INDUCTION_CHECK.md).
This is a limitation of the specified positive argument, not a
counterexample to the desired arithmetic moment.

## 5. The connection to newer repository work was checked explicitly

PR1019 was refreshed at
\(3bcc1daaeb51c71cb2785b9744cde0d641f68f4c\). Its natural-label
projection and coherent remainder retain the actual raw Möbius
coefficient vector. The first Poisson transform of that coefficient
is

\[
\mu(n)\gamma_1(n)=\alpha(n)G(n)\overline{\gamma_2(n)}.
\]

It lacks the extra \(\mu(n)\) in the new theorem. A second Gauss
cancellation returns \(\mu\), whereas the new proof needs
\(\mu^2\). A columnwise unitary change preserves the coefficient
norm but changes the specified vector and its projection. Therefore
the new estimate cannot simply be assigned to PR1019's unresolved
complement.

[PR1019_COEFFICIENT_TRANSFER_AUDIT.md](PR1019_COEFFICIENT_TRANSFER_AUDIT.md)
binds four exact source files, checks their character conventions,
and identifies the free coefficient in the primitive and continued
formulas. It preserves the projection improvement while making the
remaining transfer requirement concrete.

## 6. Sources and review

[SOURCES.json](SOURCES.json) binds the new files and their exact
mathematical parents. The proofs received independent local review
before freezing. An exact-commit review-only successor records the
remote byte bindings and the mathematical scope.

These extensions are source-dependent analytic deductions. Independent
agent review is not external peer review or formal verification. No
new finite checker is
offered as a proof of their uniform asymptotic statements. The
fourth-pass formal checker and its authenticated replay are preserved
at their original mathematical and review commits.
