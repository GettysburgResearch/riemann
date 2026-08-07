# Fixed-ratio Mertens-shell full-problem attack

Agent: `gpt56-pro-09-p`  
Date: 2026-08-07  
Branch: `agent/gpt56-pro-09-p/234-fixed-ratio-mertens-shell`  
Frozen parent: PR #229 at `2fc74c11b9929f694d8c13d060c9d55b99dc9621`  
Status: **PROPOSED / GAP-BLOCKED AT ONE BALANCED MÖBIUS SHELL ESTIMATE / RH NOT PROVED**

## Executive result

The repository-wide signed-correlation gate has been compressed to one explicit scalar signal. Fix

\[
c=\frac23
\]

and define

\[
I(x)=M(x)-M(2x/3),
\qquad
Q(t)=e^{-t/2}I(e^t).
\]

Then

\[
Q(t)=\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}
 e^{-(t-\log n)/2}
 \mathbf 1_{[0,\log(3/2))}(t-\log n),
\]

and

\[
\int_0^\infty Q(t)e^{-zt}dt
=
\frac{1-(2/3)^{z+1/2}}
{(z+1/2)\zeta(z+1/2)}.
\]

The numerator has no zero at any point with real part greater than `-1/2`. Hence this one compact shell window detects every hypothetical zeta zero to the right of the critical line.

For every fixed block length `B>0`, put

\[
E_B(J)=\int_J^{J+B}|Q(t)|^2dt.
\]

The Mellin/Hardy transfer gives the proposed exact equivalence

\[
\boxed{
\mathrm{RH}
\iff
E_B(J)=e^{o(J)}.}
\]

More quantitatively,

\[
\sup_{\zeta(\rho)=0}\left(\Re\rho-\frac12\right)
=
\frac12\limsup_{J\to\infty}
\frac{\log(1+E_B(J))}{J}.
\]

Thus a full proof no longer needs to establish a broad Farey operator theorem, a complete matrix cone, or a whole packet hierarchy. It is logically sufficient to prove a subexponential upper bound for one explicit positive Gram evaluated on the Möbius vector.

## Exact positive block Gram

For `c in (0,1)`, let `L=log(1/c)`. On a block `[J,J+B]`, only integers in one compact multiplicative annulus occur, and

\[
E_{c,B}(J)
=
\sum_{m,n}\mu(m)\mu(n)K_{c,B,J}(m,n),
\]

where

\[
K_{c,B,J}(m,n)
=
\int_J^{J+B}e^{-t}
 \mathbf 1_{\{ce^t<m\le e^t\}}
 \mathbf 1_{\{ce^t<n\le e^t\}}dt.
\]

The kernel is positive semidefinite and vanishes unless

\[
c<m/n<c^{-1}.
\]

Its full-line autocorrelation is the closed multiplicative Green kernel

\[
\frac1{\sqrt{mn}}R_c(|\log(m/n)|)
=
\left[
\frac1{\max(m,n)}-
\frac c{\min(m,n)}
\right]_+.
\]

This is a source-specific balanced Type-II object. The difficulty is an upper bound for its value on `mu`, not positivity of the kernel.

## Exact nonlinear identities

The shell satisfies two finite identities before any absolute value is taken.

### Divisor recurrence

For `x>=c^(-1)`,

\[
I_c(x)=-\sum_{k\ge2}I_c(x/k).
\]

Every destination has lower physical scale, but the unsigned coefficient mass is too large; the identity must be squared or recombined before Cauchy.

### Centered prime renewal

Let

\[
J_c(x)=\sum_{cx<n\le x}\mu(n)\log(x/n).
\]

Then

\[
\log x\,I_c(x)
+
\sum_{a\le x}\Lambda(a)I_c(x/a)
=J_c(x),
\]

and

\[
J_c(x)=\int_{cx}^{x}
\frac{M(u)-M(cx)}u\,du.
\]

This is the scalar fixed-ratio counterpart of the centered Selberg and signed semiprime equations. The prime/Möbius convolution must remain intact until its reflected square is assembled.

## High-order hierarchy

For every fixed order `m`,

\[
I_{c,m}(x)=\Delta_c^mM(x)
\]

has compact window transform

\[
\frac{(1-c^s)^m}{s},
\]

and Mellin transform

\[
\frac{(1-c^s)^m}{s\zeta(s)}.
\]

Every fixed finite order remains RH-equivalent. The shell coefficients are the signed binomial vector

\[
(-1)^r{m-1\choose r},
\qquad0\le r<m.
\]

Their total variation is `2^(m-1)`, so high order is useful only if the complete signed packet is recombined before any norm estimate.

## Terminal and top-order narrowing

The terminal Euler results on PRs #165/#233 and the higher-order closure on PR #158 imply:

- every packet with one genuinely macroscopic unrestricted integer variable is exponentially small after sufficient smoothing;
- every unresolved order-`j` Heath--Brown packet has
  \[
  j/K\ge1-\eta-o(1);
  \]
- with `eta_K=K^(-1/2)`, the hard source is confined to
  \[
  j\ge K-O(\sqrt K).
  \]

The top-band combinatorial count has zero block exponent for fixed `K`. The unresolved analytic theorem is therefore a signed estimate for the top-order truncated-Möbius tensor, with coefficient rate `epsilon_K=o(K^(-1/2))` on this schedule.

This narrowing does not prove the tensor estimate. The exact Möbius decoder shows that the hard source remains present after increasing the identity order.

## One-prime parity barrier

For `c>1/2`, if `cx<n<=x` and `p>=2` is prime, then

\[
pn>x,
\qquad
n/p<cx.
\]

Thus adding or deleting one prime factor exits the shell. Replacing one prime by another preserves Möbius parity. An internal opposite-sign pairing must alter at least three prime incidences, for example a balanced prime-versus-semiprime move

\[
pa\longleftrightarrow qra.
\]

This explains why terminal one-free-variable cancellation cannot settle the first cell. The remaining geometry is intrinsically balanced.

## Audit of the reflected-Selberg proposal

PR #226's reflected coefficient identity is a genuine improvement:

\[
2|\zeta'/\zeta(\sigma+it)|^2
=\mathcal C_\times-\mathcal C_+-\mathcal C_-.
\]

It supplies the missing Hermitian square rather than the analytic square `H(z)^2`.

However, its proposed closing lemma `L-9517` says that finite complexity induction removes both reduced and balanced rows, leaving terminal faces. The corrected source theorem on PR #233 says otherwise:

- reduced Type-I rows are eliminated by acyclic complexity descent;
- terminal rows are Euler-small;
- balanced Type-II destinations are explicitly **not estimated** and define the open theorem `BTP(K)`.

A bounded terminal endpoint count `C_*` therefore controls only the terminal family. It does not prove the balanced packet recurrence, and the first-cell Möbius mutation cannot be obtained from the terminal subfamily alone.

This scope correction is recorded as `R-23402`.

## Exact finite regression

`X-23401` verifies, using only integers and `fractions.Fraction`:

```text
divisor recurrence rows       95
formal prime-renewal rows      95
high-order shell rows          672
finite Mellin rows             4
one-prime barrier rows         12,664
rational Gram blocks           4
mutation tests                 9/9 PASS
proof-object SHA-256
0772b74939f89a2e9ac45fe38fbc0e3fd4f131c9e3d83ecdbf7ab1debb3aeff1
```

This is finite algebra and Gram factorization only.

## Non-directed reconnaissance

An ordinary exact-Möbius/double-precision integral of

\[
\int_X^{2X}\frac{|M(x)-M(2x/3)|^2}{x^2}dx
\]

produced values between approximately `0.0084` and `0.0301` for dyadic `X` from `256` through `2,097,152`. The values show no visible growth at that scale.

This is discovery evidence only. It is neither directed nor asymptotic and cannot support an RH claim.

## Exact remaining theorem

The minimal open statement is

\[
\boxed{
E_{2/3,\log2}(J)=e^{o(J)}.}
\]

A packet proof may establish a recurrence

\[
E(J)
\le
\exp\{(\varepsilon_K+o_K(1))J\}
\left[
1+
\max_{u\le(1-\delta_K)J+C_K}E(u)
\right]
\]

with

\[
\varepsilon_K/\delta_K\to0,
\]

or the corresponding tensor condition. It must preserve the exact signed top-order Möbius packet and export the first-cell source map.

## Current status

```text
fixed-ratio transform and positive Gram       PROPOSED COMPLETE
shell-energy/rightmost-zero equivalence       PROPOSED COMPLETE TRANSFER
exact divisor and prime renewal               PROPOSED COMPLETE
high-order shell hierarchy                    PROPOSED COMPLETE
terminal/free-variable closure                IMPORTED PROPOSED COMPLETE
hard-core top-order concentration             PROPOSED COMPLETE SCALE GEOMETRY
reflected Selberg Hermitian identity           IMPORTED PROPOSED COMPLETE
balanced Möbius shell contraction              OPEN
Riemann Hypothesis                             NOT PROVED
```
