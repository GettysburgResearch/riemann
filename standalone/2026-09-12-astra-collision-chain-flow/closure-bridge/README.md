# CJB26 — joint moment/defect bridge and an eight-moment infinite chain

**Proposed component proofs, pending independent review. RH is not proved.**
This add-only child continues PR875; it does not replace the earlier packet.

The main positive construction is an actual connected infinite ferromagnetic
chain matching native theta moments 2,4,6,8 and all three real-field growth
coefficients, with q in a radius-10^-6 box about 0.018145167180821594. Its
standardized tenth-moment error is strictly between .029 and .032. Existence
is proved by a full-source/full-tail Brouwer enclosure, not by a floating fit,
an independent-tail substitution, or an assumption that q can tend to zero.
Uniqueness is not claimed.

The joint bridge gives an explicit finite-moment error budget against a finite
ferromagnet that excludes nonreal gamma zeros and controls the complete
weighted defect. A specified unbounded sequence of successful finite matches
would close RH; existence of that sequence remains OPEN. An imported native
N5 defect yields a rigorous finite-order obstruction to fitting that *fixed*
stage indefinitely. A graph-wide bound on correlation variance explains why
vanishing interaction cannot supply an all-order theta realization.

The arithmetic continuation sharpens the native crossing identity to
F_((Y+1)^2-1)-F_Y=D_Y+C_Y+an explicit term of absolute value less than2.
It does not establish the missing upper bound on C_Y.

Read PROOF.md, then SOURCES.md and VALIDATION.md. The new checker expects this
folder directly below the unchanged CCF26 packet and authenticates its four
parent dependencies. It uses only Python's standard library.

```bash
python -S -B certify_chain.py --check chain_result.json
python -S -O -B certify_chain.py --check chain_result.json
python -S -B test_checks.py --part bounded
python -S -O -B test_checks.py --part bounded
python -S -B test_checks.py --part full
python -S -O -B test_checks.py --part full
```

The full part includes a fresh accepting source reconstruction and a fresh
reconstruction that must reject a changed numerical receipt. The bounded
part checks exact arithmetic/FK identities, direct spin-enumeration values
and derivatives, rational infinite-tail majorants, and four actual CLI
refusals. Execution modes are not independent arithmetic implementations.
No all-order native feasibility, new zeta zero, repository-wide scientific
validation or formal proof is supplied.
