# L-26209 — Shell, Riesz, collar, and bottom charge are one source

Claim ID: `L-26209`  
Status: `PROPOSED COMPLETE — exact Abel, filter, and finite carry algebra pending independent review`  
Scope: consolidation of the dyadic fixed-ratio shell, the boundary collar of PR #272, and the bottom-charge consumer of PR #268  
Date: 2026-08-08  
Depends on: PR #268 `L-26204`; PR #269 `L-26202`; PR #272 `L-26203`; elementary partial summation

## 1. Dyadic shell and its normalized primitive

Put

\[
b_2(n)=\mu(n)-\mathbf 1_{2\mid n}\mu(n/2)
\]

and

\[
S_2(x)=\sum_{n\le x}b_2(n)=M(x)-M(x/2).
\tag{L-26209.1}
\]

Define the complete logarithmic Riesz coordinate

\[
\boxed{
\widetilde{\mathcal R}_2(X)
=\sum_{n\le X}\frac{b_2(n)}{\sqrt n}\log\frac Xn.
}
\tag{L-26209.2}
\]

For

\[
f_X(u)=u^{-1/2}\log(X/u)
\]

one has `f_X(X)=0` and

\[
f_X'(u)=-u^{-3/2}\left(1+\frac12\log\frac Xu\right).
\]

Finite Abel summation therefore gives the exact positive-kernel identity

\[
\boxed{
\widetilde{\mathcal R}_2(X)
=\int_1^X
S_2(u)u^{-3/2}
\left(1+\frac12\log\frac Xu\right)du.
}
\tag{L-26209.3}
\]

In logarithmic coordinates, with

\[
Q_2(t)=e^{-t/2}S_2(e^t),
\qquad T=\log X,
\]

this is

\[
\boxed{
\widetilde{\mathcal R}_2(e^T)
=\int_0^T Q_2(t)
\left(1+\frac{T-t}{2}\right)dt.
}
\tag{L-26209.4}
\]

Thus the dyadic Riesz coordinate is the first polynomial Abel primitive of the normalized fixed-ratio Mertens shell.

## 2. The opposite-parity source is one finite dyadic difference

Retain

\[
\omega_2=b_2-\frac12\delta_2*b_2
\]

and define

\[
\widetilde{\mathcal R}_\omega(X)
=\sum_{n\le X}\frac{\omega_2(n)}{\sqrt n}\log\frac Xn.
\tag{L-26209.5}
\]

A finite reindexing gives

\[
\boxed{
\widetilde{\mathcal R}_\omega(X)
=\widetilde{\mathcal R}_2(X)
-2^{-3/2}\widetilde{\mathcal R}_2(X/2).
}
\tag{L-26209.6}
\]

No inverse filter or asymptotic estimate is used.

## 3. Exact bottom-charge identity

Let `c_X(2),...,c_X(X)` be the unique triangular carry inverse

\[
q^{-1/2}\log(X/q)
=\sum_{n=q}^Xc_X(n)\beta_{nq}.
\tag{L-26209.7}
\]

PR #268 proves, with its convention omitting the `q=1` term,

\[
5c_X(2)+3c_X(3)
=-6\sum_{q=2}^X\frac{\omega_2(q)}{\sqrt q}\log\frac Xq.
\]

Since `omega_2(1)=1`, equations (L-26209.5)--(L-26209.7) give

\[
\boxed{
5c_X(2)+3c_X(3)
=6\left[\log X-\widetilde{\mathcal R}_\omega(X)\right].
}
\tag{L-26209.8}
\]

Thus the proposed bottom-charge sign is not a separate arithmetic source. It is a one-sided formulation of the same dyadic-shell Riesz coordinate.

## 4. Boundary-collar identification

PR #272 completes a truncated Möbius source by one weighted dyadic pair. Its oversupport collar has half-pole jet

\[
\boxed{
A_Y^{\rm bd}
=-S_2(Y)
=-\bigl[M(Y)-M(Y/2)\bigr].
}
\tag{L-26209.9}
\]

Combining (L-26209.3) and (L-26209.9), the bottom Riesz charge is an explicit positive-kernel Abel integral of the same scalar exported by the boundary-jet programme.

Consequently the following are three exact interfaces to one source:

```text
physical shell:       Q_2(t)=e^(-t/2)[M(e^t)-M(e^t/2)];
endpoint collar jet:  -[M(Y)-M(Y/2)];
finite carry charge:  5 c_X(2)+3 c_X(3).
```

They must not be counted as independent closing theorems.

## 5. Energy-to-Riesz transfer

Fix a block length `B>0` and suppose

\[
E_j=\int_{jB}^{(j+1)B}|Q_2(t)|^2dt=e^{o(j)}.
\tag{L-26209.10}
\]

Split (L-26209.4) into blocks and apply Cauchy--Schwarz on each block. The polynomial weight is at most `1+T/2`, and there are `O(T)` blocks. Hence

\[
\boxed{
\widetilde{\mathcal R}_2(e^T)=e^{o(T)}.
}
\tag{L-26209.11}
\]

The finite difference (L-26209.6) gives the same statement for `widetilde R_omega`. Its Mellin transform contains the uncancelled factor `1/zeta(s)`, so the standard Landau/pole consumer excludes every zero with real part greater than `1/2`.

This implication is one-way at the stated scope: a scalar Riesz estimate does not automatically give the full block-energy theorem.

## 6. Consolidation rule

A proposed completion may work in any one of the following coordinates:

1. a physical shell-energy contraction;
2. a source-image domination of the boundary collar;
3. a bottom-charge/Riesz estimate.

But the proof must contain an explicit map to one of the other two and must preserve the dyadic and `2/3` Mertens mutations. A result that loses `S_2` has lost the RH-bearing source.

## 7. Proof boundary

Closed exactly:

- the Abel shell-to-Riesz identity;
- the finite dyadic source difference;
- the bottom-charge formula;
- the collar-shell identification;
- the block-energy-to-Riesz implication.

Open:

- a subexponential shell-energy estimate;
- a source-image transition domination theorem;
- an independent proof of the bottom-charge bound;
- RH.
