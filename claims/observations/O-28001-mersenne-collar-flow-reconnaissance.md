# O-28001 — Mersenne-collar fragmentation reconnaissance

Claim ID: `O-28001`  
Title: Finite linear programs find exact-support saturation flows with slowly growing Mersenne collar mass  
Status: **FLOATING DISCOVERY ONLY / NOT A CERTIFICATE**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-28002`, `T-28001`

A finite LP was assembled with one variable for every split licensed by `MCF`:

```text
non-Mersenne n:
    n-L(n)<j<L(n), with symmetric duplicates removed;

Mersenne n=2^r-1:
    j=1, representing either extreme orientation.
```

The equality constraints were all carry columns

\[
\sum_{n,j}d(n,j)\chi_{n,q}(j)
=q^{-1/2}\log(X/q),
\qquad 2\le q\le X,
\]

and the objective minimized total Mersenne-edge mass.

Ordinary SciPy/HiGHS binary64 runs returned feasible solutions at every retained endpoint:

| `X` | minimum displayed Mersenne mass |
|---:|---:|
| 10 | 0.5239776385 |
| 15 | 0.8008345182 |
| 20 | 0.8603898930 |
| 30 | 1.1512529887 |
| 40 | 1.2005390491 |
| 50 | 1.3100398692 |
| 75 | 1.5597781763 |
| 100 | 1.6320575938 |
| 150 | 1.9168266842 |
| 200 | 1.9720845116 |
| 300 | 2.2775458903 |

At `X=100`, the Mersenne masses were approximately

```text
n=3    1.0410538274
n=7    0.3993287950
n=15   0.1634251766
n=31   0.0248145896
n=63   0.0034352053
```

The collar contribution decays rapidly with dyadic depth in this finite sample.

A deterministic rule using the central split on non-Mersenne rows and the extreme split on Mersenne rows also often remains nonnegative, but it develops sparse negative node coefficients at some endpoints. Those negatives are a concrete target for Pascal-cycle redistribution; they may not be discarded.

These computations are neither directed nor exact. They do not establish finite feasibility at arbitrary `X`, the subpower collar estimate, `MCF`, or RH. They are retained only to guide the search for a constructive half-scale recursion.