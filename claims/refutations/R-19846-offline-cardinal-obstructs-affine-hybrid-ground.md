# R-19846 — An off-line Xi-cardinal quartet obstructs every cofinal affine ground-selection estimate

Claim ID: `R-19846`  
Status: **PROVED CONDITIONAL OBSTRUCTION — IF RH IS FALSE, THE AFFINE HYBRID GATE FAILS COFINALLY**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-07  
Dependencies: Xi-cardinal defect theorem `L-15613`; Hardy-strip Fourier approximation `L-16213`; exact Xi target `L-19849`; affine ground transfer `L-19861`  
Scope: load-bearing audit of `L-19865/T-19813`

## 1. Statement

Let

\[
 \Xi(z)=\xi\!\left(\frac12+iz\right).
\]

Assume RH is false, and let

\[
 \omega=\gamma+i\delta,
 \qquad \delta\ne0,
\]

be a centered nonreal zero of multiplicity `m`.  Let `V_j` be any cofinal
sequence of centered finite Fourier spaces with support radii `L_j -> infinity`
and bandwidths large enough to approximate every fixed Hardy-strip vector; the
quadratic-log schedule

\[
 N_j\ge cL_j^2
\]

is sufficient.

Let `A_j` be the exact finite localized Weil matrix on `V_j`. Let `p_j` be any
unit even target converging in a fixed Hardy strip to a global arithmetic
radical whose transform is a nonzero multiple of `Xi`. Then there is a fixed
number `kappa>0` and unit even vectors `h_j in V_j` such that

\[
 \langle h_j,A_jh_j\rangle\le-\kappa
\]

for all sufficiently large `j`, while

\[
 \langle p_j,A_jp_j\rangle\longrightarrow0.
\]

Consequently there do not exist, cofinally, nonnegative forms `D_j`, positive
numbers `c_j`, real shifts `sigma_j`, and target errors `r_j -> 0` satisfying

\[
 \boxed{A_j-\sigma_jI\succeq c_jD_j}
\tag{R-19846.1}
\]

and

\[
 \boxed{
 \langle p_j,A_jp_j\rangle-\sigma_j\le r_j.}
\tag{R-19846.2}
\]

In particular, the source-specific affine profile theorem required by
`L-19865/T-19813` is itself an off-line-zero exclusion theorem. It cannot be
obtained solely by tightening the high-ordinate support large sieve, Bessel
endpoint, Airy-fold, or periodization-fold constants.

## 2. Exact even negative cardinal vector

For every distinct zero `nu` of `Xi`, let `k_nu` be the inverse Fourier
transform of the cardinal function

\[
 K_\nu(z)=
 \frac{\Xi(z)}
 {a_\nu(z-\nu)^{m_\nu}},
 \qquad
 a_\nu=\Xi^{(m_\nu)}(\nu)/m_\nu!.
\]

The centered Weil Gram is

\[
 Q_W(k_\mu,k_\nu)
 =m_\nu\,1_{\{\nu=\overline\mu\}}.
\tag{R-19846.3}
\]

The functional equation gives the quartet

\[
 \omega,-\omega,\overline\omega,-\overline\omega.
\]

Because `Xi` is even, the cardinal vectors may be rephased so that parity
interchanges `k_omega` with `k_-omega` and interchanges
`k_bar(omega)` with `k_-bar(omega)`. Put

\[
 e_\omega=k_\omega+k_{-\omega},
 \qquad
 e_{\overline\omega}
 =k_{\overline\omega}+k_{-\overline\omega}.
\]

Both are even. Equation (R-19846.3) gives

\[
 Q_W(e_\omega,e_\omega)=0,
 \qquad
 Q_W(e_{\overline\omega},e_{\overline\omega})=0,
\]

and

\[
 Q_W(e_\omega,e_{\overline\omega})=2m.
\]

Hence the even vector

\[
 \boxed{h=e_\omega-e_{\overline\omega}}
\tag{R-19846.4}
\]

has the exact value

\[
 \boxed{Q_W(h,h)=-4m.}
\tag{R-19846.5}
\]

Thus inversion parity does not remove the off-line obstruction.

## 3. Cofinal finite approximation

For every fixed `tau<1/2`, `L-15613` gives

\[
 h\in L^2\!\left(
 \mathbb R,2\cosh(2\tau t)dt
 \right).
\]

Its Fourier transform is `Xi` divided by a fixed polynomial, so the same
Stirling estimate and Fourier-series argument used in `L-16213` gives finite
even vectors `h_j in V_j` with

\[
 \|h_j-h\|_\tau\to0.
\tag{R-19846.6}
\]

The polarized Weil form is continuous on this fixed Hardy strip. Therefore

\[
 Q_W(h_j,h_j)\to-4m,
\qquad
 \|h_j\|_2\to\|h\|_2>0.
\tag{R-19846.7}
\]

After normalization, there is `kappa>0` such that

\[
 \langle h_j,A_jh_j\rangle\le-\kappa
\tag{R-19846.8}
\]

for all sufficiently large `j`.

## 4. The Xi target has vanishing finite Weil value

Let `J_Xi` be the exact global arithmetic radical of `L-19849`. If `p_j`
converges to `J_Xi` in a Hardy strip, form continuity and global radicality give

\[
 \boxed{
 \langle p_j,A_jp_j\rangle\to0.}
\tag{R-19846.9}
\]

The exponentially small exact-residual target of `L-19862` is one concrete
realization of (R-19846.9).

## 5. Contradiction with an affine ground gate

Apply (R-19846.1) to the unit vector `h_j`. Since `D_j>=0`,

\[
 \sigma_j
 \le
 \langle h_j,A_jh_j\rangle
 \le-\kappa.
\tag{R-19846.10}
\]

On the other hand, (R-19846.2) and (R-19846.9) imply

\[
 -\sigma_j
 \le r_j-\langle p_j,A_jp_j\rangle
 \longrightarrow0.
\tag{R-19846.11}
\]

Equations (R-19846.10)--(R-19846.11) contradict one another. QED.

The same proof applies to the more detailed gate in `L-19865`: if its target
upper endpoint tends to zero, then its scalar shift must tend to zero, whereas
an off-line cardinal forces the shift to remain below a fixed negative number.

## 6. Consequences

1. A bounded or central ordinate block cannot be treated as a harmless finite
   profile error. It contains exactly the off-line cardinal signature.
2. High-ordinate support averaging does not address the obstruction: every fixed
   hypothetical zero eventually belongs to the bounded/central block.
3. The complete affine lower estimate with vanishing target excess is at least
   as strong as excluding every off-line zero.
4. The exterior-cardinal common reservoir and its constant ordinary residual
   gap remain correct algebra, but they do not turn the final indefinite sign
   into a routine local-Weyl estimate.
5. Any genuine recovery must either prove a new strip-sensitive theorem that
   directly excludes the cardinal block, or avoid selecting the Xi target as
   the ground state of the complete localized Weil matrix.

## 7. Proof boundary

- No off-line zero is asserted to exist.
- The theorem is a conditional obstruction: false RH forces failure of the
  affine gate.
- It does not disprove RH or the possibility of a new proof of the affine gate.
  It proves that such a proof would already contain the central RH argument.
- No high-frequency estimate can by itself supply that missing argument.
