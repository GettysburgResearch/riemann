# L-26902 — Uniform source-specific Schur reserve for the factor-five carry transition

Claim ID: `L-26902`  
Title: The opposite-parity carry wavelet has an absolute strict Schur reserve against the logarithmic Kummer profile on every sufficiently large row  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-26901`; elementary binomial monotonicity and variance identities  
Scope: carry-feature Schur reserve; no physical normal-Gram transference or RH conclusion

## 1. The two row vectors

Fix integers

\[
n\ge210,
\qquad m\ge1.
\]

Let

\[
Z_j=Z_{n,m}(j)
\qquad(0\le j\le n)
\]

be the pointwise opposite-parity wavelet of `L-26901`, and put

\[
F_j=\log\binom nj.
\tag{L-26902.1}
\]

Use the normalized inner product

\[
\langle u,v\rangle_n
={1\over n+1}\sum_{j=0}^nu_jv_j.
\tag{L-26902.2}
\]

The corresponding two-channel carry Gram is

\[
\mathcal G_{n,m}
=
\begin{pmatrix}
\langle Z,Z\rangle_n&\langle Z,F\rangle_n\\
\langle F,Z\rangle_n&\langle F,F\rangle_n
\end{pmatrix}
\succeq0.
\tag{L-26902.3}
\]

The issue is whether its Schur complement can degenerate as `n,m` grow through
the transition band.

## 2. A central interval with a fixed logarithmic slope

Define

\[
I_n
=
\left[
\left\lceil{n\over4}\right\rceil,
\left\lfloor{n-2\over3}\right\rfloor
\right]\cap\mathbb Z.
\tag{L-26902.4}
\]

For consecutive points `j,j+1` in this interval,

\[
F_{j+1}-F_j
=
\log{n-j\over j+1}
\ge\log2,
\tag{L-26902.5}
\]

because `3j<=n-2`.

The number of integer points in `I_n` is at least

\[
|I_n|\ge{n\over15}
\qquad(n\ge210).
\tag{L-26902.6}
\]

## 3. The source is constant on one long subinterval

The wavelet is

\[
Z_j=g_m(n)-g_m(j)-g_m(n-j),
\]

where `g_m` changes only at

\[
m,\ 2m,\ 4m.
\]

Therefore `Z_j` can change only when `j` crosses one of at most six locations:

\[
m,\ 2m,\ 4m,\ n-m,\ n-2m,\ n-4m.
\tag{L-26902.7}
\]

These cut `I_n` into at most seven consecutive constant runs. One run `J` has
length

\[
\boxed{
L:=|J|
\ge{|I_n|\over7}
\ge{n\over105}
\ge2.
}
\tag{L-26902.8}
\]

Write the common source value on this run as `z_0`.

## 4. Quantitative variance on the constant-source run

For any real scalar `a`, the value `a z_0` is constant on `J`. Let the
consecutive values of `F` there be

\[
x_0,x_1,\ldots,x_{L-1}.
\]

Equation (L-26902.5) gives

\[
x_v-x_u\ge(v-u)\log2
\qquad(v>u).
\tag{L-26902.9}
\]

For every constant `c`, the pairwise variance identity gives

\[
\begin{aligned}
\sum_{r=0}^{L-1}(x_r-c)^2
&\ge
\sum_{r=0}^{L-1}(x_r-\bar x)^2\\
&={1\over L}\sum_{0\le u<v<L}(x_v-x_u)^2\\
&\ge
{(\log2)^2\over L}
\sum_{0\le u<v<L}(v-u)^2\\
&=
{(\log2)^2L(L^2-1)\over12}.
\end{aligned}
\tag{L-26902.10}
\]

Since `L>=2`,

\[
L(L^2-1)\ge{L^3\over2}.
\]

Taking `c=a z_0` and using (L-26902.8),

\[
\boxed{
\sum_{j=0}^n(F_j-aZ_j)^2
\ge
{(\log2)^2n^3\over24\cdot105^3}.
}
\tag{L-26902.11}
\]

## 5. Comparison with the full Kummer energy

The elementary bound

\[
\binom nj\le2^n
\]

gives

\[
0\le F_j\le n\log2.
\]

Hence

\[
\sum_{j=0}^nF_j^2
\le(n+1)n^2(\log2)^2
\le2n^3(\log2)^2.
\tag{L-26902.12}
\]

Combining (L-26902.11)--(L-26902.12), and using

\[
48\cdot105^3=55,566,000<60,000,000,
\]

proves the uniform estimate

\[
\boxed{
\min_{a\in\mathbb R}
\sum_{j=0}^n(F_j-aZ_j)^2
\ge
{1\over60,000,000}
\sum_{j=0}^nF_j^2.
}
\tag{L-26902.13}
\]

The constant is deliberately conservative. It is absolute and independent of
`m`, including every row in the factor-five transition band.

## 6. Strict Schur complement

If `Z` is nonzero, the minimizing scalar is

\[
a_*={\langle Z,F\rangle_n\over\langle Z,Z\rangle_n}.
\]

Therefore (L-26902.13) is exactly

\[
\boxed{
\langle F,F\rangle_n
-{|\langle Z,F\rangle_n|^2\over\langle Z,Z\rangle_n}
\ge
{1\over60,000,000}
\langle F,F\rangle_n.
}
\tag{L-26902.14}
\]

Equivalently,

\[
\boxed{
\mathcal G_{n,m}
\succeq
\begin{pmatrix}
0&0\\
0&(60,000,000)^{-1}\langle F,F\rangle_n
\end{pmatrix}
}
\tag{L-26902.15}
\]

after completing the source square. If `Z=0`, the same conclusion is
immediate.

Thus the transition carry Gram has a genuine source-specific reserve. The
rank-one bulk degeneracy of the parity/carry transform does not persist after
the actual finite Kummer profile and its spatial variation are retained.

## 7. What this closes and what it does not

This lemma removes one ambiguity from `F5TC`: the logarithmic carry feature
cannot be asymptotically collinear with the exact `omega_2` wavelet. There is a
uniform strict reserve on every sufficiently large row. The finitely many rows
`n<210` can be included directly in any production certificate.

It does **not** prove that the physical two-frequency normal Gram is the carry
Gram. A successful full proof still needs an exact bounded source map from the
physical transition matrices to these carry features, with every cross term and
boundary row retained.

## 8. Proof boundary

Closed exactly:

1. a long constant-source run on every row;
2. a uniform variance lower bound for the binomial-log feature;
3. the absolute Schur reserve `(60,000,000)^-1`;
4. its application to all factor-five transition rows with `n>=210`.

Open:

1. the physical-normal-to-carry transference;
2. finite boundary replay for `n<210` as part of the production object;
3. DSS/shell contraction;
4. RH.
