# Numerical contract

The numerical theorem is one fixed horizon and one prescribed rational vector:
`T=log 2`, degree four, coefficients `(4284,-1839,-1199,-742,-371)/10000`.
The full source is the factorial kernel, not a finite zero model.

## Arithmetic and all-region coverage

`interval_core.py` is a byte-preserved copy of the delivered OC26 math core.
Its 160-bit integer endpoints implement outward rational addition, products,
division, square roots and logarithms. `check.py` authenticates its literal
hash before compiling its bytes. The legacy Gaussian-rational helpers are used
only by small synthetic algebra checks; its earlier numerical checker is not run.

Logarithms use range-reduced atanh series, 64 terms and their exact geometric
remainders. The new pi enclosure is Machin's `16 atan(1/5)-4 atan(1/239)`,
using 64 terms and the signed first-omitted-term enclosure for each arctangent.
The source does not call zeta, gamma or a floating-point special function.

The new certificate reconstructs every half-integer cell from x=1 to 2048:
4094 cells, each integrated as a polynomial square against exp(-s). The exact
incomplete-gamma recurrence uses exp(-log(x1/x0))=x0/x1, a rational value.
Interval lower endpoints can be replaced by zero only where nonnegativity has
already been proved (a square integral or a positive moment).

The complete tail beyond x=2048 is enclosed analytically by PROOF (7.2)-(7.3).
Its polynomial moments are factorials. No final filter state is set to zero,
and no future of a finite filter input is confused with future arithmetic data.
Compact-input replacement uses the separately proved global translation and
stable-tail inequalities; it is not a sampled box approximation.

## Discovery versus acceptance

Two local exploratory scripts used numpy/scipy and ordinary quadrature to
choose plausible coefficients and expose the difference between truncated and
complete Grams. Their outputs are NOT certificates and are not proof inputs.
The final rational coefficients are explicit inputs. Their entire claimed
result is independently reconstructed with outward integer arithmetic.
No broad prime, zero, parameter, or growing-horizon sweep was conducted.

The analytic Gram floor and translation asymptotic are paper theorems. Bounded
algebra tests exercise formulas and constants, not infinitely many ranks or
small-shift limits. The certificate's 4094 integrated cells are coverage units,
not 4094 independent theorem proofs.
