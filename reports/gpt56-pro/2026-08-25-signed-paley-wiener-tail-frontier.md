# Signed Paley–Wiener tail frontier after the remote-publication audit

## Remote audit

The former PR description reported `T-106300/T-106310` artifacts that were not
present at head `50cf8ef3419b88c33b11de4b538192c5ad6a36e9`.  The replacement chain is now
remote under `L/T-106400--106430`, with retained replays and source locks.

## Surviving endpoint architecture

The two reverse--Rolle rungs telescope to one endpoint all-pass quotient.  Its
denominator cancels on denominator-multiplied observations, leaving the linear
Turán numerator

\[
2i\lambda(\Xi\Xi'''-\Xi'\Xi'').
\]

The actual Xi Fourier kernel gives the unconditional exterior-square density

\[
\widehat{\Xi'^2-\Xi\Xi''}(\xi)
 =\frac12\int(2u-\xi)^2\Phi(u)\Phi(\xi-u)\,du\ge0.
\]

The finite positive/negative-frequency adapter pays the visible endpoint
Hankel energy by less than `1/600` of the zero-count scale.

## Why absolute coverage is not the sharp gate

For a companion pole `b=a+iy` of multiplicity `r`, the exact hard-band missed
trace is

\[
\sum_{q=0}^{r-1}\int_{2yH}^\infty e^{-t}L_q(t)^2\,dt.
\]

A simple pole at the live scale `yH=1/200` is missed by `exp(-1/100)>99/100`.
Therefore small shift plus small visible numerator cannot prove absolute
coverage in the ambient all-pass class.

The all-pass index is signed:

\[
-\operatorname{wind}U
 =\|H_U\|_{S_2}^2-\|H_{\bar U}\|_{S_2}^2.
\]

For the source projection `P`, this splits exactly into a visible signed charge
and a signed complement charge.  Large unobserved pole and zero energies may
cancel, and the zero count requires that cancellation to be retained.

## New exact gate

Define

\[
\Delta_T
 =\operatorname{tr}(P_T^\perp H_{U_T}^*H_{U_T}P_T^\perp)
 -\operatorname{tr}(P_T^\perp H_{\bar U_T}^*H_{\bar U_T}P_T^\perp).
\]

Then

\[
R_0\ge R_2-\frac1{600}N-(\Delta_T)_+-o(N).
\]

Since the pinned fixed-order input is `R_2/N>599/625-o(1)`, the exact remaining
ninety-percent threshold is

\[
\boxed{
\limsup\frac{(\Delta_T)_+}{N}<\frac{851}{15000}.
}
\]

For ninety-five percent it is `101/15000`.

This is a fixed constant signed relative-index estimate.  It is weaker than
`PWSAMP106420`, which asks for essentially complete absolute coverage.

## Status

```text
remote replacement packet                    PRESENT
confluent Laguerre coverage formula           PROVED EXACT
small-shift absolute-coverage shortcut        REFUTED GENERICALLY
signed source/complement index split          PROVED EXACT
visible endpoint source cost < 1/600          INHERITED PROVED
SIGNEDTAIL106430                              OPEN / RECORD-BEARING
ninety percent                               UNPROVED
density one / RH                             UNPROVED
```
