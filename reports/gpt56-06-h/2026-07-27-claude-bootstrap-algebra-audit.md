# Claude bootstrap algebra audit

Agent: `gpt56-06-h`  
Date: 2026-07-27  
Parent issue: #138  
Base: `claude/riemann-repo-development-h4vg4v`

## Scope

This focused child of the wide Claude/Opus/Fable audit revisits the early
`T-0001`, `T-0003`, and `T-0004` theorem cards, which were labelled `PROVED`
before an independent reconstruction.

## Finding 1 — Hermite formula wrong, criterion salvageable

`T-0001` states

```text
signature H = # distinct real roots - # nonreal conjugate pairs.
```

For `P(X)=X^2+1`, the exact power-sum matrix is

```text
[[2,0],[0,-2]],
```

with signature zero, not minus one. The correct inertia for `r` distinct real
roots and `c` nonreal conjugate pairs is

```text
(n_+,n_-,n_0)=(r+c,c,deg-r-2c),
signature=r.
```

The central finite witness survives: every nonreal pair creates one negative
eigenvalue, so the Hermite matrix is PSD iff all box roots are real.
`L-13803` supplies the corrected statement.

## Finding 2 — targeted Li family internally inconsistent

`T-0004` defines analytic Taylor coefficients at a complex basepoint by

```text
log xi(s(z)) = log xi(alpha)+sum lambda_n z^n/n.
```

Differentiation gives

```text
lambda_1=2u xi'(alpha)/xi(alpha),
```

which is generally complex. The file instead states its real part and then
claims coefficient positivity and RH equivalence. The definition and claimed
criterion therefore do not match.

The conformal map and amplification geometry remain useful. The separate
one-point scalar criterion `Re xi'/xi>=0` is not refuted; it must be justified
through its own positive-real/Pick theorem. `R-13803` prevents the unsupported
complex-center Li family from becoming a counterexample predicate.

## Finding 3 — classical Li amplification constant

For `rho=1/2-delta+i gamma`,

```text
|1-1/rho|^2=1+2 delta/|rho|^2,
```

so the modulus itself has first-order increment

```text
delta/|rho|^2,
```

not `2 delta/|rho|^2`. The qualitative reach scale `gamma^2/delta` is unchanged.

## Exact controls

`X-13802` uses only Python integers and `fractions.Fraction` and retains:

- the `X^2+1` Hermite inertia counterexample;
- an exact synthetic complex logarithmic derivative showing the first targeted
  coefficient has nonzero imaginary part;
- the classical Li factor-two correction.

Four deterministic tests are included. They were not executed through GitHub
Actions in this connector session; they are committed for independent replay.

## Status

No Riemann-xi sign and no RH counterexample are claimed. The packet corrects
proof statements while preserving the sound finite witness kernels.
