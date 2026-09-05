# L-106504 — A saturating current prices a Blaschke model by pole height

Claim ID: `L-106504`  
Status: **PROVED EXACT OPERATOR LEMMA; XI INPUT SUPPLIED BY L-106502/L-106503**  
Created: 2026-08-25  
Depends on: `L-106502`, `L-106503`; the causal model-space decomposition  
RH status: **not assumed**

Let `B` be a finite upper-half-plane Blaschke product with zeros

\[
b_j=a_j+iy_j,\qquad y_j>0,
\]

and let `K_B=H^2\ominus BH^2`.  In the positive-frequency realization, the
normalized one-factor model vector is

\[
e_{a,y}(\xi)=\sqrt{2y}\,e^{-(y+ia)\xi},
\qquad \xi\ge0.
\tag{L-106504.1}

## 1. Causal monotone-weight contraction

Let `W(xi)>=0` be nonincreasing.  For every causal inner multiplier `C`,

\[
\boxed{
T_C^*M_WT_C\preceq M_W.
}
\tag{L-106504.2}

Indeed, by the layer-cake representation, a nonincreasing `W` is a positive
mixture of prefix projections `P_[0,s]`.  Causality and isometry give

\[
T_C^*P_{[0,s]}T_C\preceq P_{[0,s]}
\]

for every `s`, and integration proves (L-106504.2).

## 2. Model-space reserve trace

Let `0<=R<=I` be a diagonal source multiplier and suppose

\[
1-r(\xi)\le W(\xi).
\tag{L-106504.3}

Using

\[
K_{B_1\cdots B_n}
=K_{B_1}\oplus B_1K_{B_2}\oplus\cdots\oplus
 B_1\cdots B_{n-1}K_{B_n}
\]

and (L-106504.2) gives

\[
\boxed{
\operatorname{tr}_{K_B}(I-R)
\le
\sum_j\int_0^\infty
 W(\xi)\,2y_j e^{-2y_j\xi}\,d\xi.
}
\tag{L-106504.4}

There is no Gram condition number and no separation constant.

## 3. Saturating Xi profile

For the untranslated odd-current profile of `L-106502`, choose `xi_0` so
that

\[
1-r^\sharp_{K,h}(\xi)
\le
W_{K,h}(\xi)
:=
\begin{cases}
1,&0\le\xi\le\xi_0,\\
C_{K,h_0}h^2e^{-\xi},&\xi>\xi_0,
\end{cases}
\tag{L-106504.5}

and enlarge `xi_0` if necessary so that `W_(K,h)` is nonincreasing for
`0<=h<=h_0`.  Then

\[
\int W_{K,h}(\xi)2y e^{-2y\xi}d\xi
\le
1-e^{-2y\xi_0}
+{2C_{K,h_0}h^2y\over2y+1}
\le C'_{K,h_0,\xi_0}y.
\]

Consequently

\[
\boxed{
\operatorname{tr}_{K_B}(I-R^\sharp_{K,h})
\le C'_{K,h_0,\xi_0}\sum_j y_j.
}
\tag{L-106504.6}

Thus a positive-density family of poles may still have `o(N)` reserve cost
when its total height is `o(N)`.  Near-real poles are not charged one full
dimension apiece.

## 4. Endpoint consequence and exact remaining obstruction

Apply (L-106504.6) to the reduced denominator pole product of
`U_(K,lambda)`.  By `L-106503`, its total upper height is at most

\[
\mathfrak h_+(p)
+\mathfrak h_+(p^{(K)})
+\lambda(\deg p-K).
\tag{L-106504.7}

Hence the **denominator model reserve** is controlled by the original and
`K`th-derivative mean heights plus the explicit companion shift.

For the actual quotient `B_+/B_-`, the numerator inner factor acts causally
*before pulling the model space back to the input*.  Reversing that action is
not covered by (L-106504.2).  The unclosed term is exactly the numerator-phase
commutator already isolated in `L-106501.9`; it may not be deleted by calling
the denominator model well conditioned.
