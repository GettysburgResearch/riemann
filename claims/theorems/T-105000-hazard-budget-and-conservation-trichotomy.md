# T-105000 — The hazard-budget theorem and the conservation trichotomy for hierarchical factor-67 schemes

Claim ID: `T-105000`
Status: **PROVED CLASSIFICATION / METHOD-SPACE THEOREM — NOT PROGRESS ON RH ITSELF**
Created: 2026-08-21
Agent: claude (external reviewer lane)
RH status: **unproved, and not addressed by this theorem**

Companions: `L-105001` (exchange-rate cap and weight bound), `L-105002`
(branch submultiplicativity), `R-105000` (impossibility corollary and the
adjudication of the third repair option of `R-99260`),
`M-105000` (scope, axiom anchors, acceptance fixtures),
`experiments/X-105000-hazard-budget/verify.py`.

## 0. Purpose

Between 2026-08-17 and 2026-08-21 at least seven refutations executed
hierarchical source constructions by the same one-prime coefficient
mismatch: the generated child carries `2r^2` (gross) or `0` (net) where the
native Möbius update requires `r = p^{-1/2}`
(`R-97600`, `R-99600`/`R-99601`, `R-99440`, `R-99260`, `R-97610`, `R-97500`,
`R-99800`). Each kill was per-construction. This packet replaces the serial
autopsies by one invariant: a **budget identity** that every admissible
scheme obeys, whose per-prime price of native delivery is `(1+o(1))/p`, and
whose total price over rough primes diverges. The recorded defects become
instances; the surviving demand is typed and its minimum size is computed.

Everything here is mathematics about the *method class*, quantified over
schemes. Nothing here bears on the truth of RH.

## 1. Setting (repo objects, all previously proved)

`T(y) = (4\sqrt y - 3)\,\mathbf 1_{y\ge1}`; positive rows
`Q_Y(j) = \int_1^Y T(Y/t)\,\kappa_j(t)\,dt/t` with `\kappa_j(t) > 0` for
`t \ge j` (`L-99240.7/8`); `Q_Y(j) = 4C_j\sqrt Y + O_j(\log 2Y)`,
`C_j = 2/(j(j-1))` (`R-99440.4`); RN thinning
`R_{Z\mid Y}(t) = \mathbf 1_{t\le Z}\,T(Z/t)/T(Y/t) \in [0,1]`,
`dM_Z = R_{Z\mid Y}\,dM_Y` (`L-99250.3/4`); parity channels with swap `S`,
`\mathcal O(S^m P) = (-1)^m\,\mathcal O(P)` (`L-97400`); rough primes
`p \ge 67`, `r_p = p^{-1/2}`.

Native demand (the conservation standard of `L-97400` / `L-99601.2`): the
scheme's signed observation reproduces
`\prod_p (I - r_p U_p)` — every rough subset `A` occurs with coefficient
`(-1)^{|A|}\prod_{p\in A} r_p`.

## 2. The admissible class

A **hierarchical scheme** `S` at root endpoint `Y` decomposes, at every node
(endpoint `Z`, reached by one-prime moves `U_p: Z \mapsto Z/p`, first-owner
disjoint and exhaustive per `L-99601 §2`), the node's positive packet into
finitely many pieces, each typed:

* **FREE** — nonnegative combinations of blocks whose nonnegativity is
  supplied by the free positivity technology already proved in-repo:
  endpoint monotonicity (`L-99210.4`), RN thinning (`L-99250.4`), profile
  monotonicity (`L-99250.7/8`), compact-fibre Hall flows (`L-99020`,
  moat `> 7/20`). Canonical shape: survival `\sigma P_Z` and generalized
  currents `\lambda_b\,(1 - \sum_p c_{b,p} R_{Z/p\mid Z})\,dM_Z \ge 0`.
* **CHILD** — a recursed copy `\alpha_i P_{Z/p_i}` entering the observation
  with one parity swap (source-faithfulness: sign
  `\mu(d)(-1)^{|h|} = \mu(k)`, `L-97400`, `L-96501.3`; omitting the swap is
  nonnative by `R-99600 §1`).
* **DEFECT** — a signed remainder admissible for the consumer:
  `|A_Z(j)| \le B_j` uniformly and/or Mellin transform holomorphic in
  `\Re s > 0` (`T-99450.1`, `L-99422`, `L-99602.6` — the class policed by
  `R-99440`).

Axioms: **(P)** all FREE/CHILD weights nonnegative; sign only architectural
("an oriented difference is not separately a positive physical row",
`L-97400`). **(L)** node partition: the I-slot coefficients sum to one
(`\sigma + \sum_b \lambda_b = 1`; the causal identities `L-96500.1` =
`L-99021.1` are instances). **(N)** half-order normalization: occurrence `k`
carries magnitude `k^{-1/2}` and activation `X/k`, transport-invariant
(`L-97400`); the consumer detector is the reciprocal-zeta pole family at
`z = s + 1/2` (`L-99602`, `L-97404`); the non-summable half-order boundary
must be preserved (`L-99704`). **(C)** conservation: the signed observation
reproduces the native marginal atomwise (`L-97400` standard; Lemma 0 of
`M-105000` shows the consumer functions pin the coefficients through the
activation-knot structure, so (C) cannot be relaxed to "consumer-level
agreement").

Verified instances (`M-105000 §2`): the alpha-child schemes of PR #566,
T-99240, T-99450, PR #649 (via `L-96500.1`); the exact ledgers `L-97400`,
`L-99601.7`, `L-100610`; the RN-corrected cylinder schemes (`L-99450 §1`).

**Delivery accounting.** At the root node, define the **sign-paid first-order
delivery** at rough prime `p`:
`d_p := \sum_b \lambda_b c_{b,p}` — the `U_p`-coefficient carried inside FREE
blocks, whose negativity is paid by the block's proved nonnegativity.
First-order mass carried by CHILD pieces is **sign-unpaid**: it conserves the
coefficient but contributes to the observation with a sign that the free
technology does not prove; the consumer inequality then *requires* dominating
it. DEFECT pieces are excluded from first-order delivery of the native scale
by their own definition (bounded / holomorphic; `R-99440 §2–3`: the native
first-order block `r_p(\cdot)Q_{Y/p}` is of order `\sqrt Y` with a
positive-real Mellin pole at `s = 1/2`).

## 3. Theorem A (hazard-budget inequality)

**Theorem A.1 (budget).** For every admissible scheme at root endpoint `Y`
and every row `j`:

```
sum_{67 <= p <= Y}  d_p * Q_{Y/p}(j)   <=   Q_Y(j).
```

*Proof.* Each FREE current block is a nonnegative measure (equivalently, a
packet-cone element: nonnegativity in `\mathbb R_+^D` is componentwise, so
the same argument runs in each typed coordinate `G`, with `Q_{Y/p}(j)`
replaced by `G(Y/p)`); integrating
`\lambda_b (1 - \sum_p c_{b,p} R_{Y/p|Y})\,dM_Y \ge 0` in the row-`j`
coordinate gives `\lambda_b (Q_Y(j) - \sum_p c_{b,p} Q_{Y/p}(j)) \ge 0`,
i.e. `\sum_p c_{b,p} Q_{Y/p}(j) \le Q_Y(j)` per unit block. Summing with
weights `\lambda_b \ge 0`, `\sum_b \lambda_b \le 1` (axiom L, survival
`\sigma \ge 0`):
`\sum_p d_p Q_{Y/p}(j) = \sum_b \lambda_b \sum_p c_{b,p} Q_{Y/p}(j)
\le \sum_b \lambda_b\, Q_Y(j) \le Q_Y(j)`. The reserve/injection variant —
a child of size `\alpha` paid from a current's mass, the `L-96651`
architecture — consumes the same budget: `\alpha\,Q_{Y/p}(j) \le
\lambda(Q_Y(j) - \sum c\,Q(j))` adds the child's consumption to the same
left-hand side. Hall two-sort blocks (`L-99020`) redistribute mass within
compact fibres `x < 67` and carry no rough `U_p` coordinate, so they do not
contribute to either side. ∎

**Theorem A.2 (price and divergence).** Define the price of full native
delivery in coordinate `G \in \{T, Q_\cdot(j)\}`:

```
Pi_G(Y) = sum_{67 <= p <= Y} r_p * G(Y/p)/G(Y).
```

Then:
(i) `Pi_G(Y) \le \sum_{67\le p\le Y} 1/p` for every admissible coordinate —
by `L-105001` (weight bound `w_p = \sqrt p\,G(Y/p)/G(Y) \le 1`, proved via
the exact identity `\sqrt{Z/Y}\,T(Y) - T(Z) = 3(1 - \sqrt{Z/Y}) \ge 0` and
profile monotonicity `Q_Z/Q_Y \le T_Z/T_Y`).
(ii) `Pi_G(Y) \ge (1 - \tfrac{3}{4} Y^{-1/4}) \sum_{67 \le p \le \sqrt Y} 1/p
\cdot \min_{p \le \sqrt Y} w_p`, and hence `Pi_G(Y) \to \infty`; by Mertens
both bounds are `\log\log Y + O(1)`.
(iii) Full sign-paid delivery (`d_p = r_p` for all rough `p \le Y`) requires
`Pi_G(Y) \le 1` in **every** coordinate `G` of the scheme's positivity cone.
The practiced class demands nonnegativity in the full typed packet vector
`\mathbf P_Y \in \mathbb R_+^D` (`L-99210.1`), and the causal identities hold
"in every linear typed coordinate simultaneously" (`L-96500.1`'s own words),
so the binding coordinate is the one with the largest weights; by
`L-105001 §2` (profile monotonicity) that is `T`, and the unit budget is
exhausted at `Y^* \in (578906,\ 584375)`:
`Pi_T(578906) = 0.99972\ldots < 1 < 1.00052\ldots = Pi_T(584375)`
(interval-guarded computation, `X-105000`). At the crossing,
`\sum_{67\le p\le Y^*} 1/p = 1.133\ldots`. A scheme that deliberately weakens
its cone to rows-only (nonnegativity demanded only in `Q(2), Q(3)`) has a
later horizon — no numeric `Q`-crossing is claimed — but still a finite one,
since `Pi_{Q(j)}(Y) \to \infty` by (i)–(ii).

**Theorem A.3 (exposure).** For every admissible scheme satisfying
conservation (C), the sign-unpaid first-order mass ("exposure")

```
E(S; Y, j) = sum_{67 <= p <= Y} (r_p - d_p) * Q_{Y/p}(j)
           >= (Pi_{Q(j)}(Y) - 1)_+ * Q_Y(j)
```

is eventually positive and of order `\sqrt Y \cdot (\log\log Y - O(1))`
(macroscopic). As a nonnegative function of the root endpoint it fails both
DEFECT typings: it is unbounded, and its Mellin transform
`\int_1^\infty E(Y)\,Y^{-s-1}dY` has convergence abscissa `\ge 1/2`, so by
Landau's theorem on nonnegative densities (the repo's own consumer engine,
`L-99272`/`L-99602`) it has a **real singularity at some
`\sigma_c \ge 1/2`** and is not holomorphic in `\Re s > 0`. The exposure
**cannot be re-typed as DEFECT**. It is a genuine open positive-sign demand
of at least this size.

*Proof.* Subtract Theorem A.1 from the conservation demand
`\sum_p r_p Q_{Y/p}(j) = Pi_{Q(j)}(Y)\, Q_Y(j)`, valid for every root
endpoint `Y` (the scheme may vary with `Y`; the bound is pointwise in `Y`).
For the typing: `E \ge 0` and `E(Y) \ge c\sqrt Y` eventually force
divergence of the transform at every real `s < 1/2`, so the abscissa of
convergence is `\ge 1/2`; Landau's theorem places a singularity at the real
point of the abscissa. When the scheme is endpoint-independent the exposure
is the fixed sum `\sum_p (r_p - d_p)\,Q_{Y/p}(j)` and the singularity is the
explicit positive-real pole of `R-99440.7` aggregated over primes with
nonnegative weights. ∎

## 4. Theorem B (conservation trichotomy)

Within the axioms, every scheme satisfying (C) carries the Theorem A.3
exposure, and the exposure resides in one of exactly three carrier types —
the three ways the axioms permit first-order mass to avoid the FREE typing —
each already named and statused in the repository:

* **(A) Exposure denied — contracted schemes.** The scheme has no carrier:
  it fails (C) with per-prime deficit `r_p - d_p` realized as the recorded
  defects — gross `2r^2` (`R-97600.2`: `\delta_p = r(1-2r)`, more than 3/4 of
  native at `p = 67`), net `0` (`R-99600.2`), one-prime subsidy `r(1-r)`
  of size `\sqrt Y` with the `s = 1/2` pole (`R-99440.3–.7`). All executed.
  New sharpenings (verified in `X-105000`): the loss fraction `1 - 2r_p >
  3/4` **iff `p > 64`** — 67 is the least rough prime above the threshold —
  and the fraction increases to 1 in `p`: no choice of factor prime tunes the
  defect away; the defect is positive for every `p \ge 5`, and the total
  quadratic overshoot available from `p \in \{2,3\}` is the constant
  `5/3 - 2^{-1/2} - 3^{-1/2} = 0.38220961\ldots`, bounded, against a
  divergent aggregate deficit.
* **(B) Exposure in deep alternating currents — exact schemes.**
  Conservation holds identically (the ledger `L-97400`; the sequential
  first-owner identity `L-99601.7`; the two-ended variant `L-100610`), and
  the exposure is precisely the one-sided control of the future-completed
  currents `(I - U_i)\prod_{h>i}(I - r_h U_h)`: the gate **FCHD67**
  (`L-99601.8` and §4 — defined *as* this demand), its aggregate `SEHC67`,
  and the current reductions `ODSB100604` / `DOBI100605` / `T-100611`.
  Status: open, RH-bearing. The degenerate wing is proved: the one-chain
  owner martingale carries the exposure with identically zero quadratic
  variation on squarefree cores (`R-99700`, owner-green-carleson: `D(n)=0`;
  "exact but degenerate"), every fixed logarithmic order fails (`R-99700`,
  adaptive-log-owner), and positive Green energy cannot orient the source
  (`R-99701`).
* **(C) Exposure in global cross-history / cross-core coupling — sign-split
  schemes.** Two positive parity channels are the minimal source-faithful
  realization of the sign character (`L-97501 §4`). Leafwise, fixed-
  orientation, and every fixed-depth variant are executed at the
  `X = 61841` witness and the fixed-depth counterexamples
  (`R-96650`/`R-96500` margin `> 17` canonical-only; `R-97301`; `R-97010`/
  `R-96501`; scalar-lift trade `R-97300.2–.4`). The surviving demand is
  global compensation across histories/cores — `CPSL67` / `GPC67` / the
  block-`L^2` cross-core estimate — each open and RH-bearing, and where
  quantified, RH-equivalent (block `L^2`: `RH \iff \mathcal E(X) =
  X^{o(1)}`, owner-degeneracy PROOF_PACKET §6; half-order window:
  `L-99823.4`).

**Exits from the axioms** (each named; none free): signed masses (breaks P;
no feasibility theory exists in-repo; one-channel signed carriage is blocked
by `L-97501 §4`); per-step factors above the exchange rate (breaks the free
cone; the `R-99440` macroscopic-subsidy class); non-`\sqrt{}` coordinates
(breaks N; `L-99704`: absolutely-summable damping deletes the detector;
`R-99820`/`R-99900`: the normalization cocycle moves coefficient and window
together — the price is invariant, `L-105001(d)`); abandoning atomwise
conservation (breaks C; blocked by knot identifiability, `M-105000` Lemma 0).

## 5. Corollary (adjudication of `R-99260 §2`, repair option 3)

`R-99260 §2` leaves exactly three repairs open, the third being "a direct
positive representation of the actual Möbius marginal". By Theorems A and B:
such a representation exists only together with an owned compensation source
of first-order mass at least `(Pi_{Q(j)}(Y) - 1)\,Q_Y(j) \sim 4C_j\sqrt Y\,
(\log\log Y - O(1))`, carrying the positive-real `s = 1/2` Mellin pole —
i.e. option 3 collapses into option 1 (a genuine sign theorem of the
FCHD67/IHR67 class). There is no third road. Full statement and proof:
`R-105000`.

## 6. What this theorem is and is not

* It is **unconditional, elementary, and machine-verified** mathematics about
  the method class practiced in this repository, axiomatized from the
  repository's own texts (all anchors in `M-105000`).
* It does **not** advance RH, refute RH, or bound any zeta zero.
* It does **not** claim the axioms capture every conceivable attack — only
  the hierarchical transport class as practiced. Any successor that breaks a
  named axiom should say which one; the exit list in §4 is the map.
* Falsifiers: an admissible scheme with sign-paid first-order delivery
  exceeding the Theorem A.1 budget (would refute the block-positivity
  argument); an admissible coordinate `G` in the class with
  `\sqrt p\,G(Y/p)/G(Y) > 1` (would refute `L-105001`); a bounded or
  Mellin-holomorphic carrier of the exposure (would refute the
  Landau/abscissa step in Theorem A.3 — i.e. exhibit a nonnegative function
  `\ge c\sqrt Y` with transform holomorphic in `\Re s > 0`, which is
  impossible; so this falsifier can only mean an error in the exposure
  lower bound itself).

```
budget inequality (A.1)                     PROVED EXACT
weight bound / price cap (L-105001)         PROVED EXACT
price divergence (A.2)                      PROVED (Mertens + interval bracket)
exposure lower bound + pole typing (A.3)    PROVED
trichotomy typing (B)                       PROVED AT STATED SCOPE
corpse reproduction                          VERIFIED (X-105000, S3-S4)
adjudication of R-99260 option 3            PROVED (R-105000)
Riemann Hypothesis                          UNPROVED / NOT ADDRESSED
```
