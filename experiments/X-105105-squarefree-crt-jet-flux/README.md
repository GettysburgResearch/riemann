# X-105105 — Fixed-window CRT jet-selector verification

This lightweight exact replay verifies L/T/R/M-105105.

It checks:

- finite primary CRT selectors for actual \(P=F/F'\) and
  \(Q=F^2/(F'F'')\) poles;
- independent Taylor-series residues of both weighted quotients;
- simple, flat, mixed-multiplicity, common, even-stationary, and nonreal
  fixtures;
- a nontrivial real/even selector with partial common cancellation
  \((m,r,s)=(1,0,3)\);
- annihilation of \(F''\)-only and every other nontarget actual pole;
- the load-bearing multiplicity factor in the second selector;
- the failure of squaring the first weighted flux;
- root-free square-free polynomial carrier construction and all-root traces;
- a nonlinear \((x^2-1)^3\) stratum that authenticates \((A_r')^r\);
- fail-closed event, target, and factor manifests;
- the frozen T-105104 dependency.

Run from repository root:

    python -B experiments/X-105105-squarefree-crt-jet-flux/verify.py
    python -B -m unittest discover \
      -s experiments/X-105105-squarefree-crt-jet-flux/tests \
      -p "test_*.py" -v
    python -B -O -m unittest discover \
      -s experiments/X-105105-squarefree-crt-jet-flux/tests \
      -p "test_*.py" -v

Expected verdict:

    PASS_T105105_FIXED_WINDOW_CRT_JET_SELECTORS

Expected proof digest:

    3edde4fdb651ae0c3781e4f832884f0d7c81247edd3b5a151c6b2c54f051cf05

The replay uses only standard-library rational and Gaussian-rational
arithmetic on degree-at-most-seven primary moduli. It performs no Xi
evaluation, zero scan, floating-point root isolation, contour quadrature,
broad suite, or heavy computation.
