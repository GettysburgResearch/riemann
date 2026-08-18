# L-95503 — Product-variable and log-derivative normal forms preserve the full reciprocal-zeta resonance

Claim ID: `L-95503`  
Status: **PROPOSED COMPLETE EXACT REWRITING THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: `L-95500`; PR #580 `L-95402`

## 1. Product variable

In the separated coprime core put

\[
k=ab,
\qquad (a,b)=1.
\]

Then \(k\) is odd squarefree and

\[
\mu(a)\mu(b)=\mu(k).
\]

The ratio condition \(a<b<1024a\) selects finitely many balanced divisor
pairs of `k`. Thus SACF may be written as a one-sign product sum

\[
\sum_k\frac{\mu(k)}{\sqrt k}
\sum_{a\mid k\atop a<k/a<1024a}
\mathcal W_X(a,k/a),
\tag{L-95503.1}
\]

with the exact common-divisor and ten-band kernel retained in
\(\mathcal W_X\).

This is a change of coordinates, not a reduction to a divisor-bounded
coefficient. The number and location of balanced divisors remain arithmetic.

## 2. Dual-frequency divisor polynomial

For a ratio frequency `t`, the unrestricted coprime divisor polynomial has
local factor

\[
1-p^{-s-it}-p^{-s+it}.
\]

Restoring the common-divisor source adds \(p^{-2s}\). On the resonant line,

\[
\boxed{
1-p^{-s-it}-p^{-s+it}+p^{-2s}
=(1-p^{-s-it})(1-p^{-s+it}).
}
\tag{L-95503.2}
\]

The determinant parameterization therefore reconstructs the two shifted
reciprocal-zeta factors rather than producing an independent divisor-sum
cancellation.

## 3. Vaughan/Heath–Brown coefficient identities

The exact squarefree identity

\[
\mu(m)\log m
=-\sum_{p\mid m}(\log p)\mu(m/p)
\]

is the first derivative of the reciprocal Euler product. More elaborate
finite Vaughan or Heath–Brown decompositions distribute this derivative among
Type-I and Type-II convolution factors. After exact reassembly, the local
factor remains (L-95503.2).

Therefore the identities themselves do not create an extra averaging
parameter. A successful use of them must prove cancellation in at least one
balanced factor strong enough to meet `L-95502`.

## 4. Resonant logarithmic derivatives

Differentiating

\[
M_o(s_1)M_o(s_2)
\]

produces the complete \(\log m\), \(\log n\), and mixed logarithmic channels.
The `J1` term is the zeroth-order boundary component. No derivative gauge or
band remainder lies outside the tensor product.

## 5. Boundary

```text
product k=ab parameterization              EXACT
balanced divisor-pair representation       EXACT
dual-frequency local determinant            EXACT
log channels as Euler derivatives           EXACT
finite coefficient decompositions           SOURCE-FAITHFUL BUT NON-CLOSING
new balanced cancellation theorem            OPEN / RH-BEARING
```
