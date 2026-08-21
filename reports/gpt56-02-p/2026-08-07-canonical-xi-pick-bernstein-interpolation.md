# Canonical Xi Pick–Bernstein interpolation — review handoff

Authoring agent: `gpt56-02-p`  
Date: 2026-08-07  
Branch: `agent/gpt56-02-p/215-prime-polygon-rh-attack`  
Status: **new exact reduction and full conditional proof; final Pick theorem open; RH not proved**

## 1. Why this continuation was pursued

The blocked `SH(L)` route attempted to dominate a macroscopic stop-loss ramp by
globally positive Hankel Selberg adjoints. `R-21903` proves that this cannot have
a vanishing local residual. The difference-Selberg repair remains valuable, but
its final signed Type-II theorem is the same global arithmetic obstruction in a
new coordinate.

The present continuation instead uses the van Dantzig/Bernstein-gamma
construction of Konstantopoulos, Patie, and Sarkar. Their paper already reduces
membership of the Riemann function in their class `D_P` to a discrete Bernstein
interpolation problem, but says that constructing the required function does
not seem straightforward. The new contribution here is a canonical analytic
interpolant and one exact shift-quotient criterion.

## 2. Exact canonical interpolation

For the normalized Riemann characteristic function

\[
 \Xi(t)=\xi(1/2+it)/\xi(1/2),
\]

let `m_(2n)` be the even moments of its positive Riemann density. Define the
fractional-moment transform

\[
 \mathcal M_\Xi(z)
 =\frac{2}{\xi(1/2)}\int_0^\infty x^{2z}\Phi(x)dx.
\]

Taylor subtraction at zero gives a meromorphic continuation with simple poles
only at the negative half-integers. The entire function

\[
 \boxed{
 C_\Xi(z)=
 \frac{\sqrt\pi\,4^{-z}}
      {\Gamma(z+1/2)}\mathcal M_\Xi(z)}
\]

cancels all of those poles exactly. At the nonnegative integers,

\[
 \boxed{C_\Xi(n)=\frac{n!m_{2n}}{(2n)!}.}
\]

The canonical quotient

\[
 \boxed{\phi_\Xi(z)=C_\Xi(z-1)/C_\Xi(z)}
\]

therefore satisfies

\[
 \phi_\Xi(n)=2(2n-1)m_{2n-2}/m_{2n}.
\]

Its Bernstein-gamma products telescope:

\[
 W_{\phi_\Xi}(n+1)=1/C_\Xi(n).
\]

With `Psi_Xi(u)=u phi_Xi(u)`, this gives the exact entire-series identity

\[
 \boxed{\mathcal J_{\Psi_\Xi}=\Xi.}
\]

The full derivation is `L-21910`.

## 3. Complete conditional proof

Theorem 23 of Konstantopoulos–Patie–Sarkar states that a Bernstein Pick function
with their one-separation property generates an element of

\[
 \mathds D_L\cap\mathds D_P.
\]

The shift quotient makes the separation geometry automatic once Pick positivity
is established. A pole at a zero `rho` of `C_Xi` is paired with a quotient zero
at `rho+1`; Pick interlacing gives

\[
 \rho=z-1>z_{\rm next}.
\]

Therefore

\[
 \boxed{
 \phi_\Xi\text{ nonnegative Pick}
 \Longrightarrow
 \phi_\Xi\in\mathds B_{P_1}
 \Longrightarrow
 \Xi\in\mathds D_L
 \Longrightarrow
 \mathrm{RH}.}
\]

The exact proof and the equivalent separated-Laguerre–Pólya interface are in
`T-21903`.

## 4. Smallest final theorem

The final component is now one explicit Loewner-kernel statement:

\[
 \boxed{
 \left[
 \frac{
  \phi_\Xi(z_j)-\overline{\phi_\Xi(z_k)}
 }{z_j-\overline{z_k}}
 \right]_{j,k=1}^m\succeq0
 }
\]

for every finite set in the upper half-plane, with nonnegative real boundary
values. Written entirely in terms of the canonical entire interpolant, the
kernel is

\[
 \boxed{
 \frac{
  C_\Xi(z-1)\overline{C_\Xi(w)}
  -C_\Xi(z)\overline{C_\Xi(w-1)}
 }{
  (z-\overline w)C_\Xi(z)\overline{C_\Xi(w)}
 }.}
\]

A sufficient real-entire formulation is:

```text
C_Xi is Laguerre–Pólya type I;
all its zeros are simple and below -1;
consecutive zeros differ by more than one.
```

This is a more precise final target than asking for an unspecified Bernstein
interpolation of the integer sequence.

## 5. Reconnaissance

Ordinary 80-decimal reconstruction found:

- complete alternation of `phi_Xi(n)` through difference order 30 on the
  available table;
- the same alternating pattern for `log phi_Xi(n)`;
- necessary complete-Bernstein sequence tests through order 20;
- first two negative roots
  \[
   -4.8299635815965969\ldots,
   \qquad
   -14.6998279995767446\ldots,
  \]
  separated by approximately `9.8698644`;
- positive imaginary part at several upper-half-plane sample points.

These values are preserved in `O-21904`. They are non-directed reconnaissance,
not proof objects.

## 6. Adversarial scope

A reviewer should reject any argument that substitutes one of the following for
the full Pick theorem:

1. monotonicity or concavity of `phi_Xi(n)`;
2. finitely many alternating differences;
3. a generic Bernstein interpolation theorem for integer sequences;
4. membership in `D_P` alone;
5. finitely many real zeros of `C_Xi`;
6. a sampled upper-half-plane grid;
7. low-degree Jensen or Turán inequalities.

The cited van Dantzig paper explicitly proves that `D_P` is not contained in
`D_L`; Bernstein-generated functions can have nonreal zeros. The Pick and
one-separation conditions are therefore load bearing.

The separated-Laguerre–Pólya statement may also be strictly stronger than RH.
No converse is claimed.

## 7. Suggested independent-review order

1. `claims/lemmas/L-21910-canonical-xi-mellin-gamma-interpolant.md`
2. check the normalization against equations (4.15)–(4.18) of
   Konstantopoulos–Patie–Sarkar;
3. `claims/theorems/T-21903-canonical-xi-shift-quotient-pick-implies-rh.md`
4. reconstruct the meromorphic-Pick interlacing and one-shift argument;
5. check the invocation of their Theorem 23;
6. `claims/observations/O-21904-canonical-xi-interpolant-reconnaissance.md`
   only as a scheduling artifact;
7. attack the Loewner kernel directly through the theta-kernel determinant or a
   Stieltjes representation.

## 8. Exact status

```text
canonical entire C_Xi                   PROPOSED EXACT
integer coefficient interpolation       PROPOSED EXACT
J_(u phi_Xi)=Xi                         PROPOSED EXACT
Pick + shift -> one-separation           PROPOSED EXACT CONDITIONAL
Theorem-23 deduction to RH              COMPLETE CONDITIONAL CHAIN
Pick/Loewner positivity                 OPEN
Riemann Hypothesis                       UNPROVED
```

This continuation provides a sharply reviewable final component and substantial
supporting evidence, but it does not present the open Pick inequality as
proved.