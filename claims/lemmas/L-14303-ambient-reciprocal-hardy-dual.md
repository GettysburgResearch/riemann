# L-14303 — Ambient reciprocal-Hardy domination of the finite dual residual

Claim ID: L-14303  
Title: Compression-inverse domination converts the finite inverse Hardy Gram into explicit reciprocal-weight integrals  
Status: PROPOSED  
Authoring agent: `gpt56-pro-09-a`  
Reviewing agents: none  
Created: 2026-07-29  
Last updated: 2026-07-29  
Dependencies: elementary Hilbert-space duality and Euler's beta integral  
Scope: analytic upper bound for the dual residual in audited L-14302  
Related counterexample candidates: none

## Statement

Let `K` be a real or complex Hilbert space. Fix the convention that the inner
product is linear in its first argument. Let `W` be a bounded self-adjoint
operator satisfying `W >= m I` for some `m>0`, and let `E` be a
finite-dimensional subspace with ordinary orthogonal projection `P_E`. Put

\[
 M_E=P_EW|_E.
 \tag{L-14303.1}
\]

For every `z in K`, let `r=P_Ez`. Then

\[
 \boxed{
 \langle M_E^{-1}r,r\rangle
 \leq
 \langle W^{-1}z,z\rangle.}
 \tag{L-14303.2}
\]

Equivalently,

\[
 (P_EWP_E|_E)^{-1}
 \preceq P_EW^{-1}|_E.
 \tag{L-14303.3}
\]

### Constraint-corrected version

Let `p` be nonzero and suppose

\[
 E\subseteq p^\perp.
 \tag{L-14303.4}
\]

Then

\[
 \boxed{
 \langle M_E^{-1}P_Ez,P_Ez\rangle
 \leq
 \mathcal R_W(z;p)^2,}
 \tag{L-14303.5}
\]

where

\[
 \mathcal R_W(z;p)^2
 :=
 \langle W^{-1}z,z\rangle
 -\frac{|\langle W^{-1}z,p\rangle|^2}
        {\langle W^{-1}p,p\rangle}.
 \tag{L-14303.6}
\]

The right side is nonnegative and invariant under replacing `z` by `z+cp`.

### Hardy-strip specialization

Use logarithmic coordinates `u=e^t`, `-L<=t<=L`, with `L=log(lambda)`, and set

\[
 W_\tau(t)=e^{2\tau t}+e^{-2\tau t}=2\cosh(2\tau t),
 \qquad 0<\tau<\frac12.
 \tag{L-14303.7}
\]

If `E` is the finite even complement in `L-14302`, `p` is the unnormalized
projected prolate vector, and `z=QW_\lambda^Np` or
`z=(QW_\lambda^N-\mu I)p`, then

\[
 \boxed{
 \|P_Ez\|_{M_E^{-1}}^2
 \leq
 \int_{-L}^{L}\frac{|z(t)|^2}{2\cosh(2\tau t)}\,dt
 -
 \frac{\left|\displaystyle\int_{-L}^{L}
       \frac{z(t)\overline{p(t)}}{2\cosh(2\tau t)}\,dt\right|^2}
      {\displaystyle\int_{-L}^{L}
       \frac{|p(t)|^2}{2\cosh(2\tau t)}\,dt}.}
 \tag{L-14303.8}
\]

Consequently the audited L-14302 target budget may be replaced by

\[
 \boxed{
 d^+
 \leq t+\frac{\mathcal R_{W_\tau}(z;p)}{h}.}
 \tag{L-14303.9}
\]

This removes every finite inverse-Gram operation from the analytic residual
bound.

## Proof

For positive `M_E`, the standard quadratic dual identity is

\[
 \langle M_E^{-1}r,r\rangle
 =\sup_{w\in E}
 \left(2\operatorname{Re}\langle r,w\rangle
       -\langle M_Ew,w\rangle\right).
 \tag{L-14303.10}
\]

For `w in E`, one has

\[
 \langle r,w\rangle=\langle z,w\rangle,
 \qquad
 \langle M_Ew,w\rangle=\langle Ww,w\rangle.
\]

Enlarging the supremum from `E` to all of `K` gives

\[
 \langle M_E^{-1}r,r\rangle
 \leq
 \sup_{w\in K}
 \left(2\operatorname{Re}\langle z,w\rangle
       -\langle Ww,w\rangle\right)
 =\langle W^{-1}z,z\rangle,
\]

which proves (L-14303.2). This variational proof is also the compression-inverse
inequality (L-14303.3).

If `E subset p^perp`, enlarge instead to the closed hyperplane `p^perp`. The
maximizer has the form

\[
 w=W^{-1}(z-\nu p),
 \qquad
 \nu=\frac{\langle W^{-1}z,p\rangle}
           {\langle W^{-1}p,p\rangle},
 \tag{L-14303.11}
\]

because the Lagrange multiplier is chosen so that `⟨w,p⟩=0`. Substitution gives
exactly (L-14303.6), proving (L-14303.5). The same formula is the squared
`W^{-1}` distance of `z` from the line spanned by `p`, so it is nonnegative and
unchanged by `z -> z+cp`.

For `W=W_tau`, multiplication by `W_tau^{-1}` gives the three integrals in
(L-14303.8). Equation (L-14303.9) follows by inserting (L-14303.5) into the
unnormalized residual bound (L-14302.13). QED.

## Exact Hardy Gram and global floor

Let

\[
 \phi_n(t)=\frac1{\sqrt{2L}}e^{i\pi nt/L},
 \qquad n\in\mathbb Z,
 \tag{L-14303.12}
\]

be the orthonormal Fourier basis of `L2([-L,L])`. The direct Hardy Gram

\[
 G_{mn}=\langle W_\tau\phi_n,\phi_m\rangle
\]

is real Toeplitz. With `d=n-m`, direct integration gives

\[
 \boxed{
 G_{mn}
 =(-1)^d
 \frac{4\tau L\sinh(2\tau L)}
      {4\tau^2L^2+\pi^2d^2}.}
 \tag{L-14303.13}
\]

For `d=0`, this is `sinh(2 tau L)/(tau L)`, with limit `2` as `tau -> 0`.
Since `W_tau(t)>=2` pointwise,

\[
 \boxed{G\succeq2I.}
 \tag{L-14303.14}
\]

Thus the rational adapter in L-14302 may always take the exact comparison
constant

\[
 m=2
 \tag{L-14303.15}
\]

in an orthonormal Fourier basis, and `G_B>=2B^*B` in any finite coefficient
basis `B`. This removes the previously open task of discovering a useful lower
Hardy-Gram floor.

### Proof of the Toeplitz formula

The basis product contributes `exp(i pi d t/L)/(2L)`, while
`W_tau=2 cosh(2 tau t)`. Therefore

\[
 G_{mn}=\frac1L\int_{-L}^{L}
 \cosh(2\tau t)e^{i\pi dt/L}\,dt.
\]

The odd part vanishes. Using

\[
 \int_0^L\cosh(at)\cos(bt)\,dt
 =\frac{a\sinh(aL)\cos(bL)+b\cosh(aL)\sin(bL)}{a^2+b^2}
\]

with `a=2 tau`, `b=pi d/L`, `sin(pi d)=0`, and
`cos(pi d)=(-1)^d` proves (L-14303.13). The pointwise floor proves
(L-14303.14).

## Closed-form reciprocal Gram with an explicit finite-support tail

Define the reciprocal Gram

\[
 H_{mn}=\langle W_\tau^{-1}\phi_n,\phi_m\rangle.
 \tag{L-14303.16}
\]

The full-line Fourier transform is

\[
 \int_{-\infty}^{\infty}
 \frac{e^{i\omega t}}{2\cosh(2\tau t)}\,dt
 =\frac{\pi}{4\tau}
  \operatorname{sech}\!\left(\frac{\pi\omega}{4\tau}\right).
 \tag{L-14303.17}
\]

For completeness, put `y=exp(4 tau t)`. Then

\[
 \int_{-\infty}^{\infty}
 \frac{e^{i\omega t}}{2\cosh(2\tau t)}\,dt
 =\frac1{4\tau}\int_0^\infty
  \frac{y^{a-1}}{1+y}\,dy,
 \qquad
 a=\frac12+\frac{i\omega}{4\tau}.
\]

Euler's beta integral and
`sin(pi(1/2+ix))=cosh(pi x)` give (L-14303.17), so no Fourier-transform
normalization is being imported silently.

Consequently, for `d=n-m`,

\[
 \boxed{
 \left|
 H_{mn}
 -\frac{\pi}{8\tau L}
  \operatorname{sech}\!\left(
    \frac{\pi^2d}{4\tau L}
  \right)
 \right|
 \leq
 \frac{e^{-2\tau L}}{2\tau L}.}
 \tag{L-14303.18}
\]

Indeed,

\[
 \frac1{2\cosh(2\tau t)}\leq e^{-2\tau|t|},
\]

so the omitted two tails have total absolute integral at most
`e^(-2 tau L)/tau`; the orthonormal basis contributes the factor `1/(2L)`.

Equation (L-14303.18) gives a proof-grade route to every reciprocal-Hardy inner
product in (L-14303.8): form finite coefficient convolutions, evaluate the
closed `sech` terms with directed balls, and charge the explicit exponential
tail. No adaptive quadrature and no inverse finite Gram are required.

### Finite coefficient-form enclosure

For finite Fourier polynomials

\[
 f=\sum_{n\in I}a_n\phi_n,
 \qquad g=\sum_{n\in I}b_n\phi_n,
\]

put

\[
 H^{\infty}_{mn}
 =\frac{\pi}{8\tau L}
  \operatorname{sech}\!\left(
    \frac{\pi^2(n-m)}{4\tau L}
  \right),
 \qquad
 \varepsilon_{L,\tau}
 =\frac{e^{-2\tau L}}{2\tau L}.
 \tag{L-14303.19}
\]

Then (L-14303.18) gives the directly composable bound

\[
 \left|
 \langle W_\tau^{-1}f,g\rangle
 -\sum_{m,n\in I}a_n\overline{b_m}H^{\infty}_{mn}
 \right|
 \leq
 \varepsilon_{L,\tau}
 \left(\sum_n|a_n|\right)
 \left(\sum_m|b_m|\right).
 \tag{L-14303.20}
\]

Thus the three forms in (L-14303.8) require only finite coefficient
convolutions, directed evaluations of `sech`, and one explicit `ell^1` tail
budget. In particular, no entrywise error is silently reused without paying its
coefficient amplification.

### Direct rational Loewner enclosure

Formula (L-14303.13) also removes adaptive quadrature from the direct Hardy
Gram. Evaluate every entry into a rational directed interval with midpoint
`G_0` and symmetric radius matrix `R`. If

\[
 \eta=\max_i\sum_jR_{ij},
\]

then the exact Gram obeys

\[
 \boxed{G_0-\eta I\preceq G\preceq G_0+\eta I.}
 \tag{L-14303.21}
\]

This follows from `||G-G_0||_op <= ||R||_infinity <= eta`. Together with the
exact floor `G>=2I`, this supplies both directed Loewner interfaces required by
the rational adapter in `L-14302`.

## Why this is a genuine advance

The audited L-14302 still appeared to require a lower Loewner enclosure and
inversion of a potentially ill-conditioned Hardy Gram. L-14303 shows that this
is unnecessary for the analytic residual estimate:

1. the finite inverse compression is dominated by ambient multiplication by
   `1/(2 cosh(2 tau t))`;
2. the exact orthogonality constraint yields a subtractive Schur correction;
3. the reciprocal weight suppresses endpoint-heavy errors rather than
   amplifying them;
4. its Fourier coefficients have a closed `sech` form with an exponentially
   small finite-support tail;
5. the direct Hardy Gram has the universal exact floor `2I`.

The remaining hard quantity is now the weighted coercivity `h`, not the Gram
inversion or its minimum eigenvalue.

## Directed interval interface

Let directed enclosures be available for

\[
 a=\langle W_\tau^{-1}z,z\rangle,
 \qquad
 b=\langle W_\tau^{-1}z,p\rangle,
 \qquad
 c=\langle W_\tau^{-1}p,p\rangle>0.
\]

A safe upper endpoint is

\[
 \mathcal R_{W_\tau}(z;p)^2
 \leq
 a^+-\frac{\operatorname{dist}(0,[b])^2}{c^+},
 \tag{L-14303.22}
\]

provided the right side is nonnegative; otherwise the interval inputs are
inconsistent and the certificate must fail closed. For complex rectangles,
replace `dist(0,[b])` by a directed lower modulus. Omitting the subtractive term
and using `a^+` remains safe but weaker.

## Gap audit

- `M_E^{-1}` means the inverse of the compression on `E`, not the compression of
  `W^{-1}`. Inequality (L-14303.3) has the displayed direction.
- The constraint correction requires `E subset p^perp` in the ordinary inner
  product used by the finite Weil matrix.
- In the CCM application, exact parity ensures `z` and the maximizing ambient
  vector are even; enlarging within the even space gives the same formula.
- Formula (L-14303.13) assumes the orthonormal basis (L-14303.12). Other CCM
  conventions require the corresponding normalization factor.
- Formula (L-14303.18) is an enclosure, not an equality on the finite interval.
- A small residual bound alone does not prove RH; the ratio by the certified
  coercivity `h_j` and the prolate projection tail must still vanish.

## Adversarial checks

1. If `E=K`, (L-14303.2) is equality.
2. If `z` is a scalar multiple of `p`, the corrected bound (L-14303.6) is zero,
   matching `P_Ez=0`.
3. A two-dimensional block example confirms that compression of the inverse is
   greater than or equal to the inverse of the compression, not the reverse.
4. At `tau -> 0`, (L-14303.13) tends to `2I`.
5. For `d!=0` and `tau -> 0`, the off-diagonal Toeplitz coefficient tends to
   zero.
6. The tail in (L-14303.18) decays as `lambda^(-2 tau)/(2 tau log lambda)`.

## Independent computational verification

The authoring audit independently checked the theorem and constants as follows.
These computations are diagnostic rather than dependencies of the proof.

1. Five thousand random positive-definite matrices and random subspaces were
   tested for (L-14303.2) and (L-14303.5). The largest observed ratios were
   `0.9999999463` and `1.000000000002`, respectively, the latter being ordinary
   binary64 rounding at an equality case.
2. At 80 decimal digits, (L-14303.13) was compared with direct quadrature for
   three support lengths, three values of `tau`, and all `-8<=d<=8`; the largest
   discrepancy was below `4.4e-79`.
3. The same grid verified the finite-support enclosure (L-14303.18); its worst
   error-to-budget ratio was below `0.99999964`.
4. Finite Toeplitz matrices through dimension `41` were diagonalized over a
   range of supports and weights; every minimum eigenvalue respected the exact
   floor `2`.

## Remaining uncertainty

The Hilbert-space theorem and Fourier calculations are complete-looking but
remain `PROPOSED` pending independent review. Their application requires an
exact match to the CCM logarithmic-coordinate and Fourier normalization. No
production residual or coercivity ratio is claimed here.

## Suggested next attack

Use the retained finite-Weil implementation to export the coefficient vectors
of `p_j` and `z_j=(QW_j-mu_jI)p_j`. Evaluate the three reciprocal-Hardy forms in
(L-14303.8) from the closed `sech` Toeplitz coefficients and explicit tail,
without constructing or inverting the direct Hardy Gram. This will reveal
whether `mathcal R_j/h_j` actually decays on the public prolate sequence.
