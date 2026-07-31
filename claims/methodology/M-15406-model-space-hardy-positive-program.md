# M-15406 — Positive completion through the model-space pole defect

Claim ID: `M-15406`  
Title: Replace bulk prime-pair cancellation by a proof that the anti-inner pole packet vanishes  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `L-15416`, `T-15407`, `R-15402`; Suzuki's meromorphic-inner criterion for `Theta_omega`  
Scope: positive-only completion of Issue #180  
Related counterexample candidates: none

## Corrected final target

`T-15407` proves the unconditional renormalized estimate

\[
 \sup_{0<\sigma\le1/2}
 \frac{\sigma}{2\pi}
 \int
 |f_h(\sigma+it)-P_+(\sigma+it)|^2dt<\infty,
 \tag{M-15406.1}
\]

where `P_+` is the exact principal-part packet of centered zeros with positive
real part.

Thus the original positive goal is now exactly

\[
 \boxed{P_+=0.}
 \tag{M-15406.2}
\]

There is no remaining diffuse Hardy defect to estimate.

## Equivalent positive interfaces

The following are the same obstruction in different coordinates.

### 1. Pole Gram

For every finite right-zero packet, certify that its positive Cauchy Gram is
zero. Since its diagonal is strictly positive whenever a residue is nonzero,
this is equivalent to absence of the packet.

### 2. Suzuki meromorphic inner function

For

\[
 \Theta_\omega(z)=
 \frac{\xi(\frac12-\omega-iz)}
      {\xi(\frac12+\omega-iz)},
 \tag{M-15406.3}
\]

boundary modulus one is automatic. The required theorem is analyticity and
innerness in the upper half-plane for every `omega>0`. A denominator zero in
the upper half-plane is exactly a member of `P_+` lying to the right of the
line `Re s=1/2+omega`.

### 3. Hankel anti-causal component

Let `H^2` be the upper-half-plane Hardy space and let

\[
 \mathsf H_\omega=P_-M_{\Theta_\omega}|_{H^2}
 \tag{M-15406.4}
\]

be the Hankel component of boundary multiplication by `Theta_omega`. Then

\[
 \boxed{
 \mathsf H_\omega=0
 \quad\Longleftrightarrow\quad
 \Theta_\omega H^2\subset H^2
 \quad\Longleftrightarrow\quad
 \Theta_\omega\text{ is inner}.}
 \tag{M-15406.5}
\]

A positive proof may therefore target one operator norm equal to zero rather
than a growing prime-pair sum.

### 4. Phase-vortex energy

`L-15416` gives

\[
 \left|\frac{\xi'}{\xi}
  (\tfrac12+\omega-it)\right|^2
 =\frac14\left(
 |\partial_t\log\Theta_\omega(t)|^2
 +|\partial_\omega\log\Theta_\omega(t)|^2
 \right).
 \tag{M-15406.6}
\]

The desired Hardy bound is finite weighted phase Dirichlet energy. A right-zero
is an interior vortex and contributes the divergent pole Gram.

### 5. Localized Weil/cardinal defect

The Xi-cardinal work in the wider stack assigns one exact indefinite block to
every off-line conjugate pair. Excluding that block is the localized-form
version of (M-15406.2).

## Four viable proof mechanisms

### A. Causal support theorem for Suzuki's kernel

Construct the inverse Fourier/Mellin kernel of `Theta_omega` for every
`omega>0` and prove it has the one-sided support required by innerness. For
large `omega` this follows from absolutely convergent arithmetic expansions;
the load-bearing theorem is uniform continuation through `0<omega<1/2` without
assuming a zero-free strip.

A certificate must preserve support, not merely show numerical smallness on the
wrong side.

### B. Collectively compact anti-Hardy family

Embed the anti-causal ranges of `H_omega` in one Hilbert space. Prove:

1. strong convergence to zero on a dense exact arithmetic core;
2. collective compactness of the complete anti-Hardy family as
   `omega downarrow 0`.

Then the collective-compactness lemma from the positive localized-Weil stack
would force operator-norm convergence to zero. A false-RH pole produces an
escaping exponential mode and necessarily violates collective compactness.

### C. Positive canonical Hamiltonian

Extend Suzuki's explicit canonical-system construction to every `omega>0` and
certify the Hamiltonian positive semidefinite. The phase-gradient identity
(M-15406.6) supplies the direct energy bridge to the Hardy target.

Finite matching digits or positivity at finitely many `omega` values do not
establish this cofinal theorem.

### D. Residue-forcing arithmetic identity

Use `L-15415` to compute the reflected bulk through the derivative, Selberg,
and archimedean streams. Derive a second arithmetic inequality with the exact
sign

\[
 0\ge \mathcal G_+(\sigma),
 \tag{M-15406.7}
\]

where `mathcal G_+` is the positive Cauchy pole Gram. Positivity would then force
`mathcal G_+=0` and close RH.

The missing inequality must include the full contour ledger; a residue-free
bulk estimate is refuted by `R-15402`.

## Proof-producing finite interfaces

### Pole-Gram checker

For declared algebraic or rational pole boxes and residue boxes, verify

\[
 C_\sigma(j,k)=
 (2\sigma-\overline a_j-a_k)^{-1}
 \tag{M-15406.8}
\]

and exact positive quadratic values. This is implemented synthetically in
`X-15408`.

### Hankel support checker

A finite packet binds:

1. exact `omega`;
2. a directed kernel representation for `Theta_omega`;
3. a split into causal and anti-causal cells;
4. a rigorous anti-causal norm;
5. a common-frame tail modulus across an `omega` interval.

Only a symbolic/cofinal zero anti-causal bound proves RH.

### Phase-energy checker

Use one compact rational symmetric profile and directed values of
`partial_t log Theta` and `partial_omega log Theta`. The checker verifies the
identity (M-15406.6) and a complete cellwise energy enclosure. Finite energy at
finitely many offsets remains a control, not a proof.

## No-go tests for proposed positive proofs

Reject any argument which:

- uses only `|Theta_omega(t)|=1` on the real boundary;
- replaces the reflected product by the Hardy modulus off the center line;
- drops crossed zero residues;
- bounds the Selberg stream termwise and calls the result the Hardy norm;
- proves compactness separately at each `omega` but not collective compactness;
- establishes the bound only for `omega>=omega_0>0`;
- invokes the zero-side expansion under RH to prove the prime-side bound.

## Immediate research tasks

1. Derive the exact relation between the filtered pole Gram and the defect
   operator `H_omega^*H_omega`.
2. Compute the anti-causal kernel for the eta ratio-8 window and search for a
   positivity-preserving renewal representation.
3. Test whether the von Mangoldt upward/downward adjoint pair supplies a common
   compactness modulus.
4. Translate the Xi-cardinal off-line block into the same Cauchy/model-space
   coordinates and compare the two exact Gram matrices.
5. Audit Suzuki's kernel construction to identify precisely which estimate uses
   `omega>1` and whether the compact filter removes that restriction.

## Honest proof boundary

The renormalized Hardy defect has been bounded. The unrenormalized bound and the
bounded mean square remain unproved because (M-15406.2) remains unproved.
Equation (M-15406.2) is not a technical tail estimate; it is exactly the
Riemann hypothesis.
