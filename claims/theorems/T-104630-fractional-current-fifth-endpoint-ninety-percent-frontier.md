# T-104630 — Fractional-current fifth-endpoint frontier for more than ninety percent

Claim ID: `T-104630`  
Status: **UNCONDITIONAL EXACT REDUCTIONS + ONE SOURCE-WEIGHTED XI ESTIMATE OPEN**  
Created: 2026-08-27  
Depends on: `L-104630--L-104632`; frozen PR #731 fifth-endpoint ledger; frozen
PR #729 strong Xi source curvature  
RH status: **unproved**

The direct fixed-order Conrey functional reconstructed in `T-104620` is a
trustworthy unconditional baseline, but its zeroth-derivative optimization is
not a plausible path to ninety percent. The quantitative route capable of
that target is the odd fifth-endpoint telescope.

The frozen exact input is

\[
R_0(T,2T)
\ge R_5(T,2T)-\|H_{U_{5,\lambda_T}}\|_{\mathcal S_2}^2-o(N),
\]

with

\[
{R_5(T,2T)\over N(T,2T)}>{997\over1000}-o(1).
\]

`T-106590/L-106591` pay every denominator direction above height `1/100`
at cost at most

\[
{3\over40}N+o(N).
\]

The remaining unweighted shallow charge formerly required a finite model-space
coverage theorem plus a phase/canonical-correlation estimate.

## 1. What the new packet closes

`L-104630` proves the exact fifth-current source sandwich

\[
e^{-H\xi-7H^2/(3\kappa_0)}\le r_{5,H}(\xi)\le e^{-H\xi}.
\]

`L-104631` resolves the identity by the fractional positive current bank

\[
{1\over\Gamma(a)}\int_0^\infty
 H^{a-1}M_{\xi^ae^{-H\xi}}\,dH=I
\]

and converts the unweighted canonical defect into a complete scale integral.
There is no uncovered model-space direction.

`L-104632` rewrites every scale integrand as an exact primal distance to the
numerator model space. Transports may be chosen separately at each source
scale, with no Gram-condition-number penalty.

## 2. The sole conclusion-bearing gate

Define

```text
FRACTRANS104630 — fractional fifth-current transport

For a=1/1000 and H_0=1/20, construct source-defined scale-wise transports
for the complete mesoscopic fifth-endpoint packet such that

  limsup I_sh(T)/N(T,2T) < 21/1000,

where I_sh is the literal current-weighted residual in L-104632.2. Retain
common factors, confluence, both denominator companion channels and every
regular-window endpoint.
```

Then the exact rational ledger of `L-104632` gives

\[
\mathfrak C_{\rm sh}<{21701\over10^6}N+o(N)
<{11\over500}N+o(N),
\]

and hence

\[
\boxed{
\mathrm{FRACTRANS104630}
\Longrightarrow
\liminf_{T\to\infty}{N_0(T,2T)\over N(T,2T)}
>{900299\over10^6}>0.9.
}
\tag{T-104630.1}
\]

## 3. Why this is a stricter frontier

The former gates left several conceptually separate tasks:

```text
finite model-space coverage;
frame conditioning;
one global phase and channel cancellation;
unweighted canonical correlation;
source/current metric mismatch;
shallow cutoff exhaustion.
```

The fractional bank closes coverage, conditioning, current-metric comparison
and cutoff exhaustion exactly. The remaining object is one positive,
scale-wise, source-weighted transport residual. It can be attacked directly
using the finite zeta-derivative packets through order six.

This theorem does not prove `FRACTRANS104630`. More than ninety percent and RH
remain unproved.
