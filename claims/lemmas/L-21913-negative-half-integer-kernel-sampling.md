# L-21913 — Negative half-integer kernel sampling

Claim ID: `L-21913`  
Title: Every negative half-integer value of the canonical Xi interpolant is an exact Taylor coefficient of the Riemann kernel, giving finite directed brackets for its real Mellin zeros  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-21910`  
Scope: exact sampling and finite root brackets; no claim that all zeros are real

## 1. Kernel Taylor coefficients

Use the normalization of `L-21910`:

\[
 \Xi(t)=\frac{2}{\xi(1/2)}
 \int_0^\infty\Phi(x)\cos(tx)\,dx.
 \tag{L-21913.1}
\]

Because `Phi` is even and entire, write

\[
 \boxed{
 \Phi(x)=\sum_{k=0}^\infty a_kx^{2k}.}
 \tag{L-21913.2}
\]

The coefficients are real. No sign assumption is imposed.

## 2. Residues of the fractional-moment transform

Recall

\[
 \mathcal M_\Xi(z)
 =\frac{2}{\xi(1/2)}
  \int_0^\infty x^{2z}\Phi(x)\,dx.
 \tag{L-21913.3}
\]

The Taylor-subtraction continuation in `L-21910` shows that the only possible
pole at

\[
 z_k=-k-\frac12
 \tag{L-21913.4}
\]

comes from

\[
 \frac{2}{\xi(1/2)}
 \int_0^1a_kx^{2z+2k}\,dx
 =\frac{2a_k}{\xi(1/2)(2z+2k+1)}.
\]

Hence

\[
 \boxed{
 \operatorname*{Res}_{z=z_k}
 \mathcal M_\Xi(z)
 =\frac{a_k}{\xi(1/2)}.}
 \tag{L-21913.5}
\]

## 3. Exact sample values of the entire interpolant

The reciprocal gamma function has the local expansion

\[
 \frac1{\Gamma(z+1/2)}
 =(-1)^kk!(z-z_k)+O((z-z_k)^2)
 \tag{L-21913.6}
\]

at `z=z_k`. Since

\[
 C_\Xi(z)=
 \frac{\sqrt\pi\,4^{-z}}{\Gamma(z+1/2)}
 \mathcal M_\Xi(z),
\]

(L-21913.5)--(L-21913.6) give the removable value

\[
 \boxed{
 C_\Xi\!\left(-k-\frac12\right)
 =\frac{\sqrt\pi}{\xi(1/2)}
 4^{k+1/2}(-1)^kk!a_k.}
 \tag{L-21913.7}
\]

Thus the complete second sampling lattice is explicit:

```text
positive integers      <-> even moments of Phi;
negative half-integers <-> Taylor coefficients of Phi.
```

Both arise from the same canonical Mellin–gamma interpolation.

## 4. Directed real-zero brackets

The positive prefactor in (L-21913.7) shows

\[
 \operatorname{sgn}
 C_\Xi(-k-1/2)=\operatorname{sgn}[(-1)^ka_k]
 \tag{L-21913.8}
\]

whenever `a_k` is nonzero. Consequently, if

\[
 \boxed{a_ka_{k+1}>0,}
 \tag{L-21913.9}
\]

then the two consecutive samples in (L-21913.8) have opposite signs. By
continuity, `C_Xi` has at least one real zero in

\[
 \boxed{
 \left(-k-\frac32,-k-\frac12\right).}
 \tag{L-21913.10}
\]

A directed interval for `a_k` and `a_(k+1)` bounded away from zero therefore
gives a finite proof-grade real-zero bracket without evaluating a Mellin
integral or solving for a root.

Conversely, absence of a sign change does not exclude an even number of real
zeros or a complex-conjugate pair. The bracket is one-sided evidence only.

## 5. Parity ledger under the final real-rootedness theorem

Assume, only for this section, that `C_Xi` has no zero at the sampling points and
all its zeros are real and simple. Let `N_k` be the number of zeros in

\[
 (-k-3/2,-k-1/2).
\]

Then (L-21913.8) gives the exact parity identity

\[
 \boxed{
 (-1)^{N_k}
 =-\operatorname{sgn}(a_ka_{k+1}).}
 \tag{L-21913.11}
\]

Thus the Taylor-coefficient sign word is a finite parity checksum for every
unit Mellin cell. Any proposed real-rootedness proof or directed zero census
must reproduce it.

The identity does not assert `N_k=1`; a uniqueness or total-positivity theorem
is still required.

## 6. Normalization warning

A common alternative kernel uses the variable `u=x/2` and represents
`xi(1/2+it/2)`. Under that convention the raw moments acquire a factor
`2^(2z)`. The factor `4^(-z)` in `C_Xi` cancels this scaling exactly, but Taylor
coefficients must be transformed at the same time. Formula (L-21913.7) is stated
only in the normalization (L-21913.1).

This warning is load bearing for numerical replay: mixing the two standard
Riemann-kernel variables multiplies the quotient samples by four.

## 7. Production interface

A proof-producing finite bracket should emit:

```text
exact kernel normalization;
directed enclosures for a_k and a_(k+1);
proof that neither enclosure meets zero;
exact rational sign contraction in (L-21913.7);
the resulting open unit interval;
optional interval-Newton uniqueness inside the bracket.
```

The exact half-integer samples can also serve as mutation tests for a direct
Mellin evaluator of `C_Xi`.

## 8. Status boundary

Closed exactly:

- the residue calculation;
- every negative half-integer sample;
- finite sign-change root brackets;
- the conditional unit-cell parity ledger;
- the normalization adapter.

Open:

- a sign theorem for all Taylor coefficients;
- uniqueness of the bracketed roots;
- exclusion of nonreal zeros;
- the generalized Stieltjes certificate of `L-21912`;
- RH.