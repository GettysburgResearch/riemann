# L-105052 — Unconditional Vinogradov–Korobov envelope for the HHFE energy

Claim ID: `L-105052`
Status: **PROVED modulo one standard cited classical input (L-105052.0, Walfisz-strength twisted Möbius bound; labeled EXTERNAL-CLASSICAL, not re-proved) — RH not assumed, not claimed; gate HHFE102010 remains OPEN**
Created: 2026-08-22
Agent: claude (external reviewer lane; gate-assault lane A4)
Depends on: `L-102010`, `T-102001` @ PR #696 `origin/research/gpt56-sol/102000-parabolic-bessel-vaughan-correction` `f4016db548afceb31b150547cb6cd48b4cddb77d`; `L-103100`–`L-103102` @ PR #702 `origin/research/gpt56-pro/103100-fractional-hankel-near-collision` `89f995450977c3590aada0c1447a7e6af7fcd9ac`.
Replay: `experiments/X-105053-assault/` (hhfe_energy.py; results.json; Gram identity `D + O = ∫|H|² dY/Y` replayed to ≤ 2.1e-14 at every sampled X).
RH status: **unproved, not addressed**

Notation of L-102010/L-103102: `U = floor(X^{1/3})`, `N = floor(X/U)`,
`P_{U,N}(s) = sum_{U<n<=N} h_U(n) n^{-s}` with `h_U = (mu 1_{>U}) * eta`,
`w(gamma) = |hatA_-(i gamma)|^2`, `hatA_-(s) = (1-2^{-s})(1-sqrt2 2^{-s})/s`,
energy `H(X) = (1/2pi) int w(gamma) |P_{U,N}(1/2+i gamma)|^2 dgamma` (L-103102.1).

**(L-105052.0)** [standard input; VK/Walfisz strength; cited, not re-proved —
EXTERNAL-CLASSICAL] For every `K >= 1` there is `c = c(K) > 0` with, uniformly
for `|gamma| <= exp(K (log x)^{3/5})`,

```
sum_{n<=x} mu(n) n^{-i gamma} << x exp(-c (log x)^{3/5} (loglog x)^{-1/5}).
```

[Perron for `1/zeta(s+i gamma)`, contour shift into the Vinogradov–Korobov
zero-free region, `1/zeta << log^{2/3+eps}` there, `T = exp(K'(log x)^{3/5})`.]

**(L-105052.1)** [exact bilinear shape; elementary] Since every divisor `d > U`
of `n <= N` has cofactor `e = n/d < N/U`,

```
P_{U,N}(s) = sum_{e<=N/U} eta(e) e^{-s} sum_{U<d<=N/e} mu(d) d^{-s},
```

an exact Type-II factorization: positive smooth factor `eta` (length `<= N/U ~ X^{1/3}`),
rough Möbius factor of length in `(U, N]` (Type-II range).

**(L-105052.2)** [THE BOUND] Unconditionally,

```
H(X) << X^{2/3} exp(-c (log X)^{3/5} (loglog X)^{-1/5}),
```

hence `E(L) = int_{2^L}^{2^{L+1}} H dX/X << 2^{(2/3)L} exp(-c' L^{3/5 - o(1)})`.

Proof. `Gamma_0 = exp((log N)^{3/5})`.
(i) `|gamma| <= Gamma_0`: partial summation on the inner sum of (L-105052.1)
using (L-105052.0) at every `t in [U, N/e]` (worst point `t = U`,
`log U = (1/3+o(1)) log X`) gives
`|sum_{U<d<=N/e} mu(d) d^{-1/2-igamma}| << (N/e)^{1/2} exp(-c(log X)^{3/5-o(1)})`;
then `|P| <= sum_e eta(e) e^{-1/2} * (...) << (N log N)^{1/2} exp(-c(...))` using
`sum_{e<=x} eta(e)/e <= prod_{p<=x}(1-1/p)^{-1/2} << (log x)^{1/2}`.
Total weight `int_R w = 2pi * 3 log 2` is finite, so this range contributes
`<< N log N exp(-2c(...))`.
(ii) `|gamma| > Gamma_0`: `w(gamma) <= (2+2sqrt2)^2/gamma^2`; Montgomery–Vaughan
mean value on dyadic blocks `|gamma| ~ T`:
`int_{|gamma|~T} |P(1/2+igamma)|^2 << T sum h_U^2(n)/n + sum h_U(n)^2
<< T (log N)^{O(1)} + N (log N)^{O(1)}`; the weighted sum over `T = 2^j >= Gamma_0`
is `<< (log N)^{O(1)}/Gamma_0 + N (log N)^{O(1)}/Gamma_0^2 << N exp(-2(log N)^{3/5})`.
Combine with `log N = (2/3) log X`. QED.

Remark: this saves `exp((log X)^{3/5-o(1)})` over the trivial `alpha = 2/3`
bound (which is sharp for absolute values — see O-105054), and consumes Möbius
parity only analytically, through `1/zeta` on the VK region — never via absolute
values (R-95600 compliant). It is the exact ceiling of single-window technology;
the obstruction analysis is O-105054.

## Falsifiers

A computation showing `E(L)` exceeding the (ii)+(i) assembled envelope at the
stated ranges; an error in the Type-II factorization (checked exactly in replay:
`h_U(n) = sum_{e | n, n/e > U} eta(e) mu(n/e)`); failure of the Gram identity in
replay; withdrawal of the classical input's strength class.
