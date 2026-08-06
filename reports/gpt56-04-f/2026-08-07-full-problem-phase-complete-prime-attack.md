# Full-problem attack: phase-complete prime energy and finite-notch exhaustion

Agent: `gpt56-04-f`  
Date: 2026-08-07  
Status: **new claims PROPOSED pending independent review; RH not claimed proved**

## 1. Why the previous frontier was too local

The recent branch work isolated many exact finite gates:

- Finsler/Loewner scalar-line positivity;
- corrected-kernel Schur floors;
- smooth-window coefficient intervals;
- singular-seam source producers;
- finite residue and matrix certificates.

Those gates are useful, but none attacks the full arithmetic tail by itself.
The repository-wide review shows three global mechanisms carrying the same
obstruction:

1. the square-screw scalar detects a rightmost zero through negative growth;
2. the terminal-prime window detects it as an exponentially escaping translated
   prime mode;
3. the Hilbert--Poisson/Weyl programmes detect it as an anti-causal or
   right-half-plane energy packet.

The missing synthesis was a positive finite arithmetic observable that keeps the
full rightmost-zero exponent without requiring a chosen sign, phase, target
root, or matrix eigenvector.

## 2. New theorem: positive energy measures the exact rightmost zero

`L-15143` uses the explicit three-piece triangular pole-free window `G_h` from
`L-15409` and the raw finite prime-power signal

\[
 Q_h(x)=\sum_n\frac{\Lambda(n)}{\sqrt n}G_h(x-\log n).
\]

For the unit block energy

\[
 B_h(X)=\int_X^{X+1}|Q_h(x)|^2dx,
\]

it proves

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
 \frac{\log(1+B_h(X))}{2X}.}
\]

The same exponent is obtained from cumulative energy and from the abscissa of
exponentially weighted `L2` convergence.

This changes the global target from

```text
find a negative scalar / prove a shrinking matrix moat
```

to

```text
prove one nonnegative finite prime-pair energy is subexponential.
```

It also removes the sparse-phase weakness of square-screw sampling. A false RH
forces exponentially deep **positive** energy blocks at the exact exponent of
the rightmost zero.

Every block is a finite Gram quadratic form over prime powers in a fixed-ratio
annulus. No zero ordinate enters its definition.

## 3. New theorem: finite notches exhaust RH and preserve false RH

`T-15117` successively convolves the triangular window with normalized boxes of
length

\[
 r_k=2\pi/\gamma_k
\]

at certified critical-line ordinates. The finite transform kills the first `M`
line-zero frequencies but is nonzero everywhere in the open shifted strip

\[
 0<\Re z<1/2.
\]

After subtracting the explicit trivial/endpoint term, let the resulting finite
prime signal be `R_M`.

The theorem proves the exact dichotomy

\[
 \boxed{
 \mathrm{RH}
 \Longrightarrow
 \|R_M\|_\infty\to0,}
\]

while under false RH, for every finite `M`,

\[
 \boxed{
 \limsup_{X\to\infty}
 \frac{
 \log\left(1+\int_X^{X+1}|R_M(x)|^2dx\right)}{2X}
 =\Theta_\zeta>0.}
\]

Therefore

\[
 \boxed{
 \mathrm{RH}
 \iff
 \lim_{M\to\infty}\|R_M\|_\infty=0}
\]

and equivalently the supremum of the unit block energies tends to zero.

This is a full-problem criterion with a sharp qualitative separation:

```text
RH:
  certified line-zero notches exhaust the complete nontrivial spectrum.

not RH:
  every finite notch family leaves an exponentially escaping prime-energy mode.
```

## 4. Directed finite interface

For an actual zero ball

\[
 \gamma_k\in[\widetilde\gamma_k-\varepsilon_k,
              \widetilde\gamma_k+\varepsilon_k],
\]

the designed notch has the rigorous attenuation

\[
 \eta_k\le
 \frac{\varepsilon_k}{\widetilde\gamma_k-\varepsilon_k}.
\]

Under RH this gives the finite global moat

\[
 U_M=
 2\sum_{k\le M}m_k
 \sup_{t\in I_k}|\widehat G_h(it)|\eta_k
 +2\sum_{k>M}m_k|\widehat G_h(i\gamma_k)|.
\]

The second sum is bounded by a zero-count shell ledger. Tightening the selected
balls and increasing `M` makes `U_M` tend to zero.

A finite directed violation is then either

\[
 |R_M(x)|>U_M
\]

or

\[
 \int_X^{X+1}|R_M(x)|^2dx>U_M^2.
\]

This is a genuine finite RH-disproof certificate. It uses:

- one exact prime-power annulus;
- finitely many certified line-zero balls;
- exact/interval convolution factors;
- one explicit transform-tail majorant;
- no assumed off-line zero and no target-root computation.

## 5. Exact connection among the repository programmes

### Square-screw

`L-19802` measures `Theta_zeta` from the growth of the negative part of the
square screw. `L-15143` measures the same number from a positive block energy.
The two are phase-sensitive and phase-complete coordinates of the same
rightmost-zero obstruction.

### Direct-xi zero deflation

Subtracting certified critical-line factors on the zero side and inserting
spectral notches on the prime side are dual operations. The same zero-ball table
should feed both consumers.

### D-0001/source-canonical matrices

Each prime block energy is already a positive finite Gram quadratic form over a
canonical prime-power manifest. It can be stored in the same source-bound matrix
ledger without a moving target polynomial or an imported zero-side sign.

### Hilbert--Poisson/Weyl

For every line offset `omega>0`, finite exponentially weighted prime energy is
equivalent to absence of a right-zero packet beyond `1/2+omega`. The
anti-causal Hardy residual and the terminal-prime signal are two boundary
realizations of the same analytic continuation obstruction.

## 6. The ambitious positive attack

The prime-side identity

\[
 Q_M=\mathcal A_{r_M}\cdots\mathcal A_{r_1}Q_h,
 \qquad
 (\mathcal A_rf)(x)=r^{-1}\int_0^rf(x-u)du,
\]

turns the full proof problem into a deterministic repeated-averaging theorem for
one explicit arithmetic signal.

A proof of either

\[
 \|R_M\|_\infty\to0
\]

or

\[
 \sup_X\int_X^{X+1}|R_M(x)|^2dx\to0
\]

from the prime side, without using the zero expansion, proves RH.

The arithmetic expansion is an exact fixed-ratio prime-pair Gram sum. Unlike the
old bounded-mean-square target, the rightmost-zero theorem needs only
subexponential block energy. This is still RH-bearing, but it is a materially
larger target than a local matrix pivot and does not demand cancellation to a
fixed constant.

The next proof attack should therefore be global and source-canonical:

1. derive the notched autocorrelation kernel explicitly;
2. seek a Selberg/renewal identity for the complete signed off-diagonal prime
   sum, retaining the pole-annihilating factor before any absolute value;
3. prove subexponential block energy uniformly in `M` along a slow support-cost
   schedule;
4. alternatively, run the directed finite moat and preserve the first strict
   violation.

## 7. What has and has not been achieved

### Achieved

- one positive finite prime observable recovers the exact rightmost-zero
  displacement;
- a finite-notch sequence converges uniformly to zero under RH;
- every finite notch sequence retains the exact false-RH growth exponent;
- square-screw, terminal-prime, direct-xi deflation, and strip-energy routes are
  placed in one exact global architecture;
- a finite source-bound disproof interface with a shrinking RH moat is explicit.

### Not achieved

- no unconditional prime-pair subexponential bound has been proved;
- no directed finite violation has been produced;
- RH is neither proved nor disproved by this contribution.

## 8. SERIOUS RESOLUTION PATH

**Yes: a serious full-problem path is present.**

The precise remaining theorem is not another local completion condition. It is
one global arithmetic statement:

\[
 \boxed{
 \sup_X\int_X^{X+1}|R_M(x)|^2dx\longrightarrow0
 \quad(M\to\infty),}
\]

where every `R_M` is an explicit finite prime-power statistic and the notch
schedule is bound to certified critical-line zeros.

A proof establishes RH. A finite violation of the explicit RH moat disproves
RH. False RH cannot hide through phase cancellation or through any finite set
of notches.

This is the route selected for further full-problem work.
