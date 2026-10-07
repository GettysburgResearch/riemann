# Numerical sanity check of the arithmetic core of "The Quasi-Riemann Hypothesis" (OpenAI, Oct 5 2026)

**Status: EMPIRICAL CHECK ONLY.** These computations test the paper's conventions and
finite identities, and look at the qualitative size of the mean square in
Proposition `thm:ms`. They do not prove anything, and they are **not evidence for the
asymptotic bound**. See "Interpretation" below.

## Files

| file | purpose |
|---|---|
| `eisenstein.py` | arithmetic in O = Z[ω], prime ideals, sextic-symbol tables (checked against exact computation) |
| `check_identities.py` | Task 1: Lemma `lem:arithmetic` for every squarefree primary n with N(n) ≤ 50000 |
| `mean_square.py` | Task 2: A_u(D), S(D,H), how S splits by the type of u, the amplification step |
| `make_tables.py` | turns the JSON output into the tables below |
| `identities.json`, `identities.log` | Task 1 output |
| `mean_square.json`, `mean_square.log` | Task 2 output |

To reproduce, run these from this directory. `-I` is isolated mode. The scripts add their own directory to `sys.path` explicitly.

```
python3 -I check_identities.py 50000 2000 identities.json          # ~70 s
python3 -I mean_square.py mean_square.json 100 200 400 800 1600 3200 6400 12800 25600 51200 102400   # ~13 min, 4 cores
python3 -I make_tables.py identities.json mean_square.json
```

## Conventions (as stated in paper §2 "Step 2", §3, Lemma `lem:arithmetic`, App. `app:gauss-identities`)

* O = Z[ω] with ω = e^{2πi/3}. An element a+bω is stored as (a,b). N(a+bω) = a²−ab+b².
* "Primary" means ≡ 1 mod 3O, that is a ≡ 1 and b ≡ 0 mod 3. S = {(2), (λ)} with λ = 1+2ω, and ν is trivial.
* Primes prime to 6 come in two kinds:
  * Split primes π are primary with N(π) = p ≡ 1 mod 3. They use O/π ≅ F_p through ω ↦ r = −a·b⁻¹ mod p.
  * Inert primes have primary generator −q, where q ≡ 2 mod 3 and q ≠ 2. They have N = q² and use O/q ≅ F_q[ω] = F_{q²}.

  Both kinds occur in every test. For example, 784 of the 14120 n in Task 1 have an inert factor.
* χ_p(u) = (u/p)_6 is the sixth root of unity ≡ u^{(N(p)−1)/6} mod p. It is 0 when p | u.
  * It is computed from discrete-log-mod-6 tables of the residue field.
  * 18000 random (u,p) values are checked against exact big-integer computation of u^{(N(p)−1)/6} mod p in O.
  * For squarefree primary n, χ_n = ∏_{p|n} χ_p.
* e(z) = exp(4πi·Im z/√3). For z = (c+dω)/M this is exp(2πi d/M).
* γ_j(n) = N(n)^{−1/2} Σ_{x mod n} χ_n(x)^j e(x/n).
  * It is computed **directly**, summing over the complete residue system {c + dω : 0 ≤ c < N/g, 0 ≤ d < g} with g = gcd(a,b). No CRT factorisation is used.
  * The other quantities are α(n) = n/|n|, μ(n) = (−1)^{#primes}, and G(n) = conj(χ_n(4))·γ_3(n).

## Task 1: Lemma `lem:arithmetic`

Every one of the **14120** squarefree primary n prime to 6 with **N(n) ≤ 50000** is tested. 8985 of them are composite.

| identity | max abs error |
|---|---|
| (a) γ_2(n)³ = μ(n)α(n) | 4.8e-15 |
| (b) γ_1γ_2 = μαG, with G = conj(χ_n(4))γ_3 | 2.9e-15 |
| (c) γ_1γ_{−1} = χ_n(−1) | 2.8e-15 |
| (d) μγ_{−1} = χ_n(−1)G⁻¹·conj(α)·γ_2 | 2.4e-15 |
| \|G(n)\| = 1 | 1.1e-15 |
| γ_3(a+bω) = (1 + i^{−b} + i^a + i^{b−a})/2 (closed form in the appendix) | 1.2e-15 |
| χ_n(4) = (n mod 2) ∈ {1, ω, ω²} (appendix) | 0 |
| (e) χ_b(a)/χ_a(b) ∈ {±1}, over 303320 coprime ordered pairs with N ≤ 2000 | 5.8e-16 |
| (e) R(a,b) agrees with (−1)^{eh+fg+fh} on square classes (−1)^e λ^f | 0 mismatches |
| (e) R(a,b) depends only on (a mod 4, b mod 4) | 0 of 144 class pairs inconsistent |
| (e) R(a,b) = Γ_quad(ab)/(Γ_quad(a)Γ_quad(b)) | 0 |
| G(ab) = G(a)G(b)R(a,b), over 19370 pairs with N(ab) ≤ 50000 | 2.2e-15 |
| `eq:crt-a`: a(ab) = a(a)a(b)χ_b(a)⁴ with ξ = 1 | 5.0e-15 |
| χ_n(−1) = R(n,n) | 1.2e-16 |
| class level, all 144 pairs of classes mod 4: G(ab) = G(a)G(b)R(a,b) | 1.8e-15 |
| class level, `eq:quotient`: G(a⁻¹) = χ_a(−1)·conj(G(a)) | 9.0e-16 |

**How G depends on n mod m.** The table gives the largest spread of G inside a residue class of n mod mO.

| m | classes hit | max spread of G within a class |
|---|---|---|
| 2 | 3 | 2.0 (not constant) |
| 4 | 12 | 1.6e-15 |
| 8, 12, 24, 36, 72 | 48, 12, 48, 108, 432 | ≤ 1.8e-15 |

**4 is the smallest modulus in the list on which G is constant**, and 2 does not work. Because n is primary, its class mod 4 is the same thing as its class in the ray class group mod 12, which is ≅ (O/4O)^×. G takes 12th roots of unity as values:

| n mod 4 | (1,0) | (3,0) | (1,1) | (3,3) | (0,1) | (0,3) | (1,2) | (3,2) | (3,1) | (2,3) | (2,1) | (1,3) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G | 1 | 1 | ω | ω | ω̄ | ω̄ | i | −i | e^{iπ/6} | e^{−iπ/6} | e^{5iπ/6} | e^{7iπ/6} |
| χ_n(−1) | + | + | + | + | + | + | − | − | − | − | − | − |

**Verdict:** No identity fails. The paper's conventions are internally consistent:
* the primary normalisation;
* the additive character e;
* the definition χ_p(u) ≡ u^{(N(p)−1)/6};
* the sign J(χ²,χ²) = −p, which gives γ_2(p)³ = −α(p).

They are also consistent for inert primes and for composite n, and with the closed forms used in Appendix `app:gauss-identities`.

## Task 2: the mean square (eq. `ms` / `intro-ms`)

The family is A_u(D) = Σ μ(n)χ_n(u)W(N(n)/D), summed over squarefree primary n prime to 6.
* W(y) = exp(4 − 1/((y−1)(2−y))) on (1,2). This is a bump with max 1 and ∫W² = 0.289.
* u runs over **all** nonzero u ∈ O with N(u) ≤ H, units and non-primary u included.
* S(D,H) = Σ|A_u(D)|².
* `diag` is the exact diagonal term Σ_n W(N(n)/D)²·#{u : N(u) ≤ H, (u,n) = 1}. This is the value S would take if the rows u ↦ χ_n(u) were exactly orthogonal.

The rows of u are split into four types:
* **sixth**: u = unit·v⁶. Here χ_n(u) = χ_n(unit)·1_{(n,v)=1}.
* **cube**: unit·v³, not a sixth power. These are quadratic twists.
* **square**: unit·v², not a sixth power. These are cubic twists.
* **rest**: everything else.

Each type's column gives its contribution to S, with the number of u in parentheses.

| D | #n | Σw²/D | θ | H | #u | S/(DH) | S/diag | sixth | cube | square | rest | max_rest \|A_u\|²/Σw² |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100 | 28 | 0.0822 | 0 | 100 | 366 | 0.2928 | 1.0164 | 133 (6) | 120 (12) | 201 (30) | 2474 | 4.50 |
| 100 | 28 | 0.0822 | 0.1 | 158 | 582 | 0.3043 | 1.0568 | 133 (6) | 120 (12) | 223 (36) | 4347 | 4.50 |
| 400 | 119 | 0.0790 | 0 | 400 | 1458 | 0.2729 | 1.0032 | 708 (6) | 1.02e3 (24) | 1.39e3 (66) | 4.06e4 | 6.59 |
| 400 | 119 | 0.0790 | 0.1 | 728 | 2646 | 0.2703 | 0.9970 | 708 (6) | 1.02e3 (24) | 1.68e3 (84) | 7.53e4 | 6.59 |
| 1600 | 457 | 0.0801 | 0 | 1600 | 5814 | 0.2782 | 1.0136 | 7.37e3 (12) | 3.11e3 (24) | 1.44e4 (138) | 6.87e5 | 7.50 |
| 1600 | 457 | 0.0801 | 0.1 | 3346 | 12120 | 0.2727 | 0.9965 | 7.37e3 (12) | 4.77e3 (42) | 2.33e4 (198) | 1.42e6 | 9.46 |
| 3200 | 898 | 0.0799 | 0 | 3200 | 11628 | 0.2759 | 1.0082 | 5.81e3 (12) | 1.26e4 (42) | 4.94e4 (186) | 2.76e6 | 8.11 |
| 3200 | 898 | 0.0799 | 0.1 | 7172 | 26016 | 0.2740 | 1.0028 | 8.71e3 (18) | 1.65e4 (54) | 7.97e4 (294) | 6.18e6 | 10.70 |
| 6400 | 1799 | 0.0824 | 0 | 6400 | 23232 | 0.2819 | 1.0045 | 2.25e4 (18) | 2.99e4 (42) | 1.26e5 (276) | 1.14e7 | 10.56 |
| 6400 | 1799 | 0.0824 | 0.1 | 15374 | 55764 | 0.2812 | 1.0029 | 2.25e4 (18) | 3.57e4 (66) | 1.78e5 (420) | 2.74e7 | 12.77 |
| 12800 | 3623 | 0.0823 | 0 | 12800 | 46452 | 0.2843 | 1.0139 | 2.93e4 (18) | 7.68e4 (66) | 3.79e5 (402) | 4.61e7 | 15.09 |
| 12800 | 3623 | 0.0823 | 0.1 | 32956 | 119562 | 0.2824 | 1.0076 | 2.93e4 (18) | 1.28e5 (102) | 5.82e5 (642) | 1.18e8 | 15.37 |
| 25600 | 7224 | 0.0814 | 0 | 25600 | 92844 | 0.2772 | 0.9987 | 9.70e4 (18) | 1.87e5 (90) | 1.10e6 (564) | 1.80e8 | 11.46 |
| 25600 | 7224 | 0.0814 | 0.1 | 70642 | 256212 | 0.2781 | 1.0020 | 9.70e4 (18) | 3.24e5 (132) | 1.85e6 (936) | 5.01e8 | 14.24 |
| 51200 | 14441 | 0.0815 | 0 | 51200 | 185772 | 0.2779 | 1.0002 | 2.55e5 (18) | 6.23e5 (120) | 3.01e6 (804) | 7.25e8 | 13.25 |
| 51200 | 14441 | 0.0815 | 0.1 | 151425 | 549354 | 0.2770 | 0.9973 | 3.72e5 (30) | 7.61e5 (168) | 5.21e6 (1386) | 2.14e9 | 16.57 |
| 102400 | 28894 | 0.0816 | 0 | 102400 | 371484 | 0.2792 | 1.0034 | 1.42e5 (18) | 1.12e6 (144) | 9.29e6 (1140) | 2.92e9 | 18.56 |
| 102400 | 28894 | 0.0816 | 0.1 | 324586 | 1177398 | 0.2783 | 1.0000 | 2.23e5 (30) | 1.73e6 (222) | 1.60e7 (2034) | 9.23e9 | 18.56 |

`mean_square.json` and `mean_square.log` also hold θ = 0.05 and D = 200 and 800. Those rows show the same pattern: S/(DH) ∈ [0.260, 0.292] and S/diag ∈ [0.958, 1.037].

The next table gives the mean of |A_u|²/Σw² for each type of u (θ = 0.1). It also gives two more statistics:
* the normalised fourth moment E|A_u|⁴/(E|A_u|²)² over the "rest" rows, which would be 2 if the A_u were complex Gaussian;
* the share of S that comes from the sixth-power rows.

| D | 100 | 400 | 1600 | 6400 | 25600 | 51200 | 102400 |
|---|---|---|---|---|---|---|---|
| unit·cube (quadratic twists) | 1.21 | 1.34 | 0.89 | 1.03 | 1.18 | 1.09 | 0.93 |
| unit·square (cubic twists) | 0.75 | 0.63 | 0.92 | 0.80 | 0.95 | 0.90 | 0.94 |
| rest | 1.00 | 0.94 | 0.94 | 0.94 | 0.94 | 0.94 | 0.94 |
| E\|A\|⁴/(E\|A\|²)², rest | 1.80 | 2.01 | 2.03 | 2.11 | 2.11 | 2.13 | 2.14 |
| sixth-power share of S | 2.8e-2 | 9.0e-3 | 5.0e-3 | 8.1e-4 | 1.9e-4 | 1.7e-4 | 2.4e-5 |

The value 0.94 for "rest" is the loss from u with (u,n) ≠ 1.

**A_1 and the amplification step.** The paper uses the trivial bound Σ_{p|n}|W| for |A_{p⁶} − A_1|. The last column gives that bound for N(p) = 7.

| D | \|A_1\| | \|A_1\|/√D | max over units \|A_ε\| | \|A_{p⁶}−A_1\|, N(p)=7 | N(p)=13 | N(p)=19 | N(p)=25 (inert) | Σ_{p\|n}\|W\|, N(p)=7 |
|---|---|---|---|---|---|---|---|---|
| 400 | 9.87 | 0.49 | 14.9 | 1.85 | 1.03 | 2.52 | 0.15 | 5.3 |
| 1600 | 2.07 | 0.05 | 31.2 | 10.5 | 5.98 | 4.01 | 1.36 | 19.9 |
| 6400 | 30.2 | 0.38 | 45.8 | 3.95 | 7.43 | 1.36 | 9.69 | 86.9 |
| 12800 | 38.0 | 0.34 | 58.1 | 3.46 | 8.39 | 6.80 | 6.23 | 177 |
| 25600 | 29.4 | 0.18 | 111 | 17.6 | 6.49 | 10.0 | 14.8 | 347 |
| 51200 | 21.1 | 0.09 | 184 | 9.18 | 21.3 | 8.80 | 15.3 | 689 |
| 102400 | 60.0 | 0.19 | 115 | 1.78 | 11.6 | 12.5 | 17.1 | 1388 |

**Consistency checks**, all D:
* max |A_{ū} − conj(A_u)| = 1.0e-12.
* A_{ε·λ⁶} = A_ε holds exactly, since λ ∈ S.
* The value of A_{p⁶} − A_1 from the χ machinery matches the direct formula −Σ_{p|n} μ(n)W(N(n)/D) to 2.9e-12.

## Interpretation (sober)

1. **Arithmetic identities.** Everything in Lemma `lem:arithmetic` that can be checked finitely holds to machine precision with the paper's stated conventions. This covers (a)–(d), the reciprocity factor R, the multiplicativity rule for G, `eq:crt-a`, and `eq:quotient` at the level of classes. It holds for split and inert primes and for composite n.

   G(n) is a function of n mod 4 when n is primary, i.e. it lives on the ray class group mod 12 ≅ (O/4)^×. R is the stated symmetric ±1 bicharacter.

   No convention mismatch was found: the generator choice, e(z), the sign of J(χ²,χ²) and the definition of χ_n(4) all agree. These are classical Gauss–Jacobi and reciprocity facts, so this mainly confirms that the paper's normalisations and signs are right.

2. **Mean square at accessible scales.** For D from 100 to 102400 and θ ∈ {0, 0.05, 0.1}, S/(DH) stays between 0.26 and 0.30. It equals the diagonal prediction (2π/√3)·(Σw²/D)·(coprimality factor ≈ 0.94) ≈ 0.278 to within a few percent, and to within 0.5% for D ≥ 25600.

   S/diag = 1.000 ± 0.04. A least-squares fit of S/diag against log D has slope 0.0024 per unit of log D. That is statistically flat, and there is no visible growth like a power of log D.

   So at these sizes the rows χ_n(·) behave as if exactly orthogonal over 0 < N(u) ≤ H, even at θ = 0 (H = D). This is consistent with eq. `ms` and is what "square-root cancellation on average" predicts.

   The largest single |A_u|²/Σw² grows slowly, from 4.5 to 18.6 as #u goes from about 10² to 10⁶. At D = 102400 this is somewhat above the complex-Gaussian estimate 0.94·ln(#u/2) ≈ 12.5. The /2 is there because |A_ū| = |A_u|.

   The normalised fourth moment over the "rest" rows drifts from 2.0 to 2.14. So the tails are mildly heavier than Gaussian. A plausible cause is that E|A_u|² varies with the small prime factors of u, and a mixture of variances raises the fourth moment. This has no visible effect on S.

3. **Breakdown by type of u.** There are at most 30 rows u = unit·v⁶. They contribute 2.8% of S at D = 100, and this falls to 2.4e-5 at D = 102400 (θ = 0.1). For these rows A_u is a Möbius sum twisted by a fixed Hecke character, and max_ε |A_ε| ≈ (0.25–0.82)·√D, which is GRH-sized.

   The quadratic-twist rows (u = unit·cube) and cubic-twist rows (u = unit·square) have mean |A_u|² equal to the generic one, within small-sample noise. The quadratic-twist rows are where a Landau–Siegel-type correlation between μ and a quadratic character would show up as a large |A_u|. No anomaly is seen, which is expected at these sizes.

4. **A_1.** |A_1(D)| ≈ (0.05–0.5)·√D, oscillating as D varies. This is GRH-type behaviour and far below the paper's D^{11/12}.

   |A_{p⁶} − A_1| is much smaller than the trivial bound Σ_{p|n}|W| that the paper uses, because it is itself a Möbius sum. The paper's argument only needs the trivial bound, which is fine.

   At these sizes Y = H^{1/6} ≤ 8.3. So the amplification inequality `prime-extract` has no numerical content here: only primes of norm 7 have p⁶ ≤ H, and only once H ≥ 117649.

5. **What this does *not* show.**
   * The asymptotic claim S ≪ D^{2+θ+ε} is a statement about all D. Ranges up to D ≈ 10⁵ cannot separate it from bounds with extra powers of log, or with secondary terms whose constants are small or which only matter at larger D.
   * Möbius coefficients are expected to look random at this scale anyway. Any real obstruction to Theorem 1.1, such as a Landau–Siegel zero of huge conductor or zeros with Re ρ > 11/12, would show up only at sizes far beyond reach.
   * The analytic parts of the proof are not tested at all: Poisson summation, the theta transformation and cusp expansions, the quadratic large sieve input, and the recursive descent. Only their arithmetic input (Lemma `lem:arithmetic`) and the qualitative size of the target mean square are checked.
   * Only ν = trivial and one weight W were used.
