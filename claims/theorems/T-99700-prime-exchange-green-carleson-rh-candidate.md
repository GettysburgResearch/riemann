# T-99700 — Prime-exchange Green--Carleson control of the zero-free SHARP box implies RH

Claim ID: `T-99700`  
Status: **PROPOSED UNCONDITIONAL CLOSURE THEOREM — ONE EXPLICIT ARITHMETIC ESTIMATE OPEN**  
Created: 2026-08-20  
Depends on: `L-99270`, `L-99700--L-99705`, the specialized Mellin--Landau consumer of PR #653  
RH status: **unproved**

## 1. Exact source

For every `X`, let `m_X^plus,m_X^minus` be the positive box-source measures of `L-99704`, after the exact same-vertex trace cancellation of `L-99705`. Let `G_X` be the reversible prime-birth/death graph of `L-99702` restricted to the three decorated squarefree fibres in (L-99705.2).

A source-faithful flow is required to:

1. use only labelled prime-power paths in `G_X`;
2. preserve every source occurrence and its full coefficient;
3. use each right-channel capacity at most once;
4. preserve the endpoint `X` and the box potential `Phi_X^Box`;
5. retain the three factor-67 fibres separately until the final scalar observation.

Let `rho_X^*` be the minimum unmatched negative mass. By `L-99704`,

\[
[-(\mathcal S_{67}h)(X)]_+
\le\sqrt X\,\rho_X^*.
\tag{T-99700.1}
\]

## 2. The conclusion-producing estimate

Define **PXGC99700** to be the source-computable prime-exchange Green--Carleson estimate

\[
\boxed{
\int_2^Y\sqrt X\,\rho_X^*\frac{dX}{X}
\ll_\varepsilon Y^\varepsilon
\qquad\text{for every }\varepsilon>0.
}
\tag{T-99700.2}
\]

This is not an unconstrained coupling-existence statement. The graph, capacities, first-owner labels, and box potential are fixed before the unknown sign is observed. The finite max-flow/min-cut dual is the explicit quantity in (L-99704.4).

## 3. Conditional conclusion

Assume PXGC99700. Equation (T-99700.1) gives

\[
\int_2^Y[(\mathcal S_{67}h)(X)]_-\frac{dX}{X}
\ll_\varepsilon Y^\varepsilon.
\tag{T-99700.3}
\]

The Mellin transform of the box scalar is

\[
\frac{1-67^{-s}}s
\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}.
\tag{T-99700.4}
\]

The new box factor has no zero in `Re s>0`. Adding the nonnegative correction represented by the left side of (T-99700.3) produces a Mellin transform holomorphic in every `Re s>epsilon`. Therefore an off-line zero `rho=1/2+delta+i gamma` would leave a nonreal pole at `s=delta+i gamma`, contradicting the nonnegative-density Landau theorem exactly as in `L-99270`.

Hence

\[
\boxed{
\mathrm{PXGC99700}\Longrightarrow\mathrm{RH}.
}
\tag{T-99700.5}
\]

## 4. Why this is a genuinely smaller and different target

PXGC99700 does not ask for:

```text
pointwise positivity of h;
pointwise positivity of the reciprocal prefix;
a positive completion trace;
an unconstrained common contraction;
within-integer owner quadratic variation to orient squarefree parity;
a colored physical row or Hall interpolation;
a power-saving Mertens estimate.
```

It asks only for subpower **unmatched capacity** in one explicit reversible graph, after a zero-free activation-safe box smoothing.

## 5. Proposed proof mechanism

The exact candidate is a capacitated electrical decomposition on logarithmic `X`-blocks:

1. cancel the neutral trace at each vertex (`L-99705`);
2. route repeated-prime and factor-67 uncertainty with the logarithmic owner kernel (`L-99701`);
3. use the detailed-balance birth edges (`L-99702`) to connect distinct squarefree integers;
4. use the bounded box potential (`L-99703`) so deep-interior edge drops are summable;
5. compress the remaining min-cut to first-owner product-boundary cuts;
6. pay the compact quotient part by the frozen factor-67 Hall certificates and the moving tail by prime-reciprocal discrepancy;
7. iterate the strict child-mass budget below `1/8` only after the flow is typed.

Steps 1--4 are proved in this packet. Step 5 is the first new hostile-review target. Steps 6--7 are available as frozen ingredients only after that cut-compression theorem is established for the same live capacities.

## Exact boundary

```text
SHARP/reciprocal Volterra bridge             PROVED
local owner martingale and logarithmic energy PROVED
owner-only orientation mechanism              REFUTED
reversible cross-source network                PROVED EXACT
activation-safe zero-free box potential        PROVED EXACT
trace cancellation / squarefree compression    PROVED EXACT
finite flow/min-cut formulation                 PROVED EXACT
PXGC99700 cut-compression/Carleson estimate      OPEN / RH-BEARING
T-99700 conditional implication                 PROVED
Riemann Hypothesis                              UNPROVED
```