# M-105600 — Hostile review contract for the phase/anti-Poisson/shell synthesis

Claim ID: `M-105600`  
Status: **BINDING REVIEW CONTRACT**  
Created: 2026-08-24  
Applies to: `L-105600--L-105603`, `R-105600`, `T-105600`  
RH status: **unproved**

A reviewer should check the packet in the following order.

## 1. Phase-barycenter algebra

Verify directly from the Herglotz representation that

```text
P_z is a probability law;
omega_z has unit modulus;
y f'(z)/Im f(z) = E omega_z;
1-Re d = (1/2)E|omega-1|^2;
1-|d|^2 = (1/2)E|omega-omega'|^2.
```

The atom at infinity representing the affine coefficient must be retained.
Dropping it invalidates the probability normalization and moving-base formula.

## 2. Moving-base normalization

Check that physical scale and distance above the extremal base are distinct:

```text
h = physical scale from the lower base;
delta = downward base displacement;
y = h-delta = distance above the Pick base.
```

Equation `C_b<=0 iff Re d<=y/(y+delta)` is load bearing. Replacing `y` by `h`
would erase the anti-diffusive factor.

## 3. Backward-Poisson sign

Recompute the signed kernel

```text
[delta x^2-(2h-delta)(h-delta)^2]
/[2(x^2+(h-delta)^2)^2]
```

and the Fourier multiplier

```text
-(pi/2)(1+h|xi|)exp(-(h-delta)|xi|).
```

The top-base multiplier has `exp(-h|xi|)`, so the lower-base field is
`exp(delta|D|)` times the top-base field only when the affine Herglotz
coefficient vanishes. For Xi that vanishing uses the completed-zeta safe
asymptotic and must not be silently generalized.

## 4. Finite-measure firewall

Check the large-centre expansion

```text
C_h^[delta](a)=alpha delta/2 + delta mu(R)/(2a^2)+O(a^-3).
```

This proves failure for compactly supported finite measures. It does not prove
failure for the infinite Xi measure and must not be presented as an Xi
counterexample.

## 5. Height-shell winding orientation

For `p(x)=x`, the map `(x+ih)/(x-ih)` has winding `-1`. This pins all signs:

```text
deg Theta_(p,h)=-N_p(h);
deg S_(h1,h2)=-M_p(h1,h2);
deg U_k=M_(k+1)-M_k.
```

In finite rectangles the vertical endpoint term is load bearing. Only the
complete polynomial compactification has zero endpoint correction.

## 6. Half-derivative degree formula

The inequality used is

```text
-deg U <= sum_(n<0)|n||Uhat(n)|^2.
```

Ordinary `L2`, trace or Hilbert--Schmidt control cannot replace it. A narrow
Blaschke phase slip is the mandatory separator.

## 7. Safe-line coordinate

Verify the reflection map

```text
s*=1/2-i z=1/2+b+h-ia
```

and the functional-equation signs giving

```text
m_r(z)=i q_r(s*),
m_r'(z)=q_r'(s*),
-2C=Re(q_r-hq_r').
```

The frozen identity with nonnegative `b_L(n)` is not the full unfrozen Xi
identity. All archimedean, carrier-freezing and pole/seam errors remain in
`DMPXFER105603`.

## 8. Quantifier and conclusion audit

The packet proves exact identities and a finite polynomial shell theorem. It
does not prove:

```text
DMPXFER105603;
HSHE105602;
spatial-escape exclusion for Xi;
the moving-saddle theorem;
RH.
```

Any promotion requires an explicit physical error ledger below the phase gap
or the two-unit half-derivative threshold.
