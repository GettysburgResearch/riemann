# Report — the ambient complement is closed by canonical finite augmentation

Agent: `gpt56-03-n`  
Issue: #189  
Stack: PR #186

## Result

Given any finite structured packet `U0` and any complete lower model

\[
A\ge gI-D,\qquad D\ge0\text{ compact},
\]

choose `0<Gamma<g`, compress `D` to `U0^perp`, and adjoin its spectral subspace
above `g-Gamma`.

The enlarged packet

\[
U=U_0\oplus\operatorname{Ran}
1_{(g-\Gamma,\infty)}(Q_0DQ_0)
\]

satisfies exactly

\[
A|_{U^\perp}\ge\Gamma I.
\]

The augmentation is finite and rank-minimal for the positive-deficit lower
model.

## Main correction to the frontier

The complement floor is not the final RH theorem once finite augmentation is
allowed. It is an exact compact-deficit construction.

What remains is the sign of the enlarged finite selected-real-zero kernel. A
hypothetical off-line cardinal direction can live in that finite kernel, so the
finite sign statement remains RH-bearing even though the ambient complement is
strictly positive.

## Validation

- exact Fraction-only replay: pass;
- nine adversarial tests: pass;
- proof object:
  `20a367a919d3e8e7fcaca91a46ab8b61cb836082c6abf83eabd535a0340d44b8`.

## Status

The boxed complement statement is proved relative to the complete lower model.
No RH proof is claimed.
