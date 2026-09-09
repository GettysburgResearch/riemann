# O-108004 — The detector on repository-native observables: label counting and Tate-monomial virtuality

```text
Claim ID: O-108004
Status:   OBSERVATION, PROVED at the stated finite scope (every verdict is
          an exact computation, asserted in the build; imported statements
          are pinned with blob SHAs and their own lane's review status)
Created:  2026-08-31 (continuation pass; the original builder was lost to
          session limits, recorded in the pass reports)
Programme: #763 (the held-out first: these observables exist only in this
          repository, so no outside work could have tested them)
Instrument: T-108002 detector; build worlds/native_imports_build.py;
          record worlds/native_imports.json (10 embedded detector runs)
RH status: RH and GRH are unproved; not addressed.
```

## Finding 1 — the detector reads the native source's label bookkeeping

The T-99930 native duplicate-67 source `beta(n) = mu(n) - 1_{67|n} mu(n/67)`
(pinned: blob `2444935b`, on main) has its documented Euler factorization
verified exactly to `n <= 500` here, and its local sequences produce:

- at every ordinary prime: refusal at A2 with witness numerator `(1 - T)` —
  virtual weight 0, multiplicity 1;
- at the duplicated prime 67: refusal at A2 with witness numerator
  `(1 - T)^2 = [1, -2, 1]` — virtual weight 0, **multiplicity 2**.

The witness numerator is `(1-T)^{#labels(p)}`: the detector recovers the
label multiplicity of the native source from coefficient data alone. Exact
packaged statement of what the native source is, in the detector's
ontology: uniformly VIRTUAL, uniformly WEIGHT 0, with the labelling
visible as virtual multiplicity — bookkept arithmetic, not motivic data.

## Finding 2 — the codex family trace laws are Tate-monomial virtual objects

The genus-2 family trace laws `T_(0,3) = q^4 - 2q - 1`,
`T_(2,2) = 2q^3 - q^2 - 2q - 2`, `T_(0,4) = -(2q^2 + 1)` (pinned: PROVED
in the unmerged codex lane at blob `d4a3da1f`, branch head `d79692ec`;
earlier conjectural form at blob `89b6b984`; used here as pinned imports
whose review status lives in that lane), evaluated along prime-power
towers `t_k = T(q_0^k)` at `q_0 = 3` and `5` (the tower evaluation is THIS
pass's construction, stated as such), give in traces mode:

- A1 HOLDS at rank = number of monomials in the law;
- A2 FAILS — with the recovered multiplicity vector exactly equal to the
  law's coefficient vector, over frequencies that are pure powers of `q`
  (verified exactly at 24 tower terms per run, six runs).

Reading: at the family-aggregate level, everything the codex laws see is
built from **Tate monomials `q^j` with signed integer multiplicities** —
no nontrivial Frobenius angles survive family aggregation, and the
detector certifies precisely that, law by law. This gives the codex lane
an independent, machine-checked characterization of what its family
traces are as structural objects (virtual Tate combinations), and gives
#763 the sharpest available contrast: individual-object data carries
angles (elliptic rows pass A4 with genuine conjugate pairs), family-
aggregated data provably does not.

## Scope

Everything here is finite and exact; nothing is claimed about the codex
lane's open gates, about individual members of the aggregated families,
or about RH. The tower evaluation is a construction choice and other
evaluations of the laws would be other (equally finite) experiments.
```
