# T-91652 corrected ledger index

Status: **proposed / frozen review required**  
Supersedes as review target: `T-91651`  
RH status: **unproved**

## Exact chain

```text
R-91650/R-91651/R-91652/R-91653       mandatory firewalls
L-91650                               causal coefficients; child mass <1/8
L-91652/L-91653/L-91654               certificate, datum, causal positivity
L-91657                               compact literal-debt sign repair
L-91658                               normalized same-index child embedding
L-91659                               complete native=current+recursive root datum
L-91660                               F_Lambda <= native endpoint deficit
L-91406/T-91650                       homogeneous packet envelope
O-91651                               review order
```

The two conclusion-producing inequalities to reconstruct are

\[
\Lambda(X)\le C+\frac18\Lambda(X/67)
\]

and

\[
\Delta_X(N_X)\le C_{root}+\Delta_X(R_XZ_X),
\qquad \widehat m(Z_X)\le54.
\]

Together with `L-91660`, the ledger proposes a subquadratic complete-prime-power gap. Exact local and external blobs are specified in `t91652-full-ledger-lock.json`.

## Scope restrictions

- `U_p` is normalized embedding; the actual child coefficient is `alpha_i`.
- Root collars, omission and common port are current and used once.
- `L-91112` is imported only for retained displays `.25--.26`.
- External endpoint consumers are pinned by source commit and blob SHA.
- No theorem in this index is promoted beyond its source status.
