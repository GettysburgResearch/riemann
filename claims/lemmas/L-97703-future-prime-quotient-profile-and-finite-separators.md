# L-97703 — The future-prime quotient profile is the minimal exact Bellman state

Claim ID: `L-97703`  
Status: **PROVED EXACT FINITE-STATE AND SEPARATOR THEOREM**  
Created: 2026-08-18  
Depends on: `L-97700`, `L-97701`  
RH status: **unproved**

Fix an endpoint `X`, a dual parameter `lambda`, and a finite set of future rough primes. For every activated squarefree future product `m`, define

\[
\mathbf D_Q(m)=\bigl(D_Q^+(X/m,\lambda),D_Q^-(X/m,\lambda)\bigr).
\tag{L-97703.1}
\]

The set is finite because `X/m>=1`. If `p` is adjoined, `L-97700` gives the upper-triangular product-DAG update

\[
\boxed{D_{Q\cup\{p\}}^\pm(m)=D_Q^\pm(m)+\rho_pD_Q^\mp(mp).}
\tag{L-97703.2}
\]

For the parity-diagonal Bellman profile

\[
G_Q(m)=\bigl(\mathcal P_Q^-D_0^+\bigr)(X/m,\lambda),
\]

the update is

\[
\boxed{G_{Q\cup\{p\}}(m)=G_Q(m)-\rho_pG_Q(mp).}
\tag{L-97703.3}
\]

This is the exact future-prime quotient recurrence. The state records the actual real quotient `X/m`. A floor-only boundary profile is not sufficient for logarithmic/square-root Lorenz coordinates unless the analytic germ on each activation cell and each `lambda`-dependent positive-part breakpoint is also retained.

## Minimality

**Orientation.** At `lambda=1`, the empty source and one even atom `(a,t,r)=(1,1,0)` both have `D^+=0`, but reverse slacks `0` and `1`. A swapped child distinguishes them, so `D^+` alone is not Markov.

**Quotient.** Two profiles can have the same root value `G(1)=1` and child values `G(p)=0` and `G(p)=2`. Under (L-97703.3) with `rho_p=1/2`, their updated roots are `1` and `0`. A root-only state cannot determine prime addition.

**Naive two-sided cone.** The cone `D^plus,D^minus>=0` is invariant under the positive swap recurrence but the literal base source does not enter it. At the smallest endpoint `X=1`, one even atom has target `1`, scalar `0`, and at `lambda=-1`

\[
\boxed{D^+=1,\qquad D^-=-1.}
\tag{L-97703.4}
\]

## Exact finite separator set

For a finite atom state, `D^+(lambda)` is continuous and piecewise affine. Its only finite breakpoints are \(\lambda=r_i/t_i\) for even atoms. An Euler-minus Bellman transform is again piecewise affine, with breakpoint set equal to the union over the finite quotient profile. Therefore a finite failure of `LBP67` occurs either

1. on a target-capacity ray as `lambda -> -infinity`, or
2. at one explicit atom ratio from the future quotient profile.

The endpoint, future-prime set, quotient product, atom ratio, and exact dual value form a complete replayable separator.