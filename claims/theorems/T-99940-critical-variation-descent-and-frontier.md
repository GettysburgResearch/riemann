# T-99940 — Critical-variation descent and exact RH-equivalent frontier

Claim ID: `T-99940`  
Status: **UNCONDITIONAL STRUCTURAL ADVANCE; FINAL ESTIMATE RH-EQUIVALENT**  
Created: 2026-08-20  
Base: PR #664 at `14692244bdaef90793a0c2a1a9bfd6e6b4bb1a2e`  
RH status: **unproved**

The duplicate-67 quadratic SHARP transform is globally positive. Its normalized
scale derivative satisfies the exact measure identity

\[
d\left(e^{-u}\mathfrak H_2(e^u)\right)
=\sum_n\frac{\beta(n)}{n^{3/2}}\delta_{\log n}
 +3e^{-u}\mathfrak H_1(e^u)du.
\]

Therefore the logarithmic negative mass of the linear SHARP transform is
exactly the exponentially weighted downward variation of the positive
quadratic normalization.

The quadratic normalization has finite ordinary variation and a positive
explicit limit, but `R-99940` proves that these facts do not control the
critical weighted variation.

Finally,

\[
\boxed{
RH
\iff
3\int_1^X(\mathfrak H_1(x))_-\frac{dx}{x}=X^{o(1)}.
}
\]

Thus the remaining theorem is completely isolated but not proved. No claim of
RH is made.

```text
quadratic positivity                        PROVED
critical distributional descent             PROVED
ordinary BV / positive limit                PROVED
critical negative-mass identity             PROVED
critical subpower variation -> RH            PROVED
RH -> critical subpower variation            PROVED
critical variation estimate                  OPEN / RH-EQUIVALENT
Riemann Hypothesis                           UNPROVEN
```
