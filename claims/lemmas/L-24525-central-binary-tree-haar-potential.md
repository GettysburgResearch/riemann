# L-24525 — Central binary-tree Green kernel and Haar potential

Claim ID: `L-24525`  
Status: **PROPOSED COMPLETE — exact finite algebra**  
Scope: global potential form of the central-Neumann cascade  
Issue: #245  
Date: 2026-08-08

This lemma rewrites the central-Neumann coefficients of `L-24523` as one
binary-tree Green transform and then as adjacent dyadic block differences of the
exact Möbius divergence potential. It is the global-potential form requested by
the signed constraint-dipole programme.

## 1. Exact Möbius floor potential

Let

\[
w_X(q)=q^{-1/2}\log(X/q),\qquad 2\le q\le X,
\]

with zero padding outside the active range. Put

\[
U_X(m)=\sum_{k\le X/m}\mu(k)w_X(mk)
\tag{L-24525.1}
\]

and

\[
R_X(m)=U_X(m)-U_X(m+1).
\tag{L-24525.2}
\]

The standard floor-Möbius inversion gives

\[
w_X(q)=\sum_{m=1}^{X}R_X(m)\left\lfloor{m\over q}\right\rfloor.
\tag{L-24525.3}
\]

Equivalently,

\[
U_X(m)=m^{-1/2}
\sum_{k\le X/m}{\mu(k)\over\sqrt k}
\log{X/m\over k}.
\tag{L-24525.4}
\]

Thus `U_X` is one normalized logarithmic Möbius-Riesz state.

## 2. Central fragmentation recurrence

Let `A_X(n)` be the central-Neumann coefficients of `L-24523`. A central split
of a parent `m` has children

\[
\lfloor m/2\rfloor,\qquad\lceil m/2\rceil.
\]

The parents contributing to node `n` are exactly

\[
2n-1,\qquad 2n\text{ with multiplicity two},\qquad 2n+1.
\]

Therefore the exact divergence equation is

\[
\boxed{
A_X(n)=R_X(n)+A_X(2n-1)+2A_X(2n)+A_X(2n+1),
}
\tag{L-24525.5}
\]

with every coefficient above `X` interpreted as zero. This is the same unique
triangular solution as the terminating Neumann construction of `L-24523`.

## 3. Binary-tree tent kernel

After `r` repeated central fragmentations, the multiplicity of a leaf of size
`n` descended from a parent of size `m` is

\[
\boxed{
K_r(m,n)=\bigl(2^r-|m-2^rn|\bigr)_+.
}
\tag{L-24525.6}
\]

Indeed the `2^r` leaves are the two adjacent integers

\[
\left\lfloor{m\over2^r}\right\rfloor,
\qquad
\left\lceil{m\over2^r}\right\rceil,
\]

with multiplicities determined by the remainder of `m` modulo `2^r`.
Consequently

\[
\boxed{
A_X(n)=\sum_{r\ge0}\sum_{m=1}^{X}K_r(m,n)R_X(m).
}
\tag{L-24525.7}
\]

The sum is finite because the tent is empty once `2^r(n-1)>X`.

## 4. Exact Haar-block formula

Apply discrete summation by parts to (L-24525.7), using
`R_X(m)=U_X(m)-U_X(m+1)`. The discrete derivative of the tent is `+1` on its
left half and `-1` on its right half. Hence

\[
\boxed{
\begin{aligned}
A_X(n)=\sum_{r\ge0}\Bigg[&
\sum_{m=2^r(n-1)+1}^{2^rn}U_X(m)\\
&-\sum_{m=2^rn+1}^{2^r(n+1)}U_X(m)
\Bigg],
\end{aligned}}
\tag{L-24525.8}
\]

where every interval is truncated at `X` and empty intervals contribute zero.

Define the binary-tree potential

\[
\boxed{
G_X(n)=\sum_{r\ge0}
\sum_{m=2^r(n-1)+1}^{2^rn}U_X(m).
}
\tag{L-24525.9}
\]

Then

\[
\boxed{A_X(n)=G_X(n)-G_X(n+1).}
\tag{L-24525.10}
\]

Thus the central coefficient vector is the discrete derivative of one explicit
global potential. Its negative coefficients are exactly the upward jumps of
`G_X`.

## 5. Exact factor-two potential recursion

The dyadic blocks contributing to `G_X(n)` split into the two descendant block
families of `2n-1` and `2n`. Therefore

\[
\boxed{
G_X(n)=U_X(n)+G_X(2n-1)+G_X(2n),
}
\tag{L-24525.11}
\]

again with zero padding above `X`. This is an exact factor-two recursion, not an
asymptotic or an operator-norm estimate.

The central negative variation of `L-24524` is now

\[
\boxed{
\mathcal V_X^-
=\sum_{n=2}^{X}\sqrt n\,[G_X(n+1)-G_X(n)]_+.
}
\tag{L-24525.12}
\]

Hence CNVD is a weighted one-sided variation theorem for one completely
specified dyadic potential.

## 6. Exact dyadic-shell decomposition

Let

\[
Y=\lfloor X/2\rfloor
\]

and extend every level-`Y` object by zero above `Y`. Define the target shell

\[
s_{X,Y}(q)=w_X(q)-\mathbf1_{q\le Y}w_Y(q).
\tag{L-24525.13}
\]

Let `B_{X,Y}` be its central-Neumann coefficient vector. Linearity and the fact
that the central matrix restricted to rows and columns at most `Y` is
independent of the ambient endpoint give

\[
\boxed{A_X(n)=A_Y(n)+B_{X,Y}(n).}
\tag{L-24525.14}
\]

The same decomposition holds for `U`, `R`, and `G`:

\[
G_X=G_Y+G_{X,Y}^{\rm shell}.
\tag{L-24525.15}
\]

Therefore

\[
\boxed{
\mathcal V_X^-
\le
\mathcal V_Y^-
+
\mathcal S_X,
}
\tag{L-24525.16}
\]

where

\[
\boxed{
\mathcal S_X
=
\sum_{n=2}^{X}\sqrt n\,[-B_{X,Y}(n)]_+.
}
\tag{L-24525.17}
\]

This is the exact central-Haar shell charge. Iterating (L-24525.16) reduces the
global CNVD theorem to the same logarithmically weighted dyadic-shell geometry
that survives in the repository's canonical WSTS packet.

## 7. Shell objective ledger

Let

\[
\ell_n=\log\binom n{\lfloor n/2\rfloor},
\qquad
c_n=\sum_{q=2}^{n}\chi_n^{\rm c}(q).
\]

The shell coefficients satisfy exactly

\[
\sum_n B_{X,Y}(n)\ell_n
=
\mathcal P(X)-\mathcal P(Y)
\tag{L-24525.18}
\]

and

\[
\sum_n B_{X,Y}(n)c_n
=
\mathcal C(X)-\mathcal C(Y).
\tag{L-24525.19}
\]

Thus

\[
\boxed{
[\mathcal P(X)-\mathcal P(Y)]
-[\mathcal C(X)-\mathcal C(Y)]
=
\sum_n B_{X,Y}(n)(\ell_n-c_n).
}
\tag{L-24525.20}
\]

The shell negative variation controls the complete shell discrepancy through
`|ell_n-c_n|<<sqrt(n)` and the signed weighted-load adapter of `L-24524`.

## 8. Interpretation and firewall

The formulas above prove that the factor-two descent is already exact at the
level of source, Green kernel, and global potential. What remains is not an
unknown finite transport map. It is the one-sided variation of the completed
shell potential after upper and lower scales have recombined.

A proof may not estimate the two halves of (L-24525.15) separately by absolute
value. The continuum multiplier of `L-24523` retains the reciprocal-zeta mode,
and the newest WSTS consolidation shows that the shell subtraction must occur
before the positive part is taken.

## Proof boundary

Proved exactly:

- the central fragmentation recurrence;
- the binary tent Green kernel;
- the dyadic Haar-block formula;
- the global-potential derivative identity;
- the exact factor-two potential recursion;
- the dyadic-shell coefficient and objective decompositions.

Open:

- a subpower bound for `mathcal S_X` or `mathcal V_X^-`;
- a nonnegative sharp central/Pascal certificate;
- RH.
