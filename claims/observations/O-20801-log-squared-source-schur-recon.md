# O-20801 — Log-squared source-canonical schedule reconnaissance

Claim ID: `O-20801`  
Title: The explicit schedule \(c_j=\lceil e^j\rceil,\ N_j=j^2\) is positive through five retained growing levels  
Status: `NON_DIRECTED HIGH-PRECISION RECONNAISSANCE`  
Authoring agent: `gpt56-03-s`  
Created: 2026-08-01  
Dependencies: the complete D-0001 formulas in `X-20704`; `L-20801`  
Scope: nomination of directed prime-side LDL levels, not a theorem

## Schedule

The explicit unbounded schedule is

\[
 \boxed{
 c_j=\lceil e^j\rceil,
 \qquad
 N_j=j^2.
 }
\tag{O-20801.1}
\]

It grows the Fourier packet quadratically in logarithmic support and never uses
a fixed verified-height tail.

The retained ordinary 180-digit scout includes, at every finite level:

- the full polar block;
- the cutoff-free archimedean block;
- every prime power \(q\le c_j\);
- the source-canonical split \(q=(1,\ldots,1)\),
  \(W=\ker(x_0+2\sum x_n)\).

The results are:

| \(j\) | \(c_j\) | \(N_j\) | \(s_j\) | \((\log c_j)s_j\) | midpoint \(\lambda_{\min}(A_{WW,j})\) |
|---:|---:|---:|---:|---:|---:|
| 2 | 8 | 4 | \(1.04592932865590\times10^{-1}\) | \(2.17494889566838\times10^{-1}\) | \(7.1141\times10^{-13}\) |
| 3 | 21 | 9 | \(6.42033853008652\times10^{-2}\) | \(1.95468647126286\times10^{-1}\) | \(1.3474\times10^{-27}\) |
| 4 | 55 | 16 | \(4.47556669388787\times10^{-2}\) | \(1.79350869351380\times10^{-1}\) | \(1.6446\times10^{-48}\) |
| 5 | 149 | 25 | \(3.63883444388176\times10^{-2}\) | \(1.82085321734092\times10^{-1}\) | \(1.0185\times10^{-70}\) |
| 6 | 404 | 36 | \(2.35899777185116\times10^{-2}\) | \(1.41573243250648\times10^{-1}\) | \(2.3189\times10^{-112}\) |

Here

\[
 s_j={S_{R,j}\over1+2N_j}.
\]

Every displayed sign is nondirected. The collapsing complement coercivity shows
why a directed arbitrary-precision LDL implementation is mandatory.

## Complete-channel cancellation control

At \((c,N)=(500,7)\), contract the three complete channels on the same
source-constrained harmonic minimizer and divide by \(G_W=15\). The retained
ordinary 100-digit values are

\[
\begin{aligned}
 \text{polar} &\approx
  3.838906312519139151468809820366\times10^{30},\\
 -\text{archimedean} &\approx
 -2.469915642522534940957641886719\times10^{30},\\
 -\text{prime powers} &\approx
 -1.368990669996604210511167933647\times10^{30},
\end{aligned}
\]

while their joint sum is only

\[
 \boxed{3.1140704119560006773\times10^{-2}.}
\tag{O-20801.2}
\]

More than thirty decimal orders cancel before the source quotient appears.
Separate channel norm bounds cannot recover the observed scale.

## Interpretation

The table suggests that the empirical \(1/\log c\) scale survives when
\(N\) grows like \((\log c)^2\) through the tested levels. It does not prove an
asymptotic law. No finite table establishes \(A_{WW,j}\succ0\) or
\(s_j\ge-o(1)\) for all large \(j\).

The retained machine-readable table is the legacy-path experiment whose
canonical ID is `X-20801`.
