# L-102957 — The exceptional large-co-owner Boolean balanced sector is empty

Claim ID: `L-102957`  
Status: **PROVED EXACT COFINAL REGIME ELIMINATION**  
Created: 2026-08-25  
Depends on: PR #751 `L-106080--L-106081`; `L-102955`  
RH status: **not assumed**

Work on one dyadic physical horizon

\[
Y\le X<2Y
\]

with the frozen Boolean Vaughan cutoff

\[
U=\lfloor Y^{1/6}\rfloor.
\]

Let one nonzero balanced source atom have physical form

\[
N=\lambda\Lambda a^2,
\qquad \lambda<\Lambda,
\qquad N\le16Y.
\]

The Boolean balanced coefficient contains disjoint factors

\[
r>U,
\qquad s>U,
\qquad(r,s)=1,
\]

inside the literal squarefree core. Consequently

\[
\boxed{a\ge rs\ge(U+1)^2>Y^{1/3}.}
\tag{L-102957.1}
\]

Suppose the exceptional horizon case of `L-106081` occurs:

\[
\Lambda>4\sqrt Y.
\]

The support inequality then gives

\[
\lambda a^2
\le {16Y\over\Lambda}
<4\sqrt Y.
\tag{L-102957.2}
\]

But \(\lambda\ge2\), and (L-102957.1) gives

\[
\lambda a^2
>2Y^{2/3}.
\]

For \(Y>64\),

\[
2Y^{2/3}>4Y^{1/2},
\]

contradicting (L-102957.2). Therefore

\[
\boxed{
Y>64
\quad\Longrightarrow\quad
\text{no Boolean balanced atom contains a label }\Lambda>4\sqrt Y.
}
\tag{L-102957.3}

The finite range \(Y\le64\) belongs to the already-declared terminal packet.

## Consequences

Every cofinal Boolean balanced atom lies in the no-exception regime. Hence the selected owner pair consists of the two smallest physical-prime labels. Every core prime is at least the larger owner \(\Lambda\). Since the core contains two distinct primes,

\[
\boxed{
\Lambda^2\le a,
\qquad
P:=\lambda\Lambda\le a.
}
\tag{L-102957.4}

Thus the two-way split `MOBOSM-NE/MOBOSM-EX` in `T-106081` collapses cofinally to its no-exception part; the exceptional subtarget is finite and does not carry a tail theorem.

This eliminates a full owner regime. It does not estimate coherent aggregation over the remaining no-exception owner pairs.