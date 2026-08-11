# R-91004 — The safe positive Stinespring measure cannot be continued naively to the critical boundary

Claim ID: `R-91004`  
Status: **EXACT VARIABLE/ABSCISSA FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91031`  
RH status: **unproved**

## 1. Two different boundary variables

The completed safe ratio used in `L-9506/L-91031` is

\[
 \frac{\xi(1+q)}{\xi(1+2a+q)}.
 \tag{R-91004.1}
\]

The critical Clark ratio is

\[
 \Theta_a\!\left(\frac12+ix\right)
 =\frac{\xi(1/2-a+ix)}{\xi(1/2+a+ix)}.
 \tag{R-91004.2}
\]

They are related by

\[
 q=-\frac12-a+ix.
 \tag{R-91004.3}
\]

Therefore taking the ordinary Hardy boundary `q->ix` of the positive safe measure in `L-91031` does **not** reach the critical Clark boundary. It merely samples

\[
 \frac{\xi(1+ix)}{\xi(1+2a+ix)},
\]

which remains in the classical safe region.

## 2. The stable Cauchy factor blocks ordinary continuation

The safe transfer contains

\[
 \frac1{(q+a)^2(q+2a)^2(q+4a)^2}.
 \tag{R-91004.4}

Its positive inverse-Laplace realization is a convolution of three Erlang densities. Its abscissa of ordinary exponential-moment continuation is bounded by the first pole

\[
 \boxed{q=-a.}
 \tag{R-91004.5}

But the critical substitution (R-91004.3) has real part

\[
 -\frac12-a<-a.
\]

Thus the positive Laplace realization encounters its first stable-state pole strictly before the desired critical line.

## 3. The arithmetic atoms have the same obstruction

The positive Green-removed measure contains the atoms

\[
 \sum_{n\ge2}\frac{F_{2a}(n)}n\delta_{\log n}.
\]

At the critical real displacement, an ordinary exponential moment would require

\[
 \sum_{n\ge2}
 \frac{F_{2a}(n)}n
 n^{1/2+a},
\]

which diverges. Positive convolution with the rational and beta/Gamma channels cannot create the cancellations needed to assign this moment.

Hence neither the arithmetic nor the stable-filter part admits the desired boundary as an ordinary positive-measure Laplace limit.

## 4. Consequence

The following implication is invalid:

```text
safe complete monotonicity / positive Stinespring measure
 -> ordinary boundary limit at q=-1/2-a+ix
 -> critical Cauchy-square Gram.
```

The final CJHI map must instead use a conservative analytic mechanism that permits pole/continuum cancellation before the boundary is taken. Legitimate possibilities include:

1. a unitary scattering colligation retaining both reflected states;
2. a Darboux/pole-null completion;
3. an indefinite-to-Hilbert Schur complement with its ground scalar retained;
4. an exact contour deformation whose residue ports are explicitly tracked.

The coefficient-one state and all hyperbolic residue channels must remain visible throughout.

This firewall does not refute the safe-side positivity theorems or the Cauchy recurrence. It forbids promoting them to RH by an ordinary Laplace-boundary argument.