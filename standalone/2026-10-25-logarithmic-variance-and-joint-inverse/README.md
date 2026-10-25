# A weaker spectral target and the actual joint inverse remainder

25 October 2026. Status: proposed research mathematics with separate
independent agent reviews. **No improved zero-free boundary is established.**

This third pass changes the spectral target substantially. It allows the
signed second moment of the legal finite resolvent to grow like
\(a/\log a\), removes physical nonnegativity, and uses only order
\(a\log a\) Fourier modes. On the arithmetic side it proves an estimate
for the complete inverse--von Mangoldt convolution and pays the
one-annulus prime-square correction. The squarefree divisor-weighted
inverse remains the unresolved part of that attack.

These additions preserve the earlier two packets and every integrated
claim. They extend PR #1021 from mathematical commit
0f07049ff1e8cc7765f6de01b4e176ad627bba4b and its publication-review head
9b6aaaf8b969cdb55b909a5bd5d5e949dc49f154. The exact dependencies are in
[SOURCES.md](SOURCES.md); review reports identify the bytes they assessed.

## 1. Main result: the variance may grow

Let \(T_a\) be the exact full trigonometric compression of the complete
Weil form on \([-a,a]\), retaining all prime powers through \(e^{2a}\),
both pole terms and the archimedean term. Use

\[
N_a=\lceil4a\log a\rceil,\qquad
u_a=(T_a-\kappa_a)^{-1}1,\qquad f_a=u_a/\int u_a,
\]

where \(\kappa_a\) lies strictly below the **full** finite minimum,
including both parity blocks.

The main [logarithmic-variance theorem](spectral/LOGARITHMIC_VARIANCE_SELECTOR.md)
proves the implication

\[
\boxed{
\int_{-a}^{a}x^2f_a(x)\,dx\le \frac{a}{10\log a}
\quad\text{for every sufficiently large integer }a
\quad\Longrightarrow\quad {\rm RH}.
}
\]

The signed moment is nonnegative because the normalized entire
resolvents have only real zeros. No physical sign condition is imposed.
The inequality concerns the actual source resolvents, not arbitrary
functions in the finite space.

| Interface | Earlier sufficient condition | This packet |
| --- | --- | --- |
| Physical density | Nonnegative, with tight mass | May change sign |
| Second moment | A uniform bound sufficed for tightness | May grow up to \(a/(10\log a)\) |
| Explicit mode schedule | \(N_a=\lceil a^3\rceil\) in the published finite positive-selector consumer | \(N_a=\lceil4a\log a\rceil\) |
| Source identification | Already unnecessary under the prior positive-selector conditions | Still unnecessary |
| Shift condition | Exact finite legality | Exact legality below the full finite minimum |
| Still unproved | All-scale source selector existence and its required bounds | All-scale source selector satisfying the displayed growing-variance inequality |

The last row remains a substantive mathematical problem. This table
does not promote that open hypothesis to an achieved estimate.

### Why the new argument works

Every degree-\(N\) trigonometric transform has compulsory zeros at
\(\pm m\pi/a\) for \(m>N\). Removing these zeros from the paired canonical
product uses part of its second-moment budget. At the stated schedule,
the remaining budget is small enough that every sampled coefficient
satisfies

\[
|F_a(n\pi/a)|\le1\quad(|n|\le N_a),\qquad
\|f_a\|_1\le2N_a+1.
\]

This is a polynomial total-variation bound for a potentially signed
density. Gaussian smoothing of the actual positive theta annihilator
then gives a positive overlap of size at least \(c/\sqrt{M_a}\), where
\(M_a=a/(10\log a)\). Its complete-source residual decays at the much
faster rate \(\exp(-c'a\log a+O(a))\). A broad null comparator and the
exact resolvent minimum force \(\kappa_a\to0\).

A separate fixed test closes the finite consumer:

\[
G(z)=\exp(1-\cosh(z/10)).
\]

Its inverse transform decays exponentially fast enough in physical
space, while \(G\) has doubly exponential decay along the real axis.
This permits faithful approximation on the \(a\log a\) Fourier grid.
Its nonvanishing at every complex zero preserves the residues in the
Laplace zero detector. The proof never treats a finite Galerkin
minimum as a lower bound for the continuum operator.

The companion
[bounded signed-selector proof](spectral/SIGNED_GAUSSIAN_SELECTOR.md)
gives the earlier stage of the argument, including a quantitative
quadratic-grid spectral-growth consumer. Both notes explicitly verify
that the compulsory zeros do not make their variance targets vacuous.
The compatible cosine-power examples do not solve the source equation.

The reduced mode count concerns Fourier dimension. The complete prime
sum still reaches \(e^{2a}\); no computational complexity breakthrough
or finite numerical proof of the all-scale condition is claimed.

## 2. An actual full-source lower estimate

The [prime-discrepancy spectral floor](spectral/PRIME_MODEL_SPECTRAL_FLOOR.md)
proves, for the full or even finite matrix,

\[
\lambda_{\min}(T_{a,N})\ge
b_*-2\left(\frac{\pi N+(2N+1)/2}{a}+\frac12\right)
\int_0^{2a}|\psi(e^u)-e^u+1|e^{-u/2}\,du,
\]

where \(b_*=4-\gamma-\pi/2-3\log2-\log\pi\).
The growing half of the pole kernel cancels the continuous main term of
the prime measure exactly. Its remaining multiplier is
\(\Re\psi_\Gamma(5/4+it/2)-\log\pi\).

This is an unconditional inequality in terms of the actual prime
discrepancy. The cited explicit prime number theorem gives a factor
\(\exp(-c a^{3/5}/(\log a)^{1/5})\) beyond the older crude exponential
floor on polynomial schedules. This saving is imported from known prime
cancellation; it does not imply a new constant zero-free half-plane.
An input discrepancy exponent \(\beta\) is returned as the same
\(\beta\), not a smaller one.

The exact signed remainder before absolute values is recorded. Any
improvement through this route must use its autocorrelation structure,
rather than recycling the same pointwise prime bound.

## 3. The inverse and prime factors can be combined exactly

The [joint logarithmic-derivative note](native/JOINT_LOG_DERIVATIVE.md)
retains the original Eisenstein physical rows, both orientations,
natural zeros, common punctures, fixed ray factors and common height.
The complete convolution satisfies

\[
\mu_E*\Lambda_E=-\mu_E\log N.
\]

Consequently its normalized moment at total length \(Y\) inherits

\[
(1+\log Y)^2
\left[U+U^{1/6}Y^{5/6}\right]
\]

up to the source's prescribed small powers, height factor and profile
seminorm. It also inherits PR #1022's capped estimate at that estimate's
licensed lengths. All divisor ranges and all prime powers must be
reassembled before using this identity.

For sufficiently large \(Y\) on the fixed annular support, the adapter
is reversible by dividing the common profile by \(\log(Yx)\).
It therefore does not create a better inverse exponent by
itself. Its possible use requires a stronger detector lower bound for
the complete signed sum.

Opening one aligned inverse/prime annulus instead leaves a squarefree
divisor-weighted Möbius polynomial and a prime-square correction.
The latter now has the paid source-dependent estimate

\[
\sum_u w(u)|\mathcal E_u|^2
\ll (UDL)^\epsilon(1+|v|)^A
\left[U+U^{1/6}(D/L)^{5/6}\right]
\]

with the fixed common profile factors as specified in the proof.
Thus prime squares are not the obstruction at the critical short
lengths. The remaining squarefree weight depends on the factorization
of the column. The native source theorem does not license its insertion
merely because it has bounded divisor multiplicity.

The note also proves why counts cannot improve themselves by a
density-to-moment-to-density cycle using only the same marginal bounds.
The target class contributes its own count back into every generated
moment. A new signed estimate or a genuine nonsaturation argument is
required to start a strict improvement.

## 4. A fresh curve encoding, with its cost kept visible

The [Jacobi transfer](fractional/JACOBI_NORM_TRANSFER.md) gives an exact
norm-profile encoding of the native Möbius coefficient:

\[
\mu(n)=\sum_{x\in\mathcal O}
\Phi(Nx/Nn)\,
\chi_n\!\left(x^2(x+1)^4\right)^\epsilon
\quad(n\text{ good and squarefree}).
\]

It preserves the common norm frequency and moves the ordinary row to
\(u x^2(x+1)^4\). The local identity and radial completion are proved
directly. Applying the available ordinary moment after freezing the
curve variable pays \(UD^3\), worse than the trivial bound, even on the
qualified nonprincipal subfamily. Short completion creates new additive
trace coefficients not covered by that ordinary theorem. The note
records this exact failed transfer so it is not mistaken for a free
route from an ordinary coefficient to the inverse.

## Review and next mathematical work

The proofs were checked by agents other than their authors and by the
coordinator. Reviews bind to SHA256 hashes and state their imported
premises. They prompted repairs to a missing parameter hypothesis, an
error-sum sign, and two finite endpoint conventions. These are internal
analytic reviews, not external peer review or formal proof verification.
No new numerical experiment is presented as evidence for a global
claim. The manifest binds the proof and review files.

The strongest unresolved targets after this pass are:

1. Prove the actual legal resolvent family satisfies the growing bound
   \(V_a\le a/(10\log a)\), or obtain a uniform lower bound on the same
   complete finite matrices.
2. Bound the actual squarefree, prime-divisor-weighted Möbius polynomial
   at the critical coupled lengths, or construct a detector lower bound
   for its signed complete reassembly. The critical class and exact
   lengths are in the joint note.

The imported working boundary \(0.874886647039964\ldots\) is unchanged.
None of the new conditional spectral statements independently certifies
that imported preprint or supplies a stronger region.
