# L-91560 — Same-index inclusion of a contracted detail packing is capacity-faithful and loss-isometric

Claim ID: `L-91560`  
Status: **PROVED EXACT CHILD-LIFT REPLACEMENT THEOREM**  
Created: 2026-08-13  
Depends on: `L-90029`; the explicit radix-four target  
RH status: **unproved**

## 1. Monotonicity of the radix-four target

For real `X>=1` and physical column `q>=2`, the radix-four detail target is

\[
 \Omega_X(q)=w_X(q)-2w_X(4q),
 \qquad
 w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X}.
\]

Its explicit form is

\[
 \boxed{
 \Omega_X(q)=
 \begin{cases}
 0,&X<q,\\[1mm]
 q^{-1/2}\log(X/q),&q\le X<4q,\\[1mm]
 q^{-1/2}\log4,&4q\le X.
 \end{cases}}
\tag{L-91560.1}
\]

Hence, for fixed `q`,

\[
\boxed{
 0<Y\le X
 \Longrightarrow
 \Omega_Y(q)\le\Omega_X(q).
}
\tag{L-91560.2}
\]

## 2. Same-index child inclusion

Let `d=(d_T)_{T>=3}` be any nonnegative detail-feasible packing at endpoint `Y`:

\[
 \sum_Td_T\Xi_T(q)\le\Omega_Y(q)
 \qquad(q\ge2).
\tag{L-91560.3}
\]

Regard the identical coefficient vector as a parent packing at endpoint `X>=Y`.
Then (L-91560.2) gives

\[
 \boxed{
 \sum_Td_T\Xi_T(q)
 \le\Omega_X(q)
 \qquad(q\ge2).
 }
\tag{L-91560.4}
\]

Thus the child packing is inserted at the same physical row indices.  No affine
map, fractional column, color, or additional collar is needed.

By `L-90029`, it is ordinarily feasible as well.

## 3. Entropy score and loss

The entropy score depends only on the row vector:

\[
 \mathcal S(d)=\sum_Td_TH_T.
\]

Same-index inclusion leaves it unchanged:

\[
\boxed{
 \mathcal S_X(d)=\mathcal S_Y(d)=\mathcal S(d).
}
\tag{L-91560.5}
\]

If a positive child packet has target mass `omega` and declared score
`omega J`, use the scaled row `omega d`.  Positive homogeneity gives

\[
\boxed{
 \ell_X^{\rm inherited}(\omega d)
 =\omega[J-\mathcal S(d)].
}
\tag{L-91560.6}
\]

The inherited loss coefficient is exactly the child target mass.

## 4. Several contracted children

Let `Y_b<=X` and let `d_b` be detail feasible at `Y_b`.  If

\[
 \omega_b\ge0,
 \qquad
 \sum_b\omega_b\le1,
\]

then

\[
\begin{aligned}
 \sum_b\omega_b\sum_Td_{b,T}\Xi_T(q)
 &\le\sum_b\omega_b\Omega_{Y_b}(q)\\
 &\le\left(\sum_b\omega_b\right)\Omega_X(q)\\
 &\le\Omega_X(q).
\end{aligned}
\]

Therefore

\[
\boxed{
 d_X^{\rm child}=\sum_b\omega_bd_b
}
\tag{L-91560.7}
\]

is a capacity-faithful parent packing and

\[
\boxed{
 \ell_X^{\rm inherited}
 =\sum_b\omega_b\ell_{Y_b}(d_b).
}
\tag{L-91560.8}
\]

## 5. Meaning for the fixed-67 typed reset

After Hall residualization has forgotten arithmetic prime provenance, both
hereditary packets may be contracted to `X/67` in the type ledger while their
arbitrary recursively chosen finite packings are included at the same physical
indices.

This replaces the invalid composition isolated in `R-91560`.  The affine Pascal
lift remains valuable for arithmetic colored children before provenance is
erased; it is not needed for this post-Hall abstract contraction.

The theorem does not by itself pay current-generation Hall bonuses or prove
that the current packet occupies only the complementary target capacity.  That
is the final source-specific producer audit.

```text
Omega_Y <= Omega_X                                EXACT
same-index child detail feasibility               EXACT
same-index ordinary feasibility                   EXACT VIA L-90029
entropy score preserved                           EXACT
subprobability child sum feasible                 EXACT
post-Hall affine child lift                       NOT NEEDED
current-generation complementary-capacity audit  OPEN
Riemann Hypothesis                                UNPROVEN
```
