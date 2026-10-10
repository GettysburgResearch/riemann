# Sep 30 Section 17: the new Poisson-transform identities, and the small helpers 17.3-17.6

```text
Status: REVIEW (bounded; external, unreviewed manuscript). Follows SEP30_INVMOMENT_REVIEW.md section 4
  (11 identities new relative to Oct 5) and SEP30_EQC_CHECK.md (identity 2, eq. (C)).
  Verdict: all 11 identities VERIFIED at the level stated in section 2 (hand derivation plus exact or
  EMPIRICAL floating-point checks with failing controls). No error was found. Lemma 17.3, Cor 17.4,
  Lemma 17.5 and Lemma 17.6: CORRECT as bounded reviews. The invmoment review called Lemma 17.5
  "[O5] lem:poisson verbatim". A diff does not support that: the displayed formula is identical after a
  notation map, but the statement and proof prose were rewritten and extended. This is not a verdict on
  Lemma 17.1, Lemma 17.2, Prop 19.2 or Theorem 1.1.
Scope: paper.tex Section 17. Proof of Lemma 17.2 from eq. (C) (10279) to the child Cauchy step
  (11380): the cube label and its norm identities (10292-10330, 10641-10655); the t' Moebius extension
  and B_{1,a}(t';y)P_a(y) (10382-10530); the weighted Cauchy (D) and the old-label fibre (10553-10655);
  the second Poisson transform (10669-10913); the new canonical data, slot regrouping, source triples
  and fibres (10913-11380). Helpers: Lemma 17.3 (9366-9484), Cor 17.4 (9486-9550, plus the
  normalized-label paragraph 9552-9580), Lemma 17.5 (9722-9781), Lemma 17.6 (12362-12469).
  The exponent ledgers of these blocks were already checked in SEP30_INVMOMENT_REVIEW.md and are cited,
  not redone.
Exact sources or dependencies:
  [OAI] pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, .../The-Quasi-Riemann-Hypothesis-September-30-2026/
        build/paper.tex, SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
        (re-hashed from git; equal to the scratch copy).
  [O5]  .../The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex at the same ref,
        SHA-256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d (lem:poisson 875-932).
  Reused read-only: reviews/sep30_eqc_check.py (symbol tables, Gauss sums, Gamma/r/R/G ray functions,
        the decomposition and the 8-row table). It is imported, not modified. sep30_invmoment_ledger.py
        was not run again.
  Imported and NOT checked: cubic reciprocity (exercised numerically through eq:signal only);
        Lemma 4.5 (lem:smooth-calculus) and the Fourier-moment bound (inverse-fourier-moment) as used
        in the 9- and 6-coordinate separations; Lemma 14.3 (the terminal input).
What was actually run: reviews/sep30_l17_identities.py (new; SHA-256 60d97dc3a77532c97425d1ed205d250b686d0e4cb0c0d8749e59067b23951587), as
  `nice -n 10 python3 -I sep30_l17_identities.py --out <scratch>/full2.json` (full) and with --quick.
  * Full: 55/55 checks pass in about 39 s. Log SHA-256 8daa93f4...ac30c, JSON 4d909c0a...2cde7,
    both scratch only. Two consecutive full runs printed identical check lines.
  * Quick: 55/55 pass in about 7 s.
  * Development history:
    - Two earlier full runs passed 52/55. Their three failures were R6 controls, then required to break
      in every configuration. The second configuration is insensitive to three dual-only mutations
      (k_new without d_k, theta swapped, f_new without d_2), at K = 2500 and at K = 500 alike.
      The criterion is now "breaks in at least one run", and the per-configuration values are
      reported in section 3.2.
    - No identity check failed in any run.
    - One development bug was mine, not the paper's: the Q2 right side at first omitted the outer
      mu(t') that the paper keeps (10500). With that factor restored, Q2 agrees to 1.4e-15.
    - A nondeterminism in Q2 was fixed: random subsets were drawn over hash-ordered sets.
  Residue symbols, valuations, norms, counts and booleans are exact integer arithmetic. Gauss sums,
  kernels and lattice sums are double precision: EMPIRICAL, not certified. Tolerance 1e-9 (pointwise
  absolute; replay relative).
Smallest remaining gap: inside Lemma 17.2, every arithmetic identity from eq. (C) to the child
  polynomial is now replayed. The smallest unverified step is analytic: the two Fourier separations
  (eq:inverse-first-separated, 10538; eq:inverse-xi-identity, 11209) together with the common-density
  moment bound (eq:inverse-joint-fourier-moments, 11247), which rest on the imported Lemma 4.5. Each was
  read, and its root and kernel exponents were checked, but neither was replayed. Inside Lemma 17.1,
  the initialization transform (11606-12271) has a ledger PASS but no identity replay. Outside
  Section 17, the Lemma 14.3 terminal branch bounds remain the load-bearing unverified input.
```

RH remains unsolved. This note checks arithmetic and combinatorial identities, and four small lemmas, inside the proof of one lemma of an external manuscript that claims a fixed zero-free half-plane Re s > 7/8. The identities are correct as written. That does not establish Lemma 17.2, the 7/8 theorem, or anything about the critical line.

## 1. Verdicts

### 1.1 The 11 new identities (SEP30_INVMOMENT_REVIEW.md §4)

| # | identity (lines) | verdict | evidence |
|---|---|---|---|
| 1 | cube pair (b_1,b_2) in the square; 8-row table; m_1 = u_1u_2R_1 (10146-10180, 10252-10272) | VERIFIED | eqc B1-B3, invmoment B1-B9 (exhaustive); used in Q2 |
| 2 | eq. (C) and the u_1-side identification (10207-10279) | VERIFIED | SEP30_EQC_CHECK.md |
| 3 | cube label: J = sJ_2, q_0 = q/J_2, (inverse-cube-actual), (fixed-cube-count), J in f_new | VERIFIED | Q1 (exact, 3000 configurations); R4 and R6 carry J into f_new |
| 4 | ỹ = hf²E and R̂ − Â_1 − Â_2 + Ê = ŝ − 2ĵ_2 (10331) | VERIFIED | eqc (ỹ); Q1 (exact) |
| 5 | side-dependent P_1 ≠ P_2 and weighted Cauchy (D) (10557) | VERIFIED | T1; hand (§3.3); Q2 has ν_1 ≠ ν_2 with a control |
| 6 | slot priority (9950) and survival of marks as original subcollections | VERIFIED | S1 (exhaustive); marks are split at t' in Q2 and carried on g'v'n in R6 |
| 7 | fixed punctures γ = (q_0,t',r_g), #Γ_σ ≤ Z^{C_c+11η/2}, normalized label measure (11336-11365) | VERIFIED (hand) | §3.6; the ball exponents come from the invmoment ledger |
| 8 | old-label fibre (10573) and new fibre D_K(f)C_K(γ) (11299), replacing the sign-sum collapse | VERIFIED | U1 (exact); U2 brute force at K_slot = 0; hand count of the exponents 9+4K and 5+2K |
| 9 | outer masks 𝓑_1, 𝓑_2 and raw-tail discards (10127) | VERIFIED (hand + EMPIRICAL) | P3 (Gaussian); the containment is the invmoment ledger (H_use, M_ch) |
| 10 | second principal exponent F − B − j (10755) | VERIFIED | invmoment D-checks; re-derived by hand in §3.5 |
| 11 | common log-Fourier densities in 9 and 6 coordinates (10444, 11135) | PARTIAL | root/kernel exponent identities checked (invmoment C-checks; §3.4 for the second); the analytic density requirement was read, not replayed |

### 1.2 The helpers

| lemma | verdict | note |
|---|---|---|
| 17.3 finite seminorm propagation (9366-9484) | CORRECT | standard backward induction on a finite DAG; the index bookkeeping is right (§4.1) |
| Cor 17.4 indexed propagation (9486-9550) | CORRECT | needs the child-profile bounds to be uniform in γ, which is implicit (§4.2) |
| 17.5 masked primitive Poisson (9722-9781) | CORRECT; "verbatim" refuted at text level | same displayed formula as [O5] eq:poisson after a notation map (P4); replayed (P1, P2) |
| 17.6 sixth-power amplification (12362-12469) | CORRECT (given eq:raw-moment and Lemma 4.5) | column identity replayed (V1); injectivity exact (V2) |

## 2. What the script checks

`reviews/sep30_l17_identities.py`, full run. Each row is one or more PASS lines. "CONTROL" lines must break the identity, and they do.

| part | claim (lines) | size | result |
|---|---|---|---|
| P1 | eq:masked-poisson, direct lattice sum against its right side | 120 (ψ,m,R), 89 nonzero; principal m = 1 and R sharing primes with m included | rel err ≤ 2.3e-14; controls ψ(h) unconjugated and ψ(d) dropped break it |
| P2 | Σ_x ψ(x)e(hx/m) = √q_m γ conj ψ(h) for all h mod m, nonunits included; |γ| = 1 | 987 (ψ,h) | ≤ 1.4e-13 |
| P3 | A Σ_{h≠0}|𝓕Φ(Aq_h)| ≪ 1; raw tail (10127) for A = 2, 3 | A ∈ [1e-3,1e3]; a ∈ [1e-2,1e2], Y ∈ [1,30] | sup 0.999; tail ratio ≤ 0.014 (EMPIRICAL, Gaussian only) |
| P4 | eq:masked-poisson = [O5] eq:poisson after the notation map | strings from git | equal |
| Q1 | q_0 integral, J_2 \| q, J squarefree; (inverse-cube-actual) ×2; R̂−Â_1−Â_2+Ê = ŝ−2ĵ_2; R̂ = ŝ+r̂_diff; (fixed-cube-count); t_p = 0 ⇒ p ∈ J_2 ∪ supp q_0; (retained-cube-label) | 3000 random (b_1,b_2,𝔄_1,𝔄_2), valuations ≤ 5; 500 (config,u) | exact, 0 failures; control q_0 := q breaks it |
| Q2 | t' Möbius extension and B_{1,a}(t';y)P_a(y) (10382-10497) as a formal-sum identity (§3.1) | 3 cube configurations, 143 squarefree u, 11121 terms | rel err ≤ 1.4e-15; 4 controls break it; 1 predicted insensitive |
| R1 | eq:second-masked-data: the g' factor is exactly the mask | 3000 | exact |
| R2 | μ(z_1)μ(z_2)γ(χ̄_{z_1}χ_{z_2}; z_1z_2) = a_0(z_1) conj a_0(z_2) G([z_2][z_1]^{-1}); 𝔊(a,b) = G(ba^{-1}); 𝔊(v'a,v'b) = 𝔊(a,b); the γ_{−1} identities | 408 coprime pairs (direct Gauss sums mod z_1z_2); all 12³ classes | ≤ 2.0e-15; 3 controls break it |
| R3 | a_0(v'n) = a_0(v')a_0(n)χ_n(v')⁴; eq:inverse-second-extraction with all factors | 247 + 505 | ≤ 3.4e-15; control breaks it |
| R4 | eq:inverse-moving-characters, complete zero-extended form | 4000 (nonunits, overlaps) | exact; controls without d_2 in f_new, or without d_k in k_new, break it |
| R5 | ray Fourier step: 12 distinct characters of (𝒪/4)^×; G([n_2][n_1]^{-1}) = Σ Ĝ(ϑ) conj ϑ(n_1)ϑ(n_2) | 144 pairs | 1.2e-15; Σ|Ĝ| = 2 |
| R6 | **end-to-end replay of the second Poisson transform written in child form** (§3.2) | 2 configurations × {radial, shifted}; columns of up to 4 primes, norms in (300,720); 790 and 2634 child terms | rel err ≤ 8.7e-16; 6 controls break it; 1 predicted insensitive (§3.2) |
| S1 | slot priority (9950) is a disjoint partition; the mark expands into (h+1)^{\|I\|} terms with priority masks | 72000 (lists,n,p); 1000 coefficient lists | exact |
| T1 | (D) | 2000 random | max excess −1.8e-14 |
| U1 | #{f squarefree : f²E \| y} ≤ d(y) | 3000 | exact |
| U2 | eq:inverse-new-fibre at K_slot = 0 by brute force (§3.7) | 5,087,327 source tuples, 5488 targets | every fibre ≤ d(f)⁹d(q_0)⁵ (max ratio exactly 1, at the empty target); control without d(q_0)⁵ breaks it |
| V1 | eq:sixth-power-column-identity | 40 (u,a,ε), u sharing primes with a, ν of order 6 | ≤ 1.7e-15; control breaks it |
| V2 | (u,a) ↦ ua⁶ injective | 71280 pairs, exact | 0 collisions |

## 3. Hand derivations and what the replays establish

### 3.1 The t' extension (10382-10497); Q2

Write Coef_a(u) for the side-a coefficient of eq. (C), with ξ taken from the 8-row table. By (retained-cube-label), Coef_a(u) = μν_aρ(u) conj χ_u(y) χ_u(CJ)⁴ χ_u(d_k) 1_{(u,rad q_0)=1} 𝔡_a(u), where y = ỹ.

For squarefree u = t'x with (t',x) = 1:
* every factor is multiplicative in the modulus, so Coef_a(t'x) = B_{1,a}(t';y) · [P_a-coefficient of x] · (mark split);
* the slot priority with the ordered list (…, t'; x) puts the t'-slots outside and leaves 𝔡_{I'}(x);
* the ray function G(u_1u_2^{-1})R(u_1u_2^{-1},P_T) depends only on the class u_1u_2^{-1}, so t' cancels.

Defining the summand for noncoprime (u_1,u_2) by this same formula, Σ_{t'|(u_1,u_2)} μ(t') recovers the coprime support exactly.

The total weight on t' is μ(t')·B_{1,1} conj B_{1,2}, which is μ(t')³ = μ(t'). This is the paper's "one additional μ(t')" (10500).

Q2 checks the identity with the paper's own pieces:
* the left side is a sum over all coprime (u_1,u_2), drawn from 143 squarefree u of norm ≤ 2600, with ν_1 ≠ ν_2, a puncture, a slot list and a kernel depending on the formal product norm and class;
* the right side is Σ_{t'} μ(t') B_{1,1} conj B_{1,2} Σ_{x_1,x_2} with marks split at t';
* x ranges over **all** squarefree x, so the zero extensions alone must supply (x, t' rad q_0 CJ) = 1.

The identity holds to 1.4e-15 in three cube configurations, including R_1 = ∅ and a valuation-3 cube. Four controls break it: dropping the inversion μ(t'), putting ν_1 on both sides at t', dropping the t' puncture, and dropping χ_{t'}(J)⁴.

**Predicted insensitive:** conjugating χ_{t'}(y) on both sides changes nothing, because it enters only as |χ_{t'}(y)|².

### 3.2 The second Poisson transform in child form (10669-11218); R6

Fix the first-side data C, J, d_k, q_0, t', ρ, ν and the marks. Put c(x) = μνρ(x) χ_x(CJ)⁴ χ_x(d_k) 1_{(x,rad q_0 t')=1} 𝔡(x) W(q_x).

The left side is computed **directly**: Σ_{y∈𝒪} Φ(q_y/K) |Σ_x c(x) conj χ_x(y)|².

The right side is written in the paper's final form:

  Σ_{g',d_2|g',v',k''} μ(d_2)μ(v') |B_o(g')|² |D_o(v';d_2,k'')|² 1_{(v',g'CJ)=1} Σ_ϑ Ĝ(ϑ)
  × Σ_{n_1,n_2} Q_1-summand(n_1) conj Q_2-summand(n_2) × K/(q_{d_2}q_{v'}√(q_{n_1}q_{n_2})) 𝓕Φ(Kq_{k''}/(q_{d_2}q_{v'}²q_{n_1}q_{n_2})).

The details of the right side:
* The Q-summand is a_0(n) ν(n)conj ϑ(n) ρ'(n) χ_n(k_new) χ_n(f_new)⁴ 𝔡(g'v'n) W(q_{g'}q_{v'}q_n).
* k_new = d_kd_2k'' is formed as an element, and f_new = JCd_2v'. The puncture is ρ' = ρ·1_{(n, rad q_0 t' r_g)=1}.
* n runs over **all** squarefree ideals of the pool. Coprimality with g', v', C, J and d_2 must therefore come from χ_n(f_new)⁴ and ρ'.
* k'' runs over all of 𝒪, including 0, so the principal pair is included.
* The radial case is Lemma 17.5 as stated. The shifted Gaussian uses the general Poisson kernel at the element k''/(d_2z_1z_2) and makes almost every pair contribute.

| config | Φ | K | child terms | dual (k''≠0) share | LHS (direct) | rel err of child form | controls: rel err |
|---|---|---|---|---|---|---|---|
| C = 31a, J = 7a·13b, d_k = 31a, rad q_0 = 19a, t' = 37a, ρ at 43b, ν of order 6, one slot list | radial | 2500 | 790 | 6.8e-3 | 42668.1583038661 | 3.9e-16 | drop μ(v') 6.7e-1; f_new without v' 4.6e-4; k_new without d_k 1.4e-2; ϑ swapped 1.0e-2; f_new without d_2 3.9e-16 (insensitive); r_g puncture dropped 5.5e-10 (below tolerance) |
| same | shifted | 2500 | 790 | 8.7e-3 | 42586.5691827129 | 1.9e-16 | 2.4e-1; 3.1e-2; 1.4e-2; 1.4e-2; 1.7e-3; 5.5e-4 |
| C = 1, J = 13a, d_k = 19b (dividing q_0), rad q_0 = 19b, t' = 1, no ρ, ν = χ_4, two slot lists | radial | 500 | 2634 | 5.2e-4 | 228.1550494398 | 8.7e-16 | 9.0; 2.6e-3; insensitive; insensitive; insensitive; 8.2e-5 |
| same | shifted | 500 | 2634 | 1.3e-5 | 228.2707256839 | 4.3e-16 | 2.2e-1; 1.9e-2; insensitive; insensitive; insensitive; 1.9e-3 |

"Dual share" is |LHS − (k'' = 0 part of the child form)|/LHS. Every mutation breaks the replay in at least one run, at 10^5 to 10^15 times the agreement level.

In the second configuration, the three mutations that touch only off-diagonal dual terms do not register: k_new without d_k, ϑ swapped, and f_new without d_2. They change only factors that are trivial when n_1 = n_2 and d_2 = 1. This is consistent with the dual part of that configuration coming from n_1 = n_2 terms alone. The cause was not investigated further. The identity itself holds there to 8.7e-16.

So the following are verified together, end to end:
* the second masked data;
* the signal/CRT ray factor G(ba^{-1});
* the v' Möbius extension and (inverse-second-extraction);
* (inverse-moving-characters);
* the regrouping into k_new and f_new, including the cube-derived J;
* the puncture triple (q_0,t',r_g);
* the ray Fourier step and the d_2 divisor of Lemma 17.5.

**Predicted insensitive:** dropping a_0(v') from D_o changes nothing, because it enters only as |D_o|².

The R6 configurations use squarefree columns of up to four primes with norms in (300, 720), so that g', d_2, v' and n are simultaneously nontrivial. The pool is primes and inert primes of norm ≤ 79.

### 3.3 Weighted Cauchy (D) and the first positive majorant (10553-10655)

(D) is Cauchy-Schwarz for the measure |w_ω|:

  |Σ w U_1 conj U_2| ≤ Σ |w||U_1||U_2| ≤ (Σ|w||U_1|²)^{1/2}(Σ|w||U_2|²)^{1/2}.

It needs no symmetry between the sides, which is why P_1 ≠ P_2 is harmless.

The passage to (inverse-first-majorant) uses four facts:
* |μ(d_k)μ(t')B_{1,1}conj B_{1,2}| ≤ 1 and |unit modes| = 1;
* |e_σ| ≤ Z^{π_β} times the old multiplicity and the absolute assigned-slot product;
* 𝓑_1 ≤ Φ_+;
* for fixed o, P_i depends on (f,h) only through y = hf²E. This is (C) together with (retained-cube-label); Q2 and R6 use exactly this form.

Grouping the (f,h) with a common y costs Σ_{f²E|y} w(f) ≤ C_0 d(y)^{C_0+1} (U1). Since 0 < q_y ≤ Z^{H_use} with H_use bounded, this is ≪ Z^{π_old}. Verified.

### 3.4 Second root and kernel (eq:inverse-second-root-kernel, 11135)

Using q_{z_1}q_{z_2} = q_{v'}²q_{n_1}q_{n_2}, N_c = s_i − g − v and λ_c = H_c − θ − (s_i − g):
* the exponent of Z in K/(q_{d_2}q_{v'}√(q_{n_1}q_{n_2})) is H_use − θ − v − N_c = λ_c + 12η + τ;
* the kernel exponent is H_use + h_2 − θ − 2v − 2N_c.

Both are as displayed. The profile W_i(y_gy_vy_1) is consistent because g + v + N_c = s_i.

### 3.5 Second principal exponent (10755)

Substitute κ_i, H_c and s_i into κ_i + H_c + s_i + B + t + ℓ + R/2. Every extracted length cancels and the result is r + 3ℓ + V − B − j = F − B − j.

The counted variables are:
* rows: Z^{H_use};
* the diagonal x: Z^{s_i+4η};
* C and t': η each;
* (q_0,J): Z^{ℓ+R/2+7η/2}.

With the 9η/2 prefactor loss, the total loss is 9/2 + 12 + 4 + 1 + 1 + 7/2 = 26, plus τ. This matches the text.

### 3.6 Source triples and the normalized measure (11336-11365)

The three balls have exponents:
* q_0: ℓ + R/2 − j + 5η/2, from (fixed-cube-count), whose identity is checked exactly in Q1;
* t': t + η;
* r_g: ĝ − θ̂ ≤ g − θ + 2η.

Their sum is C_c + 11η/2, since 5/2 + 1 + 2 = 11/2. Lattice-ideal counting needs only nonnegative upper exponents, which the source witnesses supply.

The normalized measure dν_σ = Z^{−c_σ} Σ C_K(γ) δ_γ, and its use in the child Cauchy step, is the exact rescaling (normalized-label-measure, 9565). The count appears once, as Z^{c_σ/2} from each square root, and is not squared. Verified by hand.

### 3.7 The new fibre (11299) replaces the sign sum

Oct 5 collapsed the regrouping with the exact sign sum Σμ(e)μ(w) = τ(r)1_{f'|k'}. Sep 30 instead does three things:
* it keeps μ(d_2)μ(v') in the signed weight V_σ through the Cauchy step;
* it bounds |V_σ| ≪ 𝓑_2 μ²(f_new). J, C, d_2 and v' are squarefree and pairwise coprime on the support, a fact R6 exercises;
* it dominates each fibre of ξ ↦ (γ, f_new, k_new) by d(f)^{9+4K}C_K(γ).

The hand count is:
* allocation of f into (J,C,d_2,v'): 4^{ω(f)} = d(f)²;
* the split J = sJ_2: d(f);
* (b_1,b_2) with b_1b_2 = q_0²J_2²s: d(q_0)²d(f)³;
* (𝔄_1,𝔄_2): d(q_0)²d(f)²;
* d_k | f rad q_0 (poisson-divisor-reconstruction, Q1): d(q_0)d(f);
* slots: [d(q_0)d(f)d(t')]^{2K}[d(f)d(r_g)]^{2K}.

The exponents sum to 9 + 4K on d(f) and 5 + 2K on d(q_0), as displayed. Given (d_k,d_2), k'' is unique.

U2 enumerates every source tuple (b_1,b_2,𝔄_1,𝔄_2,C,d_k,t',g',d_2,v') with the stated support conditions:
* 5 abstract primes, with cubes on 3 of them at valuations ≤ 2;
* 5,087,327 sources onto 5488 targets;
* every fibre is ≤ d(f)⁹d(q_0)⁵, with equality only at the trivial target;
* it also confirms supp 𝔅 ⊂ supp(Jq_0) and that q_0 is integral in every source.

In this small universe the minimal exponents are (5,4). The paper's (9,5) is conservative, which is harmless because Lemma 17.2 allows divisor-bounded label weights.

### 3.8 Outer masks and tails

The masks are inequalities, not identities. Their supports were checked in the invmoment ledger: the 12η budget in H_use and M_ch = M_c + η.

The raw tail (10127) follows from shell counting: O(1 + 2^jY/a) points in each shell, with kernel O((2^jY)^{−A}) there. P3 is a sanity check for one Gaussian. For a general Schwartz K it is a proof read, not a computation.

## 4. The helpers

### 4.1 Lemma 17.3 (finite seminorm propagation)

The induction is correct:
* ⟨At + Bξ⟩ ≤ max(1,‖A‖,‖B‖)⟨t⟩⟨ξ⟩;
* the profile bound raised to B' adds B'c' to both height exponents;
* the coefficient-measure bound is used at H_e = H' + B'c'_e(J');
* the ⟨t⟩-exponent is H_e + c_e(H_e), as written.

Taking maxima of indices is legitimate because p_j(w) = Σ_{|α|≤j} sup|…| is monotone in j and the tuple seminorm is 1 + Σp_j(w_i) ≥ 1 (1106, 1121). The product form and E_v = max(a_v, max_e(a_e + Σθ_{e,r}E_{v_{e,r}})) follow the same way.

As noted before (invmoment §2.3), the lemma displays no explicit index recursion. Its orders are finite but not uniform in ε.

### 4.2 Cor 17.4 (indexed propagation)

Normalizing by Z^{Φ_v} and applying (indexed-exponent-defect) gives the edge exponent δ_e. (indexed-coefficient-measure) adds δ_e^{mass}. The child bounds are uniform in labels, so they come out of the γ-integral.

The child-profile bounds must also hold uniformly in γ. The corollary says only that "the child-profile bounds of the lemma hold", so this uniformity is implicit. In the use at 11336-11365 it holds because the profiles do not depend on γ (11225-11228).

The normalized-label paragraph (9552-9580) is an exact rescaling identity. Its warning against counting twice is correct, and it is followed at 11392-11398 ("not its square", 11398).

### 4.3 Lemma 17.5 (masked primitive Poisson)

* **The formula** is the same as [O5] eq:poisson. After the map ψ, m, R, K, q, 𝓕Φ ← χ, 𝔪, 𝔯, ℋ, N, Φ̂ the normalized displays are equal strings (P4).
* **The text is not verbatim.** A word diff of 9722-9781 against 875-932 differs in 458 tokens. Oct 5 gives Φ̂ explicitly (2/√3 measure) and the principal zero-frequency product. Sep 30 instead adds the |γ| = 1 Parseval argument, the principal conventions m = 1 and ψ(0) = 1, the reduction of a ray restriction to primitive characters, and the principal nonzero-frequency bound A Σ_{h≠0}|𝓕Φ(Aq_h)| ≪ 1.
* **Correctness.** Every addition is correct: P2 for the finite transform and |γ| = 1, P3 for the bound with a Gaussian. P1 replays the identity directly, including R sharing primes with m and m = 1.

### 4.4 Lemma 17.6 (sixth-power amplification)

* ψ_u(n) = ν(n)χ_n(u)^{ε} (9227). So ψ_{ua⁶}(m) = ψ_u(m)1_{(m,a)=1}, including when u and a share primes.
* Splitting n = dm with d | rad a gives (sixth-power-column-identity), with coefficient mass ≤ d(a) (V1, with ν of order 6 and both signs ε).
* The map (u,a) ↦ ua⁶ is injective by valuations mod 6 and the primary generator (V2, exact, including units and shared primes).
* q_{ua⁶} ≤ CUP⁶ = CH.
* Averaging over ≥ c_SP primary a gives H/P = U^{1/6}H^{5/6} (V3), and e(r) = max(1,(1+5r)/6) as c → 0 (invmoment C26-C28).
* Imported: eq:raw-moment (Lemma 17.1 at m = 1) and the Sobolev step of Lemma 4.5.

No error was found.

## 5. Smallest remaining unverified steps in Lemmas 17.1 and 17.2

1. **Lemma 17.2, analytic separation.** This is the 9- and 6-coordinate Fourier identities (10538, 11209) together with (inverse-joint-fourier-moments) (11247). Algebraically they restore the profile term by term, and R6 and Q2 replay the arithmetic they separate. The open part is the uniform moment bound from the imported Lemma 4.5, at orders chosen before T_1.
2. **Lemma 17.1, initialization transform (11606-12271).** It has a ledger PASS (invmoment C19-C25), but no identity replay. Its one masked Poisson, its regrouping ψ_u(n)ψ_u(P) = ψ_u(j)²ψ_u(c) (11616) and its new label could be replayed with this script's machinery in the same way as Q2.
3. **The terminal input.** Lemma 14.3 (old-eq:4.6), which supplies the three terminal estimates. It remains target 1 of SEP30_VERIFICATION_MAP.md and is load-bearing.

## 6. Misreadings to avoid

* "All 11 identities verified" means that each displayed algebraic or arithmetic identity, count or exponent bookkeeping step is correct. It does not mean that Lemma 17.2 is proved: the analytic separation and Lemma 14.3 remain.
* The replays are floating point at small norms (≤ 7.2·10² for columns, ≤ 2.6·10³ for Q2): EMPIRICAL, not certified. The hand derivations are general.
* U2 verifies the fibre bound in one small abstract universe at K_slot = 0. The general bound rests on the hand count in §3.7.
* RH remains unsolved. Even if accepted, 7/8 is a fixed half-plane statement.
