# T-104570 — Corrected modular-scalar and adaptive-cofinal frontier

Claim ID: `T-104570`  
Status: **UNCONDITIONAL HARDENING + TWO CORRECTED SUFFICIENT GATES**  
Created: 2026-08-23  
Depends on: `T-104550`, `L-104531--L-104536`, `R-104517`, `R-104518`  
RH status: **unproved**

## 1. What the hostile reconstruction changed

The two original implementations of the fixed-order route were too strong in
incompatible ways.

1. Every finite mixed theta matrix with at least two orbits is indefinite at
   `t=0`; full matrix PSD is false.
2. Every fixed raw orbit cutoff has an eventually negative algebraic Laguerre
   tail; fixed-`N` cofinal certification is false.

Neither result refutes the complete scalar profile

\[
\mathcal L_2(t)
=\Xi'''(t)^2-\Xi''(t)\Xi''''(t).
\]

They identify the modular cancellations which a valid proof must retain.

## 2. Route A — complete modular scalar

The carrier-subtracted Jacobi mother

\[
\mathcal B(u)=e^{u/2}\vartheta(e^{2u})-2\cosh(u/2)
\]

is even and decaying, and

\[
u^2\Phi(u)=\frac{u^2}{4}(D^2-1/4)\mathcal B(u).
\]

`L-104534` integrates this complete source before orbit splitting and produces
one exact scalar modular quartic for the associated kernel `K_2`.

`L-104536` further gives

\[
\mathcal K_2(x)
=x^4\mathcal H_1(x)-2x^2\mathcal H_2(x)+\mathcal H_3(x)
\]

and the equivalent sine-tail condition

\[
\int_0^\infty\mathcal G_2(x)\sin(2tx)\,dx
\le \frac{A_2}{2t}
\qquad(t>0).
\]

Define

```text
MSINE104570 — complete modular sine-tail theorem

The displayed sine-tail inequality holds for every t>0, with G_2 formed from
the complete untruncated Jacobi source.
```

Then

\[
\boxed{
\mathrm{MSINE104570}
\Longrightarrow
\mathcal L_2(t)\ge0\quad(t\in\mathbb R).
}
\tag{T-104570.1}
\]

Unconditionally, the branch also proves the central interval

\[
|t|<\sqrt{\frac{2\mu_0\mu_2}{\mu_0\mu_4-\mu_2^2}}.
\]

## 3. Route B — adaptive directed cofinal margins

Raw finite orbit sums are forbidden by `R-104518`.  `L-104535` constructs a
jet-renormalized cutoff `G_tilde_(N,R)` satisfying

\[
\|(1+|u|)^J(\widetilde G_{N,R}-g)\|_1
\le C_{J,R}N^{C_{J,R}}e^{-\pi N^2}
\]

and cancels all odd modular jets through order `2R+1`.

Define

```text
ACDM104570 — adaptive cofinal directed-margin theorem

There exist overlapping compact intervals I_j whose union is R and parameters
N_j -> infinity, R_j -> infinity such that a directed proof gives

  min_(t in I_j) Lambda_tilde_(N_j,R_j)(t) > epsilon_j,

where epsilon_j is an explicit upper bound for the complete-source comparison
error on I_j.
```

Then

\[
\boxed{
\mathrm{ACDM104570}
\Longrightarrow
\mathcal L_2(t)>0\quad(t\in\mathbb R).
}
\tag{T-104570.2}
\]

The recommended implementation evaluates the complete modular mother near the
fixed point and uses orbit tails only away from it; the jet-renormalized source
is a finite fail-closed surrogate for that hybrid computation.

## 4. Fixed-order reverse-Rolle consequence

By `T-104550`, either corrected gate gives

\[
\boxed{
\alpha_2\ge\alpha_3>0.9873,
}
\tag{T-104570.3}
\]

where the right-hand input is Conrey's fixed-order third-derivative theorem.
This would be a genuine descent from `xi'''` to `xi''`, not use of Conrey's
independent `alpha_2>0.9584` row.

## 5. Current scientific boundary

```text
complete modular integration by parts          PROVED EXACT
three-associated-kernel compression             PROVED EXACT
symbolic central positivity interval            PROVED EXACT
finite mixed-matrix PSD                          FALSE
fixed raw cutoff cofinality                      FALSE
jet-renormalized adaptive cutoff                 PROVED EXACT
MSINE104570                                      OPEN
ACDM104570                                       OPEN
alpha_2 >= alpha_3 from alpha_3                   NOT YET ESTABLISHED
Riemann Hypothesis                               UNPROVED
```

The two live routes are now logically disjoint:

- Route A is a pen-and-paper scalar theta inequality.
- Route B is a complete-source directed cofinal certificate.

Neither may fall back to independent local PSD ports or a fixed orbit cutoff.