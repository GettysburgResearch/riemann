# Numerical test of the "Möbius generator" / Shimura-lift common-signal idea

```text
Status: EMPIRICAL (floating point; r_3(N) for N <= 10^7 exact by FFT, Hurwitz H(N) for N <= 10^6; fitted exponents carry +-0.03-0.05)
Scope: the Shimura-lift "Möbius generator" of note S0 tested on theta^3 and the Hurwitz series (non-cuspidal g; the conclusion that a smooth direct side vanishes because L(s, g x eta) is entire transfers to cuspidal g)
Exact sources: Shimura (1973)/Kohnen (1980) relation; Cohen-Eisenstein/Hurwitz coefficients; note S0 section 2
What was actually run: ../scripts/shimura/coeffs.py (writes r3.npy, H.npy; XMAX = 10^7 hard-coded), taskA.py, taskBC.py, taskBC2.py; logs not committed
Smallest remaining gap: no test with a cuspidal half-integral-weight g; only q <= 13, |D| <= 47
```

Scripts (in `../scripts/shimura/`): `coeffs.py` (coefficients), `taskA.py` (Shimura identity + Möbius detector),
`taskBC.py`, `taskBC2.py` (direct side, cutoffs, principal row). Logs: `taskA.log`, `taskBC_r3.log`,
`taskBC_H.log`, `taskBC2.log`. Data: r_3(N) for N ≤ 10^7 (FFT convolution of θ, max rounding error 6e-11),
Hurwitz H(N) for N ≤ 10^6 (direct enumeration of reduced forms (a,b,c), weights 1, 1/2, 1/3).

Cross-checks (all exact, max deviation 0): r_3(N)=12H(4N) (N≡1,2 mod 4), r_3(N)=24H(N) (N≡3 mod 8),
r_3(4N)=r_3(N), r_3(N)=0 (N≡7 mod 8), H(4N)=(3−χ_D(2))H(N) for odd N≡3 mod 4;
Σ_{N≤Z} r_3(N)/Z^{3/2} = 4.18879 = 4π/3, Σ_{N≤Z} H(N)/Z^{3/2} = 0.17428 (π/18 = 0.17453, Z=10^6).

Notation: d squarefree, D = disc(Q(√−d)) (= −d if d≡3 mod 4, else −4d), c_D(n) := Σ_{m|n} μ(m)χ_D(m)σ(n/m)
= Dirichlet coefficients of ζ(s)ζ(s−1)/L(s,χ_D) (Shimura with k=1, f = weight-2 Eisenstein, λ=σ_1).

## (A) Shimura relation and the Möbius part

**A.i Identity.** Verified exactly (max |difference| = 0, or 4.5e-13 for d=3 from float H):

* H-series: H(|D| n²)/H(|D|) = c_D(n) for all n ≤ √(10^6/|D|), d ∈ {1,2,3,5,7,11,15,23,31,39,47}.
* θ³: r_3(d n²)/r_3(d) = c_D(n_odd) (n_odd = odd part of n), for all n ≤ √(10^7/d). The naive c_D(n)
  is wrong by up to 10^4 for n even; for d ≡ 7 mod 8 the whole row vanishes (r_3(d)=0).
  Hence Σ_n r_3(dn²)/r_3(d) n^{-s} = ζ(s)ζ(s−1)(1−2^{1−s}) / [L(s,χ_D)(1−χ_D(2)2^{-s})].
* Analytic check (mpmath, Hurwitz-zeta L-values): e.g. d=3, s=4: S_d(577;4)[H]=1.3840166 vs
  ζ(4)ζ(3)/L(4,χ_{−3})=1.3840198 (tail bound 1.5e-6); r_3-row 1.13978085 vs 1.13978098 (tail 1.5e-7).
  s=3: agreement to the tail bound X^{2−s}/(s−2) ≈ 2e-3–5e-3 in all cases (d=3,5,7,11,23).

**A.ii Möbius part** M_d(X;s)=Σ_{n≤X} μ(n)χ_D(n)n^{-s}, X ≤ 10^7. Growth exponent of |M_d(X;s)| (s ≤ 1/2)
or of |M_d(X;s) − 1/L(s,χ_D)| (s > 1/2); three estimators: LS fit of log|·| on a 500-point geometric
grid 10^3–10^7 / LS fit of dyadic-window RMS / LS fit of running max (s≤1/2) or tail-sup (s>1/2).
Prediction if all zeros have Re ρ = β: exponent = β − s; GRH ⇒ 1/2 − s.

| d (D) | s=0 [pred +0.50] | s=0.25 [pred +0.25] | s=0.5 [pred +0.00] | s=0.6 [pred -0.10] | s=0.75 [pred -0.25] | s=1 [pred -0.50] |
|---|---|---|---|---|---|---|
| 3 (-3) | +0.50 / +0.49 / +0.50 | +0.14 / +0.16 / +0.19 | -0.00 / -0.00 / +0.00 | -0.07 / -0.10 / -0.13 | -0.22 / -0.25 / -0.27 | -0.48 / -0.50 / -0.51 |
| 5 (-20) | +0.48 / +0.47 / +0.52 | +0.25 / +0.22 / +0.26 | -0.00 / -0.00 / +0.01 | -0.10 / -0.15 / -0.12 | -0.24 / -0.29 / -0.26 | -0.49 / -0.53 / -0.51 |
| 7 (-7) | +0.46 / +0.46 / +0.51 | +0.21 / +0.21 / +0.25 | +0.01 / +0.01 / +0.00 | -0.14 / -0.13 / -0.09 | -0.28 / -0.27 / -0.24 | -0.52 / -0.52 / -0.49 |
| 11 (-11) | +0.54 / +0.51 / +0.50 | +0.29 / +0.27 / +0.23 | +0.02 / +0.03 / +0.00 | -0.06 / -0.09 / -0.13 | -0.21 / -0.24 / -0.27 | -0.48 / -0.48 / -0.52 |
| 15 (-15) | +0.50 / +0.51 / +0.49 | +0.28 / +0.27 / +0.23 | -0.00 / -0.03 / +0.00 | -0.10 / -0.09 / -0.13 | -0.25 / -0.24 / -0.28 | -0.51 / -0.49 / -0.53 |
| 23 (-23) | +0.51 / +0.49 / +0.53 | +0.31 / +0.26 / +0.26 | +0.06 / +0.06 / -0.00 | -0.05 / -0.08 / -0.11 | -0.21 / -0.22 / -0.24 | -0.44 / -0.46 / -0.48 |
| 31 (-31) | +0.51 / +0.55 / +0.50 | +0.25 / +0.30 / +0.24 | +0.02 / +0.03 / +0.01 | -0.10 / -0.05 / -0.10 | -0.26 / -0.20 / -0.25 | -0.49 / -0.46 / -0.49 |
| 39 (-39) | +0.49 / +0.46 / +0.49 | +0.24 / +0.21 / +0.25 | +0.06 / +0.05 / +0.00 | -0.15 / -0.14 / -0.11 | -0.30 / -0.29 / -0.25 | -0.55 / -0.53 / -0.50 |
| 47 (-47) | +0.45 / +0.51 / +0.49 | +0.23 / +0.26 / +0.23 | +0.06 / +0.01 / +0.01 | -0.15 / -0.10 / -0.09 | -0.29 / -0.25 / -0.25 | -0.53 / -0.51 / -0.50 |

Across the 9 discriminants: mean exponent (sd over d; per-fit se ≈ 0.02–0.05):
s=0: 0.49 (0.03) | 0.25: 0.24 (0.04) | 0.5: 0.02 (0.03) | 0.6: −0.10 (0.03) | 0.75: −0.25 (0.03) | 1: −0.50 (0.03).
So the fitted exponent is β − s with β = 0.50 ± 0.03 at every s: the Möbius row behaves as a detector
of the largest real part of zeros, and here reads off β = 1/2. (Values at X=10^k: M_d(X;0)/√X stays in
[−0.85, 0.77]; M_d(X;1/2) stays in [−0.6, 2.1], consistent with X^{ε} at s=1/2.)

**A.iii Frequencies.** Periodogram of X^{−1/2}M_d(X;0) in u = log X (u ∈ [log 10^3, log 10^7],
resolution ≈ 0.68) vs ordinates γ of zeros of L(1/2+iγ, χ_D) computed with mpmath:

| D | zeros γ < 14 | top periodogram peaks |
|---|---|---|
| −3 | 8.04, 11.25 | 7.5, 8.2, 8.9, 10.9, 11.6 |
| −7 | 4.48, 6.85, 11.16, 12.49 | 4.1, 4.8, 6.8, 10.9, 12.3 |
| −11 | 2.48, 6.80, 8.97, 10.11, 13.04 | 2.0, 2.7, 3.4, 8.9, 9.6 |
| −23 | 2.87, 4.22, 6.73, 8.34, ... | 2.0, 2.7, 3.4, 4.1, 4.8 |

Peaks sit at the low zeros within resolution: the explicit-formula picture X^{−1/2}Σμχ ≈ Σ_ρ X^{iγ}/(ρL'(ρ)) is visible.

## (B) Direct side D(Z) = Σ_{N≤Z} a(N)η(N), η nonprincipal mod q ∈ {5,7,11,13}

Trivial bound Σ|a(N)| ~ Z^{1.500} (exponent 1.5000±0.0000 for r_3, 1.5026 for H). Exponents below are
LS slope of log|D| on a 300-point grid Z ∈ [10^4, Z_max] / dyadic-RMS slope / running-max slope
(se ≈ 0.02 / 0.002 / 0.002). Results are identical for η and η̄, and nearly independent of q and order.

**θ³ (Z_max = 10^7), η of order ≥ 3 (orders 3,4,5,6,10,12):**

| cutoff | exponent (range over 10 characters) | comment |
|---|---|---|
| sharp, LS | 0.49 – 0.55 | |
| sharp, dyadic RMS | 0.533 – 0.536 | Z^{1/2}·(log)^{c}: |D(10^7)| ≈ 10^4 = 6e-7·Z^{3/2} |
| sharp, running max | 0.579 – 0.591 | |
| Riesz C⁰ (1−N/Z)_+ | −0.03 – +0.03 | bounded |
| Riesz C¹ (1−N/Z)²_+ | −0.54 – −0.48 | decays like Z^{−1/2} |
| Gaussian e^{−(N/Z)²} | zero to round-off | |D_W| = 1.5e-10, 4.6e-9, 1.4e-7 at Z=10^4,10^5,10^6 = 0–2 × (10^{−16}Σ|a|W) |

Each derivative of smoothness buys Z^{−1/2}: this is the Voronoi/sphere-problem boundary term
(dual terms oscillating like e(2√(mZ)), amplitude Z^{k/2−1/4} = Z^{1/2} for k=3/2). The twisted
L-function L(s,θ³⊗η) has no poles, so with a Schwartz weight the direct side vanishes faster than any
power, down to machine precision already at Z = 10^4 (Z^{1/2}/q ≈ 20 wavelengths).

**θ³, η quadratic (order 2):** D(Z) = c·Z^{3/2} + O(Z^{1/2+ε}), c = (4π/3)η(−1)(q−1)/q²:
measured D(10^7)/10^{10.5} = +0.67021, −0.51292, −0.34619, +0.29743 (q=5,7,11,13) vs predicted
+0.67021, −0.51291, −0.34618, +0.29743 (the main term is the count Σ_t η(t)#{x∈F_q³: x·x=t}, which
vanishes exactly when ηχ_q is nonprincipal, i.e. for every η of order ≥ 3). After subtracting c Z^{3/2}
the residual has exponents 0.55/0.54 (sharp), 0.01±0.03 (C⁰), −0.48±0.03 (C¹): same as the non-quadratic
case; no Z^1 secondary term for θ³.

**H-series (Z_max = 10^6), η of order ≥ 3:** sharp LS 0.50–0.60, dyadic-RMS 0.544–0.552, runmax
0.60–0.63; Riesz C⁰: −0.02–+0.04; Riesz C¹: 0.000±0.001; Gaussian: a constant (0.2–1.2 for Z=10^4,10^5;
Z=10^6 is a truncation artefact). So for the mock-modular H the smooth direct side tends to an O(1)
constant (a residue at s=0 / non-holomorphic part) instead of 0, still with no growth.
H, η quadratic: D(Z)/Z^{3/2} → 0.0277, −0.0212, −0.0142, +0.0122 (q=5,7,11,13), converging slowly
(0.0259, 0.0273, 0.0277 at Z=10^4,10^5,10^6), i.e. with a secondary term ≈ Z^1 (residual exponents after
subtracting the fitted main term: 0.68±0.04 sharp, 0.51±0.03 C⁰), as predicted by the pole of
L(2s−1,η²) at s=1 in the Shimura decomposition Σ_N a(N)η(N)N^{-s} = Σ_D a(|D|)η(|D|)|D|^{-s}·
L(2s,η²)L(2s−1,η²)/L(2s,χ_Dη²).

## (C) Principal row P(Z) = Σ_{n≤√Z} [a(n²)/a(1)] η(n)² (for H: a(4n²)/a(4), the D=−4 row)

c(n) = c_{−4}(n_odd) [θ³] / c_{−4}(n) [H] verified against the data, then extended by the formula to
n ≤ 10^6 (Z ≤ 10^{12}). Exponents in Z (Y = √Z ∈ [10^2, 10^6]):

| η | sharp P: LS / runmax | Riesz C⁰ in n/Y | Gaussian P_W(Y) | |P_W(Y)| at Y=10^2,10^3,10^4,10^5 |
|---|---|---|---|---|
| θ³ row, order ≥ 3 (10 chars) | 0.49–0.51 / 0.50–0.51 | 0.25–0.29 | 0.22–0.32 (se 0.02–0.07) | ≈ 3–35, 16–88, 20–320, 130–940 |
| H row, order ≥ 3 | 0.48–0.51 / 0.49–0.51 | 0.24–0.28 | 0.19–0.29 | ≈ 3–18, 2–85, 30–300, 100–930 |
| order 2 (η² principal) | 1.000 (main term C·Z, C≈0.36–0.41 [θ³], 0.72–0.83 [H]); residual ~Z^{0.5} | | | |

So for η² nonprincipal: sharp P ~ Z^{1/2} (= Y^1, the boundary term of Σ_{a≤Y} aη²(a)), while any
smoothing exposes the zero-driven size Y^{1/2} = Z^{1/4} (exponent 0.25±0.03): the smoothed principal
row is a genuine zero detector for L(s,χ_{−4}η²) (growth Y^{β_max}), the sharp one is not.

**Ratio |P(Z)|/|D(Z)|, sharp cutoff, same Z** (θ³: Z = 10^4,10^5,10^6,10^7; H: Z = 10^4,10^5,10^6):
θ³: 0.006–0.37, e.g. q=5 ord 4: 0.021, 0.16, 0.0059, 0.0084; q=7 ord 3: 0.11, 0.072, 0.25, 0.16;
q=13 ord 4: 0.28, 0.29, 0.14, 0.0043. H: 0.19–5.4, e.g. q=5 ord 4: 1.6, 0.65, 0.95; q=7 ord 3: 2.1, 0.70, 0.43.
No trend with Z in either case. For quadratic η the ratio decays like Z^{−1/2} (0.0055→0.00017 for q=5).

**Exponent gap (sharp):** D ~ Z^{0.53±0.03}, P ~ Z^{0.50±0.02}: gap −0.03 ± 0.04, i.e. zero within error;
the O(1) ratio for H vs O(10^{−2}–10^{−1}) for θ³ is only the normalisation a(N) ↔ a(N)/a(1) (r_3 ≈ 12–24 H).
**Exponent gap (smooth):** P_W ~ Z^{0.25}, D_W = 0 (θ³) or O(1) (H): gap +0.25, P wins trivially.

## Interpretation (feasibility of a "Shimura-lift common signal" argument)

1. The Möbius row works as advertised: Σ_{n≤X} μ(n)χ_D(n)n^{−s} grows like X^{β−s} with β = 0.50±0.03
   for all nine D and six values of s, and its oscillation frequencies in log X are the ordinates of the
   low zeros of L(s,χ_D). Nothing here is in tension with Shimura's relation, which holds exactly
   (for θ³ only after the 2-adic correction n → n_odd).

2. The direct side carries no common signal to compare against. With any smooth weight,
   Σ_N a(N)η(N)W(N/Z) is identically ≈ 0 for θ³ (machine precision from Z=10^4) and an O(1) constant
   for H, for every η of order ≥ 3. In the Shimura decomposition each row contributes
   L(2s,η²)L(2s−1,η²)/L(2s,χ_Dη²), whose poles at zeros of L(2s,χ_Dη²) would give Z^{ρ/2}; these cancel
   exactly in the sum over D because the twisted form's L-function is entire. The "common" zero signal
   of the rows is therefore invisible on the direct side.

3. With a sharp cutoff the direct side is ≈ Z^{1/2+ε} (measured 0.53–0.59), but this is the Voronoi
   boundary term (frequencies √m, dual coefficients), not zero information, and it is 10–10^2 × larger
   than the principal row for θ³ and comparable for H. A hypothetical off-line zero β of L(s,χ_{−4}η²)
   would make the smoothed principal row ~ Z^{β/2} < Z^{1/2}: never larger than the sharp direct side,
   and "larger than 0" with smooth weights carries no contradiction. The balanced probe cannot work in
   either regime.

4. What would be needed: an averaging variable (over D, or a family of twists) that breaks the
   cancellation across rows and lowers the direct-side noise below the row signal, i.e. a gain of
   Z^{(1−β)/2} ≥ Z^{1/4−δ/2} over the sharp boundary term — with square-root cancellation a family of
   size ≳ Z^{1−β}; otherwise an identity isolating a single D-row (which is just P itself).

Limitations: Z ≤ 10^7 (θ³) and 10^6 (H); exponents carry log factors (dyadic-RMS slopes 0.53–0.55
instead of 0.50); only conductors q ≤ 13 and |D| ≤ 47; fitted exponents have ±0.03–0.05 scatter;
H-series secondary terms were only fitted, not derived.

Qualification (referee pass R2): note S0 §1 says a cuspidal $g$ is required, while the tests above use non-cuspidal $g$ only; the refutation transfers because it uses only that $L(s,g\otimes\eta)$ is entire, which holds for cuspidal $g$ as well.
