# T-100320 — Prime-activation route to RH

Claim ID: `T-100320`  
Status: **UNCONDITIONAL REDUCTION; CONTINUOUS DRIFT GATE OPEN**  
Created: 2026-08-20  
Activation source: PR #681 at `295000fead70e87c17623cf0dcc2af838a60ed0c`  
Latest integrator: PR #685 at `4f69b7656f42dcb5ff250d13adc9f88e8d18f315`  
RH status: **unproved**

The actual-prime activation route is

```text
L-100320 activation prefix in (0,1]
 -> L-100321 exact envelope drift normal form
 -> CDTG100320
 -> E2(y)>=0
 -> zero-safe Mellin-Landau consumer
 -> RH.
```

The new content is that the cumulative activation jumps are closed exactly;
the only conclusion-producing arithmetic is the continuous prime-product
drift.

\[
\boxed{\mathrm{CDTG100320}\Longrightarrow RH.}
\]

For the exact minimal one-sided formulation, PR #685 proves

\[
\boxed{\mathrm{CATD100300}\iff RH,}
\]

where `CATD100300` is the subpower sum of exact cellwise negative areas.
`CDTG100320` is a stronger pointwise producer.  PR #684's finite adaptive
squaring is retained as a local method for proving the drift estimate, not as
a positivity-preserving inverse.

Neither gate is proved here.
