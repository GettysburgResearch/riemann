# T-103040 — Corrected TP2 middle-prefix frontier

Claim ID: `T-103040`  
Status: **UNCONDITIONAL KERNEL/HODGE ADVANCE; COMPLETE STAR/CYCLE ORIENTATION OPEN**  
Created: 2026-08-25  
Depends on: `L-103000--L-103007`; `R-103000--R-103002`; `T-102980--T-102990`  
RH status: **unproved**

`R-103002` corrects the first attempted composition of the TP2 kernel with the radial actual-owner source.

## 1. What is closed

The following statements are exact:

```text
the positive common half-kernel is strictly log-concave and TP2;
the signed derivative companion has a fixed Wronskian sign;
every fully formed order-concordant source minor is one-sided;
the Wronskian has finite total log-ratio budget;
the minimum-pair star potential is monotone and zero-sum;
the row-zero cycle is a positive average of symmetric four-label rectangles;
every such rectangle has a favorable ordered scalar Euler carrier.
```

## 2. What the correction restores

The radial owner difference is

\[
C_i-C_j
=(x_j-x_i)H^{(1)}_{ij}
-(x_j^2-x_i^2)H^{(2)}_{ij}.
\]

The native middle prefix `H^(1)_ij` is signed. Therefore its coefficient must be multiplied into the endpoint Plücker minor **before** the order-concordant/order-inverting split of `L-103002` is taken.

TP2 closes the part whose complete coefficient is concordant. It does not prove that the monotone owner-star coefficient remains concordant after the signed middle prefix is expanded.

## 3. Correct source-typed theorem

Define

```text
SMEP103040:
  after exact Boolean-Vaughan, carrier, common-core, completion-homotopy,
  endpoint-color, shared-owner, owner/core-overlap and finite-boundary
  recombination, the order-inverting source minors created by the signed
  middle Euler prefixes in the radial star and symmetric Pluecker rectangle
  packets have subpower logarithmic negative mass in the fixed
  derivative/outer observation.
```

The endpoint kernel contributes no additional adverse sign or power loss.

The concentrated-owner route is now

\[
\boxed{
\mathrm{SMEP}_{103040}
\Longrightarrow
\mathrm{COCURL}_{102980}
\Longrightarrow
\mathrm{OICP}_{102960}
\Longrightarrow
\mathrm{HMO}_{102940}
\Longrightarrow
\mathrm{RH}.
}
\]

The owner-gauge-invariant route remains

\[
\boxed{
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\]

## 4. Lifecycle correction

```text
L-103000--L-103004                    RETAINED EXACT
L-103005 star algebra                 RETAINED
L-103005 complete one-sided conclusion SUPERSEDED BY R-103002
L-103006--L-103007                    RETAINED EXACT
T-103020 star-closed implication      SUPERSEDED
T-103030 scalar-carrier theorem       RETAINED AT SCALAR/CARRIER SCOPE
SMEP103040                            OPEN / RH-BEARING
BCI102990                             OPEN / RH-BEARING
Riemann Hypothesis                    UNPROVED
```

The dramatic reduction survives in corrected form: all analytic endpoint geometry and all deterministic carrier geometry are solved. The remaining obstruction is exclusively the signed arithmetic middle-prefix transport.