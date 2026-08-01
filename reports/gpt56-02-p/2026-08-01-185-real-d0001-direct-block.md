# 2026-08-01 — First directed real-block shorting certificate

## Outcome

The `c=5, N=1` cutoff-free D-0001 even block has now been emitted in the exact
`L-18512` production schema and certified directly. The artifact contains the
requested inclusion, local/prime decomposition, cross, positive-sector block,
trial solve, solve residual, and metric:

\[
Q_W,\quad P_W,\quad E_W,\quad Z_W,\quad C,\quad X_N,\quad
\mathscr R_N,\quad G_W.
\]

With `M=G_E`, `h=10^{-5}`, and `X_N=0`, the directed lower matrix is

\[
\mathscr D_N=B_W-h^{-1}\mathscr R_N^*M^{-1}\mathscr R_N.
\]

The 256/384-bit directed ladders are nested entrywise, and the exact rational consumer proves

\[
\mathscr D_N-\frac14G_W\succ0,
\]

with normalized pivot lower endpoint

\[
0.010761628789247937732328\ldots>0.
\]

Consequently

\[
\Delta_{5,1}=0
\]

for this real finite packet. The exact Schur floor itself has directed lower
endpoint

\[
0.260766206605644581023310\ldots.
\]

## Why the intentionally crude solve works

The selected integer basis nearly diagonalizes the real D-0001 matrix. The
directed special-function intervals do not even resolve the sign of the tiny
cross `Z_W`; nevertheless the complete worst-case residual penalty is small
enough that the `m=1/4` LDL moat survives. This makes the result robust to both
special-function tail width and solve error.

## Production significance

The artifact demonstrates that the direct-shortening pipeline is executable on
real zeta arithmetic. It also identifies the precise remaining data problem:
the repository must export the same objects for the **canonical augmented
Suzuki packet**, rather than only this first finite D-0001 calibration block.
Once exported, the checker is unchanged.

No inference from this single positive level to a cofinal lower envelope is
made. RH is not claimed proved.
