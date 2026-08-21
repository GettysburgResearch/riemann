# L-29006 — Positive prime endpoint-fiber binding

Claim ID: `L-29006`  
Title: The complete endpoint restriction of the dyadically filtered prime Jensen field is a nonnegative superposition of the compact endpoint fibers `W_m`, and their Selberg reserve controls the associated physical step-window norm on every annulus  
Status: **PROPOSED COMPLETE EXACT SOURCE-BINDING LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08  
Dependencies: `L-29003`, `L-29004`, `L-29005`; PR #301 `L-29805`  
Scope: closes the endpoint source-binding problem for the ordinary-prime Jensen field; it does not establish the coupled interior reflected matrix or RH

## 1. Step potential and endpoint chain

Put

\[
 L=\log2
\]

and retain the compact dyadic step

\[
 g_m(r)
 =\mathbf1_{m\le r<2m}
  -\frac12\mathbf1_{2m\le r<4m}
\tag{L-29006.1}
\]

for integer `r>=0`.

Let `(x_m)_(m>=2)` be any finitely supported nonnegative sequence and define

\[
 A_x(r)=\sum_{m\ge2}x_mg_m(r),
 \qquad A_x(0)=0.
\tag{L-29006.2}
\]

For the prime field of `L-29004`, the relevant specialization is

\[
 x_m=\Lambda(m),
 \qquad
 A_x(r)=\psi(r)-\frac32\psi(r/2)+\frac12\psi(r/4).
\tag{L-29006.3}
\]

The endpoint restriction of the additive split field is

\[
 A_x(r)-A_x(1)-A_x(r-1)=A_x(r)-A_x(r-1),
\tag{L-29006.4}
\]

because `x_1=0` and hence `A_x(1)=0`.

Using the balanced-tree endpoint commutator

\[
 D_r=T_r-T_{r-1}\equiv[r,1]\pmod{\ker\partial},
\]

define the complete endpoint chain

\[
\boxed{
 \mathcal E_x
 =\sum_{r\ge2}[A_x(r)-A_x(r-1)]D_r.
}
\tag{L-29006.5}

All sums are finite.

## 2. Exact positive fiber recombination

The step `g_m` has only three jumps:

\[
 g_m(r)-g_m(r-1)
 =\mathbf1_{r=m}
  -\frac32\mathbf1_{r=2m}
  +\frac12\mathbf1_{r=4m}.
\tag{L-29006.6}

Substituting (L-29006.2) into (L-29006.5), interchanging the finite sums, and
using `L-29005` gives

\[
\begin{aligned}
 \mathcal E_x
 &=\sum_mx_m
   \left(D_m-\frac32D_{2m}+\frac12D_{4m}\right)\\
 &=\boxed{\sum_mx_mW_m.}
\end{aligned}
\tag{L-29006.7}

Since `x_m>=0`, the entire endpoint packet is a nonnegative superposition of
complete filtered fibers.  No first-difference sign theorem is needed after the
source is grouped by its prime scale `m`.

For `x_m=Lambda(m)`, this answers the source-binding question left open in
`L-29005`: the endpoint restriction of the actual ordinary-prime Jensen field
has exactly the required nonnegative fiber coefficients.

## 3. Exact aggregate Kummer and Selberg coordinates

Let `F` be the ordinary logarithmic Kummer functional and `S` the complete
ordinary Selberg forcing functional on split chains.  `L-29005` gives

\[
 F(W_m)=-\frac12L,
\tag{L-29006.8}
\]

and

\[
 S(W_m)=-L\log m+\frac12L^2.
\tag{L-29006.9}

Put

\[
 X_0=\sum_mx_m,
 \qquad
 X_1=\sum_mx_m\log m.
\]

Then (L-29006.7)--(L-29006.9) give exactly

\[
\boxed{
 F(\mathcal E_x)=-\frac12LX_0,
}
\tag{L-29006.10}

\[
\boxed{
 S(\mathcal E_x)=-LX_1+\frac12L^2X_0.
}
\tag{L-29006.11}

Consequently the complete endpoint reserve is

\[
\boxed{
\begin{aligned}
 \mathcal Q_{\rm end}(x)
 &:=F(\mathcal E_x)^2-S(\mathcal E_x)\\
 &=\frac14L^2X_0^2+LX_1-\frac12L^2X_0.
\end{aligned}}
\tag{L-29006.12}

Since every active `m>=2`, one has `log m>=L`.  Hence

\[
\boxed{
 \mathcal Q_{\rm end}(x)
 \ge\frac14L^2X_0^2+\frac12L^2X_0
 \ge\frac14L^2X_0^2.
}
\tag{L-29006.13}

The endpoint reserve is therefore strictly positive for every nonzero
nonnegative source.

## 4. Annular physical-frame bound

Let

\[
 h(t)=\mathbf1_{[0,L)}(t)-\frac12\mathbf1_{[L,2L)}(t)
\]

and

\[
 f_x(t)=\sum_mx_mh(t-\log m).
\tag{L-29006.14}

Assume first that

\[
 M\le m<2M
\]

on the support of `x`.  Then `f_x` is supported in an interval of length at
most `3L`, and

\[
 |f_x(t)|\le X_0.
\]

Therefore

\[
 \|f_x\|_2^2\le3LX_0^2.
\]

Combining with (L-29006.13) gives the absolute endpoint-frame estimate

\[
\boxed{
 \|f_x\|_2^2
 \le\frac{12}{\log2}\,\mathcal Q_{\rm end}(x).
}
\tag{L-29006.15}

By PR #301 `L-29805`, the left side is also the exact weighted sample norm of
`A_x` and is equivalent, with absolute constants, to the corresponding
reflected carry-row Gram at parent `16M`.

Thus the prime endpoint packet is controlled in both its physical step-window
and carry coordinates by the same explicit Selberg reserve.

## 5. Global dyadic decomposition

Partition an arbitrary finite source into dyadic blocks

\[
 B_k=\{m:2^k\le m<2^{k+1}\}
\]

and write `f_x=sum_k f_k`.  The support of `f_k` lies in

\[
 [kL,(k+3)L).
\]

Blocks with the same residue class modulo three have disjoint supports up to
endpoints of measure zero.  Hence

\[
 \|f_x\|_2^2
 \le3\sum_k\|f_k\|_2^2.
\]

Applying (L-29006.15) blockwise yields

\[
\boxed{
 \|f_x\|_2^2
 \le\frac{36}{\log2}
   \sum_k\mathcal Q_{\rm end}(x|_{B_k}).
}
\tag{L-29006.16}

This is a source-complete global endpoint estimate.  It incurs no Möbius total
variation and no growing inverse condition number.

## 6. Consequence for PR #297

The endpoint alternative in the former version of `T-29001` is now resolved for
the ordinary-prime Jensen field:

```text
complete endpoint coefficients
 -> group by the positive prime scale Lambda(m)
 -> exact filtered fiber W_m
 -> strict aggregate endpoint reserve
 -> absolute physical/carry frame bound.
```

No endpoint-tree recurrence is needed for this positive source packet.

However, `R-29002` shows that the ordinary interior row reserve cannot be lifted
to the complete source merely by positive scalar weighting, and the natural
generalized-prime pointwise lift is false.  The remaining theorem is therefore
a **coupled interior source-matrix inequality**, not endpoint source binding.

## 7. Proof boundary

Closed exactly, subject to review:

- the endpoint restriction of the prime Jensen field;
- its exact nonnegative `W_m`-fiber decomposition;
- its aggregate Kummer/Selberg reserve;
- an absolute annular physical-frame estimate;
- a global three-color dyadic endpoint bound.

Open:

- the complete coupled interior source matrix;
- a reflected block recurrence using that matrix;
- the atomized energy bound;
- RH.
