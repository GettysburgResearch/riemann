# X-19842 — Exact two-mode off-line quartet regression

This standard-library Fraction checker verifies the determinant identity used by
`L-19866` on the synthetic off-line parameter `Omega=3+i` and two distinct real
frequencies `1,2`.

It checks exactly that

```text
det Re(u u^T) = -[Im(u_1 conjugate(u_2))]^2 < 0
```

and that multiplying the evaluation vector by an arbitrary common complex phase
and amplitude preserves strict indefiniteness.
