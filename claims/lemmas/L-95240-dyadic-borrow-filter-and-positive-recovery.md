# L-95240 — The critical dyadic-borrow packet has a positive recovery telescope

Claim ID: `L-95240`  
Status: **PROPOSED COMPLETE EXACT ALGEBRAIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: PR #538 at `b7ed54922cee0bb6a62fd189f0f83edd3ff7441a`; the average-carry inverse notation of PR #474  
Scope: exact endpoint-scale algebra and Mellin/source audit; no all-scale packet positivity and no RH conclusion

## 1. The packet

Put

\[
 w_X(q)=q^{-1/2}\log(X/q)\mathbf 1_{q\le X}
\]

and let \(c_X\) be its exact average-carry inverse. For \(0<\rho<1\), define

\[
\boxed{
 P_{\rho,X}
 =
 w_X-(1-\rho)w_{X/2}-\rho w_{X/4}
}
\tag{L-95240.1}
\]

and

\[
\boxed{
 p_{\rho,X}
 =
 c_X-(1-\rho)c_{X/2}-\rho c_{X/4}.
}
\tag{L-95240.2}
\]

Linearity of the finite triangular inverse makes (L-95240.2) exact. No source approximation is present.

For \(\rho=1/14\), the target has the explicit positive three-piece form

\[
P_{\rho,X}(q)=q^{-1/2}
\begin{cases}
(1+\rho)\log2,&q\le X/4,\\
\rho\log(X/q)+(1-\rho)\log2,&X/4<q\le X/2,\\
\log(X/q),&X/2<q\le X,\\
0,&q>X.
\end{cases}
\tag{L-95240.3}
\]

Target positivity is not being confused with row positivity.

## 2. Exact filter factorization

Let \(\mathcal S\) be endpoint halving: \((\mathcal Sf)_X=f_{X/2}\). Then

\[
\boxed{
P_{\rho}=(I-\mathcal S)(I+\rho\mathcal S)w,
\qquad
p_{\rho}=(I-\mathcal S)(I+\rho\mathcal S)c.
}
\tag{L-95240.4}
\]

The scale polynomial is

\[
1-(1-\rho)z-\rho z^2=(1-z)(1+\rho z).
\tag{L-95240.5}
\]

Its reciprocal has coefficients

\[
\boxed{
a_j=\frac{1-(-\rho)^{j+1}}{1+\rho}>0.
}
\tag{L-95240.6}
\]

Equivalently,

\[
a_0=1,\qquad a_j=1-\rho a_{j-1}.
\tag{L-95240.7}
\]

For \(\rho=1/14\),

\[
\frac{13}{14}\le a_j\le1.
\tag{L-95240.8}
\]

With \(c_Y=0\) and \(p_{\rho,Y}=0\) for \(Y<2\), the finite recovery identity is

\[
\boxed{
c_X=\sum_{j\ge0}a_j p_{\rho,X/2^j}.
}
\tag{L-95240.9}
\]

Only finitely many terms are nonzero. There is no omitted terminal term.

Consequently,

\[
\boxed{
p_{\rho,Y}(n)\ge0\ \text{for every }Y,n
\quad\Longrightarrow\quad
c_X(n)\ge0\ \text{for every }X,n.
}
\tag{L-95240.10}
\]

This is a positive recovery theorem, not a proof of its packet-positivity hypothesis.

## 3. Mellin firewall

For a fixed inverse row, endpoint halving multiplies its Mellin transform by \(2^{-z}\). Hence the packet multiplier is

\[
\boxed{
(1-2^{-z})(1+\rho2^{-z}).
}
\tag{L-95240.11}
\]

The first factor has zeros only on \(\Re z=0\). Since \(0<\rho<1\), the second has zeros only on

\[
\Re z=\log_2\rho<0.
\]

Thus no zeta zero with \(\Re(\rho_\zeta-1/2)>0\) is cancelled. An eventual one-sign theorem for one zero-safe packet remains RH-bearing.

## 4. Exact proof boundary

Established here:

- the source-specific two-scale packet;
- its positive target pieces;
- the factorization \((1-z)(1+\rho z)\);
- positive finite recovery coefficients;
- exact recovery of every original carry row;
- the open-strip Mellin zero audit.

Open:

- \(p_{1/14,X}(n)\ge0\) for every endpoint and row;
- SHARP;
- CRCTP;
- RH.
