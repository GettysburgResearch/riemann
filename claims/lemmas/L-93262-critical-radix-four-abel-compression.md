# L-93262 — Critical radix-four Abel summation compresses Q4 to a one-switch odd-prime observable

Claim ID: `L-93262`  
Status: **PROPOSED COMPLETE EXACT SCALE-COMPRESSION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-93261`; the classical unconditional prime number theorem for convergence  
Scope: exact scale telescoping and kernel geometry; no square-root estimate

## 1. Remove the explicit base-two block

Let `A_odd(N)` be the part of `A_circ(N)` owned by odd prime bases. Equivalently,

\[
\boxed{
\mathcal A_{\rm odd}(N)
=
\sum_{\substack{p\ {\mathrm{odd}}\\k\ge1}}
(\log p)W(p^k/N).
}
\tag{L-93262.1}
\]

The omitted base-two Q4 block has only `O(log N)` atoms with bounded
coefficients and bounded kernel, so

\[
\mathcal A_\circ(N)-\mathcal A_{\rm odd}(N)=O(\log N).
\tag{L-93262.2}
\]

## 2. Finite telescoping identity

For an arbitrary finite coefficient sequence `lambda(n)`, define

\[
H_\lambda(X)=\sum_n\lambda(n)K(n/X),
\qquad
A_\lambda(X)=\sum_n\lambda(n)W(n/X).
\]

Then for every integer `J>=0`, exactly

\[
\boxed{
\sum_{j=0}^{J}4^{-j}A_\lambda(4^jN)
=
4^{-J}H_\lambda(4^JN)
-4H_\lambda(N/4).
}
\tag{L-93262.3}
\]

This is literal telescoping after inserting `W(x)=K(x)-4K(4x)`.

For the odd-prime-power coefficient, the prime number theorem and `int K=0`
give

\[
H_{\rm odd}(X)=o(X)
\]

with the standard quantitative zero-free-region saving. Therefore the first
term on the right of (L-93262.3) tends to zero and the critical Abel sum
converges:

\[
\boxed{
\mathcal B_{\rm odd}(N)
:=\sum_{j\ge0}4^{-j}\mathcal A_{\rm odd}(4^jN)
=-4H_{\rm odd}(N/4).
}
\tag{L-93262.4}
\]

No RH estimate is used for this convergence.

## 3. One-switch compact kernel

Put

\[
J(x)=-4K(4x),
\]

again extending `K` by zero. Then

\[
J(x)=
\begin{cases}
{16\over3}x(1-4x)(1-8x),&0\le x\le1/4,\\
0,&x>1/4.
\end{cases}
\tag{L-93262.5}
\]

Consequently

\[
\boxed{
\mathcal B_{\rm odd}(N)
=
\sum_{\substack{p\ {\mathrm{odd}}\\k\ge1}}
(\log p)J(p^k/N).
}
\tag{L-93262.6}
\]

The kernel has exactly one sign change:

\[
J>0\text{ on }(0,1/8),
\qquad
J<0\text{ on }(1/8,1/4).
\tag{L-93262.7}
\]

Its cumulative is the positive square

\[
\boxed{
\int_0^xJ(u)du
={8\over3}x^2(1-4x)^2
\quad(0\le x\le1/4).
}
\tag{L-93262.8}
\]

The Mellin multiplier is

\[
\boxed{
\widehat J(s)=-4^{1-s}\widehat K(s).
}
\tag{L-93262.9}
\]

It has only a **simple** zero at `s=1`.

## 4. Prime-only version

Since `|J(x)|<=16x/3`, proper odd prime powers contribute

\[
O(\sqrt N\log^2(2N)).
\]

Thus `B_odd` differs at square-root scale from the one-switch ordinary-prime
sum

\[
\sum_{p\le N/4,\ p\ {\mathrm{odd}}}(\log p)J(p/N).
\tag{L-93262.10}
\]

## 5. What this achieves and what it spends

Critical Abel summation removes one complete Q4 scale difference and converts
the minimal two-switch kernel into one switch. It also spends one of the two
zeros at `s=1`. The resulting elementary Mobius forcing is macroscopic rather
than `O(1/Y)`; see `R-93264` and `L-93265`.

## 6. Boundary

```text
finite radix-four telescope      EXACT
critical Abel convergence        UNCONDITIONAL PNT
one-switch compact kernel        EXACT
positive cumulative square       EXACT
second Mellin zero               LOST
one-switch prime bound            OPEN / RH-BEARING
RH                               UNPROVED
```
