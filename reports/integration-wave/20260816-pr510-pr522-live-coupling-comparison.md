# Comparative frozen-head review of PR #510 and recovery sibling PR #522

Review cutoff: `2026-08-16T02:06:58Z`  
Repository: `gfreund123/riemann`  
Main at cutoff: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`

```text
shared frozen parent PR #509: e01daee9cdfea35d2a7d2591f1df6c8080084119
PR #510 frozen head:          b596b1abae9213366aab4cf3f2c911ff8cfab725
PR #522 frozen head:          3e8949af3e23b8563bfbc0cf8846820cc6c66d76
PR #508 frozen head:          4ae97dffd1f76ed3244b8f3028560ffa80663caf
independent review #516:      2492bd48f8e2bafacfc04fc9237c06219b8c9bf8
```

The same claim numbers on PR #510 and PR #522 identify different files and different proofs. They are reviewed independently. Shared ancestry is context, not confirmation.

## Executive verdict

Both siblings make real progress on the bulk Volterra marginal and the formal one-row compiler. Neither constructs the complete live positive coupling required for the RH-facing endpoint theorem.

```text
shared finite/Volterra native split             VERIFIED WITH FIXES
bulk rank-one Hall incidence                    VERIFIED
PR #503 infinitesimal-causal firewall           VERIFIED
paired P61 source identity                      VERIFIED at whole-packet scope
anchored native occurrence -> stopped paths     BROKEN / UNPROVEN
complete Target-Lorenz all-parameter leaves     UNPROVEN / GAP (#516)
one coefficient signature and one quantizer     VERIFIED CONDITIONAL
q and 4q common-row assembly, including q<K     VERIFIED CONDITIONAL
native Y4 and endpoint arithmetic               VERIFIED CONDITIONAL

PR #510 L-91881 path coefficient                FALSE AS WRITTEN
PR #510 complete live coupling                  UNPROVEN / GAP
PR #510 replay                                  EMPIRICAL ONLY at full scope

PR #522 anchored path normalization             UNPROVEN / GAP
PR #522 complete live coupling                  UNPROVEN / GAP
PR #522 replay                                  EMPIRICAL ONLY at full scope
PR #522 root README rewrite                     REQUEST CHANGES / REPOSITORY HYGIENE

T-91880 on either sibling                       UNPROVEN / GAP
Riemann Hypothesis                              UNPROVEN
```

The first exact broken arrow on PR #510 is its stopped-path coefficient. PR #522 obscures the same normalization inside an undefined product of stopping and causal coefficients. Independently, both siblings still import the all-parameter Target-Lorenz theorem whose tail certificate failed review #516's inclusion audit.

## Reconstructed complete arrow

```text
full finite native Möbius row c_X
  -> exact ordinary capacity w_X
  -> exact radix-four capacity Omega_X
  -> exact literal benchmark J_Lambda(X)

split native arithmetic source
  -> anchored literal finite occurrences
  -> retained-cell Volterra occurrences
  -> signed retained-cell defect in a second ledger

bulk sector
  -> exact rank-one even/odd incidence
  -> exact residual L(X/s) p_s >= 0
  -> direct endpoint placement

anchored sector
  -> paired P61 stopping line
  -> exact path coefficients and orientation
  -> unique least rough owner
  -> complete Target-Lorenz leaf (nu, B, sigma)
  -> positive physical placement

anchored + bulk
  -> one common physical target
  -> I_anchored direct-sum Q_bulk
  -> one common thinning and explicit omissions
  -> one finite nonnegative row d_X

same d_X
  -> ordinary q total
  -> ordinary 4q total
  -> detail Xi_q = C_q - 2 C_4q
  -> all q>=2, including q<K
  -> native complement Omega_X-Xi(d_X) >= 0
  -> exact Y4 pairing
  -> finite dual
  -> prime-square moat
  -> Mellin-Landau consumer
  -> RH.
```

The bulk arrow reconstructs. The anchored arrow does not.

# I. Shared ancestry: what survives

## Exact hybrid native source

PR #509 and both siblings correctly separate the anchored literal finite Möbius source, the retained-cell Volterra source, and the signed finite/continuum defect. The defect is not promoted to positive source. The Volterra one-colour identity and exact finite comparison are coherent.

Verdict: **VERIFIED WITH FIXES**, mathematical type **ROUTE INFRASTRUCTURE**.

## Bulk rank-one coupling

At a retained bulk point all Möbius colours multiply the same positive packet `p_s`. With

\[
\pi_s(o,e)=\frac{a_oa_e}{P_+},\qquad
r_s(e)=a_e\frac{P_+-P_-}{P_+},
\]

one has exactly

\[
(\pi_s)_-=\Sigma^-_s,\qquad (\pi_s)_+ + r_s=\Sigma^+_s.
\]

Every edge cancels the identical packet, and the residual is `L(X/s)p_s>=0`.

Verdict: **VERIFIED** on the frozen positivity inputs.

## PR #503 firewall

Both siblings correctly retain the exact witness

\[
p_{1005}(14)-67^{-1/2}p_{15}(14)<0
\]

and do not apply an infinitesimal Volterra causal difference. Verdict: **VERIFIED / REFUTATION**.

## Paired P61 identity

`L-91362/L-92920` is valid as an equality of the complete paired source packet. It does not license multiplying a literal occurrence which already contains its full `k^{-1/2}` weight by the same rough factor a second time.

# II. First broken arrow: anchored path coefficients

## PR #510: exact double scaling

`L-91881` defines a literal occurrence

\[
a_\alpha=(km)^{-1/2}\log(X/(km))
\]

and then defines

\[
\omega_X=a_\alpha\prod_h(d_hp_h)^{-1/2}\prod_h\kappa_h(c_h).
\]

Take `m=1`, `k=67`, `X>67`. The native coefficient is already

\[
67^{-1/2}\log(X/67).
\]

The unique first rough owner is `(d,p)=(1,67)`, so the displayed path formula inserts a second `67^{-1/2}` and produces

\[
67^{-1}\log(X/67),
\]

not the native coefficient. A later nonnegative partition whose outgoing coefficients sum to one cannot repair the extra factor.

```text
L-91881.1 path coefficient       FALSE
anchored input marginal          NOT RECONSTRUCTED
L-91882 anchored Gamma_X         BLOCKED
```

## PR #522: normalization fork unresolved

PR #522 writes

\[
a_X(\omega)=a_X^{native}(n,k)\prod_{r\in h}\gamma_r(c)
\]

and asserts that the path weights sum back to the native coefficient. For `k=67`, the imported P61 stopping coefficient is `67^{-1/2}`. If it is included in `gamma`, the same double scaling occurs. If excluded, the theorem has not included the imported stopping coefficient and must identify where placement supplies it. No typed identity does so.

Verdict: **UNPROVEN / GAP**. A repair is plausible but is not present at the frozen head.

# III. Review #516 remains binding

Both siblings require

\[
B_\omega=R(U_\omega)-R(O_\omega)\ge0
\]

for all admissible real parameters and rows.

Review #516 proved that PR #508's `rounded_transc_std<long double>` replay did not establish directed inclusion for `sqrt` and `log`; the targeted probe produced singleton finite-binary intervals for irrational square roots. This refutes the certificate contract, not the Target-Lorenz inequality.

Therefore:

```text
compact leaf compiler                    retained conditionally
one p=67,y=15 diagnostic                 retained narrowly
all-parameter tail AVLT                  UNPROVEN / GAP
complete B_omega>=0 for every leaf       UNPROVEN / GAP
```

Neither sibling supplies a replacement inclusion-certified backend, exact primitive enclosures for every tail event, or a new analytic tail proof. Their dependency records omit review #516 and `R-93786`.

# IV. The fixed top packet is not actually omitted

Both siblings define retained bulk cells through `X-W-3`, put the entire complement in the anchored finite source, and then sum all anchored terminal paths into the final row. For example, `m=X-1`, `k=1` is anchored and has positive coefficient

\[
(X-1)^{-1/2}\log(X/(X-1))>0.
\]

Neither compiler splits

```text
anchored output source
  disjoint-union
bottom/top omitted source
```

before forming `Gamma_A`. Later both spend the fixed positive top omission to obtain

\[
5033X^{-3/2}-4452X^{-3/2}=581X^{-3/2}>0
\]

and charge omissions below one. The same source cannot be both in the output row and unused omission. Common thinning is not the fixed top omission.

```text
terminal omission ownership        UNPROVEN / GAP
terminal 581 X^(-3/2) reserve       unavailable for displayed d_X
native Y4 cost 60989                CONDITIONAL / NOT ESTABLISHED
```

# V. PR #510 separate verdict

Strengths: explicit source split, explicit bulk incidence, exact PR #503 enclosure, useful one-leaf diagnostic, correct formal coefficient/common-q/4q compiler, correct endpoint orientation, no forbidden benchmark bridge.

Failures:

1. `L-91881.1` double-scales literal rough occurrences.
2. The complete P61 path set and coefficients are not replayed.
3. The all-parameter Target-Lorenz tail remains unproved after #516.
4. Top/bottom anchored source is output and then charged as omitted.
5. `L-91882.2` uses undeclared bulk placement `E_s(dt)`.
6. Replay contains one bulk fibre, one leaf and a synthetic structural row, not the full coupling.

```text
L-91880  VERIFIED WITH FIXES
L-91881  FALSE AS WRITTEN
L-91882  UNPROVEN / GAP
L-91883  VERIFIED CONDITIONAL
L-91884  UNPROVEN / GAP
T-91880  UNPROVEN / GAP
X-91880  EMPIRICAL ONLY
```

# VI. PR #522 separate verdict

PR #522 is structurally cleaner: it imports the paired-orientation firewall, gives an explicit product incidence at the leaf, defines `P_s(dt)` for bulk placement, and has a stronger checksum/test surface.

It still fails because:

1. anchored stopping-factor normalization is unresolved;
2. the AVLT tail remains unproved after #516;
3. replay checks one bulk point and one anchored leaf, not all P61 paths or the tail;
4. top/bottom source is included in `Gamma_A^0` while later treated as omitted;
5. the lock imports PR #508/#497 but omits review #516 and `R-93786`.

```text
L-91880  UNPROVEN / GAP at anchored path map
L-91881  VERIFIED for bulk; UNPROVEN anchored
L-91882  VERIFIED CONDITIONAL
L-91883  UNPROVEN / GAP
T-91880  UNPROVEN / GAP
X-91880  EMPIRICAL ONLY
```

## Unexpected root README rewrite

PR #522 replaces the repository-wide README with its packet README. The root and standalone files are byte-identical and share blob

```text
f2d66e62226ab53b95be4c11e9cb578989535fd6
```

while PR #509's root README is

```text
f0d9e9aadfbd7b192b07e3bd0762a94e6e4da97e.
```

This unrelated change erases general repository navigation and must be reverted. Verdict: **REQUEST CHANGES / REPOSITORY HYGIENE**.

# VII. Downstream conditional results

Conditional on a valid `Gamma_X`:

- `I_anchored direct-sum Q_bulk` is one quantizer;
- one coefficient signature can control target, score, rows and boundary coordinates;
- ordinary `q` and `4q` totals can be formed on the same row before detail;
- inherited estimates cover all `q>=2`, including `q<K`;
- positive radix-four inversion yields ordinary feasibility;
- `12012+4+48972+1=60989<61000`;
- the finite-dual orientation is
  \[
  F_\Lambda(X)\le J_\Lambda(X)-\mathcal H(d_X).
  \]

These results are **VERIFIED CONDITIONAL** but not reached by either frozen producer.

# VIII. Earliest broken arrows

```text
PR #510:
literal native rough occurrence
  -/-> displayed stopped-path coefficient
  [FALSE: rough factor applied twice]

PR #522:
literal native rough occurrence
  -/-> proved normalized stopped-path marginal
  [UNPROVEN: stopping coefficient duplicated or omitted]

both:
complete Target-Lorenz leaf
  -/-> all-parameter nonnegative row bonus
  [UNPROVEN: #516 invalidated tail certificate contract]

both:
anchored source complement
  -/-> output row plus separately omitted top packet
  [UNPROVEN / double ownership]
```

# IX. Proposed repairs — not part of the verdict

1. Choose one normalization: route fully weighted literal occurrences deterministically, or start before the rough factor and let `L-91362` supply it. Do not combine both.
2. Prove an exact path-marginal identity for every anchored occurrence and replay all paths.
3. Rebuild the Target-Lorenz tail with an inclusion-certified backend or exact primitive enclosures; keep #516 in the lock until then.
4. Split `A_X=A_X^{output}\dotplus A_X^{bottom}\dotplus A_X^{top}` before physical placement and include only `A_X^{output}` in `Gamma_A`.
5. Replay actual P61 paths, weights, cutoffs and row margins—not one selected leaf.
6. Revert PR #522's root `README.md`; keep its packet front door under `standalone/`.

## Final conclusion

Neither PR #510 nor PR #522 establishes the live positive arithmetic coupling, the bounded native deficit, or RH. PR #522 is the better formal architecture, but it remains blocked at the same anchored arithmetic and Target-Lorenz interfaces and contains an unrelated root README rewrite.

\[
\boxed{\mathrm{RH}\text{ remains unproved.}}
\]
