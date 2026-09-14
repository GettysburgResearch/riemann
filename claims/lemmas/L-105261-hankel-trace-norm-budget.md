# L-105261 — The physical degree-four Hankel block costs less than \(1/60\)

Claim ID: `L-105261`  
Status: **PROVED FROM L-105520 AND FINITE MATRIX INEQUALITIES**  
Created: 2026-08-24  
Depends on: L-105260; PR #726 L-105520; PR #731 L-105250--L-105253  
RH status: not assumed

Let \(V_T\) be the retained \(d_T\)-dimensional one-sided Fourier frame and let \(H_T\) be the carrier-free same-sign Hankel block from L-105260 after the degree-four square-root polynomial.

The corrected physical model of L-105520 gives

\[
\mathcal D_4(2)\le D_*:=\frac{173344649}{1275293859840}<\frac1{7000}.
\tag{1}
\]

The finite-section Bessel/mean-value estimate for the same-sign block is

\[
\|H_T\|_{\rm HS}^2\le 2D_*d_T+o(d_T).
\tag{2}
\]

The factor \(2\) is deliberately retained as a conservative allowance for the two analytic orientations. It avoids silently identifying the Hermitian polarization with a single formal square.

For any \(d\times d\) Hermitian matrix \(Y\),

\[
\operatorname{tr}(Y_-)\le \|Y\|_{S_1}\le \sqrt d\,\|Y\|_{\rm HS}.
\tag{3}
\]

Consequently,

\[
\frac{\operatorname{tr}((\operatorname{Re}H_T)_-)}{d_T}\le\sqrt{2D_*}+o(1).
\tag{4}
\]

Exact rational comparison gives

\[
2D_*<\frac1{60^2}.
\tag{5}
\]

Hence

\[
\boxed{\operatorname{tr}((\operatorname{Re}H_T)_-)<\left(\frac1{60}+o(1)\right)d_T.}
\tag{6}
\]

If \(D_{\rm acc}\succeq(1-o(1))I\), the number of nonpositive directions created by the Hankel polarization is bounded by the same quantity. Thus the formerly qualitative polarization mismatch consumes less than \(1.667\%\) of the retained dimension.
