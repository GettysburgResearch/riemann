# L-92200 — Reciprocal Xi curvature is a pairwise squared-pole dispersion

Claim ID: `L-92200`  
Status: **PROPOSED COMPLETE EXACT IDENTITY — REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: centered Hadamard product for `xi`; `L-92000`--`L-92100`  
RH status: **unproved**

## 1. Squared-variable entire function

Put

\[
 \Xi(z)=\xi\!\left(\frac12+z\right),
 \qquad
 \Phi(t)=\Xi(\sqrt t).
\]

Because `Xi` is even of order one, `Phi` is an entire function of order
`1/2`.  Its genus-zero product is

\[
 \Phi(t)=\Phi(0)
 \prod_{\alpha}
 \left(1+\frac{t}{s_\alpha}\right)^{m_\alpha},
\]

where the squared-pole parameters are

\[
 s_\alpha=-\lambda_\alpha^2
\]

for one representative of each `plus/minus` centered zero pair.  The
parameters are invariant under conjugation and satisfy `Re s_alpha>0` because
all nontrivial zero ordinates have modulus greater than one while
`|Re lambda|<1/2`.

Define

\[
 p(t)=\frac{\Xi'(\sqrt t)}{\sqrt t\,\Xi(\sqrt t)}
     =2\frac{\Phi'(t)}{\Phi(t)},
 \qquad t>\frac14.
\]

Normal convergence gives

\[
 \boxed{
 p(t)=\sum_\alpha\frac{w_\alpha}{t+s_\alpha},
 \qquad
 w_\alpha=2m_\alpha>0.
 }
 \tag{L-92200.1}
\]

For a critical-line orbit `lambda=i b`, this is the real pole
`s=b^2` of weight `2m`.  For an off-line orbit `lambda=a+i b`, the two
squared-pole parameters are

\[
 s=c+id,
 \qquad
 \bar s=c-id,
 \qquad
 c=b^2-a^2,
 \qquad
 d=2ab,
\]

each of weight `2m`.

## 2. Pairwise curvature identity

Differentiate (L-92200.1):

\[
 p'(t)=-\sum_\alpha\frac{w_\alpha}{(t+s_\alpha)^2},
 \qquad
 p''(t)=2\sum_\alpha\frac{w_\alpha}{(t+s_\alpha)^3}.
\]

Symmetrising the double sum gives

\[
\boxed{
\begin{aligned}
 \mathcal D(t)
 &:=
 p(t)p''(t)-2p'(t)^2\\
 &=\sum_{\alpha,\beta}
 w_\alpha w_\beta
 \frac{(s_\alpha-s_\beta)^2}
 {(t+s_\alpha)^3(t+s_\beta)^3}.
\end{aligned}}
\tag{L-92200.2}
\]

Indeed

\[
 \frac1{u_\alpha u_\beta^3}
 +\frac1{u_\beta u_\alpha^3}
 -\frac2{u_\alpha^2u_\beta^2}
 =\frac{(u_\alpha-u_\beta)^2}
       {u_\alpha^3u_\beta^3},
\]

and `u_alpha-u_beta=s_alpha-s_beta`.  Conjugation invariance makes the
right-hand side real.

For an unordered pair `alpha<beta`, its contribution is

\[
 \boxed{
 2w_\alpha w_\beta
 \Re\frac{(s_\alpha-s_\beta)^2}
 {(t+s_\alpha)^3(t+s_\beta)^3}.
 }
 \tag{L-92200.3}
\]

## 3. Stieltjes and off-line readings

If all `s_alpha` are real, then every summand in (L-92200.2) is nonnegative.
This is the pairwise form of the Stieltjes inequality

\[
 p p''-2(p')^2\ge0,
\]

or equivalently the concavity of the impedance

\[
 Z(t)=\frac1{p(t)}.
\]

For one off-line conjugate pair `s=c+id`, `bar s=c-id` of equal weight `w`,
its internal pair contribution is

\[
 \boxed{
 -\frac{8w^2d^2}
 {\bigl((t+c)^2+d^2\bigr)^3}<0.
 }
 \tag{L-92200.4}
\]

Thus the reciprocal-curvature problem is exactly a competition between:

```text
positive dispersion among different real squared poles;
positive long-range interactions of narrow complex poles;
negative local interactions created by conjugate/off-line clustering.
```

## 4. Relation to the third-order Pick determinant

`L-92000/L-92002` give

\[
 \left(\frac1p\right)''
 =\frac{2(p')^2-pp''}{p^3}
 =-\frac{\mathcal D}{p^3}.
\]

Therefore

\[
 \boxed{
 \mathcal D(t)\ge0
 \quad\Longleftrightarrow\quad
 Z''(t)\le0.
 }
\]

Together with the unconditional concavity of the conjugate impedance
`t p(t)` proposed in `L-92001`, this is the sole scalar sign needed for all
three-node infinitesimal Xi Pick matrices.

## 5. Exact boundary

```text
squared-variable genus-zero product           PROPOSED COMPLETE
partial-fraction expansion of p               PROPOSED COMPLETE
pairwise curvature identity                   EXACT ALGEBRA
critical/real-pole terms                       NONNEGATIVE
single off-line internal term                 STRICTLY NEGATIVE
verified-height domination of all negatives   NEXT LEMMA / PROPOSED
Riemann Hypothesis                             UNPROVED
```
