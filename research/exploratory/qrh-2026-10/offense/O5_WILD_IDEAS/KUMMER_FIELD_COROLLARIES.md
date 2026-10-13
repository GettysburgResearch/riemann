# What the Hecke-family 7/8 statement already gives for Kummer and anticyclotomic fields

```text
Status: CONDITIONAL on HECKE-7/8 (below) + PROPOSED derivations (classical arguments, written
  here, not reviewed) + EMPIRICAL (finite exact-integer checks, Sec. 4). RH is unsolved; nothing
  here bears on the critical line. No exponent below 7/8 is claimed.
Scope: seed 2a ("does 7/8 extend to Hecke L-functions of Kummer extensions K(u^(1/6))/K?") and
  seed 10 (consequences of the 7/8 half-plane): Dedekind zeta functions of subfields of abelian
  extensions of K = Q(sqrt(-3)); least primes with a prescribed cubic/sextic residue behaviour.
Exact sources or dependencies:
  HECKE-7/8 := "for every finite-order Hecke character psi of K = Q(sqrt(-3)), L(s, psi) != 0 on
    Re s > 7/8 (pole of zeta_K excepted)". It is the Sep 30 manuscript's Thm 1.1 (external,
    unreviewed); its Lean form is accepted by comparator with two kernels
    (reviews/LEAN_BUILD_ATTEMPT.md Addendum C, trust assumptions there), and its match to all
    ray class characters of K is a reading-level check (reviews/HECKE_LEAN_FIDELITY.md lines 61-62,
    139: Cl_m = (O/m)^x / im(mu_6) since h_K = 1).
  Classical, not re-read here: Artin reciprocity and the conductor-discriminant formula
    (zeta_M = prod_psi L(s, psi) for M/K abelian); Aramata-Brauer (zeta_M / zeta_F entire when
    M/F is Galois); Kronecker-Weber; the smoothed explicit formula for Hecke L-functions.
  Repository: RUNG_STRENGTH.md Prop. R (psi_u is the Hecke character of K(u^(1/6))/K);
    CONDITIONAL_CONSEQUENCES.md (zeta and Dirichlet consequences, not repeated).
What was actually run: python3 -I galois_cubic_checks.py (part 2: least prime p = 1 mod 3 with m a
  cubic non-residue mod p, all non-cubes m <= 200000, exact integer arithmetic); output
  galois_cubic_checks.json.
Smallest remaining gap: none for the corollaries as stated, beyond HECKE-7/8 itself and an
  independent review of the two short derivations (Prop. K1, Prop. K2). They move no exponent.
```

## 0. Answer to seed 2a

The Kummer characters `ψ_u : 𝔫 ↦ (u/n)₆` are finite-order Hecke characters of `K`, i.e. ray class
characters (Prop. R of RUNG_STRENGTH; HECKE_LEAN_FIDELITY §3). So the 7/8 statement for them is
**not an extension; it is already a special case** of HECKE-7/8. What does *not* follow is 7/8 for
Hecke characters of the field `K(u^{1/6})` itself that are not induced from `K`. The Sep 30 method
is built on Patterson's cubic theta over `Q(ω)`, and no analogue over a degree-12 field is known.
Verdict: covered (ALIVE as a corollary); the genuine extension is OPEN and has no known route.

## 1. Dedekind zeta functions (Prop. K1)

**Prop. K1 (CONDITIONAL on HECKE-7/8; PROPOSED proof).** Let `F` be a number field contained in some
abelian extension `M` of `K = Q(√−3)`. Then `ζ_F(s) ≠ 0` for `Re s > 7/8`.

*Proof.* Let `σ` be complex conjugation. `σ(M)/K` is abelian, so `M̃ = M·σ(M)` is abelian over `K`
and Galois over `Q`. By Artin reciprocity and the conductor-discriminant formula,
`ζ_{M̃}(s) = ∏_ψ L(s, ψ)` over the primitive Hecke characters of `K` cut out by `M̃` (finite order).
Each factor is zero-free on `Re s > 7/8` by HECKE-7/8; `ζ_K = L(s, 1)` has its pole only at `s = 1`.
Since `F ⊂ M̃` and `M̃/Q` is Galois, `M̃/F` is Galois, so by Aramata–Brauer `ζ_{M̃}/ζ_F` is entire. A
zero of `ζ_F` would therefore be a zero of `ζ_{M̃}`. ∎

Fields covered that are **not** covered by the Dirichlet version (Lean-checked for Dirichlet `L`):
* every pure cubic field `Q(m^{1/3})` and its Galois closure `Q(ω, m^{1/3})` (an `S₃` field);
* every `Q(m^{1/6})`, and every subfield of `Q(ω, m₁^{1/6}, …, m_r^{1/6})`;
* every ring class field of an order in `K` (e.g. `Q(√−3, j(τ))` for `τ` in such an order), and
  every dihedral extension of `Q` whose quadratic subfield is `Q(√−3)`.

Abelian fields over `Q` are included as well (Kronecker–Weber: `F ⊂ Q(ζ_N) ⊂ K(ζ_N)`), but those already
follow from the Dirichlet statement.

## 2. Least primes with a prescribed residue symbol (Prop. K2)

**Prop. K2 (CONDITIONAL on HECKE-7/8; PROPOSED, standard argument).** For every integer `m ≥ 2` that is
not a cube, the least prime `p ≡ 1 (mod 3)`, `p ∤ m`, for which `m` is a cubic non-residue mod `p`
satisfies `p ≪_ε (log m)^{8+ε}`, with an effective implied constant. The same holds for sextic
non-residues of non-sixth-powers, with the exponent `8 + ε`.

*Proof sketch.* Let `ψ = ψ_m²`, the cubic Kummer character of `K(m^{1/3})/K`. It is nontrivial because
`m` is not a cube in `K`: `m ∈ Z`, and `K^{×3} ∩ Q = Q^{×3}` up to units. Its conductor `𝔣` has
`log N𝔣 ≪ log m`.
* At inert primes `q ≡ 2 (mod 3)`, `ψ(q) = 1`, because `m ∈ F_q^×` and
  `m^{(q²−1)/3} = (m^{q−1})^{(q+1)/3} = 1`.
* At a split `p = π π̄`, `ψ(π) = (m/π)₃`, and `(m/π)₃ = 1` iff `m` is a cube mod `p`.

So if `m` is a cube mod every `p ≤ y`, then `ψ(𝔭) = 1` for every unramified prime ideal of norm `≤ y`.
Take a smooth `w ≥ 0` supported in `[1/2, 1]` with `∫ w > 0`, and consider
`Σ_𝔞 Λ_K(𝔞)(1 − ψ(𝔞)) w(N𝔞/y)`. A term is nonzero only if `𝔞 = 𝔭^k` with `ψ(𝔭) ≠ 1` and
`N𝔭 ≤ N𝔞 ≤ y`, i.e. only for the ramified primes `𝔭 | 𝔣`; they contribute `≪ log m · log y`. By the explicit
formula, the `ζ_K` sum is `y ŵ(1) + O(y^{7/8+ε})`, using HECKE-7/8 for `ζ_K` itself. The `ψ` sum is
`≪ y^{7/8} log(N𝔣) (log y)^{O(1)}`, because the smoothed sum over zeros has `≪ log(N𝔣 (|γ|+2))` zeros
per unit height, all with `Re ρ ≤ 7/8`. Hence `y ≪ y^{7/8}(log m)^{1+ε}`, i.e. `y ≪ (log m)^{8+ε}`.
Effectivity: no exceptional zero is possible under the half-plane. ∎

*Comparison (survey, not re-checked).*
* Under GRH the same argument gives `(log m)^{2+ε}`.
* Unconditionally, effective Chebotarev bounds (Lagarias–Montgomery–Odlyzko; later explicit versions)
  are polynomial in the discriminant of `Q(ω, m^{1/3})`, hence polynomial in `m`.

So Prop. K2 is an exponential improvement over unconditional bounds, *if* HECKE-7/8 holds. This is the
cubic analogue of the Vinogradov-conjecture corollary that the Oct 5 manuscript records for quadratic
non-residues.

**Effective Chebotarev for `Q(ω, m^{1/6})/Q`.** The same explicit formula gives, for every conjugacy
class `C` of `G = Gal(Q(ω, m^{1/6})/Q)`,

    π_C(x) = (|C|/|G|) Li(x) + O(x^{7/8} log(x m)),

with an absolute effective constant (CONDITIONAL; PROPOSED; the reduction from `G` to `K`-Hecke
characters is the usual induction, because `G` has the abelian normal subgroup `Gal(M/K)` of index 2).

## 3. What this does not do

* It moves no exponent: every statement here *is* the 7/8 half-plane, transported.
* It does not reach Hecke characters of `K(u^{1/6})` that are not induced from `K` (§0).
* It does not apply to the Oct 5 dual family `B_h`: those Dirichlet series have no Euler product
  (DISPERSION_GRH_STEP §3(e)). So the import cannot serve as the missing base of the Oct 5 induction
  at `ρ < 1` (own idea N-f, DEAD).

## 4. Finite sanity check (EMPIRICAL; exact integers; proves nothing)

`galois_cubic_checks.py` part 2: over all non-cubes `2 ≤ m ≤ 200000`, the least prime `p ≡ 1 (mod 3)`,
`p ∤ m`, with `m^{(p−1)/3} ≢ 1 (mod p)`:
* the record holders are `(m, p) = (2,7), (6,13), (13,19), (57,31), (77,37), (714,43), (806,61),
  (2478,73), (30659,79)`;
* `max p/(log m)² = 14.57`, attained at `m = 2`.

These are finite and say nothing about the asymptotic exponent. They only confirm that the reduction in
§2, from cubic non-residues mod `p` to `ψ(π) ≠ 1` at split primes, is wired correctly: a failing
control would be a non-cube `m` with no such prime below 20000, and none occurred.
