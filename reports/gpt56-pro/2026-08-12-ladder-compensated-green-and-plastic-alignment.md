# Gamma-ladder, compensated Green, and plastic-aligned continuation

Date: 2026-08-12  
Branch: `research/gpt56-pro/91411-ladder-compensated-green`  
Parent head: `ab71aa1fe0b1fd192011bbf40f032d2f42889ea0`  
RH status: **unproved**

## Executive summary

This continuation attacked the two obligations left by `L-91410`:

```text
factor the singular continuous completed source on the full delayed packet;
turn the remaining signed source into an explicit coefficient-one operator gate.
```

The continuous source factorization is now closed exactly.  A second exact
source chart rewrites Nakamura's archimedean completion as a positive gamma
ladder minus one pole channel.  A distinguished safe scale aligns the only
continuous density switch with the only switch of the Cauchy residual, making
the complete nonprime scalar channel a positive Levy increment.

Two tempting shortcuts were then killed adversarially:

```text
one rank-one pole at one scale does not make the three-scale delayed form
finite-index;

an absolutely continuous aligned reserve cannot dominate the prime atomic
sampling norm on the complete carrier span.
```

The final object is CPPD, an explicit coupled production-port domination.  It
remains open and RH-equivalent relative to the corrected fixed-scale form-core
interfaces.

## I. Gamma ladder minus one pole

For `sigma>1`, Nakamura's continuous density satisfies

\[
 \frac{e^{-\sigma u}}u
 \left[\frac1{1-e^{-2u}}-(1+e^u)\right]du
 =\sum_{m\ge1}\frac{e^{-(\sigma+2m)u}}u du
  -\frac{e^{-(\sigma-1)u}}u du.
\]

Hence the full source is

```text
ordinary prime atoms
+ positive gamma ladder
- one positive pole measure.
```

For

\[
 r_\alpha(t)=\frac1{\alpha-it}-\frac1{\alpha+it},
\]

the completed phase derivative is exactly

\[
 \partial_\sigma\log\frac{\xi(\sigma+it)}{\xi(\sigma-it)}
 =\chi_\sigma^{\rm p}(t)
  +\sum_{m\ge1}r_{\sigma+2m}(t)
  -r_{\sigma-1}(t).
\]

Each Hardy compression of `Theta_sigma r_alpha` is rank one:

\[
 P_-M_{\Theta_\sigma r_\alpha}P_+f
 =i\Theta_\sigma(i\alpha)
  \frac{f(i\alpha)}{t-i\alpha},
\]

with norm

\[
 \frac{|\Theta_\sigma(i\alpha)|^2}{2\alpha}|f(i\alpha)|^2.
\]

The weights are explicit safe xi ratios.  This is `L-91411`.

## II. Compensated Wick-Green identity

The short continuous source has density asymptotic to `du/(2u)`.  Uncentered
endpoint vectors therefore have infinite norm.  The exact abstract repair is:

\[
 \tilde U=U-\chi C,
 \qquad
 \tilde V=V-\chi C,
 \qquad
 J=\int(\tilde U+\tilde V)d\mu,
\]

followed by

\[
\begin{aligned}
 K^{\rm comp}
={}&\operatorname{Gram}(\tilde U-\tilde V)
 +\operatorname{Gram}(C-J)\\
&-\operatorname{Gram}(\tilde U)
 -\operatorname{Gram}(\tilde V)
 -\operatorname{Gram}(C)
 -\operatorname{Gram}(J).
\end{aligned}
\]

### Hostile correction inside the proof

The first draft attempted to reuse the safe prime mode split.  That was wrong:
its individual mode vectors do not share a common trace at `u=0`.  Corrected
`L-91412` instead uses, on the bounded short-jump interval,

\[
 U_i(u)=S_uf_i,
 \qquad
 V_i(u)=f_i,
 \qquad
 C_i=f_i.
\]

Since each physical Cauchy state is in `H1`,

\[
 \|S_uf_i-f_i\|_2\le u\|f_i'\|_2,
\]

which is square integrable against `du/u`.  The long channel remains in the
safe mode-split spaces because it is supported away from zero.

The resulting full continuous ledger is

\[
\begin{aligned}
 K^{\rm cont}
={}&\operatorname{Gram}(S_uf-f)
 +\operatorname{Gram}(C-J)\\
&+\operatorname{Gram}(U^-)+\operatorname{Gram}(V^-)\\
&-\operatorname{Gram}(C)-\operatorname{Gram}(J)
 -\operatorname{Gram}(D^-).
\end{aligned}
\]

It holds on the complete carrier/delay/orientation/bridge packet.

## III. Plastic alignment

The continuous sign switch is at

\[
 \kappa=\log\varpi,
 \qquad
 \varpi^3-\varpi-1=0.
\]

The dimensionless Cauchy residual

\[
 R(s)=-\frac14(1+s)e^{-s}
 +\frac{17}{32}(1+2s)e^{-2s}
 -\frac1{16}(1+4s)e^{-4s}
\]

has exactly one switch.  Writing

\[
 R(s)=e^{-s}(1+s)(H(s)-1/4),
\]

one obtains

\[
 H'(s)=
 -\frac{s e^{-3s}}{32(1+s)^2}
 [(34s+51)e^{2s}-(24s+30)]<0.
\]

The unique root is

\[
 \tau_*=1.164606978873629364392900917962\ldots .
\]

Set

\[
 a_\diamond=\tau_*/\kappa
 =4.1415673607530469520\ldots .
\]

Then

\[
 B(u)\mathfrak r_{a_\diamond}(u)\ge0
\]

for all `u>0`.  Consequently the nonprime recurrence increment is a positive
Levy form:

\[
 \mathcal A_{a_\diamond}(x)-\mathcal A_{a_\diamond}(0)
 =\int(1-\cos xu)d\omega_\diamond(u)\ge0.
\]

Every prime residual coefficient has one sign because

\[
 \log2>\kappa.
\]

The scalar recurrence becomes

\[
 \mathcal R_\diamond(x)
 =\mathcal R_\diamond(0)
  +\int(1-\cos xu)d\omega_\diamond(u)
  -\sum_nc_n(1-\cos(x\log n)),
\]

with `c_n>0` and retained anchor

\[
 \mathcal R_\diamond(0)
 =0.0003991664044248951\ldots>0.
\]

## IV. Atomic-isolation firewall

The natural full-Gram guess

\[
 \int|F|^2d\omega_\diamond
 \ge\sum_nc_n|F(\log n)|^2
\]

is false.  For any chosen atom `u0=log n0`, the Fejer packet

\[
 A_T(u)=T^{-1}\int_0^Te^{ix(u-u_0)}dx,
 \qquad
 F_T(u)=A_T(u)-A_T(0),
\]

lies in the closure of the carrier-defect span and satisfies

\[
 \|F_T\|_{L^2(\omega_\diamond)}\to0,
 \qquad
 \|F_T\|_{L^2(\sum c_n\delta_{\log n})}^2\to c_{n_0}>0.
\]

Finite Riemann sums give strict failures on finite carrier packets.  This is
`R-91405`.

Therefore the endpoint and connection ports in the final theorem are
structurally necessary.  They are precisely what prevents prime-atom
isolation.

## V. Final exact source identity

Let `P_a` be the positive production ledger:

```text
prime jump production;
short translation production;
C-J compensation production;
long endpoints;
delay leakage;
reflected and bridge copies.
```

Let `N_a` be the adverse ledger:

```text
prime endpoints;
C and J;
long jump production;
reflected and bridge endpoint copies.
```

Let `C_a^lambda` be the explicit deterministic connection from the six safe
xi-log-derivative jets and the compensation connection.  Then

\[
 \boxed{
 \mathbb K_a^{\rm del}
 =\mathcal C_a^\lambda+\mathcal P_a-\mathcal N_a.
 }
\]

The remaining theorem is

\[
 \boxed{
 \mathcal C_a^\lambda+\mathcal P_a
 \succeq\mathcal N_a.
 }
\]

This is `CPPD_a` in `T-91402`.

## VI. Relation to the Zeta23 finite-compression result

Claude's Zeta23 theorem extracts unconditional proportions from one finite
critical-density Gabor compression using inertia and two trace moments.  It
explicitly does not assert positivity of the full Weil form.  The present
atomic-isolation firewall is the complementary full-resolution fact: once all
carriers are admitted, the atomic prime channel can be separated from an
absolutely continuous reserve.  The final proof must retain the coupled
source geometry instead of comparing marginal measures.

## VII. Verification

Retained verdict:

```text
PASS_LADDER_COMPENSATED_GREEN_ALIGNMENT
```

Selected controls:

```text
gamma-ladder identity error      2.2639e-72
rank-one secondary singular      2.6231e-17
Hardy norm formula error          0
aligned scale                     4.141567360753047
aligned increment errors          <1.4e-73
full recurrence anchor            3.9916640442489516e-4
Fejer continuous norm, T=320      2.8423095579433486e-5
Fejer atomic norm, T=320          5.930743269605442e-4
target c2 weight                  5.980231539132879e-4
```

The replay proves one finite compensated identity exactly and checks analytic
identities numerically.  It does not prove CPPD or RH.

## Exact boundary

```text
gamma-ladder/pole source chart                    EXACT
one-rung Hardy rank-one formula                   EXACT
short continuous compensation                     EXACT
full continuous packet source factorization       EXACT
plastic-aligned scalar Levy increment              EXACT
uncoupled full-packet sampling                     REFUTED
complete source identity                           EXACT
CPPD                                               OPEN / RH-EQUIVALENT
Riemann Hypothesis                                 UNPROVED
```
