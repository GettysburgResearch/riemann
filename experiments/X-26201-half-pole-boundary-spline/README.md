# X-26201 — Half-pole boundary-spline exact regression

This standard-library checker verifies the algebraic interfaces of the proposed
replacement for the refuted carry conditional-Hankel mechanism.

It checks:

- the exact `-233/64` review counterexample;
- the all-order Green derivative formula;
- concentration of the indefinite kernel in the weighted moments `(A,B)`;
- exact cancellation of `A` by weighted translated pairs;
- nonnegativity and quadratic exactness of the triangular B-spline Peano kernel;
- the dyadic oversupport coefficient ledger;
- exact retention and cancellation of the dyadic Mertens boundary shell;
- the binary digit endpoint identity;
- a same-sign Möbius cube mutation.

Run:

```bash
python verify.py
python -m unittest discover -s tests -v
```

The checker does **not** verify the complete source identity `L-26204.8`, the
Boundary-Jet Domination LMI, a cofinal finite minorant, positivity of the carry
profile, or RH.
