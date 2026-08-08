# L-32308 — Exact annular physical-to-carry isometry for the critical-null source

Claim ID: `L-32308`  
Title: The critical-null compact physical window is exactly one weighted carry split on an oversupport row, with the same RH-sensitive coefficient sequence on both sides  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: `L-32302`; the carry/floor algebra used in PR #268 `L-26802`  
Scope: exact annular source geometry; no reserve or RH conclusion

## 1. Compact floor potential

Let

\[
\omega_\dagger
=(\varepsilon-\sqrt2\delta_2)*\omega_2
\]

be the source of `L-32302`. Since

\[
\mathbf1*\mu=\varepsilon,
\]

one has

\[
\boxed{
\mathbf1*\omega_\dagger
=\varepsilon
-\left({3\over2}+\sqrt2\right)\delta_2
+\left({1\over2}+{3\sqrt2\over2}\right)\delta_4
-{\sqrt2\over2}\delta_8.
}
\tag{L-32308.1}
\]

For integers `m,r>=1`, define

\[
\boxed{
 g_m(r)=
 \mathbf1_{m\le r<2m}
 -\left({1\over2}+\sqrt2\right)\mathbf1_{2m\le r<4m}
 +{\sqrt2\over2}\mathbf1_{4m\le r<8m}.
}
\tag{L-32308.2}
\]

Finite divisor reindexing gives the exact floor formula

\[
\boxed{
 g_m(r)
 =\sum_{k\le r/m}\omega_\dagger(k)
 \left\lfloor{r\over mk}\right\rfloor.
}
\tag{L-32308.3}
\]

Thus the complete reciprocal-zeta source has a literal factor-eight compact floor image.

## 2. Physical step signal

Define the real compact window

\[
\boxed{
 h_\dagger(t)=e^{-t/2}
 \begin{cases}
 1,&0\le t<\log2,\\
 -{1\over2}-\sqrt2,&\log2\le t<\log4,\\
 {\sqrt2\over2},&\log4\le t<\log8,\\
 0,&\text{otherwise}.
 \end{cases}
}
\tag{L-32308.4}
\]

For any finitely supported coefficient sequence `x`, put

\[
\alpha_x=\sum_m{x_m\over\sqrt m}\delta_{\log m},
\qquad
Q_x=h_\dagger*\alpha_x,
\]

and

\[
F_x(r)=\sum_mx_mg_m(r).
\]

For almost every `t` with

\[
\log r\le t<\log(r+1),
\]

one has exactly

\[
\boxed{
Q_x(t)=e^{-t/2}F_x(r).
}
\tag{L-32308.5}
\]

Consequently

\[
\boxed{
\|Q_x\|_{L^2(\mathbb R)}^2
=\sum_{r\ge1}{|F_x(r)|^2\over r(r+1)}.
}
\tag{L-32308.6}
\]

No approximation or continuum limit enters.

## 3. Carry split of the same potential

For a carry row `n`, set

\[
(\mathcal S_nF)(j)=F(n)-F(j)-F(n-j).
\]

Equation (L-32308.3) gives

\[
\boxed{
(\mathcal S_nF_x)(j)
=\sum_{q\le n}(\omega_\dagger*x)(q)\chi_{n,q}(j).
}
\tag{L-32308.7}
\]

Thus physical convolution and carry splitting act on the **same coefficient sequence** `x`; the carry coefficient is simply `omega_dagger*x`.

For the RH-sensitive choice

\[
\boxed{x=\Lambda_\dagger,}
\tag{L-32308.8}
\]

where `Lambda_dagger` is the positive generalized-prime sequence of `L-32302`, the carry feature is

\[
\boxed{
W_\dagger=\omega_\dagger*\Lambda_\dagger.
}
\tag{L-32308.9}
\]

The physical transform contains the logarithmic derivative of the positive inverse `A_dagger`; every off-line zeta zero remains a pole because the compact local factor `P_dagger(2^-s)` has no zero in the open critical strip.

## 4. Exact annular weighted isometry

Assume

\[
x_m=0\qquad\text{unless}\qquad M\le m<2M.
\]

Because `g_m` is supported on `[m,8m)`,

\[
\operatorname{supp}F_x\subset[M,16M).
\]

Choose

\[
U=16M,
\qquad
N=2U-1=32M-1.
\]

For `1<=j<U`, both `F_x(N)` and `F_x(N-j)` vanish, so

\[
(\mathcal S_NF_x)(j)=-F_x(j).
\]

Equation (L-32308.6) therefore becomes the exact congruence

\[
\boxed{
\|Q_x\|_2^2
=\sum_{j=1}^{16M-1}
 {|(\mathcal S_NF_x)(j)|^2\over j(j+1)}.
}
\tag{L-32308.10}
\]

In particular the annular RH-sensitive physical Gram for `x=Lambda_dagger` is exactly the weighted carry Gram of `W_dagger` on one explicit oversupport row.

## 5. Why this matters

The earlier factor-five programme had to distinguish:

```text
RH-sensitive physical source W;
reserved generalized-prime carry source P.
```

That source distinction still exists for any inverse-source recurrence, but there is **no unidentified physical-to-carry operator** for the critical-null source: equation (L-32308.10) is exact on the RH-sensitive coefficient vector itself.

Any remaining proof obligation is therefore an arithmetic inequality inside one declared weighted carry Hilbert space, not a metric-identification problem.

## 6. Proof boundary

Closed exactly:

- compact floor potential;
- physical step representation;
- weighted `L2` identity;
- exact additive carry split;
- RH-sensitive source specialization;
- common annular oversupport isometry.

Open:

- a strict reserve or upper recurrence for the RH-sensitive feature `W_dagger`;
- lower-scale source-change control;
- RH.
