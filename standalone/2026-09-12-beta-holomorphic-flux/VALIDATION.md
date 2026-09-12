# Validation record

Status: author-executed finite algebra tests. Independent mathematical review remains outstanding. This record does not accept RH, a native zero sign, or any entire analytic proof.

## Commands actually run

In a clean local packet directory:

```sh
python -I check.py --emit results.json --self-test
python -I -O check.py --check results.json --self-test
```

Both passed. Normal and optimized modes were also replayed after clean ZIP extraction; both passed against the retained results. Each self-test rejects four altered records through the same fresh-reconstruction acceptance function.

The primitive arithmetic is exact Python integers and `fractions.Fraction`, with a small exact field implementation for `Q(sqrt(2),sqrt(3))`. No floating value or external special-function library enters the accepting calculation. The checker independently compares the moment recurrence with gamma rising factorials and the reciprocal sinh series at the endpoints, through order 12. Five rational parameters are tested. This finite sample is not the proof of the all-parameter assertions.

The checks also include the exact antiderivative/radical reduction of the continuum norm majorant, the two beta quadratic bounds, the uniform-scale quadratic bound, strict complex-ball invariance and contraction, normalization margin, weight edge identities, and 24 persistent-multiplicity velocity cases. The triple-collision control is synthetic polynomial algebra, not a native root isolation.

Exploratory SciPy maximization and SymPy simplification were used to choose and derive the weight constants. They are not retained as certificates or trusted in acceptance. The final norm bound is the analytic pointwise maximization and exact integral in PROOF.md, backed by the exact algebra replay. The initial smaller cubic/decaying weights were design exploration, not accepted competing results.

## What was not done

No numerical evaluation of the native regularized flux, no primitive xi-value certificate, no native collision tracking, no all-height zero census, no interval integration campaign, no complete predecessor replay, no whole-repository validation, and no Lean build were performed. The analytic proof has been author-checked, not independently reviewed or machine verified.

## Review priorities and smallest open gate

Review the all-t contraction integral; the state-space closure and bilinear bounds; the complex-parameter patching; the Mellin subtraction signs/domain; the persistent-multiplicity/Puiseux argument; and the two ordered limits of the regularized balance.

The required completion is a source-specific upper bound by zero on the limiting signed integral in PROOF.md (32). It is not established by any passing check. Removing this open gate would require an additional mathematical proof, not changing a status label.
