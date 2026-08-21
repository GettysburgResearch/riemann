# L-99930 — Activation-zero supercritical powers are globally positive

Claim ID: `L-99930`  
Status: **PROVED EXACT**  
Created: 2026-08-20  
RH status: **not assumed**

Put

\[
 \beta(n)=\mu(n)-\mathbf 1_{67\mid n}\mu(n/67)
\]

and

\[
 S(y)=4(\sqrt y-1)\mathbf 1_{y\ge1}.
\]

For real `m>=2`, define

\[
 G_m(X)=\sum_{n\ge1}\frac{\beta(n)}{\sqrt n}S(X/n)^m.
 \tag{L-99930.1}
\]

The sum is finite because `S(X/n)=0` for `n>X`.

## Labelled Euler representation

Use one labelled copy of every prime and a second labelled copy of `67`.  For a
finite label subset `A`, let `n_A` be the product of its labels, with the two
copies of `67` regarded as distinct before projection.  Then

\[
 \sum_A(-1)^{|A|}F(n_A)
 =\sum_n\beta(n)F(n)
 \tag{L-99930.2}
\]

for every finitely supported function `F`.  At the `67`-fibre the coefficients
are exactly `(1,-2,1)`.

For fixed `X`, put

\[
 w_m(A)=n_A^{-1/2}S(X/n_A)^m,
\]

with zero value when `n_A>X`, and let

\[
 M_j=\sum_{|A|=j}w_m(A).
\]

If `q` is a label in an active set `A`, write `B=A\setminus\{q\}` and
`Y=X/n_B`.  Then

\[
 S(Y)-\sqrt q\,S(Y/q)=4(\sqrt q-1)>0,
\]

so

\[
 \frac{w_m(A)}{w_m(B)}
 =q^{-1/2}\left(\frac{S(Y/q)}{S(Y)}\right)^m
 <q^{-(m+1)/2}.
 \tag{L-99930.3}
\]

The elementary bound

\[
 2^{-3/2}+3^{-3/2}+5^{-3/2}+7^{-3/2}
 +11^{-3/2}+\frac1{3\sqrt{11}}
 +13^{-3/2}+\frac1{3\sqrt{13}}
 +67^{-3/2}<1
 \tag{L-99930.4}
\]

controls the complete prime sum, including the second `67` label.  Indeed every
prime at least `11` lies in one of the progressions `6k-1`, `6k+1`, and the two
integral tails in (L-99930.4) dominate those progressions.

Double-counting pairs `(A,q)` with `q in A` gives

\[
 jM_j<\vartheta M_{j-1},\qquad \vartheta<1.
 \tag{L-99930.5}
\]

Hence `M_(2r)>M_(2r+1)` at every nonempty adjacent pair.  Therefore

\[
 \boxed{G_m(X)>0\qquad(X>1,\ m\ge2),}
 \tag{L-99930.6}
\]

while `G_m(1)=0`.

The zero `S(1)=0` is load-bearing: unlike the ordinary SHARP carrier, no signed
activation atom appears when the endpoint crosses an integer.