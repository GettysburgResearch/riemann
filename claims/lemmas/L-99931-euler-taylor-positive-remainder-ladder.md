# L-99931 — Every subcritical Euler–Taylor remainder is positive

Claim ID: `L-99931`  
Status: **PROVED EXACT**  
Created: 2026-08-20  
Depends on: `L-99930`  
RH status: **not assumed**

Fix an integer `m>=3`.  For `1<=k<=m`, define the positive-part Taylor
remainder

\[
 r_{m,k}(z)=(-1)^k\left[(1-z)_+^m-
 \sum_{j=0}^{k-1}(-1)^j\binom mjz^j\right],\qquad z\ge0.
 \tag{L-99931.1}
\]

Taylor's integral formula gives

\[
 \boxed{
 r_{m,k}(z)=
 \frac{m!}{(m-k)!(k-1)!}
 \int_0^{\min(z,1)}(z-t)^{k-1}(1-t)^{m-k}\,dt.
 }
 \tag{L-99931.2}
\]

Thus `r_(m,k)>=0`.  Moreover, for `c>=1`, the change of variables `t=cs`
and monotonicity of `(1-t)^(m-k)` give

\[
 \boxed{r_{m,k}(cz)\le c^k r_{m,k}(z).}
 \tag{L-99931.3}
\]

Define

\[
 E_{m,k}(X)=
 \sum_{n\ge1}\frac{\beta(n)}{n^{(m+1)/2}}
 r_{m,k}\!\left(\sqrt{n/X}\right).
 \tag{L-99931.4}
\]

For `k<=m-2` this series is absolutely convergent.  In the labelled Euler
model, adjoining a label `q` changes a positive summand by at most

\[
 q^{-(m+1)/2}q^{k/2}=q^{-(m+1-k)/2}.
 \tag{L-99931.5}
\]

The exponent in (L-99931.5) is at least `3/2`.  The strict prime-label bound
(L-99930.4), followed by the same adjacent-level pairing, proves

\[
 \boxed{E_{m,k}(X)>0
 \qquad(X>0,\ 1\le k\le m-2).}
 \tag{L-99931.6}
\]

## Exact alternating enclosures

Put

\[
 B(a)=\sum_{n\ge1}\frac{\beta(n)}{n^a}
 =\frac{1-67^{-a}}{\zeta(a)},\qquad a>1,
\]

and

\[
 F_m(X)=\sum_{n\ge1}\frac{\beta(n)}{n^{(m+1)/2}}
       (1-\sqrt{n/X})_+^m.
 \tag{L-99931.7}
\]

For every `k<=m-2`, finite Taylor expansion followed by absolutely convergent
Dirichlet summation gives

\[
 \boxed{
 F_m(X)=
 \sum_{j=0}^{k-1}(-1)^j\binom mj
 X^{-j/2}B\!\left(\frac{m+1-j}{2}\right)
 +(-1)^kE_{m,k}(X).
 }
 \tag{L-99931.8}
\]

Thus all Euler–Taylor layers whose effective exponent is strictly larger than
one have a certified alternating orientation.  The last proved layer is
`k=m-2`, where the effective prime exponent is `3/2`.

The next remainder `E_(m,m-1)` is still absolutely defined, but its local
removal ratio is asymptotically `1/q`; the prime harmonic mass diverges.  Its
sign is not asserted by this lemma.