# L-90419 — The classical Selberg integral closes every nonmean PIG Haar mode

Claim ID: `L-90419`  
Title: The unconditional Selberg–Saffari–Vaughan mean square for primes in short intervals bounds the complete nonconstant Haar tree of the compact-Q4 innovation at PIG scale; the sole surviving endpoint scalar is the mean mode  
Status: **PROPOSED COMPLETE UNCONDITIONAL REDUCTION USING A CLASSICAL EXTERNAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90416`, `R-90411`; the classical Selberg integral bound of Saffari–Vaughan  
Scope: one integer endpoint `N=2^M`; it proves the nonmean continuous-position energy bound, not the mean estimate, deterministic PIG, the repaired global PIG-to-pole adapter, or RH

## 1. Classical external input

Write

\[
 \psi(x)=\sum_{n\le x}\Lambda(n)
\]

and, for integers `x>=0`, `h>=1`,

\[
 \mathcal E(x,h)
 =\psi(x+h)-\psi(x)-h.
\tag{L-90419.1}
\]

We use the classical unconditional Selberg-integral estimate in the conservative form

\[
 \boxed{
 \sum_{0\le x\le X}
 |\mathcal E(x,h)|^2
 \ll Xh\log^2(2X)
 }
\tag{L-90419.2}
\]

uniformly for `1<=h<=X`. This follows from the standard Selberg/Saffari–Vaughan short-interval mean-square theorem; the discrete formulation is identical to the corresponding integral on unit cells when `h` is integral.

Reference: B. Saffari and R. C. Vaughan, *On the fractional parts of x/n and related sequences. II*, Ann. Inst. Fourier (Grenoble) **27** (1977), no. 2, 1–30. Only the upper bound (L-90419.2) is used.

## 2. A maximal short-interval consequence

Let

\[
 \mathcal M_H(x)
 =\max_{1\le h\le H}|\mathcal E(x,h)|.
\]

Binary decomposition of every interval length `h<=H` into at most

\[
 1+\lfloor\log_2H\rfloor
\]

dyadic intervals, followed by Cauchy–Schwarz and (L-90419.2) at each dyadic length, gives

\[
 \boxed{
 \sum_{0\le x\le X}
 \mathcal M_H(x)^2
 \ll XH\log^4(2X)
 }
\tag{L-90419.3}
\]

uniformly for `1<=H<=X`. The fourth logarithmic power is deliberately generous; the binary argument gives a slightly smaller power.

### Proof detail

For one fixed `h`, write its binary expansion and partition `(x,x+h]` consecutively into at most one interval of each dyadic length. Then

\[
 |\mathcal E(x,h)|^2
 \le L
 \sum_{r\le L}
 |\mathcal E(x+v_r,2^r)|^2,
 \qquad L\ll\log(2H),
\]

where each `v_r` is a partial sum of lower binary digits. For each `r`, the map `x -> x+v_r` has multiplicity one. Summing over `x`, then over `r`, and using (L-90419.2) gives (L-90419.3).

## 3. Maximal interval sums for the compact-Q4 coefficient

Retain

\[
 c_\circ(m)
 =\Lambda(m)
 -4\mathbf1_{4\mid m}\Lambda(m/4)
 +a_4(m),
\tag{L-90419.4}
\]

where

\[
 a_4(m)=3(\log4)
 \sum_{r\ge1}\mathbf1_{m=4^r}.
\]

Put

\[
 D_\circ(x,h)
 =\sum_{x<m\le x+h}c_\circ(m).
\tag{L-90419.5}
\]

Let

\[
 y=\left\lfloor\frac x4\right\rfloor,
 \qquad
 h'=\left\lfloor\frac{x+h}{4}\right\rfloor
     -\left\lfloor\frac x4\right\rfloor.
\]

Then exactly

\[
 \begin{aligned}
 D_\circ(x,h)
 ={}&\mathcal E(x,h)
 -4\mathcal E(y,h')\\
 &+[h-4h']
 +\sum_{x<m\le x+h}a_4(m).
 \end{aligned}
\tag{L-90419.6}

Here

\[
 |h-4h'|\le3,
 \qquad
 0\le h'\le h/4+1,
\]

and the four-adic interval contains at most `O(log(2X))` atoms. Applying (L-90419.3) to the first term, then to the quarter-scale term and using the four-to-one multiplicity of `x -> floor(x/4)`, yields

\[
 \boxed{
 \sum_{0\le x\le X}
 \max_{1\le h\le H}|D_\circ(x,h)|^2
 \ll XH\log^4(2X)
 }
\tag{L-90419.7}

for `1<=H<=X`. The atom and floor terms are absorbed by the displayed right side.

## 4. Triangular windows are sums of nested interval errors

For a standard Haar interval of half-length `ell`, the triangular functional of `L-90416` satisfies exactly

\[
 \boxed{
 T_{u,\ell}(c_\circ)
 =\sum_{r=0}^{\ell-1}
 D_\circ(u+r,2\ell-2r-1).
 }
\tag{L-90419.8}

Indeed, a coefficient at offset `t` occurs for exactly

\[
 \min(t,2\ell-t)
\]

values of `r`.

Cauchy–Schwarz gives

\[
 |T_{u,\ell}(c_\circ)|^2
 \le\ell
 \sum_{r=0}^{\ell-1}
 |D_\circ(u+r,2\ell-2r-1)|^2.
\tag{L-90419.9}

As `u` ranges over the standard bases `0,2ell,4ell,...`, the integers `u+r`, `0<=r<ell`, are pairwise distinct. Therefore (L-90419.7), with `H=2ell`, implies

\[
 \boxed{
 \sum_u|T_{u,\ell}(c_\circ)|^2
 \ll N\ell^2\log^4(2N).
 }
\tag{L-90419.10}

The same bound holds for the reflected triangular windows.

## 5. One complete Haar scale

By `L-90416`,

\[
 H_{u,\ell}
 =\frac{
 T_{u,\ell}(c_\circ)
 -T_{N-u-2\ell,\ell}(c_\circ)
 }{\sqrt{2\ell}}.
\]

Hence

\[
 \boxed{
 \sum_u|H_{u,\ell}|^2
 \ll N\ell\log^4(2N).
 }
\tag{L-90419.11}

No distinction between fine and coarse scale remains in this estimate.

## 6. Sum the complete nonconstant Haar tree

Sum (L-90419.11) over all dyadic half-lengths

\[
 1\le\ell\le N/2.
\]

Since

\[
 \sum_{\ell\text{ dyadic},\ell\le N/2}\ell<N,
\]

we obtain

\[
 \boxed{
 \sum_{u,\ell}|H_{u,\ell}|^2
 \ll N^2\log^4(2N).
 }
\tag{L-90419.12}

Haar Parseval and the corrected PIG normalization of `R-90411` give

\[
 \boxed{
 \frac1N\int_0^1|Q_{c_\circ,N}(\theta)|^2d\theta
 =\frac{|\overline R_N|^2}{N}
 +O(\log^4(2N)).
 }
\tag{L-90419.13}

Thus **every nonconstant spatial mode is already unconditionally at PIG scale**.

## 7. Exact final endpoint scalar

Equation (L-90419.13) proves that endpoint PIG is equivalent, up to an unconditional logarithmic term, to

\[
 \boxed{
 |\overline R_N|
 \ll\sqrt N\,\log^B(2N)
 }
\tag{L-90419.14}

for some fixed `B`.

By `L-90413`, `overline R_N` is the zero-safe mean prime-ramp scalar. By `L-90418`, it is also the inclusive uniform-Pascal current row

\[
 \overline R_N
 =\frac{N+1}{N}
   \sum_{d\le N}i_\circ(d)\beta_{N,d}
 +\frac1N C_\circ(N).
\tag{L-90419.15}

Therefore the formerly high-dimensional positive innovation theorem has collapsed to one scalar which is simultaneously:

```text
zeroth Fourier mode;
scaling/Haar coefficient;
zero-safe filtered-Chebyshev Riesz mean;
inclusive uniform-Pascal current row;
positive top-annulus source ramp.
```

## 8. Logical boundary

The theorem does **not** make the remaining scalar easy. Its Mellin transform retains every open-strip zeta zero, so (L-90419.14) is RH-strength.

Closed unconditionally, subject to review:

1. maximal compact-Q4 short-interval mean square;
2. all triangular-window square sums;
3. every nonconstant Haar scale, including the former coarse tree;
4. complete nonmean PIG energy `O(log^4 N)` after normalization;
5. reduction of endpoint PIG to the mean scalar alone.

Open:

1. the mean bound (L-90419.14);
2. deterministic PIG;
3. PR #371's repaired global PIG-to-pole adapter;
4. RH.
