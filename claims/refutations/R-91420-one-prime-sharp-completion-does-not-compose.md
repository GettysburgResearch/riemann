# R-91420 — The one-prime SHARP-preserving completion does not compose over distinct rough primes

Claim ID: `R-91420`  
Status: **EXACT ALGEBRAIC REFUTATION OF THE CASCADE CLAIM; CORRECTED ONE-PRIME-PER-RESET ROUTE SURVIVES**  
Created: 2026-08-12  
Corrects: the arbitrary-cascade sentence in `L-91325-monotone-transport-disintegration-forgets-rough-colors.md`  
Depends on: `L-91317`, `L-91319`, `L-91327`, `L-91328`  
RH status: **unproved**

## 1. One-prime maps

Put \(r=p^{-1/2}\in(0,1)\). In the physical state \(u=(L,R)^{\mathsf T}\), the exact rough Euler map of `L-91317/L-91319` is

\[
M(r)=
\begin{pmatrix}
1+r-2r^2&-2r(1-r)\\
r(1-r)&(1-r)^2
\end{pmatrix}.
\tag{R-91420.1}
\]

The minimal entrywise nonnegative one-column completion of `L-91319` is

\[
N(r)=
\begin{pmatrix}
1+r-2r^2&0\\
r(1-r)&(1-r)(1-2r)
\end{pmatrix}.
\tag{R-91420.2}
\]

For the SHARP row \(w=(1,2)\),

\[
\boxed{wN(r)=wM(r).}
\tag{R-91420.3}
\]

Thus the completion is exact for one rough factor.

## 2. Two distinct factors

Let \(r=p^{-1/2}\) and \(s=q^{-1/2}\), with \(p,q>1\). Direct multiplication gives

\[
\boxed{
wN(s)N(r)-wM(s)M(r)
=
\left(
0,\,
12rs(1-r)(1-s)
\right).
}
\tag{R-91420.4}
\]

Every factor in the second coordinate is positive. Therefore, for every input with \(R>0\),

\[
wN(s)N(r)u>wM(s)M(r)u.
\tag{R-91420.5}
\]

The one-step identity cannot be iterated by simply multiplying the completed matrices.

## 3. General one-shot completion

For a finite packet with diagonal multipliers

\[
0<B\le A\le1,
\]

the exact physical map is

\[
M(A,B)=
\begin{pmatrix}
2A-B&-2(A-B)\\
A-B&2B-A
\end{pmatrix}.
\tag{R-91420.6}
\]

Among corrections supported in the \(R\)-input column and annihilated by \(w\), the unique minimal correction is

\[
\Delta(A,B)=
\begin{pmatrix}
0&2(A-B)\\
0&-(A-B)
\end{pmatrix}.
\tag{R-91420.7}
\]

It gives

\[
N(A,B)=M(A,B)+\Delta(A,B)
=
\begin{pmatrix}
2A-B&0\\
A-B&3B-2A
\end{pmatrix},
\tag{R-91420.8}
\]

and still

\[
wN(A,B)=wM(A,B).
\tag{R-91420.9}
\]

But \(N(A,B)\) is entrywise nonnegative if and only if

\[
\boxed{3B\ge2A.}
\tag{R-91420.10}
\]

For a product of distinct rough primes,

\[
\frac BA=\prod_{p\in P}\frac{1-p^{-1/2}}{1-p^{-1}}
=\prod_{p\in P}\frac1{1+p^{-1/2}},
\tag{R-91420.11}
\]

which eventually falls below \(2/3\). Hence no global two-state completion in this minimal one-column class can both remain positive and preserve SHARP exactly through arbitrary multiprime products.

## 4. Exact four-state repair

The four-state parity dilation of `L-91327` is not affected. With

\[
z=(X_+,X_-,Y_+,Y_-)^{\mathsf T},
\]

\[
J_4=
\begin{pmatrix}
2&-2&-1&1\\
1&-1&-1&1
\end{pmatrix},
\quad
\widetilde D_4(A,B)=\operatorname{diag}(A,A,B,B),
\tag{R-91420.12}
\]

one has exactly

\[
\boxed{J_4\widetilde D_4(A,B)=M(A,B)J_4.}
\tag{R-91420.13}
\]

Arbitrary distinct-prime composition is therefore exact before projection.

## 5. Consequence for the claimed proof composition

`L-91325-monotone-transport-disintegration-forgets-rough-colors.md` states that the one-prime SHARP identity survives arbitrary completed rough cascades. Equation (R-91420.4) disproves that statement.

This does **not** refute the factor-54 programme. `L-91328` now shows that the intended architecture processes one new least rough prime before contraction. A corrected proof may therefore use the one-prime completion once per generation, provided that the intervening reset is explicitly proved to preserve the native SHARP/capacity ledger.

Until that reset identity is written, the stack is not a complete proof under the project's terminology.

## 6. Correct proof boundary

```text
one-prime positive completion                    EXACT
one-prime SHARP preservation                     EXACT
arbitrary cascade of completed two-state maps    REFUTED
global minimal two-state positivity              FAILS when 3B<2A
four-state rough semigroup                       EXACT
one-prime-per-reset support logic                AVAILABLE
reset-boundary positive projection               OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```
