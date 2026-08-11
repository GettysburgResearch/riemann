# X-91014 — Safe Jordan / one-Green to Pick continuation firewall

Exact standard-library regression for `R-91005`, `L-91014`, and `L-91015`.

It checks:

- positive partial fractions for the bare one-Green control;
- positive partial fractions for the zeta-Jordan-preserving modified rational channel;
- positive finite Hankel matrices for both safe Laplace kernels;
- the exact strictly negative two-point target Pick determinant;
- the exact infinitesimal Schwarz--Pick defect;
- the symmetric polynomial functional equation.

Expected verdict:

```text
PASS_SAFE_JORDAN_PICK_CONTINUATION_FIREWALL
```

The replay proves finite rational algebra only.  It does not evaluate `xi`, formalize
the Nevanlinna--Pick/Montel theorem, prove the actual safe Pick matrices positive, or
prove RH.
