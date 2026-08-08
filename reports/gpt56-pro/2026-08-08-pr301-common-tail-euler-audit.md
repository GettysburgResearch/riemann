# Adversarial audit of PR #301's recombined common-tail Euler step

## Frozen scope

```text
Repository: gfreund123/riemann
PR:         #301
Frozen head: 060943ce211f97b59c1ce60e1a74dff8154dceb1
Review branch: review/gpt56-pro-301-common-tail-euler-audit
```

This audit targets the load-bearing sequence

```text
recombine shifted-even and unshifted-odd cutoff legs
-> type D_k=A_k-B_k as a positive Hausdorff sequence
-> apply an alternating Euler transform to D_k
-> emit a finite positive Pascal source with 2^-M remainder damping
-> zero paired-tail Cycle Debt
-> RH.
```

## Verdict

```text
positive Hausdorff typing of D_k          VERIFIED
positivity of finite differences          VERIFIED
alternating remainder identity for D_k    VERIFIED AS AN ARTIFICIAL SERIES
identification with actual common tail    FALSE
2^-M recombined-tail damping              UNAVAILABLE
complete finite Pascal source manifest    UNPROVEN
T-29802 as an RH proof                    REJECTED AS WRITTEN
Riemann Hypothesis                        UNPROVED
```

## Decisive calculation

For

\[
A_k=(2kq-1)^{-s},
\qquad
B_k=((2k+1)q)^{-s},
\qquad
D_k=A_k-B_k,
\]

the actual recombined common tail is

\[
Q_K=\sum_{k\ge K}D_k.
\]

The alternation in the original interleaved source

```text
+A_K,-B_K,+A_(K+1),-B_(K+1),...
```

has already been consumed by the pairing. `L-29808.6` introduces a new series

\[
\widetilde Q_K
=\sum_{k\ge K}(-1)^{k-K}D_k,
\]

which is not `Q_K`.

If

\[
D_k=\int y^k\,d\sigma(y),
\]

then

\[
Q_K=\int\frac{y^K}{1-y}\,d\sigma(y),
\qquad
\widetilde Q_K=\int\frac{y^K}{1+y}\,d\sigma(y).
\]

The denominators are different.

At the elementary control `q=s=K=1`,

\[
D_k=\frac1{2k-1}-\frac1{2k+1},
\]

so

\[
\sum_{k\ge1}D_k=1,
\qquad
\sum_{k\ge1}(-1)^{k-1}D_k=\frac\pi2-1.
\]

The first two terms already give the exact rational contradiction

\[
\frac45=D_1+D_2
\ne
D_1-D_2=rac8{15}.
\]

## Correct surviving structure

The actual positive common tail has an exact interlacing telescope. Define

\[
G_k=((2k-1)q)^{-s}-(2kq-1)^{-s}\ge0.
\]

Then

\[
B_{k-1}-B_k=G_k+D_k,
\]

and hence

\[
\sum_{k=K}^{L}D_k
=B_{K-1}-B_L-\sum_{k=K}^{L}G_k.
\]

Passing to the limit,

\[
\boxed{
\sum_{k\ge K}D_k
=B_{K-1}-\sum_{k\ge K}G_k.
}
\]

Thus the entire infinite common tail is one first-boundary atom minus an explicit positive interlacing reserve. For `q=1`, the reserve vanishes and the tail telescopes exactly to that one atom.

This is stronger structural information than a generic norm bound, but it does not by itself emit the capacity-weighted Pascal flow required by PR #272.

## Exact replay

`X-30101-recombined-tail-euler` uses only integers and `fractions.Fraction` and verifies:

```text
ordinary two-term common tail        4/5
artificial alternating tail          8/15
Hausdorff ordinary kernel            1/2
Hausdorff alternating kernel         1/6
interlacing identity rows            10,496
direct pair recombination rows        2,277
```

Retained digest:

```text
6d0b3839f4c1062229a226535abd6fc6e1289b47ac57b13a7a8fd1972fe99338
```

## Corrected frontier

A viable repair must choose one exact route.

### Route A — retain the original alternation

Apply finite Euler transformation to the original interleaved sequence and emit every mixed shifted/unshifted finite-difference source label. Pairing may occur only after that exact transformation.

### Route B — use the ordinary interlacing tail

Replace the invalid Euler denominator by the exact boundary-minus-reserve formula of `L-30102`, then construct a source-bound carry/Pascal map for:

```text
one first-boundary collar atom
-
positive interlacing reserve.
```

No `2^-M` damping may be claimed on this route without a new exact identity.

## Final disposition

PR #301 contains important correct algebra, but the submitted full proof does not survive this source check. The corrected interlacing identity is pushed as a repair seed; an unconditional RH proof has not yet been obtained.
