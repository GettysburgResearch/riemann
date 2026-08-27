# L-105386 — High Xi derivatives converge to trigonometric critical cells on every fixed rescaled disk

Claim ID: `L-105386`  
Status: **PROVED UNCONDITIONALLY FROM REAL-SADDLE CONCENTRATION — REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105385`; the positive Xi Fourier representation  
RH status: **not assumed**

## 1. Odd derivative normalization

Let `r` tend to infinity through odd integers and put

\[
F_r(z)=\Xi^{(r)}(z).
\]

Use the tilted law `P_(r+1)` of `L-105385` and define

\[
\omega_r^2=\mathbb E_{r+1}[U^2].
\tag{L-105386.1}
\]

Since `F_r'(0)\ne0`, define

\[
\boxed{
G_r^{\rm odd}(y)
={\omega_rF_r(y/\omega_r)\over F_r'(0)}.
}
\tag{L-105386.2}
\]

The positive Fourier representation gives the exact expectation

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
\tag{L-105386.3}
\]

## 2. Even derivative normalization

Let `r` tend to infinity through even integers. Put

\[
\omega_r^2=\mathbb E_{r+2}[U^2].
\tag{L-105386.4}
\]

The real-saddle locations for exponents `r` and `r+2` are asymptotic, so under
the law `P_r`,

\[
U/\omega_r\longrightarrow1
\]

in every fixed positive and negative moment. Define

\[
\boxed{
G_r^{\rm even}(y)
={F_r(y/\omega_r)\over F_r(0)}.
}
\tag{L-105386.5}
\]

Then

\[
\boxed{
G_r^{\rm even}(y)
=
\mathbb E_r
\left[
\cos\left({yU\over\omega_r}\right)
\right].
}
\tag{L-105386.6}
\]

## 3. Compact complex convergence with derivatives

For every fixed `R,H>0`, the real-saddle tail estimates imply a uniform bound
on

\[
\mathbb E_s\exp(HU/\omega_r)
\]

in the relevant tilted laws. Together with the fixed-moment convergence of
`L-105385`, the power series in (L-105386.3) and (L-105386.6) may be passed to
the limit uniformly on

\[
|\operatorname{Re}y|\le R,
\qquad
|\operatorname{Im}y|\le H.
\]

The same is true after any fixed number of `y` derivatives. In particular,

\[
\boxed{
G_r^{\rm odd}(y)
\longrightarrow\sin y,
\qquad
(G_r^{\rm odd})'(y)
\longrightarrow\cos y,
\qquad
(G_r^{\rm odd})''(y)
\longrightarrow-\sin y,
}
\tag{L-105386.7}
\]

and

\[
\boxed{
G_r^{\rm even}(y)
\longrightarrow\cos y,
\qquad
(G_r^{\rm even})'(y)
\longrightarrow-\sin y,
\qquad
(G_r^{\rm even})''(y)
\longrightarrow-\cos y.
}
\tag{L-105386.8}
\]

All convergence is locally uniform in the complex plane.

### Direct series justification

For odd derivatives,

\[
G_r^{\rm odd}(y)
=
\sum_{n\ge0}{(-1)^ny^{2n+1}\over(2n+1)!}
\mathbb E_{r+1}
\left[(U/\omega_r)^{2n}\right].
\]

For even derivatives,

\[
G_r^{\rm even}(y)
=
\sum_{n\ge0}{(-1)^ny^{2n}\over(2n)!}
\mathbb E_r
\left[(U/\omega_r)^{2n}\right].
\]

The exponential-moment bound dominates these series on compact sets, while
each fixed coefficient tends to one.

## 4. Fixed critical cells

Fix `J>=1`.

For odd derivatives, let

\[
y_j^{\rm odd}={\pi(2j+1)\over2},
\qquad 0\le j<J.
\]

For even derivatives, let

\[
y_j^{\rm even}=\pi j,
\qquad 1\le j\le J.
\]

Hurwitz's theorem, or Rouché's theorem on disjoint small circles around these
simple zeros of cosine or sine, gives unique positive critical points
`c_(r,j)` of `F_r` such that

\[
\boxed{
\omega_rc_{r,j}\longrightarrow y_j^p
}
\tag{L-105386.9]
\]

for the corresponding parity `p`. The normative clean formula is

\[
\boxed{
\omega_rc_{r,j}\longrightarrow y_j^p.
}
\tag{L-105386.9}
\]

There are no additional critical points in any fixed compact rescaled interval
once the small critical disks are removed, because the limiting derivative is
bounded away from zero there.

## 5. Fixed-cell residue asymptotics

At a critical point `c_(r,j)`, put `y_(r,j)=omega_r c_(r,j)`. In both parities,
the scaling gives

\[
\boxed{
\rho_{r,j}
={F_r(c_{r,j})\over F_r''(c_{r,j})}
={1\over\omega_r^2}
{G_r(y_{r,j})\over G_r''(y_{r,j})}.
}
\tag{L-105386.10}
\]

Using (L-105386.7)--(L-105386.9),

\[
\boxed{
\omega_r^2\rho_{r,j}\longrightarrow-1.
}
\tag{L-105386.11}
\]

In particular, every fixed central critical cell is real, simple and has a
strictly negative residue for all sufficiently high derivative orders.

## 6. Critical atom convergence

Define

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
\tag{L-105386.12}
\]

These limits are exactly the tangent and cotangent atoms of `L-105382`.

## 7. Scope

The number `J` and the rescaled complex box are fixed before the derivative
limit. The theorem gives no control when `J` grows with `r`, no complete
real-rootedness in an expanding box, and no tail estimate for all critical
atoms. The initial malformed tag display in (L-105386.9) is immediately
superseded by the clean repeated formula and must not be cited. The theorem
does not prove `CRVH105330`, full critical capacity, low-order descent, or RH.
