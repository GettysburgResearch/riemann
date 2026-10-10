# Actual sextic-family moments M_2, M_4, M_6 at H = D^(1+θ)

```text
Status: EMPIRICAL (FLOATING_RECONNAISSANCE)
Scope: finite. nu = 1, S = {(2),(lambda)}, one fixed bump W on (1,2).
  D in {500, 707, 1000, ..., 64000} (half-octaves, 15 values);
  H = D^(1+theta), theta in {0.05, 0.1, 0.25} for all D, theta = 0.5 for D <= 32000,
  H = D^2 for D <= 5657.  Largest row sets: 1.16e8 rows (D = 5657, H = D^2) and
  2.08e7 rows (D = 32000, H = D^1.5).
  Balanced-divisor test (PR 910, eq. 3.5): D in {500, 1000, 2000, 4000, 8000},
  X in {D, D/2, D/4, D/16}, c in {1, p_7, p_7 p_13}, theta in {0.05, 0.1, 0.25}.
Exact sources or dependencies: OpenAI Oct 5 11/12 manuscript (PR 908 import), PR 910 sections 7-8
  (UPSTREAM_HEIGHT_AND_MOMENTS.md, Prop. 7.2 and section 8; FOURTH_MOMENT_REDUCTION.md, eqs. 3.1-3.5;
  local ref pr910), w5copg numerics (origin/claude/openai-math-riemann-analysis-w5copg,
  standalone/2026-10-07-openai-quasi-rh/numerics/eisenstein.py, copied here unchanged,
  sha256 bc6af658...e584ae9).
What was actually run (4-core machine shared with other jobs, load 5-9; 2 threads per run):
  python3 -I validate.py 400 30 ; python3 -I validate.py 5000 10                     (~1 s each)
  sh results/run_main.sh:
    moments.py ... --D 500 .. 5657 --d2-max 5657                                      320 s
    moments.py ... --D 8000 .. 64000 --theta-cap 32000:0.25                           827 s
    diag.py ... --D 500 .. 64000 --exact2-max 22627 --exact3-max 2000 --samples 1e6   316 s
  sh results/run_balanced.sh  (balanced.py, D = 500 .. 8000)                         ~5 min
  python3 -I exact_diag1.py <moments for D=500,1000> 2.5e5                             8 s
  python3 -I make_tables.py results > results/tables.md
Smallest remaining gap: every statement here is a finite floating-point observation.
  The moment bounds sum_u |A_u(D)|^{2k} << D^{k+eps} H at H = D^{1+theta} (PR 910 (7.1),
  k = 2, 3) and the balanced mean square (3.5) are theorem-level statements about all D;
  nothing below proves them or extrapolates them.  Values are not directed or certified.
```

RH is unsolved. This folder does not prove any zero-free region. It checks one thing: do the
*actual* sextic rows A_u(D) have moments of diagonal size in the regime H = D^(1+θ) that PR 910 needs?
PR 910 tested only ±1 surrogate phases.

## Verdict (finite range only)

| k | rung (PR 910 Prop. 7.2) | M_{2k} / diagonal, all D and θ tested | trend of the ratio in D (fitted exponent) | verdict |
|---|---|---|---|---|
| 1 | 11/12 (imported) | 0.965 – 1.007 | ≤ 0.005 in absolute value | diagonal-sized |
| 2 | 17/24 | 0.92 – 1.02 (D ≥ 1414: 0.973 – 1.019) | +0.001 … +0.009 (s.e. ≈ 0.01) | **diagonal-sized** |
| 3 | 23/36 | 0.87 – 1.24 (D ≥ 1414: 0.95 – 1.08) | −0.002 … +0.016 (s.e. ≈ 0.02) | **diagonal-sized** |

* For each k, M_{2k}(D,H) agrees with the exact diagonal L0(H)·E_k(D) to within sampling noise.
  * This holds at θ = 0.05 and θ = 0.1, and also at θ = 0.25, θ = 0.5 and H = D².
  * At D = 64000 and θ = 0.05 the ratios are 0.999 (k=1), 0.998 (k=2) and 0.998 (k=3).
* The ratio does not depend on θ in any systematic way. There is also no excess at small θ, where the
  number of rows H is far below the number of product columns D^k.
* The only growth is in the diagonal itself:
  * E_2/(2E_1²) rises from 1.02 to 1.07 over the range.
  * E_3/(6E_1³) rises from 1.06 to 1.22.

  This is the slow (log D)-power growth expected of a random multiplicative model. It is D^{o(1)} and is
  allowed by the D^ε in (7.1). The raw fitted exponents of M_{2k} exceed k + h by at most +0.04 (k = 3,
  D ≥ 4000). All of that excess comes from this diagonal growth.
* No row class grows beyond diagonal size, but at small D the structured rows cause the visible
  deviations.
  * The structured classes are sixth-power rows, cube rows (quadratic twists), square rows (cubic twists)
    and rational rows.
  * They hold O(H^{1/2}) rows. A few of them have large |A_u|.
  * At small D and θ they carry a large share of M_6. At D = 500, θ = 0.05, cube rows give 33 % of M_6;
    this explains that cell's ratio of 1.24. At D = 1414 and 2828, sixth-power rows give 7–9 %.
  * The share decays with D. Sixth+cube+square rows together give at most 2 % of M_6 for D ≥ 4000, and
    0.3 % at D = 64000 (θ ≤ 0.1). See §3.
  * Per row, the real-valued classes match the real-Gaussian factors 3/2 (k=2) and 5/2 (k=3).
* PR 910's (3.5) holds numerically on the actual sextic symbols, uniformly in X ∈ [D/16, D] and in the
  three tested c.
  * The mean square of B_{c,u}(X) over 0 < N u ≤ D^{1+θ} equals its exact diagonal within 0.936 – 1.031.
  * It equals 0.040 – 0.047·H X² at X = D.

What this does **not** show:
* Numerics cannot separate D^ε from a constant.
* They cannot rule out an off-diagonal term that only appears beyond D = 6.4·10⁴.
* They cannot rule out a term that only appears for some other W or ν.
* The diagonal-sized behaviour is the expected behaviour under GRH-type heuristics (see §5). Seeing it is
  a consistency check, not evidence toward a proof of (7.1).

## 1. Conventions

* O = Z[ω]. The family is
  A_u(D) = Σ_n μ(n) χ_n(u) W(N n/D), where:
  * n runs over squarefree ideals prime to 6, each with its primary generator;
  * χ_n(u) = ∏_{p|n} (u/p)_6, extended by 0 when (u,n) ≠ 1;
  * ν = 1, and W(y) = exp(4 − 1/((y−1)(2−y))) on (1,2).

  These are exactly the w5copg conventions, which were checked there against the paper's lemma identities.
* **Rows:** u runs over all nonzero elements of O with 0 < N u ≤ H, units and non-primary u included. This
  follows the manuscript's "0 < Nu ≤ H" and PR 910 (7.1).
  * The six associates of an ideal give different rows, because χ_n(εu) = χ_n(ε)χ_n(u).
  * L0(H) = #{u : 0 < N u ≤ H} ≈ 3.628 H.
  * The identity A_{ū} = conj(A_u) was verified to 1e-13. Only rows with b ≥ 0 are evaluated; rows with
    b > 0 are counted twice.
* **Diagonal.** For k ≤ 5 the principal condition ∏ n_i/∏ m_j = sixth power forces ∏ n_i = ∏ m_j as
  ideals, because the exponents lie in [−k, k]. At a fixed product all Möbius signs agree. The diagonal is
  therefore

  diag_{2k}(D,H) = Σ_r c_k(r)² #{u : (u,r)=1} ≈ L0(H)·E_k(D),

  where:
  * E_k = Σ_r c_k(r)² ∏_{p|r}(1−1/Np);
  * c_k(r) = Σ_{n_1⋯n_k = r} ∏ W(N n_i/D).

  The density form was checked against exact inclusion–exclusion lattice counts for k = 1 at D = 500 and
  1000: they agree to 1e-3 (`results/exact_diag1_D500_1000.json`).

  E_k is also exactly the 2k-th moment of the random model in which X_p = 0 with probability 1/Np and is
  otherwise uniform on μ_6.
  * E_1 is computed exactly.
  * E_2 is computed exactly by grouping ordered pairs by their product ideal, for D ≤ 22627.
  * E_3 is computed exactly by grouping triples, for D ≤ 2000.
  * All E_k are also computed by 10⁶-sample Monte Carlo. Exact and Monte Carlo values agree within
    1.5σ wherever both exist (32 comparisons; the largest is 1.50σ).
  * Monte Carlo standard errors: 0.25 % for E_2, 0.5 – 0.6 % for E_3.
  * The "k!" Gaussian normalisation is reported separately below.

## 2. Main tables

The full tables are in `results/tables.md`. That file includes M_2, the 8th-moment diagonal and the
complete class tables.

**Ratio M_4 / diag_4**, with diag_4 = L0(H)·E_2(D). E_2 is exact for D ≤ 22627 and Monte Carlo
(s.e. 0.3 %) above:

| D | θ=0.05 | θ=0.1 | θ=0.25 | θ=0.5 | H=D² |
|---|---|---|---|---|---|
| 500 | 1.0035 | 0.9877 | 0.9928 | 1.0227 | 0.9978 |
| 1000 | 0.9342 | 0.9582 | 0.9828 | 1.0000 | 0.9989 |
| 2000 | 0.9799 | 0.9831 | 0.9908 | 1.0020 | 0.9998 |
| 4000 | 0.9730 | 1.0009 | 1.0010 | 0.9953 | 1.0003 |
| 5657 | 0.9926 | 0.9891 | 0.9967 | 1.0017 | 0.9998 |
| 8000 | 0.9899 | 0.9897 | 0.9960 | 0.9973 | |
| 16000 | 1.0025 | 1.0077 | 0.9959 | 0.9987 | |
| 22627 | 1.0021 | 1.0077 | 1.0029 | 0.9986 | |
| 32000 | 0.9937 | 0.9927 | 0.9966 | 0.9958 | |
| 45255 | 1.0081 | 1.0047 | 0.9993 | | |
| 64000 | 0.9978 | 1.0002 | 0.9994 | | |

**Ratio M_6 / diag_6**, with diag_6 = L0(H)·E_3(D). E_3 is exact for D ≤ 2000 and Monte Carlo
(s.e. 0.5–0.6 %) above:

| D | θ=0.05 | θ=0.1 | θ=0.25 | θ=0.5 | H=D² |
|---|---|---|---|---|---|
| 500 | 1.2440 | 1.1552 | 1.0801 | 1.0461 | 0.9975 |
| 1000 | 0.8818 | 0.8952 | 0.9511 | 0.9940 | 0.9971 |
| 2000 | 0.9790 | 0.9650 | 0.9708 | 1.0043 | 0.9996 |
| 4000 | 0.9552 | 1.0019 | 1.0044 | 0.9905 | 1.0011 |
| 5657 | 0.9528 | 0.9514 | 0.9893 | 1.0002 | 0.9942 |
| 8000 | 0.9838 | 0.9696 | 0.9826 | 0.9900 | |
| 16000 | 0.9945 | 1.0036 | 0.9915 | 0.9967 | |
| 22627 | 0.9945 | 0.9998 | 0.9916 | 0.9900 | |
| 32000 | 0.9791 | 0.9877 | 0.9916 | 0.9884 | |
| 45255 | 1.0192 | 1.0188 | 1.0040 | | |
| 64000 | 0.9984 | 1.0062 | 1.0001 | | |

The scatter at small θ is sampling noise in the rows. At D = 500 and θ = 0.05 there are only 2478 rows.
The scatter is larger for k = 3 because |A|⁶ is heavier-tailed. It shrinks as L0(H) grows, and at H = D²
every ratio is 1.000 ± 0.006.

**Diagonal constants.** These show the log-type growth of the diagonal itself. ex = exact, mc = Monte Carlo.

| D | E_1/D | E_2/(2E_1²) | E_3/(6E_1³) | E_4/(24E_1⁴) (mc) | \|A_1\|/√E_1 |
|---|---|---|---|---|---|
| 500 | 0.0819 | 1.021 (ex) | 1.063 (ex) | 1.14 | 0.79 |
| 2000 | 0.0775 | 1.043 (ex) | 1.134 (ex) | 1.28 | 0.58 |
| 8000 | 0.0759 | 1.046 (ex) | 1.148 (mc) | 1.32 | 0.89 |
| 22627 | 0.0766 | 1.057 (ex) | 1.192 (mc) | 1.43 | 1.06 |
| 64000 | 0.0767 | 1.066 (mc) | 1.217 (mc) | 1.49 | 1.20 |

**Gaussian normalisation.** M_4/(L0·2E_1²) rises from 1.00 to 1.065. M_6/(L0·6E_1³) rises from 1.05 to
1.22. Both track the diagonal constants above. To convert to the paper's normalisation, use
M_{2k}/(D^k H) = ratio · (E_k/D^k) · (L0/H), with E_1/D ≈ 0.077 and L0/H ≈ 3.628.

**Fitted exponents.** These are least-squares slopes in log D at fixed θ. Here α_k is the slope of
log M_{2k} and β_k is the slope of log(M_{2k}/diag_{2k}).

| H | D range | α_1−(1+h) | β_1 | α_2−(2+h) | β_2 | α_3−(3+h) | β_3 |
|---|---|---|---|---|---|---|---|
| D^1.05 | 500–64000 | −0.001 | +0.005 | +0.005 | +0.009 | +0.010 | +0.000 |
| D^1.05 | 4000–64000 | +0.001 | +0.002 | +0.013 | +0.007 | +0.038 | +0.016 |
| D^1.1 | 4000–64000 | −0.001 | −0.000 | +0.009 | +0.003 | +0.032 | +0.011 |
| D^1.25 | 4000–64000 | −0.000 | +0.000 | +0.007 | +0.001 | +0.023 | +0.002 |
| D^1.5 | 4000–32000 | −0.002 | +0.000 | +0.003 | −0.000 | +0.015 | −0.002 |
| D² | 500–5657 | −0.016 | +0.000 | −0.019 | +0.001 | −0.010 | −0.000 |

A ±3 % scatter over a ln-range of 2.8 corresponds to about ±0.01 in β. The positive α excess for k = 3
equals the growth of E_3/(6E_1³). β is the honest off-diagonal indicator, and it is zero within noise.

## 3. Row-type decomposition

The row classes are disjoint:
* **sixth**: u = ε v⁶. Here χ_n(u) = χ_n(ε)·1_{(n,v)=1}, so A_u is a copy of A_ε. A_1 is one of these.
* **cube**: u = ε v³, excluding sixth powers. Here χ_n(u) = χ_n(ε)(v/n)_2, a quadratic twist.
* **square**: u = ε v², excluding sixth powers. These are cubic twists.
* **generic**: all remaining rows.

"Rational" rows (b = 0, u ∈ Z) are reported as an overlapping diagnostic. For them A_u is real, because
ū = u.

In the table, share is the class contribution divided by M_{2k}. Per-row is the class mean of |A_u|^{2k}
divided by the generic-row mean.

| D, H | class | #u | share k=2 | share k=3 | per-row k=2 | per-row k=3 | max \|A_u\|²/E_1 |
|---|---|---|---|---|---|---|---|
| 64000, D^1.1 | sixth | 30 | 9.1e-5 | 6.4e-5 | 2.13 | 1.49 | 3.1 |
| | cube | 180 | 3.9e-4 | 7.2e-4 | 1.52 | 2.81 | 11.1 |
| | square | 1566 | 2.1e-3 | 2.0e-3 | 0.93 | 0.88 | 7.6 |
| | generic | 700302 | 0.997 | 0.997 | 1 | 1 | 23.3 |
| | rational | 878 | 2.0e-3 | 4.0e-3 | 1.59 | 3.21 | 17.0 |
| 32000, D^1.5 | sixth | 54 | 8.1e-6 | 8.0e-6 | 3.11 | 3.09 | 4.0 |
| | cube | 594 | 4.0e-5 | 6.5e-5 | 1.39 | 2.27 | 13.3 |
| | square | 8634 | 4.1e-4 | 4.0e-4 | 0.99 | 0.97 | 9.0 |
| | rational | 4784 | 3.8e-4 | 6.6e-4 | 1.63 | 2.86 | 18.4 |
| 5657, D² | sixth | 60 | 6.4e-7 | 4.1e-7 | 1.24 | 0.79 | 2.6 |
| | cube | 1098 | 1.4e-5 | 2.3e-5 | 1.52 | 2.42 | 11.5 |
| | square | 20448 | 1.7e-4 | 1.8e-4 | 0.99 | 1.00 | 15.8 |
| | rational | 11314 | 1.4e-4 | 2.3e-4 | 1.45 | 2.41 | 17.7 |

What the classes show:
* **Real-valued rows behave like real Gaussians.** A real Gaussian has E X⁴/E|Z|⁴ = 3/2 and
  E X⁶/E|Z|⁶ = 15/6 = 5/2 against a complex Gaussian. The rational rows give 1.45–1.69 and 2.0–3.3.
* **Cube rows sit between the real and complex behaviour.** For the third of them with ε = ±1 the twist
  (v/n)_2 is real.
* **Sixth-power rows are copies of A_ε.** Their values are close to the six Möbius sums
  A_ε(D) = Σ μ(n)χ_n(ε)W twisted by unit characters, and |A_ε|²/E_1 ≤ 4.4.

These are mostly O(1) per-row factors. The class sizes are about L0(H^{1/6}), 3.6 H^{1/3}, 3.6 H^{1/2}
and 2√H rows respectively. **No class has a contribution growing beyond diagonal size.**

At small D, though, these few rows control the M_6 fluctuations. Combined share of sixth+cube+square rows
in M_6 at θ = 0.05:

| D | 500 | 707 | 1000 | 1414 | 2000 | 2828 | 4000 | 8000 | 16000 | 32000 | 45255 | 64000 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| share | 0.344 | 0.058 | 0.037 | 0.114 | 0.029 | 0.111 | 0.022 | 0.009 | 0.012 | 0.008 | 0.020 | 0.003 |
| M_6/diag | 1.244 | 0.867 | 0.882 | 0.974 | 0.979 | 1.076 | 0.955 | 0.984 | 0.994 | 0.979 | 1.019 | 0.998 |

* At D = 500, θ = 0.05, cube rows give 33 % of M_6.
* At D = 1414 and D = 2828, sixth-power rows give 9 % and 7 %. Here |A_ε(D)| happens to be large:
  |A_ε|²/E_1 is about 4–6, so |A_ε|⁶ is tens of times the generic mean.
* In M_4 the largest special share is 9 % (cube rows, D = 500).

For a class of size ≍ H^{1/m} with |A_u|²/E_1 ≈ τ, the expected share is about H^{1/m−1}·τ^k/k!. This
decays in H at every fixed k, and the data follow it. The generic-row maximum of |A_u|²/E_1 is 6–26. It
grows roughly like ln L0(H), as for an exponential tail.

**Structured rows as potential obstructions (exponent bookkeeping, not numerics).** Write h = 1+θ, and
take a class of ≍ H^{1/m} rows whose |A_u| is of size D^β.
* That class stays within D^k H iff β ≤ 1/2 + (1 − 1/m)h/(2k).
* For the sixth-power rows (m = 6) this threshold is 1/2 + 5h/(12k). That is exactly PR 910's extracted
  exponent: 17/24 at k = 2 and 23/36 at k = 3 as θ → 0.
* Bounding the principal-row sub-sum of (7.1) is therefore *equivalent* to the conclusion drawn from it. The
  extraction is exponent-lossless. A proof of (7.1) must contain the cancellation in A_1 and cannot bound
  those rows trivially. PR 910 already notes that these rows cannot be dropped.
* Cube rows (m = 3) need quadratic-twist Möbius sums ≪ D^{1/2+h/(3k)} on average.
* Square rows (m = 2) need cubic-twist sums ≪ D^{1/2+h/(4k)} on average.
* Any *single* row above D^{1/2+h/(2k)} breaks the bound. That is 0.7625 at k = 2 and 0.675 at k = 3 for
  h = 1.05.
* By sextic reciprocity, standard but not re-derived here, n ↦ (u/n)_6 is a finite-order Hecke character of
  conductor ≪ N u. So (7.1) at fixed k also implies Möbius-sum cancellation for every row character of
  conductor ≤ D^h. Conversely, GRH for these characters implies (7.1) for every k.

In the data every class sits at β ≈ 1/2: |A_1|/√E_1 = 0.1–1.5 for all D. So no structured obstruction is
visible. The remaining question for (7.1) is entirely unconditional proof, not a structural counterexample
in this range.

## 4. Balanced-divisor mean square (PR 910 FOURTH_MOMENT_REDUCTION.md, eq. 3.5)

The quantity is

B_{c,u}(X) = Σ_{(a,b)=1, (ab,cS)=1} μ(a)μ(b)χ_{ab}(u)W(Na/X)W(Nb/X) = Σ_r μ(r)χ_r(u)𝒲_X(r).

* The columns are r = ab, built from all coprime pairs, with 𝒲_X(r) = Σ_{d|r} W(Nd/X)W(Nr/(XNd)) exactly
  as in (3.3).
* The construction was checked against a direct double sum with exact symbols at X = 60, for c = 1 and
  c = p_7: the error is 1e-14.
* "diag" is L0(H)·Σ_r 𝒲_X(r)² ∏_{p|r}(1−1/Np).

| D | X | N c | #columns | θ | Σ_u\|B\|²/(H X²) | Σ_u\|B\|²/diag |
|---|---|---|---|---|---|---|
| 1000 | 1000 | 1 | 37624 | 0.05 / 0.1 / 0.25 | 0.040 / 0.041 / 0.042 | 0.946 / 0.964 / 0.984 |
| 2000 | 2000 | 1 | 143918 | 0.05 / 0.1 / 0.25 | 0.042 / 0.042 / 0.043 | 0.974 / 0.982 / 0.991 |
| 2000 | 1000 | 1 | 37624 | 0.05 / 0.1 / 0.25 | 0.043 / 0.042 / 0.042 | 0.999 / 0.987 / 0.985 |
| 2000 | 286 | 7 | 2357 | 0.05 / 0.1 / 0.25 | 0.037 / 0.036 / 0.036 | 1.025 / 0.999 / 0.997 |
| 2000 | 22 | 91 | 21 | 0.05 / 0.1 / 0.25 | 0.043 / 0.044 / 0.044 | 0.981 / 0.994 / 0.998 |
| 4000 | 4000 | 1 | 583079 | 0.05 / 0.1 | 0.042 / 0.043 | 0.978 / 1.002 |
| 8000 | 8000 | 1 | 2305320 | 0.05 / 0.1 | 0.041 / 0.041 | 0.994 / 0.993 |

All cases, including D = 500 and the smaller X at D = 4000 and 8000, are in `results/tables.md` and
`results/balanced.json`.
* Every ratio to the diagonal lies in 0.936–1.031.
* The normalised mean square at X = D lies in 0.040–0.047, with a slow log-type drift inherited from
  Σ𝒲_X(r)² ≍ X² log X. Across all X the range is 0.0017–0.056. The small value is X = 11, where the
  W-support holds only 3 ideals.
* There is no sign of a moving-exclusion (c-dependent) excess.
* E|B|⁴/(E|B|²)² ≈ 4–11 for X ≥ 60, close to the value 6 that B ≈ A² would give for Gaussian A.

So (3.5) is consistent with the data, uniformly in X ≤ D at the full H = D^{1+θ}. It is still the unproved
input.

## 5. Interpretation and caveats

* The agreement with the diagonal at H = D^{1.05} is in a regime where the large sieve gives nothing:
  * For k = 2 there are about D² columns and only about D^{1.05} rows.
  * Classical duality bounds give only (H + D^k)·‖c‖², which is D^{k−1−θ} times too large.

  The data say the actual coefficients c_k(r) behave like a random multiplicative model on these short row
  ranges. This is the expected behaviour, and seeing it confirms no theorem.
* Only ν = 1 and one W were tested. PR 910 needs the bound for every smooth annular test in the Mellin
  argument.
* D ≤ 6.4·10⁴, so the largest products in M_6 have norm about 2·10¹⁵. All values are binary64; none is
  certified.
* Nothing here strengthens any reviewed statement. The PR 910 rungs 17/24 and 23/36 remain *conditional*
  on unproved moment bounds.

## Files

| file | role |
|---|---|
| `eisenstein.py` | w5copg arithmetic in Z[ω] and sextic-symbol tables (copied unchanged) |
| `sextic_kernel.c` | C inner loop: prefix-tree evaluation of Σ_n w_n χ_n(u) on lattice segments, and the random-model sampler. Compiled to `build/sextic_kernel.so` on first use; that file is generated and should not be committed |
| `common.py` | prime tables, prefix tree, lattice segments, threaded evaluation, family set-up |
| `validate.py` | checks the kernel against exact-symbol direct sums (error ≤ 2e-13), the symmetries A_ū = conj(A_u), A_{−27u} = A_{64u} = A_u, and timing |
| `moments.py` | streaming M_2 … M_8 by H and by row class |
| `diag.py` | E_k(D): exact for k = 1, 2 (D ≤ 22627) and 3 (D ≤ 2000); Monte Carlo for all |
| `exact_diag1.py` | exact inclusion–exclusion check of the density form of the diagonal (k = 1) |
| `balanced.py` | PR 910 (3.5) test |
| `make_tables.py` | builds `results/tables.md` |
| `results/` | `moments.json`, `diag.json`, `balanced.json`, `exact_diag1_D500_1000.json`, logs, run scripts |
