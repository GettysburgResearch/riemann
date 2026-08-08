# L-23810 — Carry-flow divergence and exact Möbius inversion

Claim ID: `L-23810`  
Title: Atomized carry saturation is exactly a balanced fragmentation-flow problem with one uniquely determined Möbius divergence  
Status: **PROPOSED EXACT FINITE LEMMA — COMPLETE ALGEBRAIC PROOF**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23808`  
Scope: finite algebra; no positivity theorem

## 1. Split flow and divergence

Fix an integer endpoint `X>=2`.  For every split

\[
 n=j+(n-j),\qquad 2\le n\le X,\quad 1\le j<n,
\]

let `d_(n,j)` be a finitely supported real coefficient.  Its node divergence is

\[
\boxed{
 r_m=
 \sum_{j=1}^{m-1}d_{m,j}
 -\sum_{n>m}\bigl(d_{n,m}+d_{n,n-m}\bigr),
 \qquad 1\le m\le X,
}
\tag{L-23810.1}
\]

where a central child is counted twice.  This convention makes the parent
coefficient positive and each child coefficient negative.

For every integer base `q>=2`, define the carry load

\[
 L_q(d)=\sum_{n,j}d_{n,j}\chi_{n,j}(q).
\tag{L-23810.2}
\]

The floor-defect identity of `L-23808` gives exactly

\[
\boxed{
 L_q(d)=\sum_{m=1}^{X}r_m\left\lfloor{m\over q}\right\rfloor.
}
\tag{L-23810.3}
\]

Also

\[
\boxed{
 \sum_{m=1}^{X}m r_m=0,
}
\tag{L-23810.4}
\]

because every split conserves its parent size.

Thus all Pascal four-cycle changes of the internal fragmentation tree leave
both the complete carry vector and the binomial objective unchanged: they leave
`r` unchanged.

## 2. The unique divergence attached to a target carry vector

Let a target vector `w(q)` be prescribed for `2<=q<=X`, and put

\[
 w(1)=0,
 \qquad w(q)=0\quad(q>X).
\tag{L-23810.5}
\]

Define its Möbius tail transform

\[
\boxed{
 u_m=\sum_{k\le X/m}\mu(k)w(mk),
 \qquad 1\le m\le X,
 \qquad u_{X+1}=0,
}
\tag{L-23810.6}
\]

and the discrete divergence

\[
\boxed{
 r_m=u_m-u_{m+1}.
}
\tag{L-23810.7}
\]

Then

\[
\boxed{
 w(q)=\sum_{m=1}^{X}r_m\left\lfloor{m\over q}\right\rfloor
 \qquad(1\le q\le X).
}
\tag{L-23810.8}
\]

### Proof

Starting from any vector `r`, put

\[
 W(q)=\sum_mr_m\lfloor m/q\rfloor.
\]

Möbius inversion over multiples gives

\[
\begin{aligned}
 \sum_{k\le X/m}\mu(k)W(mk)
 &=\sum_n r_n
   \sum_{k\le n/m}\mu(k)
       \left\lfloor{n/m\over k}\right\rfloor\\
 &=\sum_{n\ge m}r_n,
\end{aligned}
\]

using the elementary identity

\[
 \sum_{k\le N}\mu(k)\lfloor N/k\rfloor=1.
\]

Thus the Möbius transform of `W` is the tail sum of `r`.  Equations
(L-23810.6)--(L-23810.7) invert this relation and prove (L-23810.8).
Uniqueness follows from the same calculation.  The row `q=1` gives
(L-23810.4).

## 3. Exact reformulation of BCT

For the prime-ramp target

\[
 w_X(q)=q^{-1/2}\log(X/q),\qquad 2\le q\le X,
\tag{L-23810.9}
\]

let `r_X` be (L-23810.6)--(L-23810.7).

Fix `0<eta<1/2`.  The following are equivalent.

1. There is a nonnegative atomized carry flow supported on
   \[
   \eta n\le j\le(1-\eta)n
   \]
   whose column loads equal `w_X`.
2. The vector `r_X` is the divergence of a nonnegative `eta`-balanced binary
   fragmentation flow.

Hence exact zero-slack BCT is not a mysterious matrix event: it is the concrete
finite question whether the explicitly known signed node measure `r_X` can be
realized by balanced downward fragmentation.

For a packing with slack `s_q>=0`, replace `w_X` by `w_X-s`; the same theorem
applies to its Möbius divergence.  In particular, a subpolynomial total slack is
exactly a subpolynomial perturbation of the floor-transform data, not an omitted
prime or an analytic tail.

## 4. Farkas dual in node-potential coordinates

Let `h_q=1-y_q`, where `y_q>=0` is a dual carry weight, and define

\[
 H(m)=\sum_{q=2}^{X}h_q\lfloor m/q\rfloor.
\tag{L-23810.10}
\]

The balanced split constraints are exactly

\[
\boxed{
 H(n)\le H(j)+H(n-j)
 \quad\text{for every retained balanced split.}
}
\tag{L-23810.11}
\]

Moreover

\[
\boxed{
 \sum_{q=2}^{X}w_X(q)h_q
 =\sum_{m=1}^{X}r_X(m)H(m).
}
\tag{L-23810.12}
\]

Thus BCT is equivalently the assertion that every divisor-floor potential which
is balanced-subadditive has nonpositive pairing with `r_X`, up to the permitted
subpolynomial slack.

This is the exact bridge to:

- Pascal-cycle transport on the primal side;
- signed common-cell/BTP estimates on the dual side;
- the first-cell Mertens mutation, which tests the Möbius tail transform in
  (L-23810.6).

## 5. Proof boundary

Closed exactly:

- carry load equals the floor transform of divergence;
- the target divergence is uniquely recovered by Möbius inversion;
- BCT is equivalent to nonnegative balanced fragmentation of `r_X`;
- the Farkas dual is balanced subadditivity of one divisor-floor potential.

Open:

- positivity/existence of the balanced fragmentation flow for the prime-ramp
  divergence;
- a subpolynomial-slack construction;
- RH.
