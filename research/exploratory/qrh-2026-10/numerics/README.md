# Finite numerical checks: QRH Lemma 7.1, Kintali eq. (1), joint moment, cubic Gauss sums

```text
Status: EXPLORATORY. Labels per item: EXACT (integer or Gaussian-integer arithmetic,
        or sympy identity), FLOATING_RECONNAISSANCE (ordinary double precision; not
        directed, not certified), EMPIRICAL (statistics at finite size). No RH claim. No
        claim about the manuscripts' main theorems.
Scope: finite only. Lemma 7.1: brute force in O/p^t for N p <= 31, t <= 4; series vs
       closed form for all 77 good primes with N p <= 400. Kintali eq. (1): all odd c with
       N(c) <= 10^4; every class mod 36; 342,684 coprime pairs with N <= 2000. Joint moment:
       D <= 8000. Cubic Gauss sums: N c <= 2*10^5.
Exact sources or dependencies: OpenAI QRH manuscript (30 Sep 2026; sha256 in
       ../scripts/SOURCES.txt), Sections 4.1, 4.2 and 7.2, eqs. (4.1)-(4.2), Prop. 8.3;
       Kintali QRH manuscript, eq. (1) and App. A.1. Formulas were read from the rendered
       PDFs (pdftoppm, 250-400 dpi); see the warning below. eisenstein.py is a verbatim copy
       of the w5copg branch file (details below).
What was actually run: see "Commands" (Python 3, numpy 2.5.3, sympy 1.14.0). Total about 4.5 min.
Smallest remaining gap: (1) The coefficient (7.4) was never checked to factor into the local
       series (7.10). That step uses the unit factor (7.9), the b_*/xi/tau cancellation and the
       pair-phase cancellation, and only the local identity was checked here. (2) The
       analytic assertions of Lemma 7.1 were only sampled. (3) Everything here is finite.
```

RH remains unsolved. Nothing here supports the manuscripts' zero-free half-planes. These
checks show only that particular finite algebraic identities used inside the arguments
hold for the computed cases.

## Relation to prior work (not duplicated)

Branch `origin/claude/openai-math-riemann-analysis-w5copg` (head `bd670c92`), in
`standalone/2026-10-07-openai-quasi-rh/numerics/` (`RESULTS.md`, `eisenstein.py`,
`check_identities.py`, `mean_square.py`), already checks the prime and composite Gauss
identities. In the present manuscript's numbering these are Lemma 4.2, (4.5)-(4.7) and
sextic reciprocity (e). That branch covers:

* every squarefree primary n with N(n) <= 50000, to max error <= 5e-15;
* γ_3 = four-term formula;
* χ_n(4) = n mod 2;
* G constant on classes mod 4;
* the sextic mean square for D <= 102,400.

Those checks were **not repeated** here; cite w5copg for them.

`eisenstein.py` in this folder is a byte-identical copy of the w5copg file. It is git blob
`85fb092d69c70097cd67c569e621889100749c98`, sha256 `bc6af658...e584ae9`. It was read
before running.

## Warning: the text extraction drops overbars

`paper.txt` (pdftotext) loses every complex-conjugation bar. Compare the extracted text
with the PDF:

| eq. | extracted text gives | PDF has |
|---|---|---|
| (7.6) | `a_p = α(p)³η(p)³` | `\bar α(p)³ η(p)³` |
| (7.6) | `b_p = α(p)²η(p)²χ_p(4)` | `\bar α(p)² η(p)² \bar χ_p(4)` |
| (7.10) | `(a_p γ_3)^l` | `(a_p \bar γ_3)^l` |
| (7.12) | `D = η(p)χ_p(u)Q^{-x}` | `D = η(p) \bar χ_p(u) Q^{-x}` |
| Lemma 4.2 | `H(4)` | `\bar H(4)` |
| (4.7) | `G(c) = χ_c(4)γ_3(c)` | `G(c) = \bar χ_c(4) γ_3(c)` |
| Kintali (1) | `G(c) = χ_c(4)Γ_q(c)` | `G(c) = \bar χ_c(4) Γ_q(c)` |

The Lemma 7.1 identity **fails** when any one of these bars is dropped (ablation rows
below). Any repository transcription made from `paper.txt` should be re-read against the
PDF.

## Results

| # | identity / claim | range checked | max deviation | verdict | label |
|---|---|---|---|---|---|
| L1 | (7.7) = (7.8): local Poisson coefficient C_p(t,k,j′), brute force in O/p^t | split N=7 (t≤4, k≤3), 13, 19 (t≤3, k≤2), 31 (t≤2); inert N=25 (t≤2); j′≤t+2; 524 cases, 117 nonzero | 3.3e-14 (rel.) | PASS | FLOATING_RECONNAISSANCE |
| L2 | Gauss lifts g_{χ^r}(p^t,p^{j′}) (both lines, incl. Ramanujan case 6\|r) | same primes, r=0..5; 630 cases | 9.4e-16 (rel.) | PASS | FLOATING_RECONNAISSANCE |
| L3 | series (7.10) = closed form (7.11), P_p and P_p^* | all 77 good primes with N≤400 (74 split, 3 inert); j=0..5; ρ∈μ_6 random; η random unit modulus; Im x, w, z ~ N(0,25); 2×1386 cases | P: 2.2e-15; P^*: 6.6e-14 (rel.) | PASS | FLOATING_RECONNAISSANCE |
| L3a | ablation: drop the bar on γ_3 in (7.10) | 12 primes × 6 j | 0.43 (j=2,3,4 fail) | identity FAILS | (control) |
| L3b | ablation: drop the bar on χ_p(4) in b_p | same | 0.15 (j=3 fails) | FAILS | (control) |
| L3c | ablation: α in place of \bar α in a_p, both sides | same | 0.074 (j=3 fails) | FAILS | (control) |
| L3d | ablation: random Gauss phases \|G_r\|=√Q (Lemma 4.2 violated) | same | 0.16 | FAILS | (control) |
| L4 | table (7.16) sums to (7.11), each j=0..5 (geometric sums in R, V) | symbolic | difference ≡ 0 | PASS | EXACT (sympy) |
| L5 | (7.17): H_p−1 = [D(V+W−VW)−VW+(1−V)(1−W)E_p]/(1−D), and the W=D=0 case | symbolic | ≡ 0 | PASS | EXACT (sympy) |
| L6 | stated decay at the (7.15) corner x=7/8, z=33/200, w=19/20: \|H_p−1\|Q^{363/200} (p∤u), \|H_p−1\|Q^{33/40} (p\|u) | Q = 7 … 10^6, 400 random phase draws each | scaled values 2.6→0.81 and 1.41→1.02 (bounded, decreasing) | consistent | FLOATING_RECONNAISSANCE |
| L6′ | same at the (7.14) corner x=.51, z=.34, w=.53 (ε_0=.04): Q^{1.02}, Q^{0.02} scalings | same | 2.2→1.09 and 3.1→2.09 | consistent | FLOATING_RECONNAISSANCE |
| K1 | Kintali (1): Γ_q(c) = \|c\|^{-1}Σ_{x mod c} e(x²/c) = (1+i^{-b}+i^a+i^{b-a})/2, every odd c | all 27,234 odd c with N(c)≤10^4: 24,207 non-primary, 9,072 divisible by λ, 3,018 divisible by 3 | 1.3e-14 | PASS | FLOATING_RECONNAISSANCE |
| K2 | \|Γ_q\|=1; Γ_q periodic mod 4; R(v,w) ∈ {±1}, symmetric, bicharacter on all 12 odd classes mod 4 | 1,728 triples | 0 failures | PASS | EXACT |
| K2′ | 108 primary classes mod 36 prime to 6: R sign-valued, symmetric, independent of lifts, bicharacter; \|G\|=1; G(vw)=G(v)G(w)R(v,w) | 108² pairs, 108³ = 1,259,712 triples | 0 failures; \|G\|−1 ≤ 1.1e-16 | PASS (descends mod 36; in fact G is a function mod 4, i.e. on ray classes mod 12, and not mod 2) | EXACT |
| K2″ | OpenAI (4.4) table r((−1)^eλ^f,(−1)^gλ^h)=(−1)^{eh+fg+fh}; Γ_q(1,−1,λ,−λ)=(1,1,i,−i) | all 16 | 0 | PASS (re-check of w5copg) | EXACT |
| K3 | G(p³)=Γ_q(p)=γ_3(p); R(p,p)=χ_p(−1); χ_p(4)=(p mod 2); G(p²)=χ_p(4) | 2,265 primes N≤20000 | 0 failures | PASS | EXACT (symbols) |
| K4 | (A.2) χ_v(w)=R(v,w)χ_w(v) incl. **nonsquarefree** coprime primary v, w; χ_n(−1)=R(n,n) | 606 ideals N≤2000 (39 nonsquarefree), 342,684 ordered pairs | 0 failures | PASS | EXACT |
| J | joint moment (below) | D=L=U ∈ {500,…,8000}; D=8000, L=2000 | see table | no anomaly vs multiplicative null | EMPIRICAL |
| P | Σ γ_2(c)α(c)^k over primary squarefree (c,6)=1, N c≤X | X ≤ 2·10^5 (56,433 terms) | see below | X^{5/6} for k=0 only | EMPIRICAL |

Convention notes. All checks use the following conventions:

* χ_p(a) ≡ a^{(N p−1)/6} mod p.
* "Primary" means ≡ 1 mod 3.
* e(z) = exp(2πi·(ω-coordinate of z)), which equals exp(4πi Im z/√3).
* Inert primes use the generator −q.

With exactly these conventions and the PDF's overbars, every identity above holds.

* L3 uses the actual G_r of each prime. The ablations show that the table depends on the
  Lemma 4.2 relations: γ_1γ_2 = −α\barχ_p(4)γ_3, γ_4/γ_1 = −\barα/G(p), γ_2γ_4 = 1 and
  γ_3² = ω_p. An earlier 110-dpi rendering seemed to show `−\overline{α/G}`; the
  400-dpi rendering shows `−\overline{α(p)}/G(p)`, which is what holds.
* η was taken to be an arbitrary unit complex number, not only a root of unity, and the
  identity still held.
* Kintali's statement that the formula for R "applies also to noncoprime pairs" is
  definitional and was not tested further.

## Joint moment test (EMPIRICAL)

The objects are M_u(t) = D^{-1/2}Σ_n μ(n)χ_n(u)W(Nn/D)N(n)^{-it} and
S_u(t) = L^{-1/2}Σ_l χ_l(u)W(Nl/L)N(l)^{-it}.

* n runs over squarefree ideals and l over all ideals, both prime to 6.
* W(y) = e^{4−1/((y−1)(2−y))} on (1,2).
* Rows are all elements u with U ≤ N u < 2U and (u,6)=1.
* The twist grid is |t| ≤ 25 in steps of 0.04.
* t_u = argmax_t |M_u S_u|, which is the single common height that Prop. 8.3 assigns to a row.

Two null models use the same supports and weights:

* **iid**: each χ_n(u) is replaced by an independent uniform sixth root of unity;
* **mult**: each χ_p(u) is randomised and the result extended multiplicatively, so M_u
  and S_u share prime values as the true characters do.

| D=L=U | rows | E max\|M\|² | E max\|S\|² | joint_max / marg_max (sextic · iid · mult) | joint_max / typical-t marginals | corr(max\|M\|², max\|S\|²) (sextic · iid · mult) |
|---|---|---|---|---|---|---|
| 500 | 900 | 0.176 | 0.177 | 0.640 · 0.635 · 0.683 | 3.06 | 0.118 · −0.021 · 0.113 |
| 1000 | 1824 | 0.172 | 0.182 | 0.679 · 0.610 · 0.648 | 3.22 | 0.184 · 0.016 · 0.126 |
| 2000 | 3600 | 0.172 | 0.174 | 0.653 · 0.626 · 0.667 | 3.10 | 0.139 · 0.029 · 0.142 |
| 4000 | 7278 | 0.166 | 0.177 | 0.637 · 0.629 · 0.651 | 3.05 | 0.077 · 0.015 · 0.101 |
| 8000 | 14472 | 0.168 | 0.176 | 0.650 · 0.626 · 0.650 | 3.14 | 0.121 · 0.016 · 0.121 |
| 8000 (L=2000) | 14472 | 0.168 | 0.179 | 0.654 · 0.621 · 0.650 | 3.18 | 0.142 · 0.008 · 0.105 |

Reading:

* The rowwise-maximised joint moment E_u max_t|M_uS_u|² is about 0.65 times the product of
  the separately maximised marginals.
* It is about 3.1 times the product of the typical-twist marginals. That factor is the
  cost of maximising over a window of length 50.
* There is a small positive row correlation (about 0.1) between max|M|² and max|S|². The
  multiplicative null reproduces it, and the iid null does not. It therefore comes from
  M and S sharing prime values, not from anything specific to the arithmetic of χ_n(u).
* No ratio drifts with D across 500 to 8000.

This is consistent with the rows behaving like a random multiplicative family at these
sizes, and says nothing asymptotic.

## Cubic Gauss-sum sums (EMPIRICAL; Patterson mechanism reconnaissance)

Inputs and validation:

* γ_2 at primes was computed by direct summation.
* The identity γ_2(p)³ = −α(p) held to 3.9e-15 for all 18,019 primes with N ≤ 2·10^5.
* The shortcut γ_2(\bar π) = \overline{γ_2(π)} was checked to 1.8e-15 for N ≤ 2·10^4.
* Composite c were handled with the CRT rule γ_2(ab) = γ_2(a)γ_2(b)χ_b(a)^4. It matched
  direct sums to 1.9e-15 on 425 composites with N ≤ 3000.

Results for 5000 ≤ X ≤ 2·10^5:

* **k = 0:** |S_0(X)|/X^{5/6} = 0.195–0.198, stable. The fitted exponent is 0.840, against
  5/6 = 0.833. This matches the Heath-Brown–Patterson main term.
* **k ∈ {±1, ±2, 3}:** |S_k(X)|/X^{1/2} stays between 0.004 and 0.36. At X = 2·10^5,
  |S_k| ≤ 81, while √X = 447 and a random walk of 56,433 unit terms would be about 238.
  - The angular twist removes the X^{5/6} term at this range.
  - The fitted log-log exponents are unstable (−0.2 to 0.6) because the sums oscillate. No
    exponent should be read off them.

A finite fit is not a theorem.

## Commands

From this directory. `-I` is isolated mode, and the scripts add their own directory to `sys.path`.

```
python3 -I check_local_euler.py results/local_euler.json                       # 51.8 s
python3 -I check_kintali_phase.py results/kintali_phase.json 10000             # 17.1 s
python3 -I joint_moment.py results/joint_moment.json 500 1000 2000 4000 8000   # 83.9 s
python3 -I patterson_probe.py results/patterson_probe.json 200000              # 106.7 s
```

The JSON output and the full logs are in `results/`.

| file | content |
|---|---|
| `check_local_euler.py` | Lemma 7.1: (7.7) vs (7.8) brute force; lifts; (7.10) vs (7.11); ablations; sympy (7.16), (7.17); decay probe |
| `check_kintali_phase.py` | Kintali (1), A.1, A.2: Gauss-sum evaluation, exhaustive classes mod 4 and mod 36, symbols |
| `joint_moment.py` | rowwise-maximised joint moment vs marginals, with two null models |
| `patterson_probe.py` | growth of Σ γ_2(c)α(c)^k |
| `eisenstein.py` | O = Z[ω] arithmetic and sextic-symbol tables (verbatim from w5copg) |
