# Suzuki completed Jordan–Hankel source lock — 2026-08-12

## Primary source

Masatoshi Suzuki, **A canonical system of differential equations arising from the Riemann zeta-function**, RIMS Kôkyûroku Bessatsu B34 (2012), 397–435; arXiv:`1204.1827v2`.

The official arXiv record inspected for this packet reports submission on 2012-04-09 and revision v2 on 2016-09-23.  Exact theorem numbering follows that source.

## Imported statements

The local files import only the following source-level facts.

1. For `omega>0`,
   ```text
   Theta_omega(z)=xi(1/2-omega-i z)/xi(1/2+omega-i z).
   ```
2. For `omega>=1/2`, `Theta_omega` is a meromorphic inner function in the upper half-plane unconditionally; more generally Suzuki states the exact zero-free-region equivalence for the family.
3. Suzuki's generalized-Jordan coefficients are
   ```text
   c_omega(n)=n^omega product_(p|n)(1-p^(-2 omega)).
   ```
4. Suzuki gives an explicit compactly supported archimedean kernel `g_omega` and the completed multiplicative impulse
   ```text
   h_omega(x)=x^(-1) sum_(n<=x)c_omega(n)g_omega(n/x).
   ```
5. The shifted Mellin transform of `h_omega` is `Theta_omega`.
6. The multiplicative Hankel operator
   ```text
   (H_omega f)(x)=int_0^infinity h_omega(xy)f(y)dy
   ```
   extends to an isometry on `L^2(0,infinity)` in the unconditional safe range, and its Mellin action is multiplication by `Theta_omega` followed by reflection.
7. Functional-equation symmetry gives `Theta_omega(z)Theta_omega(-z)=1`; hence the isometric extension is a unitary involution.

## Repository identification

The exact identity

```text
c_a(n)=n^a q_a(n),
q_a(n)=product_(p|n)(1-p^(-2a))
```

identifies Suzuki's arithmetic coefficient sequence with the generalized-Jordan source of main `L-91014`, `L-91029` and branch `L-91030`.

This supports the local conclusion that Suzuki's `H_a` is the explicit completed **amplitude-level** Jordan/gamma/two-sided-Hardy scattering operator.

## Statements not imported

No source status transfers to the following local additions:

- the scalar Cauchy mother or its refutation;
- the delay-fibre form-core repair;
- the Poisson first-chaos reduction;
- the normalized Jordan radial-curvature Gram;
- the fixed-scale delayed screw criterion;
- CDFHTI or any positive tangent lift;
- any proof of RH.

Suzuki's unitary amplitude intertwining does not assert positivity of the radial Wigner–Smith curvature.  The latter distinction is local `R-91009` and is load bearing.

## Review boundary

```text
Suzuki innerness/Hankel/Mellin statements       IMPORTED PRIMARY-SOURCE THEOREMS
Jordan coefficient identification               EXACT LOCAL ALGEBRA
amplitude-level source completion                CLOSED
positive tangent/curvature completion            OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVED
```
