# L-105387 — Corrected compact-scale Xi trigonometric critical-cell theorem

Claim ID: `L-105387`  
Status: **PROVED UNCONDITIONALLY FROM REAL-SADDLE CONCENTRATION; SUPERSEDES L-105386**  
Created: 2026-08-23  
Depends on: `L-105385`; the positive Xi Fourier representation  
RH status: **not assumed**

`L-105386` contains a malformed tag delimiter and is non-normative. This file
is the clean theorem.

## 1. Odd normalization

Let `r` tend to infinity through odd integers, put `F_r=Xi^(r)`, and use the
tilted law `P_(r+1)` of `L-105385`. Define

\[
\omega_r^2=\mathbb E_{r+1}[U^2]
\tag{L-105387.1}
\]

and

\[
\boxed{
G_r^{\rm odd}(y)
={\omega_rF_r(y/\omega_r)\over F_r'(0)}.
}
\tag{L-105387.2}
\]

Then

\[
\boxed{
G_r^{\rm odd}(y)
=
\mathbb E_{r+1}
\left[
{\omega_r\over U}
\sin\left({yU\over\omega_r}\right)
\right].
}
\tag{L-105387.3}
\]

## 2. Even normalization

Let `r` tend to infinity through even integers. Put

\[
\omega_r^2=\mathbb E_{r+2}[U^2]
\tag{L-105387.4}
\]

and

\[
\boxed{
G_r^{\rm even}(y)
={F_r(y/\omega_r)\over F_r(0)}.
}
\tag{L-105387.5}
\]

Since the real-saddle locations for exponents `r` and `r+2` are asymptotic,
under `P_r` one has `U/omega_r -> 1` in every fixed moment. Moreover,

\[
\boxed{
G_r^{\rm even}(y)
=
\mathbb E_r
\left[
\cos\left({yU\over\omega_r}\right)
\right].
}
\tag{L-105387.6}
\]

## 3. Locally uniform complex convergence

The real-saddle tail bounds imply uniform exponential-moment control on every
fixed rescaled vertical strip. Therefore the expectation power series and any
fixed number of derivatives may be passed to the limit locally uniformly in
the complex plane. Thus

\[
\boxed{
G_r^{\rm odd}\to\sin,
\qquad
(G_r^{\rm odd})'\to\cos,
\qquad
(G_r^{\rm odd})''\to-\sin,
}
\tag{L-105387.7}
\]

and

\[
\boxed{
G_r^{\rm even}\to\cos,
\qquad
(G_r^{\rm even})'\to-\sin,
\qquad
(G_r^{\rm even})''\to-\cos.
}
\tag{L-105387.8}
\]

For example, the odd series is

\[
G_r^{\rm odd}(y)
=
\sum_{n\ge0}
{(-1)^ny^{2n+1}\over(2n+1)!}
\mathbb E_{r+1}
\left[(U/\omega_r)^{2n}\right],
\]

and the even series is analogous.

## 4. Fixed critical cells

Fix `J>=1`. For odd derivatives define

\[
y_j^{\rm odd}={\pi(2j+1)\over2},
\qquad 0\le j<J,
\]

and for even derivatives define

\[
y_j^{\rm even}=\pi j,
\qquad 1\le j\le J.
\]

Rouché's theorem on disjoint small circles about these simple zeros of the
limiting derivative gives unique positive critical points `c_(r,j)` of `F_r`
with

\[
\boxed{
\omega_rc_{r,j}\longrightarrow y_j^p
}
\tag{L-105387.9}
\]

for the corresponding parity `p`. Away from those circles, the limiting
derivative is bounded away from zero, so there are no additional critical
points in a fixed compact rescaled interval.

## 5. Fixed-cell residue asymptotics

At `y_(r,j)=omega_r c_(r,j)`, both normalizations give

\[
\boxed{
\rho_{r,j}
={F_r(c_{r,j})\over F_r''(c_{r,j})}
={1\over\omega_r^2}
{G_r(y_{r,j})\over G_r''(y_{r,j})}.
}
\tag{L-105387.10}
\]

Consequently,

\[
\boxed{
\omega_r^2\rho_{r,j}\longrightarrow-1.
}
\tag{L-105387.11}
\]

Every fixed central critical cell is therefore real, simple, and has a
strictly negative residue for all sufficiently high derivative orders.

## 6. Critical-atom convergence

Put

\[
s_{r,j}=c_{r,j}^{-2},
\qquad
W_{r,j}=-{2\rho_{r,j}\over c_{r,j}^2}.
\]

Then

\[
\boxed{
{s_{r,j}\over\omega_r^2}
\longrightarrow{1\over(y_j^p)^2},
\qquad
W_{r,j}
\longrightarrow{2\over(y_j^p)^2}.
}
\tag{L-105387.12}
\]

These are exactly the tangent and cotangent atoms of `L-105382`.

## 7. Scope

The number of cells and the rescaled complex box are fixed before the
derivative limit. No growing-cell, expanding-box, or complete critical-tail
control is proved. The theorem does not establish `CRVH105330`, full critical
capacity, low-order descent, or RH.
