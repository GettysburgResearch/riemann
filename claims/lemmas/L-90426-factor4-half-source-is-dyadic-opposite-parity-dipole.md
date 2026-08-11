# L-90426 — The factor-four half-filter is exactly the dyadic opposite-parity dipole

Claim ID: `L-90426`  
Title: The spectral half of the phase-locked factor-16 filter is the existing dyadic opposite-parity Möbius source, with positive inverse, zero bare field, and an exact two-row average-carry image  
Status: **PROPOSED COMPLETE EXACT IDENTIFICATION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90423`--`L-90425`; the average-carry matrix definition; overlaps the source of PR #268  
Scope: exact source and row algebra; no sign theorem or RH conclusion

## 1. Minimal factor-four source

Let

\[
P_2(y)=(1-y)(1-y/2)
 =1-\frac32y+\frac12y^2.
\tag{L-90426.1}
\]

Define

\[
\boxed{
\Omega_2(s)=\frac{P_2(2^{-s})}{\zeta(s)}
}
\tag{L-90426.2}
\]

and let `omega_2` be its coefficient sequence. Then

\[
\boxed{
\omega_2(n)
 =\mu(n)-\frac32\mathbf1_{2\mid n}\mu(n/2)
   +\frac12\mathbf1_{4\mid n}\mu(n/4).
}
\tag{L-90426.3}
\]

This is exactly the dyadic opposite-parity dipole previously isolated on PR #268.

The factor-four endpoint half-filter of `L-90425`,

\[
\mathcal G(X)
 =\mathcal H(X)-\frac32\mathcal H(X/2)
  +\frac12\mathcal H(X/4),
\tag{L-90426.4}
\]

has Mellin multiplier `P_2(2^-s)`. Its kernel is supported on `[X/4,X]`:

\[
\boxed{
W_2(u)=
\begin{cases}
\frac12-4u,&1/4<u\le1/2,\\
2u-1,&1/2<u\le1,\\
0,&\text{otherwise}.
\end{cases}}
\tag{L-90426.5}
\]

The roots `y=1,2` lie on `Re s=0,-1`, so the half-filter is itself zero-safe in the open critical strip.

## 2. Positive inverse and generalized primes

Let

\[
B_2(s)=\Omega_2(s),
\qquad A_2(s)=B_2(s)^{-1}.
\]

At two,

\[
\boxed{
A_{2,\mathrm{loc}}(y)
 =\frac1{(1-y)^2(1-y/2)}.
}
\tag{L-90426.6}
\]

Hence every inverse coefficient is positive. The generalized von Mangoldt sequence satisfies

\[
\Lambda_2(p^k)=\log p\quad(p\text{ odd}),
\tag{L-90426.7}
\]

and

\[
\boxed{
\Lambda_2(2^k)
 =\left(2+2^{-k}\right)\log2>0.
}
\tag{L-90426.8}
\]

The coefficientwise Jordan ratios `A_2(s-tau)/A_2(s)` are nonnegative for every `tau>=0`, by the same geometric-factor calculation as in `L-90424`.

## 3. Zero-bare field

Multiplication by zeta gives

\[
\boxed{
\mathbf1*\omega_2
 =\delta_1-\frac32\delta_2+\frac12\delta_4.
}
\tag{L-90426.9}
\]

Its prefix is

\[
H_2(m)=
\begin{cases}
0,&m=0,\\
1,&m=1,\\
-1/2,&m=2,3,\\
0,&m\ge4.
\end{cases}
\tag{L-90426.10}
\]

Thus every deep balanced bare carry row vanishes exactly.

## 4. Exact two-row average-carry image

For

\[
\beta_{nq}
 =\frac{\lfloor n/q\rfloor
        [q-1-(n\bmod q)]}{n+1},
\tag{L-90426.11}
\]

finite averaging of the prefix/carry identity gives, for any source `b` with prefix potential `H_b`,

\[
\sum_{q=2}^n b(q)\beta_{nq}
 =H_b(n)-\frac2{n+1}\sum_{j=0}^nH_b(j).
\tag{L-90426.12}
\]

Applying (L-90426.10),

\[
\boxed{
\sum_{q=2}^n\omega_2(q)\beta_{nq}
 =
\begin{cases}
-5/6,&n=2,\\
-1/2,&n=3,\\
0,&n\ge4.
\end{cases}}
\tag{L-90426.13}
\]

So the entire infinite source is compressed by the average-carry matrix to the bottom two rows.

## 5. Own-current relation

Let

\[
q_2=-\omega_2\log=\omega_2*\Lambda_2.
\tag{L-90426.14}
\]

The divisor-prefix current satisfies

\[
\zeta(s)B_2'(s)
 =P_2'(2^{-s})
 +P_2(2^{-s})\left(-\frac{\zeta'}{\zeta}(s)\right),
\tag{L-90426.15}
\]

with the derivative interpreted in `s`. Therefore the ordinary factor-four scalar (L-90426.4) is the own current of `omega_2` plus only a fixed dyadic gauge supported at `2,4`.

This identifies the endpoint half-filter, the old bottom-charge source, and the zero-bare positive-inverse current as one object.

## 6. Proof boundary

Closed exactly here:

1. factor-four source identification;
2. annular kernel;
3. positive inverse and generalized primes;
4. positive Jordan deformation;
5. zero-bare prefix;
6. exact two-row carry image;
7. own-current typing.

Open:

1. bottom-charge sign or growth;
2. factor-four current energy;
3. RH.
