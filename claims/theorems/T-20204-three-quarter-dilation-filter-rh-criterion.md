# T-20204 — The canonical three-quarter dilation filter

Claim ID: `T-20204`  
Title: One explicit two-dilation Gram portfolio is RH-equivalent and confines all negative prime weight to `q<n^(3/(2R))`  
Status: `PROPOSED — COMPLETE CONSEQUENCE OF T-20203/L-20205; COFINAL SIGN OPEN`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20203`; `L-20204`; `L-20205`  
Scope: every fixed integer `R>=4`

## 1. Exact filter

Fix an integer `R>=4` and put

\[
 c_R=(R-1)(R-3).
\]

Define

\[
\boxed{
 \mathcal E_R(t)=c_R\mathcal D_2(t)+\mathcal D_R(t).}
\tag{1}
\]

Equivalently,

\[
\boxed{
\mathcal E_R(t)
=(5R^2-16R+12)\Psi(t)
-(R-1)(R-3)\Psi(2t)
-\Psi(Rt).}
\tag{2}
\]

It is a positive integer-weighted Gram portfolio of the four-tap vectors in
`L-20204`.

Under RH, `E_R(t)>=0` for every real `t`.

## 2. Pole-descent converse

The Laplace bracket of (1) is

\[
\begin{aligned}
&2c_R F\!\left({1\over2}-{iz\over2}\right)
 +R F\!\left({1\over2}-{iz\over R}\right)\\
&\qquad-\left(4c_R+R^2\right)
 F\!\left({1\over2}-iz\right).
\end{aligned}
\tag{3}
\]

At an off-line parent zero of multiplicity `m`, holomorphic cancellation requires

\[
\boxed{
 (4c_R+R^2)m
 =4c_Rm_2+R^2m_R,}
\tag{4}
\]

where `m_2` and `m_R` are the multiplicities of the descendants at horizontal
scales `1/2` and `1/R`. The parent multiplicity is therefore a positive weighted
average of the two descendant multiplicities. At least one descendant has
multiplicity at least `m`; iterating gives a zero accumulation at `1/2`.

Thus the Landau/pole-descent argument of `T-20203` applies without modification.

## 3. Critical mesh and exact prime threshold

Use

\[
 t={2\over R}\log n,
 \qquad
 u={\log q\over t}.
\]

For `0<=u<=1`, the prime weights of `D_2` and `D_R` are respectively

\[
 3u-2
\]

and

\[
 (R-1)((R+1)u-R).
\]

Their weighted sum factors exactly:

\[
\begin{aligned}
&c_R(3u-2)+(R-1)((R+1)u-R)\\
&\qquad=(R-1)(R-2)(4u-3).
\end{aligned}
\tag{5}
\]

Every component is nonnegative for `u>=1`. Hence

\[
\boxed{
\text{the complete mixture prime weight is negative exactly for }
 u<{3\over4}.}
\tag{6}
\]

Since `e^t=n^(2/R)`, this is

\[
\boxed{
 q<n^{3/(2R)}.}
\tag{7}
\]

Every prime power from `n^(3/(2R))` through the complete cutoff `n^2` has
nonnegative weight.

## 4. Global criterion

The derivative of `E_R` has exponential order `R/2`, and the critical mesh has
spacing `O(1/n)`. Therefore `T-20203` yields

\[
\boxed{
 RH
 \iff
 \mathcal E_R\!\left({2\over R}\log n\right)\ge0
 \text{ eventually}.}
\tag{8}
\]

Equivalently,

\[
\boxed{
 RH
 \iff
 \left(-\mathcal E_R\!\left({2\over R}\log n\right)\right)_+
 =n^{o(1)}.}
\tag{9}
\]

This is one fixed three-scale scalar with integer coefficients.

## 5. Preferred explicit instance

Take `R=16`. Then

\[
 c_{16}=195
\]

and

\[
\boxed{
 \mathcal E_{16}(t)
 =1036\Psi(t)-195\Psi(2t)-\Psi(16t).}
\tag{10}
\]

The pole-cancellation multiplicity relation is

\[
 1036m=780m_2+256m_{16},
\]

and the negative prime channel is exactly

\[
\boxed{q<n^{3/32}.}
\tag{11}
\]

The complete prime manifest remains `q<=n^2`. This is the recommended first
symbolic and directed production target.

Other simple choices are

```text
R=8:   c_R=35,   adverse prefix n^(3/16)
R=32:  c_R=899,  adverse prefix n^(3/64)
R=64:  c_R=3843, adverse prefix n^(3/128)
```

## 6. Why the filter is useful

Compared with the single `R`-defect, whose adverse exponent is `2/(R+1)`, the
three-quarter filter has exponent `3/(2R)`. It also has:

- exact integer coefficients;
- only three screw scales `1,2,R`;
- an explicit positive FIR Gram portfolio;
- a positive-mixture pole-descent proof;
- one duplicate-free square-cutoff prime stream;
- a termwise-positive Lerch combination inherited from the two components.

It is therefore a substantially cleaner target for the prime-polygon and
Selberg-pair attacks than an arbitrary optimized mixture.

## 7. Proof boundary

- The coefficient factorization and threshold are exact.
- The cofinal sign/subpower estimate is not proved.
- The large positive prime band still cancels the polar channel to order-one
  accuracy, so a phase-blind PNT estimate remains insufficient.
- Finite positive values do not imply (8) or RH.
