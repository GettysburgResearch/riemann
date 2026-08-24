# A Hermitian-compatible Wick bank and matrix companion flux

## Abstract

We audit a proposed ninety-percent critical-line-zero route based on the
low-order Hermite–Pick residue matrix.  The audit finds a precise obstruction:
a formal scalar square in a commutative source algebra is not the Hermitian
polarization produced by an off-real Xi contour.  We prove that no one-channel
holomorphic scalar filter can cancel both Hermitian source levels one and two.
We then construct a minimal two-channel analytic bank which cancels both
levels exactly and remains positive for every strict scalar contraction.  We
also polarize the companion Lorentz-energy identity to a complete matrix
identity.  These results reduce the ninety-percent problem to one explicit
signed strip/companion negative-trace estimate.  That estimate is not proved;
90% and RH remain open.

## 1. Scalar obstruction

Put

\[
r(z)=\Re(1-z)^{-1}.
\]

For `w(z)=1+az+bz^2+O(z^3)`, the degree-one terms of `|w|^2 r` vanish only for
`a=-1/2`.  The mixed degree-two coefficient then equals `-1/4`, independently
of `b`.  Hence a scalar analytic Wick factor cannot realize the formal
second-order source square inside a Hermitian fold.

## 2. Two-channel bank

Take

\[
w_0=1-z/2-z^2/4,
\qquad
w_1=z/2.
\]

For independent lower/upper boundary variables `z,y`, the bank satisfies

\[
\Lambda(z,y)=
[w_0(z)w_0(y)+w_1(z)w_1(y)]
\frac12[(1-z)^{-1}+(1-y)^{-1}]
=1+O_{\rm total}((z,y)^3).
\]

On the Hermitian slice `y=bar z`, this is the sole nonzero channel eigenvalue.

Direct expansion gives

\[
\Lambda(z)=1+O_{\rm Herm}(|z|^3)
\]

with every total degree-one and degree-two bidegree exactly zero.  Moreover
`Lambda(z)>0` for `|z|<1`, and

\[
|\Lambda(z)-1|
\le
\frac{r^3(4+3r+r^2)}{16(1-r)^2}
\quad(|z|\le r<1).
\]

At `r=1/4`, the bank lies between `9139/9216` and `9293/9216`.

## 3. Matrix companion identity

For a real derivative chain set

\[
p=F_k,
\quad E=F_{k+1}+i\delta F_k,
\quad H=F_{k+1}+\lambda F_{k-1}.
\]

For a source-owned real analytic observation vector `Phi`, integrate

\[
\frac{H^2}{pE}\Phi\Phi^{\mathsf T}
\]

over the toothed lower contour.  Every real `p`-zero contributes

\[
(1+\lambda\rho_c)^2\Phi(c)\Phi(c)^{\mathsf T},
\]

and the real-line density is the PSD matrix

\[
\frac{\delta}{\pi}
\frac{H(x)^2}{F_{k+1}(x)^2+\delta^2F_k(x)^2}
\Phi(x)\Phi(x)^{\mathsf T}dx.
\]

The exact residue theorem leaves only the signed vertical and companion-pole
matrix.  Also

\[
R_\Phi
=\frac1{2\lambda}
(G_\Phi+\lambda^2S_\Phi-D_\Phi),
\]

so the companion defect is literally the matrix debt against the positive
Pick anchor.

## 4. Ninety-percent cut

If the bank is realized as the actual folded Xi strip observation and the
Gram-normalized negative trace of the complete companion/partial-index
remainder is less than

\[
\frac{9139}{184320}d_T,
\]

then fewer than `d_T/20` compression directions are nonpositive.  The exact
confluent Cauchy-index signature therefore gives more than 90% of zeta zeros
on the line.

The analytic strip realization and this negative-trace estimate remain open.

## 5. Calibration firewall

A constant holomorphic contour carrier integrates to zero.  Hence the horizontal identity term of the bank cannot itself count critical points; its cancellation is precisely what reappears as the strip partial-index/endpoint ledger.
