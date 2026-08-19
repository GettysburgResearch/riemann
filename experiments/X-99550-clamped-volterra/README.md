# X-99550 — Exact clamped-Volterra algebra replay

The verifier uses only Python's standard library and exact `Fraction`
arithmetic.  It checks:

- the coefficient action of the Euler/Volterra operator on the one-colour atom;
- the double clamp at activation;
- the scaled density formula;
- the reverse Green-kernel derivative jump;
- the exact coefficient dictionary of the one-colour integral identity;
- mutations that would reintroduce a boundary mode or knot atom;
- fail-closed status flags for inherited campaigns and RH.
