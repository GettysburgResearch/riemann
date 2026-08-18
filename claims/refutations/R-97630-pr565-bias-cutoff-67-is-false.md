# R-97630 — PR #565's `1/40` lower bias from `x>=67` is false

Claim ID: `R-97630`  
Status: **EXACT DIRECTED REFUTATION OF THE PUBLISHED CUTOFF**  
Frozen target: PR #565 at `339e3367660f40c74795802a6f8170b15e19b13a`  
RH status: **unproved**

Let
\[
P_{61}=\prod_{p\le61}p,\qquad
H_x(n)=\min\!\left(\log4,\log\frac xn\right)_+,
\]
and
\[
q_*(2)=15,\quad q_*(3)=6,\quad q_*(4)=3,\quad q_*(m)=6\ (m\ge5).
\]
Put
\[
A_*(x)=\sum_{m\ge2}\frac{q_*(m)}{\sqrt m}H_x(m),
\]
\[
F(x)=\sum_{d\mid P_{61}}\frac{\mu(d)}{\sqrt d}A_*(x/d),\qquad
M(x)=\sum_{d\mid P_{61}}\frac1{\sqrt d}A_*(x/d).
\]

PR #565 claims
\[
\frac1{40}M(x)\le F(x)\qquad(x\ge67).
\]

At the exact endpoint `x=184`, the retained 256-bit outward-rounded certificate gives
\[
F(184)\approx10.6935796487738299508,
\]
\[
M(184)\approx445.8576035426028363156,
\]
and
\[
\boxed{M(184)-40F(184)>18.11.}
\]
The violation is not isolated: integer endpoints `148,...,238` contain failures.
This refutes the cutoff `67`, not positivity of `F`.
