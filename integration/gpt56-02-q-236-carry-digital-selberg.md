# Integration handoff — carry–digital–Selberg proposal

Branch:

```text
agent/gpt56-02-q/236-carry-digital-selberg
```

Status:

```text
full proposed proof candidate
one load-bearing quotient-layer identity pending adversarial review
RH not independently verified
```

## New claims

- `L-23601` — exact carry interpretation, affine Möbius contraction, and closed
  finite inverse.
- `L-23602` — continuum carry profile, Mellin transform, sharp dual constant,
  and dyadic-shell bridge.
- `L-23603` — proposed dyadic conditional-Hankel/reflected-Selberg positivity
  theorem.
- `T-23601` — direct Landau deduction from `L-23603` to RH.
- `M-23601` — fail-closed review protocol.
- `X-23601` — exact finite algebra regression.

## Dependencies

Review against:

1. PR #234 `L-23405/L-23406` for the aligned shell;
2. PR #219 `L-21906/L-21907` for differenced Selberg adjoints;
3. PR #229 `L-23004` for conditional-Hankel positivity;
4. the rejected Farey geometry and first-cell Mertens firewall;
5. the standard Landau Mellin theorem and zeta functional equation.

## Merge discipline

Do not merge or promote the RH conclusion before an independent symbolic replay
of `L-23603.15`.

The following claims remain useful even if that identity fails:

```text
L-23601 exact carry Green inversion
L-23602 exact continuum/dyadic bridge
X-23601 finite regression
```

A failed quotient-layer replay classifies `L-23603/T-23601` as rejected at the
frozen commit; it does not invalidate those independent components.
