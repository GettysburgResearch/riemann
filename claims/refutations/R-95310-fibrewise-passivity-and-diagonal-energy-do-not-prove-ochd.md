# R-95310 — Fibrewise passivity and diagonal energy do not prove OCHD

Claim ID: `R-95310`  
Status: **EXACT SOURCE-BLIND FIREWALL**  
Created: 2026-08-17  
Depends on: `L-95310/L-95311`; PR #563

On the interval

\[
\frac23\le x\le\frac34,
\]

all scaled terms \(W(2^rx)\) with \(r\ge1\) vanish. Hence

\[
K_0(x)=W(x),
\qquad
K_1(x)=0.
\tag{R-95310.1}
\]

On this interval,

\[
W(x)=\frac{x(1-x)(2x-1)}3
\ge\frac2{81}.
\tag{R-95310.2}
\]

Replace the actual Möbius signs temporarily by \(+1\) on the odd squarefree
cores in

\[
\frac{2X}{3}\le m\le\frac{3X}{4}.
\]

Every fibrewise state identity, passive norm and diagonal square estimate is
unchanged by this sign replacement. However the critical observation is at
least

\[
\frac2{81}
\sum_{\substack{2X/3\le m\le3X/4\\m\ {\rm odd\ squarefree}}}
\frac{\log m}{\sqrt m}
\gg
\sqrt X\log X,
\tag{R-95310.3}
\]

using the elementary positive density of odd squarefree integers.

At the same time its diagonal square is only \(O(\log^2X)\) on this block.

Therefore:

\[
\boxed{
\text{fibrewise passivity}
+
\text{polylog diagonal energy}
\not\Longrightarrow
\text{critical deterministic output control}.
}
\tag{R-95310.4}
\]

The actual Möbius signs, and specifically their cross-core cancellation, are
load bearing.
