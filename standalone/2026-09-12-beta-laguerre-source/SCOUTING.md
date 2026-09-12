# Nondirected exploration — excluded from proof acceptance

The optional mpmath computation used the exact moment-recursion FORMULA but
computed its values and a finite Laguerre transform with nondirected arithmetic.
High working precision does not bound the omitted Laguerre tail.

At theta=1, the code differentiates the normalized moment recurrence and then
forms a finite approximation to partial_theta M. Dividing that by 2 xi'(rho)
would describe the first raw-Mellin zero displacement under theta=1-epsilon,
IF the derivative approximation and the simple reference zero were certified.
Neither was certified by this scout. The reference rho is supplied by
mpmath.zetazero and is not an input to the accepting checker.

Retained outputs, showing REAL parts of this formal displacement:

| mpmath reference index | height (approx.) | order 1000 | order 1500 |
|---|---:|---:|---:|
| 4 | 30.424876 | -1.7339399001 | -1.7339401358 |
| 9 | 48.005151 | -10.63066108 | -11.41897490 |
| 10 | 49.773832 | +7.27748524 | +1.80863902 |
| 11 | 52.970321 | +41.69243730 | -7.69139435 |
| 12 | 56.446248 | +963.37464393 | -1.28822071 |

`scout_comparison.json` retains the corresponding complex values. The change
of sign in the last two rows and the large drift in the tenth row prevent a
sign conclusion. Agreement in the first row is not promoted to certification.
These are not numerical evaluations of the signed sum over all zero events.

The derivative coefficients were built at 535 and 760 decimal digits and
retained at 75 digits; evaluation of the comparison used 45 decimal digits.
Separate ordinary function scouts used orders 200 and 1000 for a few rational
parameters. Their observed central roots were not counted on complete contours,
and no zero census or confinement statement is based on them.

An order-2500 derivative run failed to complete within its command timeout.
A prior interactive-execution request also failed before running. Neither is
counted as a completed check. No background computation is claimed.

The rigorous function-value estimate in PROOF.md is independent of these
scouts. With the conservative norm constant 1500 it is far too wide at order
1000 to certify the displayed high-height behavior. In particular the proof
supplies NO remainder for the PARAMETER derivative computed here. The scout
is retained only to prevent an unsupported discovery claim and enable a later
researcher to reproduce the failed numerical inference.
