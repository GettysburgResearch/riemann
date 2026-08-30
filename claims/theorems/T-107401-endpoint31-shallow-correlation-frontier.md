# T-107401 — Endpoint-31 shallow-correlation frontier with \(37/500\) allowance

Claim ID: `T-107401`  
Programme aliases: `XI90.SHALLOW31`, `XI.SOURCE_PICK_31_SHALLOW`  
Status: **MACROSCOPIC AND DEEP CHARGE CLOSED; ONE SHALLOW XI-SPECIFIC GATE OPEN**  
Created: 2026-08-30  
Depends on: `L-107401--L-107404`; endpoint winding algebra of PR #731  
Programme issue: #744  
RH status: **unproved**

Let \(U_{31,\lambda_T}\) be the reduced endpoint-31 all-pass quotient on the
regular mesoscopic exhaustion, with the window-adapted positive shift of
`L-107404`.

Factor the denominator inner function by pole height at

\[
\eta=rac1{100}.
\]

The exact model-space split is

\[
\|H_{U_{31,\lambda_T}}\|_{\mathcal S_2}^2
=
\mathcal C_{31,\le1/100}(T)
+\mathcal C_{31,>1/100}(T).
	ag{T-107401.1}
\]

By `L-107404`,

\[
\mathcal C_{31,>1/100}(T)
\le
\left(rac1{40}+o(1)ight)N(T,2T).
	ag{T-107401.2}
\]

Define the single remaining gate

```text
SHALLOW31SOURCEPICK107401:

limsup_(T->infinity)
  C_(31,<=1/100)(T)/N(T,2T)
< 37/500.
```

Since

\[
rac1{40}+rac{37}{500}=rac{99}{1000},
\]

and `L-107400` gives

\[
rac{R_{31}(T,2T)}{N(T,2T)}>rac{999}{1000}-o(1),
\]

the endpoint winding identity yields

\[
oxed{
\mathrm{SHALLOW31SOURCEPICK}_{107401}
\Longrightarrow
\liminf_{T	o\infty}
rac{N_0(T,2T)}{N(T,2T)}>0.9.
}
	ag{T-107401.3}
\]

## Relation to the Xi source constant

`L-107401` gives the carrier-adapted central source constant \(1/62\). The
remaining room inside the shallow allowance is

\[
oxed{
rac{37}{500}-rac1{62}
=rac{897}{15500}
>0.0578.
}
	ag{T-107401.4}
\]

Thus a physical shallow transfer theorem may lose more than five percent of
the total zero count beyond the central source constant and still prove the
record.

Define the stronger but source-aligned sufficient statement

```text
XI31SHALLOWTRANSFER107401:

C_(31,<=1/100)(T)
 <= (1/62 + delta + o(1)) N(T,2T)
for one fixed delta < 897/15500,
retaining numerator phase, forced unit index, confluence and endpoints.
```

Then

\[
oxed{
\mathrm{XI31SHALLOWTRANSFER}_{107401}
\Longrightarrow
\mathrm{SHALLOW31SOURCEPICK}_{107401}
\Longrightarrow
>90\%.
}
	ag{T-107401.5}
\]

Neither shallow gate is proved. `R-107400` remains binding: the forced unit
spectrum cannot be deleted by radial or diagonal source softening.

```text
alpha_31 > 999/1000                       PROVED
endpoint-31 height <=1/4000 N              PROVED
all deep charge above 0.01 <=1/40 N        PROVED
shallow allowance 37/500                   PROVED EXACT
central source constant 1/62               PROVED
extra shallow transfer room 897/15500      PROVED EXACT
SHALLOW31SOURCEPICK107401                   OPEN
XI31SHALLOWTRANSFER107401                  OPEN
more than ninety percent                   UNPROVED
Riemann Hypothesis                         UNPROVED
```
