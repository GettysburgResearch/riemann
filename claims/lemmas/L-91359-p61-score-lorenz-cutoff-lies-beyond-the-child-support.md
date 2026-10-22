# L-91359 — The P61 score-Lorenz cutoff lies beyond the child support

Claim ID: `L-91359`  
Status: **PROVED EXACT SUPPORT-SEPARATION THEOREM; DIRECTED BASE REPLAY PROVIDED**  
Created: 2026-08-13  
Frozen input: PR #439 at `87c34e48b5839e81183302a4f2c48a83bb5c38a6`  
Depends on: `L-91328`, `L-91345`, `L-91348`, `L-91358`, `X-91136`  
RH status: **unproved**

Let `P=P_61`, `p>=67`, `1<=y<=67`, `x=py`, and let `E_S,O_S` be the positive even and odd causal score measures

\[
K_S(d)=W_S(x,d)-p^{-1/2}W_S(y,d).
\]

The score-Lorenz cutoff is strictly larger than `y` once

\[
|O_S|>E_S([1,y]).
\]

Write `s=sqrt(p)` and `u=sqrt(y)`. Define reciprocal prefixes `A_E,A_O` and inverse-square-root prefixes `B_E,B_O`. Exact enumeration of all P61 divisor states and every one-sided breakpoint in `1<=y<=67` proves

\[
A_O(67y)-A_E(y)>3/8.
\]

The exact minimum is

\[
\frac{3493838105587227913831}{9022183181492843921790}
\]

at the right-hand state `y=65`.

Put

\[
G(s,y)=|O_S|-E_S([1,y]).
\]

Between parent activations,

\[
\partial_sG
=5u[A_O(s^2y)-A_E(y)]-s^{-2}\mathfrak S_{61}(y).
\]

The positive Euler corridor gives `0<mathfrak S_61(y)<5u`; hence

\[
\partial_sG>5u(3/8-1/67)>0.
\]

Every new odd parent activation creates an upward jump, so `G` increases for all `s>=sqrt(67)`.

The directed base replay at `p=67` checks 354 real breakpoints and both one-sided states. It proves

\[
G(\sqrt{67},y)>19
\qquad(1<=y<=67),
\]

with minimum lower endpoint above `19.792707960495` at `y=1` from the right. Therefore

\[
\boxed{c_{Lorenz}>y}
\]

for every real `p>=67` and `1<=y<=67`.

Every Lorenz residual source is consequently in the outer regime. Its child subtraction vanishes and

\[
\frac{K_R(d;j)}{K_S(d)}
=
\frac{Q_{py/d}(j)}{5\sqrt{py/d}-3}.
\]

Together with `L-91358`, the unresolved row family has `y<c<2000`. `L-91360` supplies global monotonicity of the displayed outer ratio.

Replay:

```bash
cd experiments/X-91136-p61-score-lorenz-cutoff-beyond-child
python3 verify.py
```

```text
PASS_P61_SCORE_LORENZ_CUTOFF_BEYOND_CHILD
```

Boundary:

```text
cutoff c>y                                  PROVED
inner residual regime                       ELIMINATED
outer normalized row order                  L-91360
common literal-row subordination            OPEN / LRPT
Riemann Hypothesis                          UNPROVEN
```
