# L-91880 — The exact native input is a disjoint finite/Volterra arithmetic source

Claim ID: `L-91880`  
Status: **PROVED EXACT SOURCE/OBSERVATION DECOMPOSITION**  
Created: 2026-08-16  
Primary inputs: `L-91870`, `L-91760`, native finite row `L-91377`  
RH status: **unproved**

For integer `X`, put

\[
K=\left\lfloor\frac X{67}\right\rfloor+1,\qquad W=10000,
\]

and

\[
\mathcal I_X=\{K+2,\ldots,X-W-3\}.
\]

Let

\[
d_X^\star(m)=\sum_{k\le X/m}\frac{\mu(k)}{\sqrt{km}}\log\frac{X}{km},
\]

and let `R` be the exact finite component-row map.

## 1. Literal finite sector

Let `d_(X,A)^star` be the restriction of `d_X^star` to `m notin I_X`, and define

\[
c_{X,A}=\mathcal R b_{X,A}^\star.
\]

Its occurrence space is the literal finite native set

\[
\mathscr S_{X,A}=\{(m,k,\varepsilon):m\notin\mathcal I_X,\ km\le X,\ \mu(k)=\varepsilon\ne0\},
\]

with positive occurrence mass

\[
a_{X,m,k}=\frac1{\sqrt{km}}\log\frac{X}{km}.
\]

The sign is the parity label `epsilon`, not a signed mass.

## 2. Volterra bulk sector

Use the tagged complete-cell set

\[
\mathscr T_{X,B}=\coprod_{n\in\mathcal I_X}\{n\}\times[0,1).
\]

For `s=n+u` and `x=X/s`, define

\[
\ell_x(k)=\frac1{\sqrt k}\left(2\sqrt{\frac xk}-1\right)>0,
\]

and the paired positive measures

\[
d\Sigma_{X,B}^{\pm}(s,k)=\frac2s\,\mathbf1_{\mu(k)=\pm1}\,\ell_{X/s}(k)\,ds.
\]

Every colour multiplies the same positive infinitesimal row `p_s`.

## 3. Exact hybrid identity

Let `bar c_(X,I)` be the Volterra row obtained by integrating over the complete cells `I_X`, and let `E_X^I` be the exact retained-cell finite/continuum defect. Then

\[
\boxed{c_X=c_{X,A}+\overline c_{X,I}+\mathcal R E_X^I.}
\tag{L-91880.1}
\]

The three terms have different types:

```text
c_(X,A):
    literal finite native arithmetic source;

bar c_(X,I):
    exact native Volterra Möbius source;

R E_X^I:
    signed observation comparison, never positive source.
```

The parent marginal is therefore the native Möbius datum. The canonical `P_61` rough lift is not used as the input marginal.

## 4. Bulk is terminal

On every bulk cell, `1<X/s<67`. Hence all active root colours are composed only of primes at most `61`. The bulk source has no rough first-owner coordinate. Its rank-one cancellation is terminal and current-owned.

All rough ownership is confined to the anchored finite sector.

## 5. Native coordinates

Applying the exact native observations to (L-91880.1) gives, before estimates,

\[
w_X=C(c_{X,A})+C(\overline c_{X,I})+v(E_X^I),
\]

\[
\Omega_X=\Xi(c_{X,A})+\Xi(\overline c_{X,I})+\mathcal D_4v(E_X^I),
\]

and the analogous exact benchmark/literal-score identity.

```text
finite native source                 exact
bulk native Volterra source          exact
signed comparison                    separate
bulk rough lift                      absent
bulk causal difference               absent
```