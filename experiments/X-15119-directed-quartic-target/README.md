# X-15119 — Directed completed-zeta quartic target and ladder consumer

This experiment starts the target-preservation ladder of `M-15105`.

## Independent target producer

The producer uses

\[
 \xi(1/2+w)=4\int_0^\infty\Phi(u)\cosh(wu)\,du,
\]

\[
 \Phi(u)=\sum_{n\ge1}
 (2\pi^2n^4e^{9u/2}-3\pi n^2e^{5u/2})
 e^{-\pi n^2e^{2u}}.
\]

Thus `xi^(2k)(1/2)=4 int u^(2k) Phi(u) du`.  The retained calculation uses:

- exact alternating Machin bounds for `pi`;
- outward-rounded `decimal.Decimal` interval operations;
- composite Simpson integration on `[0,1]` and `[1,2]` with `h=1/20000`;
- exact symbolic fourth-derivative envelopes, inflated to the retained rational bounds;
- `n<=8`, with an analytic omitted-`n` and `u>2` budget below `1e-50`.

The resulting interval is

```text
tau4 in
[0.00007434028042155903583783846060250156947306763135396599249702198862838833,
 0.00007435011671954168375079742480823382176135706727491864190486602389042017]
```

An independent Arb/MPFR replay is recommended before theorem promotion; the
current trusted transcendental primitive is Python's correctly rounded Decimal
`exp` with guard precision and outward widening.

## Ladder status

`verify_ladder.py` is fail closed.  The retained certificate has no operator
rows because no actual finite matrices for `A_(M,N)` and `K_(M,N)` are committed
by the source manuscript.  It therefore reports `QUARTIC_TARGET_ONLY` rather
than inventing surrogate values.

Run:

```bash
python verify_ladder.py certificates/target-only.json
python -m unittest discover -s tests -v
```
