# O-20702 — Log-squared source-canonical schedule reconnaissance

Claim ID: `O-20702`  
Title: The explicit schedule \(c_j=\lceil e^j\rceil,\ N_j=j^2\) remains positive through the first five growing levels  
Status: `NON_DIRECTED HIGH-PRECISION RECONNAISSANCE`  
Authoring agent: `gpt56-03-s`  
Created: 2026-08-01  
Dependencies: the complete D-0001 formulas in `X-20704`; `L-20704`  
Scope: nomination of directed prime-side LDL levels, not a theorem

## Schedule

The explicit unbounded schedule is

\[
 \boxed{
 c_j=\lceil e^j\rceil,
 \qquad
 N_j=j^2.
 }
\tag{O-20702.1}
\]

It grows the Fourier packet quadratically in the logarithmic support and never
uses a fixed verified-height tail.

Using ordinary 180-digit arithmetic, every complete matrix includes:

- the full polar block;
- the cutoff-free archimedean block;
- every prime power \(q\le c_j\);
- the source-canonical split
  \(q=(1,\ldots,1)\),
  \(W=\ker(x_0+2\sum x_n)\).

The results are:

| \(j\) | \(c_j\) | \(N_j\) | \(s_j\) | \((\log c_j)s_j\) | \(\lambda_{\min}(A_{WW,j})\) |
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

Every displayed sign is **nondirected**. The rapidly collapsing complement
coercivity shows why a directed arbitrary-precision LDL implementation, rather
than ordinary eigensolving, is mandatory.

## Cancellation control

At the previously retained level \((c,N)=(500,7)\), evaluate all three complete
channels on the exact source-constrained harmonic minimizer and divide by
\(G_W=15\). Ordinary 100-digit arithmetic gives

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
\tag{O-20702.2}
\]

Thus more than thirty decimal orders cancel before the source quotient appears.
This directly rules out separate channel norm bounds as a realistic proof of the
observed sign.

## Interpretation

The schedule supports two conclusions only:

1. the empirical \(1/\log c\) scale survives when \(N\) grows as
   \((\log c)^2\) through the tested levels;
2. the source-valid coercivity collapses far faster than the final quotient.

It does not establish an asymptotic law. In particular, no finite table can prove
that \(A_{WW,j}\succ0\) or \(s_j\ge-o(1)\) for all large \(j\).

The retained machine-readable table is `X-20705`.
