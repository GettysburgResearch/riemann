# L-32311 — Uniform carry Schur reserve for the critical-null wavelet

Claim ID: `L-32311`  
Title: The critical-null compact wavelet stays uniformly transverse to the actual generalized-prime Kummer profile on every sufficiently large row  
Status: **PROPOSED COMPLETE ELEMENTARY LEMMA — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: `L-32302`; the binomial-log variance argument of PR #269 `L-26902`  
Scope: one-wavelet carry reserve; no collective source-change recurrence or RH conclusion

## 1. Profiles

For a row `n`, let

\[
F_n(j)=\log\binom nj,
\qquad0\le j\le n.
\]

For a scale `m`, let

\[
Z_{n,m}(j)=g_m(n)-g_m(j)-g_m(n-j)
\]

be the critical-null wavelet of `L-32302/L-32308`, where `g_m` changes only at

\[
m,\ 2m,\ 4m,\ 8m.
\]

Let the generalized-prime profile be

\[
P_n^\dagger(j)
=\sum_{q\le n}\Lambda_\dagger(q)\chi_{n,q}(j).
\]

Since

\[
\Lambda_\dagger(q)
=\Lambda(q)
 +(\log2)(1+2^{-r}+2^{r/2})\mathbf1_{q=2^r},
\]

one has

\[
\boxed{P_n^\dagger=F_n+D_n}
\tag{L-32311.1}
\]

with

\[
D_n(j)=(\log2)
\sum_{2^r\le n}(1+2^{-r}+2^{r/2})\chi_{n,2^r}(j)\ge0.
\tag{L-32311.2}
\]

## 2. The digital correction is lower order in row energy

Since every carry indicator is at most one,

\[
D_n(j)
\le
\log n+2\log2
 +(\log2)\sum_{2^r\le n}2^{r/2}.
\]

The geometric sum satisfies

\[
\sum_{r=1}^{\lfloor\log_2n\rfloor}2^{r/2}
\le{\sqrt2\over\sqrt2-1}\sqrt n<4\sqrt n.
\]

For `n>=16`, `log n<=sqrt n`, and therefore

\[
\boxed{0\le D_n(j)\le5\sqrt n.}
\tag{L-32311.3}
\]

Hence

\[
\boxed{\|D_n\|_2\le8n}
\tag{L-32311.4}
\]

for `n>=16`, where the norm is the unnormalized Euclidean norm on `j=0,...,n`.

On the other hand, for

\[
k=\lfloor n/3\rfloor,
\]

and `n>=12`, the central binomial block gives

\[
F_n(j)\ge {n\over4}\log3
\qquad(k\le j\le n-k).
\]

There are at least `n/3` such indices, so

\[
\boxed{
\|F_n\|_2^2
\ge{(\log3)^2\over48}n^3
>{n^3\over48}.
}
\tag{L-32311.5}
\]

Thus

\[
{\|D_n\|_2\over\|F_n\|_2}
\le {8\sqrt{48}\over\sqrt n}
<{56\over\sqrt n}.
\tag{L-32311.6}
\]

## 3. Variance reserve for one wavelet

Use the same central interval

\[
I_n=
\left[
\left\lceil{n\over4}\right\rceil,
\left\lfloor{n-2\over3}\right\rfloor
\right]\cap\mathbb Z.
\]

For consecutive `j,j+1` there,

\[
F_n(j+1)-F_n(j)
=\log{n-j\over j+1}\ge\log2.
\tag{L-32311.7}
\]

The wavelet `Z_(n,m)` can change only when `j` crosses one of

\[
m,2m,4m,8m,n-m,n-2m,n-4m,n-8m.
\]

These at most eight locations split `I_n` into at most nine constant runs. Since `|I_n|>=n/15`, one run has length

\[
L\ge n/135.
\]

For `n>=270`, `L>=2`. On that run, for every scalar `a`, the pairwise variance identity gives

\[
\sum_{j=0}^n(F_n(j)-aZ_{n,m}(j))^2
\ge{(\log2)^2L(L^2-1)\over12}
\ge{(\log2)^2n^3\over24\cdot135^3}.
\tag{L-32311.8}
\]

Since `0<=F_n(j)<=n log2`,

\[
\|F_n\|_2^2\le2n^3(\log2)^2.
\]

Therefore

\[
\boxed{
\min_a\|F_n-aZ_{n,m}\|_2^2
\ge\kappa_0\|F_n\|_2^2,
\qquad
\kappa_0={1\over120000000}.
}
\tag{L-32311.9}
\]

The chosen constant is slightly smaller than the exact value `1/(48*135^3)`.

## 4. Transfer to the actual generalized-prime profile

For

\[
n\ge2\cdot10^{12},
\]

(L-32311.6) gives

\[
{\|D_n\|_2\over\|F_n\|_2}
<{\sqrt{\kappa_0}\over2}.
\]

Hence for every scalar `a`,

\[
\begin{aligned}
\|P_n^\dagger-aZ_{n,m}\|_2
&\ge\|F_n-aZ_{n,m}\|_2-\|D_n\|_2\\
&\ge{\sqrt{\kappa_0}\over2}\|F_n\|_2.
\end{aligned}
\]

Also

\[
\|P_n^\dagger\|_2
\le(1+\sqrt{\kappa_0}/2)\|F_n\|_2<2\|F_n\|_2.
\]

Therefore

\[
\boxed{
\min_{a\in\mathbb R}
\|P_n^\dagger-aZ_{n,m}\|_2^2
\ge{1\over2000000000}\|P_n^\dagger\|_2^2
}
\tag{L-32311.10}
\]

uniformly in `m`, for every `n>=2*10^12`.

The huge threshold is deliberately conservative; only existence of an absolute threshold and reserve is used. Every smaller row is finite and belongs in a production certificate if this route is pursued.

## 5. Proof boundary

Closed exactly or elementarily:

- `P_dagger=F+D`;
- the `O(sqrt n)` pointwise correction;
- the long constant-source run;
- an absolute reserve for the ordinary Kummer profile;
- transfer of that reserve to the actual generalized-prime profile.

Open:

- a collective reserve for the complete RH-sensitive source-change family;
- a strict annular recurrence;
- RH.
