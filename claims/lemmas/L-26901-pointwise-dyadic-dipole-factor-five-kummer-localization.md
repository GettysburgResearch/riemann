# L-26901 — Pointwise dyadic dipole and factor-five Kummer localization

Claim ID: `L-26901`  
Title: The opposite-parity dyadic source is a compact pointwise carry wavelet, and every negative logarithmic Kummer coupling lies in one fixed factor-five transition band  
Status: **PROPOSED EXACT LEMMA — COMPLETE FINITE ALGEBRA AND ELEMENTARY SIGN PROOF**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-26201`; PR #268 `L-26201`; Kummer's theorem; elementary binomial monotonicity  
Scope: source-specific carry/reflected localization; no transition-band contraction or RH conclusion

## 1. Scaled dyadic two-contact source

Retain

\[
b_2(k)=\mu(k)-\mathbf 1_{2\mid k}\mu(k/2)
\]

and the carry indicator

\[
\chi_{n,q}(j)
=\left\lfloor {n\over q}\right\rfloor
 -\left\lfloor {j\over q}\right\rfloor
 -\left\lfloor {n-j\over q}\right\rfloor .
\]

For integers `m>=1`, `n>=1`, and `0<=j<=n`, define

\[
Y_{n,m}(j)
=\sum_{k\le n/m}b_2(k)\chi_{n,mk}(j).
\tag{L-26901.1}
\]

Since

\[
\mathbf 1*b_2=\varepsilon-\delta_2,
\]

one has, for every real `x>=0`,

\[
\sum_{k\le x/m}b_2(k)\left\lfloor{x\over mk}\right\rfloor
=\mathbf 1_{m\le x<2m}.
\tag{L-26901.2}
\]

Substitution in the floor formula for the carry gives the exact scaled box
identity

\[
\boxed{
Y_{n,m}(j)
=
\mathbf 1_{m\le n<2m}
-\mathbf 1_{m\le j<2m}
-\mathbf 1_{m\le n-j<2m}.
}
\tag{L-26901.3}
\]

The old `m=1` two-contact theorem is the first member of this complete scaled
family.

## 2. The opposite-parity source is a compact pointwise wavelet

Define

\[
\boxed{
\omega_2(k)
=b_2(k)-\frac12\mathbf 1_{2\mid k}b_2(k/2)
=\mu(k)-\frac32\mathbf1_{2\mid k}\mu(k/2)
 +\frac12\mathbf1_{4\mid k}\mu(k/4).
}
\tag{L-26901.4}
\]

Its Dirichlet series is

\[
\sum_{k\ge1}{\omega_2(k)\over k^s}
={ (1-2^{-s})(1-2^{-s-1})\over\zeta(s)}.
\tag{L-26901.5}
\]

The extra Euler factor has no zero in `Re s>0`, so this source has the same
rightmost-zero obstruction as the dyadic shell.

Put

\[
g_m(x)
=\mathbf1_{m\le x<2m}
 -\frac12\mathbf1_{2m\le x<4m}.
\tag{L-26901.6}
\]

The pointwise carry profile of the complete source is

\[
\begin{aligned}
Z_{n,m}(j)
&=\sum_{k\le n/m}\omega_2(k)\chi_{n,mk}(j)\\
&=Y_{n,m}(j)-\frac12Y_{n,2m}(j).
\end{aligned}
\]

Hence

\[
\boxed{
Z_{n,m}(j)=g_m(n)-g_m(j)-g_m(n-j).
}
\tag{L-26901.7}
\]

This is a literal compact carry wavelet before averaging, taking a norm, or
passing to a quotient polytope.

## 3. Pointwise sign bands

The wavelet has two exact pointwise sign sectors.

### Inner band

If

\[
m\le n<2m,
\]

then `g_m(n)=1`, neither `j` nor `n-j` can enter the negative band
`[2m,4m)`, and they cannot both lie in `[m,2m)`. Therefore

\[
\boxed{Z_{n,m}(j)\ge0\quad(0\le j\le n).}
\tag{L-26901.8}
\]

### Outer band

If

\[
2m\le n<4m,
\]

then `g_m(n)=-1/2`. At most one of `j,n-j` can lie in `[2m,4m)`. If one does,
the other contributes either zero or `+1`; if neither does, both contributions
are nonnegative. In every case

\[
\boxed{Z_{n,m}(j)\le0\quad(0\le j\le n).}
\tag{L-26901.9}
\]

Thus the source itself contains an exact positive inner band and negative outer
band. The affine carry tail beyond `4m` cancels pointwise in the source
coefficient, but its reflected Kummer coupling still needs a sign calculation.

## 4. Reflected logarithmic Kummer coupling

Put

\[
F_n(j)=\log\binom nj
\]

and define

\[
\boxed{
\mathcal K(n,m)
={1\over n+1}\sum_{j=0}^n Z_{n,m}(j)F_n(j).
}
\tag{L-26901.10}
\]

Kummer's theorem identifies this as the reflected coupling of the dyadic
source with the ordinary von Mangoldt carry profile.

The pointwise sign bands imply immediately

\[
\mathcal K(n,m)\ge0
\quad(m\le n<2m),
\tag{L-26901.11}
\]

and

\[
\mathcal K(n,m)\le0
\quad(2m\le n<4m).
\tag{L-26901.12}
\]

For `n>=4m`, `g_m(n)=0`; symmetry of `F_n` gives

\[
\boxed{
(n+1)\mathcal K(n,m)
=D(n,m),
}
\tag{L-26901.13}
\]

where

\[
\boxed{
D(n,m)
=\sum_{j=2m}^{4m-1}F_n(j)
 -2\sum_{j=m}^{2m-1}F_n(j).
}
\tag{L-26901.14}
\]

## 5. The far coupling is nonnegative from factor five onward

### Monotonicity in the parent row

Let `N=n+1`. Since

\[
F_{n+1}(j)-F_n(j)
=\log{N\over N-j},
\]

the equal total coefficient in (L-26901.14) cancels the `log N` terms and gives

\[
\boxed{
\exp(D(n+1,m)-D(n,m))
=
{\displaystyle
 \prod_{r=0}^{m-1}(N-m-r)^2
 \over\displaystyle
 \prod_{r=0}^{m-1}(N-2m-r)(N-3m-r)}.
}
\tag{L-26901.15}
\]

For `n>=4m`, every factor is positive, and each copy of `N-m-r` is strictly
larger than the corresponding factors `N-2m-r` and `N-3m-r`. Hence

\[
\boxed{D(n+1,m)>D(n,m)\qquad(n\ge4m).}
\tag{L-26901.16}
\]

### The factor-five base row

At `n=5m`, use

\[
F_{5m}(j)=F_{5m}(5m-j).
\]

Splitting the first sum in (L-26901.14) at `3m` gives

\[
\boxed{
D(5m,m)
=
\sum_{r=0}^{m-1}
 [F_{5m}(2m+r)-F_{5m}(m+r)]
 +F_{5m}(2m)-F_{5m}(m).
}
\tag{L-26901.17}
\]

The sequence `F_(5m)(j)` is nondecreasing in the distance coordinate
`min(j,5m-j)`. For every `0<=r<m`,

\[
\min(2m+r,3m-r)\ge m+r,
\]

and also `2m>=m`. Therefore every bracket in (L-26901.17) is nonnegative:

\[
D(5m,m)\ge0.
\tag{L-26901.18}
\]

Combining (L-26901.16)--(L-26901.18) proves

\[
\boxed{
\mathcal K(n,m)\ge0
\qquad(n\ge5m).
}
\tag{L-26901.19}
\]

## 6. Exact localization of every negative reflected row

Equations (L-26901.11), (L-26901.12), and (L-26901.19) give the fail-closed
localization

\[
\boxed{
(\mathcal K(n,m))_-\ne0
\quad\Longrightarrow\quad
2m\le n<5m.
}
\tag{L-26901.20}
\]

Thus the complete RH-bearing opposite-parity source has no negative reflected
Kummer coupling in the infinite quotient tail. Every possible negative row is
confined to the three full quotient cells `2,3` and the transition cell `4`.

This is substantially smaller than:

- a generic balanced Type-II packet;
- all odd-column leakage;
- an unbounded terminal-face dictionary;
- a full Green-energy estimate.

It is also source specific: the same-sign odd Möbius cube is retained and
paired with its actual dyadic siblings before the sign is taken.

## 7. Correct next theorem

The remaining physical theorem is now a **factor-five transition contraction**
on the actual two-frequency normal Gram. A production object need only retain
and certify the complete source matrices for

\[
2m\le n<5m,
\]

including every dyadic sibling and every cross term. The inner band and the
entire far tail are already nonnegative in the logarithmic Kummer projection.

This lemma does not assert that scalar Kummer positivity alone controls the
physical normal Gram. The reviewed independent-frequency source map remains
mandatory.

## 8. Proof boundary

Closed exactly:

1. the scaled `b_2` box identity;
2. the pointwise compact `omega_2` wavelet;
3. its positive inner and negative outer sign bands;
4. the exact far-field Kummer formula;
5. monotonicity in `n` and the factor-five base inequality;
6. localization of every negative logarithmic Kummer row to `2m<=n<5m`.

Open:

1. the source-specific two-frequency transition LMI on that finite ratio band;
2. DSS or an equivalent shell-energy contraction;
3. RH.
