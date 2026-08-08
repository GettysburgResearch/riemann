# L-26205 — The continuum parabolic obstacle has zero boundary charge

Claim ID: `L-26205`  
Title: Tail majorization of the parabolic defect gives an explicit positive defect-to-slack transport with no loss of the sharp objective  
Status: **PROPOSED COMPLETE CONTINUUM THEOREM — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #260  
Dependencies: PR #265 `L-26202`; PR #248 `L-24520`; elementary one-dimensional transport  
Scope: continuum scale model only; the finite divisor-incidence transfer remains open

## 1. Continuum defect

Let

\[
 B(t)=2\sqrt t\left[
  \log{1\over t}-2(1-\sqrt t)
 \right],
 \qquad 0<t\le1,
\]

and

\[
 g(t)=-B'(t)={\log t+4\over\sqrt t}-4.
\]

The continuum response and critical target are

\[
 F(\theta)=\sum_{1\le k\le1/\theta}g(k\theta),
 \qquad
 h(\theta)=\theta^{-1/2}\log(1/\theta),
\]

and the signed defect is

\[
 E(\theta)=F(\theta)-h(\theta).
\tag{L-26205.1}
\]

PR #265 `L-26202` proves the two exact statements

\[
\int_0^1E(\theta)\,d\theta=0
\tag{L-26205.2}
\]

and

\[
\boxed{
 H(a):=\int_a^1E(\theta)\,d\theta\le0
 \qquad(0<a\le1).
}
\tag{L-26205.3}
\]

The second statement is strictly stronger than cancellation of the total
mass. It records the order in which positive defect and negative slack occur.

## 2. Positive and negative defect measures

Write

\[
 E(\theta)\,d\theta=d\mu_+(\theta)-d\mu_-(\theta),
\]

where

\[
 d\mu_+=E_+(\theta)d\theta,
 \qquad
 d\mu_-=E_-(\theta)d\theta.
\tag{L-26205.4}
\]

Equation (L-26205.2) gives equal finite total masses. Equation (L-26205.3)
gives, for every `a`,

\[
\mu_+([a,1])\le\mu_-([a,1]).
\tag{L-26205.5}
\]

Equivalently, the positive-defect measure is stochastically smaller than the
negative-slack measure.

Let `M` denote their common mass and let `Q_+,Q_-:[0,M]\to[0,1]` be their
right-continuous quantile functions. The tail order (L-26205.5) is equivalent
to

\[
\boxed{Q_+(s)\le Q_-(s)\qquad(0\le s\le M).}
\tag{L-26205.6}
\]

Thus the measure

\[
\pi=(Q_+,Q_-)_\#(ds)
\tag{L-26205.7}
\]

is a coupling of `mu_+` and `mu_-` supported on

\[
\boxed{0<u\le v\le1.}
\tag{L-26205.8}
\]

This is a completely explicit one-dimensional Strassen coupling; no compactness
or duality theorem is required beyond the quantile construction.

## 3. Positive incidence blocks cancel the complete continuum defect

For one coupled pair `(u,v)` with `u<=v`, let a positive continuum incidence
block of mass `dt` have constraint response

\[
-dt\,\delta_u+dt\,\delta_v.
\tag{L-26205.9}
\]

This is the continuum analogue of the exact finite constant block

\[
+t\,\mathbf1_{A<m\le B},
\qquad A<B,
\]

whose divisor-gradient response is

\[
-t\,\mathbf1_{q\mid A}+t\,\mathbf1_{q\mid B}
\]

in PR #248 `L-24520`.

Integrating (L-26205.9) against the coupling `pi` gives

\[
-\mu_++\mu_-=-E(\theta)d\theta.
\tag{L-26205.10}
\]

Therefore the transported response satisfies

\[
\boxed{
 E(\theta)d\theta
 +\int(-\delta_u+\delta_v)d\pi(u,v)
 =0.
}
\tag{L-26205.11}
\]

The entire signed defect is canceled before either sign is estimated.

Every transport block is positive in the physical carry coordinate. Hence the
continuum parabolic benchmark remains nonnegative throughout the deformation.

## 4. The sharp objective is not spent

A finite incidence block from `A` to `B>A` increases the carry objective by

\[
 t\log(B/A).
\]

The corresponding continuum objective gain is

\[
\log(v/u)\ge0.
\]

Consequently the complete transport has gain

\[
\boxed{
 \mathcal G_{\rm tr}
 =\iint_{u\le v}\log(v/u)\,d\pi(u,v)\ge0.
}
\tag{L-26205.12}
\]

In the loss convention used in several carry branches, this is a nonpositive
transport loss.

Thus the continuum parabolic certificate simultaneously has:

```text
nonnegative physical coordinates;
exact target response;
no loss of the sharp mass-four objective.
```

In particular the continuum analogue of the least affine boundary charge is
exactly zero.

## 5. What remains in the finite problem

The continuum theorem removes a possible analytic obstruction. The remaining
finite difficulty is entirely arithmetic and combinatorial:

1. the response of an integer interval block is a divisor-incidence dipole,
   not a pure column dipole;
2. endpoints must be rounded without separating repeated prime-power charges;
3. quotient-cell and floor-transition boundaries must be recombined before
   positive parts are taken;
4. the fixed-ratio Möbius shell must survive as a mandatory scalar mutation.

A valid finite proof must therefore lift the coupling `pi` to source-bound
integer blocks while proving that the unmatched affine charge is `X^o(1)`.
The exact affine completion of `L-26204` then absorbs that charge at cost
`X^o(1)`.

## 6. Finite transport target

The direct production target suggested by the continuum theorem is:

> For every `epsilon>0` and all sufficiently large `X`, construct a signed
> divisor-incidence deformation `H_X` of the canonical Green equality state
> such that
> \[
> V_Xb_X^{H}\le w_X
> \]
> and
> \[
> \max_m\bigl(b_X^{(0)}(m)-b_X^H(m)\bigr)_+
> \le C_\epsilon X^\epsilon.
> \tag{L-26205.13}
> \]

The deformation must be assembled from complete quotient cells and signed
endpoint dipoles before the maximum is taken. Equation (L-26205.13), followed
by `L-26204`, gives the sharp prime-ramp lower bound and RH.

This finite statement is not proved here.

## 7. Review boundary

Closed exactly in the continuum model:

- tail stochastic domination;
- the quantile defect-to-slack coupling;
- cancellation of the complete signed defect;
- positivity of every transport block;
- nonnegative objective gain;
- zero continuum affine charge.

Open:

- a source-bound integer/divisor lift with subpower unmatched charge;
- the cofinal prime-ramp estimate;
- RH.
