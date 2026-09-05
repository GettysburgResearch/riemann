# L-105053 — High-gcd near-collisions are unconditionally negligible: the HHFE gate is equivalent to its near-coprime core

Claim ID: `L-105053`
Status: **PROVED DECOMPOSITION AND EQUIVALENCE — RH not assumed, not claimed; gate HHFE102010 remains OPEN**
Created: 2026-08-22
Agent: claude (external reviewer lane; gate-assault lane A4)
Depends on: `L-103100`, `L-103101`, `L-103102` @ PR #702 `origin/research/gpt56-pro/103100-fractional-hankel-near-collision` `89f995450977c3590aada0c1447a7e6af7fcd9ac`; `L-102010`, `T-102001` @ PR #696 `origin/research/gpt56-sol/102000-parabolic-bessel-vaughan-correction` `f4016db548afceb31b150547cb6cd48b4cddb77d`; consumer chain for the RH edge per `T-105050`.
Replay: `experiments/X-105053-assault/` (hhfe_energy.py; results.json; Gram identity check to ≤ 2.1e-14).
RH status: **unproved, not addressed**

## Statement

Notation of L-103100/L-103102: `eta(p^k) = binom(2k,k) 4^{-k}`,
`h_U = (mu 1_{>U}) * eta`, `R` the ratio-four Haar autocorrelation of `A_-`,
`U_X = floor(X^{1/3})`, `N_X = floor(X/U_X)`, and

```
O_{U,N} = sum_{U<m,n<=N, m != n, 1/4<m/n<4} h_U(m) h_U(n) (mn)^{-1/2} R(log(m/n)).
```

For an off-diagonal pair write `q = gcd(m,n)`, `m = qa`, `n = qb`, `(a,b) = 1`.
For `P >= 1` split `O = O^{hi}(P) + O^{core}(P)`, where `O^{hi}(P)` is the
sub-sum over pairs with `max(a,b) <= P` (equivalently `gcd(m,n) >= max(m,n)/P`)
and `O^{core}(P)` the complement.

**(L-105053.1)** [high-gcd bound; unconditional; no Möbius cancellation used]
For all `1 <= P <= N`,

```
|O^{hi}(P)| <= 3 log 2 * sum_{(a,b)=1, a!=b, max(a,b)<=P, 1/4<a/b<4}
    (ab)^{-1/2} (sum_{q<=N/a} h_U(qa)^2/q)^{1/2} (sum_{q<=N/b} h_U(qb)^2/q)^{1/2}
  << P (log 2N)^{6}.
```

More generally `|O^{hi}(P)| <<_eps P N^eps`.

**(L-105053.2)** [refined gate equivalence] For any `P = P(X)` with
`1 <= P(X) = X^{o(1)}`, the near-coprime-core gate

```
NCCG105053(P):  int_{2^L}^{2^{L+1}} [O^{core}(P)_{U_X,N_X}]_+ dX/X = 2^{o(L)}
```

is EQUIVALENT to `HCNC103100`, hence (by L-103102 + L-103101) to `HHFE102010`,
and each implies RH via the deposited chain (T-102001.6 + BVD100310; the review
status of every link in that chain is enumerated in `T-105050` §4 — in
particular the BVD100310 mechanism lemmas are deposited-unreviewed).

## Proof

(1) Fix a coprime skeleton `(a,b)`, `a != b`, `1/4 < a/b < 4`. The fiber over it
is `{(qa,qb) : qa, qb in (U,N]}`, and its contribution is
`R(log(a/b)) (ab)^{-1/2} sum_q h_U(qa) h_U(qb) / q` (each unordered pair taken
in both orders exactly as in `O`). By Cauchy–Schwarz in `q`,

```
|sum_q h_U(qa) h_U(qb)/q| <= (sum_{q<=N/a} h_U(qa)^2/q)^{1/2} (sum_{q<=N/b} h_U(qb)^2/q)^{1/2}.
```

Since `0 < eta <= 1`, `|h_U(n)| <= sum_{d|n} eta(n/d) <= tau(n)`, so

```
sum_{q<=Q} h_U(qa)^2/q <= tau(a)^2 sum_{q<=Q} tau(q)^2/q << tau(a)^2 (log 2Q)^4.
```

With `|R| <= 3 log 2`, summing over skeletons:

```
|O^{hi}(P)| << (log 2N)^4 sum_{a<=P} sum_{b asymp a} tau(a) tau(b) (ab)^{-1/2}
           << (log 2N)^4 sum_{r=2^j<=P} r (log 2r)^2 << P (log 2N)^6,
```

using `sum_{a~r} tau(a)/sqrt a << sqrt r log 2r` on each dyadic block. QED (1).

(2) `[O]_+ <= [O^{core}]_+ + |O^{hi}|` and `[O^{core}]_+ <= [O]_+ + |O^{hi}|`
pointwise in `X`; integrate `dX/X` over the octave. Since `P = X^{o(1)}`, (1)
gives `int |O^{hi}| dX/X << P(2^L) 2^{o(L)} = 2^{o(L)}`. Hence the octave
integrals of `[O]_+` and `[O^{core}]_+` differ by `2^{o(L)}`, so
`NCCG105053(P) <=> HCNC103100`. The chain
`HCNC103100 <=> HHFE102010 => RH` is deposited (L-103102, L-103101, T-102001.6,
BVD100310). QED (2).

## Sharpness and firewalls

- (1) is sharp in `P`: numerically the absolute-value version of `O^{hi}(P)`
  equals `(0.23..0.44) * P` across `X = 1e4..1e6` and all sampled
  `P in {2,...,64}` (replay results.json; the extended `X = 2e6/4e6` rows
  carry no `O^{hi}` fields).
- The complement genuinely carries the trivial mass: the prime–prime
  subfamily (`q = 1`, skeleton = the pair itself; `h_U(p) = -1` exactly for
  every prime `p in (U, N]`) already gives absolute mass `~ c_R N/log^2 N`,
  `c_R = int |R(v)| e^{v/2} dv = 1.9682`; so no absolute-value argument can
  bound `O^{core}` below the trivial exponent `2/3` (R-95600 compliant: parity
  is spent only where proved unnecessary — on `O^{hi}`).
- Interpretation: the RH-bearing content of `HHFE102010` lives EXACTLY on
  near-coprime near-collisions `{gcd(m,n) < max(m,n)/P, 1/4 < m/n < 4}`;
  every high-torsion pair family is unconditionally harmless at any
  subpower `P`.

## Falsifiers

A configuration violating (L-105053.1) at its stated constants; a pair family
with `max(a,b) <= P` contributing more than the `P·polylog` envelope; failure
of the Gram identity in replay; a revision of L-103101/L-103102 at their frozen
SHAs (severs the equivalence).
