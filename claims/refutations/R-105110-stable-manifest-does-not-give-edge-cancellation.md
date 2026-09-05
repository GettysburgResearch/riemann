# R-105110 — Stable manifest data do not give individual-edge cancellation

Claim ID: R-105110

Status: **PROPOSED EXACT REFUTATION**

Created: 2026-08-23

Depends on: L-105107; R-105106; L-105109; L-105110

RH status: **unproved**

## Refuted inference

The following implication is false:

> Parity, a complete stable critical-point manifest, fixed target residue
> data, absence of exterior critical points, and bounded optimal selector
> norm force every selector-weighted oriented edge integral to stay bounded.

## Exact counterfamily

For integers \(N\ge1\), let

\[
F_N(z)=
\exp\!\left(\frac{1-e^{-Nz^2}}{2N}\right).
\tag{R-105110.1}
\]

This is real, even, entire, and zero-free.  Moreover,

\[
\frac{F_N'}{F_N}=ze^{-Nz^2},
\qquad
\frac{F_N}{F_N'}=\frac{e^{Nz^2}}z.
\tag{R-105110.2}
\]

Thus \(F_N'\) has exactly the one simple zero \(0\) globally.  The complete
first manifest, target coefficient, and optimal selector are fixed:

\[
\mathcal P_{1,N}=\{0\},
\qquad q_{1,0}=1,
\qquad W_{1,N,*}=1,
\qquad \tau_{1,N}=1.
\tag{R-105110.3}
\]

On the rectangle

\[
\Omega_N=\{z:|\Re z|<1,\ |\Im z|<1/(8N)\},
\tag{R-105110.4}
\]

the upward right edge \(E_N\) satisfies

\[
\boxed{
\left|\int_{E_N}W_{1,N,*}\frac{F_N}{F_N'}\,dz\right|
>\frac{e^N}{5N}>\frac{N^2}{30}.
}
\tag{R-105110.5}
\]

There is no approaching exterior critical point: no other critical point
exists anywhere.  The failure lies entirely in the pole-subtracted
holomorphic remainder.  Nevertheless the residue theorem gives

\[
\frac1{2\pi i}\int_{\partial\Omega_N}
W_{1,N,*}\frac{F_N}{F_N'}\,dz=1.
\tag{R-105110.6}
\]

Hence the other three oriented edges cancel the unbounded right-edge
contribution in the full contour sum.  Full-contour cancellation and
individual-edge cancellation are distinct assertions.

## What is not refuted

L-105110 supplies a valid sufficient estimate after exterior principal parts
are subtracted **and** the remaining edge \(L^1\) norm is bounded.  The family
above violates that remainder hypothesis; it does not refute the theorem.

The family varies with \(N\), is of infinite order, treats the first quotient
only, and uses shrinking-height windows.  It is not Xi and does not refute a
future estimate exploiting fixed-function Xi structure, a cofinal phase
law, or paired-edge cancellation.  No RCMV104530 or RH conclusion follows.
