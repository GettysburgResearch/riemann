# Review addendum — T-105105 fixed-window CRT jet selectors

Checkpoint base:
75bf12b76014da6ea983ac1dc8083aaac79132ce.

Review the new weighted identities only after authenticating the complete
interior \(F',F''\) event manifest and the actual post-cancellation pole
orders. The selector congruences are primary: target terms are
\(w^{r-1}\) and \(r w^{2r-2}\), while every nontarget selector vanishes to
the full actual pole order.

The square-free polynomial construction is a separate all-root corollary.
Do not relabel its algebraic trace as a real-window moment without certified
localization or explicit nonreal correction.

Replay:

    python -B experiments/X-105105-squarefree-crt-jet-flux/verify.py
    python -B -m unittest discover -s experiments/X-105105-squarefree-crt-jet-flux/tests -p "test_*.py" -v
    python -B -O -m unittest discover -s experiments/X-105105-squarefree-crt-jet-flux/tests -p "test_*.py" -v

Expected:

    PASS_T105105_FIXED_WINDOW_CRT_JET_SELECTORS
    3edde4fdb651ae0c3781e4f832884f0d7c81247edd3b5a151c6b2c54f051cf05

The Xi manifest, selector norm, weighted edge estimates, cofinal limit,
RCMV104530, and RH remain open.
