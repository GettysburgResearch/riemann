# L-102008 — The two Vaughan Möbius wings collapse to one Möbius owner with positive multiplicity

Claim ID: `L-102008`
Status: **PROVED EXACT ARITHMETIC REDUCTION**
Created: 2026-08-21
Depends on: `L-102001`
RH status: **not assumed**

Retain the audited gcd form

\[
\mathcal B_U(X)
=\sum_{\substack{g,a,b\ge1\\\mu^2(gab)=1\\ga>U,\ gb>U}}
\frac{\mu(a)\mu(b)}{g\sqrt{ab}}
\mathcal L_K\!\left(\frac{X}{g^2ab}\right).
\tag{L-102008.1}
\]

For `V>0` and squarefree `m`, define the ordered balanced-divisor
multiplicity

\[
\boxed{
N_V(m)
=\sum_{a\mid m}
\mathbf1_{a>V}\mathbf1_{m/a>V}.
}
\tag{L-102008.2}
\]

Set `m=ab`. Since `mu^2(gab)=1`, the factors `a` and `b` are coprime and
squarefree. Therefore

\[
\mu(a)\mu(b)=\mu(ab)=\mu(m),
\]

independently of how the prime factors of `m` are split between the two wings.
Summing over those ordered splits gives

\[
\boxed{
\mathcal B_U(X)
=\sum_{\substack{g,m\ge1\\\mu^2(gm)=1}}
\frac{\mu(m)}{g\sqrt m}
N_{U/g}(m)
\mathcal L_K\!\left(\frac{X}{g^2m}\right).
}
\tag{L-102008.3}
\]

Thus the common gcd core is sign-free and the apparent two-wing sign
`mu(a)mu(b)` is exactly one Möbius sign `mu(m)`. The price is the explicit
nonnegative multiplicity `N_(U/g)(m)`.

## Immediate support geometry

From the definition,

\[
N_V(m)>0\quad\Longrightarrow\quad m>V^2.
\tag{L-102008.4}
\]

If `supp K subset [1,C]` and the summand in (L-102008.3) is active, then

\[
g^2m\le X.
\tag{L-102008.5}
\]

For `U=floor(X^(1/3))`, (L-102008.4)--(L-102008.5) place the single signed wing
in the exact band

\[
\frac{U^2}{g^2}<m\le\frac{X}{g^2}.
\tag{L-102008.6}
\]

No independent summation over `g` and `m` is asserted; the physical cutoff is
still coupled.

## Exact unique-largest-prime recurrence

Let `m=pc` be squarefree with `p` not dividing `c`. Partition the divisors of
`pc` according to whether they contain `p`. Directly from (L-102008.2),

\[
\begin{aligned}
N_V(pc)
={}&\sum_{a\mid c}
 \mathbf1_{a>V}\mathbf1_{pc/a>V}\\
&+\sum_{a\mid c}
 \mathbf1_{pa>V}\mathbf1_{c/a>V}.
\end{aligned}
\]

Replacing `a` by `c/a` in the second sum shows that the two sums are equal.
Hence

\[
\boxed{
N_V(pc)
=2\sum_{a\mid c}
\mathbf1_{a>V}\mathbf1_{c/a>V/p}.
}
\tag{L-102008.7}
\]

Choose now `p=P^+(m)`. This owner is unique, and

\[
\boxed{
\mu(m)N_V(m)
=-2\mu(c)
\sum_{a\mid c}
\mathbf1_{a>V}\mathbf1_{c/a>V/p}.
}
\tag{L-102008.8}
\]

The divisor count on the right is nonnegative. If `p>V`, the second threshold
is automatic and

\[
\boxed{
N_V(pc)=2\#\{a\mid c:a>V\}.
}
\tag{L-102008.9}
\]

## Matrix meaning

The balanced Vaughan terminal is therefore not intrinsically a two-Möbius
sign problem. After exact gcd grouping and unique largest-prime ownership it
has:

```text
one sign-free square core g^2;
one unique largest prime p of the wing m;
one remaining Möbius sign mu(c);
one positive oriented divisor multiplicity.
```

This is the first exact source dictionary aligning the large-divisor Hankel
form with the largest-prime / positive-divisor-renewal mechanism of
`L-100603`. It does not yet prove the required negative-mass estimate: the
positive multiplicity, the `g` cutoff, and the owner-frozen kernel remain
coupled.