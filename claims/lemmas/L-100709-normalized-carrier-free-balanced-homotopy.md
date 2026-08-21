# L-100709 — The normalized balanced homotopy derivative has two exact carrier zeros

Claim ID: `L-100709`  
Status: **PROVED EXACT LOCAL/PRODUCT IDENTITY; PHYSICAL ONE-SIDED ESTIMATE OPEN**  
Created: 2026-08-21  
Depends on: `L-100703`; `L-100708`  
RH status: **not assumed**

For a prime label `p`, put

\[
r_p=p^{-1/2},
\qquad
a_p=r_p^2=p^{-1},
\qquad Y_p=r_pU_p.
\]

The local balanced homotopy factor is

\[
H_{p,t}=I-tY_p-(1-t)Y_p^2,
\qquad0\le t\le1.
\tag{L-100709.1}
\]

On the critical half-order carrier `P(X)=sqrt(X)`,

\[
U_pP=r_pP,
\qquad Y_pP=a_pP.
\]

Thus the exact carrier eigenvalue of `H_(p,t)` is

\[
\boxed{
c_{p,t}=1-ta_p-(1-t)a_p^2>0.
}
\tag{L-100709.2}
\]

Define the carrier-normalized factor

\[
\overline H_{p,t}=c_{p,t}^{-1}H_{p,t}.
\]

Then

\[
\overline H_{p,t}P=P.
\tag{L-100709.3}
\]

## 1. Exact derivative factorization

Differentiate the quotient. Since

\[
\partial_tH_{p,t}=Y_p^2-Y_p,
\qquad
\partial_tc_{p,t}=a_p^2-a_p,
\]

direct polynomial division gives

\[
\boxed{
\partial_t\overline H_{p,t}
=
\frac{(1-a_p)(Y_p-a_pI)(Y_p-I)}{c_{p,t}^2}.
}
\tag{L-100709.4}
\]

Indeed, the numerator

\[
(Y_p^2-Y_p)c_{p,t}-H_{p,t}(a_p^2-a_p)
\]

is independent of `t`, has leading coefficient `1-a_p`, and vanishes at
`Y_p=a_pI` and `Y_p=I`.

The two roots have distinct physical meanings:

```text
Y_p=a_p       kills the X^(1/2) critical carrier;
Y_p=1         kills the X^(-1/2) reciprocal carrier.
```

No claim about the constant mode is being made.

In Mellin notation `z=s+1/2`, the local derivative multiplier is

\[
\boxed{
\frac{(1-p^{-1})(p^{-z}-p^{-1})(p^{-z}-1)}
     {[1-tp^{-1}-(1-t)p^{-2}]^2}.
}
\tag{L-100709.5}
\]

It is nonzero at a nontrivial zeta zero in the open strip, while it vanishes at
both real carrier locations `z=1` and `z=0`.

## 2. Product homotopy

For a finite labelled prime set, including two independent `67` coordinates,
put

\[
\overline{\mathscr H}_t=\prod_p\overline H_{p,t}.
\]

All factors commute, so

\[
\boxed{
\partial_t\overline{\mathscr H}_t
=
\sum_p
\frac{(1-p^{-1})(Y_p-p^{-1}I)(Y_p-I)}{c_{p,t}^2}
\prod_{q\ne p}\overline H_{q,t}.
}
\tag{L-100709.6}
\]

At the endpoints,

\[
\overline H_{p,0}
=
\frac{I-p^{-1}U_{p^2}}{1-p^{-2}},
\qquad
\overline H_{p,1}
=
\frac{I-p^{-1/2}U_p}{1-p^{-1}}.
\tag{L-100709.7}
\]

Thus (L-100709.6) is an inverse-free, carrier-normalized path from the squared
Euler state to the native state.

## 3. Interaction with the cubic collar

Apply the product identity to the cubic decomposition

\[
\Psi=P-64+C
\]

from `L-100708`. Every normalized factor fixes `P`, and the derivative in
(L-100709.6) annihilates it exactly. Therefore the derivative of the normalized
physical packet is supported entirely on

```text
the reciprocal carrier X^(-1/2), if present;
the inactive cubic collar C;
activation interfaces of the finite source.
```

For the centered double-owner residual, the constant and critical carrier are
already absent, so only the collar layer cake remains.

This proves that the balanced transition estimate can be posed without a
hidden `sqrt(X)/log(X)` carrier. It does **not** prove its sign: the retained
finite rough-prime counterexample on this branch shows that completion by the
other prime factors can reverse a locally positive transition.

## Correct remaining target

The remaining statement is a source-specific, logarithmically integrated
estimate for the carrier-free product derivative (L-100709.6), after insertion
of the exact threshold layer cake (L-100708.4). A source-blind pointwise cone is
not valid; cancellation across prime labels and activation thresholds must be
retained.