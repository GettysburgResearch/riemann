# T-101000 — Implication hypergraph and minimal closure cut sets

Claim ID: `T-101000`  
Status: **PROVED EXACT INTEGRATION THEOREM; RH UNPROVED**  
Created: 2026-08-20  
Base main SHA: `677203992eb0168920365ee45ae9db76bfa97dcf`  
Review cutoff: 2026-08-20  
RH status: **unproved**

The accompanying node matrix and hyperedge registry reconstruct the current
conclusion-facing graph by mathematical type rather than route name.

## 1. Detector quotient

The following criteria lie in the RH-equivalent detector class on their frozen
inputs:

```text
AFCD / critical weighted variation;
ACAD / activation-zero envelope negative mass;
MWOC / minimal compact wavelet;
LPMW / rough largest-prime wavelet;
BVD / balanced Vaughan trilinear;
HTOC / Hardy tail;
DGOC / divisor-GCD owner square.
```

They expose different structure, but proving a complete instance of any one is
already conclusion-bearing.  They should not be counted as independent middle
lemmas in an additive proof ledger.

## 2. New exact translation edges

`L-101000` proves

\[
\boxed{\mathrm{AFCD}\Longrightarrow\mathrm{ACAD}.}
\]

`L-101001` proves

\[
\boxed{\mathrm{LPMW}\Longleftrightarrow\mathrm{BVD}}
\]

modulo an absolutely integrable error.

`L-101002` proves that signed phase-Hasse physical packing is the minimal
wavelet realization, not an independent detector.

## 3. Genuine conjunctive hyperedges

The matrix retains four honest source-cover packets.

### H-CV

```text
global shifted-quadratic positivity       VERIFIED
activation-free distributional descent    VERIFIED
critical weighted-variation estimate      OPEN
--------------------------------------------------
RH
```

The first input cannot replace the third; PR #690 gives an exact smooth
countermodel.

### H-SQ

```text
finite small-prime Euler squaring          VERIFIED
depth-one large-prime collar geometry      VERIFIED
source-faithful oriented collar variation  OPEN
--------------------------------------------------
AFCD -> RH
```

Neither an alternating inverse nor an endpoint-dependent Landau diagonal is
allowed.

### H-LP

```text
minimal compact wavelet                    VERIFIED
smooth-sector Rankin estimate              VERIFIED
rough largest-prime signed estimate        OPEN
--------------------------------------------------
MWOC -> RH
```

### H-V

```text
extra half-order zero moment               VERIFIED
all Type-I lattice terms                   VERIFIED
balanced trilinear signed estimate          OPEN
--------------------------------------------------
MWOC -> RH
```

By `L-101001`, `H-LP` and `H-V` are two coordinate systems on one terminal
gate.

## 4. Minimal open cut sets

After contracting exact equivalences and removing false edges, the live graph
has two minimal structural cut classes:

```text
CV  critical one-sided variation;
XD  signed cross-core dispersion.
```

A proof may close either class directly.  Alternatively, a genuinely new
hyperedge may transfer a verified estimate from one class to the other.  No
such transfer is currently proved in both directions.

## 5. Research implication

The matrix recommends two coordinated attacks rather than more detector
renaming:

1. combine finite squaring with an oriented depth-one collar estimate on the
   fixed activation-free scalar;
2. combine largest-prime ownership with the balanced Vaughan coordinates and
   preserve cancellation through the compact wavelet.

These are the two places where multiple partial theorems already meet on one
literal source ledger.

```text
implication matrix                         VERIFIED
translation edges L-101000--L-101002      VERIFIED
minimal cut computation                    VERIFIED
critical variation class                   OPEN / RH-EQUIVALENT
cross-core dispersion class                OPEN / RH-EQUIVALENT
Riemann Hypothesis                         UNPROVED
```
