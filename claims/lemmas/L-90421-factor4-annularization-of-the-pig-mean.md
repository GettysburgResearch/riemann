# L-90421 — The PIG mean has an exact zero-safe factor-four annularization

Claim ID: `L-90421`  
Title: A second dilation difference removes the complete lower quarter of the compact-Q4 mean, producing a piecewise-linear scalar supported on `[X/4,X]` whose Mellin multiplier has no zero in the right half-plane  
Status: **PROPOSED COMPLETE EXACT RH-EQUIVALENT ANNULAR REDUCTION — INDEPENDENT REVIEW REQUIRED; RH UNPROVED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `T-90420`; elementary dilation algebra  
Scope: one scalar annulus; no unconditional sign or critical-growth estimate

## 1. Definition

Extend `M_circ(X)` by zero for `0<X<1`. Define

\[
 \boxed{
 \mathcal A_4(X)
 =2M_\circ(X)-3M_\circ(X/2)+M_\circ(X/4).
 }
\tag{L-90421.1}

The coefficient polynomial is

\[
 P(y)=2-3y+y^2=(1-y)(2-y).
\tag{L-90421.2}

## 2. Exact annular support

For a coefficient `c(m)`, the kernel of `M(X/2^r)` is

\[
 \left(\frac{2^{r+1}m}{X}-1\right)
 \mathbf1_{m\le X/2^r}.
\]

If `m<=X/4`, the combined coefficient in (L-90421.1) is

\[
 2\left(\frac{2m}{X}-1\right)
 -3\left(\frac{4m}{X}-1\right)
 +\left(\frac{8m}{X}-1\right)=0.
\]

Therefore

\[
 \boxed{
 \begin{aligned}
 \mathcal A_4(X)
 ={}&\sum_{X/4<m\le X/2}
 c_\circ(m)\left(1-\frac{8m}{X}\right)\\
 &+\sum_{X/2<m\le X}
 c_\circ(m)\left(\frac{4m}{X}-2\right).
 \end{aligned}
 }
\tag{L-90421.3}

The scalar is supported exactly on the fixed annulus

\[
 \boxed{X/4<m\le X.}
\tag{L-90421.4}

No tail or asymptotic truncation is involved.

## 3. Mellin multiplier and zero safety

Dilation by `1/2` multiplies the Mellin transform by `2^{-z}`. Hence

\[
 \boxed{
 \widehat{\mathcal A_4}(z)
 =(2-3\,2^{-z}+4^{-z})\widehat M_\circ(z).
 }
\tag{L-90421.5}

The new multiplier factors as

\[
 \boxed{
 2-3\,2^{-z}+4^{-z}
 =(1-2^{-z})(2-2^{-z}).
 }
\tag{L-90421.6}

Its zeros satisfy either

\[
 2^{-z}=1
 \quad\text{or}\quad
 2^{-z}=2,
\]

and therefore lie on

\[
 \Re z=0
 \quad\text{or}\quad
 \Re z=-1.
\]

Thus the annularization cannot cancel any nontrivial zeta zero, and in fact is zero-safe throughout

\[
 \Re z>0.
\tag{L-90421.7}

## 4. RH-equivalent critical growth

Under RH, `T-90420` gives

\[
 M_\circ(X)\ll\sqrt X\log^2(2X),
\]

so

\[
 \boxed{
 \mathcal A_4(X)
 \ll\sqrt X\log^2(2X).
 }
\tag{L-90421.8}

Conversely, suppose for every `epsilon>0`,

\[
 \mathcal A_4(X)=O_\epsilon(X^{1/2+\epsilon}).
\tag{L-90421.9}

Then its Mellin transform is holomorphic for `Re z>1/2`. Equations (L-90421.5)--(L-90421.7) and the zero-safe transform of `T-90420` exclude every zeta zero in that half-plane. Hence RH follows.

Therefore

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal A_4(X)=O_\epsilon(X^{1/2+\epsilon})
 \text{ for every }\epsilon>0.
 }
\tag{L-90421.10}

## 5. Interpretation

The sole endpoint PIG obstruction can now be presented in a genuinely compact arithmetic coordinate:

```text
one fixed annulus [X/4,X];
one piecewise-linear kernel;
ordinary prime-power coefficient c_circ;
no open-strip multiplier zero.
```

This factor-four annularization is shorter than the phase-blind factor-64 sign criterion of PR #352 because the present consumer asks for critical growth, not an eventual sign uniform over every critical phase.

The theorem does not make the annular estimate elementary. The annular scalar still retains every off-line zeta pole and is RH-equivalent.

## 6. Proof boundary

Closed exactly:

1. factor-four dilation polynomial;
2. complete cancellation below `X/4`;
3. explicit two-band kernel;
4. Mellin factorization;
5. zero safety in `Re z>0`;
6. critical-growth equivalence to RH.

Open:

1. an unconditional critical-growth estimate for `A_4(X)`;
2. RH.
