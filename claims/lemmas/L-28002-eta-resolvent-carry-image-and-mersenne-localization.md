# L-28002 — The eta-resolvent carry source is positive off the Mersenne collar

Claim ID: `L-28002`  
Title: The complete odd-Möbius eta source has an exact binary-scale carry image; central splits are positive except at `2^r-1`  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-28001`; the floor formula for carry indicators  
Scope: exact source/carry algebra; no cofinal flow or RH conclusion

## 1. Eta-resolvent coefficient

Let `a_eta(n)` be the coefficient of

\[
\frac1{\eta(s)}
=\frac1{(1-2^{1-s})\zeta(s)}.
\]

Writing `n=2^v m` with `m` odd,

\[
a_\eta(n)=
\begin{cases}
\mu(m),&v=0,\\
2^{v-1}\mu(m),&v\ge1.
\end{cases}
\tag{L-28002.1}
\]

Its convolution with the constant-one function is especially simple:

\[
\boxed{
(\mathbf1*a_\eta)(n)
=n\,\mathbf1_{\{n\text{ is a power of }2\}}.
}
\tag{L-28002.2}

Indeed its Dirichlet series is

\[
\zeta(s)\eta(s)^{-1}
=\frac1{1-2^{1-s}}
=\sum_{r\ge0}\frac{2^r}{(2^r)^s}.
\]

## 2. Exact divisor prefix

For integer `x>=1`, put

\[
A_\eta(x)
=\sum_{q\le x}a_\eta(q)\left\lfloor\frac xq\right\rfloor.
\tag{L-28002.3}
\]

Summing (L-28002.2) gives

\[
\boxed{
A_\eta(x)
=\sum_{2^r\le x}2^r
=2^{\lfloor\log_2x\rfloor+1}-1.
}
\tag{L-28002.4}

Set `A_eta(0)=0`.

## 3. Pointwise carry image

For

\[
\chi_{n,q}(j)
=\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac{n-j}{q}\right\rfloor,
\]

define

\[
Y_n(j)=\sum_{q=2}^{n}a_\eta(q)\chi_{n,q}(j).
\tag{L-28002.5}
\]

The `q=1` carry indicator is zero, so (L-28002.4) gives

\[
\boxed{
Y_n(j)
=A_\eta(n)-A_\eta(j)-A_\eta(n-j).
}
\tag{L-28002.6}

Let

\[
L(x)=2^{\lfloor\log_2x\rfloor}
\qquad(x\ge1)
\]

be the largest power of two not exceeding `x`. Then

\[
\boxed{
Y_n(j)=2[L(n)-L(j)-L(n-j)]+1.
}
\tag{L-28002.7}

This is a complete pointwise source identity before averaging, norms, or positive parts.

## 4. Exact sign classification

Fix

\[
L=2^r\le n<2^{r+1}=2L.
\]

Since `j+(n-j)=n<2L`, at most one child can be at least `L`.

### Central binary window

If

\[
n-L<j<L,
\tag{L-28002.8}
\]

then both children are below `L`. Hence

\[
L(j)+L(n-j)\le L
\]

and

\[
\boxed{Y_n(j)\ge1.}
\tag{L-28002.9}

### Exterior binary window

If

\[
j\le n-L
\qquad\text{or}\qquad
j\ge L,
\tag{L-28002.10}
\]

then one child has binary scale `L`, while the other has positive binary scale. Therefore

\[
\boxed{Y_n(j)\le-1.}
\tag{L-28002.11}

Thus the sign is determined exactly by whether the split crosses the current dyadic boundary.

## 5. Central splits and the Mersenne exception

Take the central split

\[
j=\lfloor n/2\rfloor.
\]

If

\[
n\le2L-2,
\]

then

\[
n-L<\lfloor n/2\rfloor<L,
\]

so

\[
\boxed{Y_n(\lfloor n/2\rfloor)\ge1.}
\tag{L-28002.12}

The only row in the binary block `[L,2L)` for which the central window is empty is

\[
\boxed{n=2L-1.}
\tag{L-28002.13}

At this Mersenne row every split has negative source charge. The central split has

\[
\boxed{
Y_{2L-1}(L-1)=1-L.
}
\tag{L-28002.14}

However, the extreme split `1+(n-1)` gives the minimal-magnitude charge

\[
\boxed{
Y_{2L-1}(1)=-1.
}
\tag{L-28002.15}

Thus the complete negative eta-source geometry is concentrated on the logarithmic family

\[
3,7,15,31,\ldots,2^r-1.
\]

## 6. Riesz pairing

Define the eta Riesz coordinate

\[
\mathcal R_\eta(X)
=\sum_{q=2}^{X}
\frac{a_\eta(q)}{\sqrt q}
\log\frac Xq.
\tag{L-28002.16}
\]

For any exact split-flow saturation

\[
\sum_{n,j}d_{n,j}\chi_{n,q}(j)
=q^{-1/2}\log(X/q),
\]

finite interchange gives

\[
\boxed{
\mathcal R_\eta(X)
=\sum_{n,j}d_{n,j}Y_n(j).
}
\tag{L-28002.17}

Therefore a nonnegative exact flow supported in the central binary window away from Mersenne rows, and using the extreme split at Mersenne rows, satisfies

\[
\boxed{
\mathcal R_\eta(X)
\ge
-\sum_{2^r-1\le X}d_{2^r-1,1}.
}
\tag{L-28002.18}

This converts the reciprocal-zeta lower envelope into one explicit logarithmic collar mass.

## 7. Mellin firewall

Termwise integration initially gives

\[
\boxed{
\int_1^\infty
\mathcal R_\eta(X)X^{-z-1}dX
=
\frac{\eta(z+1/2)^{-1}-1}{z^2}.
}
\tag{L-28002.19}

The factor `1-2^(1-s)` has no zero in the open critical strip. Hence every zeta zero with real part greater than `1/2` produces an uncancelled pole in (L-28002.19).

A subpower lower envelope for `R_eta`, obtained for example from (L-28002.18), is therefore an RH-bearing one-sided criterion through the existing Riesz/Landau transfer.

## 8. Proof boundary

Established exactly:

1. the power-of-two convolution collapse;
2. the divisor-prefix formula;
3. the pointwise carry image;
4. the complete sign classification;
5. positivity of every central split except Mersenne rows;
6. the unit negative extreme split at each Mersenne row;
7. the exact Riesz pairing and Mellin source.

Not established:

1. a nonnegative exact saturation flow with subpower Mersenne collar mass;
2. the one-sided eta Riesz bound;
3. RH.