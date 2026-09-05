# L-106433 — Rational all-pass tails are explicit Cauchy--exponential quadratic forms

Claim ID: `L-106433`  
Status: **PROVED EXACT FOR FINITE REDUCED RATIONAL ALL-PASS SYMBOLS; CONFLUENT FORM INCLUDED**  
Created: 2026-08-25  
Depends on: `L-106415`, `L-106430`, `L-106432`  
RH status: **not assumed**

Let \(U\) be a scalar reduced rational all-pass function on the real line,
normalized to a unimodular constant at infinity. Let its poles in the upper
half-plane be

\[
b_j=a_j+iy_j,\qquad y_j>0,
\]

initially simple, and write

\[
U(t)=\omega+\sum_{j=1}^{m_-}\frac{c_j}{t-b_j}.
\tag{L-106433.1}
\]

For \(r>0\), residue calculus gives

\[
\boxed{
\widehat U(-r)
=
i\sum_{j=1}^{m_-}c_j e^{ib_jr}.
}
\tag{L-106433.2}
\]

Put

\[
s_{jk}=-i(b_j-\overline{b_k})
=(y_j+y_k)-i(a_j-a_k),
\qquad \Re s_{jk}>0.
\tag{L-106433.3}
\]

## 1. Negative visible and tail matrices

Using

\[
\int_H^\infty(r-H)e^{-sr}\,dr=\frac{e^{-sH}}{s^2}
\qquad(\Re s>0),
\]

`L-106432` yields

\[
\boxed{
\|H_UP_H^\perp\|_{\mathcal S_2}^2
=
\sum_{j,k}
c_j\overline{c_k}
\frac{e^{-s_{jk}H}}{s_{jk}^2}.
}
\tag{L-106433.4}
\]

Likewise,

\[
\boxed{
\|H_UP_H\|_{\mathcal S_2}^2
=
\sum_{j,k}
c_j\overline{c_k}
\frac{1-e^{-s_{jk}H}}{s_{jk}^2}.
}
\tag{L-106433.5}
\]

Both expressions are real and nonnegative because they are Gram integrals,
although that positivity is not termwise in the displayed Cauchy matrix.

Apply the same construction to \(U^{-1}=\overline U\). Its upper-half-plane
poles are the upper zeros of \(U\); denote their locations and residues by
\(\alpha_\ell,d_\ell\). Subtracting the corresponding quadratic forms gives
the signed complement \(\mathcal D_H(U)\) exactly.

Thus the endpoint signed-tail problem is one explicit difference of two
positive Cauchy--exponential forms at the pole and zero companion divisors.

## 2. Simple-factor calibration

For

\[
U_b(t)=\frac{t-\overline b}{t-b},
\qquad b=a+iy,
\]

one has

\[
\widehat U_b(-r)=-2y e^{ibr},
\qquad r>0.
\]

Consequently,

\[
\boxed{
\|H_{U_b}P_H\|_{\mathcal S_2}^2
=1-e^{-2yH},
\qquad
\|H_{U_b}P_H^\perp\|_{\mathcal S_2}^2
=e^{-2yH}.
}
\tag{L-106433.6}
\]

At the live scale \(yH=1/200\), one simple anti-inner factor has

\[
1-e^{-1/100}=0.009950166\ldots
\]

visible energy and

\[
e^{-1/100}=0.990049833\ldots
\]

complement energy. This is linear at first order in \(yH\), while the
four-channel source ratios of `L-106410--L-106413` are squared source
constants. Their equality cannot be presumed.

## 3. Confluent factors

A pole of order \(r\) contributes terms

\[
r^q e^{ibr},\qquad 0\le q<r,
\]

to the Fourier kernel. Its visible and tail blocks are obtained by
differentiating

\[
\frac{1-e^{-sH}}{s^2},
\qquad
\frac{e^{-sH}}{s^2}
\]

with respect to the confluent pole coordinates. This is the spectral analogue
of the Laguerre/confluent sampling blocks in `L-106430`; collisions introduce
no unspecified conditioning constant.

## 4. Scope

The theorem is a finite exact formula. Passing to cofinal Xi companion
divisors requires the endpoint, common-factor, exponential-type and trace
exhaustion ledgers. No favorable Xi asymptotic is asserted here.
