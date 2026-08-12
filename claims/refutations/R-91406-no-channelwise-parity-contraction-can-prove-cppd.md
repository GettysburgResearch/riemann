# R-91406 — No channelwise parity contraction can prove CPPD

Claim ID: `R-91406`  
Status: **EXACT PHASE-RESONANCE FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91414`, `L-91415`, `R-91405`  
RH status: **unproved**

## 1. The tempting shortcut

After the Hadamard reduction, one may try to dominate the adverse even and odd
ports channel by channel, for example

\[
 E_{\rm p}^*E_{\rm p}\preceq C\,O_{\rm p}^*O_{\rm p}
 \tag{R-91406.1}
\]

or

\[
 O_-^*O_-\preceq C\,E_-^*E_-.
 \tag{R-91406.2}
\]

with one finite constant independent of the carrier packet.  Neither type of
uniform comparison is available on the complete translation range.

## 2. Exact scalar phase obstruction

At one jump length `u`, a carrier frequency `xi` gives endpoint phase

\[
 z=e^{i\xi u}.
\]

The squared parity amplitudes are

\[
 |E|^2=\frac{|1+z|^2}{2},
 \qquad
 |O|^2=\frac{|1-z|^2}{2}.
 \tag{R-91406.3}

Therefore

\[
 \frac{|E|^2}{|O|^2}
 =\cot^2\left(\frac{\xi u}{2}\right)
 \tag{R-91406.4}
\]

and

\[
 \frac{|O|^2}{|E|^2}
 =\tan^2\left(\frac{\xi u}{2}\right).
 \tag{R-91406.5}
\]

The first ratio diverges as `xi u -> 2 pi k`; the second diverges as
`xi u -> (2k+1)pi`.  Hence no finite `C` can make either (R-91406.1) or
(R-91406.2) valid on all carriers.

The extreme cases are already exact:

```text
T=I:   odd production vanishes, even endpoint survives;
T=-I:  even endpoint vanishes, odd production survives.
```

## 3. Finite packets do not remove the obstruction

The carrier set is continuous.  Given any finite collection of independent
connection coordinates, choose sufficiently many near-resonant carrier
packets and solve the finite homogeneous system that annihilates those
coordinates while retaining one parity resonance.  This is the parity version
of the Fejer atomic-isolation argument in `R-91405`.

Thus finitely many uncoupled scalar anchors cannot turn a channelwise parity
comparison into CPPD.

## 4. Consequence for the plastic domain wall

Plastic alignment removes the scalar sign mismatch of the continuous density,
but it does not remove the phase resonances (R-91406.4)--(R-91406.5).  The
short and long parity ports must be coupled through the full completed
connection and through the prime endpoint geometry.

The legal target is one joint contraction

\[
 E_{\rm p}\oplus(C+J)/\sqrt2\oplus O_-
 \longrightarrow
 \mathcal G_a\oplus
 O_{\rm p}\oplus T_{\rm sh}\oplus(C-J)/\sqrt2\oplus E_-
 \tag{R-91406.6}
\]

with all delays, orientations and the bridge retained.

## 5. Relation to the Claude compression lesson

The upstream Zeta23 argument succeeds precisely because it keeps the complete
finite Hermitian compression and uses inertia rather than attempting to sign
each zero or frequency separately.  The present firewall is the source-side
analogue: parity components that are individually unbounded relative to one
another may still admit a coupled full-matrix Schur complement.

## 6. Exact boundary

```text
Hadamard parity reduction                         EXACT
channelwise even <= odd                           FALSE
channelwise odd <= even                           FALSE
finite uncoupled anchor repair                     FALSE IN GENERAL
joint connection-aware parity contraction          OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```