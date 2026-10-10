# A4 at n = 3: no older moving character at a nonunit second-transform prime

```text
Status:      PROPOSED (exploratory, unreviewed, not integrated). RH is not addressed. Verdict:
             A4 is PROVED at n = 3 (PROPOSED), relative to the inherited datum class and
             second-transform construction (core (A) of CUBIC_N3_GAPS Sec. 4), which this note
             does not re-derive. The proof does not use any sextic-specific fact. At n = 3 it is
             simpler than at n = 6, because the reciprocity phase R is identically 1. So
             Corollary 4.H(4) (e_p = i + 1, residue 1 mod 3 at i = 1, f = v_1) and Lemma 4.G
             (kappa_2 = 1) no longer import A4. Everything here sits inside a CONDITIONAL
             scheme (SKETCH.md, Theorem C4, conditional on (H-A), (H-B)) and is not evidence
             for any global statement.
Scope:       one local bookkeeping statement about the column twist at a prime p of the
             complete common support of a nonzero genuine second allocation (D_2, E_2):
             equal multiplicity i, 3 does not divide i, nonunit. Finite and local. It is not
             a statement about the size of any sum.
Exact sources or dependencies:
             manuscript paper.tex at commit 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, path
             standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
             The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, sha256
             42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed here;
             read as untrusted data). Lines read: 557-603 (conventions, S, primary), 933-960
             (reciprocity, R), 1060-1072 (eq:row-fixed-ray-reduction), 6936-6990 (datum class:
             twist tau, D_mov, punctures), 7081-7232 (lem:full-correlation,
             lem:complete-support-correlation), 12490-12525 (moving support, Theta),
             12990-13085 (eq:centered-coefficient-form, tau_1, zero retention), 13180-13290
             (first transform: e, r, tau_C, tau_D), 13455-13532 and 13570-13594 (amplifier),
             13596-13800 (second transform, G_c, V_id, e_p), 13874-13945 (child rows,
             Moebius t), 14300-14390 (Theta rows, forced residues), 14945-14960 (masks).
             This directory: LEMMAS_4BCD_GH.md (Corollary 4.H, Lemma 4.G), LF_THETA_THIRD.md
             (Sec. 4, 5), SKETCH.md Sec. 4 (Lemma 4.G, Lemma 4.H, Corollary 4.H). Imported
             standard fact: cubic reciprocity for primary elements of Z[omega] (I1).
             Repo HEAD at time of writing: 4cdc12733b2e2ee118edd61a66f09c32da2fb304.
What was actually run:
             nice -n 10 python3 -I a4_checks.py (this directory) -> a4_checks.out:
             5/5 checks PASS, 4/4 failing controls detected, under 1 s, one process.
             Script sha256 5b463416...a0a0da4; output sha256 67cf3f27...d11848b. Exact integer
             and Z[omega] arithmetic, brute-force congruence sums on moduli of norm <= 931,
             residue symbols over primes of norm <= 3000. No floating point. No Lean, lake or
             comparator process.
Smallest remaining gap:
             The proof uses three facts about the cubic transcription of the manuscript's
             construction. (a) Every column twist tau_1 is a fixed S-ray character times
             displayed residue-symbol factors, evaluated on the full column u. (b) The second
             transform's columns are u = D_2 a with the complete common support extracted.
             (c) Earlier extracted primes (first transform e, r; amplifier extractions; old
             masks) are coprime to every later residual column. These hold in the manuscript
             at n = 6 and are order-free in form, but the cubic induction as a whole is
             core (A) and is not re-derived here. Also not re-derived: the cubic amplifier
             (h -> h p^3); only its puncture property is used.
```

## 1. The claim, made precise

**Terminology.** The manuscript says "existing moving character" (l. 14352). LEMMAS_4BCD_GH and
LF_THETA_THIRD call the same thing "older". This note uses *older* = *existing*.

**Moving character.** A row sum carries a twist `τ` (l. 6955-6961, 12494-12505). It is displayed
as a product of:

* a *fixed* finite-ray character, whose conductor primes lie in `S`;
* *moving residue-symbol factors*, i.e. symbols `χ_q(n)^e` or `χ_n(k)^e`. Here `q` is a good prime,
  or `k` is a good element, chosen or frozen at a `Z`-dependent label.

A moving factor *is attached at* `p` if `p = q` or `p | k`. `D_mov` is the squarefree product of
all good primes at which some displayed moving factor has its natural zero. That includes
exponents divisible by `n`, and factors that cancel after multiplication (l. 6958-6963). A moving
character "with moving conductor cannot be relabeled as fixed" (l. 6979-6980). In the column
coefficient (eq:centered-coefficient-form, l. 13052-13068) the twist is called `τ_1`. It is one
zero-extended product of a fixed finite-ray character and moving residue-symbol factors,
multiplicative on full products with all zeros retained (l. 13052-13084).

**Order ("older").** Moving factors accumulate along the induction. The child of a second
transform has row character (l. 13936-13942)

    Ψ_{h'}(n) = τ_1(n) ρ(n) χ_n(G_c V_id h'),   ρ ∈ Θ.

So the child's twist is `τ' = τ_1 · ρ · χ_·(G_c V_id)`, with moving support of length at most
`q̃ + w_o + t_2 + V` (l. 13787-13789). Relative to a given second transform:

* the **older** moving characters are the displayed moving factors of `τ_1`. These come from the
  input datum's `τ` (all ancestors), the current first transform (`χ_a(𝔢𝔯)`, `ξ_𝔯`, l. 13227-13231),
  and the amplifier extractions (`R(p,u)^i χ_p(u)^{2i}`, l. 13477-13492);
* the **new** moving character is `n ↦ χ_n(G_c V_id)` with `e_p = v_p(G_c V_id) mod n`
  (l. 13767-13775).

**A4 (statement at n = 3).** Fix a nonzero genuine second allocation. This means `u = D_2 a`,
`v = E_2 b` with the complete common support extracted, `(a,b) = 1`, `(ab, D_2E_2) = 1`, and the
allocation coefficient `B(u)τ_1(u)·1_mask(u)` not identically zero. Let `p` be a common prime of
equal multiplicity `i` with `3 ∤ i`, nonunit (`p | j/G_c`). Then:

* **(A4.1)** `p ∉ S`, `p ∤ D_mov(τ_1)`, `p` is not in any old common mask, and `p` is not among
  the first-transform primes `𝔢, 𝔯` or the extracted amplifier primes. In particular no older
  moving factor is attached at `p`.
* **(A4.2)** As a character of the residual column `n` (coprime to `p`), the `p`-component of
  `Ψ_{h'}` is exactly `χ_p^{i+1+v_p(h')}`. No other factor contributes at `p`: not `τ_1`, not
  `ρ, ρ' ∈ Θ`, not the reciprocity phases, and nothing from the Möbius ideal `𝔱`, the factor
  allocation or a frozen slot.
* **(A4.3)** Hence `e_p = i + 1` (because `v_p(G_c) = i` and `v_p(V_id) = 1`). Exceptional
  induction forces `v_p(h') ≡ −(i+1) (mod 3)`, which gives `1, 0, 2, 1, 0, 2` for `i = 1, …, 6`.
  At `i = 1` the forced residue is `1`, so `r_p = 1` and `f ≥ v_1`.

**What must be excluded at p.**

* (E1) An older factor attached at `p` with exponent `≢ 0 (mod 3)`. This would shift `e_p`.
* (E2) A fixed-ray component ramified at `p`.
* (E3) A same-generation factor attached at `p` acting on the residual column. For example, the
  factor `conj(χ_a(E_2))` that appears when the congruence is solved at the primes of `a`, before
  it cancels.
* (E4) Contributions at `p` from `𝔱`, from factor allocations, or from frozen slots.

Only (E1) with exponent `≡ 1 (mod 3)` at `i = 1` would affect the ledger (Sec. 5).

## 2. The manuscript's justification (n = 6), located and checked

The relevant passage has two parts.

* **l. 14317-14324 (support disjointness).** "Every prime in the existing full displayed moving
  support is a common column zero, as is every extra common puncture. This is true initially,
  remains true for `𝔢, 𝔯` in the first transform, and remains true for an amplifier prime. For a
  nonzero genuine second allocation, the factors `τ_1(D_2), τ_1(E_2)` and the old common masks
  therefore force its complete radical to be disjoint from all those supports." The passage adds
  that this is decided before any frozen scalar is bounded, and that the artificial residual
  extension cannot revive an impossible allocation.
* **l. 14349-14357.** At an `i = 1` nonunit prime, `G_cV_id` has valuation 2. "There is no
  existing moving character at that prime, and every character of `Θ` is unramified there. Sextic
  reciprocity therefore shows `v_p(h') ≡ 4 (mod 6)`." (Citation fix already noted in
  LF_THETA_THIRD Sec. 5: the A4 sentence is at l. 14352-14353.)

**Check of each step at n = 6.** All steps hold.

1. *Initially.* The datum convention requires every good prime carrying a displayed moving zero
   to be in `D_mov`, or to be moved into a common puncture `R` by an exact refactorization. "No
   zero prime may be omitted from both supports" (l. 6966-6976). This holds by hypothesis on the
   class.
2. *First transform.* The new characters `χ_a(𝔢𝔯)ξ_𝔯(a)` are attached at primes of the extracted
   `C, D`. The residuals satisfy `(ab, CD) = 1`, and "its new moving primes belong to the
   extracted support and puncture every residual factor" (l. 13193-13200, 13271-13275). The
   second transform's columns are built from these residuals, so they are coprime to `CD`.
3. *Amplifier.* In the extracted terms the residual product is punctured at the pool prime
   (l. 13489-13492). In the main term `𝓗(hp^6)` the pool prime moves into the row and creates no
   column character. A new extra mask is supported on frozen columns or a frozen amplifier prime
   (l. 14952-14954).
4. *Zero at the allocation.* `τ_1` is multiplicative on full products with zeros
   (l. 13077-13084). If `p | D_2` and `p ∈ D_mov(τ_1) ∪ R`, then `τ_1(D_2 a)1_{(D_2a,R)=1} = 0` for
   every `a`, and the whole allocation vanishes. The manuscript discards such allocations before
   any absolute bound (l. 13204-13207, 13761-13762).
5. *Fixed characters.* `p | D_2` lies outside `S` because column sums exclude `S` (l. 598-603).
   So `Θ` and the fixed part of `τ_1` are unramified at `p`.
6. *Same-generation factors.* lem:complete-support-correlation (l. 7197-7232) gives
   `F(D_2a, E_2b; j) = F(D_2,E_2;j) R(a,E_2) conj(R(b,D_2)) R(a,b) χ_a(j) conj(χ_b(−j))`. The
   factor `conj(χ_a(E_2))` from the primes of `a` cancels against `χ_{E_2}(a)` from the change of
   variables at `D_2E_2`, leaving only the fixed-ray phase `R(a, E_2)` (proof, l. 7213-7224). The
   Möbius `𝔱` is disjoint from `D_2E_2` (l. 13905-13908). Factor allocations and frozen slots give
   row scalars only (l. 13915-13950).

The one place where sextic arithmetic enters the manuscript's argument is the last step,
"sextic reciprocity". It is needed to turn `χ_n(p)^e` into `χ_p(n)^e` up to the fixed-ray phase
`R(n,p)`, which is unramified at `p`. That step is correct at `n = 6`.

## 3. Re-derivation at n = 3

**Lemma A4(3) (PROPOSED).** The statements (A4.1)-(A4.3) of Sec. 1 hold at `n = 3`, given the
cubic transcription of the datum class and of the two transforms (the gap in the header).

*Proof.*

(A4.1)

* `p ∉ S`, as in step 5.
* Suppose some displayed moving factor of `τ_1` is attached at `p`. Each such factor vanishes at
  every argument divisible by `p`:
  * `χ_p(x)^e = 0` when `p | x`;
  * `χ_x(p)^e` and `χ_x(k)^e` with `p | k` contain the factor `χ_p(p) = 0` when `p | x`;
  * a factor with `3 | e` is displayed as `1_{(x,p)=1}` by the zero-retention convention
    (l. 13081-13082, "six" → "three").
* By multiplicativity on full products, `τ_1(D_2 a) = τ_1(D_2)τ_1(a)`, and `τ_1(D_2) = 0`.
* An old common mask containing `p` likewise gives `1_{(D_2a,R)=1} = 0`.
* So the allocation is identically zero, contradicting the hypothesis.
* The first-transform primes and the extracted amplifier primes are coprime to all residual
  columns (steps 2-3, which are order-free). The cubic amplifier uses `h ↦ hp^3` in place of
  `hp^6`, but only its puncture property is used here.

(A4.2) Take `n` primary and coprime to `3pS`.

* *Older factors.* By (A4.1) each moving factor of `τ_1` is attached at primes `q ≠ p`. A symbol
  `χ_q(n)^e` is a character of `n` modulo `q`. By cubic reciprocity `χ_n(q) = χ_q(n)` for coprime
  good primaries, so `R ≡ 1` ([K5]). So every older factor is unramified at `p`.
* *Fixed characters.* The fixed-ray part of `τ_1` and `ρ ∈ Θ` have conductor in `S`.
* *Correlation phases.* At `n = 3` the phases `R(a,E_2)`, `R(b,D_2)`, `R(a,b)` are identically 1.
  The complete-support correlation reduces to `F(D_2a, E_2b; j) = F(D_2,E_2;j) χ_a(j) conj(χ_b(−j))`
  ([K1], with the un-cancelled control [K1-CTRL] failing). So the second transform puts no factor
  attached at `p` on the residual column, apart from `χ_a(j)`.
* *Other contributions.* `𝔱`, factor allocations and frozen slots contribute nothing at `p`, by
  step 6, which is order-free.
* *The remaining factor.* `χ_n(G_cV_id h') = Π_{π | G_cV_id h'} χ_π(n)^{v_π(G_cV_id h')}` by
  multiplicativity and cubic reciprocity. The unit and `S`-part of `h'` give an `S`-ray character
  (Lemma 4.H(5)). So the `p`-component is `χ_p^{v_p(G_cV_id h')} = χ_p^{i+1+v_p(h')}`.

(A4.3)

* `G_c = (D_2,E_2)` has `v_p(G_c) = min(i,i) = i`, and `V_id` is the squarefree product of the
  nonunit primes, so `v_p(V_id) = 1`.
* `χ_p` has exact order 3 on `(O/p)^×`, since `3 | q_p − 1` for good `p`.
* By CRT, the inducing character of `Ψ_{h'}` has conductor exponent 1 at `p` iff
  `3 ∤ i + 1 + v_p(h')`. A member of `Θ` has conductor in `S`, so exceptionality forces
  `v_p(h') ≡ −(i+1) (mod 3)`. This is Corollary 4.H(1) with `e_p = i + 1`.
* At `i = 1` the residue is `1`, so `𝔥_0` has `p`-exponent `r_p = 1` and `q_{𝔥_0} ≥ Z^{v_1}`.
  This is sharp: `h' = p` is exceptional (LF_THETA_THIRD [B3]). ∎

**Sextic-specific facts? None are used.**

* *`χ_p^3` and sixth-power residues.* The only order-dependent ingredient in (A4.1) is the
  zero-retention convention for exponents divisible by `n`. It is not even needed for (A4.2)-(A4.3).
  A factor attached at `p` with `3 ∤ e` vanishes on multiples of `p` because of the definition of
  the residue symbol. A factor with `3 | e` that was (wrongly) not zero-retained is unramified at
  `p`, so it would not change the residue. The convention matters for the moving-support count
  `q'`, not for A4's conclusion. So the extra principal powers at `n = 3` cause no difficulty: for
  example, nonunit `i = 2` gives `e_p = 3 ≡ 0`, and such a prime is represented only by its
  puncture (l. 13778-13783).
* *Order-6 unit action.* Not used. Units sit in the `S`-part of `h'` and give `S`-ray characters
  (Lemma 4.H(5), units mod cubes, 3 classes).
* *Sextic reciprocity.* It is replaced by cubic reciprocity, with `R ≡ 1` ([K5]). The sextic
  symbol does violate `χ_a(b) = χ_b(a)` on 1180 of 2926 prime pairs ([K5-CTRL6]). That is why the
  manuscript carries `R` at `n = 6`. At `n = 3` the step is strictly simpler.

## 4. Checks (`a4_checks.py`, output `a4_checks.out`)

| tag | what | result |
|---|---|---|
| K1 | `F(Da,Eb;j) = F(D,E;j)χ_a(j)conj(χ_b(−j))` (`R = 1`). Brute-force congruence sums. 6 configurations: equal `i = 1, 2`, unequal, split `pp̄`, with residual norms 13 and 19. 48 `(config, j)` cases, 34 nonzero | exact, PASS |
| K1-CTRL | the formula keeping the un-cancelled `conj(χ_a(E))χ_b(D)` (a character attached at primes of `D, E` on the residual) | detected (fails) |
| K2 | 6 displayed moving-factor forms attached at `q` (`Nq = 7`): `χ_q(u)^{1,2}`, `χ_u(q)^{1,2}`, `χ_u(qr)`, zero-retained `χ_q^3`. All vanish on all 86 good primary `u` with `q | u`, `Nu ≤ 2000` | exact, PASS |
| K2-CTRL | the "unit-part extension" `χ_q(u q^{−v_q(u)})` is nonzero on 86/86 such columns (54 nontrivial). It would survive into `D_2` | detected |
| K3 | `n ↦ χ_p(n)^{e_old} χ_n(p^{2+k})` is `S`-ray (constant on primary primes in each class mod 18, `Nn ≤ 1500`) iff `e_old + 2 + k ≡ 0 (mod 3)`, for `Np = 7, 13`, `k = 0..5`. With `e_old = 0` (A4) this gives `k ∈ {1, 4}` | exact, finite, PASS |
| K3-CTRL | a surviving older `χ_p^1` would give `k ∈ {0, 3}`, i.e. `r_p = 0` | detected |
| K4 | ledger cost table (Sec. 5) | exact (Fractions), PASS |
| K5 | cubic reciprocity on 2926 pairs of good primary primes with norm ≤ 400 | exact, PASS |
| K5-CTRL6 | sextic symbol: reciprocity without `R` fails on 1180/2926 pairs | detected |

K1-K3 and K5 are finite illustrations on small moduli, not proofs. The proof is Sec. 3.

## 5. If A4 had failed: the counterexample shape and its cost (labelled hypothetical)

Suppose an allocation survived with an older factor `χ_p^{e_old}` at a nonunit equal prime.
This is impossible by (A4.1). Then `r_p = −(i+1+e_old) mod 3`. With the (LF) per-prime entry
`F_2 = 2i − (2/3)i − 1 + 1/3 + r_p/3` and `b_2 = i` ([K4]):

| `i` | `e_old = 0` (A4) | `e_old = 1` | `e_old = 2` |
|---|---|---|---|
| 1 | `r_p = 1`, `F_2 − b_2 = 0` | `r_p = 0`, **`F_2 − b_2 = −1/3`** | `r_p = 2`, `+1/3` |
| 2 | `0`, `0` | `2`, `+2/3` | `1`, `+1/3` |
| 4 | `1`, `+1` | `0`, `+2/3` | `2`, `+4/3` |
| 5 | `0`, `+1` | `2`, `+5/3` | `1`, `+4/3` |

So the only damaging shape is a surviving older exponent `≡ 1 (mod 3)` at a nonunit `i = 1`
prime. That would cost `1/3` per unit log-norm of such primes. If such primes dominated `b_2`, it
would give `F_2 = (2/3)b_2`, i.e. `κ_2 = 2/3 = 2θ` and zero margin (as in LF_THETA_THIRD
[C-CTRL1]). The manuscript itself would lose the same `1/3` at `n = 6` in that case: its residue
would move from `4` to `3 (mod 6)` with `e_old = 1`. Since (A4.1) excludes every such survivor,
none of this occurs.

## 6. Verdict and effect on the other notes

* **A4 at n = 3: PROVED (PROPOSED)**, relative to the inherited cubic datum class and transforms
  (core (A)). The manuscript's `n = 6` justification (l. 14317-14324 plus l. 14352-14353) is
  correct. Its only sextic input, reciprocity with phase `R`, becomes trivial at `n = 3`.
* **Corollary 4.H(4)** (LEMMAS_4BCD_GH Sec. 4): the clause "if there is no older moving
  character at `p` (imported, A4)" can be dropped on nonzero allocations. So `e_p = i + 1` and
  `f ≥ v_1` hold (PROPOSED).
* **Lemma 4.G** (`κ_2 = 1`) and **(LF)** (LF_THETA_THIRD): their dependence on A4 is discharged.
  They still depend on core (A).
* **SKETCH Sec. 4, Corollary 4.H, third bullet:** "at a second-transform prime with no older
  moving character" is always satisfied on nonzero genuine allocations.
* **Not changed:** the conditional status of Theorem C4 ((H-A), (H-B)). This note gives no
  evidence for any global statement.
