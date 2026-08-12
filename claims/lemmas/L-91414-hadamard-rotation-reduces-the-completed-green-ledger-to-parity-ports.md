# L-91414 — Hadamard rotation reduces the completed Green ledger to parity ports

Claim ID: `L-91414`  
Status: **PROVED EXACT FULL-PACKET PORT REDUCTION; PARITY DOMINATION OPEN**  
Created: 2026-08-12  
Depends on: `L-91409`, corrected `L-91412`, `T-91402` on PR #411  
RH status: **unproved**

## 1. The universal two-port rotation

Let `H` be a complex Hilbert space and let

\[
 U,V:\mathcal D\longrightarrow H
\]

be two linear source maps on a common coefficient space. Define their even and
odd Hadamard ports

\[
 \boxed{
 E=\frac{U+V}{\sqrt2},
 \qquad
 O=\frac{U-V}{\sqrt2}.
 }
 \tag{L-91414.1}
\]

Then, as fully polarized operator identities,

\[
 \boxed{
 -U^*V-V^*U=O^*O-E^*E
 }
 \tag{L-91414.2}
\]

and

\[
 \boxed{
 U^*V+V^*U=E^*E-O^*O.
 }
 \tag{L-91414.3}
\]

This is simply the unitary rotation

\[
 \frac1{\sqrt2}
 \begin{pmatrix}1&1\\1&-1\end{pmatrix}
 \tag{L-91414.4}
\]

on the ordered endpoint pair `(U,V)`.  It preserves every cross-carrier,
cross-delay, cross-orientation and bridge term before any norm is taken.

## 2. Prime packet

The full prime Wick--Green identity of `L-91409` has the form

\[
 \mathfrak P_a^{\rm prime}
 =D_{\rm p}^*D_{\rm p}
  -U_{\rm p}^*U_{\rm p}
  -V_{\rm p}^*V_{\rm p},
 \qquad
 D_{\rm p}=U_{\rm p}-V_{\rm p}.
 \tag{L-91414.5}
\]

Put

\[
 O_{\rm p}=\frac{D_{\rm p}}{\sqrt2},
 \qquad
 E_{\rm p}=\frac{U_{\rm p}+V_{\rm p}}{\sqrt2}.
 \tag{L-91414.6}
\]

Since

\[
 U^*U+V^*V=E^*E+O^*O,
\]

we obtain the sharper one-positive-port/one-adverse-port identity

\[
 \boxed{
 \mathfrak P_a^{\rm prime}
 =O_{\rm p}^*O_{\rm p}
  -E_{\rm p}^*E_{\rm p}.
 }
 \tag{L-91414.7}
\]

Thus the two prime endpoint charges of the previous ledger are not independent:
they are one even endpoint port.

## 3. Singular short channel

Corrected `L-91412` uses the direct translation production map

\[
 T_{\rm sh}(u)=S_u f-f
 \tag{L-91414.8}
\]

and the finite no-jump/connection pair `(C,J)`.  Its connection contribution is

\[
 (C-J)^*(C-J)-C^*C-J^*J.
 \tag{L-91414.9}
\]

A second Hadamard rotation gives

\[
 \boxed{
 (C-J)^*(C-J)-C^*C-J^*J
 =\frac12(C-J)^*(C-J)
  -\frac12(C+J)^*(C+J).
 }
 \tag{L-91414.10}
\]

Hence the complete short-channel source, apart from its declared finite
compensation connection, is

\[
 \boxed{
 T_{\rm sh}^*T_{\rm sh}
 +\frac12(C-J)^*(C-J)
 -\frac12(C+J)^*(C+J).
 }
 \tag{L-91414.11}
\]

The adverse short endpoint is one symmetric port, not the two separate ports
`C` and `J`.

## 4. Long channel

The signed long channel enters with the reversed Wick--Green orientation:

\[
 -K^-
 =U_-^*U_-+V_-^*V_--(U_--V_-)^*(U_--V_-).
 \tag{L-91414.12}
\]

Define

\[
 E_-:=\frac{U_-+V_-}{\sqrt2},
 \qquad
 O_-:=\frac{U_--V_-}{\sqrt2}.
 \tag{L-91414.13}
\]

Then

\[
 \boxed{
 -K^-=E_-^*E_- - O_-^*O_-.
 }
 \tag{L-91414.14}
\]

Thus the long channel contributes one positive even endpoint port and one
adverse odd production port.

## 5. Full parity-rotated completed source identity

Retain the compressed-delay leakage, the reflected Hardy orientation, the
bridge coordinates, and the finite completed connection

\[
 \mathcal C_a^\lambda
\]

from `T-91402`.  Apply the same Hadamard rotation to every reflected and bridge
endpoint pair.  Let

\[
 \mathcal P_a^{\rm par}
\]

be the direct-sum Gram of

```text
prime odd production                     O_p;
short translation production             T_sh;
short odd connection                      (C-J)/sqrt(2);
long even endpoint                        E_-;
compressed-delay leakage;
reflected and bridge copies.
```

Let

\[
 \mathcal N_a^{\rm par}
\]

be the direct-sum Gram of

```text
prime even endpoint                       E_p;
short even connection                     (C+J)/sqrt(2);
long odd production                       O_-;
reflected and bridge copies.
```

Then the full delayed screw/Weil packet has the exact identity

\[
 \boxed{
 \mathbb K_a^{\rm del}
 =\mathcal C_a^\lambda
  +\mathcal P_a^{\rm par}
  -\mathcal N_a^{\rm par}.
 }
 \tag{L-91414.15}

Equation (L-91414.15) is equivalent to `T-91402.1`, but it removes every
redundant endpoint coordinate and makes the surviving sign geometry explicit.

## 6. Plastic-aligned domain wall

At the scale

\[
 a_\diamond
 =4.1415673607530469\ldots
\]

of `L-91413`, the sign switch of the continuous completed source and the sign
switch of the physical Cauchy residual occur at the same jump length

\[
 \kappa=\log\varpi.
\]

The short side `0<u<kappa` therefore carries the odd translation-production
geometry of (L-91414.11), while the long side `u>kappa` carries the even
endpoint geometry of (L-91414.14).  The completed continuous source is a
literal parity domain wall:

```text
short jumps:  odd port favourable, even port adverse;
long jumps:   even port favourable, odd port adverse.
```

The finite compensation connection is the boundary coordinate at the wall.
The prime atomic channel remains a separate coupled odd-versus-even pair and
must not be replaced by continuous measure domination (`R-91405`).

## 7. Strategic consequence

CPPD no longer asks for a contraction between two long lists of unrelated
ports.  It asks for one connection-aware parity transfer

\[
 \boxed{
 \mathcal N_a^{\rm par}
 \longrightarrow
 \mathcal C_a^\lambda\oplus
 \mathcal P_a^{\rm par}
 }
 \tag{L-91414.16}

that preserves every packet cross term with coefficient one.

The identity is exact.  Existence of the contraction remains open and is
RH-bearing.