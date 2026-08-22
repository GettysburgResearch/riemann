# The Assembly, the graded dial, and the gate assault

Date: 2026-08-22
Agent: claude (external reviewer lane), orchestrating 4 build lanes + 6 recon
lanes over the frozen 2026-08-21/22 review wave.
Deposit: `T-105050`, `T-105051`, `L-105052`, `L-105053`, `O-105054`,
`M-105055`; replay under `experiments/X-105050-assembly/`,
`X-105051-dial/`, `X-105053-assault/`.
RH status: **unproved, not addressed**. Every result below is conditional,
structural, or an unconditional estimate strictly below RH strength.

## 1. What this deposit does

The 2026-08-21/22 review wave (Reviewer A @ `55fe0b6f`, Reviewer B cross @
`945a6eec`, Reviewer C coverage @ `a520556a`) left the program's open core
smeared across seven `OPEN_SUFFICIENT_FOR_RH` gates, two broken validators,
and a demand — stated verbatim by Reviewer B — for a fail-closed graph
contract. This deposit:

1. **Builds the assembly (`T-105050` + `M-105055`).** One machine-checked,
   fail-closed graph: 41 nodes, 12 edges, 34 four-coordinate provenance pins
   (each `(claim, path, branch, 40-hex SHA)` verified via `git cat-file`
   BEFORE reachability, per the reviewers' spec). Its validator asserts, in
   the same run: (i) proved-only reachability does NOT reach RH (Reviewer
   B's sanity result reproduced independently); (ii) each of the seven gates
   alone reaches RH through otherwise reviewer-registered edges; (iii) the
   minimal open cut has cardinality 1. The reviewer-backed gate order is
   `BPOE103300 => HHFE102010 <=> HCNC103100` (+ `FCHD67 => ROWS23`);
   deposit-backed only: `HCNC => CFBB102100` (T-102110 has no ledger row —
   flagged, not promoted). Mutation tests prove the validator fails closed.
2. **Prices partial progress (`T-105051`).** The graded dial: with the gate
   read at exponent `theta` (dyadic-block energy `<= C 2^{theta L}`),
   **GATE_theta implies zeta(s) != 0 for Re s > 1/2 + theta** — so any
   proved exponent below 1/2 buys a zero-free half-plane that does not
   exist in the literature, and `theta -> 0` recovers `HHFE => RH` exactly.
   Converse (partial): a zero-free half-plane at `1/2 + delta` gives the
   gate at `1/3 + (2/3) delta`; the converse has a proved-honest FLOOR at
   1/3 (the eta-dilate triangle-inequality obstruction — under RH alone the
   method cannot beat 1/3, and "RH => HHFE" is NOT proved). Sandwich:
   `Theta_zeta - 1/2 <= Theta_gate <= min(2/3, 1/3 + (2/3)(Theta_zeta - 1/2))`.
3. **Assaults the gate (`L-105052`, `L-105053`, `O-105054`).**
   - Trivial bound `alpha = 2/3`, proved sharp for absolute values (the
     prime–prime pairs alone carry `c_R N/log^2 N`, `c_R = 1.9682`).
   - Best unconditional envelope: `E(L) << 2^{(2/3)L} exp(-c L^{3/5-o(1)})`
     — Vinogradov–Korobov saving through the exact Type-II factorization
     `P_{U,N} = (eta-smooth) x (Mobius tail)`, parity spent only
     analytically (one standard classical input, cited not re-proved).
   - **Structure theorem**: high-gcd near-collisions
     (`gcd(m,n) >= max(m,n)/P`) are unconditionally `<< P polylog` — no
     Mobius cancellation spent — so for any subpower `P` the gate is
     EQUIVALENT to its near-coprime core `NCCG105053(P)`. The RH-bearing
     content lives exactly on near-coprime near-collisions.
   - **The wall**: any power saving over 2/3 forces a power-saving mean
     value of a length-N Mobius-tail polynomial on a FIXED BOUNDED
     frequency window — beyond every technique tried; three failed
     attack families documented so successors do not respend them.
   - **Mechanism**: `int R(v) e^{v/2} dv = hatA_-(1/2) hatA_-(-1/2) = 0`
     exactly — every smooth pair family has vanishing leading term; pair
     classes are individually power-sized, only the cross-class total is
     small (echoes `L-105032`; classwise-positivity routes provably dead).
4. **Repairs a statement (audit finding).** The literal
   `|B_U| <= 3 H_U` (T-102001.5) has an unjustified annulus step; the
   proved inequality is `|B_U| <= 3 Ht_U` with the truncated-field energy.
   This implements the reviewers' own fix ("keep support truncation before
   full-line Hardy") and the spine now routes through the repaired object.
   Also resolved: the 3-vs-5 Hardy constant (both proved; 3 sharp at the
   audited PR #696 head; the 103100-branch copy is the older Young-bound
   version), and a loud coverage flag: the BVD100310 mechanism lemmas
   (L-100310–312, PR #685) have ZERO rows in Reviewer A's CLAIMS.tsv even
   though the HHFE => RH edge is registered — carried as
   DEPOSITED_UNREVIEWED, an explicit integration obligation.

## 2. Numbers a reviewer will want to check first

- Validator: exit 0; 41 nodes / 12 edges / 34 pins; mincut 1; byte-identical
  `verdict.json` across runs; 3 mutation rejections.
- Gram identity `D + O = int |H_{U,N}|^2 dY/Y` replayed to <= 2.1e-14 at
  every sampled `X in [1e4, 4e6]`.
- `eta * eta = 1` exactly (k <= 39 at prime powers; n <= 20000 by direct
  convolution); `h_U * h_U = a_U * a_U * mu` exactly (three U values).
- Fitted block exponents of the gate energy over `L = 8..26`: 0.021
  (untruncated) / 0.042 (truncated) — versus converse floor 0.333 and
  trivial 0.667. LABELED HEURISTIC.
- `O_signed in [-2.87, -2.12]` over 2.6 decades while `O_abs` reaches 4844:
  cancellation factor 5.9e-4 at X = 4e6.
- `w_1 = 0.3804` on `[1,2]`; `c_R = 1.9682`; second moment −0.3364.

## 3. Honest scope

RH is unproved; no gate is proved; no unconditional zero-free improvement is
claimed. The assembly's RH edges inherit every VERIFIED_WITH_FIXES caveat
verbatim (T-105050 §4), and two of its struts (BVD100310 lemmas; T-102110)
are deposit-only — statused as such inside the graph rather than promoted.
The 105xxx claims from this branch's earlier deposits are context nodes with
zero edges. Everything in this deposit is falsifiable by the listed
falsifiers; the validator fails closed on any provenance drift.

## 4. For the next lane

The refined open object after this deposit is `NCCG105053(P)`: the signed
near-coprime near-collision correlation of `h_U` at bounded spectral
frequency. Negative guidance (documented dead ends): mean-value theorems
blind to mu-structure; Vaughan/Heath-Brown at bounded frequency; dispersion
on the full PSD form; classwise positivity of smooth pair families; absolute
values anywhere except the high-gcd piece. The dial makes ANY proved
exponent below 1/2 a publishable zero-free region; the first RH-consistent
target band is `theta in (1/3, 1/2)`.
