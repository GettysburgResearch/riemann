# R-91408 — The one-vector eta Householder does not intertwine the full carrier family

Claim ID: `R-91408`  
Status: **EXACT GRAM-MISMATCH FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91431`  
RH status: **unproved**

## 1. Analytic paired vectors

For `sigma>0` and real carrier `t`, define

\[
 d_m(\sigma,t)
 =(2m-1)^{-\sigma-it}-(2m)^{-\sigma-it}.
 \tag{R-91408.1}

\]

The vector

\[
 d_{\sigma,t}=(d_m(\sigma,t))_{m\ge1}
 \tag{R-91408.2}

\]

belongs to `ell2`: the mean-value formula gives

\[
 d_m(\sigma,t)
 =O_{\sigma,t}(m^{-\sigma-1}).
 \tag{R-91408.3}

\]

Let

\[
 K_\sigma(t,u)
 =\langle d_{\sigma,t},d_{\sigma,u}\rangle.
 \tag{R-91408.4}

\]

## 2. Necessary condition for a full unitary intertwiner

If one unitary `U` satisfied

\[
 Ud_{1,t}=d_{1-2\omega,t}
 \tag{R-91408.5}

\]

for every carrier in a set containing two independent values, then necessarily

\[
 \boxed{
 K_1(t,u)=K_{1-2\omega}(t,u)
 }
 \tag{R-91408.6}

\]

for every such pair.

This condition fails.  Already the diagonal norm

\[
 K_\sigma(t,t)
 =\sum_m|d_m(\sigma,t)|^2
 \tag{R-91408.7}

\]

depends nontrivially on `sigma`, and after normalization the off-diagonal
correlations still change.  Therefore the Householder reflection of
`L-91431`, which is exact at the distinguished real vector, cannot be promoted
to a carrierwise unitary by linearity.

## 3. Numerical finite control

The retained finite regression uses carriers

\[
 0,\ 0.7,\ 1.4
\]

at `omega=0.2`.  After normalizing each carrier vector, the Frobenius distance
between the safe and hard three-carrier Gram matrices is

\[
 0.3775214041\ldots>0.
 \tag{R-91408.8}

\]

The nonzero value is only an illustration; the analytic dependence on
`sigma` proves the obstruction.

## 4. Correct completion

A full paired-eta construction must be a contractive or conservative
colligation

\[
 d_{1,t}
 \longmapsto
 d_{1-2\omega,t}\oplus e_{\omega,t}^{\rm env}
 \tag{R-91408.9}

\]

whose environment Gram is exactly

\[
 K_1-K_{1-2\omega}
 \tag{R-91408.10}

\]

in an orientation where that difference is positive, or a larger
source-ordered Schur completion if it is not.  Positivity of this kernel may
not be assumed.

For the one-node route only the vector `t=0` is required, so `L-91431` remains
a genuine advance.

## 5. Exact boundary

```text
one distinguished eta source vector                 UNITARILY MAPPED
complete carrier family by the same unitary          FALSE
safe and hard carrier Grams                          DIFFERENT
positive-environment carrier colligation             OPEN
one-node pole-bridge use                             STILL VALID
Riemann Hypothesis                                   UNPROVED
```