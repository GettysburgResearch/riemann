# R-102872 — Positive complementary factors do not orient their arithmetic product

Claim ID: `R-102872`  
Status: **PROVED SOURCE-VERSUS-POINTWISE FIREWALL**  
Created: 2026-08-24  
Depends on: `L-102898--L-102900`; `R-102870`  
RH status: **not assumed**

The complementary-temperature identity

\[
\sigma_t*\sigma_{1-t}=\Gamma_{1/2}
\]

is an arithmetic convolution identity.  It does not say that the fixed scalar
observation of \(\Gamma_{1/2}\) is the pointwise product of the two
first-order observations.

A finite exact fixture already disproves such an inference.  Let

\[
a=\delta_1-\delta_2,
\qquad
b=\delta_1+\delta_2,
\]

and choose one linear observation whose kernel values at the three relevant
arguments are

\[
K_0=2,\qquad K_1=1,\qquad K_2=3.
\]

Then

\[
\mathcal O[a]=K_0-K_1=1>0,
\]

\[
\mathcal O[b]=K_0+K_1=3>0,
\]

but

\[
a*b=\delta_1-\delta_4
\]

and

\[
\boxed{
\mathcal O[a*b]=K_0-K_2=-1<0.
}
\]

Thus even two positive factor observations can have a negative arithmetic
product observation.

The same firewall applies to the eventually positive strict-completion
fields.  Neither eventual positivity, free tensor energy minimization, nor the
flat temperature connection proves `GMBC102893` or `CTZD102897`.  Physical
source recombination must be retained through the signed fixed kernel.
