# L-28005 — Four-channel binary–ternary parity frame

Claim ID: `L-28005`  
Title: The critical binary–ternary source has a closed-strip four-channel frame, coefficientwise positive summed Selberg forcing, and a finite Bézout reconstruction of the reciprocal-zeta source  
Status: **PROPOSED COMPLETE EXACT SOURCE THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-28004`; finite polynomial Bézout algebra

## 1. Four completely multiplicative twists

For `epsilon,eta in {+1,-1}`, put

\[
\chi_{\epsilon,\eta}(n)
=\epsilon^{v_2(n)}\eta^{v_3(n)}.
\tag{L-28005.1}
\]

Twist the critical source and every associated coefficient sequence:

\[
\sigma_{\epsilon,\eta}
=\chi_{\epsilon,\eta}\sigma_{2,3},
\qquad
a_{\epsilon,\eta}
=\chi_{\epsilon,\eta}a_\sigma,
\]

\[
\Lambda_{\epsilon,\eta}
=\chi_{\epsilon,\eta}\Lambda_\sigma,
\qquad
C_{\epsilon,\eta}
=\chi_{\epsilon,\eta}C_{+,+}.
\tag{L-28005.2}
\]

Because the twists are completely multiplicative, they commute with Dirichlet
convolution and multiplication by `log n`.  Hence

\[
\boxed{
C_{\epsilon,\eta}
=\sigma_{\epsilon,\eta}
*(a_{\epsilon,\eta}\log^2)
=\Lambda_{\epsilon,\eta}\log
+\Lambda_{\epsilon,\eta}*\Lambda_{\epsilon,\eta}.}
\tag{L-28005.3}
\]

## 2. Local source polynomials

Let

\[
p_p(z)=(1-z)^2(1-\sqrt p\,z)
\qquad(p=2,3)
\tag{L-28005.4}
\]

and

\[
\mathcal O_6(s)=\prod_{p\ne2,3}(1-p^{-s}).
\]

Then

\[
\boxed{
\Sigma_{\epsilon,\eta}(s)
=p_2(\epsilon 2^{-s})
 p_3(\eta 3^{-s})
 \mathcal O_6(s).}
\tag{L-28005.5}
\]

Every channel has the same nontrivial zeta zeros.  Its local extra factors have
zeros only on boundary lines or outside the open right critical half-strip.

## 3. Closed-strip frame reserve

For a complex number `z` with `|z|<=1/sqrt(p)`,

\[
\begin{aligned}
|p_p(z)|^2+|p_p(-z)|^2
&\ge
(1-|z|)^4
\left(
|1-\sqrt p\,z|^2
+|1+\sqrt p\,z|^2
\right)\\
&\ge2(1-p^{-1/2})^4.
\end{aligned}
\tag{L-28005.6}
\]

Therefore, throughout

\[
\frac12\le\Re s\le1,
\]

\[
\boxed{
\sum_{\epsilon,\eta=\pm1}
|\Sigma_{\epsilon,\eta}(s)|^2
\ge
4(1-2^{-1/2})^4(1-3^{-1/2})^4
|\mathcal O_6(s)|^2.}
\tag{L-28005.7}
\]

Since

\[
\frac1{\zeta(s)}
=(1-2^{-s})(1-3^{-s})\mathcal O_6(s),
\]

one obtains the explicit comparison

\[
\boxed{
\sum_{\epsilon,\eta}|\Sigma_{\epsilon,\eta}(s)|^2
\ge\kappa_{2,3}
\left|\frac1{\zeta(s)}\right|^2,}
\tag{L-28005.8}
\]

where

\[
\kappa_{2,3}
=
\frac{4(1-2^{-1/2})^4(1-3^{-1/2})^4}
{(1+2^{-1/2})^2(1+3^{-1/2})^2}>0.
\tag{L-28005.9}
\]

A reverse comparison holds with another absolute constant.  Thus the four
channels are uniformly equivalent to the reciprocal-zeta source on the entire
closed critical strip.

## 4. Coefficientwise positive summed forcing

By `L-28004`, the untwisted forcing satisfies

\[
C_{+,+}(n)\ge0.
\]

Summing (L-28005.2) over the four twists gives

\[
\boxed{
\sum_{\epsilon,\eta}C_{\epsilon,\eta}(n)
=
\bigl(1+(-1)^{v_2(n)}\bigr)
\bigl(1+(-1)^{v_3(n)}\bigr)
C_{+,+}(n)
\ge0.}
\tag{L-28005.10}
\]

The sum vanishes unless both `v_2(n)` and `v_3(n)` are even, and equals
`4C_(+,+)(n)` otherwise.

Applying the correct independent-frequency reflected identity separately to all
four channels and adding therefore gives a genuine coefficientwise positive
summed Selberg forcing.  No channel is estimated before the sum is formed.

## 5. Exact parity orthogonalization

Let `Z_(epsilon,eta)` be any four physical fields formed with the same real
window and the four sources.  Define the four parity components

\[
Z_{a,b}
=\frac14
\sum_{\epsilon,\eta=\pm1}
\epsilon^a\eta^bZ_{\epsilon,\eta},
\qquad a,b\in\{0,1\}.
\tag{L-28005.11}
\]

Then `Z_(a,b)` contains exactly the source coefficients satisfying

\[
v_2(n)\equiv a\pmod2,
\qquad
v_3(n)\equiv b\pmod2,
\]

and the Hadamard identity gives

\[
\boxed{
\sum_{\epsilon,\eta}
\|Z_{\epsilon,\eta}\|_2^2
=4\sum_{a,b\in\{0,1\}}
\|Z_{a,b}\|_2^2.}
\tag{L-28005.12}
\]

All cross terms between distinct two-prime parity sectors disappear, while every
odd-prime Möbius sign remains.

## 6. One-variable Bézout identity

For `r=sqrt(p)`, set

\[
\begin{aligned}
U_{p,+}(z)
={}&\frac12
+\frac{4r^2+4r+1}{4(r+1)^2}z
+\frac{r(2r+1)}{4(r+1)^2}z^2,\\
U_{p,-}(z)
={}&\frac12
-\frac{4r^2+4r+1}{4(r+1)^2}z
+\frac{r(2r+1)}{4(r+1)^2}z^2.
\end{aligned}
\tag{L-28005.13}
\]

Direct polynomial multiplication gives

\[
\boxed{
U_{p,+}(z)p_p(z)
+U_{p,-}(z)p_p(-z)=1.}
\tag{L-28005.14}
\]

Tensoring the identities for `p=2` and `p=3` yields

\[
\boxed{
1=
\sum_{\epsilon,\eta=\pm1}
U_{2,\epsilon}(z)
U_{3,\eta}(w)
 p_2(\epsilon z)p_3(\eta w).}
\tag{L-28005.15}
\]

Multiplication by `mathcal O_6(s)` gives an exact finite reconstruction of the
odd-core reciprocal-zeta source from the four channels, using at most two dyadic
and two ternary delays.  Multiplying once more by
`(1-2^{-s})(1-3^{-s})` reconstructs `1/zeta(s)` itself.

Thus no infinite channel inverse is required.

## 7. Production consequence

The physical front end of the binary–ternary programme can now be organized as

```text
four parity channels
-> coefficientwise positive summed reflected forcing
-> exact parity orthogonalization
-> finite Bézout reconstruction
-> compact untwisted critical source
-> factor-108 carry transition.
```

The remaining obligation is an upper estimate for the complete four-channel
physical block which preserves a strict part of the source-image reserve after
all finite transition and collar terms are charged.

The theorem does not assert that the twisted channels individually have positive
inverse coefficients or compact carry images.  Those properties belong to the
untwisted channel.  The finite Bézout synthesis is what returns the paired
physical information to that compact source.

## 8. Proof boundary

Closed exactly or elementarily:

1. four twisted source identities;
2. a closed-strip frame reserve;
3. coefficientwise positivity of the summed forcing;
4. exact two-prime parity orthogonalization;
5. finite tensor Bézout reconstruction.

Open:

1. the four-channel independent-frequency physical upper estimate;
2. preservation of strict reserve under the finite synthesis and collars;
3. the compact-source energy theorem;
4. RH.
