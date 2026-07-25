# LITERATURE.md

Classical results this repository relies on, and — more importantly — the
status of each reliance.  Per M-0004, a recalled-but-unverified statement is
flagged, and the flag records whether being wrong would cause a **false
positive** (a spurious counterexample) or a **miss** (a real counterexample
overlooked).  A false-positive-direction flag may not be used at all.

**This agent had no access to the literature during the session.**  Everything
below is either (a) reproved in this repository, (b) a standard result used in
a form robust to misremembering, or (c) flagged.  Treat every citation as a
pointer for a human to check, not as a verified reference.

---

## A. Reproved here — no citation needed

| Result | Where |
|---|---|
| Euler-Maclaurin summation with periodic-Bernoulli remainder, and an explicit bound for `zeta` | L-0001 (derivation given) |
| Argument principle applied to a rectangle with certified enclosures | L-0002 (proof given) |
| Count-matching: box count = sign changes implies RH in the box | L-0004 (proof given) |
| Taylor-model enclosure with explicit tail | L-0006 (proof given) |
| Hermite-Hankel box criterion | T-0001 (proof given, from the residue theorem + Hermite's theorem) |

## B. Standard results used, not reproved

| Result | Used in | Risk if misremembered |
|---|---|---|
| `zeta` has no zeros with `Re s >= 1` (Hadamard, de la Vallee Poussin) | L-0004, last paragraph only | Would break the *scope* of L-0004, not its certificates.  Far weaker than RH; its standard proof does not use RH |
| Functional equation `xi(s) = xi(1-s)`, reflection `xi(conj s) = conj xi(s)` | T-0001(b), and as a test | Wrong here would be caught immediately by the functional-equation test in `tests/` |
| Hermite's theorem: signature of the Hankel form of a real polynomial counts distinct real roots | T-0001(c) | This is the load-bearing algebraic input.  **A reviewer should check this statement first.** |
| Explicit formula for `psi(x)` | X-0005, O-0001, O-0002 | Only used for interpretation of an uncertified screen |
| Mertens' theorem | O-0001 | Only used for interpretation |
| `\|B~_{2n}(x)\| <= \|B_{2n}\|` for the periodic Bernoulli function | L-0001 | Follows from its Fourier series; sketched in L-0001 |
| Delves-Lyness contour moments for locating zeros | T-0001 (attribution) | Attribution only — the method is derived from scratch |
| `Lambda >= 0` (Rodgers-Tao) and RH `<=>` `Lambda <= 0` | motivation for X-0004 / Z-0002 | Motivational only; no claim depends on it |

## C. Flagged: recalled, unverified, and load-bearing to some degree

### Q-0005 — Csordas-Smith-Varga Lehmer-pair criterion
**Recalled:** a "Lehmer pair" with the discriminator
`D_n = g_n^2 sum_{j != n,n+1} [(gamma_j - gamma_n)^-2 + (gamma_j - gamma_{n+1})^-2]`
below an explicit threshold yields a lower bound for the de Bruijn-Newman
constant `Lambda`.
**Direction of risk:** FALSE POSITIVE — a wrong constant could turn an ordinary
close pair into an apparent proof that `Lambda > 0`, i.e. an apparent
disproof of RH.
**Therefore: NOT USED.**  X-0004 computes and reports `D_n`, which is well
defined independently of the constant, and states no consequence.  The smallest
value found below `T = 2000` is `D = 0.0259` at `gamma = 1977.17`.
Note additionally that X-0004's `D_n` truncates the zero sum, making it a
*lower* bound for the true `D_n` — the wrong direction for certifying a pair,
and another reason the criterion is not applied.

### Q-0007 — Robin's reduction to superabundant numbers
**Recalled:** if Robin's inequality fails for some `n > 5040`, it fails for some
superabundant `n`; hence testing colossally abundant numbers is the right
search.
**Direction of risk:** MISS — a wrong recollection means the search set is
badly chosen and a counterexample elsewhere is never seen.  It cannot produce a
false counterexample, because every reported margin is computed exactly for the
specific `n` tested.
**Therefore: used**, to choose the test set only, and flagged in the X-0003
module docstring.

### The exceptional set of Robin's inequality
**Recalled:** the inequality `sigma(n) < e^gamma n log log n` is asserted for
`n > 5040`, and fails for the finite list
`2,3,4,5,6,8,9,10,12,16,18,20,24,30,36,48,60,72,84,120,180,240,360,720,840,2520,5040`.
**Direction of risk:** FALSE POSITIVE if the threshold `5040` were wrong in the
permissive direction.  X-0003 therefore excludes everything with `n <= 5040` by
the *threshold*, not by matching the list, so the list being misremembered is
harmless.  The seven "violations" the first run reported were all in this range
and were correctly reclassified as non-counterexamples.

---

## D. What a human with library access should check first

1. Hermite's theorem as stated in T-0001(c) — the load-bearing algebraic input.
2. The Csordas-Smith-Varga constant (Q-0005) — it sits directly on the path
   from a Lehmer pair to `Lambda > 0`, which would disprove RH.
3. Robin's reduction (Q-0007) — determines the entire arithmetic search set.
4. Whether the Hermite-Hankel packaging of T-0001 is already in the literature.
   It very plausibly is; the repository claims only that it is implemented and
   certified here, not that it is new.
