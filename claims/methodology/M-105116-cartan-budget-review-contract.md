# M-105116 - Cartan budget optimization review contract

Claim ID: M-105116

Status: **REVIEW CONTRACT**

Created: 2026-08-23

RH status: **unproved**

## Required checks

1. Declare the positive scalarization weights \(u_j\); a different carrier
   objective can have a different optimizer.
2. Use the nominal radius coefficients \(v_j\), including every
   \(r_{2,j},A_j,\beta_j\) factor.
3. Remove zero-load indices before claiming uniqueness.
4. Keep the cap \(0<\varepsilon_j\le1\); large budgets cannot reduce the
   logarithmic factor below \(\log2\) within L-105114.
5. Optimize on a closed budget.  Use a separate positive fractional slack
   to recover the strict geometric gate.
6. Check cap activity through \(u_j/v_j\), not by assuming the interior
   formula.
7. Add epsilon-independent spatial terms after the optimization.
8. Distinguish nominal radius from the possibly smaller actual merged-disk
   and projection loads.
9. Retain the safe-set normalization factor; it can diverge as
   \(\delta\downarrow0\).
10. Do not infer Xi absorption merely because the finite allocation is
    optimal.

## Fail-closed scope

The following remain false unless separately proved:

- inverse growth-load allocation is optimal for the stated logarithmic sum;
- all functions receive equal epsilon without the common coefficient ratio;
- an active strict open budget has an attained optimizer;
- the exact merged-projection loss always equals its total-radius bound;
- the optimized generic Cartan loss is absorbable by actual selectors;
- RCMV104530 or RH follows.
