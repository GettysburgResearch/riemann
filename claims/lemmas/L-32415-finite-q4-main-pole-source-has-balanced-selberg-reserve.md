# L-32415 — The finite Q=4 main-pole source has a complete balanced Selberg reserve

Claim ID: `L-32415`  
Title: The two-tap radix-four source which removes the zeta pole has positive inverse/generalized-prime coefficients and a strict Selberg–Kummer reserve on every quarter-balanced row  
Status: **PROPOSED COMPLETE THEOREM — ANALYTIC TAIL + EXACT FINITE REPLAY; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: elementary Euler products; the Chebyshev estimate used in `L-32405`; finite carry algebra  
Scope: exact source and all-row reserve theorem; no global reflected recurrence or RH conclusion

## 1. A denominator-free radix-four source

Put

\[
 F_4(s)=1-4^{1-s},
 \qquad
 B_\sharp(s)=\frac{F_4(s)}{\zeta(s)},
 \qquad
 A_\sharp(s)=B_\sharp(s)^{-1}
 =\frac{\zeta(s)}{1-4^{1-s}}.
\tag{L-32415.1}
\]

In coefficient notation

\[
\boxed{
 b_\sharp=(\varepsilon-4\delta_4)*\mu .
}
\tag{L-32415.2}
\]

The local inverse factor is

\[
 \frac1{1-4\,4^{-s}}
 =\sum_{r\ge0}4^r\,4^{-rs}.
\]

Hence

\[
\boxed{
 a_\sharp(n)
 =\sum_{0\le r\le v_4(n)}4^r
 =\frac{4^{v_4(n)+1}-1}{3}>0,
}
\tag{L-32415.3}
\]

where `v_4(n)=max{r:4^r|n}`.

Its generalized von Mangoldt sequence is

\[
\boxed{
 \Lambda_\sharp(n)
 =\Lambda(n)
  +(\log4)\sum_{r\ge1}4^r\mathbf1_{n=4^r}
 \ge0.
}
\tag{L-32415.4}
\]

Let

\[
 C_\sharp
 =\Lambda_\sharp\log+\Lambda_\sharp*\Lambda_\sharp.
\tag{L-32415.5}
\]

## 2. Pole ledger and the finite physical source

The atomized carry window contributes one factor `zeta(s)`. Thus the bare physical source is exactly

\[
\boxed{
 \zeta(s)B_\sharp(s)=1-4^{1-s},
}
\tag{L-32415.6}
\]

a two-tap radix-four filter.

If

\[
 L_\sharp=-A_\sharp'/A_\sharp,
\]

the RH-sensitive physical current is

\[
\boxed{
 F_4(s)L_\sharp(s)N_\theta(s).
}
\tag{L-32415.7}
\]

At `s=1`, `F_4(s)=(s-1)log4+O((s-1)^2)` and

\[
 -\zeta'/\zeta=\frac1{s-1}+O(1),
 \qquad
 F_4'/F_4=\frac1{s-1}+O(1).
\]

Therefore

\[
\boxed{
 F_4(s)L_\sharp(s)=2\log4+O(s-1),
}
\tag{L-32415.8}
\]

so the deterministic zeta pole is removed.

Every zero of `F_4` lies on `Re(s)=1`; every nontrivial zeta zero lies in `0<Re(s)<1`. Hence for a zeta zero `rho` of multiplicity `m_rho`,

\[
\boxed{
 \operatorname*{Res}_{s=\rho}
 [F_4(s)L_\sharp(s)]
 =-m_\rho F_4(\rho)\ne0.
}
\tag{L-32415.9}
\]

Thus the source is pole-preserving at every nontrivial zero while having only a finite bare physical source.

## 3. Balanced Kummer coordinates

For a split `n=j+k`, define

\[
 P_\sharp(n,j)
 =\sum_{q\le n}\Lambda_\sharp(q)\chi_{n,q}(j),
\]

\[
 S_\sharp(n,j)
 =\sum_{q\le n}C_\sharp(q)\chi_{n,q}(j),
\]

and

\[
\boxed{
 \mathcal R_\sharp(n,j)
 =P_\sharp(n,j)^2-S_\sharp(n,j).
}
\tag{L-32415.10}
\]

The theorem is

\[
\boxed{
 0\le S_\sharp(n,j)<P_\sharp(n,j)^2
}
\tag{L-32415.11}
\]

for every integer

\[
 n\ge4,
 \qquad n/4\le j\le3n/4.
\]

Moreover, for every `n>=4735` in the same cone,

\[
\boxed{
 \mathcal R_\sharp(n,j)
 >\frac1{20}P_\sharp(n,j)^2.
}
\tag{L-32415.12}
\]

## 4. Cofinal proof

Because `Lambda_sharp>=Lambda`, ordinary Kummer gives

\[
 P_\sharp(n,j)
 \ge\log\binom nj
 \ge\frac n4\log2
\tag{L-32415.13}
\]

on the quarter-balanced cone, exactly as in `L-32405`.

Let

\[
 \Psi_\sharp(x)=\sum_{q\le x}\Lambda_\sharp(q).
\]

The local correction obeys

\[
 (\log4)\sum_{4^r\le x}4^r
 \le\frac43x\log4
 =\frac83x\log2.
\]

Combining this with the elementary Chebyshev bound

\[
 \psi(x)\le2x\log2
\]

gives

\[
 \Psi_\sharp(x)<\frac{14}{3}x\log2<\frac{10}{3}x.
\tag{L-32415.14}
\]

Since every coefficient of `C_sharp` is nonnegative, the same partial-summation argument as `L-32405.12--17` yields

\[
\boxed{
 S_\sharp(n,j)<15n\log n.
}
\tag{L-32415.15}
\]

For `n>=4735`, therefore,

\[
 \frac{S_\sharp}{P_\sharp^2}
 <\frac{240\log n}{n(\log2)^2}
 \le\frac{1355200}{1502889}
 <\frac{19}{20},
\tag{L-32415.16}
\]

using the same exact rational bounds

\[
 \log2>69/100,
 \qquad
 \log4735<847/100.
\]

This proves the complete infinite tail and (L-32415.12).

## 5. Exact finite replay

`experiments/X-32415-finite-q4-main-pole-reserve/verify.py` uses only the Python standard library, integer arithmetic, and `fractions.Fraction`.

The sole change from the reviewed Q=4 replay is the local generalized-prime coefficient:

```text
old Euler–Blaschke source at 4^r:
    (4^r-1) log 4;

finite main-pole source at 4^r:
    4^r log 4.
```

Every logarithm is enclosed by a directed atanh series with 55 terms and denominator scale `10^24`. The checker certifies

```text
classification
PASS_EXACT_FINITE_Q4_MAIN_POLE_BALANCED_RESERVE

balanced rows
2,803,709

finite endpoint
4734

minimum row
(8,4)

minimum reserve lower bound
0.0603418064194869442739233553...
```

The decimal is orientation only. The proof uses the exact scaled integer margin in the JSON result.

Retained result digest:

```text
5eba6316ddf6df719c0f85c3d7bd4ee6e1174eab3904e83b3fc626b2d417ae76
```

This completes the finite range and hence (L-32415.11).

## 6. Exact filtered Chebyshev prefix

The physical current coefficient is

\[
 c_\sharp=(\varepsilon-4\delta_4)*\Lambda_\sharp.
\]

Writing

\[
 G_\sharp(x)=\sum_{n\le x}c_\sharp(n),
\]

one obtains, for `x>=4`,

\[
\boxed{
 G_\sharp(x)
 =\psi(x)-4\psi(x/4)+4\log4.
}
\tag{L-32415.17}
\]

Indeed the local tower telescopes:

\[
 (\log4)\sum_{4^r\le x}4^r
 -4(\log4)\sum_{4^r\le x/4}4^r
 =4\log4.
\]

Thus the deterministic linear prime density is removed already at the prefix level.

By PNT,

\[
 G_\sharp(x)=o(x).
\tag{L-32415.18}
\]

Consequently its balanced additive physical defect is `o(n)` uniformly, while the reserve is `gg n^2` cofinally. Hence the current/reserve ratio tends to zero, just as for the denominator-bearing Q=4 source, but with no infinite bare-source collar.

This observation is not an RH estimate: `o(n)` is far weaker than the square-root scale.

## 7. Why this source is useful

The source has the simultaneous features

```text
bare physical source                 two taps only;
Dirichlet inverse                    positive;
generalized primes                  nonnegative;
main zeta pole                       removed;
artificial local poles               absent after physical multiplication;
nontrivial zeta-zero poles           all retained;
quarter-balanced Selberg reserve     strict for every n>=4.
```

The analogous radix-two pole-killing source fails the row reserve already at `(6,2)` (`R-32402`). The radix-four spacing removes that local collision.

This creates a second, simpler source-complete reflected route. It does not replace the Euler–Blaschke/all-pass source automatically: the finite source has no critical-line all-pass state, so its global scale recurrence must be derived independently.

## 8. Proof boundary

Closed here, subject to independent replay/review:

1. exact two-tap source and positive inverse;
2. nonnegative generalized-prime sequence;
3. main-pole removal and retention of every nontrivial zeta-zero pole;
4. strict all-row quarter-balanced Selberg–Kummer reserve;
5. exact finite directed replay;
6. explicit filtered-Chebyshev prefix and unconditional `o(x)` density cancellation.

Still open:

1. source-convolved independent-frequency reflected use of this reserve;
2. a subexponential physical-current bound or equivalent recurrence;
3. RH.
