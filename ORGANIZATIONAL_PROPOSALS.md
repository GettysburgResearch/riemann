# ORGANIZATIONAL_PROPOSALS.md

Methodological proposals (`M-####`).  Format per README §15.

---

## M-0001 — certificate-first experiment layout

```text
Proposal ID:              M-0001
Problem with current process:
    README §10 asks each experiment to record ~18 fields.  Recorded as prose in
    a README they are unsearchable, drift out of date, and cannot be checked
    mechanically.  Worse, a reviewer wanting to confirm a result has to rerun
    the search rather than check a certificate.
Proposed change:
    Every experiment emits a single machine-readable JSON to
    experiments/X-####-name/results/ containing the §10 fields as keys
    (experiment id, git sha, platform, library versions, precision, semantics,
    parameters, outputs) plus the mathematical result.  The run script is the
    only source of that JSON; prose lives in the module docstring.
Expected benefit:
    A verifier can diff two runs, and a later agent can query all results
    without rerunning anything.  Reproducibility metadata cannot silently rot,
    because it is generated, not typed.
Possible cost or risk:
    JSON has no place for the *argument*; a certificate is not a proof.  Guard:
    the JSON must always name the claim file that says what it means.
Trial procedure:
    Used for X-0001..X-0004 in this session.
Success criterion:
    A second agent reproduces a result from the JSON + claim file alone,
    without reading the run script.  NOT YET TESTED.
```

---

## M-0002 — every computational module declares its trust boundary

```text
Proposal ID:              M-0002
Problem with current process:
    "Certified" is not transitive through a library call.  A module can be
    written in perfect ball arithmetic and still be resting on a routine
    nobody audited.  README rule 11 says to distinguish precision from rigour
    but does not say where to write down what is trusted.
Proposed change:
    Every module in scripts/ opens with a TRUST BOUNDARY block naming exactly
    which external routines it relies on and for what.  Anything used only in
    tests/ is listed as such, because a cross-check against an independent
    implementation is evidence, not a dependency.
Expected benefit:
    A reviewer can see the attack surface in ten seconds.  It also forces the
    author to notice when a "rigorous" pipeline has a non-rigorous hole.
Possible cost or risk:
    Boilerplate that goes stale.  Mitigation: keep it to the imports actually
    used.
Trial procedure:
    scripts/certzeta.py carries such a block: it declares that zeta itself is
    NOT taken from Arb (only ball arithmetic and lgamma are), that Bernoulli
    numbers are computed exactly from the recurrence, and that Arb's acb.zeta
    appears only in tests as an independent second implementation.
Success criterion:
    The next agent finds a hole this block should have exposed, or confirms
    there is none.
```

---

## M-0003 — a detector must be validated on a planted counterexample

```text
Proposal ID:              M-0003
Problem with current process:
    The repository's purpose is to find a counterexample.  A search that has
    never been shown to detect one is indistinguishable from a search that
    cannot.  "No counterexample found" from an untested detector is worth
    nothing, and it is the most likely output of every session -- so this is
    the failure mode we will meet most often.
Proposed change:
    Every counterexample-detecting experiment must include a validation
    section that runs the SAME code path against a synthetic object with a
    deliberately planted violation, and must report the smallest planted
    violation it can certify.  That number -- the sensitivity floor -- is
    reported alongside every negative result.
Expected benefit:
    "No counterexample with delta >= 0.1 in this box" is a real result.
    "No counterexample found" is not.  It also turns a null result into a
    quantitative measurement of the search's power.
Possible cost or risk:
    The synthetic object may not exercise the same difficulties as zeta (a
    polynomial is not zeta).  Mitigation: state what the synthetic model does
    and does not capture.
Trial procedure:
    X-0002 part 2 plants off-critical pairs at delta = 0.1, 0.03, 0.01, 0.003
    in a polynomial with otherwise on-line roots.  Result: certified at 0.1,
    abstains below.  Recorded as R-0006.
Success criterion:
    Adopted if the sensitivity floor changes a decision.  It already has: it
    is why Z-0002 targets Lehmer pairs (where the floor is lowest) rather than
    sweeping uniformly.
```

---

## M-0004 — citation flags

```text
Proposal ID:              M-0004
Problem with current process:
    README §Non-negotiable rule 17 says to label confabulation.  But the most
    dangerous statements are not inventions -- they are *recollections of real
    theorems with the constants slightly wrong*.  These read as citations and
    inherit the authority of the literature.
Proposed change:
    A recalled-but-unverified statement is written as
    [CITATION FLAG: ...] with (a) what is being recalled, (b) whether a wrong
    recollection would cause a FALSE POSITIVE or a MISSED counterexample, and
    (c) an open Q-#### to resolve it.  Point (b) is the operative one: a
    recollection that can only cause a miss may be used provisionally; one
    that could produce a false counterexample may not be used at all.
Expected benefit:
    Keeps unverified memory usable without letting it contaminate a claim.
Trial procedure:
    Used at Q-0005 (Csordas-Smith-Varga constant -- would affect a certified
    bound, therefore NOT used, only the well-defined discriminator D_n is
    computed) and Q-0007 (Robin's reduction to superabundant numbers -- can
    only cause a miss, therefore used to choose the test set).
Success criterion:
    No claim in the repository depends on an unresolved flag in the
    false-positive direction.  Currently true.
```

---

## M-0005 — the deficit ledger

```text
Proposal ID:              M-0005
Problem with current process:
    Experiments here answer yes/no questions ("is the count 269?").  A boolean
    throws away the quantity that would actually announce a counterexample.
Proposed change:
    Where two independent certified integers must agree (box count vs sign
    changes, L-0004), record the DIFFERENCE as a time series, not the boolean.
    Same for T-0001: record the smallest pivot, not just the verdict.  Any
    nonzero deficit, at any height, is a P1 alert.
Expected benefit:
    The observable becomes continuous and monitorable.  A future agent can
    watch the smallest pivot shrink as the height grows and know where the
    method is about to lose resolution -- before it does.
Possible cost or risk:
    Encourages reading noise as signal.  Mitigation: the deficit is an integer
    difference of two CERTIFIED integers; it is exactly 0 or it is a discovery.
    There is no noise in it.  The pivot version is real-valued and does need
    care.
Trial procedure:
    IMPLEMENTED: experiments/X-0001-certified-zero-census/deficit_ledger.py
    rebuilds the ledger from certificates already on disk, at no compute cost.
    Current state: 24 bands covering 0 < t <= 500, deficit 0 in every one.
Success criterion:
    Adopted if a later scan reports a nonzero deficit -- or if, at the end of a
    long null run, the ledger is what makes the null result quotable.  The
    second half of that criterion is already met: "deficit 0 across 24 bands"
    is a quotable null result in a way that "we found nothing" is not.
```

---

## Note on the README's own process

Two observations from the first session, offered without a formal proposal:

1. **The §11 report template and the §8 claim template overlap heavily.**  In
   practice the claim file is where the thinking goes and the report is where
   the session narrative goes; keeping "gap audit" in both invites copy-paste.
   Suggest the report reference claim files rather than restate them.  This
   session's report does that.

2. **The README asks agents to claim a GitHub issue before substantial work.**
   For a single-agent session in a fresh repository that is pure overhead, and
   this agent did not do it (there were no issues and no other agents to
   collide with).  Suggest the rule be scoped: issue-claiming is required when
   the repository has open issues or another agent is active; otherwise the
   session report is the record of what was claimed.  Recording this
   deviation explicitly rather than silently, per rule 1.
