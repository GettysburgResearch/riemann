# X-24504 — Central-Neumann Haar and positivity mutation

Status: `EXACT_RATIONAL + DIRECTED_DECIMAL FINITE CHECK`  
Scope: finite algebra for `L-24523/L-24525` and the exact counterexample in `R-24504`  
RH: not proved

Run:

```bash
python3 experiments/X-24504-central-neumann-haar/verify.py \
  > experiments/X-24504-central-neumann-haar/results/verification.json
```

The checker uses only the Python standard library.

## Exact rational layer

At a deliberately irregular rational target and endpoint `X=64`, it verifies:

- the descending central-fragmentation recurrence;
- the binary tent Green kernel;
- the dyadic Haar-block formula;
- `A_X(n)=G_X(n)-G_X(n+1)`;
- `G_X(n)=U_X(n)+G_X(2n-1)+G_X(2n)`;
- exact saturation of every integer carry column;
- exact dyadic-shell linearity with `Y=floor(X/2)`.

Representative counts:

```text
recurrence rows   63
saturation rows   63
shell rows        63
tent terms       465
Haar terms       321
```

## Directed counterexample layer

At the actual critical target

```text
w_X(q)=q^(-1/2) log(X/q),
X=10050,
n=11,
```

100-decimal outward rounding proves

```text
A_X(11) < 0.
```

The full interval is retained in `results/verification.json` and in `R-24504`.
This refutes pure central pointwise positivity, not the exact signed saturation,
CNVD/CHSS, another balanced producer, or RH.

## Retained digests

```text
verify.py SHA-256
7709890d3ee96441e7b7d5b366a28280eadb34c45ee7970a110e78e43ff63f13

results/verification.json SHA-256
fb023ed7ae9ca491a2eb4a54f9b9177ec3efea9e3153a10baa66f2f8c15c9185

payload content_sha256
67c579f67093985f436ac98f25e6aac4dce52a9a4ccef1a0e231763bdea34d7a
```

The checker certifies no asymptotic shell-variation estimate and no statement
about the Riemann Hypothesis.
