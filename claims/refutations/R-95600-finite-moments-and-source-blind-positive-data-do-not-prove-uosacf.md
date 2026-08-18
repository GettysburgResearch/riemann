# R-95600 — Finite moments and source-blind positive data cannot prove UOSACF

Claim ID: `R-95600`  
Status: **EXACT SCOPE FIREWALL**  
Created: 2026-08-18  
Depends on: exact top Q4 band from PR #580

On

\[
\frac23\le x\le\frac34,
\]

the annular kernels satisfy

\[
J_0(x)=W(x)=\frac{x(1-x)(2x-1)}3\ge\frac2{81},
\qquad
J_1(x)=0.
\tag{R-95600.1}
\]

Replace the actual Möbius signs by \(+1\) on the odd squarefree cores in

\[
\frac{2X}{3}\le m\le\frac{3X}{4}.
\]

This replacement preserves:

```text
all ten activation bands;
all fifteen inner squarefree/coprime moments;
all gcd and ratio constraints;
the complete diagonal;
every source-blind PSD or absolute-value datum;
every local kernel and passive fibre norm.
```

Yet the output satisfies

\[
\sum_{\substack{2X/3\le m\le3X/4\\m\ {\rm odd\ squarefree}}}
\frac{\log m}{\sqrt m}J_0(m/X)
\gg
\sqrt X\log X,
\tag{R-95600.2}
\]

while its diagonal is only \(O(\log^2X)\).

Therefore no argument based solely on the finite inner moments, local
activation geometry, diagonal energy, positive-kernel completion, or
source-blind inequalities can establish UOSACF. The outer Möbius parity must
be used before absolute values.


---
