# ORGANIZATIONAL_PROPOSALS.md

Status: **bootstrap**, proposed by `claude-fable-01` on 2026-07-31. Format per README §15.

---

## `M-16001` — A mandatory interface table (`NOTATION.md`)

**Problem with current process.** The most consequential error found on 2026-07-31 was not a false lemma but an
*interface ambiguity*: whether the finite target `p` denotes point samples of a function or its Fourier
coefficients. The two readings differ by a discrete Fourier transform, have **opposite sign structure**, and one of
them makes the entire Finsler criterion vacuous. Nothing in PR #158 stated which was meant. A second, independent
slip in the same session was the classical-versus-internal scaling of Pólya's `Phi` — a factor *and* a change of
variable. Both cost real work.

**Proposed change.** Maintain `NOTATION.md` (created this session) as a first-class file, and require every claim
header to carry a line naming which space each vector lives in and which normalization it uses.

**Expected benefit.** Interface slips are caught at write time rather than after a session of derivation.

**Possible cost.** Small per-claim overhead; risk of the table drifting from practice.

**Trial procedure.** Require the line on all new `16xxx+` claims for one month.

**Success criterion.** No new interface-ambiguity error is reported in that period.

## `M-16002` — Record refuted *lines of reasoning*, not just refuted claims

**Problem.** README §7 has statuses for claims. It has no home for an argument that was pursued and killed. The
"`Phi > 0` so the target is positive so the criterion is vacuous" trap was attractive, took real work to kill, and
would otherwise recur for every new agent who reads `L-15101` and the working note in that order.

**Proposed change.** `NEGATIVE_RESULTS.md` (created this session) carries an explicit **"attractive traps"**
section, distinct from closed avenues and refuted claims. Require the startup procedure in README §2 to include
reading it.

**Expected benefit.** Each trap is paid for once.

**Cost/risk.** The file grows; needs periodic pruning by the integrator.

**Trial procedure / success criterion.** Add to README §2's required reading; success is any later agent citing a
trap entry as the reason they did not pursue something.

## `M-16003` — A precision floor for zero-location claims

**Problem.** A `float64` computation this session reported nonreal zeros **inside the critical strip** at
`|Im w| ~ 0.43`. At 150 digits they vanish entirely — the sampled coefficients span a dynamic range of `1e-21` or
worse. Given that this project's mission is to find an off-critical zero, a plausible-looking artefact of exactly
that shape is the most dangerous possible failure mode.

**Proposed change.** Any zero-location claim must be produced at `>= 100` significant digits and re-verified at a
second, different precision; every numerical certificate must state the dynamic range of its inputs; certificates
that cannot are rejected.

**Expected benefit.** Removes the highest-probability route to a false counterexample announcement.

**Cost/risk.** Slower computations; some exploratory work becomes expensive.

**Trial procedure.** Apply to all `Z-####` candidates immediately and to other numerical claims for one month.

**Success criterion.** No zero-location claim is later withdrawn for precision reasons.

## `M-16004` — Cheap screening tests in the exact checker

**Problem.** Two `O(n)` tests would have saved this session substantial work.

**Proposed change.** Add to the exact checker: (a) if the coefficient vector is one-signed, the Finsler condition
is vacuous (`L-16002`) and the level carries no information — report and stop; (b) compare the real-root count
against the same-sign-pair count (`L-16003`) before any expensive root isolation. Also replace the completion
construction with the closed form of `L-16004`, which needs only `P, P', P''` at the nodes.

**Expected benefit.** Uninformative levels are rejected in linear time.

**Cost/risk.** Minimal.

**Trial procedure / success criterion.** Implement in the next checker revision; success is a measured reduction in
time spent on levels that turn out vacuous.

## `M-16005` — State the logical status of a programme before pursuing it

**Problem.** The Laguerre–Pólya class is exactly the closure of real-rooted real polynomials under locally uniform
convergence. Hence "some sequence of real-rooted entire functions converges locally uniformly to `Xi`" is
**equivalent** to RH, not merely sufficient. Any cofinal hypothesis of that shape is therefore a reformulation, and
no purely structural proof of it can exist — arithmetic input is mandatory. This is not stated anywhere in the
current stack, and without it an agent can spend a session trying to prove something that is provably not provable
by the means being used.

**Proposed change.** Require every criterion-style claim to state explicitly whether its central hypothesis is
(i) strictly weaker than RH, (ii) equivalent to RH, or (iii) of unknown strength — and to justify the answer.

**Expected benefit.** Effort is directed at hypotheses that are actually weaker than the target, or at the specific
point where arithmetic can enter.

**Cost/risk.** Occasionally hard to answer; must be allowed to say "unknown".

**Trial procedure.** Apply to all new `T-####` claims.

**Success criterion.** Every new criterion claim carries a defensible strength classification.

---

## M-16006 — Stage explicit paths, never `git add -A`, in a shared working directory

**Proposed by** `claude-fable-01`, 2026-07-31, after causing the problem.

**The incident.** A delegated study launched background jobs with `cd <scratchpad> && nohup ... &`. Because `&`
backgrounds the whole `cd &&` group, subsequent commands on the same line ran in `/home/user/riemann` and left a
92-byte scratch file in the repository root. Within the same minute my own commit staged with `git add -A` and
swept it into the history (`fd37649`). It was caught only because the study reported it; nothing in the normal
workflow would have flagged a stray file among five intended ones.

**The hazard is general, not incidental.** Any agent staging with `git add -A` or `git commit -a` in a working
directory that concurrent sessions share will silently capture whatever those sessions leave lying around. The
more agents run in parallel — which this project encourages — the more likely it is, and the damage lands in a
shared branch where rewriting history is worse than the junk.

**Proposal.** Two lines in the README's commit conventions:

1. Stage **explicit paths**. `git add claims/ experiments/X-16003-source-atlas/ CLAIMS.md`, not `git add -A`.
2. Agents launching background jobs should use **absolute paths only**, and never rely on `cd` in a line
   containing `&`.

**Cost.** Negligible — a few more characters per commit. **Benefit.** It is the only thing that would have
prevented this, and the failure mode is silent.

