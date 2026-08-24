# M-105430 — Hostile review contract for Xi critical-sign rigidity

Claim ID: `M-105430`  
Status: **BINDING REVIEW PROTOCOL**  
Created: 2026-08-24  
Depends on: `L-105430--L-105434`, `T-105430`  
RH status: **unproved**

Review in the following order.

## 1. Coordinate and safe-half-plane sign

Verify the centered convention

\[
\Xi(z)=\xi(1/2+iz)=\xi(1/2-iz)
\]

and therefore

\[
{\Xi^{(r)}(z)\over\Xi^{(r+1)}(z)}
=i{\xi^{(r)}(1/2-iz)\over\xi^{(r+1)}(1/2-iz)}.
\]

Recheck the uniform right-half-plane Bell-polynomial estimate and the sign

\[
\operatorname{Re}\bigl(\xi^{(r+1)}/\xi^{(r)}\bigr)>0.
\]

The uniformity in the complete vertical variable is load bearing.

## 2. Fixed-strip bounds and good sides

Re-derive:

```text
upper bound for Xi^(r) on every fixed physical strip;
lower bound for Xi^(r+1) on the positive safe line;
O_r(log X) zeros in every unit real interval;
a cofinal side with horizontal zero separation >=c/log X.
```

The Jensen center is `X+iA_r`, not the negative safe line.

In the paired Hadamard comparison, the sum in `L-105431.9` runs over both signs
and the factor `1/2` converts absolute distances to squared distances. Removing
that factor is an error.

## 3. Bottom boundary

At a simple pole,

\[
\operatorname{Im}{\rho_c\over x-c+iy}
={-\rho_c y\over(x-c)^2+y^2}.
\]

The sign is favourable exactly when `rho_c<=0`. Verify uniform convergence of
the remaining analytic term on each fixed compact bottom edge.

Multiple nonremovable critical points are not covered by this simple-pole
calculation. They must remain in the confluent ledger.

## 4. Rectangle harmonic measure

Recheck the separation-of-variables formula for the vertical-side harmonic
measure in

\[
(-X,X)\times(\varepsilon,H)
\]

and the bound

\[
\omega_{\rm side}(z_0)
\ll_{z_0,H}
\exp[-\pi(X-|\Re z_0|)/(H-\varepsilon)].
\]

The limit order is:

```text
fix X_n;
let epsilon down to zero;
then let n tend to infinity.
```

The side growth is `exp(O(log X loglog X))`, so its product with harmonic
measure tends to zero.

## 5. Global-versus-local firewall

`L-105432` assumes every zero of the derivative is real globally. It cannot be
applied to a finite-height moving-saddle endpoint as though that derivative
were globally real-rooted.

The finite-window Schur-complement theorem remains correct and its two blocks
remain independent. The new collapse is a global Xi-specific consequence of
completed-zeta growth and the complete critical hierarchy.

## 6. Herglotz saturation

Verify

\[
F(iy)/F'(iy)=O(i/\log y)
\]

and hence the Herglotz affine coefficient

\[
a=\lim_{y\to\infty}\operatorname{Im}\widehat m_F(iy)/y
\]

is zero. Real boundary continuation away from the discrete poles excludes a
continuous Herglotz measure. The source measure is therefore purely atomic.

## 7. Binding separator

The quartic

\[
z^4-z^2+1
\]

has all critical points real and positive imaginary-axis ratio, but the outer
critical residues equal `3/16>0`. Any proof omitting the residue sign is false.

## 8. Scientific boundary

```text
safe half-plane                                PROVED / REVIEW
subexponential good sides under critical reality PROVED CONDITIONAL / REVIEW
critical sign -> Pick/real-rootedness          PROVED CONDITIONAL / REVIEW
exact source saturation                        PROVED CONDITIONAL
complete Xi critical sign                      OPEN / RH-EQUIVALENT
finite-height-to-global descent                 OPEN
Riemann Hypothesis                              UNPROVEN
```
