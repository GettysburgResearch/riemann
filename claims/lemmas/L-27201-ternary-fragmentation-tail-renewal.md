# L-27201 — Deterministic ternary fragmentation and its exact tail renewal

Claim ID: `L-27201`  
Title: One fixed `1/3–2/3` split converts the Möbius divergence into an exact zero-slack carry representation, and coefficient positivity is equivalent to monotonicity of one scalar tail renewal  
Status: **PROPOSED EXACT ALGEBRA / POSITIVITY OPEN**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-26205`; exact carry/Möbius inversion from PR #272; outer `5n>X` sign theorem from PR #208  
Scope: every finite target; no RH conclusion without the positivity clause

## 1. Fixed ternary split

For every integer `n>=2`, put

\[
a(n)=\left\lceil\frac n3\right\rceil,
\qquad
b(n)=\left\lfloor\frac{2n}3\right\rfloor=n-a(n).
\tag{L-27201.1}
\]

Both children are balanced:

\[
\frac n4\le a(n)\le b(n)\le\frac{3n}4
\]

(with the finitely many smallest `n` checked directly).

Let `w(2),...,w(X)` be any finite target. Define its multiples-Möbius transform

\[
u_m=\sum_{k\le X/m}\mu(k)w(mk),
\qquad u_{X+1}=0,
\tag{L-27201.2}
\]

and the node divergence

\[
r_m=u_m-u_{m+1}\quad(2\le m\le X),
\qquad
r_1=-\sum_{m=2}^Xmr_m.
\tag{L-27201.3}
\]

## 2. Deterministic descending producer

Process `n=X,X-1,...,2`. Let `I_n` be the incoming mass already sent to `n`
by larger parents, and define

\[
\boxed{A_X(n)=r_n+I_n.}
\tag{L-27201.4}
\]

Send the complete amount `A_X(n)` through the single split

\[
n\longrightarrow a(n)+b(n).
\tag{L-27201.5}
\]

Equivalently,

\[
A_X(n)
=r_n+
\sum_{m>n:\,a(m)=n}A_X(m)
+
\sum_{m>n:\,b(m)=n}A_X(m).
\tag{L-27201.6}
\]

This recurrence is triangular and therefore defines one unique real coefficient
vector for every target.

## 3. Exact divergence and carry saturation

Let

\[
d_{n,j}=A_X(n)\mathbf 1_{j=a(n)}.
\]

Then the divergence of `d` is exactly `r` at every node. Consequently the
atomized carry identity of `L-26205` gives

\[
\boxed{
\sum_{n=q}^{X}A_X(n)
\left[
\left\lfloor\frac nq\right\rfloor
-
\left\lfloor\frac{a(n)}q\right\rfloor
-
\left\lfloor\frac{b(n)}q\right\rfloor
\right]
=w(q)
}
\tag{L-27201.7}
\]

for every integer `2<=q<=X`, with no remainder.

Thus

\[
\boxed{A_X(n)\ge0\text{ for all }n}
\tag{L-27201.8}
\]

is a deterministic sufficient certificate for `MFT_{1/4}`. It replaces the
quadratic split LP by one descending recurrence.

## 4. Exact tail renewal

Define

\[
S_X(n)=\sum_{m=n}^{X}A_X(m),
\qquad S_X(n)=0\quad(n>X).
\tag{L-27201.9}
\]

The target divergence has tail

\[
\sum_{m=n}^{X}r_m=u_n.
\tag{L-27201.10}
\]

For the ternary split, a parent `m>=n` contributes to this tail as follows:

- `+1` if both children are below `n`, equivalently
  `n<=m<ceil(3n/2)`;
- `0` if exactly one child is at least `n`;
- `-1` if both children are at least `n`, equivalently `m>=3n-2`.

Therefore

\[
\boxed{
u_n
=S_X(n)-S_X\!\left(\left\lceil\frac{3n}{2}\right\rceil\right)
-S_X(3n-2),
}
\tag{L-27201.11}
\]

or, equivalently,

\[
\boxed{
S_X(n)
=u_n
+S_X\!\left(\left\lceil\frac{3n}{2}\right\rceil\right)
+S_X(3n-2).
}
\tag{L-27201.12}
\]

Finally,

\[
\boxed{A_X(n)=S_X(n)-S_X(n+1).}
\tag{L-27201.13}
\]

Hence ternary fragmentation positivity is exactly the one-dimensional statement
that the explicitly defined renewal tail `S_X` is nonincreasing.

## 5. Explicit parent recurrences

For `n=2k`,

\[
\boxed{
A_X(2k)
=r_{2k}
+A_X(3k)+A_X(3k+1)
+A_X(6k-2)+A_X(6k-1)+A_X(6k).
}
\tag{L-27201.14}
\]

For `n=2k+1`,

\[
\boxed{
A_X(2k+1)
=r_{2k+1}
+A_X(3k+2)
+A_X(6k+1)+A_X(6k+2)+A_X(6k+3).
}
\tag{L-27201.15}
\]

Terms with index greater than `X` are zero.

## 6. Unconditional outer sector

The reviewed outer carry theorem proves

\[
r_n\ge0\qquad(5n\ge X)
\tag{L-27201.16}
\]

with endpoint conventions handled separately. Descending induction in
(L-27201.6) then gives

\[
\boxed{A_X(n)\ge0\qquad(5n\ge X).}
\tag{L-27201.17}
\]

Thus the deterministic producer closes the same outer four-fifths
unconditionally. The exact remaining range is `n<X/5`.

## 7. Proof boundary

Closed exactly:

- deterministic ternary source grammar;
- exact divergence;
- exact saturation of every carry column;
- scalar tail-renewal formula;
- equivalence between flow positivity and tail monotonicity;
- unconditional outer sector.

Open:

- `A_X(n)>=0` in the inner range `n<X/5` for the logarithmic target;
- a polylogarithmic negative-part substitute;
- RH.
