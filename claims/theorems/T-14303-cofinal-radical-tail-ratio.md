# T-14303 — Cofinal radical-tail residual ratios vanish

Claim ID: `T-14303`  
Title: An exact fixed `E`-radical satisfies both requested tail/coercivity limits on a cofinal packet sequence  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: `L-14309`, `L-14311`, `L-14312`, `L-14313`  
Scope: the residual/coercivity blocker isolated in `T-14302`  
Related counterexample candidates: none

## Cofinal construction

Fix the exact self-Fourier Riemann source `h_R` and its nonzero global radical
vector `R` from `L-14312`. For integers `j>=4`, put

\[
 a_j=j,
 \qquad
 \lambda_j=e^j,
 \qquad
 \tau_j=\frac12-\frac1j.
 \tag{T-14303.1}
\]

Let

\[
 k_j=1_{[-j,j]}R,
 \qquad
 t_j=R-k_j.
 \tag{T-14303.2}
\]

For each `j`, let `S_j` be the finite generalized-prolate packet from
`L-14313`, enlarged to contain `k_j`. Define the complement moat

\[
 h_j=
 \inf_{\substack{0\ne g\in S_j^\perp}}
 \frac{QW_{\lambda_j}(g,g)}{\|g\|_{j,\tau_j}^2}
 \tag{T-14303.3}
\]

and the cross residual

\[
 \mathfrak T_j
 =\sup_{\substack{g\in S_j^\perp\\
                   \|g\|_{j,\tau_j}=1}}
 |QW_{\lambda_j}(k_j,g)|.
 \tag{T-14303.4}
\]

## Main conclusion

The moat satisfies

\[
 \boxed{h_j\ge e^{-j}=\lambda_j^{-1}.}
 \tag{T-14303.5}
\]

For every `N`,

\[
 \boxed{\mathfrak T_j=O(\lambda_j^{-N}).}
 \tag{T-14303.6}
\]

Moreover

\[
 \|k_j\|_2^2\longrightarrow\|R\|_2^2>0.
 \tag{T-14303.7}
\]

Therefore both displayed limits in the project critical path hold:

\[
 \boxed{
 \frac{\mathfrak T_j}{h_j}\longrightarrow0,}
 \tag{T-14303.8}
\]

and

\[
 \boxed{
 \frac{\mathfrak T_j^2}
 {h_j\|k_j\|_2^2}\longrightarrow0.}
 \tag{T-14303.9}
\]

The second is the squared-residual term entering the block Temple--Schur lower
floor of `L-14308` and `T-14302`.

## Proof

`L-14313` gives the Hardy coercivity bound

\[
 h_j\ge\frac{3e^2}{4e^j}>e^{-j},
\]

which proves (T-14303.5).

The supremum in (T-14303.4) is taken over a subset of the unit vectors used in
the complete residual of `L-14312`. Hence, for every `N`,

\[
 \mathfrak T_j\le C_Ne^{-Nj}=C_N\lambda_j^{-N}.
\]

This proves (T-14303.6). Equation (T-14303.7) is `L-14312.12`.
Choosing `N=2`, for example,

\[
 \frac{\mathfrak T_j}{h_j}
 \le C_2\lambda_j^{-1}\to0.
\]

Choosing `N=2` again and using the eventual positive lower bound for
`||k_j||^2` gives

\[
 \frac{\mathfrak T_j^2}{h_j\|k_j\|^2}
 \le C\lambda_j^{-3}\to0.
\]

QED.

## Rayleigh value

`L-14312` also gives, for every `N`,

\[
 \rho_j:=\frac{QW_{\lambda_j}(k_j,k_j)}{\|k_j\|_2^2}
 =O(\lambda_j^{-N}).
 \tag{T-14303.10}
\]

Thus the scalar row of the Schur-corrected low block satisfies

\[
 \rho_j-
 \frac{\mathfrak T_j^2}{h_j\|k_j\|_2^2}
 \longrightarrow0.
 \tag{T-14303.11}
\]

## What this closes

The theorem closes the analytic tail/coercivity ratio for one exact global
radical truncation, and for every fixed finite packet of such truncations. It
also proves that the loss caused by moving the Hardy strip to `tau_j->1/2` is
far weaker than the exact tail decay.

## What remains before RH

The low space `S_j` is larger than `span{k_j}`. The block theorem requires a
lower bound for the **entire** corrected finite matrix

\[
 B_j-h_j^{-1}R_j^*M_j^{-1}R_j.
 \tag{T-14303.12}
\]

T-14303 proves that the row and column belonging to every fixed exact radical
truncation vanish. It does not prove nonnegativity of the remaining growing
multiband packet. That finite but support-dependent low block is now the sole
unclosed part of this particular lower-floor construction.

## Ground-vector interpretation warning

Although (T-14303.8) is numerically the stronger ratio, the `h_j` used here is
the complement moat after a finite generalized-prolate enlargement. It is not
a spectral gap on `k_j^perp` alone. Therefore (T-14303.8) must not be advertised
as convergence of `k_j` to a unique ground eigenvector. The directly valid
application is the block/squared-residual route (T-14303.9).

## Proof boundary

- The theorem inherits the source normalization and global radical theorem.
- The symbol packet inherits the sign and Fourier normalization of `L-14311`.
- No numerical extrapolation or finite-prefix inference is used.
- This theorem proves the requested ratio, not the full Riemann hypothesis.
