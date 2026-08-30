# Archimedean one-sided ladders: gamma divisors and the parity boundary

Status: **exact local calibration and obstruction; classical analytic inputs;
not a new arithmetic realization or a novelty claim**.

Scope: real `GL(1)` unitary types; complex shifts of real gamma factors;
finite virtual gamma products with integer multiplicities; an explicit
infinite-dimensional polynomial ladder.  No global completion, epsilon
factor, explicit-formula theorem, RH, or GRH is proved.

Exact programme source: issue [#763](https://github.com/gfreund123/riemann/issues/763),
lane `M2/ARCHRIGID`, at repository commit
`6675c19f20760301d8c91dedc4a7836170003512`.  This packet does not depend on the
unproved finite-place geometric gates.

What was actually run: the companion bounded exact replay checks rational
shift reduction, pole-divisor tails, all binary parity pairs and triples,
finite basis intertwining, dual defects, and the real/complex ladder split.
It does **not** computationally certify analytic continuation or an infinite
determinant.  Those steps have proofs below using the stated classical input.

Smallest remaining gap: a canonical arithmetic/archimedean carrier that
explains these boundary maps and compatible finite-place operations without
choosing them to reproduce prescribed local factors.

## 1. Normalization and imported facts

Fix real positive logarithms of `pi` and `2 pi`, and put

\[
 \Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),\qquad
 \Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s).
\]

Different conventions for the constant in `Gamma_C` exist; this one is used
throughout.  The following facts are imported, not discovered here:

- Gamma has simple poles at the nonpositive integers and no zeros
  ([NIST DLMF 5.2](https://dlmf.nist.gov/5.2)).
- Its shift and duplication identities are classical
  ([DLMF 5.5.1 and 5.5.5](https://dlmf.nist.gov/5.5)).
- The Hurwitz zeta continuation satisfies
  `zeta_H(0,a)=1/2-a` and
  `zeta_H'(0,a)=log Gamma(a)-(1/2)log(2 pi)` for `a>0`
  ([DLMF 25.11.13 and 25.11.18](https://dlmf.nist.gov/25.11)).
  Holomorphic continuation extends the latter identity to `Re(a)>0`,
  with the logarithm continued from the positive axis.

Consequently, as meromorphic identities,

\[
 \frac{\Gamma_{\mathbb R}(s+2)}{\Gamma_{\mathbb R}(s)}
 =\frac{s}{2\pi},\qquad
 \Gamma_{\mathbb R}(s)\Gamma_{\mathbb R}(s+1)
 =\Gamma_{\mathbb C}(s).
\tag{1.1}
\]

Regularized determinant descriptions of archimedean factors are established
territory.  For example, Connes--Consani construct a much richer cyclic
homology realization in
[*Cyclic homology, Serre's local factors and the lambda-operations*](https://arxiv.org/abs/1211.4239).
The elementary ladder below is a calibration model, not a replacement for
that theory and not evidence of an unexplored ontology.

## 2. `ARCHLADDER-1`: the exact finite-rank divisor obstruction

Let `J` be finite, let `mu_j` be arbitrary complex numbers, and let `m_j` be
integers.  Define the nonzero meromorphic function

\[
 F(s)=\prod_{j\in J}\Gamma_{\mathbb R}(s+\mu_j)^{m_j}.
\]

For each coset `c` in `C/(2 Z)`, let
`M_c=sum_{mu_j in c} m_j`.  Then

\[
 \boxed{F\text{ is rational in }s
 \quad\Longleftrightarrow\quad M_c=0\text{ for every coset }c.}
\tag{2.1}
\]

The same coset condition is necessary for
`F=E R`, where `R` is a nonzero rational function and `E` is an entire
nowhere-zero function.

**Proof.** In a fixed coset choose one representative `mu`.  Repeated use of
(1.1) expresses every factor in that coset as a rational function times
`Gamma_R(s+mu)^{m_j}`.  Thus `M_c=0` in every coset is sufficient.

For necessity, write the shifts in one coset as `mu+2k_j`, with integer
`k_j`.  At `s=-mu-2N`, for every sufficiently large integer `N`, all the
factors in this coset have a simple pole before exponentiation.  The divisor
order of their product is exactly `-M_c`.  Other cosets have no divisor
there: their pole progressions are disjoint.  A nonzero `M_c` therefore gives
infinitely many zeros or poles.  A rational function, even multiplied by an
entire nowhere-zero factor, cannot have that divisor.  This proves both
claims.  The empty product is correctly included as `F=1`.  QED.

For integral shifts, (2.1) is the pair of conditions that the total even-shift
multiplicity and the total odd-shift multiplicity both vanish.  Cancellation
of the *total* multiplicity alone is insufficient:
`Gamma_R(s+1)/Gamma_R(s)` is not rational.

Every nonempty **effective** product (`m_j>=0`, at least one positive) fails
(2.1).  Hence it cannot equal a finite product or quotient of determinants
of fixed finite-dimensional affine operator pencils, even up to a
nowhere-zero entire normalization.  Such determinants are polynomials;
their quotients are rational.  This excludes only this fixed finite-rank
model class, not a matrix with gamma functions deliberately inserted into
its entries, infinite rank, regularization, or nonlinear spectral changes.

Virtual products are an essential exception, not a loophole to hide:

\[
 \Gamma_{\mathbb R}(s+2)/\Gamma_{\mathbb R}(s)=s/(2\pi).
\]

## 3. `ARCHLADDER-2`: a carrier with a literal boundary

Let `A=C[u]` and, for any complex `mu`, let `F_mu=A e_mu` carry the connection

\[
 \Theta_\mu=-2u\frac{d}{du}-\mu.
\]

It is rank one over `A` but infinite-dimensional over `C`.  Its distinguished
basis `u^n e_mu`, `n>=0`, has eigenvalues `-(2n+mu)`.  On the completion with
this basis orthonormal the diagonal operator has its natural closed domain;
the polynomial module is an invariant core.  No zeros of an arithmetic
`L`-function are used to define it.

Multiplication by `u` is an intertwining injection, giving the exact sequence

\[
 0\longrightarrow F_{\mu+2}
 \xrightarrow{\ u\ } F_\mu
 \longrightarrow C_\mu\longrightarrow0,
\tag{3.1}
\]

where `Theta` on the one-dimensional quotient is `-mu`.  Thus the gamma
shift has an actual missing boundary state, not an added scalar correction.
For real `t>0`, the convergent heat trace is

\[
 H_\mu(t)=\operatorname{Tr}(e^{t\Theta_\mu})
 =\frac{e^{-\mu t}}{1-e^{-2t}},\qquad
 H_\mu(t)-H_{\mu+2}(t)=e^{-\mu t}.
\tag{3.2}
\]

### Exact regularization, including the constant

Initially assume `Re(s+mu)>0`.  On principal powers continued from positive
`s+mu`, the spectral zeta of `(s-Theta_mu)/(2 pi)` is

\[
 Z_\mu(w;s)
 =\sum_{n\ge0}\left(\frac{s+\mu+2n}{2\pi}\right)^{-w}
 =\pi^w\zeta_H\left(w,\frac{s+\mu}{2}\right),\quad \Re w>1.
\]

Define `det_zeta=exp(-partial_w Z_mu(0;s))`.  The imported Hurwitz identities
give, by direct substitution,

\[
 \boxed{\det_\zeta\left(\frac{s-\Theta_\mu}{2\pi}\right)
       =\frac{\sqrt2}{\Gamma_{\mathbb R}(s+\mu)}.}
\tag{3.3}
\]

The reciprocal-gamma expression supplies its entire continuation in `s`.
The normalized inverse determinant is `sqrt2/det_zeta`, not `1/det_zeta`.
Direct sums multiply determinants.  We make no general multiplicativity
claim for regularized determinants of operator *products*.

The disjoint spectra of `F_mu` and `F_{mu+1}` interlace into the spacing-one
ladder `-(n+mu)`, `n>=0`.  Its determinant is
`(2 pi)^{s+mu}/Gamma(s+mu)=2/Gamma_C(s+mu)`.
Thus the normalization in (1.1) agrees with the literal direct-sum split,
including the constants `sqrt2 * sqrt2 = 2`.

## 4. `ARCHLADDER-3`: parity tensor and duality have the same defect

For the real unitary character

\[
 \chi_{\epsilon,t}(x)=\operatorname{sgn}(x)^\epsilon |x|^{it},
 \quad\epsilon\in\{0,1\},\ t\in\mathbb R,
\]

use the standard local factor `Gamma_R(s+epsilon+it)` and assign the ladder
`F_{epsilon+it}`.  Character tensor and dual are

\[
 (\epsilon,t)\otimes(\eta,v)
 =(\epsilon\mathbin\oplus\eta,t+v),\qquad
 (\epsilon,t)^\vee=(\epsilon,-t),
\tag{4.1}
\]

where `oplus` is addition modulo two.

Ordinary tensoring over `C` is **not** the desired operation on ladders.
The sum operator on `F_mu tensor_C F_nu` has eigenvalue
`-(2k+mu+nu)` with multiplicity `k+1`, rather than one.  This already fails
for two even types.  Matching gamma determinants does not fix tensor type.

Balanced tensoring over `A`, with the induced connection, does give

\[
 F_\mu\otimes_A F_\nu\simeq F_{\mu+\nu}.
\tag{4.2}
\]

The sum connection is well-defined by the Leibniz rule.  Set
`c(epsilon,eta)=epsilon eta`.  Since
`epsilon+eta=(epsilon op eta)+2c`, multiplication by `u^c` defines a
canonical intertwining map

\[
 F_{\epsilon+it}\otimes_A F_{\eta+iv}
 \longrightarrow F_{(\epsilon\oplus\eta)+i(t+v)}.
\tag{4.3}
\]

It is an isomorphism unless both types are odd.  In the odd--odd case its
cokernel is the single boundary state of eigenvalue `-i(t+v)`.
Associativity is exact, not a fitted pairwise rule, because

\[
 c(\epsilon,\eta)+c(\epsilon\oplus\eta,\kappa)
 =c(\eta,\kappa)+c(\epsilon,\eta\oplus\kappa).
\tag{4.4}
\]

Both sides equal `floor((epsilon+eta+kappa)/2)`.  The even trivial type is
the unit and the maps are symmetric.  This defines a **lax**, not strong,
monoidal assignment on the category of these types and scalar maps.
Extension by finite direct sums is allowed; no representation category
beyond this specified one is asserted.

Likewise the `A`-linear connection dual of `F_mu` is `F_{-mu}`.  For an odd
type, the character dual ladder is instead `F_{-mu+2}`.  The natural map
from the character dual ladder into the connection dual is multiplication
by `u^epsilon`.  Equivalently, evaluation

\[
 F_{\epsilon+it}\otimes_A F_{\epsilon-it}\longrightarrow A
\]

is multiplication by `u^epsilon`; it is perfect only for even types.
Its odd cokernel is the same one-dimensional boundary.  Hence duality,
parity carry, and the finite gamma quotient (1.1) record one exact defect.

After localization to `C[u,u^{-1}]` the maps become invertible.  But the
spectrum becomes two-sided and the positive-time heat trace in (3.2)
diverges.  The particular one-sided regularization in (3.3) no longer
applies.  Localization is therefore not a free repair that preserves all
the analytic data.  This does not exclude a different, justified
two-sided regularization.

## 5. Why this is a useful firewall, and what it does not settle

One upstream polynomial grading simultaneously gives the gamma shift,
parity interlacing, a regularized determinant, and compatible tensor/dual
boundary maps.  The type operations were not replaced by multiplication of
scalar gamma factors: local factors multiply under **direct sum**, not
under tensor.  A rule demanding scalar tensor multiplicativity would even
fail at the tensor unit, whose local gamma factor is not one.

The bounded held-out checks are the eight triple-parity cases, nonzero
spectral twists, backward and fractional virtual gamma shifts, and the
spacing-one ladder split.  They check exact algebra only; they do not
turn this classical model into an arithmetic source.

This closes the proposed *finite affine determinant* version of `ARCHRIGID`
and isolates the failure of a particular naive strong-tensor model.  It
does not classify all archimedean categories or rule out a different
infinite-dimensional strongly functorial construction.  To promote this
lane, a later result must explain the boundary through an independently
motivated geometric object and bind its local operations to finite places
and an explicit-formula trace law.  Merely rephrasing (3.3) is not enough.

## 6. Reproduction and source boundary

From the repository root:

```text
python research/riemann-structures/archimedean_ladder_boundary.py --check
python -O research/riemann-structures/archimedean_ladder_boundary.py --check
python -m unittest discover -s tests -p test_archimedean_ladder_boundary.py
python -O -m unittest discover -s tests -p test_archimedean_ladder_boundary.py
```

The source manifest authenticates the *frozen* programme blob, not the
mutable current programme map.  External analytic references are explicitly
imported assumptions; the replay does not download or certify them.
Rational-shift fixtures are exact `Fraction` arithmetic.  The proof of
(2.1), not a finite scan, covers arbitrary complex shifts and every finite
list.  No numerical gamma or zero calculation is used.
