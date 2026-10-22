# L-32410 — Same-scale parity current synthesis uses less than two fifths of the analysis reserve

Claim ID: `L-32410`  
Title: After the final two-contact factor is included, the exact finite Bézout synthesis of the parity currents has a five-delay critical block charge strictly below `2/5` of the fixed parity-frame analysis reserve  
Status: **PROPOSED COMPLETE EXACT FINITE-FILTER LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-09  
Dependencies: PR #263 `L-26205/L-26206`; PR #334 `L-32402/L-32403`; `L-32409`  
Scope: same-scale current synthesis only; delayed derivative gauge remains a separate state

## 1. Current synthesis coefficients

Retain the positive Bézout polynomial

\[
U(z)=\sum_{j=0}^3u_jz^j
\]

with

\[
U(z)p(z)+U(-z)p(-z)=1.
\]

For the reconstructed inverse-zeta current the same-scale synthesis carries the final two-contact factor `1-z`. Put

\[
\boxed{
V_+(z)=(1-z)U(z),\qquad
V_-(z)=(1-z)U(-z).
}
\tag{L-32410.1}

Writing

\[
V_\pm(z)=\sum_{j=0}^4v_{\pm,j}z^j,
\]

direct expansion gives

\[
\begin{aligned}
v_+={}&\left(
 {1\over2},
 -{25\over6}+{7\sqrt2\over2},
 {14\over3}-{10\sqrt2\over3},
 {11\over3}-{19\sqrt2\over6},
 -{14\over3}+3\sqrt2
\right),\\
v_-={}&\left(
 {1\over2},
 {19\over6}-{7\sqrt2\over2},
 -{8\over3}+{11\sqrt2\over3},
 -{17\over3}+{17\sqrt2\over6},
 {14\over3}-3\sqrt2
\right).
\end{aligned}
\tag{L-32410.2}

All delays are exact multiples of `log 2`.

## 2. Critical block charge

On a vertical line `sigma>=1/2` put

\[
r=2^{-\sigma}\le2^{-1/2}.
\]

In physical logarithmic coordinates, multiplication by `z^j` is translation by `j log 2` with amplitude `r^j`. Therefore the Cauchy charge of the complete two-channel same-scale current synthesis is

\[
 q_V(r)
 =\sum_{j=0}^4
 \left(v_{+,j}^2+v_{-,j}^2\right)r^{2j}.
\tag{L-32410.3}

Every coefficient in this polynomial in `r^2` is nonnegative, so the maximum on the closed critical strip occurs at `r^2=1/2`. Exact simplification gives

\[
\boxed{
q_V(2^{-1/2})
={587\over8}-{195\sqrt2\over4}
=4.4320888343\ldots
}
\tag{L-32410.4}

(the decimal is orientation only).

## 3. Comparison with the fixed analysis reserve

`L-26205/L-32402` prove on the same critical annulus

\[
|p(z)|^2+|p(-z)|^2\ge{45\over4}.
\]

Hence the normalized same-scale synthesis charge is at most

\[
\boxed{
\rho_V
={q_V(2^{-1/2})\over45/4}
={587\over90}-{13\sqrt2\over3}.
}
\tag{L-32410.5}

Moreover

\[
\boxed{
{2\over5}-\rho_V
={390\sqrt2-551\over90}>0.
}
\tag{L-32410.6}

Indeed

\[
2\cdot390^2=304200>551^2=303601.
\]

Thus

\[
\boxed{\rho_V<{2\over5}.}
\tag{L-32410.7}

This bound is exact and uniform for every `sigma>=1/2` in the declared annulus.

## 4. Finite-block form

Let `I_m=[m log2,(m+1)log2]` and let

\[
E_m=\int_{I_m}(|q_+(x)|^2+|q_-(x)|^2)\,dx.
\]

The same-scale reconstructed current

\[
q_{\rm syn}(x)
=\sum_{j=0}^4r^j
[v_{+,j}q_+(x-j\log2)+v_{-,j}q_-(x-j\log2)]
\]

satisfies

\[
\boxed{
\int_{I_m}|q_{\rm syn}(x)|^2dx
\le q_V(r)\sum_{j=0}^4E_{m-j}.
}
\tag{L-32410.8}

There is no fractional-block collar.

Equation (L-32410.7) says that the **same-scale finite synthesis itself is strictly below the fixed source-frame reserve**. This is a filter-budget statement; it does not assert that the entire source-convolved reflected current is bounded by the analysis reserve.

## 5. Composition with the derivative-gauge theorem

`L-32409` gives the exact current identity

\[
q_0=q_{\rm syn}+\mathcal G,
\]

where every term of `G` is delayed by at least one `log 2` block:

```text
one odd-core state at delay 1;
reconstructed Mobius boundary at delays 2,4,6.
```

Therefore there is no unaccounted **current-scale** term after exact parity synthesis:

```text
same scale:
    finite current synthesis, normalized charge <2/5;

strictly earlier blocks:
    complete derivative gauge.
```

This is the source-compatible scale separation needed by a future Hermitian recurrence.

## 6. Proof boundary

Closed exactly here:

1. the five-delay current synthesis coefficients;
2. their critical weighted square budget;
3. the strict normalized bound `<2/5`;
4. exact dyadic block alignment;
5. separation of all remaining current terms into the delayed gauge of `L-32409`.

Open:

1. source-convolved reflected accounting of the delayed gauge without double spending the paired Selberg reserve;
2. the resulting coefficient-one global recurrence;
3. RH.
