# L-32417 — Simple radix-four plus/minus pair has a complete balanced Selberg reserve

Claim ID: `L-32417`  
Title: After exact two-channel orthogonalization, the finite radix-four plus/minus sources have nonnegative generalized-prime coordinates and a strict paired Selberg–Kummer reserve on every quarter-balanced row  
Status: **PROPOSED COMPLETE THEOREM — ANALYTIC TAIL + EXACT FINITE REPLAY; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32416`, `L-32415`; elementary Chebyshev estimate and finite carry algebra  
Scope: complete paired carry-row reserve; no global reflected recurrence or RH conclusion

## 1. Paired source

Retain the nonnegative orthogonal generalized-prime channels of `L-32416`,

\[
 \Lambda_0=\frac{\Lambda_-+\Lambda_+}{2},
 \qquad
 \Lambda_1=\frac{\Lambda_--\Lambda_+}{2},
\]

and the complete paired second moment

\[
\boxed{
 C_{\rm pair}
 =\Lambda_0\log
  +\Lambda_0*\Lambda_0
  +\Lambda_1*\Lambda_1\ge0.
}
\tag{L-32417.1}
\]

For `n=j+k`, define

\[
 P_r(n,j)=\sum_{q\le n}\Lambda_r(q)\chi_{n,q}(j),
 \qquad r=0,1,
\tag{L-32417.2}
\]

\[
 S_{\rm pair}(n,j)
 =\sum_{q\le n}C_{\rm pair}(q)\chi_{n,q}(j),
\tag{L-32417.3}
\]

and

\[
\boxed{
 \mathcal R_{\rm pair}(n,j)
 =P_0(n,j)^2+P_1(n,j)^2-S_{\rm pair}(n,j).
}
\tag{L-32417.4}
\]

Equivalently, with `P_\pm=P_0\pm P_1` and the individual Selberg forcings `S_\pm`,

\[
\boxed{
 \mathcal R_{\rm pair}
 ={1\over2}\left[
  P_-^2-S_-+P_+^2-S_+
 \right].
}
\tag{L-32417.5}
\]

The individual plus-channel reserve need not be positive. The theorem concerns the exact Hermitian pair before either channel is estimated separately.

## 2. The theorem

For every integer

\[
 n\ge4,
 \qquad
 {n\over4}\le j\le{3n\over4},
\]

one has

\[
\boxed{
 0\le S_{\rm pair}(n,j)
 <P_0(n,j)^2+P_1(n,j)^2.
}
\tag{L-32417.6}
\]

Moreover, for every `n>=4735` in the same cone,

\[
\boxed{
 \mathcal R_{\rm pair}(n,j)
 >\frac1{20}\left[P_0(n,j)^2+P_1(n,j)^2\right].
}
\tag{L-32417.7}

Thus the extremely simple two-tap source frame has a strict all-row paired reserve.

## 3. Cofinal lower bound for the paired energy

The channel `Lambda_0` contains the ordinary von Mangoldt sequence coefficientwise. Hence ordinary Kummer gives

\[
 P_0(n,j)
 \ge\log\binom nj
 \ge\frac n4\log2
\tag{L-32417.8}
\]

on the quarter-balanced cone. Since `P_1>=0`,

\[
\boxed{
 P_0^2+P_1^2
 \ge\frac{n^2(\log2)^2}{16}.
}
\tag{L-32417.9}
\]

## 4. Cofinal upper bound for the complete paired forcing

By construction

\[
 \Lambda_0+\Lambda_1=\Lambda_\sharp,
\]

where `Lambda_sharp` is the positive generalized-prime sequence of the finite main-pole source `L-32415`.

Coefficientwise,

\[
\begin{aligned}
 C_{\rm pair}
 &=\Lambda_0\log
  +\Lambda_0*\Lambda_0
  +\Lambda_1*\Lambda_1\\
 &\le
 (\Lambda_0+\Lambda_1)\log
 +(\Lambda_0+\Lambda_1)*(\Lambda_0+\Lambda_1)\\
 &=C_\sharp,
\end{aligned}
\tag{L-32417.10}
\]

because the omitted mixed convolutions are nonnegative.

`L-32415` proves the elementary complete mass bound

\[
 \sum_{q\le n}C_\sharp(q)<15n\log n.
\]

Since every carry indicator is zero or one,

\[
\boxed{
 S_{\rm pair}(n,j)<15n\log n.
}
\tag{L-32417.11}
\]

For `n>=4735`, combining (L-32417.9)--(L-32417.11) gives

\[
 \frac{S_{\rm pair}}{P_0^2+P_1^2}
 <\frac{240\log n}{n(\log2)^2}
 \le\frac{1355200}{1502889}
 <\frac{19}{20},
\tag{L-32417.12}
\]

using the exact rational logarithm bounds already retained by `L-32415`.

This proves (L-32417.7) and the complete infinite tail.

## 5. Exact finite replay

`experiments/X-32417-simple-radix4-paired-reserve/verify.py` uses only the Python standard library, integer arithmetic, and `fractions.Fraction`.

It constructs directed logarithm intervals for `Lambda_0`, `Lambda_1`, and `C_pair`, then checks

\[
 P_{0,\rm lo}^2+P_{1,\rm lo}^2>S_{{\rm pair},\rm hi}
\]

on every quarter-balanced row with `4<=n<=4734`. Mathematical nonnegativity of `P_0,P_1` is used to replace a tiny negative interval lower endpoint caused solely by outward rounding by zero before squaring.

The retained result is

```text
classification
PASS_EXACT_SIMPLE_Q4_PLUS_MINUS_PAIRED_RESERVE

balanced rows
2,803,709

finite endpoint
4734

minimum row
(6,2)

minimum reserve lower bound
2.013296516059285484657603611882504471051884008001...
```

The decimal is orientation only. The proof uses the exact scaled integer margin in the JSON payload.

Retained result digest:

```text
2dfe95c0dcfd9a6d2faf03c6e3cd570dfdccc65bf6b4c616d1c8887759dd6f96
```

This completes the finite range and proves (L-32417.6).

## 6. Why this is stronger structurally than a one-channel reserve

The plus source by itself has alternating local generalized-prime coefficients, while the minus source is the positive source of `L-32415`. Orthogonalization before taking a sign gives

```text
channel 0: ordinary primes + even four-adic levels;
channel 1: odd four-adic levels only;
```

with both channels nonnegative.

The same orthogonalization gives

\[
 {P_-^2+P_+^2\over2}=P_0^2+P_1^2
\]

and

\[
 {C_-+C_+\over2}=C_{\rm pair}.
\]

Therefore the reserve is source-complete for the exact plus/minus frame; no channel, convolution cross term, or two-adic level has been discarded.

Combined with `L-32416.6--9`, the pair also reconstructs the ordinary inverse-zeta current at zero delay and carries an explicit nonnegative current-detail square. This removes the finite synthesis/gauge layer from the remaining reflected problem.

## 7. Proof boundary

Closed here, subject to replay/review:

1. nonnegative orthogonal generalized-prime channels;
2. nonnegative complete paired forcing;
3. strict paired reserve on every quarter-balanced row;
4. uniform cofinal reserve fraction;
5. exact directed finite replay through the analytic threshold.

Still open:

1. source-convolved independent-frequency placement of the paired reserve;
2. use of the zero-delay current reconstruction to derive a global energy inequality;
3. RH.
