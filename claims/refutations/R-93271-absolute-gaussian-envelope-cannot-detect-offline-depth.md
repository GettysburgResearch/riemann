# R-93271 - Absolute Gaussian prime envelopes cannot dominate a terminal off-line depth

Claim ID: `R-93271`
Status: **EXACT ASYMPTOTIC FIREWALL**
Created: 2026-08-16
Refutes: closure of First-Hermite positivity by coefficientwise absolute Gaussian majorants alone

For the First-Hermite prime kernel, the absolute all-integer envelope contains the exponent

\[
E_q(u)=\frac u2-\frac{u^2}{4q}.
\tag{R-93271.1}
\]

Completing the square gives

\[
E_q(u)=\frac q4-\frac{(u-q)^2}{4q},
\tag{R-93271.2}
\]

so

\[
\boxed{\sup_{u\ge0}E_q(u)=\frac q4.}
\tag{R-93271.3}
\]

A terminal off-line zero of horizontal depth `0<y<1/2` contributes on the zero side at exponential scale

\[
e^{qy^2}.
\tag{R-93271.4}
\]

But

\[
\boxed{\frac14-y^2>0.}
\tag{R-93271.5}
\]

Hence the coefficientwise absolute prime envelope has strictly larger exponential scale:

\[
e^{q/4}
=e^{qy^2}e^{q(1/4-y^2)}.
\tag{R-93271.6}
\]

Multiplying the prime kernel by any fixed-order polynomial or any subexponential-order finite difference changes only `e^{o(q)}` and cannot reverse this strict exponential inequality.

Truncating below the saddle does not solve the problem: the omitted tail still contains the saddle unless it is controlled with signed cancellation. Truncating beyond the saddle retains the same `q/4` absolute maximum.

Therefore no argument based only on coefficientwise absolute Gaussian domination can exclude a terminal depth `y<1/2`. A valid proof must preserve signed prime phases, use the carrier-resolved scale transform of `L-93272`, or provide an equivalent non-absolute mechanism.
