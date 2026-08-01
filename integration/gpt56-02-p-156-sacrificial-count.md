# Integration handoff — sacrificial harmonic count and direct-Schur bypass

Target stack: PR #169 / Issue #156.

## Import order

1. `L-18501` — sharp evaluation count from any high-frame subspace of
   codimension at most the radical rank.
2. `T-18501` — composition with the counted harmonic visible transfer.
3. `L-18503` — alternative direct harmonic-Schur saturation, bypassing the
   selected-zero count entirely.
4. `L-18502` — explicit Poisson corrector scale; use only with its omitted-zero
   and harmonic-survival gates.
5. `X-18501` — exact Fraction-only count/angle replay.

## Preferred production attempt A — cardinal quotient

On the exact complete harmonic packet, export:

```text
G_C
K_T^C
radical basis R
critical-line cardinal quotient basis W
B_T
```

Then certify:

```text
codim_U W <= dim R
W* (K_T^C-(B_T+beta)G_C) W > 0
R* (epsilon G_C-K_T^C) R > 0
0 <= epsilon < B_T+beta.
```

`X-18501` returns the sharp count and automatic principal-angle moat. The
cardinal quotient is preferred because global cardinal vanishing converts the
omitted-zero budget into a localization-tail estimate at a fixed selected-zero
set.

## Preferred production attempt B — direct one-end Schur witness

Export the exact harmonic Schur form

```text
S_U=B-L* C^-1 L
```

and one same-end packet `W` satisfying

```text
codim_U W <= dim R.
```

Certify directly

```text
S_U|W >= Gamma G_C|W
```

from the dimension-uniform local-Weyl theorem on the **harmonic lifts**. Then
`L-18503` gives, for any `alpha<t<Gamma`,

```text
lambda_min(S_U,G_C)
>=-alpha-beta^2/(t-alpha).
```

This route does not use `K_T`, `B_T`, the terminal-prime opposite-end cross, or
a principal angle. It retains the complete Weil cancellation before taking a
norm.

## Exact finite data required

```text
complete packet dimension
radical rank
witness rank and codimension
metric and form/evaluation Loewner boxes
radical compression endpoint alpha or epsilon
complete radical cross-residual endpoint beta
one strict witness floor
assembly radius
```

## Fail-closed rules

- The witness must lie inside the declared complete low packet.
- Source dimension alone does not prove packet containment.
- The harmonic lift, not the unlifted profile, must satisfy the frame or
  local-Weyl floor.
- A raw Gaussian corrector does not inherit cardinal omitted-zero cancellation.
- A packet-specific count does not establish complete low-index capture unless
  the packet is the actual complete low packet.
- No cofinal conclusion may be drawn from a finite numerical ladder.
