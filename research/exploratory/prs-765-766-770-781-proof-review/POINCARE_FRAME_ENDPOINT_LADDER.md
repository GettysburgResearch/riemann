# Poincare-frame endpoint ladder

This is the front door for the third-pass source-normalized ladder theorem.

1. [Part I — source frame, energy saturation, pure period model, and exact centers](POINCARE_FRAME_ENDPOINT_LADDER_PART_I.md)
2. [Part II — far-block elimination, recentered determinant census, weak interlacing, and the strict subcritical regime](POINCARE_FRAME_ENDPOINT_LADDER_PART_II.md)
3. [Critical divisor-renewal transition](CRITICAL_DIVISOR_RENEWAL_TRANSITION.md)

## Main results

Let `L=L(k)` satisfy

\[
L(k)\log(k+2)=o(k).
\]

Using the exact source-normalized Poincare coefficient frame from PR #766,
every original nested determinant `D_i`, `i<=J<=L(k)`, has exactly one
simple real zero in a fixed disc about the exact one-mode center
`c_hat(k,J)`. The centers are separated by `12+o(1)`. The zeros weakly
interlace; equality is exactly the vanishing of the source Schur coupling
and corresponds to cancellation in the determinant quotient.

In the subcritical range

\[
L(k)^2\log(L(k)+2)=o(k),
\]

the coupling is `S_{J-i}(1+o(1))`, all inequalities are strict, and the
parent gap/residue laws hold in recentered form. If also
`L^2 log(k/L+2)=o(k)`, the centers return to `12J+o(1)`.

At the critical fixed-offset scale `J^2/k -> tau`, the effective coupling is

\[
g_h(\tau)
=-\frac{h}{24\tau}[z^h]
\exp\!\left[-24\tau
\sum_{r\ge1}\frac{\sigma_{-1}(r)}r z^r\right].
\]

Its zeros are the leading merger resonances. In particular
`g_2(tau)=3/2-24tau`, so the first exact resonance is `tau=1/16`.

All statements are proposed analytic theorems requiring independent review.
RH and GRH remain unproved.