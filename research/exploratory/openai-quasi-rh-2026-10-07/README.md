# OpenAI's quasi-Riemann hypothesis (family 003): reconstruction, checks and a programme

```text
Status: IMPORTED (external claim, not reviewed here) + EMPIRICAL (two floating checks) + PROPOSED (programme)
Scope: global external statement (Re s > 7/8); our checks are finite and floating
Exact sources or dependencies: github.com/openai/math @ adc7f1241b42e322a6451854ab7e4b4c146bf78a (2026-10-06)
  preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/  (7/8, 16.7k lines of TeX)
  preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/     (11/12, human-edited, 4k lines)
  preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/
  lean/docs/003.md, lean/ComparatorChallenges/{QuasiRiemannHypothesis,DirichletSevenEighths,HeckeSevenEighths,SiegelZeros}.lean
What was actually run: scripts/gauss_identity_check.py (FLOATING_RECONNAISSANCE), scripts/family_mean_square.py (FLOATING_RECONNAISSANCE),
  scripts/endpoint_certificate_replay.py (exact-rational grid search, not a certificate);
  a source audit of the Lean tree (see section 3). No Lean build or comparator run was completed here.
Smallest remaining gap: for RH itself, theta = 3/8 -> 0 in every fixed-detector hook below; for this note, an independent
  Lean build/comparator replay and an exact replay of the Part II exponent certificate.
```

RH remains unproved. Nothing here changes that. The external result is a **fixed zero-free half-plane**, not the critical line.

## 1. What is claimed

**Theorem (OpenAI 003, 7/8 paper, Thm 1.1).** Every finite-order Hecke L-function over $F=\mathbb{Q}(\sqrt{-3})$ has no zero in $\Re s>7/8$. The same holds for every Dirichlet L-function, including $\zeta$. The principal pole at $s=1$ is allowed.

The result is uniform in the conductor and the height. Companion claims are:

- **11/12, a second proof** (October 5 paper, human-edited). It uses a different and simpler route, described in §2.1.
- **Landau–Siegel.** An absolute $c>0$ with $(1-\beta)\log q\ge c$ for every real zero of every real primitive character. This uses an **independent** interpolation-determinant (transcendence-style) argument over $\mathbb{Q}(\sqrt d,\sqrt2)$. It is weaker than the 7/8 half-plane, which already gives $1-\beta\ge 1/8$, so it serves as a cross-check.
- **Stated consequences:**
  - $n(p)\le C(\log p)^A$ (Vinogradov's least-nonresidue conjecture), and deterministic polynomial-time square roots mod $p$;
  - an effective bound $\pi(x;q,a)-\mathrm{li}(x)/\varphi(q)\ll x^{11/12}\log x$, uniform in $q\le x$;
  - an effective bound $h(D)\gg\sqrt{|D|}/\log\log|D|$;
  - completeness of Euler's 65 idoneal numbers.
- **Formal status as documented by OpenAI (lean/docs/003.md):** the 7/8 bounds for $\zeta$, for Dirichlet L-functions and for Hecke L-functions over $\mathbb{Q}(\sqrt{-3})$, and the Siegel gap, are formalized. "The paper's later applications are not included."

**Consequences for $\zeta$ that we can state at once.** All of these are standard deductions from a zero-free half-plane; they are PROPOSED here, not separately reviewed.

- $M(x)=\sum_{n\le x}\mu(n)\ll_\varepsilon x^{7/8+\varepsilon}$;
- $\psi(x)=x+O(x^{7/8}\log^2x)$;
- $1/\zeta(s)\ll_\varepsilon |t|^\varepsilon$ on $\Re s\ge 7/8+\delta$;
- $\Theta:=\sup\Re\rho\le 7/8$.

## 2. How the proof works

### 2.1 The 11/12 route (October 5 paper)

This is the cleanest version of the mechanism.

1. **Reduction to a Möbius sum.** Fix a finite-order Hecke character $\nu$ of $K=\mathbb{Q}(\omega)$ and a smooth $W$. Put
   $A_1(D)=\sum_{\mathfrak n}\mu(\mathfrak n)\nu(\mathfrak n)W(N\mathfrak n/D)$, with $\mathfrak n$ prime to $6\,\mathrm{cond}(\nu)$.
   - If $A_1(D)\ll D^{\sigma_0+\varepsilon}$ for every $W$, then $L_K(s,\nu)\ne0$ on $\Re s>\sigma_0$.
   - Proof: take $W(y)=y^{-\rho}\phi(y)$. Then $\int A_1(D)D^{-s}\,dD/D=\widehat W(s)/L^S_K(s,\nu)$ is holomorphic past $\rho$, but $\widehat W(\rho)=\int\phi\,dy/y>0$, a contradiction.
   - This is a fixed-Mellin-detector argument of exactly the type used in our `mellin_landau` packet.
2. **Family embedding.** Insert the sextic residue symbol: $A_u(D)=\sum\mu(\mathfrak n)\nu(\mathfrak n)(u/\mathfrak n)_6W(N\mathfrak n/D)$.
   - For primes $p$ of norm about $Y$, $A_{p^6}(D)=A_1(D)+O(D/Y)$. These sixth-power rows are copies of the principal member.
3. **The key mean square (Prop. 3.1).** $\sum_{0<N u\le H}|A_u(D)|^2\ll D^{1+\varepsilon}H$ with $H=D^{1+\vartheta}$.
   - The paper then takes $Y=H^{1/6}$, so the $\asymp Y/\log Y$ copies give $|A_1|^2\ll D^{2+\vartheta}/Y$. That yields $A_1\ll D^{11/12+\varepsilon}$.
4. **Why the mean square holds for $\mu$ and fails for generic coefficients.**
   - For generic coefficients the sixth-power rows violate any large sieve. For example, with $a_n\equiv1$ there are $\asymp H^{1/6}$ principal rows of size $D$.
   - The proof instead uses an arithmetic identity specific to $\mu$ over $\mathbb{Z}[\omega]$. For squarefree primary $n$,
     $$\gamma_2(n)^3=\mu(n)\,\frac{n}{|n|},\qquad \mu(n)\gamma_{-1}(n)=\chi_n(-1)G(n)^{-1}\overline{\alpha(n)}\gamma_2(n),$$
     where $\gamma_j$ is the normalized Gauss sum of $\chi_n^j$ and $G$ is a fixed ray-class factor.
   - In other words, **the Möbius function is the cube of the normalized cubic Gauss sum, up to the angle $n/|n|$.**
   - Poisson summation in $u$ produces $\gamma_{-1}(n)$. The identity turns $\mu(n)\gamma_{-1}(n)$ into $\gamma_2(n)$, which by Patterson's formula is a Fourier coefficient of Kubota's cubic theta function.
5. **Analysis of the dual.**
   - The dual sum is a twisted sum of theta coefficients. Theta automorphy (Patterson; the Dunn–Radziwiłł cusp expansions) converts the twist $\chi_h^{-1}\chi_h^{-2}=\chi_h^3$ into a **quadratic** character.
   - The Heath-Brown / Goldmakher–Louvel quadratic large sieve then applies, avoiding the $(KD)^{2/3}$ loss of general higher-order large sieves.
   - Cube factors $nb^3$ are removed by Möbius inversion, and a recursive descent (two Poisson steps, $\mathcal H'/X'$ fixed) closes the estimate.

**Extraction barrier of this route.** With only an $L^2$ bound of large-sieve shape $D(D+H)$, the principal-row amplifier gives $|A_1|^2\lesssim D(D+H)/H^{a}$. Here $a$ is the density exponent of principal rows ($a=1/6$ for sixth powers), and the bound is optimal at $H\asymp D$. So $\sigma_0=1-a/2=11/12$. Higher family moments at their natural lengths give the same exponent. **Route 2.1 cannot go below 11/12 without new information.**

### 2.2 The 7/8 route (September 30 paper)

1. **A family supremum.** Let $\beta_*$ be the supremum of real parts of zeros over **all** primitive finite-order Hecke characters of $F$.
   - Proposition 2.1 ("continuation from a common signal"): suppose a probe $J_\eta$ satisfies $|J_\eta|\ll Z^{C(\sigma_0)+\omega}$ and $|J_\eta-f_\eta|\ll Z^{C(\beta_*)-\sigma}$, where $f_\eta$ is a Mellin integral of $1/L_F^S(s,\eta)$ and $\omega,\sigma$ do not depend on $\eta$.
   - Then $\beta_*\le\sigma_0$.
2. **Part I (11/12 again).** The probe is a completed cubic-theta sum averaged against sextic characters.
   - Reflection plus an additive large sieve bound it directly by $Z^{1/4+\varepsilon}$.
   - Poisson summation writes it as a principal Mellin signal containing $1/L_F(s,\eta)$, plus rows $u a^6$ with $u$ sixth-power-free. Those rows are Hecke twists of the target.
   - A **zero detector** turns each row whose twisted L-function has a zero above a floor into a large Möbius polynomial and a large plain polynomial. The sextic large sieve (Lemma 9.1, Prop. 9.2) counts such rows, with exponent $R(\delta)=\min\{1,\max(1-\delta/2,\ 4/3-\delta)\}$, where $4/3$ comes from the Blomer–Goldmakher–Louvel $(KD)^{2/3}$ term.
3. **Part II (7/8) is a bootstrap.**
   - It feeds $\kappa=2\beta_*-1\le5/6$ from Part I back in. It adds a compensated probe (selected prime slots cancel an unwanted Euler factor), uses asymmetric scales $l_x=17/48$, $l_y=23/48$, $h=13/16$, $\ell=1/6$, and adds two new moment inductions:
     - a marked inverse moment (Lemma 17.1);
     - a fourth moment with short prime factors (Lemma 18.1), stated only for $\kappa\in[3/4,1]$.
   - The final exponent certificate (Lemma 20.2, "compensated endpoint certificate") has margin $-E_*\ge 49/440640$. So **7/8 is where this exact geometry runs out, not a proved barrier of the method.**

## 3. What we checked

**Pivotal identity (EMPIRICAL, `scripts/gauss_identity_check.py`).** All five identities of the paper's Lemma 4.1 (October 5 paper) hold numerically:

- $\gamma_2^3=\mu\alpha$;
- $\gamma_1\gamma_2=\mu\alpha G$;
- $\gamma_1\gamma_{-1}=\chi_n(-1)$;
- the Möbius conversion identity;
- $|G|=1$.

They were checked on 77 primary primes of norm ≤ 400 (split and inert, excluding the primes above 2 and 3) and on 126 squarefree composites. The maximum error was $1.2\cdot10^{-13}$. This is floating reconnaissance, not a certificate. The prime case of the cube identity is classical (Gauss–Jacobi with $J(\chi_p^2,\chi_p^2)=-p$).

**Family mean square (EMPIRICAL, `scripts/family_mean_square.py`).** Rows are all nonzero $u\in\mathbb{Z}[\omega]$ with $Nu\le H=D^{1.1}$. Columns are squarefree primary $n$ with $D<Nn<2D$, prime to 6, with a fixed smooth bump and $\nu=1$.

| $D$ | rows | $\sum\lvert A_u\rvert^2/(DH)$ for $\mu$ | for $a_n\equiv1$ | principal-row share, $\mu$ / $1$ | $\lvert A_1\rvert$, $\mu$ / $1$ |
|---:|---:|---:|---:|---:|---:|
| 200 | 1236 | 0.0622 | 0.0618 | 0.002 / 0.035 | 2.6 / 12.0 |
| 400 | 2646 | 0.0623 | 0.0630 | 0.001 / 0.034 | 3.6 / 25.0 |
| 800 | 5646 | 0.0615 | 0.0652 | 0.000 / 0.060 | 1.1 / 49.5 |
| 1600 | 12120 | 0.0636 | 0.0648 | 0.000 / 0.058 | 1.5 / 100.4 |
| 3200 | 26016 | 0.0638 | 0.0680 | 0.000 / 0.077 | 1.6 / 200.3 |

The normalized mean square for $\mu$ is flat, as Prop. 3.1 predicts. The constant-coefficient control shows the principal rows taking a growing share, which is the failure mode of generic coefficients. At these sizes the predicted $D^{1/12}$ separation is too small to be decisive. This is consistent with the claim and proves nothing.

**Part II endpoint certificate (EXACT_RATIONAL grid, `scripts/endpoint_certificate_replay.py`).** Lemma 20.2 of the 7/8 paper claims $-E_*\ge 49/440640\approx1.11\cdot10^{-4}$ on $0\le\delta\le5/6$, $0\le x\le1/2$. We searched a $401\times401$ exact-rational grid and then refined locally. The minimum is $-E_*\approx2.28\cdot10^{-4}$, at $\delta\approx0.387$, $x=1/2$ (the boundary $x=1/2$ binds). This is consistent with the lemma. A grid search is not a proof; an interval or branch-and-bound replay is task 2 below. It confirms that 7/8 sits at the edge of this geometry.

**Lean (source audit only; not execution evidence).** The comparator statements carry no hypotheses and use Mathlib's `riemannZeta` and `DirichletCharacter.LFunction`. The comparator permits only `propext`, `Quot.sound` and `Classical.choice`. A whole-word grep of the 2,926-file proof tree finds no `sorry`, `admit`, `axiom`, `native_decide`, `extern`, `unsafe` or `opaque`. We did not build it or run the comparator. Details are in [LEAN_AUDIT.md](LEAN_AUDIT.md).

## 4. Relation to this repository

The repository's RH-facing machinery consists of fixed smoothed Möbius detectors whose **subpower** ($\theta=0$) negative mass implies RH via Landau/Mellin. Examples are M4/M7, `API.MELLIN.SUBPOWER_NEGATIVE_MASS`, the critical SHARP power $m=1$, and the 5:3 scalar. OpenAI's Proposition 2.1 is the same kind of statement, at $\theta=3/8$ and for a family.

**Direct quantitative plug-ins.** These are PROPOSED deductions; each needs a short written proof before review.

| Repository object | What 7/8 gives unconditionally | What RH needs |
|---|---|---|
| Fixed Mellin detector $F$ with continuation through $1/\zeta(s+\tfrac12)$ (M4/M7) | $F(x)\ll x^{3/8+\varepsilon}$ off its explicit main terms; negative mass $N_F(Y)\ll Y^{3/8+\varepsilon}$ | $Y^{\varepsilon}$ |
| SHARP $\mathfrak h^{[1]}$ (Mellin $\frac{(1-67^{-s-1/2})(s+3/2)}{s(s-1/2)\zeta(s+1/2)}$) | $\mathfrak h^{[1]}(x)=c_0+O(x^{3/8+\varepsilon})$ with $c_0=-3(1-67^{-1/2})/\zeta(1/2)>0$ | positivity for all $x$ (OPEN.ARITH.CV) |
| Wavelet energy abscissa $=\Theta+\tfrac12$ (VERIFIED_WITH_FIXES) | abscissa $\le 11/8$ | $1$ |
| T-9501 $\mathcal E(x)$ (PROPOSED) | $O(x^{-9/8+\varepsilon})$ | $O(x^{-3/2+\varepsilon})$ |
| Vinogradov–Korobov import sites (safe-disc annulus T-91004, Dickman corridor, causal line-one bound $e^{-c\sqrt{\log X}}$, R30) | power savings in place of $\exp(-c(\log X)^{\alpha})$ | not applicable; these are sharpened inputs |

**The principal-member obstruction.** REFUTATIONS §5 records that nonprincipal family control can vanish while the principal component is large (R-108450 / B-020). The exploratory Dirichlet-family programme (#736) stopped at a quadratic-residue Gram and the PRIMCAR ⇒ PRIMLS gate. OpenAI's construction resolves that individualization problem in one concrete setting:

- **Family estimate:** the sextic family over $\mathbb{Q}(\sqrt{-3})$.
- **Individualization mechanism:** the sixth-power rows, or the $\beta_*$ bootstrap.
- **Principal-member cost:** density $H^{-5/6}$, i.e. the extraction exponent $1-a/2$.
- **What makes it work:** the coefficient is $\mu$ itself, through $\mu=\bar\alpha\gamma_2^3$. It is not a generic source, so R-108450 is not contradicted.

**What does not move.**

- The Robin canonical tail is RH-equivalent; a half-plane only bounds the size of a hypothetical violation.
- Fixed-$P_{61}$ contains no zeta zeros.
- The Pick order-4 positivity, the Weil floor and every other $\theta=0$ cut remain open.
- The repository has no Landau–Siegel, cubic-Gauss-sum or metaplectic material; this is all new territory here.

## 5. Proposed programme (ranked)

1. **Import and replay (weeks).**
   - Record 003 as an external comparison (precedent: RESULTS_INDEX "External work"), pinned at `adc7f124`.
   - Run the OpenAI `lake build` and the comparator checks independently, and record the axiom report.
   - Add a $\theta$-indexed consumer, "zero-free $\Re s>\tfrac12+\theta$ ⇔ negative mass $\ll Y^{\theta+\varepsilon}$", to M4/M7 and the Lean `FixedDetectorConsumer`. Then every OPEN_SUFFICIENT/OPEN_RH_EQUIVALENT row gets a measured distance to RH ($3/8$), and further progress on the half-plane flows automatically into the repository.
2. **Exponent ledger for Part II (EXACT_RATIONAL).**
   - Transcribe the affine constraint system of Part II: geometry, row counts $R(\delta)$, $D_x$, $P_x$, capacities, and the regions of Lemmas 17.1 and 18.1.
   - Re-prove the $49/440640$ endpoint certificate with exact rational interval arithmetic.
   - Then:
     - re-optimize the geometry;
     - try a **Part III** iteration with $\kappa<3/4$, which needs Lemma 18.1 below $3/4$;
     - run a sensitivity table showing the $\sigma_0$ obtained if (a) the sextic large sieve loses its $(KD)^{2/3}$ term, (b) Lemma 18.1's region widens, or (c) a density hypothesis holds for the sextic family.
   - This is the analogue of an exponent database for this argument, and it says which input to attack.
3. **Barrier theorem (for REFUTATIONS if negative).** Determine the fixed point of the $\beta_*$ bootstrap under *optimal conjectural* inputs (sharp sextic large sieve, sharp family moments).
   - If it stays above 1/2, that is a clean no-go for this route.
   - If it reaches 1/2, it is a roadmap that reduces RH to explicit family estimates.
4. **Input upgrades.** OpenAI family 023 (unconditional Patterson first moment for cubic Gauss sums, Lean) proves structured-prime Gram and dispersion bounds for exactly the "rows with prime factors" in 003. These are the most plausible source of better row counts. Large-values (Huxley/Guth–Maynard-type) estimates for the sextic family are a second.
5. **Function-field synthetic control.** Run the whole 003 pipeline over $\mathbb{F}_q[T]$ with $q\equiv1\pmod 6$, where RH holds and everything is computable. Measure the true size of each inequality in the chain to locate the lossy steps. The repository's function-field components (B-026) provide the setting; this is a SYNTHETIC_CONTROL, not a transfer.
6. **Family-embed our own detectors (the #736 continuation).** Recast a fixed detector (the 5:3 scalar, rows $f_j$ or SHARP) over $\mathbb{Q}(\sqrt{-3})$ with the sextic twist. Ask whether its dual is again a cubic-theta object, and whether the detector smoothing improves the extraction exponent $1-a/2$.
7. **Breadth (lower priority for RH).** OpenAI family 029 already ports 003 Part I to every cyclotomic $F\supseteq\mu_{12}$, with a uniform width of $10^{-6}$. Porting Part II there would give quasi-GRH half-planes for Kummer-field Dedekind zetas.
