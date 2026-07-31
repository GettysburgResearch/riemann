# Research report — cardinal defect completion of the finite visible block

Agent: `gpt56-02-o`  
Date: 2026-07-31  
Stack: PR #163 / Issue #156  
Status: exact finite-block reduction; no proof of RH

## Objective

The requested final implication asks for one packet sequence that simultaneously
captures the positive weighted symbol deficit and has vanishing localized
compression and cross residual:

\[
 \eta_j(L_j,G_j)\le G_j/2,\qquad
 \alpha_j\to0,\qquad
 \beta_j^2/G_j\to0.
\]

The current repository had separated the low packet into a radical-like
zero-evaluation near-kernel and an evaluation-visible block.  The latter still
appeared to require a direct cofinal positivity theorem.

## Main discovery

The completed zeta function itself supplies exact cardinal defect vectors.

For every distinct centered zero `omega`, define

\[
 K_\omega(z)
 =
 \frac{\Xi(z)}
 {(\Xi^{(m_\omega)}(\omega)/m_\omega!)
  (z-\omega)^{m_\omega}}.
\]

It equals one at `omega` and zero at every other distinct zero.  The polarized
Weil form therefore has exact Gram

\[
 Q_W(k_\omega,k_\nu)
 =m_\nu\,1_{\nu=\overline\omega}.
\]

A real centered zero gives one positive coordinate.  An off-line conjugate pair
gives the exact block

\[
 m\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]

and the vector difference has value `-2m`.

This turns the vague “visible block” into a completely diagonalized defect
space.

## Positive critical-line deflation

For a finite proof-grade real-zero set `Z`, subtract

\[
 Q_Z(f,g)
 =
 \sum_{\gamma\in Z}
 m_\gamma\overline{\widehat f(\gamma)}\widehat g(\gamma).
\]

The subtraction is positive.  Every line-cardinal `k_gamma` then becomes an
exact radical of the residual form.  Exact Connes--Consani `E`-range vectors
remain radicals because their transforms vanish at every zeta zero.

Therefore the finite packet can be enlarged by the cardinal vectors of already
certified line zeros.  Their localization errors are tail errors, not unknown
finite signs.  The original form is larger than the residual form, so any lower
floor proved after deflation lifts back to the original operator.

This completes the finite critical-line-visible block conceptually.

## Correct cofinal theorem

Let

\[
 \widetilde D_j=D_{j,G_j}+Q_{Z_j,j}
\]

and let `L_j` be a localized packet of exact residual radicals.  If

\[
 \eta_j
 =
 \operatorname{Tr}((I-P_{L_j})\widetilde D_j)
 <G_j,
\]

then the residual complement floor is

\[
 \Gamma_j=G_j-\eta_j.
\]

With packet block and cross bounds `alpha_j,beta_j`, block Schur gives

\[
 F_j\ge
 -\alpha_j-\frac{\beta_j^2}{G_j-\eta_j}.
\]

In particular,

\[
 \eta_j\le G_j/2,\quad
 \alpha_j\to0,\quad
 \beta_j^2/G_j\to0
\]

imply `F_j->0-`.

## Exact obstruction to the final trace theorem

Nonresonant periodized `E`-range density is only an `L2` statement.  If an
off-line zero exists, its cardinal difference `v` has

\[
 Q_W(v,v)=-2m<0
\]

and a finite weighted tail norm.  Were `v` approximable by exact global
`E`-radicals with simultaneously vanishing exterior form tail, form continuity
would force `Q_W(v,v)=0`, a contradiction.

Thus local `L2` approximants can exist only with escaping exterior form norm.
The desired simultaneous theorem is not an automatic strengthening of density;
it must eliminate the off-line defect itself.

## Exact checker

`X-15604` verifies the cardinal Gram, inertia, positive line deflation, off-line
negative witness, and a generic Schur floor with Fraction-only arithmetic.

Retained proof digests:

```text
critical-line residual control
dd98782fc79a3049846529fa4a0c539505528516d2e1c2791836c6bf6dda43a3

off-line-pair control
965202da2f7471353f6d9667b71551730912c3fad383967fc9a2acc604bcf48a
```

Ten adversarial tests pass.

## Final status

The path is narrowed further:

```text
finite certified line-visible block       solved by positive deflation
fixed finite packet localization tails    solved
block Schur composition                    solved
cofinal positive-defect trace saturation  unresolved
off-line cardinal defect exclusion         exactly the RH-bearing step
```

No full proof of RH has been obtained.  Any honest completion must now prove that
the positive defect packet captures the weighted localization trace cofinally,
or otherwise exclude the exact off-line cardinal signature block.
