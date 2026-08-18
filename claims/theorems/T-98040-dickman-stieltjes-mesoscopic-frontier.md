# T-98040 — Dickman–Stieltjes mesoscopic factor-67 frontier

Claim ID: `T-98040`<br>
Status: **UNCONDITIONAL POSITIVITY THEOREM; DEEP CRITICAL PRODUCER OPEN**<br>
Created: 2026-08-18<br>
Depends on: `L-98040--L-98042`; PR #603; the fixed scalar consumer<br>
RH status: **unproved**

For the literal native state

\[
\mathcal F(Y,z)=
\sum_{P^-(m)\ge z}{\mu(m)\over\sqrt m}b(Y/m),
\qquad
u={\log Y\over\log z},
\]

there is an absolute constant `c_0>0` such that

\[
\boxed{
2\le u\le
c_0(\log Y)^{3/8}(\log\log Y)^{-3/4}
\quad\Longrightarrow\quad
\mathcal F(Y,z)>0
}
\tag{T-98040.1}
\]

uniformly for all sufficiently large `Y`.

The exact mechanism is

\[
{\mathcal F(Y,z)\over\sqrt Y}
=
\underbrace{\int\rho(u-\log x/\log z)\,dh(x)}_{
 a_*\rho(u)(1+o(1))>0}
+
\underbrace{O\!\left(
 u e^{-c(\log z)^{3/5}(\log\log z)^{-1/5}}
\right)}_{
 o(\rho(u))}.
\]

Thus the complete bounded `P_61` source remainder is absorbed into the positive
continuous profile. A negative state, if one exists, must lie in the deeper
corridor

\[
\boxed{
{\log Y\over\log z}
\gg
{(\log Y)^{3/8}\over(\log\log Y)^{3/4}}.
}
\tag{T-98040.2}
\]

This packet retains the live conclusion boundary:

```text
all fixed-power states                         POSITIVE
PR #603 near-critical logarithmic corridor     POSITIVE
new mesoscopic Stieltjes corridor               POSITIVE
centered polylog boundary correction            RETAINED
fixed/small least-prime root                     OPEN / RH-BEARING
GPC67                                           OPEN
Riemann Hypothesis                              UNPROVED
```

The remaining conclusion-producing theorem is still the native zero-hinge
producer `GPC67`, equivalently its exact root Type-II/Bellman formulation. The
new result removes every state below the mesoscopic depth (T-98040.2); it does
not rename the surviving root sign as a proof.
