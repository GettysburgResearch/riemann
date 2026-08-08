# L-26201 — Möbius–Poisson factorization of carry corrections

Claim ID: `L-26201`  
Title: Every carry correction is the Poisson tail of one cellwise Möbius charge, and the canonical Green correction supplies a source-bound all-integer extension  
Status: **PROPOSED — COMPLETE EXACT FINITE ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #260  
Dependencies: `L-23701`, `L-23803`, `L-24501`, `L-24509`  
Scope: finite algebra; no asymptotic estimate

## 1. Divisor-gradient coordinates

Fix an integer `X>=2`. For a vector

\[
b=(b_2,\ldots,b_X),\qquad b_{X+1}=0,
\]

put

\[
\boxed{
v_q(b)=\sum_{kq\le X}(b_{kq}-b_{kq+1})
\qquad(2\le q\le X).
}
\tag{L-26201.1}
\]

Let `b^(0)` be any reference vector and write

\[
s_m=b_m-b_m^{(0)},\qquad s_{X+1}=0.
\tag{L-26201.2}
\]

Define the discrete charge

\[
\boxed{
\gamma_m=s_m-s_{m+1}
\qquad(2\le m\le X).
}
\tag{L-26201.3}
\]

The induced change in every divisor coordinate is then

\[
\boxed{
h(q):=v_q(b)-v_q(b^{(0)})
=\sum_{kq\le X}\gamma_{kq}.
}
\tag{L-26201.4}
\]

This identity is merely a regrouping of the finite sum; it uses no sign
assumption and no prime restriction.

## 2. Exact Möbius inversion over multiples

Let `mu` denote the Möbius function. The ordinary inversion identity on the
poset of multiples gives

\[
\boxed{
\gamma_m
=\sum_{k\le X/m}\mu(k)h(mk).
}
\tag{L-26201.5}
\]

Indeed,

\[
\begin{aligned}
\sum_{k\le X/m}\mu(k)h(mk)
&=\sum_{k\le X/m}\mu(k)
  \sum_{\ell mk\le X}\gamma_{\ell mk}\\
&=\sum_{r\le X/m}\gamma_{rm}\sum_{k\mid r}\mu(k)
=\gamma_m.
\end{aligned}
\]

Conversely,

\[
\boxed{
s_m=\sum_{n=m}^{X}\gamma_n.
}
\tag{L-26201.6}
\]

Thus the complete carry correction factors as

```text
constraint change h
    -> Möbius charge gamma
    -> one-dimensional Poisson tail s
    -> corrected b.
```

The reciprocal-zeta channel is present explicitly in the first arrow; it is not
hidden in a matrix inverse.

## 3. Prime-power constraints and the Green extension

Let

\[
\mathcal Q_X=\{p^a:p^a\le X\}.
\]

The carry LP prescribes only the coordinates `h(q)` for
`q in Q_X`. A correction nevertheless induces values (L-26201.4) at every
integer `2<=q<=X`.

For the canonical endpoint-projected Green correction of `L-24509`, let

\[
r_q=v_q(b^{(0)})-w_X(q),
\qquad q\in\mathcal Q_X,
\]

solve

\[
G_XT=r,
\tag{L-26201.7}
\]

put

\[
F_T(j)=\sum_{q\in\mathcal Q_X}T_qf_q(j),
\]

and define

\[
b^\star_m=b_m^{(0)}+F_T(m-1)-F_T(m).
\tag{L-26201.8}
\]

Then

\[
v_q(b^\star)=w_X(q)
\qquad(q\in\mathcal Q_X).
\tag{L-26201.9}
\]

Equations (L-26201.4)--(L-26201.6), applied to `b=b^star`, define an exact
all-integer extension

\[
h^\star(q)=v_q(b^\star)-v_q(b^{(0)})
\qquad(2\le q\le X)
\tag{L-26201.10}
\]

and its source-bound charge

\[
\boxed{
\gamma^\star_m
=\sum_{k\le X/m}\mu(k)h^\star(mk).
}
\tag{L-26201.11}
\]

At prime powers `h^star(q)=-r_q`; at composite non-prime-powers its value is
not guessed or set to zero. It is determined by the same finite Green
potential.

This resolves an ambiguity in earlier carry discussions: a prime-power
correction may be analyzed cellwise by Möbius inversion only after its complete
all-integer extension has been declared.

## 4. Quotient cells

On the cell

\[
\frac{X}{R+1}<m\le\frac XR,
\tag{L-26201.12}
\]

formula (L-26201.11) contains only

\[
\mu(1),\ldots,\mu(R).
\]

Hence every fixed quotient cell is an exact finite signed affine problem. The
boundary values shared by neighboring cells are part of the same charge
sequence `gamma^star`; they may not be widened independently.

This is the precise algebraic interface needed to combine the carry
quotient-layer decoder with signed Green or dipole transport.

## 5. Relation to the adjacent-flow map

If a potential `F` is used as in `L-25301`,

\[
s_m=F_{m-1}-F_m,
\]

then

\[
\gamma_m=F_{m-1}-2F_m+F_{m+1}.
\tag{L-26201.13}
\]

Thus the adjacent-flow constraint matrix is the composition

\[
\boxed{
F
\ \xrightarrow{\ \Delta^2\ }\ 
\gamma
\ \xrightarrow{\ \text{sum over multiples}\ }\ 
h.
}
\tag{L-26201.14}
\]

Its inverse is correspondingly

\[
h
\ \xrightarrow{\ \mu\text{-inversion}\ }\ 
\gamma
\ \xrightarrow{\ \text{Poisson summation}\ }\ 
s,
\]

followed by one boundary normalization for `F`.

The canonical Green solve and the cellwise Möbius decoder are therefore two
coordinate descriptions of the same finite correction.

## 6. Proof boundary

Closed exactly:

- divisor-gradient factorization;
- Möbius inversion over multiples;
- Poisson recovery;
- the source-bound all-integer extension of the Green correction;
- quotient-cell finiteness.

Not closed:

- positivity of the corrected vector;
- subpower contact debt;
- the sharp prime-ramp estimate;
- RH.
