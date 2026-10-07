# The OpenAI quasi-Riemann hypothesis release: what is claimed, how, and what it changes here

```text
Status: IMPORTED (external, not reviewed in this repository) + PROPOSED consequences + EMPIRICAL replay
Scope: global (if the import is accepted); every consequence below is conditional on the import
Exact sources or dependencies:
  openai/math @ adc7f1241b42e322a6451854ab7e4b4c146bf78a (2026-10-06)
    preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/   (7/8 paper, 16,677 TeX lines)
    preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/      (11/12 paper, 3,988 lines, human-edited)
    preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/ (773 lines)
    lean/OAI/NumberTheory/DirichletL/** and lean/ComparatorChallenges/{QuasiRiemannHypothesis,
      DirichletSevenEighths,HeckeSevenEighths,SiegelZeros}.{lean,json}
What was actually run: see "Verification performed here" (static Lean audit of the full import
  closure, a local Lean build, and a numerical replay of the arithmetic core over Z[omega])
Smallest remaining gap: independent mathematical review of the analytic chain
  (theta transformation with ray-class twists -> completed mean square -> transfer recursion),
  and a completed comparator run, before anything here is integrated.
```

RH remains unproved. The OpenAI claim is a **fixed zero-free half-plane**, not the critical line.

## 1. The claims

Let $F=\mathbb Q(\sqrt{-3})$, $\mathcal O=\mathbb Z[\omega]$.

* **7/8 theorem (Sept 30 paper, Thm 1.1).** Every finite-order Hecke $L$-function over $F$ has no zero in $\Re s>7/8$. Hence every Dirichlet $L$-function, including $\zeta$, has no zero in $\Re s>7/8$ (principal pole at $s=1$ allowed). Uniform in the character, conductor and height.
* **11/12 theorem (Oct 5 paper, Thm 1.1).** The same with $11/12$; a shorter, cleaner, human-edited proof. It is also Part I of the 7/8 paper.
* **Landau–Siegel (Oct 1 paper).** $(1-\beta)\log q\ge c$ for every real zero of every primitive real character, $c>0$ absolute (non-explicit). Trivially implied by the 7/8 theorem, but proved there by an unrelated interpolation-determinant method.
* Stated corollaries: $\pi(x;q,a)=\mathrm{li}(x)/\varphi(q)+O(x^{11/12}\log x)$ uniformly in $q\le x$ (effective; $7/8$ with the stronger theorem); least quadratic nonresidue $n(p)\le C(\log p)^A$ (Vinogradov's conjecture); deterministic polynomial-time square roots mod $p$ and Miller's test; effective $h(D)\gg\sqrt{|D|}/\log\log|D|$; completeness of Euler's 65 idoneal numbers.

### Formal status claimed by OpenAI

Comparator challenge `ComparatorChallenges/QuasiRiemannHypothesis.lean`:

```lean
theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0
```

against Mathlib's own `riemannZeta`, permitted axioms `propext`, `Quot.sound`, `Classical.choice`. Companion challenges cover all Dirichlet characters (`DirichletCharacter.LFunction`), finite-order Hecke characters over $F$, and the Siegel gap. The 11/12 paper's separate proof is *not* the formalized one; the Lean development follows the 7/8 paper.

## 2. How the 11/12 proof works (the clean version)

**Step 1 (Möbius sums).** For a finite-order Hecke character $\nu$ and smooth $W$, put
$A_1(D)=\sum_{\mathfrak n}\mu(\mathfrak n)\nu(\mathfrak n)W(N\mathfrak n/D)$.
A bound $A_1(D)\ll D^{\theta+\varepsilon}$ for all smooth $W$ gives holomorphy of $1/L_F(s,\nu)$ on $\Re s>\theta$ by a Mellin transform (paper2 §3). Dirichlet $L$-functions follow from $L_F(s,\chi\circ N)=L(s,\chi)L(s,\chi\chi_{-3})$.

**Step 2 (embed in a family with many copies of the principal member).** Twist by sextic residue symbols $\chi_n(u)=(u/n)_6$:
$$A_u(D)=\sum_{n}\mu(n)\nu(n)\chi_n(u)W(Nn/D).$$
Key proposition (paper2 Prop. `thm:ms`): for $H=D^{1+\vartheta}$,
$$\sum_{0<N u\le H}|A_u(D)|^2\ll_\varepsilon D^{1+\varepsilon}H\qquad(\text{square-root cancellation on average}).$$
Because $\chi_n(p^6)=\mathbf 1_{p\nmid n}$, every row $u=p^6$ is a copy of the principal member: $A_{p^6}(D)=A_1(D)+O(D/Y)$ for $Np\sim Y$. There are $\asymp Y/\log Y$ such rows with $Y=H^{1/6}$, so
$$|A_1(D)|^2\ll D^{1+\varepsilon}H^{5/6}+D^2H^{-1/3}\;\Longrightarrow\;A_1(D)\ll D^{11/12+5\vartheta/12+\varepsilon}.$$

**Step 3 (Poisson in the row, Möbius disappears).** Poisson summation in $u$ produces sextic Gauss sums $\gamma_{-1}(n)$. The arithmetic miracle is
$$\mu(n)\gamma_{-1}(n)=\chi_n(-1)G(n)^{-1}\overline{\alpha(n)}\gamma_2(n),\qquad \alpha(n)=n/|n|,$$
with $G$ a fixed ray-class factor. For a prime, the sign $\mu(p)=-1$ is exactly the classical cubic Jacobi-sum evaluation $J(\chi_p^2,\chi_p^2)=-p$ for primary $p$, i.e. $\gamma_2(p)^3=-\alpha(p)$. So **Möbius times a sextic Gauss sum is a cubic Gauss sum**, up to a Grössencharacter and a ray-class phase.

**Step 4 (automorphy).** Cubic Gauss sums at squarefree indices are Fourier coefficients of Kubota's cubic theta function (Patterson). After completing the sum with cube factors $nb^3$, the theta transformation (Dunn–Radziwiłł form, extended to fixed ray-class twists) turns the dual sum into sums twisted by the **quadratic** character $\chi_h^3$. Goldmakher–Louvel's quadratic large sieve over $F$ then gives the completed mean square $\ll(\mathcal H+\mathcal H^2/X)$, avoiding the $(MN)^{2/3}$ loss of the general higher-order large sieve.

**Step 5 (remove the cube factors).** Möbius inversion over the cube variable, with a recursive "transfer estimate" (two more Poisson summations that shrink both scales by $N(b)^3$ at a fixed ratio), closes the induction in $O_\vartheta(1)$ steps (Heath-Brown's admissible-exponent method).

### The 7/8 upgrade

The 7/8 paper reorganizes the argument as a bootstrap over the **whole family** of primitive finite-order Hecke characters of $F$. Let $\beta_*$ be the supremum of real parts of their zeros. A probe $J_\eta(Z)$ is bounded directly through theta reflection and large sieves (the "low" side). The same probe, after Poisson summation, equals a principal Mellin integral of $Z^{C(s)}H_\eta(s)/L_F(s,\eta)$ plus nonprincipal rows (the "high" side). Each row is itself a twisted Hecke $L$-function in the same family, so its zeros are $\le\beta_*$ by definition. A zero detector converts every row with a zero near $\beta_*$ into large Dirichlet polynomials, and moment bounds count those rows. If $\beta_*>\sigma_0$, the two bounds continue $1/L$ uniformly past $\beta_*$, which is a contradiction (Prop. `lem:continuation-criterion`). Part II adds prime "compensation" slots, asymmetric scales ($h=13/16$, $\ell=1/6$, $l_x=17/48$, $l_y=23/48$, $C(s)=s-11/16$), an inverse-moment induction and a plain fourth-moment induction.

## 3. Why the method stops short of RH: a leverage–exponent law

Abstracting Step 2: suppose the rows $u$ with $Nu\le H$ satisfy a square-root mean square $\sum_u|A_u|^2\ll D^{1+\varepsilon}(H+D)$. Suppose also that a subset of $\gg H^{1-c}$ rows are principal copies ($A_u\approx A_1$). Then
$$|A_1|^2\ll\frac{D(H+D)}{H^{1-c}}\quad\Longrightarrow\quad\text{zero-free for }\Re s>\frac{1+c}{2}\ (H\asymp D).$$
Sixth powers give $c=5/6$, hence $11/12$. **RH would need subpower principal leverage ($c=0$).** That is exactly the gate this repository names `PLEV106000` in the Dirichlet-family programme (#736).

A Dirichlet family modulo $q$ has the principal member once among $\varphi(q)$ rows ($c=1$, no saving). This matches the binding barrier recorded there: "family dimension … gives no principal saving." OpenAI's choice of a residue-symbol family **indexed by the numerator** makes the principal pattern recur on all sixth powers. They pay a *power* leverage cost, and that is why the result is quasi-RH rather than RH.

The 7/8 bootstrap beats the naive law ($c_{\rm eff}=3/4$) through **propagation**. Rows whose own $L$-function has a zero near $\beta_*$ also carry the signal. This is precisely the architecture of programme #740: "one bad zero → principal defect → propagated family statistic → unconditional family bound → contradiction."

## 4. Relation to this repository

| Repository object | Relation to the OpenAI work |
|---|---|
| OPEN_CUTS §5 / PROGRAMMES §5, principal-member extraction; #736 mandatory ledger | OpenAI fills the ledger: FAMILY ESTIMATE = Prop. `thm:ms`; INDIVIDUALIZATION = sixth-power rows; PRINCIPAL-MEMBER COST = $H^{5/6}$ (power); CONCLUSION = quasi-GRH, not RH |
| #740 off-line-zero propagation | 7/8 paper = a working propagation theorem (zero detector + row counts + continuation criterion), with the rightmost zero of the *whole closed family* as the bootstrap variable, so it is not circular |
| REFUTATIONS §5 "nonprincipal control can miss the principal member" | Consistent. OpenAI's mean square *includes* the principal-copy rows and is proved from the Möbius-specific Gauss-sum duality, not from a nonprincipal estimate |
| `OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS`, `OPEN.DIRECTMAIN.TAYLOR_CRITICAL`, `OPEN.ARITH.CV` (all "subpower" gates) | Each becomes an exponent-reduction problem with known starting exponent $3/8=\theta-1/2$ (§5) |
| D-final R15 (reciprocal growth on $\Re w\ge a>\Theta$, no bound on $\Theta$ assumed) | Becomes unconditional for every $a>7/8$ |
| Wavelet energy abscissa $=\Theta+1/2$; tent energy exponent $2\Theta-1$ (reviews A-115/A-117) | Unconditionally $\le 11/8$ and $\le 3/4$. FINAL_AUDIT's "VK saving stays $X^{1-o(1)}$, not a fixed power improvement" now gets the fixed power |
| OPEN_CUTS §6 causal Euler products (theorem only on $\Re s=1$) | Half-plane target becomes available on compact subsets of $\Re s>7/8$; the strip $(1/2,7/8]$ remains |
| Dickman/Bellman corridor "on standard VK/de Bruijn input"; Catalan VK safe disc | VK inputs can be replaced by power-saving PNT inputs; corridor widths need recomputation |
| T-9503 totient criterion ($\vartheta_1=\Theta_\zeta$) | $P(x)=4/\pi^2+O(x^{-9/8+\varepsilon})$ unconditionally; RH needs $x^{-3/2+\varepsilon}$ |
| L-91027 (inner/Hermite–Biehler scattering function if no zero in $\Re s>1/2+a$) | Unconditional for $a\ge3/8$ |
| Robin, SHARP $m=1$, seven-point certificate | No qualitative change: any off-line zero still gives Robin violations, and the SHARP sign needs exponent 0 |
| Formal track (`formal/`, comparator workflow) | OpenAI's Lean library is Apache-2.0 and uses the same comparator discipline. Reuse needs a toolchain bump (repo `v4.33.0-rc2` → `v4.34.1`) |

Nothing in this repository concerns $\mathbb Q(\sqrt{-3})$, cubic/sextic residue symbols, metaplectic theta functions or large sieves. The tools that drive the OpenAI proof are new here.

## 5. Immediate consequences to record (PROPOSED, conditional on the import)

Write $\Theta\le7/8$, so $\delta:=\Theta-\frac12\le\frac38$.

1. **Mertens/Möbius.** $\sum_{n\le x}\mu(n)\ll x^{7/8+\varepsilon}$, and the same for $\beta(n)=\mu(n)-\mathbf 1_{67\mid n}\mu(n/67)$ (Perron + R15).
2. **Fixed Mellin detectors.** For any fixed detector with $\mathcal MF(s)=\widehat K(s)/\zeta(s+\frac12)$ and $\widehat K$ decaying faster than $|t|^{-1-\eta}$ on vertical lines, $F(x)\ll x^{3/8+\varepsilon}$, hence $N_F(Y)\ll Y^{3/8+\varepsilon}$. The open RH gate is the same bound with exponent 0. Verify kernel decay separately for rows 2, 3 and the 5:3 scalar.
3. **Critical Taylor detector.** Using the R17 splitting, $C_m(X)\ll X^{3/8+\varepsilon}$ and $N(Y)\ll Y^{3/8+\varepsilon}$.
4. **Conductor-uniform family inputs.** $1/L(s,\chi)$ is holomorphic on $\Re s>7/8$ for every Dirichlet $\chi$, uniformly in $q$. This removes the exceptional-zero caveat from every Dirichlet-family statement at the $\delta=3/8$ level. It does not help at $\delta=0$.
5. **A priori finiteness for absorption/bootstrap arguments.** $X^{-\sigma}$-weighted negative masses are finite for $\sigma>3/8$. Continuity-in-$\sigma$ arguments (reviews D CLAIMS 69, conjunctive packet) therefore get a starting point.

Each item should become its own claim with a new ID, an `IMPORTED` dependency pinned to the SHA above, and the usual review.

## 6. How to push this forward

Ranked by payoff and feasibility. Tier 0 and Tier 1 are concrete and mostly routine. Tier 2 is the real research frontier.

**Tier 0: verify before building on it (days).**
1. Finish the Lean build and run the comparator proper (`lake env comparator ComparatorChallenges/QuasiRiemannHypothesis.json`, plus the Dirichlet, Hecke and Siegel configs). §7 records the local build state.
2. Do a theorem-sized review of the 11/12 paper (3,988 lines) in the order of §8. It is the shortest complete path, and Part I of the 7/8 paper is the same mechanism.
3. Register the import (`IMPORTED`, pinned SHA, exact statements as in §1), following the precedent of the earlier `openai/PrimeGaps186` imports.

**Tier 1: cash in the half-plane across this repository (weeks).**
4. Turn §5 into claims, one per open "subpower" gate: Mertens, fixed Mellin detectors, critical Taylor, wavelet and tent abscissae, totient criterion, L-91027, causal Euler on $\Re s>7/8$, VK→power replacements in Dickman/Bellman and the Catalan safe disc. The repository's RH frontier then becomes a single, uniform **exponent ledger**: every gate is currently known at exponent $3/8$ and needed at exponent $0$. Progress on any gate becomes measurable as an exponent.
5. Do the same formally. Depend on OpenAI's Apache-2.0 Lean library (after the toolchain bump) and prove, e.g., `∑_{n≤x} μ n = O(x^{7/8+ε})` and the $3/8$ negative-mass bound for a fixed detector. These would be the formal track's first unconditional, non-trivial analytic theorems about the actual zeta source. They would also exercise the "actual-Xi source" repair contract against a mature Mathlib-native development.

**Tier 2: lower the exponent (months; this is where a dramatic advance would come from).**
6. *Leverage.* By §3, any family with a provable square-root mean square and principal-copy density $H^{-c}$ gives $\Re s>(1+c)/2$. Two routes:
   * Search for families with smaller $c$ in which Möbius is still Fourier-dual to automorphic coefficients. The sextic/cubic case is the smallest order in which the Davenport–Hasse relation produces the sign $\mu(p)=-1$; quartic characters over $\mathbb Q(i)$ give only a trivial identity.
   * Or improve propagation, so that more rows carry the bad-zero signal (the 7/8 route, $c_{\rm eff}=3/4$).
7. *Swap in the better family estimate.* The 7/8 paper counts detector rows with a general sextic large sieve, which carries a $(KD)^{2/3}$ term. The 11/12 paper proves a square-root mean square for the specific Möbius family, avoiding that term. A worked computation of which constraint is binding at 7/8, and what replacing the sieve would give, is the first research task. See the addendum in §6a when it is available.
8. *Repository machinery inside the OpenAI family.* Programmes #736/#740 already contain exact principal/quadratic-root leverage identities (the $(\rho+1)/(\rho-1)$ coefficient, the $\chi\mapsto\chi^2$ temperature map) and fixed detectors with audited non-cancelling multipliers. Transplant them from Dirichlet characters mod $q$ to the sextic residue-symbol family over $\mathbb Z[\omega]$. The cube rows $u=v^3$ (quadratic twists) and square rows $u=v^2$ (cubic twists) are the analogues of the quadratic-root channels found in #736. Each is a candidate for additional leverage beyond the sixth powers.
9. *Atlas (#741).* Add the sextic family and its mean square to the detector atlas. The replay in `numerics/` is a ready pilot: $S/\text{diag}=1.000\pm0.04$ for $D\le10^5$.

What the combination cannot do: none of the repository's one-sided positivity criteria is needed for, or improves, the OpenAI argument as it stands. Its estimates are two-sided mean squares. The main flow of value is OpenAI → repository (Tier 1). The conceptual flow is the reverse: this repository's ledgers (#736, #740) are exactly the right language for analysing and extending the OpenAI method.

## 7. Verification performed here

* **Static audit of the formal proof.** The import closure of `OAI.NumberTheory.DirichletL.Nonvanishing` is 2,924 local modules, 486,490 lines. It was scanned for `sorry`, `axiom`, `native_decide`, `unsafe`, `implemented_by`, `@[extern]`, `ofReduceBool`, `debug.skipKernelTC`, `run_cmd`, `#eval`, `IO.Process`: **no occurrences.** External imports in that closure are Mathlib (400), PrimeNumberTheoremAnd (2) and RellichKondrachov (1).
* **Local build.** Lean `v4.34.1`, Mathlib from cache, pinned dependencies plus OpenAI's shipped `patches/*-lean4341.patch`. Note: `lake exe cache get` without `lake update` does not apply these patches. Without them, one RellichKondrachov file fails to compile and contains a `sorry`; the patched file contains none. At the time of writing, about 4,400 of 7,061 build jobs had completed with no errors after patching. The final result is recorded in the addendum below.
* **Arithmetic core (EMPIRICAL, `numerics/`).** Every identity of paper2 Lemma `lem:arithmetic` holds to about 5e-15 for all 14,120 squarefree primary $n$ prime to 6 with $N(n)\le50{,}000$ (split, inert and composite). Gauss sums are computed directly, not via CRT. Reciprocity $R$ is the stated $\pm1$ bicharacter, and $G$ factors through $(\mathcal O/4)^\times$. A second, separately written implementation (`independent_prime_replay.py`) confirms $\gamma_2(\pi)^3=-\alpha(\pi)$ and $\gamma_1\gamma_2=-\alpha G$ for all 207 primary split primes below 3000.
* **Mean square (EMPIRICAL).** $\sum_{Nu\le H}|A_u(D)|^2$ equals its orthogonal-diagonal prediction to within 4% for $D=100\ldots102{,}400$, $\vartheta\in\{0,0.05,0.1\}$, with no visible log growth. This is a convention and sanity check only. It is **not** evidence for the asymptotic bound, and the analytic steps are untested (see `numerics/RESULTS.md`).

## 8. Referee checklist (where to look first)

1. **paper2 App. `app:fixed-ray`, the cubic theta transformation with fixed ray-class twists.** This is the one genuinely new automorphic input. Check the cusp expansions, the $\chi_h^3$ (quadratic) twist claimed in eq. `intro-quadratic-twist`, and the uniformity of the transformed weights within a ray class (Lemma `lem:reflection-uniformity`).
2. **The Grössencharacter $\overline{\alpha(n)}$ inside theta sums.** The completed sum carries $\overline{\alpha(nb^3)}$, a character of infinite order. Check that the summation formula applies with this angular twist and that the dual weights $V_*^\sharp$ keep their rapid decay.
3. **Transfer recursion (paper2 §`sec:transfer-proof`).** The "enlarged row range" trick ($Y=XL_b/\mathcal H$) and the claim that $\mathcal H'/X'$ stays fixed while both scales contract. Check the common factors and dyadic ranges suppressed in the outline.
4. **Diagonal and zero-frequency terms** in the Poisson comparison (eq. `intro-poisson-comparison`), including rows $u$ sharing factors with $n$ and the sixth-power rows themselves.
5. **7/8 paper only:** the uniformity of margins "independent of the target" in Prop. `prop:parameter-order`; the treatment of rows whose inducing character lies in the finite group generated by the target (Sec. `sec:plain`); and the boundary case $\delta=5/6$.
