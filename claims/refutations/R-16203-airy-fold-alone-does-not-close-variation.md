# R-16203 — An Airy fold alone does not give the required operator-variation bound

Claim ID: `R-16203`  
Status: **REFUTED AS A GENERAL INFERENCE**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Targets: the informal source-specific conclusion following `L-16210.29`

## 1. The overstrong inference

A nondegenerate fold has a local Airy scaling. It is tempting to infer that the
complete profile density has variation

```text
V_R=O(R^(1/3) polylog R)=o(R).                           (R-16203.1)
```

That conclusion is false without a one-branch or cross-cancellation theorem.
Away from the fold, one oscillatory integral typically has two stationary
branches. Each branch separately is regular, but their product contains a fast
interference phase whose variation is order `R`.

## 2. Exact scalar counterexample

Let `chi` be a nonzero smooth real cutoff supported in an interval on which
`psi'` is bounded away from zero. Define

```text
Phi_R(x)=chi(x)[exp(iR psi(x))+exp(-iR psi(x))].           (R-16203.2)
```

Each separate branch

```text
chi(x)exp(+-iR psi(x))                                   (R-16203.3)
```

has density `chi(x)^2`, whose variation is independent of `R`.

The full density is

```text
H_R(x)=|Phi_R(x)|^2
 =2chi(x)^2[1+cos(2R psi(x))].                            (R-16203.4)
```

On any subinterval where `chi=1` and `|psi'|>=c>0`,

```text
H_R'(x)=-4R psi'(x)sin(2R psi(x)).                        (R-16203.5)
```

A change of variables and the mean value of `|sin|` give

```text
boxed:
Var(H_R)>=c_1R                                            (R-16203.6)
```

for all sufficiently large `R`. At the same time,

```text
integral H_R(x)dx=2 integral chi^2+O(R^-1),               (R-16203.7)
```

so the scalar Gram remains uniformly positive and bounded.

Thus a uniformly nondegenerate Gram and individually harmless branches do not
imply the `o(R)` variation gate of `L-16220`.

## 3. Application to radial prolate tails

For the leading radial phase at `sigma=0`,

```text
phi(z)=sqrt(z^2-1)-omega log z.                           (R-16203.8)
```

In logarithmic position, the stationary-frequency map is

```text
omega(z)=z^2/sqrt(z^2-1).                                (R-16203.9)
```

It decreases from infinity to `2` on `(1,sqrt(2))` and increases from `2` to
infinity on `(sqrt(2),infinity)`. Therefore every frequency `omega>2` has two
stationary points. The Airy model controls their collision at `omega=2`; it does
not remove the two-branch interference for `omega>2`.

A fixed frequency window inside `(2,4/sqrt(3))` excludes stationary points from
Poisson aliases `k>=2`, as proved in `L-16212`, but it still contains the two
stationary points of the first alias. Hence the single-alias window by itself
does not prove (R-16203.1).

## 4. Horizontal-strip consequence

The same phenomenon can occur in

```text
K_R(x,y)=Phi_R(x-iy)^*Phi_R(x+iy).                        (R-16203.10)
```

Differentiating in `y` multiplies the cross phase by its local complex frequency.
Thus an Airy pointwise bound also does not automatically give

```text
U_R=o(R).                                                 (R-16203.11)
```

The horizontal-displacement budget must be proved for the full combined profile,
not inferred from the size of one Airy neighborhood.

## 5. Correct alternatives

The operator local Weyl theorem remains valid. Its source-specific hypothesis
can be discharged by any of the following genuinely stronger inputs:

1. **one-branch reduction:** prove that one radial stationary branch is lower
   order after exact normalization;
2. **branch-resolved zero estimate:** control the cross phase directly against
   the zero-counting measure, beyond the absolute `O(log T)` remainder;
3. **endpoint-jet suppression:** modify the exact-radical source so that the far
   branch loses additional inverse powers; see `L-16221`;
4. **phase-adapted operator theorem:** retain oscillation in the Stieltjes error
   instead of charging total variation.

## 6. Corrected status

```text
L-16210/L-16220 abstract local Weyl theorem: PASSED
local Airy normal form:                                 PASSED
Airy fold => full V_R+U_R=o(R):                         REFUTED GENERALLY
source-specific CCM profile gate:                       OPEN
```

This correction prevents the positive route from treating a local turning-point
estimate as a complete global profile theorem. No RH conclusion is affected,
because the profile gate had not been promoted.
