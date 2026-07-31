# T-14303 — The exact Riemann radical satisfies the cofinal tail/coercivity limits

Claim ID: `T-14303`  
Title: Gaussian radical-tail decay beats a complete polynomial Hardy moat  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: `L-14312`, `L-14313`, `L-14308`, `T-14302`  
Scope: the numerator/denominator blocker in the positive localized-Weil program  
Related counterexample candidates: none

## Statement

For integers `j>=4`, put

\[
 \lambda_j=e^j,
 \qquad
 a_j=j,
 \qquad
 \tau_j=\frac12-\frac1j.
 \tag{T-14303.1}
\]

Let `r=E(h_R)` be the exact global Riemann-radical vector of `L-14312`, write
`R(x)=r(e^x)`, and set

\[
 k_j=1_{[-a_j,a_j]}R.
 \tag{T-14303.2}
\]

For each `j`, let `P_j` be the finite complete multiband packet supplied by
`L-14313` at support `a_j`, transported back to `[-a_j,a_j]`, and put

\[
 S_j=P_j+\operatorname{span}\{k_j\}.
 \tag{T-14303.3}
\]

Define

\[
 h_j=
 \inf_{\substack{g\in \mathfrak D(Q_W^{a_j})\cap S_j^\perp\\g\ne0}}
 \frac{Q_W^{a_j}(g,g)}{\|g\|_{a_j,\tau_j}^2}
 \tag{T-14303.4}
\]

and

\[
 \mathfrak T_j=
 \sup_{\substack{g\in \mathfrak D(Q_W^{a_j})\cap S_j^\perp\\
                  \|g\|_{a_j,\tau_j}=1}}
 |Q_W^{a_j}(k_j,g)|.
 \tag{T-14303.5}
\]

Then

\[
 \boxed{
 \frac{\mathfrak T_j}{h_j}\longrightarrow0,}
 \tag{T-14303.6}
\]

and

\[
 \boxed{
 \frac{\mathfrak T_j^2}
 {h_j\|k_j\|_2^2}\longrightarrow0.}
 \tag{T-14303.7}
\]

Thus the requested squared-residual Schur penalty vanishes along an explicit
cofinal support sequence.

## Proof

By `L-14313`,

\[
 h_j\ge\lambda_j^{-1}.
 \tag{T-14303.8}
\]

By `L-14312`, the cross bound holds for every finite packet containing `k_j`.
Therefore fixed constants `C,M` satisfy

\[
 \mathfrak T_j
 \le C\lambda_j^M(1+\log\lambda_j)^{3/2}
 e^{-\pi\lambda_j^2}.
 \tag{T-14303.9}
\]

It follows that

\[
 \frac{\mathfrak T_j}{h_j}
 \le C\lambda_j^{M+1}(1+\log\lambda_j)^{3/2}
 e^{-\pi\lambda_j^2}\longrightarrow0,
\]

proving (T-14303.6).

Also `L-14312` gives

\[
 \|k_j\|_2\to\|R\|_2>0.
\]

Hence `||k_j||_2^2>=c_R>0` eventually, and

\[
 \frac{\mathfrak T_j^2}{h_j\|k_j\|_2^2}
 \le\frac{C^2}{c_R}
 \lambda_j^{2M+1}(1+\log\lambda_j)^3
 e^{-2\pi\lambda_j^2}
 \longrightarrow0.
\]

This proves (T-14303.7).  QED.

## One-dimensional diagonal

The exact radical identity also gives

\[
 Q_W^{a_j}(k_j,k_j)=Q_W(t_j,t_j),
 \qquad t_j=R-k_j.
 \tag{T-14303.10}
\]

The two-tail version of `L-14312` yields

\[
 |Q_W^{a_j}(k_j,k_j)|
 \le C\lambda_j^M e^{-2\pi\lambda_j^2}.
 \tag{T-14303.11}
\]

Thus the explicit radical row and column of the block Temple--Schur matrix have
a vanishing diagonal and a vanishing squared cross correction.

## What has and has not been closed

The theorem closes the exact asymptotic comparison

```text
external global-radical tail / complete finite-packet coercivity.
```

The numerator is Gaussian-small while the complete Hardy moat is only
polynomially small.  No extrapolated numerical decay law is used.

The first limit is proved on the complement of the enlarged finite packet
`S_j`.  It is not a proof that the complement of `span{k_j}` alone has a
positive ground-state gap.  The theorem therefore applies directly to the
block/squared-residual route of `L-14308` and `T-14302`.

## Remaining low-block theorem

This result does not prove RH.  `T-14302` still requires the entire corrected
finite low block

\[
 B_j-h_j^{-1}R_j^*M_j^{-1}R_j
 \tag{T-14303.12}
\]

outside its explicit radical row to have lower eigenvalue
`>=-epsilon_j`, with `epsilon_j->0`.  The generally growing multiband packet
contains the unresolved directions.

The remaining positive-path problem is therefore finite-dimensional at every
support but not yet uniformly controlled:

> approximate the complete low-symbol packet, in the Weil graph/form norm,
> by truncations of global `E`-radical sources with a cofinal uniform error.

## Proof boundary and gap audit

- No form of RH is used.
- The global radical and localized-symbol normalizations remain independent
  source gates.
- The packets are finite existence objects; no practical rank estimate is
  claimed.
- A finite Ritz calculation gives upper spectral values and cannot replace the
  missing low-block lower bound.
- The theorem proves the exact ratio requested in the block setting, not the
  final cofinal lower envelope required for RH.
