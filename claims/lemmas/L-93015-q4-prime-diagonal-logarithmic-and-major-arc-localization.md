# L-93015 - The Q4 prime diagonal is logarithmic and all distinct-prime obstruction lies on the square-root major arc

Claim ID: `L-93015`  
Status: **PROPOSED COMPLETE UNCONDITIONAL REDUCTION - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: PR #483 at exact head `87bd7ad2127f98b6141b4c03355556f2b95f6404`, especially `L-93242`; PR #383 at `d764be15bd8ea902ad260484eab44d19a9e82175`, especially `L-90411` and `L-90412`; PR #474 at `56eeaccb2b041fdf68b6e718bad85032ecbdc66a`, especially `T-93010` and `L-93013`  
Scope: the complete actual compact-Q4 endpoint row; no estimate for the remaining low-mode distinct-prime correlation and no RH conclusion

## 1. Import the complete prime-base row decomposition

Retain the actual compact-Q4 source

\[
c_\circ(m)
=
\Lambda(m)
-4\mathbf1_{4\mid m}\Lambda(m/4)
+3(\log4)\sum_{r\ge1}\mathbf1_{m=4^r}.
\tag{L-93015.1}
\]

PR #483 `L-93242` partitions it coefficientwise by underlying prime base:

\[
\boxed{
c_\circ(m)=\sum_p c_{\circ,p}(m).
}
\tag{L-93015.2}
\]

The complete four-adic correction is assigned to `p=2`. For endpoint `N`, let

\[
R_N=\sum_{p\le N}R_{N,p}
\qquad\text{in }\mathbb R^N
\tag{L-93015.3}
\]

be the corresponding exact row decomposition, and put

\[
D_N=\sum_{p\le N}\|R_{N,p}\|_2^2.
\tag{L-93015.4}
\]

`L-93242` proves the safe bound `D_N<=576 N^2 log^2 N`. The first advance
here is to sum all prime-tower mass before taking the maximum square.

## 2. Sum the tower mass before squaring

For one prime define

\[
A_{p,N}=\sum_{m\le N}|c_{\circ,p}(m)|.
\tag{L-93015.5}
\]

Let

\[
\psi_p(x)
=
(\log p)\#\{k\ge1:p^k\le x\}.
\tag{L-93015.6}
\]

Then

\[
A_{p,N}
\le
\psi_p(N)+4\psi_p(N/4)
+3(\log4)\mathbf1_{p=2}\#\{r:4^r\le N\}.
\tag{L-93015.7}
\]

Consequently

\[
\boxed{
\sum_pA_{p,N}
\le
\psi(N)+4\psi(N/4)+3\log N.
}
\tag{L-93015.8}
\]

The elementary dyadic central-binomial argument gives the safe Chebyshev bound

\[
\psi(x)\le4x
\qquad(x\ge1).
\tag{L-93015.9}
\]

For `N>=2`,

\[
\sum_pA_{p,N}\le10N.
\tag{L-93015.10}
\]

Also, prime by prime,

\[
A_{p,N}\le8\log(2N).
\tag{L-93015.11}
\]

Hence

\[
\sum_pA_{p,N}^2
\le
\left(\max_pA_{p,N}\right)\sum_pA_{p,N}
\le80N\log(2N).
\tag{L-93015.12}
\]

Every row coordinate is a sum of three prefixes, so

\[
|R_{N,p}(j)|\le3A_{p,N}.
\]

It follows that

\[
\boxed{
D_N
\le9N\sum_pA_{p,N}^2
\le720N^2\log(2N).
}
\tag{L-93015.13}
\]

Thus the complete same-prime diagonal is `O(N^2 log N)`, rather than merely
`O(N^2 log^2 N)`.

For the normalized endpoint PIG,

\[
\mathfrak D_\circ(N)=\frac{D_N}{N^2},
\]

we obtain

\[
\boxed{
0\le\mathfrak D_\circ(N)\le720\log(2N).
}
\tag{L-93015.14}
\]

The coherence bounds of `L-93240/L-93242` improve correspondingly. If

\[
\mathscr P_\circ(N)=N^{-2}\|R_N\|_2^2,
\]

then the canonical obstruction direction has at least

\[
\boxed{
\frac{\mathscr P_\circ(N)}{720\log(2N)}
}
\tag{L-93015.15}
\]

positively projecting prime bases, and every minimum half-carrier has at least

\[
\boxed{
\frac{\mathscr P_\circ(N)}{2880\log(2N)}
}
\tag{L-93015.16}
\]

prime bases.

## 3. Mean and sine coordinates block by block

For each prime block define its row mean

\[
M_{p,N}
=
\frac1N\sum_{j=0}^{N-1}R_{N,p}(j)
=
\sum_{m\le N}c_{\circ,p}(m)
\left(\frac{2m}{N}-1\right).
\tag{L-93015.17}
\]

For `1<=a<N`, define the additive sine coordinate

\[
S_{p,N}(a)
=
\sum_{m=1}^{N-1}c_{\circ,p}(m)
\sin\frac{2\pi am}{N}.
\tag{L-93015.18}
\]

Let

\[
M_N=\sum_pM_{p,N},
\qquad
S_N(a)=\sum_pS_{p,N}(a).
\tag{L-93015.19}
\]

The exact inverse-circle-Laplacian identity of `L-90411` gives

\[
\boxed{
\mathscr P_\circ(N)
=
\frac{|M_N|^2}{N}
+
\frac1{N^3}
\sum_{a=1}^{N-1}
\frac{|S_N(a)|^2}{\sin^2(\pi a/N)}.
}
\tag{L-93015.20}
\]

Applying the same identity to every prime block and polarizing gives the
complete distinct-prime Gram correlation

\[
\boxed{
\begin{aligned}
\mathfrak C_{\ne p}(N)
={}&
\frac2N\sum_{p<r}M_{p,N}M_{r,N}\\
&+
\frac2{N^3}\sum_{a=1}^{N-1}
\frac{\sum_{p<r}S_{p,N}(a)S_{r,N}(a)}
     {\sin^2(\pi a/N)}.
\end{aligned}
}
\tag{L-93015.21}
\]

This is the Fourier form of the positive row-space split in `L-93242`. No
max-kernel or weighted-Goldbach cancellation has been separated prematurely.

The prime-block coordinates themselves are explicit finite prime-power orbit
sums:

\[
\boxed{
\begin{aligned}
S_{p,N}(a)
={}&
(\log p)
\sum_{\substack{k\ge1\\p^k<N}}
\sin\frac{2\pi ap^k}{N}\\
&-
4(\log p)
\sum_{\substack{k\ge1\\4p^k<N}}
\sin\frac{2\pi a(4p^k)}{N}\\
&+
3(\log4)\mathbf1_{p=2}
\sum_{\substack{r\ge1\\4^r<N}}
\sin\frac{2\pi a4^r}{N}.
\end{aligned}
}
\tag{L-93015.22}
\]

Thus the remaining nonzero modes are literal correlations between distinct
prime-power phase orbits.

## 4. The complete coefficient energy is elementary

Using

\[
|u+v+w|^2\le3(|u|^2+|v|^2+|w|^2),
\]

(L-93015.1), the bound

\[
\sum_{m\le x}\Lambda(m)^2
\le(\log x)\psi(x),
\]

and (L-93015.9), one obtains the safe estimate

\[
\boxed{
\sum_{m=1}^{N-1}|c_\circ(m)|^2
\le96N\log(2N).
}
\tag{L-93015.23}
\]

Let

\[
d_N(a)=\min(a,N-a),
\qquad
K_N=\lceil\sqrt N\rceil.
\tag{L-93015.24}
\]

Finite Fourier Parseval gives

\[
\sum_{a=0}^{N-1}|S_N(a)|^2
\le
N\sum_{m=1}^{N-1}|c_\circ(m)|^2.
\tag{L-93015.25}
\]

For `d_N(a)>=K_N`,

\[
\sin\frac{\pi a}{N}
\ge\frac{2d_N(a)}N
\ge\frac{2K_N}N.
\tag{L-93015.26}
\]

Combining (L-93015.23)--(L-93015.26) yields the unconditional minor-arc bound

\[
\boxed{
\frac1{N^3}
\sum_{\substack{1\le a<N\\d_N(a)\ge K_N}}
\frac{|S_N(a)|^2}{\sin^2(\pi a/N)}
\le24\log(2N).
}
\tag{L-93015.27}
\]

This is the complete full-row minor-arc energy after PIG normalization.

## 5. The distinct-prime minor arc is also logarithmic

For each prime block, its centered sine energy is no larger than its complete
row energy. Hence

\[
\frac1{N^3}
\sum_{a=1}^{N-1}
\frac{\sum_p|S_{p,N}(a)|^2}{\sin^2(\pi a/N)}
\le
\frac{D_N}{N^2}
\le720\log(2N).
\tag{L-93015.28}
\]

Define the distinct-prime minor-arc correlation

\[
\mathfrak C_{\ne p}^{\rm min}(N)
=
\frac2{N^3}
\sum_{\substack{1\le a<N\\d_N(a)\ge K_N}}
\frac{\sum_{p<r}S_{p,N}(a)S_{r,N}(a)}
     {\sin^2(\pi a/N)}.
\tag{L-93015.29}
\]

Since

\[
2\sum_{p<r}S_pS_r
=
\left(\sum_pS_p\right)^2-\sum_pS_p^2,
\]

(L-93015.27)--(L-93015.28) give

\[
\boxed{
|\mathfrak C_{\ne p}^{\rm min}(N)|
\le744\log(2N).
}
\tag{L-93015.30}
\]

Thus even the absolute distinct-prime cross correlation is harmless on every
additive mode outside the square-root major arc.

## 6. Pure distinct-prime major-arc criterion

Define

\[
\boxed{
\begin{aligned}
\mathfrak C_{\ne p}^{\rm maj}(N)
={}&
\frac2N\sum_{p<r}M_{p,N}M_{r,N}\\
&+
\frac2{N^3}
\sum_{\substack{1\le a<N\\d_N(a)<K_N}}
\frac{\sum_{p<r}S_{p,N}(a)S_{r,N}(a)}
     {\sin^2(\pi a/N)}.
\end{aligned}
}
\tag{L-93015.31}
\]

There are fewer than

\[
2\lceil\sqrt N\rceil
\]

nonzero additive modes in (L-93015.31), plus the one mean coordinate.

By the complete prime-block Gram split,

\[
\mathscr P_\circ(N)
=
\mathfrak D_\circ(N)
+
\mathfrak C_{\ne p}^{\rm maj}(N)
+
\mathfrak C_{\ne p}^{\rm min}(N).
\tag{L-93015.32}
\]

Equations (L-93015.14) and (L-93015.30) give

\[
\boxed{
\left|
\mathscr P_\circ(N)-\mathfrak C_{\ne p}^{\rm maj}(N)
\right|
\le1464\log(2N).
}
\tag{L-93015.33}
\]

Consequently

\[
\boxed{
\mathscr P_\circ(N)\ll(\log N)^A
\text{ for some fixed }A
\iff
|\mathfrak C_{\ne p}^{\rm maj}(N)|
\ll(\log N)^{A'}
\text{ for some fixed }A'.
}
\tag{L-93015.34}
\]

Conditional on independent acceptance of `T-93010`, this is the sharper Q4
criterion

\[
\boxed{
\mathrm{RH}
\iff
\text{the mean plus fewer than }2\sqrt N+O(1)
\text{ low distinct-prime phase correlations are polylogarithmic.}
}
\tag{L-93015.35}
\]

All same-prime towers, every high additive mode, and the complete four-adic
gauge have been removed unconditionally.

## 7. Large-additive-modulus character form

For a surviving nonzero mode `a` with `d_N(a)<K_N`, put

\[
g=(a,N),\qquad q=N/g.
\]

After replacing `a` by `N-a` when necessary, one has `1<=a<K_N`, and hence

\[
\boxed{
q=\frac{N}{(a,N)}
\ge\frac Na
>\sqrt N.
}
\tag{L-93015.36}
\]

The exact character decomposition of `L-90414` therefore applies to every
surviving nonzero total coordinate with additive modulus above the square-root
scale. The local prime-divisor correction is explicit and polylogarithmic. An
imprimitive character may have smaller primitive conductor, so the statement is
about additive modulus and does not promote every term to large primitive
conductor.

The final Q4 gate may be stated in either coordinate:

```text
prime-block phase form:
    mean + O(sqrt N) low correlations between distinct prime-power orbits;

character form:
    mean + O(sqrt N) weighted covariances of prime sums
    at additive moduli q > sqrt N, with the complete prime diagonal removed.
```

No large-modulus mean-square estimate strong enough for this weighted covariance
is asserted here.

## 8. Relation to the other agent's packet

PR #483 supplies the exact positive prime-block Gram and the canonical coherence
direction. This packet does not duplicate those claims. It strengthens and
localizes them:

```text
PR #483:
    complete row -> prime diagonal + all distinct-prime cross;

this lemma:
    prime diagonal = O(log N) after normalization;
    distinct-prime minor arc = O(log N);
    only mean + O(sqrt N) low distinct-prime modes remain.
```

The Q4 route has therefore moved from a full endpoint Gram to one deterministic
square-root-major-arc resonance theorem between different Euler factors.

## 9. Proof boundary

Established unconditionally, subject to review:

1. improved complete prime diagonal `D_N<=720 N^2 log(2N)`;
2. improved prime-carrier lower bounds with one logarithmic denominator;
3. exact prime-block mean/sine decomposition;
4. explicit prime-power phase-orbit formula;
5. complete coefficient energy `O(N log N)`;
6. full-row minor-arc PIG bound;
7. absolute distinct-prime minor-arc bound;
8. reduction to the pure distinct-prime square-root major arc.

Imported and not re-proved:

- the complete prime-base row split of PR #483;
- the endpoint-PIG-to-RH criterion of `T-93010`.

Open:

1. polylogarithmic control of (L-93015.31);
2. endpoint PIG;
3. RH.
