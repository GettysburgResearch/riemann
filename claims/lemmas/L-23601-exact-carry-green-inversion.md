# L-23601 — Exact carry Green inversion

Claim ID: `L-23601`  
Title: The binomial-carry matrix has an affine Möbius contraction and a closed triangular inverse  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-q`  
Created: 2026-08-07  
Scope: finite algebra; no RH input

## 1. Carry matrix

For integers `2 <= q <= n`, write

\[
n=kq+r,\qquad 0\le r<q,
\]

and define

\[
\boxed{
\beta_{nq}=
\frac{k(q-1-r)}{n+1}.}
\tag{L-23601.1}
\]

If `J` is uniform on `{0,...,n}`, then

\[
\chi_{n,q}(J)
=\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac Jq\right\rfloor
-\left\lfloor\frac{n-J}{q}\right\rfloor
\in\{0,1\}
\]

is the carry at the `q`-place when adding `J` and `n-J`, and

\[
\boxed{
\beta_{nq}=\frac1{n+1}\sum_{J=0}^n\chi_{n,q}(J).}
\tag{L-23601.2}
\]

Indeed each of the `k` complete residue blocks contains exactly `q-1-r`
carry residues.

An equivalent floor identity is

\[
\boxed{
\beta_{nq}
=\left\lfloor\frac nq\right\rfloor
-\frac2{n+1}\sum_{j=0}^n
 \left\lfloor\frac jq\right\rfloor.}
\tag{L-23601.3}
\]

The matrix `Beta_X=(beta_(nq))_(2<=q<=n<=X)` is upper triangular in the
orientation `q` by `n`, with

\[
\beta_{nn}=\frac{n-1}{n+1}>0.
\tag{L-23601.4}
\]

## 2. Binomial entropy coordinate

Put

\[
G_n=\frac1{n+1}\sum_{j=0}^n\log {n\choose j}.
\tag{L-23601.5}
\]

Legendre's formula, summed over `j`, gives the exact finite identity

\[
\boxed{
G_n=\sum_{q=p^a\le n}\Lambda(q)\beta_{nq}.}
\tag{L-23601.6}
\]

No asymptotic prime theorem enters this formula.

## 3. Affine Möbius contraction

Let `mu` be the Möbius function. For every `2 <= m <= n`,

\[
\boxed{
\sum_{k\le n/m}\mu(k)\beta_{n,mk}
=\frac{2m-n-1}{n+1}.}
\tag{L-23601.7}
\]

### Proof

Insert (L-23601.3). Möbius inversion gives

\[
\sum_{k\le n/m}\mu(k)
\left\lfloor\frac{n}{mk}\right\rfloor=1.
\]

For the averaged floor term, interchange the finite sums and apply the same
identity at every `j`:

\[
\sum_{k\le n/m}\mu(k)
\sum_{j=0}^n\left\lfloor\frac{j}{mk}\right\rfloor
=\sum_{j=m}^n 1=n-m+1.
\]

Therefore

\[
1-\frac{2(n-m+1)}{n+1}
=\frac{2m-n-1}{n+1},
\]

which proves (L-23601.7).

This identity is the exact discrete Green reduction: the floor/carry row becomes
an affine function of `n` after one source-bound Möbius contraction.

## 4. Closed inverse

Fix `X` and any real data `w(q)`, `2<=q<=X`. There is a unique vector
`c_X(n)`, `2<=n<=X`, satisfying

\[
\boxed{
w(q)=\sum_{n=q}^X c_X(n)\beta_{nq}.}
\tag{L-23601.8}
\]

Define

\[
\boxed{
u_m=\sum_{k\le X/m}\mu(k)w(mk),}
\tag{L-23601.9}
\]

and put `U_j=sum_(m>=j)u_m`. Then

\[
\boxed{
 c_X(j)=
 \frac{
 (j+1)[j u_j-(j-2)u_{j+1}]+2U_{j+2}
 }{j(j-1)}.}
\tag{L-23601.10}
\]

### Proof

Apply (L-23601.7) to (L-23601.8):

\[
 u_m
 =\sum_{n=m}^X c_X(n)\frac{2m-n-1}{n+1}.
\tag{L-23601.11}
\]

Writing `d_n=c_X(n)/(n+1)` gives

\[
 u_m=\sum_{n=m}^X(2m-n-1)d_n.
\]

Two finite differences, followed by the identity
`sum_(n>=j+2)d_n`, give (L-23601.10). Conversely substitution reconstructs
(L-23601.11), and Möbius inversion reconstructs (L-23601.8).

## 5. Prime-ramp datum

For the proof-facing choice

\[
\boxed{
w_X(q)=q^{-1/2}\log(X/q),\qquad 2\le q\le X,}
\tag{L-23601.12}
\]

one has

\[
\boxed{
 u_m=m^{-1/2}
 \sum_{k\le X/m}\frac{\mu(k)}{\sqrt k}
 \log\frac{X/m}{k}.}
\tag{L-23601.13}
\]

Thus Carry Saturation,

\[
c_X(n)\ge0\quad(2\le n\le X),
\tag{L-23601.14}
\]

is a completely explicit finite Möbius–Riesz inequality. The formula also
shows why the first four quotient layers are elementary and why the first
negative Möbius layers cannot be treated term by term.

## 6. Positive-minorant formulation

Exact saturation is stronger than needed. It is enough to find numbers
`d_X(n)>=0` satisfying

\[
\boxed{
\sum_{n=q}^X d_X(n)\beta_{nq}\le w_X(q)
\qquad(2\le q\le X),}
\tag{L-23601.15}
\]

and

\[
\boxed{
\frac12\sum_{n=2}^X n d_X(n)
\ge4\sqrt X-o(\sqrt X),}
\tag{L-23601.16}
\]

with a logarithmic bound on the lower-order coefficient mass. Since
`Lambda(q)>=0`, (L-23601.6) then converts the minorant into a lower bound for
the complete prime-power ramp.

The continuation on this branch constructs `d_X` from the continuum Green
profile rather than assuming the stronger pointwise assertion (L-23601.14).

## 7. Proof boundary

Closed exactly:

- the carry interpretation;
- the binomial/prime-power factorization;
- the affine Möbius contraction;
- the complete triangular inverse;
- the positive-minorant interface.

Not proved here:

- positivity of the exact inverse;
- construction of a sharp nonnegative minorant;
- RH.
