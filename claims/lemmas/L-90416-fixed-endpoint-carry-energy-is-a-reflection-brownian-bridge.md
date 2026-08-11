# L-90416 — Fixed-endpoint carry energy is a reflection Brownian-bridge form

Claim ID: `L-90416`  
Title: After its single mean coordinate is removed, every symmetric carry row is exactly the Brownian-bridge energy of the reflection-antisymmetric prefix source  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: elementary finite summation; `L-90411/L-90703` for comparison only  
Scope: one fixed integer endpoint and any finite prefix source; no arithmetic estimate, PIG, or RH conclusion

## 1. Symmetric prefix row

Let `N>=3`, let `c(1),...,c(N)` be real or complex coefficients, and put

\[
 C(x)=\sum_{m\le x}c(m),\qquad C(0)=0.
\]

For a fixed scalar `kappa`, define the symmetric row

\[
 \boxed{
 Q_N(j)=C(N)-C(j)-C(N-j)-\kappa,
 \qquad 1\le j\le N-1.
 }
 \tag{L-90416.1}
\]

This includes the own compact-Q4 row of `T-90404/L-90703` after taking

\[
 c=c_\circ,\qquad \kappa=4\log4.
\]

Write

\[
 M=N-1.
\]

For each source atom define

\[
 k_m(j)=1-\mathbf1_{m\le j}-\mathbf1_{m\le N-j}.
 \tag{L-90416.2}
\]

Then

\[
 Q_N(j)=\sum_{m=1}^N c(m)k_m(j)-\kappa.
 \tag{L-90416.3}
\]

A direct count gives

\[
 \boxed{
 \frac1M\sum_{j=1}^{N-1}k_m(j)
 =\frac{2m-N-1}{N-1}.
 }
 \tag{L-90416.4}
\]

Consequently the exact row mean is

\[
 \boxed{
 \overline Q_N
 =\frac1M\sum_{m=1}^N(2m-N-1)c(m)-\kappa.
 }
 \tag{L-90416.5}
\]

The constant gauge enters only this one coordinate.

## 2. Nested central intervals

Put

\[
 L_m=|2m-N-1|,
 \qquad
 t_m=\frac{L_m}{M},
 \qquad
 s_m=\operatorname{sgn}(2m-N-1).
 \tag{L-90416.6}
\]

If `L_m>0`, the function `k_m` is `s_m` times the indicator of the centered interval of exactly `L_m` row positions. If `L_m=0`, its centered part is zero. Hence

\[
 k_m(j)-\frac{2m-N-1}{M}
 =s_m\,[\mathbf1_{j\in I_m}-t_m],
 \tag{L-90416.7}
\]

where the intervals `I_m` are nested and centered.

For two such atoms, nesting gives

\[
 \boxed{
 \frac1M\sum_{j=1}^{N-1}
 \left(k_m(j)-\frac{2m-N-1}{M}\right)
 \overline{
 \left(k_r(j)-\frac{2r-N-1}{M}\right)}
 =s_ms_r K_{\rm BB}(t_m,t_r),
 }
 \tag{L-90416.8}
\]

with the Brownian-bridge kernel

\[
 \boxed{
 K_{\rm BB}(u,v)=\min(u,v)-uv.
 }
 \tag{L-90416.9}
\]

No limiting or probabilistic argument is involved: this is an exact covariance identity for nested finite intervals.

## 3. Reflection compression

The involution

\[
 m\longmapsto N+1-m
\]

preserves `t_m` and reverses `s_m`. Therefore only the reflection-antisymmetric part of the source survives away from the mean.

For

\[
 1\le m\le\lfloor N/2\rfloor,
\]

define

\[
 \boxed{
 d_N(m)=c(N+1-m)-c(m),
 \qquad
 \tau_m=\frac{N+1-2m}{N-1}.
 }
 \tag{L-90416.10}
\]

Then the complete centered energy is

\[
 \boxed{
 \frac1{N-1}\sum_{j=1}^{N-1}
 |Q_N(j)-\overline Q_N|^2
 =\sum_{m,r\le\lfloor N/2\rfloor}
 d_N(m)\overline{d_N(r)}
 K_{\rm BB}(\tau_m,\tau_r).
 }
 \tag{L-90416.11}
\]

Thus the fixed-endpoint row has the exact orthogonal split

```text
one symmetric mean coordinate
+
Brownian-bridge energy of c(N+1-m)-c(m).
```

For the compact-Q4 source this means that the nonconstant PIG mass depends only on reflected differences of the explicit prime-power coefficient `c_circ`; all reflection-symmetric source mass is confined to `Qbar_N`.

## 4. Green/tail representation

The Brownian kernel has the elementary covariance representation

\[
 K_{\rm BB}(u,v)
 =\int_0^1
 [\mathbf1_{x\le u}-u]
 [\mathbf1_{x\le v}-v]\,dx.
 \tag{L-90416.12}
\]

Hence (L-90416.11) is equivalently

\[
 \boxed{
 \frac1{N-1}\sum_{j=1}^{N-1}
 |Q_N(j)-\overline Q_N|^2
 =\int_0^1
 \left|
 \sum_{\tau_m\ge x}d_N(m)
 -\sum_m\tau_m d_N(m)
 \right|^2dx.
 }
 \tag{L-90416.13}
\]

The tail sum has the exact arithmetic form

\[
 \sum_{m\le R}d_N(m)
 =[C(N)-C(N-R)]-C(R).
 \tag{L-90416.14}
\]

Thus the nonconstant PIG energy is a centered Selberg-type mean square of symmetric short-interval source discrepancies.

## 5. Relation to the Fourier normal form

`K_BB` is the Green kernel of `-d^2/dx^2` with Dirichlet endpoints. Its sine eigenvalues are `1/(pi^2 k^2)`. Therefore (L-90416.11) is the radial/reflection version of the inverse-circle-Laplacian formula in `L-90411` and the cosine-antiderivative formula in `L-90703`.

The new content is the exact state compression:

\[
 c(1),\ldots,c(N)
 \quad\longmapsto\quad
 \overline Q_N,
 \ d_N(1),\ldots,d_N(\lfloor N/2\rfloor).
\]

The apparent full source packet contains no other dynamic coordinate.

## 6. Sharp scope

The largest eigenvalue of the sampled Brownian kernel is of order `N`. Therefore the generic estimate obtained from

\[
 \sum_m|d_N(m)|^2\ll N\log N
\]

still loses one factor of `N`; this theorem alone does not prove PIG. It shows exactly that the surviving gain must be a reflection-sensitive arithmetic estimate, not a generic carry or Fourier norm bound.

## 7. Proof boundary

Closed exactly here:

1. the row mean formula;
2. nested-interval covariance;
3. reflection compression to `d_N(m)`;
4. exact Brownian-bridge quadratic form;
5. exact Green/tail representation;
6. equivalence with the prior inverse-Laplacian coordinate.

Open:

1. a critical-scale estimate for the Q4 reflection differences;
2. transfer to the exact global block measure after the PR #371 repairs;
3. PIG and RH.
