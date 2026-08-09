# L-34405 — The compact Q=4 full three-jet reconstruction has only strictly delayed gauges

Claim ID: `L-34405`

Status: **PROPOSED COMPLETE EXACT THREE-JET ROUTING THEOREM — INDEPENDENT REVIEW REQUIRED**

Created: 2026-08-09

Dependencies: `L-34401`, PR #342 `L-34003/L-34006`

Scope: exact zeroth/first/second source-jet reconstruction of the compact Q=4 innovation from the parity pair.  It proves that every derivative gauge is strictly delayed.  It does not by itself prove a curvature upper bound, a global recurrence, or RH.

## 1. Finite source reconstruction

Retain the common odd Euler core

\[
\mathcal O(s)=\prod_{p\ {m odd}}(1-p^{-s}),
\qquad z=2^{-s},
\qquad L=\log2,
\]

and the parity sources

\[
B_+(s)=p(z)\mathcal O(s),
\qquad
B_-(s)=p(-z)\mathcal O(s).
\]

Let

\[
B_0(s)=\frac1{\zeta(s)}=(1-z)\mathcal O(s)
\]

be the ordinary Möbius source and

\[
B_\circ(s)=T(z)\mathcal O(s),
\qquad
T(z)=(1-z)(1-4z^2)
\]

the compact Q=4 source.

`L-34401` supplies explicit finite polynomials `W_+,W_-` such that

\[
\boxed{
B_\circ=W_+B_+ +W_-B_-.
}
\tag{L-34405.1}
\]

It also supplies a polynomial `R_H` satisfying the exact first-gauge identity

\[
\boxed{
\dot W_+B_+ +\dot W_-B_-
=LzR_H(z)B_0,
}
\tag{L-34405.2}
\]

where a dot denotes differentiation in `s`.  Every monomial on the right contains at least one factor `z`, hence at least one delay `log 2` in critical logarithmic coordinates.

## 2. First jet

Write

\[
q_\star=B_\star'(s)
\]

for `star in {circ,+,-,0}`.  Differentiating (L-34405.1),

\[
\boxed{
q_\circ
=W_+q_+ +W_-q_- +G_1,
\qquad
G_1=LzR_H(z)B_0.
}
\tag{L-34405.3}

Thus the only part not passing through the same finite synthesis filters `W_+-` is a strictly delayed ordinary-Möbius bare-source gauge.

This recovers the source classification of `L-34401`.

## 3. Second jet

Put

\[
t_\star=B_\star''(s).
\]

Differentiate (L-34405.3):

\[
\boxed{
\begin{aligned}
t_\circ={}&W_+t_+ +W_-t_-\\
&+\dot W_+q_+ +\dot W_-q_-\\
&+G_1'.
\end{aligned}}
\tag{L-34405.4}

Because `z'=-Lz`, differentiating the explicit gauge gives

\[
\boxed{
G_1'
=LzR_H(z)q_0
-L^2z\bigl(R_H(z)+zR_H'(z)\bigr)B_0.
}
\tag{L-34405.5}

Likewise

\[
\boxed{
\dot W_\pm(z)=-LzW_\pm'(z).
}
\tag{L-34405.6}

Every term on the second and third lines of (L-34405.4) therefore has an explicit factor `z`.

Consequently the complete second jet has the exact routing

```text
same finite parity synthesis:
    W_+ t_+ + W_- t_-;

strictly delayed parity-current gauges:
    -L z W_+' q_+ - L z W_-' q_-;

strictly delayed ordinary-Mobius current gauge:
    L z R_H q_0;

strictly delayed ordinary-Mobius bare gauge:
    -L^2 z (R_H+zR_H') B_0.
```

There is **no new zero-delay second-current source**.

## 4. The actual Q=4 scale-innovation jets

The compact source is also the one-step source difference

\[
B_\circ=(1-4^{-s})B_4.
\]

Put

\[
x=4^{-s},
\qquad
L_4=\log4=2L.
\]

Let

\[
b_4=B_4,
\qquad q_4=B_4',
\qquad t_4=B_4''
\]

in multiplier notation.  Direct differentiation gives

\[
\boxed{
q_\circ
=(1-x)q_4+L_4x b_4,
}
\tag{L-34405.7}
\]

and

\[
\boxed{
t_\circ
=(1-x)t_4+2L_4xq_4-L_4^2x b_4.
}
\tag{L-34405.8}

Define the actual source-difference jets used by the aligned Q=4 innovation ledger,

\[
\boxed{
 i_\circ=(1-x)q_4,
\qquad
 t_\circ^{\rm rel}=(1-x)t_4.
}
\tag{L-34405.9}
\]

Then

\[
\boxed{
 i_\circ=q_\circ-L_4x b_4,
}
\tag{L-34405.10}
\]

and

\[
\boxed{
 t_\circ^{\rm rel}
=t_\circ-2L_4xq_4+L_4^2x b_4.
}
\tag{L-34405.11}
\]

Thus passing from the own compact first/second derivatives to the **actual scale-innovation jets** introduces only scale-four delayed Q=4 bare/current gauges.

## 5. Complete three-jet source classification

Combine Sections 1--4.  The actual Q=4 compact innovation through second order has the following complete source routing:

```text
current block / finite predecessor window:
    the same explicit parity synthesis W_+, W_- applied to
    the parity bare/current/second-current jets;

strict dyadic predecessors:
    parity first-current gauges from z W_+-';
    ordinary-Mobius current from z R_H q_0;
    ordinary-Mobius bare source from z(R_H+zR_H')B_0;

strict scale-four predecessor:
    Q=4 bare/current gauges x b_4 and x q_4.
```

Every gauge outside the parity second-jet synthesis is delayed by at least `log 2`; the final Q=4 conversion gauges are delayed by `log 4`.

No source species remains untyped:

```text
parity pair;
ordinary Mobius boundary/current;
Q=4 bare/current predecessor.
```

All three already occur in the live source/reserve/scattering graph.

## 6. Curvature consequence and exact limitation

The matching parity augmented state on PR #329 has curvature

\[
\mathcal A_{\rm pair}
=\mathcal R_{\rm pair}
 +Q_+^2+Q_-^2
 -Y_+T_+-Y_-T_-.
\]

PR #346 `L-34402` and PR #329 `L-32306` already give the coefficient-one local absorption

\[
2\|q_\circ\|^2
\le \mathcal A_{\rm pair}+\text{fixed collar}.
\]

The present theorem shows that the *second-current terms required by the same curvature calculation* introduce no new current-scale source.  They are the same parity second jets plus strict predecessor gauges.

This removes the possible obstruction

```text
first-current frame closes,
but differentiating once more creates a new same-scale source.
```

It does **not** yet prove that the signed curvature produced by (L-34405.4) is bounded above by the parity curvature.  Curvature is not monotone under an arbitrary contractive synthesis, and that sign must still be supplied by an exact Hermitian/energy identity.

The remaining target is now narrower:

> place the finite three-jet reconstruction (L-34405.1)--(L-34405.6) inside one source-matched Hermitian curvature ledger and show that every term outside the matching parity curvature is a strict predecessor state or a nonnegative dissipation.

## 7. Proof boundary

Closed exactly:

1. zeroth-order compact/parity finite synthesis;
2. first derivative with a delayed Möbius bare gauge;
3. second derivative with only delayed parity-current and Möbius current/bare gauges;
4. exact relation between own compact jets and the actual Q=4 scale-innovation jets;
5. proof that no new zero-delay source species appears through second order.

Still open:

1. Hermitian sign/no-double-spend for the complete three-jet curvature;
2. coefficient-one delayed recurrence for the matching augmented curvature state;
3. global subexponential energy;
4. RH.
