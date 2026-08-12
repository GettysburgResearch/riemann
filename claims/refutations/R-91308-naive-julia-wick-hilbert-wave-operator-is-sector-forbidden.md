# R-91308 — A naive Julia–Wick Hilbert wave operator is forbidden by product-sector disjointness and the pole bridge

Claim ID: `R-91308`  
Status: **EXACT ARCHITECTURAL REFUTATION / CORRECTION TO T-91305–T-91306**  
Created: 2026-08-12  
Depends on: `L-91327`–`L-91330`  
RH status: **unproved**

## 1. The tempting construction

The first Julia–Wick proposal suggested the following sequence:

```text
form the safe primewise lossless Julia cascade;
select the normalized all-detail inverse corner;
complete it in the same prime Fock vacuum;
append independent gamma/theta/Brownian/p=2 ports;
take the critical-line limit as a bounded or partial-isometric wave operator.
```

This construction is impossible.

## 2. Sector obstruction

`L-91327` proves that the normalized inverse product lies in the vacuum incomplete tensor sector exactly for

\[
 \sigma>\frac12+\omega.
\]

At the critical Xi line \(\sigma=1/2\) it is disjoint for every \(\omega>0\). Moreover, its nontrivial log-translates are mutually disjoint in the Kakutani sense, so the physical translation group is not implemented by the product unitaries in that sector.

Tensoring with a fixed independent archimedean Hilbert space cannot change inequivalence after restriction to the prime algebra.

## 3. Orientation obstruction

`L-91329` proves

\[
 \mathcal T_{d_\omega}A_\omega
 =\mathcal JF_\omega.
\]

Thus the all-detail inverse maps the interacting Suzuki Green vector to the free endpoint vector. It is the deconvolution output, not the forward producer of the interacting Hardy vector.

## 4. Hard-range pole obstruction

`L-91330` proves

\[
 e^{-t/2}\mathcal JF_\omega(e^t)
 \sim
 \frac{C_{0,\omega}}{1-\omega}
 e^{(1/2-\omega)t}.
\]

Therefore this free endpoint is not in \(L^2\) for \(0<\omega\le1/2\). The full forward Jordan channel cancels this mode through the exact zero of

\[
 \frac{\zeta(s-\omega)}{\zeta(s+\omega)}
\]

at \(s=1-\omega\). Removing the forward channel reintroduces the instability.

## 5. Finite-cutoff obstruction

At a finite prime cutoff the pole coefficient is multiplied by

\[
 C_{\omega,P}(1-\omega),
 \qquad
 \log C_{\omega,P}(1-\omega)
 \sim
 \frac{P^{2\omega}}{2\omega\log P}.
\]

Thus finite Euler products amplify the unstable bridge; they do not approximate the analytic zero that cancels it.

## 6. Correct conclusion

The exact all-prime inverse remains useful as a cylinder distribution, but a valid completion must be:

```text
unbounded rather than bounded on the source side;
sector-changing rather than a same-vacuum strong limit;
entangled across the complete prime tail and the archimedean bridge;
formed before taking the Hilbert norm;
translation-covariant only after the completed output is constructed.
```

Accordingly, `T-91306` may survive only after replacement by the entangled pole-bridge theorem `T-91307`. Any claimed proof using the naive product Hilbert limit is rejected.
