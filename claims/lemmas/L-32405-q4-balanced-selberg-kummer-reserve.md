# L-32405 — The Q=4 Euler–Blaschke source has a complete balanced Selberg–Kummer reserve

Claim ID: `L-32405`  
Title: On every carry row with split ratio in `[1/4,3/4]`, the main-pole-killing `Q=4` generalized-prime square strictly dominates its complete Selberg forcing  
Status: **PROPOSED COMPLETE THEOREM — ANALYTIC TAIL PLUS EXACT FINITE REPLAY; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32404`; the elementary Chebyshev estimate `psi(x)<=2 x log 2`; finite carry algebra  
Scope: source-matched balanced carry rows for the `Q=4` Euler–Blaschke Dirichlet system; no RH conclusion or block recurrence

## 1. The `Q=4` system

Put

\[
 B_4(s)=\frac{1-4^{1-s}}{(1-4^{-s})\zeta(s)},
 \qquad
 A_4=B_4^{-1}.
\]

By `L-32404`, the generalized von Mangoldt sequence is

\[
 \boxed{
 \Lambda_4(q)
 =\Lambda(q)
 +(\log4)\sum_{r\ge1}(4^r-1)\mathbf1_{q=4^r}
 \ge0.
 }
 \tag{L-32405.1}
\]

Let

\[
 C_4=\Lambda_4\log+\Lambda_4*\Lambda_4.
 \tag{L-32405.2}
\]

For integers `n>=2` and `0<=j<=n`, define

\[
 \chi_{n,q}(j)
 =\left\lfloor\frac nq\right\rfloor
  -\left\lfloor\frac jq\right\rfloor
  -\left\lfloor\frac{n-j}{q}\right\rfloor
 \in\{0,1\},
\]

\[
 \boxed{P_4(n,j)=\sum_{q\le n}\Lambda_4(q)\chi_{n,q}(j),}
 \tag{L-32405.3}
\]

and

\[
 \boxed{S_4(n,j)=\sum_{q\le n}C_4(q)\chi_{n,q}(j).}
 \tag{L-32405.4}
\]

The reserve is

\[
 \mathcal R_4(n,j)=P_4(n,j)^2-S_4(n,j).
 \tag{L-32405.5}
\]

## 2. The theorem

For every integer

\[
 n\ge4,
 \qquad
 \frac n4\le j\le\frac{3n}{4},
\]

one has

\[
 \boxed{
 0\le S_4(n,j)<P_4(n,j)^2.
 }
 \tag{L-32405.6}
\]

Moreover, for every `n>=4735` in the same balanced cone,

\[
 \boxed{
 \mathcal R_4(n,j)>\frac1{20}P_4(n,j)^2.
 }
 \tag{L-32405.7}
\]

Thus the source which kills the deterministic zeta pole and is all-pass on the critical line still has a uniform strict Selberg–Kummer reserve on the complete fixed balanced cone.

## 3. Lower bound for the generalized Kummer profile

Because `Lambda_4>=Lambda`, Kummer's identity gives

\[
 P_4(n,j)
 \ge\sum_q\Lambda(q)\chi_{n,q}(j)
 =\log\binom nj.
 \tag{L-32405.8}
\]

By symmetry assume `j<=n/2`. In the balanced cone, `j>=n/4`. The product formula gives

\[
 \binom nj
 =\prod_{r=0}^{j-1}\frac{n-r}{j-r}
 \ge\left(\frac nj\right)^j
 \ge2^j.
\]

Hence

\[
 \boxed{
 P_4(n,j)\ge\frac n4\log2.
 }
 \tag{L-32405.9}
\]

## 4. Elementary mass bound for `Lambda_4`

Write

\[
 L_4(x)=\sum_{q\le x}\Lambda_4(q).
\]

The elementary Chebyshev estimate

\[
 \psi(x)\le2x\log2
 \tag{L-32405.10}
\]

follows, for example, by bounding each dyadic increment of `psi` by the logarithm of a central binomial coefficient and summing the resulting geometric series.

The local `Q=4` correction obeys

\[
\begin{aligned}
 &(\log4)\sum_{4^r\le x}(4^r-1)\\
 &\qquad<\log4\sum_{4^r\le x}4^r
 \le\frac43x\log4
 =\frac83x\log2.
\end{aligned}
\]

Therefore

\[
 L_4(x)
 <\frac{14}{3}x\log2.
\]

Using the elementary rational upper bound `log 2 < 5/7`,

\[
 \boxed{L_4(x)<\frac{10}{3}x.}
 \tag{L-32405.11}
\]

## 5. Complete Selberg forcing is only `O(n log n)`

Since every `C_4(q)` and every carry indicator is nonnegative,

\[
 S_4(n,j)\le\sum_{q\le n}C_4(q).
 \tag{L-32405.12}
\]

The logarithmic part is bounded by

\[
 \sum_{q\le n}\Lambda_4(q)\log q
 \le\log n\,L_4(n)
 <\frac{10}{3}n\log n.
 \tag{L-32405.13}
\]

For the convolution part,

\[
\begin{aligned}
 \sum_{q\le n}(\Lambda_4*\Lambda_4)(q)
 &=\sum_{a\le n}\Lambda_4(a)L_4(n/a)\\
 &<\frac{10}{3}n
   \sum_{a\le n}\frac{\Lambda_4(a)}a.
\end{aligned}
 \tag{L-32405.14}
\]

Partial summation and (L-32405.11) give

\[
 \sum_{a\le n}\frac{\Lambda_4(a)}a
 <\frac{10}{3}\left[1+\log\frac n2\right].
 \tag{L-32405.15}
\]

For `n>=4735`, we have `n>4096`, and the rational lower bound `log2>69/100` gives

\[
 \log n>12\log2>8.28>24(1-\log2).
\]

Consequently

\[
 1+\log(n/2)<\frac{25}{24}\log n.
 \tag{L-32405.16}
\]

Combining (L-32405.12)--(L-32405.16),

\[
\begin{aligned}
 S_4(n,j)
 &<\left[
   \frac{10}{3}
   +\left(\frac{10}{3}\right)^2\frac{25}{24}
   \right]n\log n\\
 &=\frac{805}{54}n\log n\\
 &<\boxed{15n\log n}.
\end{aligned}
 \tag{L-32405.17}
\]

## 6. Strict asymptotic reserve

Equations (L-32405.9) and (L-32405.17) imply

\[
 \frac{S_4(n,j)}{P_4(n,j)^2}
 <\frac{240\log n}{n(\log2)^2}.
 \tag{L-32405.18}
\]

The function `log n/n` decreases for `n>e`. The exact rational log enclosures used by `X-32402` include

\[
 \log2>\frac{69}{100},
 \qquad
 \log4735<\frac{847}{100}.
 \tag{L-32405.19}
\]

Thus, for every `n>=4735`,

\[
 \frac{S_4(n,j)}{P_4(n,j)^2}
 <
 \frac{240(847/100)}{4735(69/100)^2}
 =\frac{1355200}{1502889}
 <\frac{19}{20}.
 \tag{L-32405.20}
\]

This proves (L-32405.7), and in particular strict positivity, throughout the infinite tail.

## 7. Exact finite range

It remains to prove the finite table

\[
 4\le n\le4734,
 \qquad
 \lceil n/4\rceil\le j\le\lfloor n/2\rfloor,
\]

the other half following by symmetry.

`experiments/X-32402-q4-selberg-reserve/verify.py` uses only the Python standard library and `fractions.Fraction`.

Every logarithm is enclosed by the exact identity

\[
 \log y
 =2\sum_{r=0}^{M-1}\frac{x^{2r+1}}{2r+1}+R_M,
 \qquad
 x=\frac{y-1}{y+1},
\]

with

\[
 0<R_M
 <\frac{2x^{2M+1}}{(2M+1)(1-x^2)},
 \qquad 1\le y<2.
\]

The verifier uses `M=55` and fixed-point denominator `10^24`, constructs rigorous intervals for `Lambda_4`, `C_4`, and their divisor-prefix carry sums, and checks

\[
 P_{4,\mathrm{lo}}(n,j)^2
 >S_{4,\mathrm{hi}}(n,j)
\]

for every row.

Replay result:

```text
classification
PASS_EXACT_Q4_BALANCED_SELBERG_KUMMER_RESERVE

balanced rows
2,803,709

finite endpoint
4734

minimum certified row
(n,j)=(8,4)

minimum reserve lower bound
1.982153862092292642942383343265608318216102562329...
```

The result payload digest is

```text
570d1302e47ad299f0854b407c1aa8cf477aca76ad3629e0e8838d9a3073feeb
```

This completes the finite range and proves (L-32405.6).

## 8. Why this matters

The failed `lambda=2` pole-killing source of `R-32402` already develops a negative row at `(6,2)`. The Euler–Blaschke `Q=4` source avoids that defect while preserving all of the desired analytic properties:

```text
main zeta pole at s=1              removed;
critical line                      exact all-pass;
Re(s)>1/2                           strict attenuation;
Dirichlet inverse                  positive;
generalized primes                 nonnegative;
nontrivial zeta-zero poles         all retained;
balanced Selberg--Kummer reserve    strict for every n>=4.
```

The remaining difficulty is no longer construction of a source-matched balanced reserve. It is the source-convolved reflected block / neutral principal return which turns that reserve into a global energy recurrence.

## 9. Proof boundary

Closed here:

1. nonnegative complete forcing;
2. an elementary uniform mass estimate for `Lambda_4`;
3. strict quantitative reserve for every `n>=4735`;
4. rigorous finite interval verification of every remaining balanced row;
5. the complete all-`n` balanced theorem.

Open:

1. a physical-field-to-reserve congruence for the `Q=4` source;
2. the neutral lower-scale recurrence after the reflected identity;
3. an unconditional subexponential pole-field energy bound;
4. RH.
