# X-20808 — Prime-positive square-diagonal reconnaissance

Claim ID: `X-20808`  
Status: `EMPIRICAL — NON-DIRECTED`  
Authoring agent: `gpt56-03-w`  
Created: 2026-08-07  
Theorem target: `T-20804`

## Artifact

```text
experiments/X-20808-prime-positive-square-diagonal/
  recon.py
  README.md
  results/recon-1e7.json
```

## Retained run

```text
prime-power cutoff     10,000,000
prime-power rows       665,134
square levels n        2,...,3162
base                   a=log(2)/2
all binary64 margins   positive
```

The exact integer manifest SHA-256 is

```text
ad1fe1520966ca5c41885166f4a28a0d543922f087881175c0c15e89425fc56a.
```

At the last level, the 80-decimal-place ordinary replay gives

```text
n                       3162
r_n                     47
exp(t_n)                1.4090764204902637137340406848... < 2
positive prime ramp     12600.9672192272113120387039903...
A(2 log n)              12601.0051209049633386503562836...
r_n^2 A(t_n)            97.7098679914833611349042671...
J_a(n)                  97.6719663137313345232519737...
```

## Verification performed

```text
python3 -m py_compile recon.py
python3 recon.py --limit 10000000 --digits 80
```

The script explicitly checks strict ordering of the prime-power manifest and
retains the manifest digest.

## Proof boundary

The prime-power enumeration is exact. The transcendental scan is binary64 and
the two replays use ordinary mpmath, not outward intervals. The result is a
normalization and scheduling check only. It neither certifies any finite sign nor
establishes the cofinal theorem.