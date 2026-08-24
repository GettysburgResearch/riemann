# L-105330 — The critical-residue Pick form is a shifted-zero derivative

Claim ID: `L-105330`  
Status: **PROVED EXACT AT REGULAR FINITE-CONTOUR SCOPE**  
Created: 2026-08-23  
Depends on: argument principle; `L-105303`; `L-105320`  
RH status: **not assumed**

Let `F` be entire and let `Omega` be a bounded positively oriented contour.
Assume `F'` has no zero on `partial Omega`, every zero of `F'` in `Omega` is
simple, and no such zero is a zero of `F`.  Put

\[
E_\alpha(z)=F'(z)-\alpha F(z).
\tag{L-105330.1}
\]

For sufficiently small complex `alpha`, `E_alpha` is nonzero on the boundary
and its enclosed zeros vary analytically, counted with multiplicity.  For a
function `H` holomorphic near the closed region define

\[
Z_H(\alpha)
={1\over2\pi i}\int_{\partial\Omega}
H(z){E_\alpha'(z)\over E_\alpha(z)}\,dz.
\tag{L-105330.2}
\]

## 1. Exact deformation identity

Since

\[
\partial_\alpha\log E_\alpha=-{F\over E_\alpha},
\]

one has

\[
\partial_\alpha{E_\alpha'\over E_\alpha}
=\left(-{F\over E_\alpha}\right)'.
\]

Differentiation under the contour and integration by parts give

\[
\boxed{
Z_H'(0)
={1\over2\pi i}\int_{\partial\Omega}
H'(z){F(z)\over F'(z)}\,dz.}
\tag{L-105330.3}

Equivalently, if the zeros of `F'` are `c`,

\[
\boxed{
Z_H'(0)
=\sum_{F'(c)=0}H'(c){F(c)\over F''(c)}.}
\tag{L-105330.4}

The same formula follows from the implicit derivative

\[
c'(0)={F(c)\over F''(c)}.
\]

## 2. Exact recovery of the Pick matrix

Let `phi_1,...,phi_d` be source-fixed holomorphic observation functions and
let `W` be a source-fixed holomorphic function nonzero at the critical points.
Choose primitives `H_ij` satisfying

\[
H_{ij}'(z)=-W(z)^2\phi_i(z)\phi_j(z).
\tag{L-105330.5}

Then

\[
\boxed{
Z_{H_{ij}}'(0)
=-{1\over2\pi i}\int_{\partial\Omega}
{F\over F'}W^2\phi_i\phi_j
}
\tag{L-105330.6}

is exactly the Wick-preconditioned critical-residue matrix entry.  Thus the
entire low-order Hermite--Pick compression is one parameter derivative of the
zero statistic for `F'-alpha F`.

The choice of additive constant in `H_ij` is irrelevant because the number of
enclosed zeros is locally constant in `alpha`, so the derivative of a constant
times that count is zero.

## 3. Confluent scope

If an enclosed zero of `F'` is multiple, (L-105330.3) remains the correct
contour identity.  Its local expansion gives the confluent jet blocks of
`L-105310`.  The simple-zero statement above is sufficient for the exact
source calculation; multiplicities are charged by `L-105311`.

## 4. Meaning

The low-order Pick matrix is not an unrelated zero statistic.  It is the
linear response of the xi-prime zero configuration to the natural perturbation
`F' -> F'-alpha F`.
