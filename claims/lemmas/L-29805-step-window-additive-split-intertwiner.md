# L-29805 — Step-window/additive-split intertwiner

Claim ID: `L-29805`  
Title: The opposite-parity multiplicative step window is exactly intertwined with the atomized carry split operator, with an annular physical/carry frame inequality  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Dependencies: PR #269 `L-26901`; elementary interval arithmetic  
Scope: explicit source-specific physical/carry adapter; not the full PR #241 prime normal block

## 1. The compact step window

Let

\[
 L=\log2
\]

and define

\[
 h(t)=\mathbf1_{[0,L)}(t)
      -{1\over2}\mathbf1_{[L,2L)}(t).
\tag{L-29805.1}

For an integer scale `m>=1`, put

\[
 g_m(n)=\mathbf1_{m\le n<2m}
        -{1\over2}\mathbf1_{2m\le n<4m}.
\tag{L-29805.2}

Then

\[
 h(t-\log m)=g_m(n)
\]

for every

\[
 \log n\le t<\log(n+1).
\tag{L-29805.3}

## 2. Exact sample representation

Let `(x_m)` be finitely supported and define

\[
 f_x(t)=\sum_mx_mh(t-\log m),
\tag{L-29805.4}

\[
 F_x(n)=\sum_mx_mg_m(n).
\tag{L-29805.5}

Equation (L-29805.3) gives

\[
\boxed{
 f_x(t)=F_x(n)
 \quad\text{on }[\log n,\log(n+1)).
}
\tag{L-29805.6]

Consequently the physical norm is the exact weighted sample norm

\[
\boxed{
 \int_0^\infty|f_x(t)|^2dt
 =\sum_{n\ge1}\log{n+1\over n}\,|F_x(n)|^2.
}
\tag{L-29805.7]

## 3. Exact carry intertwiner

PR #269 proves the pointwise source wavelet

\[
 Z_{n,m}(j)=g_m(n)-g_m(j)-g_m(n-j).
\tag{L-29805.8]

Therefore

\[
\boxed{
 \sum_mx_mZ_{n,m}(j)
 =F_x(n)-F_x(j)-F_x(n-j).
}
\tag{L-29805.9]

Thus the complete source recombination commutes with the map

\[
 f(t)\longmapsto
 F(n)-F(j)-F(n-j).
\]

The physical compact step basis and the atomized additive-split carry basis are not merely analogous; they are two exact representations of one finite coefficient vector.

## 4. Exact annular row frame

Assume

\[
 x_m=0\quad\text{unless }M\le m<2M.
\tag{L-29805.10]

Then

\[
 F_x(n)=0\quad\text{unless }M\le n<8M.
\tag{L-29805.11]

Set

\[
 N=16M.
\]

For every `j` in the support of `F_x`, the reflected index `N-j` lies outside that support, and `F_x(N)=0`.  Hence

\[
 F_x(N)-F_x(j)-F_x(N-j)=-F_x(j).
\]

The reflected copy gives

\[
\boxed{
 {1\over N+1}
 \sum_{j=0}^{N}
 |F_x(N)-F_x(j)-F_x(N-j)|^2
 ={2\over16M+1}
 \sum_{n=M}^{8M-1}|F_x(n)|^2.
}
\tag{L-29805.12]

Put the left side equal to `E_M(x)`.  Since

\[
 {1\over n+1}
 \le\log{n+1\over n}
 \le{1\over n},
\]

one obtains

\[
\boxed{
 E_M(x)
 \le\int|f_x(t)|^2dt
 \le{17\over2}E_M(x).
}
\tag{L-29805.13]

The constants are absolute.  This is a source-specific physical/carry frame on every multiplicative annulus.

## 5. Polarization

Every identity above polarizes.  For two coefficient vectors `x,y` supported in the same annulus,

\[
 \int f_x\overline{f_y}
 =\sum_n\log{n+1\over n}F_x(n)\overline{F_y(n)},
\]

and the carry-row bilinear form at `N=16M` is the corresponding reflected-copy sample Gram.  Thus (L-29805.13) is a congruence estimate on the entire annular source span, not only on individual wavelets.

## 6. Scope correction

The window `h` is the physical realization of the finite dyadic numerator

\[
 (1-2^{-s})(1-2^{-s-1})/s.
\]

It is not, by itself, the inverse-zeta prime signal in PR #241.  Applying `omega_2` once in the coefficients and again through the carry wavelet would double-count the source.

Therefore this lemma supplies:

- an exact sampling adapter;
- a proof-grade mutation for a proposed physical-to-carry map;
- an annular frame for the finite numerator potential.

It does **not** identify the full independent-frequency prime normal Gram with the carry Gram without the remaining source convolution and boundary ledger.

## 7. Proof boundary

Closed exactly:

1. the step-function sample representation;
2. the weighted physical norm identity;
3. the additive-split carry intertwiner;
4. the annular frame inequality;
5. polarization.

Open:

1. insertion of the complete inverse-zeta/generalized-prime source;
2. a strict global recurrence;
3. RH.
