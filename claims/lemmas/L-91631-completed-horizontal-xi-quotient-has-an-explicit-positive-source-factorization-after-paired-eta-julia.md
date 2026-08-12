# L-91631 — The completed horizontal Xi quotient has an explicit positive source factorization after paired-eta Julia

Claim ID: `L-91631`  
Status: **PROVED EXACT ANALYTIC/SOURCE FACTORIZATION; MODEL EXHAUSTION OPEN**  
Created: 2026-08-12  
Depends on: `L-91630`; `L-91530`; `L-91430`  
RH status: **unproved**

## 1. Eta integral notation

Retain

\[
 I_\eta(z)=\frac{\eta_D(z)}{z}
 =\int_{\mathcal E}e^{-zy}dy,
 \qquad \Re z>0.
\]

Let

\[
 0<\omega<\frac12,
 \qquad
 s_0=1-\omega,
 \qquad
 s_1=1+\omega,
 \qquad
 L=\log2,
\]

and

\[
 F_L(z)=\frac{1-e^{-Lz}}{z}.
\]

## 2. Exact completed factorization

`L-91530` gives

\[
 \frac{\xi(s-\omega)}{\xi(s+\omega)}
 =\frac{\eta_D(s-\omega)}{\eta_D(s+\omega)}
  \frac{F_L(s-s_0)}{F_L(s-s_1)}
  \pi^\omega
  \frac{s-\omega}{s+\omega}
  \frac{\Gamma((s-\omega)/2)}{\Gamma((s+\omega)/2)}.
\]

Since `eta_D(z)=z I_eta(z)`, this becomes

\[
 \boxed{
 \begin{aligned}
 \frac{\xi(s-\omega)}{\xi(s+\omega)}
 ={}&
 \frac{I_\eta(s-\omega)}{I_\eta(s+\omega)}
 \left(\frac{s-\omega}{s+\omega}\right)^2\\
 &\times
 \frac{F_L(s-s_0)}{F_L(s-s_1)}
 \pi^\omega
 \frac{\Gamma((s-\omega)/2)}{\Gamma((s+\omega)/2)}.
 \end{aligned}
 }
\]

Every apparent pole at `s_0` or `s_1` is already removed by the compact bridge.

## 3. The residual rational factor is lossless

Define

\[
 b_\omega(s)=\frac{s-\omega}{s+\omega}.
\]

For `Re s>0`,

\[
 |b_\omega(s)|<1,
\]

and for `s=it` on the boundary,

\[
 |b_\omega(it)|=1.
\]

Thus `b_omega` is the elementary right-half-plane Blaschke factor and
`b_omega^2` is a lossless inner two-section channel.

## 4. Positive gamma Laplace source

For `Re s>omega`, the beta integral gives

\[
 \boxed{
 \pi^\omega
 \frac{\Gamma((s-\omega)/2)}{\Gamma((s+\omega)/2)}
 =\frac{2\pi^\omega}{\Gamma(\omega)}
  \int_0^\infty
  e^{-(s-\omega)t}
  (1-e^{-2t})^{\omega-1}dt.
 }
\]

Hence, for every fixed `sigma>omega`, the carrier kernel

\[
 \boxed{
 \mathscr G_{\sigma,\omega}(x,y)
 =\pi^\omega
  \frac{\Gamma((\sigma+i(x-y)-\omega)/2)}
       {\Gamma((\sigma+i(x-y)+\omega)/2)}
 }
\]

is positive semidefinite.  It is the Gram of the phase vectors
`e^{-ixt}` in the positive measure

\[
 \frac{2\pi^\omega}{\Gamma(\omega)}
 e^{-(\sigma-\omega)t}
 (1-e^{-2t})^{\omega-1}dt.
\]

## 5. Complete arithmetic source ledger

The completed quotient has now been reorganized into the following explicit
source/transfer components:

```text
paired-eta hard source
    = safe paired-eta returned state
      + positive paired-eta Julia detail;

b_omega^2
    = lossless rational inner channel;

F_L(s-s0)/F_L(s-s1)
    = compact finite-interval dyadic/gamma bridge;

gamma ratio
    = positive beta/Laplace carrier source.
```

All source spaces and carrier kernels are explicit and positive.  The only
quotient remaining in the analytic formula is the ratio between the hard and
safe paired-eta amplitudes, and `L-91630` replaces its source geometry by a
coefficient-one returned-state-plus-detail identity.

## 6. Scope firewall

The factorization is a complete **arithmetic source ledger**.  It does not
assert that the completed Xi quotient is a Schur multiplier, nor does it
identify the source details with the critical/stable model outputs.

A source-to-model colligation is still required before the nonnegative
hyperbolic output can be declared absent.

## 7. Exact boundary

```text
completed eta/bridge/gamma factorization         EXACT
paired-eta source dilation                       EXACT POSITIVE
rational residual factor                         INNER / LOSSLESS
gamma residual factor                            POSITIVE LAPLACE SOURCE
all source-side unbounded pole/tail issues        REMOVED
critical/stable model identification              OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```
