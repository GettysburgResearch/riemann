# L-99714 — A blockwise growing safe moment tower has subpower inverse cost

Claim ID: `L-99714`  
Status: **PROVED EXACT OPERATOR / COMBINATORIAL THEOREM**  
Created: 2026-08-20  
Depends on: `L-99713`; the fixed-order identity of PR #600  
RH status: **not assumed**

Let

\[
(SF)(x)=F(x/2)
\]

and let `W` be the compact packet of `L-99713`.  For an integer `M>=1`, put

\[
W^{[M]}=(I-S)^M W.
\tag{L-99714.1}
\]

The Mellin multiplier is `(1-2^-s)^M`, whose zeros lie only on `Re s=0`.
It cannot cancel a reciprocal-zeta pole in `Re s>0`.

## 1. Positive finite inverse

On endpoint functions extended by zero below one,

\[
\boxed{
(I-S)^{-M}
=
\sum_{j\ge0}{M+j-1\choose M-1}S^j.
}
\tag{L-99714.2}
\]

At `x<2^(L+1)`, the sum terminates at `j<=L`, and its total coefficient mass
is exactly

\[
\boxed{
\sum_{j=0}^{L}{M+j-1\choose M-1}
={M+L\choose M}.
}
\tag{L-99714.3}
\]

Because every inverse coefficient is nonnegative,

\[
W_-(x)
\le
\sum_{j=0}^{L}{M+j-1\choose M-1}
 (W^{[M]})_-(x/2^j).
\tag{L-99714.4}
\]

The same inequality holds after logarithmic integration.

## 2. Growing order on dyadic blocks

For `L>=3`, choose

\[
\boxed{
M_L=
\left\lfloor{L\over(\log(L+e))^3}\right\rfloor\vee1.
}
\tag{L-99714.5}
\]

The elementary binomial estimate gives

\[
\log{L+M_L\choose M_L}
\le
M_L\log\!\left({e(L+M_L)\over M_L}\right)
=o(L).
\tag{L-99714.6}
\]

Hence

\[
\boxed{
{L+M_L\choose M_L}=2^{o(L)}=x^{o(1)}
\qquad(2^L\le x<2^{L+1}).
}
\tag{L-99714.7}
\]

Therefore a subpower logarithmic negative-mass estimate for the blockwise
filtered packets `W^[M_L]` implies the same estimate for `W`, and hence RH by
`L-99713`.

## 3. Geometry of the filtered kernel

If `Phi` is the compact ratio-eight kernel of `L-99713`, then

\[
\Phi_M(y)=\sum_{j=0}^M(-1)^j{M\choose j}\Phi(y/2^j).
\tag{L-99714.8}
\]

It is supported in

\[
1\le y\le 2^{M+3},
\tag{L-99714.9}
\]

and its Mellin transform has a zero of order `M` at `s=0`.  Thus, on the block
`2^L<=x<2^(L+1)`, the active multiplicative width is

\[
2^{M_L+3}=x^{o(1)},
\tag{L-99714.10}
\]

while the packet has `M_L` exact logarithmic moments removed.

The direct coefficient mass of the forward filter is at most `2^M`, also
`x^(o(1))` for (L-99714.5).

## 4. Conclusion-facing reduction

Define the blockwise phase packet

\[
\mathscr W_{x,L}(w)
=
\sum_n{\beta(n)\over\sqrt n}
 \Phi_{M_L}(x/n)n^{-w}.
\tag{L-99714.11}
\]

A proof may therefore combine, at only subpower total cost:

```text
M_L growing exact zero moments;
subpower multiplicative support width;
adaptive strip tau_x=1/loglog x;
Cauchy-Poisson owner gap >=1/loglog x;
positive inverse back to the compact conclusion packet W.
```

This removes all low-frequency kernel modes before the source-owner Carleson
packing is attempted.  It does not itself estimate the remaining balanced
phase-sensitive cross terms.