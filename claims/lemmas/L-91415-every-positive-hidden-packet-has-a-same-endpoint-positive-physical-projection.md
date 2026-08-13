# L-91415 — Every positive four-mode packet has a same-endpoint positive physical projection with target exactness and bounded score deficit

Claim ID: `L-91415`  
Status: **PROVED EXACT POINTWISE / MEASURE-VALUED PROJECTION THEOREM**  
Created: 2026-08-13  
Depends on: positive hidden ledgers `L-91337`; canonical positive packet cone  
RH status: **unproved**

## 1. Positive hidden packet

At one endpoint let

\[
z=(x^+,x^-,y^+,y^-)\in\mathbb R_{\ge0}^4.
\]

Its positive hidden target and score are

\[
T=x^++y^-,
\qquad
S=2x^++x^-.
\tag{L-91415.1
}

A positive physical state `(L,R)` has

\[
T_{\rm phys}=L+2R,
\qquad
S_{\rm phys}=2L+R.
\]

For fixed target `T`, the positive physical cone permits exactly the score
interval

\[
\frac T2\le S_{\rm phys}\le2T.
\]

## 2. Clipped score

Define

\[
\bar S=\max\left(\frac T2,\min(S,2T)\right)
\]

and

\[
\boxed{
L=\frac{2\bar S-T}{3},
\qquad
R=\frac{2T-\bar S}{3}.
}
\tag{L-91415.2
}

Then `L,R>=0` and

\[
\boxed{L+2R=T,}
\tag{L-91415.3
}

\[
\boxed{2L+R=\bar S.}
\tag{L-91415.4
}

Thus the projection is target exact at the same endpoint.

## 3. Score deficit

If `S<=2T`, then `bar S>=S` and the projection is score-favorable. If `S>2T`,

\[
S-\bar S=S-2T=x^- -2y^-.
\]

Consequently

\[
\boxed{
(S-S_{\rm phys})_+
=(x^- -2y^-)_+
\le x^-.
}
\tag{L-91415.5
}

The complete positive score deficit is therefore bounded by one coordinate of
the original positive packet.

The projected physical mass obeys

\[
L+R=\frac{T+\bar S}{3}\le T\le x^++x^-+y^++y^-.
\tag{L-91415.6
}

## 4. Measure-valued form

Let the four coordinates be positive measures. Use their sum as a dominating
measure and apply (L-91415.2) to the Radon--Nikodym densities. The resulting
`L` and `R` are positive measures and equations (L-91415.3)--(L-91415.6) hold
as measure identities/inequalities.

The construction is measurable and positively homogeneous.

## 5. Application to survival and branch excesses

For each exact least-prime branch, extract the common canonical child

\[
\alpha_jI(L,R),
\qquad
\alpha_j=\min(h_j^X,h_j^Y).
\]

Keep that packet as the only recursive child. Apply the present projection,
**at the branch's actual child endpoint**, to the nonnegative excess

\[
(H_j-\alpha_jI_4)I(L,R).
\]

Apply it at the parent endpoint to the survival packet `Q_infty I(L,R)`.

Every unmatched packet is therefore realized without moving it between
endpoints. The total positive score deficit is bounded by the total `X^-`
coordinate of the exact positive partition, hence by the parent hidden mass.

## 6. Physical packet cone

The output is a positive `(L,R)` measure at its native endpoint. By the
canonical positive packet theorem, it has nonnegative target, component rows,
ordinary/radix-four responses and a finite mass-proportional local producer.

Thus every nonrecursive survival/excess packet is a valid current packet with
uniform debt per unit positive mass.

## 7. Consequence

The exact branch decomposition now has:

```text
canonical recursive child: alpha_j I(L,R) at X/p_j;
positive current excess: same endpoint as its exact branch;
positive survival packet: parent endpoint;
child mass sum <= parent mass;
all local score deficit <= parent positive mass.
```

No branch is identified with an `r`-scaled child, and no unmatched mode mass is
relocated between endpoints.

```text
same-endpoint target exactness             EXACT
positive physical output                   EXACT
score deficit <= X-minus mass              EXACT
measure-valued projection                  EXACT
survival/branch excess realization         EXACT
finite packet producer                     IMPORTED
Riemann Hypothesis                         UNPROVED
```
