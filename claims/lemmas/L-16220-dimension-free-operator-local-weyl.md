# L-16220 — Dimension-free operator-valued local Weyl scalarization

Claim ID: `L-16220`  
Status: **PROVED ABSTRACT THEOREM**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Depends on: the unconditional Riemann--von Mangoldt remainder

## 1. Purpose

`L-16210` stated a fold-admissible local Weyl theorem for a fixed packet. The
same argument is dimension-free when the profile density is measured directly
in operator norm and operator variation. No trace, row-sum or packet-size loss
is intrinsic.

This closes the abstract operator-valued local Weyl step on a growing radical
frame. The remaining source-specific question is whether the actual arithmetic
profiles satisfy the required operator-variation budget.

## 2. Growing profile space

For every `R>=2`, let `H_R` be a finite-dimensional Hilbert space, with dimension
allowed to grow arbitrarily. Let

```text
Phi_R(z):H_R->C                                           (L-16220.1)
```

be holomorphic for `|Im z|<=1/(2R)`. Define the positive operator density

```text
K_R(x,y)
 :=Phi_R(x-iy)^* Phi_R(x+iy),                             (L-16220.2)

H_R(x):=K_R(x,0)=Phi_R(x)^*Phi_R(x),                      (L-16220.3)
```

and the profile Gram

```text
D_R=(1/(2pi)) integral_R H_R(x)dx.                        (L-16220.4)
```

Assume the dimension-free Gram gate

```text
boxed:
0<cI<=D_R<=CI                                             (L-16220.5)
```

with constants independent of `R` and `dim H_R`.

## 3. Operator budgets

Assume

```text
L_R:=integral_R
 [1+|log(max(|x|,R^-1)/(2pi))|]
 ||H_R(x)||_op dx <=C_L.                                 (L-16220.6)
```

Let `|dH_R|_op` be the variation measure of the operator-valued function in
operator norm and put

```text
V_R:=integral_R
 [1+log(2+|x|)] |dH_R|_op(x).                            (L-16220.7)
```

For the horizontal displacement put

```text
U_R:=integral_R sup_(|y|<=1/(2R))
 ||partial_y K_R(x,y)||_op dx.                           (L-16220.8)
```

No coordinate basis and no entrywise estimate occurs.

## 4. Exact zero-side operator

Write every nontrivial zero as

```text
rho=beta+i gamma,
0<beta<1,                                                 (L-16220.9)
```

with multiplicity and the symmetric Weil convention. Define

```text
A_R=(1/R) sum_rho
 K_R(gamma/R,(beta-1/2)/R).                              (L-16220.10)
```

Under the declared integrability assumptions the sum is absolutely convergent.
Then there are self-adjoint operators `C_R,E_R` on `H_R` such that

```text
boxed:
A_R=(log R)D_R+C_R+E_R,                                  (L-16220.11)

||C_R||_op<=C_0,                                         (L-16220.12)

||E_R||_op
 <=C_1 [log(2R)/R][1+V_R+U_R].                           (L-16220.13)
```

The constants are independent of the dimension.

If

```text
boxed:
V_R+U_R=o(R),                                             (L-16220.14)
```

then

```text
boxed:
D_R^(-1/2)A_RD_R^(-1/2)
 =log R I+O_op(1)+o_op(log R),                            (L-16220.15)
```

and therefore

```text
boxed:
inf_a ||D_R^(-1/2)(A_R-aD_R)D_R^(-1/2)||_op/a ->0.       (L-16220.16)
```

This is the complete growing-frame scalarization required in `T-16204`.

## 5. Proof by scalar duality

For unit vectors `u,v in H_R`, define the scalar bounded-variation function

```text
h_(u,v)(x)=<u,H_R(x)v>.                                  (L-16220.17)
```

Then

```text
|h_(u,v)(x)|<=||H_R(x)||_op,                             (L-16220.18)

|dh_(u,v)|<=|dH_R|_op.                                   (L-16220.19)
```

Apply Stieltjes integration against the positive-ordinate counting function

```text
N(T)=T/(2pi)log(T/(2pi))-T/(2pi)+O(log(T+2)).            (L-16220.20)
```

The main density, after `T=Rx`, gives

```text
(log R)/(2pi) integral h_(u,v)(x)dx
 +(1/(2pi)) integral h_(u,v)(x)log(|x|/(2pi))dx.          (L-16220.21)
```

The first term is `<u,(log R)D_Rv>`, and the second defines `C_R`. Equation
(L-16220.6) gives the dimension-free bound (L-16220.12).

For the counting remainder `S(T)=O(log(T+2))`, Stieltjes integration by parts
gives

```text
|(1/R) integral h_(u,v)(T/R)dS(T)|
 <=C log(2R)(1+V_R)/R.                                   (L-16220.22)
```

The bound is uniform in `u,v`; taking the supremum proves the corresponding
operator-norm estimate.

For the horizontal displacement, the mean-value theorem gives

```text
||K_R(x,(beta-1/2)/R)-K_R(x,0)||_op
 <=(1/(2R))sup_(|y|<=1/(2R))
   ||partial_yK_R(x,y)||_op.                             (L-16220.23)
```

The elementary zero-density upper bound then yields

```text
||horizontal error||_op
 <=C log(2R)(1+U_R)/R.                                   (L-16220.24)
```

Combining (L-16220.22)--(L-16220.24) proves
(L-16220.11)--(L-16220.13). Whitening with (L-16220.5) proves
(L-16220.15)--(L-16220.16). QED.

## 6. No hidden dimension factor

The proof never sums matrix entries and never takes a trace. All estimates are
performed after testing against arbitrary unit vectors. Thus packet dimension
enters only through the actual sizes of

```text
D_R^(-1), V_R, U_R, L_R.                                 (L-16220.25)
```

If a frame change `U_R` has condition number `kappa_R`, the safe transported
budgets may acquire powers of `kappa_R`; `L-16218` bounds those powers by
polylogarithms. There is no additional unavoidable factor `dim H_R`.

## 7. Important limitation

Condition (L-16220.14) is substantive. A superposition of two stationary
branches can have a bounded Gram but operator variation `Theta(R)` because of
rapid cross interference. `R-16203` gives an exact counterexample. Therefore an
Airy fold estimate for each branch separately does not automatically verify
this theorem for the unsplit arithmetic tail.

Valid ways to close the source-specific gate include:

1. prove that only one stationary branch survives after exact source repair;
2. prove cancellation of the cross branch against the zero measure by a stronger
   exponential-sum theorem;
3. impose endpoint-jet conditions that suppress the far stationary branch;
4. replace variation by a proof-grade oscillatory operator estimate tailored to
   the actual phase.

## 8. Proof boundary

This abstract theorem is unconditional and dimension-free. It does not prove
that the CCM/Dunster arithmetic profiles satisfy (L-16220.6)--(L-16220.14), and
it does not prove RH.
