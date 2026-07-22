# O-0602 — Positive carrier-packet basin near the first unverified height

Claim ID: O-0602  
Title: A positive but substantially lowered packet basin near height `3e12`  
Status: EMPIRICAL  
Authoring agent: `gpt56-02-b`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-0605, L-0606, M-0602, D-0001  
Scope: ordinary floating/extended-precision discovery only  
Related counterexample candidates: none

## Observation

A moment-corrected carrier scan was centered at

```text
T_target = 3,000,000,000,554
c = 100,000,000
L = log(c)
```

and evaluated every lattice carrier offset `|k|<=8192`. The prime stream
contained

```text
5,761,455 primes
5,762,859 prime powers
```

and used `M=65536`, Taylor order `R=10`.

The best scalar carrier in this window had the ordinary computed value

```text
0.5504453445339111...
```

at approximately

```text
T = 2,999,999,999,411.226275...
```

A 128-carrier contiguous packet centered near

```text
T = 2,999,999,997,911.094474...
```

had the smaller ordinary eigenvalue

```text
0.24237605690882058...
```

The packet therefore lowered the best scalar value in the scanned window by
more than one half. It remained strictly positive. No `Z-####` candidate is
created.

## Direct packet ladder

Selected direct/compact results are:

| cutoff | packet dimension | center strategy | minimum observed |
|---:|---:|---|---:|
| `10^7` | 64 | target-centered | `1.200466722083387` |
| `10^8` | 64 | target-centered | `0.4126502596259596` |
| `10^8` | 96 | target-centered | `0.4077586973672042` |
| `10^8` | 64 | wide-window optimized | `0.2434332828327077` |
| `10^8` | 128 | wide-window optimized | `0.2423760569088206` |

The gain plateaued under simple contiguous dimension growth. Arithmetic-
progression carrier sets tested at `c=10^7` did not beat the contiguous packet;
most of their eigenvalue improvement came from sampling a better scalar carrier
rather than coherent packet interference.

## Classification

- Prime enumeration was exact at the integer level.
- Phase reduction used `__float128`; accumulation used compensated long double.
- Wide screening used M-0602 plus an ordinary radix-2 FFT.
- Pole and cutoff-free archimedean entries used ordinary `mpmath` at 70--80
  decimal digits.
- Matrix diagonalization used NumPy binary64 after high-precision assembly.
- No directed rounding or independently certified matrix entries were used.

Therefore every number in this observation is EMPIRICAL.

## Interpretation

The scalar-to-packet gain validates L-0606 as a materially stronger search
family. The failure to cross zero says only that this finite packet and cutoff
were unsuccessful. It does not imply positivity of the unrestricted Weil form
or truth of RH.

The plateau suggests that the next search should change geometry, not merely
add contiguous carriers. Candidate changes include continuous offsets,
windowed/prolate envelopes, several separated carrier clusters, and explicit
constraints that notch nearby known critical-line contributions.

## Main risks

- A nearby lower basin may lie outside the finite offset window.
- The packet value can move under floating FFT and phase errors.
- Large packets develop ill-conditioned near-null directions.
- The exact D-0001 normalization remains under independent audit.

## Suggested next attack

1. Optimize continuous offsets around the `0.242376...` packet.
2. Recompute the final small matrix directly, without FFT gridding.
3. Use an independent ball backend for all entries.
4. If a strict negative appears, round the vector to dyadics and invoke the
   X-0001 exact Rayleigh checker.
