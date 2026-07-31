# X-15610 — Exact deficit-normal-form regression

This standard-library-only experiment verifies the finite algebra behind
`L-15624` and `L-15625`.

It checks two mechanisms.

1. **Packet-adapted Schur completion.** Starting from
   \[
   A=\begin{pmatrix}0&1/10\\1/10&2\end{pmatrix},
   \qquad
   D=\begin{pmatrix}4&-1/10\\-1/10&2\end{pmatrix},
   \qquad G=3,
   \]
   with packet `span(e1)`, the exact completed deficit is
   \[
   D^\sharp=
   \begin{pmatrix}
   3&-1/10\\
   -1/10&601/300
   \end{pmatrix}.
   \]
   It is positive, the new lower-model slack has identically zero packet row,
   and the reduced four-defect upper bound is
   \[
   {121\over120}<{3\over2}=\Gamma-t.
   \]
2. **Spectral normal form.** For a diagonal operator with packet eigenvalues
   zero and complement eigenvalues `5/2,4`, the exact spectral deficit has no
   clipped mass outside the packet. Replacing `5/2` by the additional low
   eigenvalue `1/2` creates uncaptured clipped trace `3/2`, strictly exceeding
   the available gap `1`.

Run:

```bash
python experiments/X-15610-deficit-normal-forms/verify.py
```

Expected verdict:

```text
PASS_EXACT_L15624_L15625_REGRESSION
```

Proof-object SHA-256:

```text
2c6a54a08b7f9f04a8c3f8eb588ca1c37484b28c6e72ec70b2026689e13634cb
```

This is an exact synthetic regression. It does not evaluate Suzuki's operator,
prove the cofinal complement trace vanishes, or prove RH.
