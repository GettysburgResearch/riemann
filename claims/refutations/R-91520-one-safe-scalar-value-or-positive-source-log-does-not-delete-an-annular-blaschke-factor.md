# R-91520 — One safe scalar value or positive source log does not delete an annular Blaschke factor

Claim ID: `R-91520`  
Status: **EXACT ONE-NODE IDENTIFICATION FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91520/L-91521`; `R-91407`  
RH status: **unproved**

## 1. The tempting shortcut

The logarithmic telescope is additive and every annular log mass is positive.
It is tempting to compare a positive arithmetic log innovation with the safe
real value of the horizontal Xi quotient and declare the hyperbolic annular
factor absent.

That implication is false without a source-to-model identification.

## 2. Two different Blaschke factors can have the same one-node modulus

Fix an interior node `eta>0`. For a right-half-plane zero

\[
 \zeta=x+iy
\]

the modulus is

\[
 |b_\zeta(\eta)|^2
 =\frac{(\eta-x)^2+y^2}
        {(\eta+x)^2+y^2}.
\]

There are infinitely many distinct pairs `(x,y)` giving the same value.
For example, at `eta=1`,

\[
 \zeta_1=\frac15
\]

has modulus squared `4/9`. Choosing

\[
 \zeta_2=\frac3{10}+i\sqrt{47/100}
\]

gives the same modulus:

\[
 \frac{(1-3/10)^2+47/100}
      {(1+3/10)^2+47/100}
 =\frac{96/100}{216/100}
 =\frac49.
\]

Thus the quotient

\[
 \frac{b_{\zeta_1}}{b_{\zeta_2}}
\]

has unit modulus at the chosen interior node while its denominator contains a
nonconstant hyperbolic Blaschke factor.

## 3. Consequence

A single value

\[
 |\Theta_a(\eta)|
\]

or a scalar positive source norm at that node does not determine the
hyperbolic factor. Stable/critical and hyperbolic contributions may trade
modulus while leaving the total scalar unchanged.

Likewise, positivity of a source innovation sequence does not imply

\[
 \Lambda_{a_j,a_{j-1}}^{\rm ann}(\eta)=0.
\]

The arithmetic map must identify which part of the source log belongs to the
critical and deterministic stable outputs.

## 4. What the logarithmic route still gains

The firewall does not negate `L-91520`. Once a valid source-ordered canonical
factorization is present, the hyperbolic term is one additive scalar and has no
cross-generation weight. The remaining identification is smaller than full
operator CPPD, but it is not automatic from scalar values.

## 5. Exact boundary

```text
annular log telescope                          EXACT
positive source log alone deletes annular mass FALSE
one interior scalar determines Blaschke factor FALSE
source-ordered log-factor identification       OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```
