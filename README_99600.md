# T99600 — Three-interface hostile audit of the SHARP/common-parent closure

This add-only review successor is based on the live SHARP/Radon--Nikodym
candidate at PR #647, exact head

```text
306d1c66fe4e848efda0bd78b5475aeeed3d5563
```

It also audits the calibration-coboundary proposal in PR #648 and the fixed-row
Mellin consumer inherited from PRs #642 and #646.

**The Riemann Hypothesis remains unproved.**

## Verdict

The three most vulnerable interfaces are:

1. the compact SHARP Hall/root-source certificate;
2. promotion of the contracted `alpha`-child hazard to the native rough Euler
   source, including use of the same operator in a calibration coboundary;
3. the fixed-row noncancellation/Landau finish.

This packet obtains three different outcomes.

### Interface 1 — compact Hall and endpoint nesting

The complete compact Hall-prefix calculation is independently reconstructed
with exact outward rational square-root intervals. Every threshold
`1 <= t < 67` has margin above `7/20`; the unique worst state is

```text
t=13, x=67,
0.359317660596810 < H_13(67) < 0.359317660601486.
```

The exact SHARP child density is not a raw support cutoff. It is

```text
R_(Z|Y)(t)=1_(t<=Z) T(Z/t)/T(Y/t),
T(y)=4sqrt(y)-3.
```

The packet proves the projective cocycle

```text
R_(W|Z) R_(Z|Y)=R_(W|Y).
```

Thus the finite Hall and endpoint-restriction interfaces are closed at the
stated scalar/fixed-row scope.

### Interface 2 — native rough coefficients

This is the binding failure.

For one rough prime, the published contracted identity is

```text
P=(1-r)P+r(P-rUP)+r^2 UP.
```

It is an exact identity for `P`, but its net shifted coefficient is zero. The
native Euler factor is

```text
(I-rU)P,
```

whose shifted coefficient is `-r`. With parity-labelled export, the two
contracted shifted copies have signed magnitude `2r^2`, still not the native
magnitude `r`; the missing amount is

```text
r-2r^2>0  (p>=67).
```

Therefore the `alpha`-child operator cannot be promoted to the native
rough-prime source without an additional exact source theorem. A calibration
coboundary using that same operator telescopes perfectly but preserves the
wrong marginal.

The replacement is an exact sequential first-owner Euler identity. For ordered
rough primes, it retains every future prime inside one paired current:

```text
prod_i(I-r_i U_i)
 = s_k I
   + sum_i lambda_i (I-U_i) prod_(h>i)(I-r_h U_h).
```

This is coefficient-exact and owner-exact. Its remaining sign is the
future-completed first-difference gate `FCHD67`; that gate is nonlocal and
remains open.

### Interface 3 — analytic consumer

The large-row Euler--Maclaurin noncancellation argument is unnecessary.
If rows `2` and `3` are nonnegative, their exact numerators obey

```text
P2(z)=2*2^(-z)-1-3^(-z),
3P3(z)=5*3^(-z)-2^(-z)-1-3*4^(-z).
```

Putting `a=2^(-z)` and using `P2(z)=0` gives `3^(-z)=2a-1`; substitution in
`3P3` gives

```text
-3(a-1)(a-2).
```

For `Re z>0`, `|a|<1`, so the numerators have no common zero. This closes the
analytic finish with exact two-row algebra.

The packet also weakens PR #647's open pointwise Harnack tail: it is enough that

```text
integral_1^T (H_67^sharp(x))_- dx/x = T^o(1).
```

The negative part then has a Mellin transform holomorphic throughout
`Re s>0`; adding it to the signed Harnack density produces a nonnegative
Landau witness with the same reciprocal-zeta poles.

## Exact current frontier

```text
compact SHARP Hall                         PROVED / REPLAYED HERE
SHARP RN child map and cocycle             PROVED EXACT
raw-cutoff child map                       REFUTED
alpha-child identity as native Euler       REFUTED
sequential first-owner Euler identity      PROVED EXACT
FCHD67 future-completed current sign       OPEN / RH-BEARING
two-row noncancellation                    PROVED EXACT
fixed-row Landau consumer                  PROVED
Harnack pointwise tail                     OPEN / OVERSTRONG
Harnack subpower negative mass             SUFFICIENT / OPEN
Riemann Hypothesis                         UNPROVED
```

## Replay

```bash
python3 experiments/X-99600-three-interface-audit/verify.py \
  --output experiments/X-99600-three-interface-audit/results/verification.json
sha256sum -c T99600_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T99600_THREE_INTERFACE_HOSTILE_AUDIT
244a399ac904a10d76c9b1e454ec71b67ee87314e9b7670a96a6fbe71f730dac
```
