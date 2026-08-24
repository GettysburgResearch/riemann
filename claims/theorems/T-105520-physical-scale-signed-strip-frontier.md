# T-105520 — Physical-scale signed strip frontier for ninety percent

Claim ID: `T-105520`  
Status: **UNCONDITIONAL MODEL/REDUCTION THEOREM; NINETY PERCENT OPEN**  
Created: 2026-08-24  
Depends on: `L-105500`, `L-105520--L-105522`, `T-105340`; PR #731 `T-105250`  
RH status: **unproved**

## 1. Model side is no longer the bottleneck

At the physically correct half-order symbol and the full scaled cutoff
\(\alpha=2\), the degree-four square-root Wick polynomial obeys

\[
\mathcal D_4(2)
\le
\frac{173344649}{1275293859840}
<
\frac1{7000}.
\]

Thus the frozen model has more than enough rank reserve for ninety percent.
This statement uses the corrected \(n^{-1/2-it}\) symbol and the scaled
prime-simplex law.

## 2. Compression side does not need pointwise zero-freeness

By `L-105521`, any source-fixed holomorphic observation family gives a valid
compression, even if its common scalar multiplier has zeros.  Consequently
the scalar zeros of \(P_K\) are not the obstruction.

The obstruction is the off-real polarization and strip transfer:
the formal \(P_K(x)^2\) source identity must be realized as the correct
Hermitian Hardy coordinate \(P_K(X)^*(R+R^*)P_K(X)\), with every edge and
freezing term retained.

## 3. One-sided conclusion gate

Let \(C_T\) be a source-owned Xi residue compression on a regular dyadic
window, of dimension

\[
d_T=(1-o(1))N_1(T,2T).
\]

Suppose it has an exact decomposition

\[
C_T=B_T+E_T,
\]

and a positive Gram \(G_T\) such that

\[
B_T\succeq\kappa_TG_T,
\qquad
\kappa_T\to1.
\]

Define

\[
\widetilde E_T
=
G_T^{-1/2}E_TG_T^{-1/2}.
\]

The single signed estimate

\[
\boxed{
\operatorname{tr}\bigl((\widetilde E_T)_-\bigr)
<
\left(\frac1{20}-o(1)\right)d_T
}
\tag{T-105520.1}
\]

is named `STRIPNEG105520`.

By `L-105522`,

\[
\nu_+(C_T)>\left(\frac{19}{20}-o(1)\right)d_T.
\]

The confluent full-signature/Cauchy-index theorem then gives

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0(T,2T)}{N(T,2T)}
>0.9.
}
\tag{T-105520.2}
\]

This conclusion counts critical-line zeros with multiplicity; endpoint bits
are \(o(N)\).

## 4. Exact remaining analytic statement

`STRIPNEG105520` must control the negative trace of precisely:

```text
Hardy-strip polarization remainder;
left/right safe-line folding discrepancy for the chosen observations;
vertical/end-point contour flux;
archimedean freezing;
smooth-taper conditioning;
companion-pole and collar terms;
any omitted-prime source tail not already covered by L-105342/L-105253.
```

The coefficient-freezing and omitted-prime rows are already power-saving on
their pinned scopes.  The unresolved part is the signed strip/companion
remainder.

PR #731's positive Lorentz companion energy is a natural producer for this
negative trace.  A matrix-valued companion-flux domination of
\(\operatorname{tr}((\widetilde E_T)_-)\) by less than \(d_T/20\) would close
(T-105520.2).  That domination is not proved here.

## 5. Status

```text
half-order normalization                         PROVED / REPAIRED
physical alpha=2 degree-four energy <1/7000      PROVED
compression without a zero-free unit             PROVED
safe-line accretive anchor                        PROVED
negative-trace absorption                        PROVED
STRIPNEG105520                                    OPEN / RECORD-BEARING
ninety percent for zeta                           UNPROVED
public record beaten                              NO
Riemann Hypothesis                                UNPROVED
```
