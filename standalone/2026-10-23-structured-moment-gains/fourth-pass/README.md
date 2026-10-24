# Rectangular cubic moments, moving presentations, and reflected numerators

24 October 2026. **Proposed source-dependent mathematics.** This fourth
pass extends the structured cubic moment to a new rectangular range,
moving natural characters, and every fixed divisor weight. It also
proves a power saving for an explicitly defined component of the
reflected fourth moment. The complete global zero-free consumer remains
open; no smaller global half-plane is asserted.

The first three passes are preserved byte for byte. The mathematical
parent of this additive pass is the third-pass review commit
[b8127aa](https://github.com/GettysburgResearch/riemann/commit/b8127aa7ed2581d5d16ac9267795593bc19c9876).
The inherited third-pass theorem is frozen at
[f11e866](https://github.com/GettysburgResearch/riemann/commit/f11e86684905c6417683a9f45ac75c223da6a162).
All new claims below retain its pinned analytic inputs and explicit
zero-free hypothesis. Independent agent review does not replace
external peer review or formal verification.

## 1. The combined coefficient theorem

Work over the Eisenstein integers with the inherited primary-generator
conventions. Let \(G(n)\) be the normalized cubic Gauss coefficient and
\(\chi_n\) the cubic character, extended by zero on nonunits. Let
\(K\ge1\) be a fixed integer, and put

\[
a_K(n)=\mu(n)d_K(n)=\mu(n)K^{\omega(n)}.
\]

Let \(\theta_R\) have fixed angular order and fixed ramified ray data.
Its moving finite part is a natural sextic presentation on a squarefree
radical \(R\). **Every moving good conductor prime and every moving good
redundant zero belongs to \(R\)**, including primes at which local
exponents cancel; the fixed ramified data are separate.
The whole presentation is common to the row mean. Define

\[
J_{K,R}(A,B)=
\sum_aW(a/\sqrt A)
\left|\sum_n
\frac{a_K(n)\theta_R(n)G(n)}{\sqrt{Nn}}\,
\overline{\chi_n(a)}V(Nn/B)\right|^2 .
\]

The rows \(a\) are unrestricted by squarefreeness. The weights are in
the fixed smooth classes of the inherited theorem.

Assume \(\mathrm{ZF}_\beta\): all primitive finite-character twists of
the fixed angular type are zero-free in \(\Re s>\beta\), for a fixed
\(1/2<\beta<1\); the possible principal pole is permitted. Under this
hypothesis and the pinned source estimates, there is an
**existential** \(\eta_K>0\), uniform in the allowed moving presentation,
such that

\[
\boxed{
J_{K,R}(A,B)\ll (AB)^\epsilon
\begin{cases}
A+(AB)^{2/3-\eta_K},& A\ge B\ge2,\\[2mm]
A^{1/3}B^{2/3}+A^{1/3}B^{1-2\eta_K},&1\le A\le B.
\end{cases}}
\]

The first case requires \(NR\le B^{2/3}\). In the second case set
\(C\asymp(B/A)^{1/3}\); the sufficient restriction is
\(NR\le(B/C)^{2/3}\). Constants may depend on fixed \(K\), the angular
order, the initial ray data, \(\beta\), and the test class.
No numerical value is assigned to \(\eta_K\).

The proof has three distinct new steps:

1. **Exact cubic amplification.**
   For \(K=1\), the normalized column \(F_h(B)\) satisfies
   \[
   F_h(B)=\sum_{d\mid\operatorname{rad}c}
   \frac{\mu(d)\theta_R(d)G(d)\overline{\chi_d(h)}}{\sqrt{Nd}}\,
   F_{h d c^3}(B/Nd).
   \]
   The extra factor \(d\) in the output row supplies the Gauss
   reciprocity phase. Averaging \(Nc\asymp C\), retaining all zero
   masks, and bounding the complete fibre gives the rectangular
   theorem. The corresponding identity for the \(a_K\)-weighted
   column uses \(a_K(d)\) in the outer coefficient and the same
   \(a_K\)-weighted column at the shortened inner scale.
2. **Natural reflection with a moving radical.**
   Primitive conductor times redundant radical is bounded by the
   full displayed support. The exact natural functional equation
   keeps the common conjugate character and every zero. Its Euler
   quotient is bounded on the symmetry line; the common dual cutoff
   charges the full radical. Principally induced rows are separated
   before reflection. This permits canceled local characters without
   replacing them by unmasked phases.
3. **Fixed divisor weights.**
   The exact identity
   \[
   a_K=\mu^{*K}*h_K,\qquad
   \sum_{j\ge0}h_K(p^j)x^j=\frac{1-Kx}{(1-x)^K}
   \]
   has a powerful-supported, absolutely summable correction for
   \(\Re s>1/2\). The short Möbius identity reduces \(\mu^{*K}\) to
   at most \(3K\) factors. The exceptional argument extends to this
   fixed factor count. The large powerful-divisor tails are bounded
   explicitly with the unrestricted-inner cubic sieve. Deleted Euler
   factors are combined before bounding, avoiding artificial poles.

The complete proofs are
[CUBIC_POWER_RECTANGULAR_EXTENSION.md](CUBIC_POWER_RECTANGULAR_EXTENSION.md),
[MOVING_SEXTIC_TWIST_EXTENSION.md](MOVING_SEXTIC_TWIST_EXTENSION.md),
[NATURAL_PRESENTATION_TWIST_EXTENSION.md](NATURAL_PRESENTATION_TWIST_EXTENSION.md),
and [MOBIUS_DIVISOR_COEFFICIENT_ADAPTER.md](MOBIUS_DIVISOR_COEFFICIENT_ADAPTER.md).
The odd-local moving-twist note is retained as its own reviewed result;
the later natural-presentation note states the broader scope explicitly.

## 2. A signed fourth-moment component with a power saving

For a nonprincipal primitive sextic character induced by a squarefree
physical row \(u\), the central functional equation gives

\[
|L(1/2+i\tau,\psi_u)|^4
=2\Re\left\{\mathcal E_u(\tau)^{-2}
\sum_n\frac{d_4(n)\psi_u(n)}{(Nn)^{1/2+i\tau}}
V_\tau(Nn/Q_u^2)\right\}.
\]

The finite part of \(\mathcal E_u^{-2}\) is the actual coefficient
\(\mu(u)\overline{\gamma_2(u)}\), up to fixed angular and ray factors.
Writing \(n=t h^2\), with \(t\) squarefree and no imposed coprimality
between \(t,h\), gives the cubic phase that matches the conjugate of
the new moment.

For \(Nu\asymp U\), \(Nn\asymp X\), \(Nt\asymp T\),
\(1\le X\le U^2\), and \(1\le T\le X\), the specified signed block
satisfies

\[
\boxed{
|\mathcal C_{X,T}(U,\tau)|
\ll (XU)^\epsilon(1+|\tau|)^C
U^{1-\eta}X^{-1/6}T^{2/3}}
\]

in the stated shortened-column range
\(T\le U^{2/5}X^{1/10}\), with a fixed strict margin.
Consequently the sum of the components
\(T\le X^{1/4}U^{3\eta/4}\), including the controlled AFE tails, is
\(\ll U^{1-\eta/3}\) for a sufficiently small fixed growing height
range. At the balanced scale \(X\asymp U^2\), this covers
\(T\le U^{1/2+3\eta/4}\).

The result concerns squarefree physical rows, fixed initial
ramification, and the unamplified signed component. It does not give a
power saving for the full fourth moment, arbitrary detected classes,
or all prime-amplified terms. The larger squarefree cores remain in
the exact signed expression.

See [ROOT_NUMBER_FOURTH_MOMENT_SMALL_CORE.md](ROOT_NUMBER_FOURTH_MOMENT_SMALL_CORE.md)
for the normalization, common profiles, conductor condition, tail
argument, and remaining phase.

## 3. Exact route to a smaller boundary

[CUBIC_RAW_CONSUMER.md](CUBIC_RAW_CONSUMER.md) derives the complete first
Poisson expression for the raw cubic inverse, including the \(f,m,l\)
weights, moving twists, punctures, and genuine diagonal. It proves the
following conditional implication:

\[
I_\theta(H,D)\ll H(HD)^\epsilon
\quad\text{for every }H\ge D^{\alpha+c}
\quad\Longrightarrow\quad
B_{\rm new}=\frac12+\frac{\alpha}{3},
\]

with the full hypotheses and strict buffers in that note.
To beat the source-qualified benchmark
\(B_{\rm flat}=0.874886647039964\ldots\), it would suffice to obtain

\[
\alpha<1.124659941119892\ldots .
\]

For example, \(\alpha=28/25\) would imply
\(B_{\rm new}=131/150=0.873333\ldots\).
**This is a target, not an achieved zero-free boundary.**
Already the unit-divisor core at this target requires a complete
coefficient-preserving estimate
\(J(D^{22/25},D)\ll D^{1+\epsilon}\).
The rectangular estimate proved here does not establish that bound.

Two additional exact reductions identify other possible consumers:

- [SIXTH_MOMENT_ROOT_NUMBER_REDUCTION.md](SIXTH_MOMENT_ROOT_NUMBER_REDUCTION.md)
  applies the functional equation to the full sixth power. Cubing the
  root number removes its nonconstant finite Gauss phase, and angular
  Poisson removes the zero Fourier mode. Every nonzero mode remains.
  The divisor-weight theorem above supplies its squarefree
  \(\mu d_6\) coefficient class, but the full sextic coupling,
  opposite cubic orientation after a square decomposition, and
  nonsquarefree sectors still require estimates.
- [PRIME_AMPLIFIER_COMPLETION_AND_KERNEL.md](PRIME_AMPLIFIER_COMPLETION_AND_KERNEL.md)
  proves the exact quartic local completion statement for a prime
  fourth-power amplifier. The projection changes the Fourier kernel.
  Its mass cannot remain concentrated in the short kernel range
  required by the proposed recursion; the ordinary kernel cannot be
  retained after the projection.

The sixth-moment comparison would need an unamplified loss below
\(0.18010287536465091825\ldots\) at the active inherited geometry.
That number is a necessary consumer comparison, not a proved moment
loss or an interval certificate.

[RECTANGULAR_EXPONENT_OBSTRUCTION.md](RECTANGULAR_EXPONENT_OBSTRUCTION.md)
gives a feasible size-exponent model for the currently used
repetition/Gram inequalities.
[M2_CAPACITY_AND_RECIPROCAL_CHECKS.md](M2_CAPACITY_AND_RECIPROCAL_CHECKS.md)
identifies the exact capacity-limiting M2 edge and the costs of
reciprocal truncation. These are limitations of the specified
estimates, not arithmetic counterexamples or impossibility theorems.

## 4. Relevant repository work checked in this pass

The recent PR list and branch heads were refreshed on 24 October 2026
before this publication. Their statements are not strengthened here.

| Work | Relevance to this pass | Remaining requirement |
| --- | --- | --- |
| [PR #1019](https://github.com/GettysburgResearch/riemann/pull/1019), head 3bcc1daa | Its natural-label result controls the actual projected Möbius vector; its physical quartic calculation uses the correct cube numerator. | The complementary projection and full inverse consumer are still needed. The annular quartic cost is retained. |
| [PR #1015](https://github.com/GettysburgResearch/riemann/pull/1015) | Its complete primitive pairing gives a scalar improvement and a finite operator estimate. | Neither statement supplies the continued complementary inverse expression. |
| [PR #1014](https://github.com/GettysburgResearch/riemann/pull/1014) | It records a precise native inverse-moment input sufficient for the conditional \(0.874\) target. | That stronger input remains unproved and is not supplied by the new rectangular theorem. |
| [PR #1018](https://github.com/GettysburgResearch/riemann/pull/1018), head 591c880b | The shifted-center detector cancels the local counts and yields a source-dependent classical-form region. | Its own scope is a secondary classical result; it does not lower the fixed half-plane boundary. |
| [PR #1012](https://github.com/GettysburgResearch/riemann/pull/1012) | Its proposed all-unitary orbit theorem is a possible supplier of the explicit \(\mathrm{ZF}_\beta\) premise. | This packet does not independently certify its complete boundary argument. |

The source-qualified numerical benchmark is
[Liu, arXiv:2610.26835v1, Theorem 17.1](https://arxiv.org/html/2610.26835v1).
The new coefficient and rectangular theorems are conditional
deductions from the exact source chain in [SOURCES.json](SOURCES.json).

## 5. Review and finite validation

The mathematical files were independently checked locally before
freezing. A separate review-only successor records the exact remote
mathematical commit, file hashes, reviewer authorship boundaries, and
remaining gaps. The source files are not edited to incorporate later
review receipts.

The finite checker
[check_cube_amplification.py](check_cube_amplification.py) works
exactly in a formal \(\mathbb Z[\omega]\) reciprocity model. It checks:

- 27 multiplicativity and normalization pairs;
- 6,912 complete cube-amplification identities with zero masks;
- 1,331 divisor-square fibre bounds;
- 174 instances rejecting omission of the required divisor in the row.

Ordinary and optimized Python produce identical reports, matching
[cube_amplification_report.json](cube_amplification_report.json).
The checker authenticates those finite formal identities. It does
not evaluate primitive Gauss sums, prove an analytic estimate, or
certify a zero-free region.

~~~sh
python3 -I -S -B check_cube_amplification.py
python3 -I -S -B -O check_cube_amplification.py
~~~
