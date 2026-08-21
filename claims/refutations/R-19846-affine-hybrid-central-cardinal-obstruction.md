# R-19846 — An off-line Xi-cardinal direction obstructs the affine hybrid profile gate

Claim ID: `R-19846`  
Status: **PROVED CONDITIONAL OBSTRUCTION — FALSE RH FORCES FAILURE OF THE FINAL AFFINE GATE**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-07  
Dependencies: Xi-cardinal defect theorem `L-15613`; exact Xi radical target `L-19849`; hybrid residual gap `L-19862`; affine ground transfer `L-19861`; continuity of the Weil form in the declared Hardy/form topology  
Scope: adversarial audit of the final analytic theorem in `T-19813`

## 1. Purpose

`T-19813` reduced the positive finite route to one source-specific affine estimate

\[
 A_j-\sigma_j I\succeq c_jD_j,
 \qquad c_j>0,
 \tag{R-19846.1}
\]

together with the target-line upper bound

\[
 A_j(p_j,p_j)-\sigma_j
 \le C_j^{\rm tar}c_jm_j,
 \qquad
 m_j=D_j(p_j,p_j),
 \qquad
 C_j^{\rm tar}m_j\to0.
 \tag{R-19846.2}
\]

Here `p_j` is the normalized Xi target, while the exact hybrid residual Gram
satisfies

\[
 D_j|_{p_j^\perp}\succeq I,
 \qquad
 m_j\to0.
 \tag{R-19846.3}
\]

The present theorem proves that, if RH is false, (R-19846.1)--(R-19846.2)
cannot hold on any cofinal Hardy/form-dense diagonal.  Thus the remaining
source-specific profile theorem is not a routine normalization lemma.  In this
architecture it already excludes the exact off-line cardinal signature.

The argument does **not** claim that proving (R-19846.1)--(R-19846.2) would be
circular.  A new prime-side proof of those inequalities would be a proof of RH.
It does show that high-ordinate support averaging cannot by itself establish the
missing central block.

## 2. Off-line cardinal witness

Assume RH is false.  Let

\[
 \omega=\gamma+i\delta,
 \qquad \delta\ne0,
 \tag{R-19846.4}
\]

be a nonreal centered zero of `Xi`, of multiplicity `m_omega`.  Let
`k_omega,k_(bar omega)` be the cardinal vectors of `L-15613`, and put

\[
 h_\omega=k_\omega-k_{\bar\omega}.
 \tag{R-19846.5}
\]

The exact polarized Weil Gram gives

\[
 \boxed{
 Q_W(h_\omega,h_\omega)=-2m_\omega<0.}
 \tag{R-19846.6}
\]

Both cardinal vectors lie in every fixed Hardy strip below width `1/2`, so
`h_omega` belongs to the form topology used by the finite diagonal route.

Let `J_Xi=E(p_+)` be the exact global arithmetic radical whose transform is a
nonzero multiple of `Xi`.  Since `J_Xi` is a Weil radical,

\[
 Q_W(J_\Xi,g)=0
 \tag{R-19846.7}
\]

for every common form-domain vector `g`.

Orthogonalize the cardinal witness in the ordinary Hilbert metric:

\[
 h_\omega^\perp
 =h_\omega
 -{\langle h_\omega,J_\Xi\rangle
   \over\|J_\Xi\|^2}J_\Xi.
 \tag{R-19846.8}
\]

Then

\[
 h_\omega^\perp\perp J_\Xi,
 \qquad
 Q_W(h_\omega^\perp,h_\omega^\perp)=-2m_\omega.
 \tag{R-19846.9}
\]

Normalize once and put

\[
 u_\omega={h_\omega^\perp\over\|h_\omega^\perp\|},
 \qquad
 \kappa_\omega
 ={2m_\omega\over\|h_\omega^\perp\|^2}>0.
 \tag{R-19846.10}
\]

Thus

\[
 \boxed{Q_W(u_\omega,u_\omega)=-\kappa_\omega.}
 \tag{R-19846.11}
\]

## 3. Transfer to the growing finite spaces

Let `V_j` be the finite Fourier spaces of `T-19813`, with support and cutoff
tending cofinally.  The Xi target projections satisfy

\[
 p_j\longrightarrow {J_\Xi\over\|J_\Xi\|}
 \tag{R-19846.12}
\]

in the declared Hardy/form topology after zero extension and the common real
normalization.

The same Gevrey/Fourier density argument used in the finite-to-global Weil
criterion approximates `u_omega` by vectors in `V_j`.  Orthogonalizing those
approximants against `p_j` changes them by `o(1)`, because of
(R-19846.8) and (R-19846.12).  Therefore there are unit vectors

\[
 u_j\in V_j\cap p_j^\perp
 \tag{R-19846.13}
\]

such that

\[
 u_j\to u_\omega
 \tag{R-19846.14}
\]

in the form topology.  Consequently

\[
 \boxed{
 A_j(u_j,u_j)\longrightarrow-\kappa_\omega.}
 \tag{R-19846.15}
\]

In particular, for all sufficiently large `j`,

\[
 A_j(u_j,u_j)\le-\frac34\kappa_\omega.
 \tag{R-19846.16}
\]

The hybrid residual theorem gives the independent positive bound

\[
 \boxed{D_j(u_j,u_j)\ge1.}
 \tag{R-19846.17}
\]

No source-conditioning or alias estimate enters this step.

## 4. The Xi target has vanishing exact Weil value

Let `W_jp_j` denote the complete global-minus-finite residual of the exactly
normalized Xi lift.  `L-19862` gives

\[
 m_j=\|W_jp_j\|^2\to0
 \tag{R-19846.18}
\]

at an arbitrarily prescribed exponential rate.  The residual also tends to zero
in the common Hardy/form topology after the cutoff constant is enlarged.

Exact radicality gives

\[
 A_j(p_j,p_j)
 =Q_W(W_jp_j,W_jp_j).
 \tag{R-19846.19}
\]

Form continuity therefore yields

\[
 \boxed{A_j(p_j,p_j)\to0.}
 \tag{R-19846.20}
\]

This is the finite shadow of the exact identity
`Q_W(J_Xi,J_Xi)=0`.

## 5. Contradiction with the affine gate

Assume (R-19846.1).  Applying it to `u_j` and using
(R-19846.16)--(R-19846.17) gives

\[
 -\frac34\kappa_\omega-\sigma_j
 \ge c_j,
 \tag{R-19846.21}
\]

hence

\[
 \boxed{-\sigma_j\ge c_j+\frac34\kappa_\omega.}
 \tag{R-19846.22}
\]

By (R-19846.20), eventually

\[
 A_j(p_j,p_j)-\sigma_j
 \ge c_j+\frac12\kappa_\omega.
 \tag{R-19846.23}
\]

But the target upper bound (R-19846.2) says

\[
 A_j(p_j,p_j)-\sigma_j
 \le c_j\,[C_j^{\rm tar}m_j].
 \tag{R-19846.24}
\]

Since `C_j^tar m_j->0`, the right side is `o(c_j)`.  Equations
(R-19846.23)--(R-19846.24) are incompatible whether `c_j` tends to zero,
stays bounded, or tends to infinity:

- if `c_j` is bounded along a subsequence, the fixed term
  `kappa_omega/2` contradicts (R-19846.24);
- if `c_j` tends to infinity, divide by `c_j` to obtain `1<=o(1)`.

Therefore:

\[
 \boxed{
 \mathrm{RH\ false}
 \quad\Longrightarrow\quad
 \text{the affine hybrid gate fails cofinally}.}
 \tag{R-19846.25}
\]

Equivalently,

\[
 \boxed{
 \text{the complete affine gate of }T\text{-19813}
 \quad\Longrightarrow\quad
 \mathrm{RH}.}
 \tag{R-19846.26}
\]

This implication is obtained before invoking the finite real-zero theorem or
Hurwitz.

## 6. Why high-ordinate support averaging cannot close the central block

The rank-one support large sieve controls oscillatory families whose phases vary
on the support scale.  A fixed off-line cardinal witness is a bounded-ordinate,
form-stable direction.  Its negative value (R-19846.11) does not average away as
support grows.

Placing this direction in the scalar shift forces the shift below the negative
witness by at least the positive complement charge `c_jD_j(u_j)`.  The Xi target
then pays the same shift while its own exact residual energy tends to zero.
That is precisely the contradiction above.

Thus a valid proof of the affine gate must contain a genuinely strip-sensitive
argument that excludes the central cardinal signature.  It cannot be assembled
only from:

```text
Riemann--von Mangoldt smooth density;
high-ordinate support averaging;
Bessel/Airy endpoint bounds;
periodization-fold estimates;
source graph conditioning;
or a target residual cutoff.
```

## 7. Relationship to other repository routes

The obstruction is the same exact object identified independently by:

- `L-15613`: the off-line Xi-cardinal negative block;
- `T-19701`: the Schur-corrected kernel floor is RH-equivalent under capture;
- `T-21703`: the positive Brownian off-line variance defect;
- the square-screw and Möbius-safe-energy criteria: every fixed off-line zero
  creates a polynomial or exponential growth mode.

These are not four independent errors.  They are four coordinate systems for
the same strip-sensitive obstruction.

## 8. Status correction

The algebraic hybrid reservoir and the affine spectral theorem remain valid.
The classification of the source-specific profile theorem changes:

```text
exact hybrid residual target/gap       PROVED/PROPOSED FOR REVIEW
abstract affine spectral transfer       PROVED
high-frequency profile mechanisms       PROPOSED ANALYTIC TOOLS
complete central-inclusive affine gate  RH-BEARING / UNPROVED
T-19813 as completed RH proof            GAPS/BLOCKED
RH                                       UNPROVED
```

A future completion must prove a new strip-sensitive theorem directly.  A
source-specific prime-side proof of (R-19846.1)--(R-19846.2) would still be a
valid proof of RH; it simply cannot be advertised as a routine final assembly
step.
