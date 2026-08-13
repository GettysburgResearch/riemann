# L-92101 — One high off-line orbit is absorbed by a small critical reserve fraction

Claim ID: `L-92101`  
Status: **PROVED EXACT RATIONAL CURVATURE DOMINATION**  
Created: 2026-08-13  
Depends on: `L-92000/L-92002`; `L-92100`  
RH status: **unproved**

Fix `t>1/4`. An off-line centered-zero orbit with representative

\[
 \lambda=a+ib,\qquad 0<|a|<1/2,
\]

and multiplicity `m` contributes

\[
 q(t)=\frac{4mU}{U^2+B^2},\qquad
 U=t+c,\quad c=b^2-a^2,\quad B=2ab.
\]

One unit of a critical-line orbit of squared ordinate `r` contributes

\[
 R(t)=\frac2{t+r}.
\]

Assume `c>r` and put

\[
 \kappa=\frac{B^2}{(c-r)^2}<1,
 \qquad
 s=\frac{c-r}{U}\in(0,1).
\]

For `E[f]=ff''-2(f')^2`, direct differentiation gives

\[
 \boxed{
 \mathcal E[q]
 =-\frac{32m^2B^2}{(U^2+B^2)^3},
 \qquad
 \mathcal E[R]=0.
 }
\tag{L-92101.1}

Define

\[
 Q_\kappa(s)
 =1-\kappa+3\kappa s(2-s)+\kappa^2s^2(3-2s).
\]

Then `Q_kappa(s)>=1-kappa>0`, and the exact cross curvature is

\[
\boxed{
 \mathcal C[q,R]
 :=qR''+Rq''-4q'R'
 =\frac{16m s^2Q_\kappa(s)}
 {U^4(1+\kappa s^2)^3(1-s)^3}>0.
}
\tag{L-92101.2}

Also

\[
 -\mathcal E[q]
 =\frac{32m^2\kappa s^2}
 {U^4(1+\kappa s^2)^3}.
\tag{L-92101.3}

Choose

\[
 \boxed{
 \epsilon(a,b,m;r)=\frac{2m\kappa}{1-\kappa}.
 }
\tag{L-92101.4}

Since

\[
 \mathcal E[q+\epsilon R]
 =\mathcal E[q]+\epsilon\mathcal C[q,R]
\]

and `(1-s)^3<=1`, equations (L-92101.2)--(L-92101.4) give

\[
 \boxed{
 \mathcal E[q+\epsilon R]\ge0.
 }
\tag{L-92101.5}

Equivalently, `1/(q+epsilon R)` is concave.

Suppose now that `0<r<=H^2/4` and `|b|>=H`, with `H^2>=3`. Then

\[
 c-r\ge b^2-1/4-H^2/4\ge(2/3)b^2.
\]

Since `B^2<b^2`,

\[
 \kappa\le\frac9{4b^2}<\frac12
\]

at the verified zeta height, and therefore

\[
 \boxed{
 \epsilon(a,b,m;r)\le\frac{9m}{b^2}.
 }
\tag{L-92101.6}

Thus the share of one low critical orbit needed for one hypothetical high
off-line orbit is quadratically summable in its ordinate.

## Exact boundary

```text
off-line curvature defect                 EXACT
critical reserve curvature                ZERO EXACTLY
cross curvature                           STRICTLY POSITIVE EXACT
absorbing fraction                        EXACT
high-orbit bound <=9m/b^2                 EXACT
global reserve budget                     L-92102
Riemann Hypothesis                        UNPROVED
```
