# NGR26 — admissible multiseed feedback with a fixed limiting target

Status: proposed component proofs, independent review required. **RH and the
subexponential regularized energy bound remain unproved.**
Parent: #838 at `459c3f78b3dc8c95ae6cc7b1bec0154499d76c9f`.

Read [PROOF.md](PROOF.md), then [ATTEMPT.md](ATTEMPT.md). This is a direct
continuation on the actual factorial/Mobius source, not another divisor graph.

For a finite polynomial feedback P of minimum degree m and maximum degree D,
use gamma shape D AND rate D, with symbol `(1+z/D)^(-D)`. The paper proves:

- Every resulting residual is unconditionally in L1 and L2, with an explicit
  proper-kernel construction and a complete future-tail bound.
- Its output is a bounded convolution of the original factorial source and
  matches its target before `m log(Y+1)`. The targets converge in L2 to a fixed
  unit-norm delayed exponential, rather than disappearing with degree.
- Each hypothetical off-line zero retains the complete exponential detection
  rate, with a constant independent of degree and coefficients. Subexponential
  regularized energy would therefore still prove RH.

A fully specified ridge-minimum sequence is proposed; its required upper bound
is not proved or numerically evaluated. Scalar feedback is still ruled out by
fixed auxiliary seed zeros. A separate diagnostic proves that raw square
integrability of both specified seed powers at every order is Lindelof-equivalent;
that assumption is not needed for the new regularization.

Run the exact bounded controls and the changed-copy tests:

```bash
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_rejections.py
python -I -S -B -O test_rejections.py
```

The tests check finite kernel algebra, formal-parameter native coefficients,
complete polynomial-tail algebra and declared synthetic ridge problems. They do
not evaluate the new actual high-degree energies or machine-prove the analysis.
No parent numerical campaign, source branch or canonical claim is modified.
