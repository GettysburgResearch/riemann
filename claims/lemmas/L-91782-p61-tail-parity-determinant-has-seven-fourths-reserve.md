# L-91782 — The `P_61` parity-prefix determinant has a `7/4` reserve above `166000`

Claim ID: `L-91782`  
Status: **PROVED EXACT/DIRECTED TAIL-ARITHMETIC RESERVE**  
Created: 2026-08-15  
Replay: `X-91780-target-lorenz-compact-avlt`  
RH status: **unproved**

For a real prefix `z` define

\[
 A_e(z)=\sum_{\substack{d|P_{61}\\d\le z\\\mu(d)=1}}\frac1d,
 \quad
 A_o(z)=\sum_{\substack{d|P_{61}\\d\le z\\\mu(d)=-1}}\frac1d,
\]

\[
 B_e(z)=\sum_{\substack{d|P_{61}\\d\le z\\\mu(d)=1}}\frac1{\sqrt d},
 \quad
 B_o(z)=\sum_{\substack{d|P_{61}\\d\le z\\\mu(d)=-1}}\frac1{\sqrt d}.
\]

Then

\[
 \boxed{
 \Delta(z)=A_e(z)B_o(z)-A_o(z)B_e(z)>\frac74
 \qquad(z\ge166000).
 }
\tag{L-91782.1}
\]

The proof enumerates all `2^18` divisor-prefix states. Rational `A` sums are
exact. Every inverse square root is enclosed by integer square comparison at
fixed denominator `10^60`; the determinant lower endpoint uses

\[
 A_e B_o^{\rm lo}-A_o B_e^{\rm hi}.
\]

There are `259133` states meeting the tail condition. The minimum begins at
prefix `168113` and has directed lower value

\[
 1.7529746231757814\ldots>\frac74.
\]

This reserve is the leading arithmetic coefficient in an Euler--Green attack
on the unbounded proportional determinant. It does **not** by itself control
the component-row boundary packet, the causal child correction, or the native
root ledger; no analytic-tail AVLT theorem is claimed here.
