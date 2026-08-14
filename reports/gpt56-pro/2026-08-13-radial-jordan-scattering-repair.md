# Radial Jordan/scattering repair after the PR #202 adversarial review

Date: 2026-08-13  
Frozen source head: PR #202 `6de0ecba3c0bb0fb4eafd15e0369ff8ae0e4ca69`

**RH remains unproved.**

## Correction

The atomic Radon–Nikodym unitary of `L-19874` is valid, but its displayed
triangular intertwiner is false:

\[
 \widetilde U V_\omega g(t,u)=m(u)g(u-t),
\]
while

\[
 V_\beta M_mg(t,u)=m(u-t)g(u-t).
\]

The correct identity is multiplication by `m(u)` after triangular lifting.
Thus the Jordan tail-Hankel block is not the ordinary-prime block with one input
multiplier.

## Exact replacement

The Jordan measure has the positive radial decomposition

\[
 d\omega^J_{a,c}(u)
 =\frac4{a^2}\int_0^a u\,d\beta_{b,c+2b}(u)db.
\]

This yields the first-chaos isometry

\[
 f(u)\mapsto\frac2a\sqrt u\,f(u)
\]
into the radial direct integral of ordinary-prime score spaces.

On the triangular source, `u=t+(u-t)` forces two carrier ports.  The exact
operator formula is

\[
 H_{\omega^J_{a,c}}
 =\frac4{a^2}\int_0^a
   [M H_{\beta_{b,c+2b}}+H_{\beta_{b,c+2b}}M]db.
\]

This is the proper constructive source chart.  It retains all carrier cross
terms and makes visible the output-carrier derivative omitted by `L-19874.20`.

## New frontier

For each radial fibre, attach the explicit ordinary-prime conditional-variance
Julia environment.  Then prove that the coherent radial integral of:

```text
output-carrier Julia port;
input-carrier Julia port;
radial connection;
gamma/pole completion;
theta/Brownian reserve;
compressed delays, both orientations and bridge
```

is one conservative completed source whose visible defect is the delayed Weil
form.

The radial integral must remain coherent; replacing it by an orthogonal sum and
dropping cross-`b` terms would overcount the Jordan source.

## Boundary

```text
atomic RN unitary                                  RETAINED EXACT
old triangular input intertwiner                   FALSE
positive radial prime mixture                      EXACT
first-chaos radial isometry                        EXACT
carrier-anticommutator tail-Hankel formula          EXACT
radial coherent Julia/Fisher completion             OPEN
completed defect = delayed Weil form                OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```
