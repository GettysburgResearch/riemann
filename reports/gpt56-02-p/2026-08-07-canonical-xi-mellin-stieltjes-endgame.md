# Canonical Xi Mellin–Stieltjes endgame

Authoring agent: `gpt56-02-p`  
Date: 2026-08-07  
Branch: `agent/gpt56-02-p/215-prime-polygon-rh-attack`  
Status: **exact new reduction and substantial unconditional front half; final all-order Stieltjes theorem open; RH not proved**

## Executive result

The Bernstein–Pick route has been sharpened. One-unit zero spacing and a
Bernstein interpolation are sufficient but unnecessary. The preferred route is
now

```text
Riemann kernel Phi
-> canonical entire Mellin-gamma interpolant C_Xi
-> generalized Stieltjes curvature of C_Xi
-> all zeros of C_Xi real and below -1/2
-> negative zeros of the Mellin transform of Phi(sqrt y)
-> KPS Theorem 16
-> Xi in the Lukacs class D_L
-> RH.
```

The exact remaining theorem is

\[
 \boxed{
 -\frac{d^2}{dz^2}\log C_\Xi(z)
 =a+\int_{1/2}^{\infty}\frac{d\rho_\Xi(t)}{(z+t)^2},
 \qquad a\ge0,\ \rho_\Xi\ge0.}
\]

Equivalently, prove the complete Sokal derivative hierarchy for one explicit
real function. The first continuum member of that hierarchy is already proved
by Csordas–Varga.

## 1. Canonical entire interpolation

For

\[
 \Xi(t)=\xi(1/2+it)/\xi(1/2)
\]

and its positive Fourier kernel `Phi`, define

\[
 \mathcal M_\Xi(z)
 =\frac{2}{\xi(1/2)}\int_0^\infty x^{2z}\Phi(x)dx
\]

and

\[
 \boxed{
 C_\Xi(z)=
 \frac{\sqrt\pi\,4^{-z}}
      {\Gamma(z+1/2)}\mathcal M_\Xi(z).}
\]

Taylor subtraction shows that the Mellin poles occur only at negative
half-integers and the reciprocal gamma factor cancels every one. Hence `C_Xi`
is entire.

At nonnegative integers,

\[
 \boxed{C_\Xi(n)=n!m_{2n}/(2n)!.}
\]

The shift quotient

\[
 \phi_\Xi(z)=C_\Xi(z-1)/C_\Xi(z)
\]

therefore interpolates the exact moment-ratio sequence in the van Dantzig paper,
and its generalized-gamma products telescope to

\[
 \mathcal J_{u\phi_\Xi}=\Xi.
\]

These identities are `L-21910`.

## 2. A weaker and cleaner deduction to RH

Set

\[
 f_\Xi(y)=\Phi(\sqrt y).
\]

Its Mellin transform satisfies

\[
 \boxed{
 M_{f_\Xi}(s)
 =\frac{\xi(1/2)}{\sqrt\pi}
 4^{s-1/2}\Gamma(s)C_\Xi(s-1/2).}
\]

The gamma and exponential factors have no zeros. Thus real-rootedness of
`C_Xi`, together with its positivity on `(-1/2,infinity)`, forces every Mellin
zero to be negative.

The hypotheses of Konstantopoulos–Patie–Sarkar Theorem 16 hold for
`f_Xi`: positivity, analyticity at zero, and superexponential decay. Taking
`n=1` there, the normalized Fourier transform of

\[
 f_\Xi(x^2)=\Phi(x)
\]

belongs to `D_L`. It is exactly `Xi`. Their Theorem 3 then gives RH.

Therefore

\[
 \boxed{C_\Xi\text{ real-rooted}\Longrightarrow\mathrm{RH}.}
\]

This is `T-21904`. It is strictly weaker than the Pick/one-separation theorem
`T-21903`.

## 3. Exact positive-measure interface

Define

\[
 \mathcal S_\Xi(z)
 =-\frac{d^2}{dz^2}\log C_\Xi(z).
\]

At a zero `lambda` of multiplicity `m`,

\[
 \mathcal S_\Xi(z)
 =\frac{m}{(z-\lambda)^2}+\text{holomorphic}.
\]

Hence a generalized Stieltjes representation supported on `[1/2,infinity)`
can have singularities only at real points `lambda<=-1/2`, and it excludes every
nonreal zero.

For real `x>-1/2`, let `P_x` be the Mellin-tilted Riemann-kernel law

\[
 dP_x(u)=
 \frac{u^{2x}\Phi(u)}{\int v^{2x}\Phi(v)dv}du,
\]

and let `kappa_r(x)` be the cumulants of `log u`. Then exactly

\[
 \boxed{
 \mathcal S_\Xi^{(n)}(x)
 =\psi_{n+1}(x+1/2)-2^{n+2}\kappa_{n+2}(x).}
\]

Sokal's order-two theorem translates generalized Stieltjes membership into the
real inequalities

\[
 F_{n,k}^{[2]}(x)
 =(-1)^n\sum_{j=0}^k
 \binom kj
 \frac{\Gamma(n+k+2)}{\Gamma(n+j+2)}
 x^j f^{(n+j)}(x)\ge0
\]

for every `n,k>=0`, where

\[
 f(x)=\mathcal S_\Xi(x-1/2).
\]

This is `L-21912`.

## 4. Unconditional continuum progress

Csordas and Varga prove

\[
 t\longmapsto\log\Phi(\sqrt t)
\]

is strictly concave. Their Proposition 2.3 says the gamma-normalized Mellin
moment is then strictly log-concave for every real order.

After the exact substitution `t=u^2`, their normalized moment is `C_Xi` up to a
positive exponential factor. Consequently

\[
 \boxed{
 (\log C_\Xi)''(x)<0
 \qquad(x>-1/2),}
\]

or

\[
 \boxed{
 \mathcal S_\Xi(x)>0.}
\]

Equivalently,

\[
 \boxed{
 4\operatorname{Var}_x(\log u)
 <\psi_1(x+1/2).}
\]

Thus the complete `F_(0,0)^[2]` continuum inequality is closed. The shift
quotient is also strictly increasing on its positive real domain. This is
`L-21914`.

The earlier integer Turán theorem is preserved separately in `L-21911` as a
normalization check.

## 5. Exact second sampling lattice

If

\[
 \Phi(x)=\sum_{k=0}^{\infty}a_kx^{2k},
\]

then residue cancellation gives

\[
 \boxed{
 C_\Xi(-k-1/2)
 =\frac{\sqrt\pi}{\xi(1/2)}
 4^{k+1/2}(-1)^kk!a_k.}
\]

Therefore `a_k a_(k+1)>0` gives a strict real-zero bracket in

\[
 (-k-3/2,-k-1/2).
\]

These are finite proof-grade interfaces after directed Taylor-coefficient
enclosure. They also provide a parity checksum for every unit Mellin cell under
the final real-rootedness hypothesis. This is `L-21913`.

A normalization warning is included: the common Rodgers–Tao kernel variable is
half the variable used here, and mixing those conventions multiplies raw quotient
samples by four.

## 6. What remains

The final theorem is no longer the positivity of `S_Xi` itself; that is proved.
It is the all-order strengthening

\[
 \boxed{
 F_{n,k}^{[2]}(x)\ge0
 \quad\text{for every }n,k\ge0,\ x>0.}
\]

with `n+k>0`, or an explicit construction of the positive measure `rho_Xi`.

Potential mechanisms:

1. an Andréief determinant for the tilted logarithmic cumulants, with a
   theta-kernel total-positivity factor;
2. a direct theta-series decomposition of the Stieltjes measure;
3. a proof that the Mellin kernel is a `PF_infinity` density after gamma
   normalization;
4. the stronger Pick theorem for `C_Xi(z-1)/C_Xi(z)`.

A proof of complete monotonicity alone is insufficient. The generalized
Stieltjes class is strictly stronger, and the extra `k` inequalities are
load bearing.

## 7. Reconnaissance only

Ordinary high-precision calculations retained in `O-21904` show:

- many alternating finite differences of the quotient sequence;
- positive imaginary parts at selected upper-half-plane points;
- two real negative zeros of `C_Xi` near
  `-4.82996358` and `-14.69982800`.

No interval root count, nonreal-zero exclusion, or all-order inequality follows
from those computations.

## 8. Review order

1. `claims/lemmas/L-21910-canonical-xi-mellin-gamma-interpolant.md`
2. `claims/theorems/T-21904-mellin-zero-route-to-rh.md`
3. `claims/lemmas/L-21912-generalized-stieltjes-xi-zero-interface.md`
4. `claims/lemmas/L-21914-continuum-log-concavity-of-xi-interpolant.md`
5. `claims/lemmas/L-21913-negative-half-integer-kernel-sampling.md`
6. `claims/lemmas/L-21911-csordas-varga-first-bernstein-shadow.md`
7. `claims/theorems/T-21903-canonical-xi-shift-quotient-pick-implies-rh.md`
8. `claims/observations/O-21904-canonical-xi-interpolant-reconnaissance.md`

## 9. Exact boundary

```text
canonical entire interpolant C_Xi              PROPOSED EXACT
positive/negative sampling lattices             PROPOSED EXACT
continuum log-concavity and first Sokal member   PUBLISHED INPUT + EXACT ADAPTER
C_Xi real-rooted => RH                           COMPLETE CONDITIONAL CHAIN
Stieltjes all-order hierarchy                    OPEN
C_Xi real-rooted                                 OPEN
Riemann Hypothesis                               UNPROVED
```

The work is ready for adversarial review as a sharply delimited full proposal,
but the final all-order positive-measure theorem has not been presented as
proved.