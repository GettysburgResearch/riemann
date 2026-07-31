# L-16210 — Fold-admissible local Weyl scalarization

Claim ID: `L-16210`  
Status: **PROVED ABSTRACT ZERO-MEASURE THEOREM**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-07-31  
Depends on: the Riemann--von Mangoldt formula; the zero-side normalization of `L-16209`

## 1. Purpose

The first formulation of the normalized tail-profile route asked for a uniform
pointwise `C1` envelope after scaling by `R_lambda`. Radial prolate tails have a
fold in the map from logarithmic position to Mellin frequency. Standard cubic
stationary phase produces an Airy layer whose pointwise height and derivative
need not remain uniformly bounded.

Uniform `C1` control is unnecessary. The Stieltjes proof behind `L-16209` only
needs the matrix spectral density to have variation `o(R_lambda)`. This lemma
supplies the exact replacement.

## 2. Profile packet and Gram

Let `R>=2` and let

```text
Phi_R(z)=(Phi_(1,R)(z),...,Phi_(r,R)(z))                  (L-16210.1)
```

be a finite row-vector packet, holomorphic in

```text
|Im z|<=1/(2R).                                          (L-16210.2)
```

On the real line put

```text
H_R(x)=Phi_R(x)^* Phi_R(x),                               (L-16210.3)

D_R=(1/(2pi)) integral_R H_R(x) dx.                      (L-16210.4)
```

Assume the uniform Gram gate

```text
boxed:
0<cI<=D_R<=CI                                             (L-16210.5)
```

for constants independent of `R`.

## 3. Fold-admissible budgets

Assume the logarithmic moment bound

```text
L_R:=integral_R
 (1+|log(|x|/(2pi))|) ||H_R(x)|| dx <=C_L.               (L-16210.6)
```

Interpret the logarithm near zero as `log(max(|x|,1/R))`; changing this cutoff
modifies the final bounded matrix by `O(1)`.

Let `|dH_R|` be the total-variation measure of the Hermitian matrix function,
using any fixed finite-dimensional operator norm, and put

```text
V_R:=integral_R
 (1+log(2+|x|)) |dH_R|(x).                               (L-16210.7)
```

For the horizontal zero displacement define

```text
K_R(x,y)
 :=Phi_R(x-iy)^* Phi_R(x+iy),                             (L-16210.8)

U_R:=integral_R sup_(|y|<=1/(2R))
 ||partial_y K_R(x,y)|| dx.                              (L-16210.9)
```

The admissibility condition is only

```text
boxed:
V_R+U_R=o(R).                                             (L-16210.10)
```

No pointwise bound on `Phi_R'` is required.

## 4. Zero-side matrix

Use the same centered zero parameter and conjugation convention as in
`L-16209`. Thus, if a nontrivial zero is

```text
rho=beta+i gamma,
```

its scaled ordinate is `x=gamma/R` and its scaled horizontal displacement has
absolute value at most `1/(2R)`. Define the exact zero-side matrix

```text
A_R=(1/R) sum_rho K_R(gamma/R,(beta-1/2)/R),              (L-16210.11)
```

with the symmetric multiplicity convention of the Weil form.

Then there are Hermitian matrices `C_R,E_R` such that

```text
boxed:
A_R=(log R)D_R+C_R+E_R,                                  (L-16210.12)

||C_R||<=C_0,                                             (L-16210.13)

||E_R||
 <=C_1 (log(2R)/R)(1+V_R+U_R).                           (L-16210.14)
```

The constants depend only on the fixed packet size and the constants in the
Riemann--von Mangoldt remainder.

Consequently, under (L-16210.10),

```text
boxed:
||E_R||=o(log R).                                         (L-16210.15)
```

If `m_R,M_R` are the extreme generalized eigenvalues of `(A_R,D_R)`, then

```text
boxed:
m_R=log R+O(1)+o(log R),
M_R=log R+O(1)+o(log R),                                  (L-16210.16)

(M_R-m_R)/(M_R+m_R)->0.                                  (L-16210.17)
```

## 5. Proof: main density term

Write the zero-counting measure as

```text
dN(t)=dM(t)+dS(t),                                       (L-16210.18)
```

where the Riemann--von Mangoldt main term has density

```text
M'(t)=(1/(2pi))log(t/(2pi))+O(t^-2),                     (L-16210.19)
```

and

```text
S(t)=O(log(2+t)).                                         (L-16210.20)
```

For the line-centered values, the main term is

```text
(1/R) integral_0^infinity H_R(t/R)dM(t).
```

Putting `t=Rx` gives

```text
(log R)D_R
 +(1/(2pi)) integral H_R(x)log(|x|/(2pi))dx
 +O(R^-1).                                               (L-16210.21)
```

The second term is the bounded matrix `C_R`; (L-16210.6) gives
(L-16210.13).

## 6. Proof: Riemann--von Mangoldt remainder

Set

```text
F_R(t)=R^-1 H_R(t/R).                                     (L-16210.22)
```

Stieltjes integration by parts gives

```text
integral F_R dS=-integral S dF_R,                         (L-16210.23)
```

with boundary terms obtained by truncation and then removed using
(L-16210.6)--(L-16210.7). After `t=Rx`,

```text
||integral F_R dS||
 <=(C/R) integral log(2+R|x|)|dH_R|(x)
 <=C log(2R)(1+V_R)/R.                                   (L-16210.24)
```

This proves the `V_R` part of (L-16210.14).

## 7. Proof: horizontal displacement

For each zero, the mean-value theorem in the strip gives

```text
||K_R(x,(beta-1/2)/R)-K_R(x,0)||
 <=(1/(2R)) sup_(|y|<=1/(2R))
   ||partial_y K_R(x,y)||.                               (L-16210.25)
```

Applying the main zero-density bound to this nonnegative scalar majorant gives

```text
||(off-line shift error)||
 <=C log(2R)(1+U_R)/R.                                   (L-16210.26)
```

No RH assumption occurs: only `0<beta<1` is used. Equations
(L-16210.24)--(L-16210.26) prove (L-16210.14).

## 8. Spectral conclusion

Whiten by `D_R`. From (L-16210.5), boundedness of `C_R` and
`E_R=o(log R)` give

```text
D_R^(-1/2)A_RD_R^(-1/2)
 =log R I+O(1)+o(log R).                                 (L-16210.27)
```

The min--max principle proves (L-16210.16)--(L-16210.17). QED.

## 9. Fold scale

For a one-dimensional nondegenerate fold, cubic stationary phase has the local
form

```text
Phi_R(x)
 =R^(1/6) A(R^(2/3)(x-x_0))+lower-order terms.           (L-16210.28)
```

The corresponding product density has total variation `O(R^(1/3))`. Thus a
finite collection of folds with square-summable amplitudes satisfies

```text
V_R+U_R=O(R^(1/3) polylog R)=o(R).                       (L-16210.29)
```

This observation is not used as an imported theorem here; it records the exact
source-specific estimate now required from the radial prolate translation.

## 10. Improvement over the previous gate

`L-16209` remains valid under its stronger hypotheses. This lemma shows that the
source block does **not** require a uniformly bounded profile derivative.
Directed production may instead certify:

```text
profile Gram floor,
logarithmic L1 moment,
weighted matrix variation V_R,
horizontal-shift budget U_R.                             (L-16210.30)
```

An Airy spike is therefore not an obstruction to the RH route.
