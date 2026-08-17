# L-97203 — The 5:3 rough defect has a positive Julia Gram and an exact small-Fourier cone

Claim ID: `L-97203`  
Status: **PROVED EXACT GLOBAL-IN-R FINITE THEOREM**  
Created: 2026-08-17  
Depends on: `L-97200/L-97201`; the one-prime commutator correction announced in PR #564  
Scope: every finite rough set satisfying the stated mass inequality; not the cofinal rough product  
RH status: **not assumed**

Let

\[
B(u)=\min(2\log2,u)_+,
\]

and put

\[
\phi_*(u)
=6B(u)-\frac9{\sqrt2}B(u-\log2)
+\frac32B(u-2\log2).
\tag{L-97203.1}
\]

Direct evaluation at the breakpoints proves

\[
\boxed{0\le\phi_*(u)\le6\log2.}
\tag{L-97203.2}
\]

Its three nontrivial lower margins are

\[
12-\frac9{\sqrt2},
\qquad
\frac{27}{2}-9\sqrt2,
\qquad
15-9\sqrt2,
\]

all strictly positive. For \(u\ge4\log2\),

\[
\phi_*(u)=(15-9\sqrt2)\log2=:c_*.
\tag{L-97203.3}
\]

For a finite rough set \(R\), define

\[
\psi_{*,X}(d)=d^{-1/2}\phi_*\!\left(\log\frac Xd\right),
\]

\[
B_{R,X}=\sum_{(n,R)=1}n^{-1/2}H_X(n),
\qquad
D_{R,X}=\sum_{d\mid R}\mu(d)\psi_{*,X}(d).
\]

The rough-only 5:3 state is exactly

\[
\boxed{A^*_{R,X}=6B_{R,X}-D_{R,X}.}
\tag{L-97203.4}
\]

## Positive Julia object

For each divisor \(d\mid R\), the matrix

\[
\psi_{*,X}(d)
\begin{pmatrix}1&\mu(d)\\\mu(d)&1\end{pmatrix}
\]

is positive semidefinite. Hence

\[
\boxed{
J^*_{R,X}
=\sum_{d\mid R}\psi_{*,X}(d)
\begin{pmatrix}1&\mu(d)\\\mu(d)&1\end{pmatrix}
\succeq0.
}
\tag{L-97203.5}
\]

Its off-diagonal is exactly \(D_{R,X}\). Moreover,

\[
\boxed{
\sum_{d\mid R}\psi_{*,X}(d)^2
\le36(\log2)^2(1+\log X).
}
\tag{L-97203.6}
\]

This improves the loose `441(1+log X)` envelope while preserving the same
scientific boundary: PSD trace does not itself give a trace-free extraction.

## Small-Fourier cone

Put

\[
\sigma(R)=\sum_{p\in R}p^{-1/2}.
\]

If \(X<67\), no nontrivial rough divisor is active and the positive unsieved
source gives \(A^*_{R,X}\ge0\). If \(X\ge67\), then \(B_{R,X}\ge\log4\), the
root term equals \(c_*\), and dropping the negative odd-parity terms gives

\[
D_{R,X}
\le c_*+6\log2\sum_{k\ge1}e_{2k}(p^{-1/2}:p\in R).
\]

Since \(e_m\le\sigma(R)^m/m!\),

\[
D_{R,X}
\le c_*+6\log2\bigl(\cosh\sigma(R)-1\bigr).
\tag{L-97203.7}
\]

Therefore

\[
\boxed{
\sigma(R)\le
\operatorname{arcosh}\!\left(\frac{1+3\sqrt2}{2}\right)
\Longrightarrow
A^*_{R,X}\ge0\quad\text{for every }X\ge1.
}
\tag{L-97203.8}
\]

The exact rational Taylor certificate in `X-97200` proves that every set of at
most thirteen primes at least 67 lies in this cone. This closes accumulated
parity through thirteen arbitrary rough colours, not merely through a fixed
depth fixture.

The cone condition is sufficient, not necessary. It does not cover the cofinal
rough product and is not RH.
