# L-90417 — The compact-Q4 innovation is an exact radix-four difference on the Haar tree

Claim ID: `L-90417`  
Title: On every aligned Haar interval, the Q4 compact innovation coefficient is the ordinary-prime triangular coefficient minus eight times its radix-four predecessor, plus a harmless finite four-adic atom  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM + SHARP COARSE-HAAR REDUCTION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90416`; the exact compact coefficient formula of `L-90412`  
Scope: aligned endpoints `N=4^M`; no estimate for the surviving coarse prime square function and no PIG or RH conclusion

## 1. The scale-four coefficient operator

For a sequence `a`, define

\[
 (D_4a)(m)=4\mathbf1_{4\mid m}a(m/4).
\tag{L-90417.1}
\]

The hard prime part of the compact-Q4 prefix coefficient is

\[
 \boxed{c_{\rm pr}=\Lambda-D_4\Lambda.}
\tag{L-90417.2}
\]

The remaining local atom is

\[
 a_4(m)=3(\log4)\sum_{r\ge1}\mathbf1_{m=4^r},
\tag{L-90417.3}
\]

so

\[
 c_\circ=c_{\rm pr}+a_4.
\tag{L-90417.4}
\]

## 2. Exact triangular scaling

Let `N=4^M`. On a standard Haar interval with dyadic half-length `ell>=4`, the base point `u` and reflected base point `N-u-2ell` are divisible by four.

For the triangular functional of `L-90416`, direct substitution `t=4r` gives

\[
 \boxed{
 T_{u,\ell}(D_4a)
 =16T_{u/4,\ell/4}(a).
 }
\tag{L-90417.5}
\]

Indeed,

\[
 w_\ell(4r)=4w_{\ell/4}(r),
\]

and the source coefficient itself contributes the second factor four.

Applying the same identity to the reflected interval gives the exact unnormalized Haar relation

\[
 \boxed{
 A_{D_4a,N}(u,\ell)
 =16A_{a,N/4}(u/4,\ell/4),
 }
\tag{L-90417.6}
\]

where

\[
 A_{c,N}(u,\ell)=\sqrt{2\ell}\,H_{c,N}(u,\ell).
\]

Because

\[
 \sqrt{2(\ell/4)}=\frac12\sqrt{2\ell},
\]

one obtains the normalized formula

\[
 \boxed{
 H_{D_4a,N}(u,\ell)
 =8H_{a,N/4}(u/4,\ell/4).
 }
\tag{L-90417.7}
\]

## 3. Exact Q4 Haar recurrence

Equations (L-90417.2), (L-90417.4), and (L-90417.7) give, for every standard Haar interval with `ell>=4`,

\[
 \boxed{
 \begin{aligned}
 H_{c_\circ,N}(u,\ell)
 ={}&H_{\Lambda,N}(u,\ell)\\
 &-8H_{\Lambda,N/4}(u/4,\ell/4)
 +H_{a_4,N}(u,\ell).
 \end{aligned}
 }
\tag{L-90417.8}
\]

Thus the compact innovation is not merely analogous to a wavelet. It is an exact radix-four difference of the same reflected triangular prime statistic on adjacent scales.

The dyadic Haar tree splits into two independent radix-four scale chains according to the parity of `log_2 ell`. No additional source state is created as the scale descends.

## 4. The four-adic atom is harmless

The atom prefix contains only

\[
 O(1+\log N)
\]

jumps. Hence its bridge values satisfy

\[
 \boxed{
 \|Q_{a_4,N}\|_{L^\infty(0,1)}
 \ll1+\log N
 }
\tag{L-90417.9}
\]

and therefore

\[
 \boxed{
 \int_0^1|Q_{a_4,N}(\theta)|^2d\theta
 \ll(1+\log N)^2.
 }
\tag{L-90417.10}
\]

It may be placed entirely in the polynomial forcing ledger. It cannot carry a supercritical zero mode.

## 5. Exact coarse-Haar form of the remaining theorem

Let

\[
 \mathcal H_{>\sqrt N}(c_\circ)
 =\sum_{\substack{\ell>\sqrt N\\\ell\text{ dyadic}}}
   \sum_u|H_{c_\circ,N}(u,\ell)|^2.
\tag{L-90417.11}
\]

By `L-90416`, the complete position energy satisfies

\[
 \boxed{
 \begin{aligned}
 \int_0^1|Q_{c_\circ,N}|^2
 ={}&|\overline R_N|^2
 +\frac1N\mathcal H_{>\sqrt N}(c_\circ)\\
 &+O(\log N)
 \end{aligned}
 }
\tag{L-90417.12}
\]

in PIG-normalized units, with the convention that the displayed `O(log N)` is the fine-tree contribution after division by `N`.

Therefore a sufficient and, modulo the already-proved fine bound, equivalent endpoint theorem is

\[
 \boxed{
 |\overline R_N|^2
 +\frac1N\mathcal H_{>\sqrt N}(c_\circ)
 \ll\log^B N.
 }
\tag{L-90417.13}
\]

Using (L-90416.8), the coarse term is explicitly

\[
 \boxed{
 \sum_{\ell>\sqrt N}\sum_u
 \frac{
 |T_{u,\ell}(c_\circ)
  -T_{N-u-2\ell,\ell}(c_\circ)|^2
 }{2\ell N}.
 }
\tag{L-90417.14}
\]

There are fewer than `sqrt(N)` summands. Every summand is a difference of two local triangular prime windows of equal width and is linked to its radix-four predecessor by (L-90417.8).

## 6. Relation to the Fourier major-mode gate

The Fourier reduction of `L-90411`--`L-90415` leaves

```text
one zero frequency
+ O(sqrt(N)) low additive frequencies.
```

The present theorem leaves

```text
one scaling coefficient
+ fewer than sqrt(N) coarse local Haar coefficients.
```

These are two orthonormal descriptions of the same surviving low-complexity subspace. The Haar coordinate has two advantages:

1. every coefficient is a local reflected triangular prime sum;
2. the Q4 scale difference is exact and state-preserving by (L-90417.8).

It does not make the remaining estimate sub-RH. A power mode with real exponent greater than `1/2` necessarily appears in the coarse tree, consistent with `R-90406`.

## 7. Proof boundary

Closed exactly here:

1. scale-four action on triangular windows;
2. normalized factor-eight Haar recurrence;
3. decomposition of the compact innovation into an ordinary-prime scale difference plus a finite atom;
4. two-chain state structure on the dyadic Haar tree;
5. polynomial four-adic atom energy;
6. exact coarse-Haar formulation of the remaining endpoint PIG theorem.

Open:

1. the coarse reflected triangular-prime square-function bound;
2. the mean/scaling coefficient;
3. deterministic PIG;
4. the repaired global pole adapter;
5. RH.
