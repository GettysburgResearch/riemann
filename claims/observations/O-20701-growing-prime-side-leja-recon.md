# O-20701 — Growing complete prime-side packets under rational-Leja framing

Claim ID: `O-20701`  
Status: `NON_DIRECTED HIGH-PRECISION RECONNAISSANCE`  
Authoring agent: `gpt56-03-r`  
Created: 2026-08-01  
Experiment: `X-20704`

## Complete source

The experiment evaluates

\[
A_{N,c}^{\rm pole}
+A_{N,c}^{\rm arch}
+A_{N,c}^{\rm pp}
\]

with every prime power \(q\le c\), then constructs the first and conditional
second frames by the product formulas of `L-20701/L-20702`.

No absolute zero tail is used in the matrix value.

## Retained ladder

| \(c\) | \(N\) | prime powers | first-frame zero indices | conditional zero | complete Schur floor |
|---:|---:|---:|---|---:|---:|
| 5 | 1 | 4 | 1 | 3 | `5.71566363185582e-5` |
| 10 | 2 | 7 | 2,1 | 9 | `5.33728373245523e-9` |
| 20 | 3 | 12 | 1,4,22 | 2 | `4.34686257296169e-14` |
| 50 | 4 | 23 | 1,3,7,2 | 24 | `3.38306171806071e-18` |
| 100 | 5 | 35 | 1,2,6,3,19 | 4 | `1.79592080793679e-22` |
| 200 | 6 | 60 | 2,1,7,4,23,3 | 12 | `2.49629933812205e-27` |
| 500 | 7 | 114 | 5,2,1,21,3,9,65 | 4 | `4.81980622711246e-33` |

Every midpoint complete Schur pivot is positive.

## Frame behavior

The rational-Leja pivots remain on ordinary scales—roughly between
\(3\times10^{-3}\) and \(10^{-1}\)—through \(N=7\). In contrast, the
unnormalized kernel coefficient metric reaches approximately

\[
2.55\times10^{30}
\]

at \((c,N)=(500,7)\).

This confirms the distinction:

```text
raw Cauchy coordinate condition:
    artificial and removable by exact products;

kernel metric / selected-frame ratio:
    intrinsic and must be retained.
```

## Joint residual

At every retained level,

\[
S_{N,c}
=
P_{Y\mid Z}+R_{Y\mid Z}^{\rm corr}
\]

was assembled numerically. The residual is positive in this particular ladder,
but its scale is comparable to the final Schur floor. It cannot be replaced by
a coarse absolute norm.

At \((500,7)\),

\[
\begin{aligned}
\text{selected frame ratio}&\approx1.18896\times10^{-33},\\
\text{joint residual ratio}&\approx3.63085\times10^{-33},\\
\text{complete Schur floor}&\approx4.81981\times10^{-33}.
\end{aligned}
\]

## Natural support experiment

A separate midpoint sweep with \(c=N\), \(2\le N\le12\), also gives positive
complete Schur pivots. This geometry is better aligned with the normalized
zero/pole lattice because \(L=\log c\asymp\log N\).

One level, \((c,N)=(3,3)\), has a **negative joint residual after selected-line
subtraction** even though the complete Schur pivot stays positive. This is a
useful strict control: selected mass and residual must be combined before a
verdict.

## Classification

These values are scheduling evidence only:

- mpmath special functions;
- nondirected zeta ordinates;
- ordinary high-precision eigensolves.

The next directed targets are the small polynomial-support levels, beginning
with \((c,N)=(2,2),(3,3),(4,4)\), because they stress both the positive and
negative joint-residual cases.
