# Riemann Hypothesis Multi-Agent Counterexample Project

## Mission

The purpose of this repository is to **resolve the Riemann hypothesis by constructing and rigorously proving a counterexample**.

The Riemann hypothesis asserts that every nontrivial zero \(\rho\) of the analytically continued Riemann zeta function satisfies

\[
\operatorname{Re}(\rho)=\frac12.
\]

A valid counterexample could take the form of:

- a rigorously certified nontrivial zero \(\rho\) with \(\operatorname{Re}(\rho)\neq \tfrac12\);
- a rigorously certified region, disjoint from the critical line, containing a nontrivial zero;
- a finite witness violating a theorem known to be equivalent to the Riemann hypothesis, with every hypothesis and computation certified;
- or another rigorously equivalent construction that disproves the hypothesis.

A floating-point approximation, suspicious numerical value, unexplained plot, or unverified software output is **not** a counterexample.

This is an ambitious objective. **We will achieve it.**

Agents should investigate boldly, develop unconventional abstractions, and pursue ideas that initially appear speculative or unlikely.

**Do not fear confabulation.**

In exploratory research, an imaginative false conjecture can be more useful than a cautious repetition of known ideas. Agents are encouraged to invent structures, lemmas, transforms, explicit formulae, zero-detection methods, equivalent criteria, certified algorithms, and possible counterexample constructions.

However, confabulation must be made visible. Every statement must be clearly labeled as proved, computationally observed, conjectured, speculative, or refuted. Creativity is encouraged; silently presenting invention as established fact is not.

The objective is not merely to generate interesting discussion. The objective is to produce an auditable and cumulative body of research in which:

- possible counterexamples are actively pursued;
- candidate off-critical zeros and equivalent witnesses are preserved;
- useful ideas are preserved;
- duplicated work is minimized;
- computational results are reproducible;
- numerical claims are rigorously certified when used as proof;
- claimed proofs are adversarially checked;
- false lemmas are identified quickly;
- failed approaches remain available to later researchers;
- organizational methods improve as the project progresses;
- no speculative claim is silently promoted to a theorem.

**Be imaginative in discovery and uncompromising in verification.**

---

## 1. Repository operating model

This repository has five primary coordination layers:

1. **README.md** — stable operating rules and project mission.
2. **GitHub Issues** — active tasks, ownership, discussion, and blocking dependencies.
3. **Agent reports** — append-only records of individual research sessions.
4. **Pull requests** — reviewable research contributions.
5. **CURRENT_STATE.md** — the current integrated understanding of the project.

Agents should not treat chat history as durable project knowledge.

Any result, idea, failure, candidate zero, equivalent-criterion witness, computational discovery, or organizational suggestion that may matter later must be written into the repository.

---

## 2. Required startup procedure

Before beginning a research session, every agent must:

1. Read this README.
2. Read `CURRENT_STATE.md`, if present.
3. Read `OPEN_PROBLEMS.md`, if present.
4. Read `CLAIMS.md`, if present.
5. Read `CANDIDATES.md` and `NEGATIVE_RESULTS.md`, if present.
6. Search open issues and pull requests for overlapping work.
7. Read the latest relevant files under `reports/`.
8. Select or create a GitHub issue for the task.
9. Announce an agent ID and claim the issue before substantial work begins.
10. Consider whether the current repository structure or coordination process can be improved.

If one of the foundational project-state files does not yet exist, agents may open an issue or pull request to bootstrap it rather than silently assuming its contents.

Agents may attack the full hypothesis, pursue a narrow analytic lemma, construct candidate counterexamples, investigate equivalent criteria, develop certified zero-finding algorithms, audit another agent’s argument, or reorganize existing ideas into a stronger framework.

---

## 3. Agent identity

Each research thread must use a unique, persistent agent ID.

Suggested format:

```text
<model-or-human>-<number>
```

Examples:

```text
gpt56-01
gpt56-02
claude-03
human-gideon
verifier-01
integrator-01
```

Every issue comment, report, commit, and pull request should identify the responsible agent.

Do not reuse another active agent’s ID.

When the same agent begins a substantially new independent attempt, it may either retain its existing identity or create a clearly related sub-identity:

```text
gpt56-01-a
gpt56-01-b
```

---

## 4. Task ownership

GitHub Issues are the authoritative task registry.

An issue should contain:

- a precise research question;
- the relationship to constructing or certifying a Riemann-hypothesis counterexample;
- known dependencies;
- relevant claim, lemma, candidate, or experiment IDs;
- expected deliverables;
- suggested verification methods;
- current owner;
- current status.

Before working on an issue, comment:

```text
CLAIMED BY: <agent-id>
STARTED: <UTC timestamp>
BRANCH: agent/<agent-id>/<issue-number>-<short-name>
APPROACH: <one-paragraph plan>
```

A claim should normally expire after 24 hours without an update. Another agent may then take over, but must preserve and reference the earlier work.

Multiple agents may work on the same issue when independent attempts are useful. They must use separate branches and explicitly mark the attempts as independent.

Agents are encouraged to open issues for:

- candidate off-critical zeros;
- certified zero-counting in off-line regions;
- equivalent-criterion witnesses;
- explicit-formula anomalies;
- analytic continuation and functional-equation checks;
- argument-principle or Rouché-theorem certification;
- Turing-method and zero-counting improvements;
- interval-arithmetic and ball-arithmetic implementations;
- tail bounds and truncation-error estimates;
- proof gaps;
- computational searches;
- adversarial verification;
- synthesis of multiple approaches;
- improvements to the project’s organizational structure.

---

## 5. Branch and commit conventions

Never push research directly to the default branch. The initial repository bootstrap is the only automatic exception.

Branch naming:

```text
agent/<agent-id>/<issue-number>-<short-description>
```

Examples:

```text
agent/gpt56-01/17-certified-offline-rectangle
agent/claude-03/22-check-li-coefficient-witness
agent/verifier-01/31-audit-lemma-L0012
agent/gpt56-04/44-argument-principle-search
```

Commit messages should use one of these prefixes:

```text
idea:
candidate:
proof:
experiment:
verification:
refutation:
report:
organization:
docs:
```

Examples:

```text
candidate: record off-critical zero enclosure from ball arithmetic
proof: establish tail bound for contour evaluation
experiment: scan rectangles through height 10^6
verification: independently reconstruct lemma L-0017
refutation: expose branch-cut error in logarithmic derivative
report: summarize failed Li-coefficient search
organization: propose certified-computation checklist
```

Commit partial work frequently.

A failed approach is still useful project information.

---

## 6. Pull request rules

Each pull request should address one coherent contribution.

A pull request must state:

- agent ID;
- issue addressed;
- exact contribution;
- relationship to the counterexample objective;
- claim IDs added or changed;
- dependencies;
- verification performed;
- numerical precision and certification method, when applicable;
- unresolved doubts;
- files that a reviewer should inspect first;
- any suggested improvements to the research process.

A pull request must not describe a result as a proof unless the complete proof is present in the repository.

Large speculative explorations should normally be submitted as research reports or candidate constructions rather than theorem claims.

Agents should not merge their own proof claims.

Proof-level contributions require review by at least one independent agent.

Claims purporting to construct a genuine counterexample or disprove the full Riemann hypothesis require at least two independent adversarial reviews before being marked verified.

Whenever practical:

- one verifier should reconstruct the analytic argument independently;
- one verifier should reproduce the certified computation using an independent implementation or library;
- and one review should actively search for precision, contour, branch, truncation, and equivalence errors.

---

## 7. Research claim classification

Every mathematical claim must have a stable identifier.

Use:

```text
D-####  Definition
Q-####  Open question
O-####  Observation
C-####  Conjecture
Z-####  Candidate off-critical zero or equivalent witness
L-####  Lemma
T-####  Theorem
X-####  Computational experiment
R-####  Refutation
M-####  Methodological or organizational proposal
```

Examples:

```text
Z-0003
L-0017
C-0009
X-0032
R-0004
M-0006
```

Every claim must have exactly one status:

```text
IDEA
EMPIRICAL
PARTIAL
PROPOSED
PROVED
INDEPENDENTLY_VERIFIED
REFUTED
SUPERSEDED
```

Meanings:

- **IDEA** — an informal possibility without substantial support.
- **EMPIRICAL** — supported computationally, but not proved or certified.
- **PARTIAL** — a rigorous result with incomplete scope.
- **PROPOSED** — a complete-looking proof, witness, or certification has been submitted but not independently verified.
- **PROVED** — the argument has passed an initial detailed review.
- **INDEPENDENTLY_VERIFIED** — independently reconstructed or reproduced by another agent.
- **REFUTED** — a counterexample, computation, or logical failure is known.
- **SUPERSEDED** — replaced by a clearer, corrected, or stronger formulation.

No result may jump directly from `IDEA` to `INDEPENDENTLY_VERIFIED`.

A numerical zero candidate remains a candidate until the existence of an actual nontrivial zero and its separation from the critical line have both been rigorously certified and independently reproduced.

---

## 8. Required structure for mathematical claims

Each candidate construction, lemma, or theorem file should contain:

```text
Claim ID:
Title:
Status:
Authoring agent:
Reviewing agents:
Created:
Last updated:
Dependencies:
Scope:
Related counterexample candidates:
```

Then include the following sections.

### Statement

A fully quantified, unambiguous mathematical statement.

### Definitions

All nonstandard terminology and notation, including the precise normalization of \(\zeta(s)\), \(\xi(s)\), zero-counting functions, contours, branches, and numerical enclosures used.

### Motivation

Explain how the claim could contribute to constructing or validating a Riemann-hypothesis counterexample.

### Proof or construction

Provide the complete argument or construction with no appeals to inaccessible chat history.

### Analytic domain audit

State explicitly:

- where each function is analytic or meromorphic;
- which poles and trivial zeros are present or excluded;
- which branch of every multivalued function is used;
- whether contours cross zeros, poles, branch cuts, or singularities;
- and whether all deformations of contours are justified.

### Dependency audit

List every earlier result used and the precise point where it is used.

### Gap audit

Deliberately search for:

- confusing an approximate zero with a proof that a zero exists;
- failure to prove that a candidate is nontrivial;
- failure to prove that the real part differs from \(1/2\);
- an interval enclosure that still intersects the critical line;
- unjustified use of analytic continuation;
- a contour passing through or too near a zero or pole;
- an incorrect zero count from the argument principle;
- branch-cut inconsistencies in \(\log \zeta\), \(\zeta'/\zeta\), powers, or roots;
- omitted truncation or discretization error;
- catastrophic cancellation or insufficient working precision;
- unproved tail estimates;
- non-rigorous library functions hidden inside a supposedly rigorous computation;
- circular dependence on the Riemann hypothesis;
- using an equivalent criterion without checking all of its hypotheses;
- numerical sign claims whose error interval contains zero;
- assuming a zero is simple without proof;
- double-counting symmetric or conjugate zeros;
- extrapolating finite searches to an infinite conclusion;
- confusing a discrepancy between implementations with a mathematical contradiction.

### Adversarial tests

Include small examples, edge cases, alternate formulations, independent precision levels, contour perturbations, symmetry checks, or computational tests that could expose an error.

### Remaining uncertainty

State any part of the argument about which the author is not fully confident.

### Suggested next attack

Describe the most promising way another agent could prove, strengthen, exploit, or refute the claim.

---

## 9. Counterexample candidate requirements

Every proposed counterexample should receive a stable `Z-####` identifier.

A candidate file should include:

```text
Candidate ID:
Status:
Proposing agent:
Object or construction:
Claimed failure mode:
Dependencies:
Verification status:
```

A valid candidate should normally fall into one of two forms.

### A. Direct off-critical zero candidate

The candidate proposes a region \(B\subset\mathbb{C}\), preferably with rational or rigorously enclosed endpoints, such that:

1. \(B\) lies inside the critical strip \(0<\operatorname{Re}(s)<1\);
2. \(B\) is disjoint from the critical line \(\operatorname{Re}(s)=1/2\);
3. \(B\) contains at least one zero of \(\zeta(s)\);
4. the zero is nontrivial;
5. all claims are proved exactly or by certified interval or ball arithmetic.

The candidate file must address:

#### Exact region

Define the rectangle, disc, contour, or other enclosure precisely.

#### Zero-existence certificate

Prove that the region contains a zero. Acceptable routes may include a rigorously implemented argument principle, Rouché theorem, interval Newton or Krawczyk method, certified zero count, or another complete analytic certificate.

#### Off-critical-line certificate

Prove that the entire enclosure is separated from \(\operatorname{Re}(s)=1/2\). A midpoint whose decimal expansion is not \(0.5\) is insufficient.

#### Nontriviality and singularity exclusion

Prove that the enclosure excludes the pole at \(s=1\), all trivial zeros, and every singularity invalidating the chosen argument.

#### Multiplicity and zero count

State whether the certificate proves existence, exact count, uniqueness, or multiplicity. Do not claim more than the method certifies.

### B. Equivalent-criterion witness

The candidate proposes a finite witness violating a criterion rigorously equivalent to the Riemann hypothesis.

The candidate file must address:

#### Exact criterion

State the equivalence theorem in full, including all quantifiers, domains, normalizations, and exceptional cases.

#### Exact witness

Define the integer, coefficient, inequality, sequence index, matrix, polynomial, or other finite object precisely.

#### Certified violation

Prove the violation with exact arithmetic or a rigorous enclosure whose sign or ordering is unambiguous.

#### Equivalence audit

Verify that the direction from the witnessed violation to the falsity of the Riemann hypothesis uses no missing hypothesis and no unproved assumption.

### Common verification plan

Every candidate must state exactly what mathematical and computational checks are needed before acceptance.

A decimal approximation alone is never a candidate certificate.

---

## 10. Computational result requirements

Computational evidence is welcome and may play a central role in discovering a counterexample.

However:

**Never call ordinary floating-point evidence a proof. Numerical computation becomes part of a proof only when every approximation, rounding error, truncation error, and analytic hypothesis is rigorously controlled.**

Every experiment must record:

- experiment ID;
- research question;
- exact code and commit SHA;
- command used;
- parameter ranges;
- software environment;
- operating system and architecture when relevant;
- compiler and library versions;
- numerical backend;
- precision and guard digits;
- rounding mode or interval/ball semantics;
- truncation and tail bounds;
- random seeds, when applicable;
- output or output digest;
- interpretation;
- limitations;
- associated issue and claim IDs.

Place experiments under:

```text
experiments/X-####-short-name/
```

Suggested contents:

```text
README.md
run.py
requirements.txt
results/
certificates/
```

Large generated files should not be committed unless genuinely necessary. Prefer scripts and compact certificates that regenerate or verify results.

Computational searches should aim not only to repeat known zero scans, but also to discover:

- candidate off-critical enclosures;
- inconsistencies between independent zero-counting methods;
- anomalous values in equivalent criteria;
- unstable regions revealing numerical weaknesses;
- improved contour or subdivision strategies;
- sharper tail estimates;
- identities that convert empirical anomalies into finite rigorous witnesses;
- failures of proposed lemmas;
- structures suggesting an existence theorem.

Whenever possible, include automated tests that distinguish between:

- raw floating-point output;
- high-precision but non-rigorous output;
- interval- or ball-certified output;
- heuristic interpretation;
- rigorous mathematical consequence.

A certified computation should ideally emit a compact proof certificate that an independent verifier can check without rerunning the entire search.

---

## 11. Agent session reports

At the end of every substantial session, create:

```text
reports/<agent-id>/<YYYY-MM-DD>-<issue-number>-<short-name>.md
```

Reports are append-only historical records.

Do not overwrite another agent’s report.

Each report must contain:

```text
Agent:
Issue:
Branch:
Starting hypothesis:
Approaches attempted:
New results:
Candidate counterexamples:
Certified computations:
Failed approaches:
Potential errors:
Files changed:
Claims affected:
Recommended next actions:
Organizational improvement ideas:
```

A report must distinguish among:

- proved facts;
- certified computational facts;
- non-rigorous computational observations;
- plausible conjectures;
- speculative ideas;
- candidate counterexamples;
- known failures;
- organizational suggestions.

Even when no mathematical progress was made, record what was attempted and why it failed.

Agents should also consider whether the difficulty encountered arose from the mathematics, numerical analysis, implementation, or deficiencies in the project’s coordination, indexing, file structure, review process, or division of work.

---

## 12. Handoffs between agents

When handing work to another agent:

1. Create or update the relevant issue.
2. Link the latest report.
3. Identify the exact unresolved step.
4. List the files and claims that must be read.
5. State what has already been tried.
6. State what would falsify the current approach.
7. State whether an organizational change would make continuation easier.

Recommended handoff format:

```text
HANDOFF FROM: <agent-id>
HANDOFF TO: any / <specific-agent-id>
CURRENT CLAIM OR CANDIDATE: <claim-id>
BLOCKING STEP:
FILES TO READ:
FAILED ATTEMPTS:
MOST PROMISING NEXT MOVE:
MAIN ANALYTIC OR NUMERICAL RISK:
POSSIBLE ORGANIZATIONAL IMPROVEMENT:
```

Do not use vague instructions such as “continue the proof” or “search higher.”

A useful handoff should allow another agent to begin productive work without reconstructing the entire history of the project.

---

## 13. Independent verification protocol

A verifier should begin without relying on the original author’s confidence.

The verifier should:

1. Restate the claim independently.
2. Reconstruct the proof from its explicit dependencies.
3. Check every quantifier, domain, and boundary case.
4. Check analyticity, poles, trivial zeros, contours, and branches.
5. Reproduce small cases and limiting cases.
6. Attempt to negate or strengthen the claim.
7. Check whether any dependency is circular or assumes the Riemann hypothesis.
8. Recompute numerical bounds using an independent implementation when practical.
9. Increase precision and perturb contours or subdivisions.
10. Verify all error, tail, and truncation bounds.
11. Record the first unsupported inference, if one exists.
12. Submit either:
    - a verification report;
    - a correction request;
    - a formal refutation.

Review comments should identify exact file paths and exact logical or computational steps.

“Looks correct” is not sufficient verification.

For a claimed direct zero counterexample, the verifier should independently reproduce:

- the exact enclosure;
- the proof that at least one zero lies inside;
- the proof that the enclosure is disjoint from the critical line;
- the proof that the zero is nontrivial;
- every supporting analytic estimate;
- every numerical error bound;
- and the absence of hidden assumptions equivalent to the desired conclusion.

For an equivalent-criterion witness, the verifier should independently reproduce:

- the exact criterion and normalization;
- the exact witness;
- the certified violation;
- the implication from the violation to falsity of the Riemann hypothesis;
- and all arithmetic or analytic dependencies.

---

## 14. Integrator role

One designated integrator maintains:

```text
CURRENT_STATE.md
CLAIMS.md
OPEN_PROBLEMS.md
CANDIDATES.md
NEGATIVE_RESULTS.md
```

Ordinary research agents should propose changes to these files through pull requests, but the integrator resolves conflicts and maintains consistent status classifications.

The integrator does not decide mathematical truth by authority.

The integrator records the strongest status justified by repository evidence.

The integrator should periodically:

- merge accepted reports;
- close duplicated issues;
- identify conflicting claims;
- request independent reviews;
- mark stale tasks;
- update the dependency graph;
- create synthesis issues;
- identify promising candidate counterexamples;
- summarize major failed directions;
- review organizational proposals;
- improve templates and repository structure where justified.

The integrator may create dedicated issues for organizational improvements suggested by agents.

---

## 15. Improving the research process

The project’s organizational system is itself experimental.

All agents are invited to propose better ways to:

- coordinate parallel research;
- reduce duplicated effort;
- preserve partial insights;
- represent dependencies;
- rank promising approaches;
- detect contradictions;
- conduct adversarial review;
- divide long arguments into verifiable units;
- share computational artifacts and certificates;
- track candidate zeros and equivalent witnesses;
- summarize large bodies of work;
- allocate agents dynamically;
- improve communication between research threads.

Organizational proposals should use `M-####` identifiers when substantial.

A methodological proposal should include:

```text
Proposal ID:
Problem with current process:
Proposed change:
Expected benefit:
Possible cost or risk:
Trial procedure:
Success criterion:
```

Agents should not wait until the end of the project to suggest improvements.

While working on the mathematics, continuously consider how the group itself could reason, communicate, verify, and collaborate more effectively.

Useful organizational experiments may be tested on a limited set of issues before becoming project-wide rules.

The README is not immutable. Changes may be proposed through pull requests and adopted when they improve the project’s ability to construct and verify a counterexample.

---

## 16. Recommended repository structure

```text
README.md
CURRENT_STATE.md
OPEN_PROBLEMS.md
CLAIMS.md
CANDIDATES.md
NEGATIVE_RESULTS.md
NOTATION.md
LITERATURE.md
ORGANIZATIONAL_PROPOSALS.md

claims/
  definitions/
  observations/
  conjectures/
  candidates/
  lemmas/
  theorems/
  refutations/
  methodology/

experiments/
  X-0001-example/

certificates/

reports/
  gpt56-01/
  gpt56-02/
  claude-01/
  verifier-01/
  integrator-01/

scripts/
tests/

.github/
  ISSUE_TEMPLATE/
  PULL_REQUEST_TEMPLATE.md
```

---

## 17. Non-negotiable rules

1. Never conceal uncertainty.
2. Never call ordinary floating-point evidence a proof.
3. Never call a decimal approximation to a zero a counterexample.
4. Never rely on inaccessible chat context.
5. Never silently delete failed work.
6. Never modify another agent’s branch without coordination.
7. Never merge a claimed major theorem or counterexample without independent review.
8. Never assume the desired conclusion inside an intermediate lemma.
9. Never treat eloquence, length, confidence, or model identity as evidence.
10. Always preserve exact statements and dependencies.
11. Always distinguish numerical precision from numerical rigor.
12. Always state all analytic domains, singularities, contours, and branch choices.
13. Always distinguish a suspicious value from a certified zero enclosure.
14. Always distinguish a finite search from a universal theorem.
15. Always record potentially useful false starts.
16. Always remain open to unconventional ideas.
17. Do not fear confabulation, but label it.
18. Always suggest organizational improvements when they could help the group.
19. Always leave the repository more understandable than you found it.

---

## 18. Initial instruction for every new agent

Use the following instruction when starting a new research thread:

```text
You are one researcher in a coordinated multi-agent project whose goal is
 to resolve the Riemann hypothesis by constructing and rigorously proving
 a counterexample.

The goal is ambitious, and we will achieve it.

Do not fear confabulation. Generate bold hypotheses, unusual analytic
constructions, new transforms, speculative lemmas, equivalent criteria,
and unconventional certified-computation strategies. However, clearly
label everything as proved, certified computational, empirical,
conjectural, speculative, or refuted.

Before doing mathematical work:

1. Read README.md and all available project-state files, relevant open
   issues, relevant pull requests, and recent reports.
2. Choose or create one precise GitHub issue.
3. Assign yourself a unique agent ID.
4. Claim the task in the issue.
5. Work on a separate agent branch.
6. Clearly distinguish proof, partial proof, certified computation,
   ordinary computation, conjecture, speculation, candidate, and refutation.
7. Preserve failed approaches.
8. Pursue a counterexample directly or develop mathematical and certified
   computational tools that could enable one.
9. End the session with an agent report and a reviewable pull request.
10. Include ideas for improving the research organization itself.
11. Never call ordinary floating-point evidence a proof.
12. Do not claim resolution of the Riemann hypothesis unless every analytic
    dependency, zero-existence claim, off-critical-line separation, error
    bound, and equivalence step is explicitly established in the repository.
13. Be imaginative in discovery and uncompromising in verification.
```

---

## 19. Current project objective

The project’s objective is to construct a genuine counterexample to the Riemann hypothesis and prove rigorously that it is a counterexample.

The immediate objectives are to:

- discover candidate off-critical zeros or finite equivalent witnesses;
- develop certified methods capable of proving that a zero exists in a specified region;
- prove separation of candidate regions from the critical line;
- investigate equivalent criteria that may admit finite, exact counterexamples;
- derive lemmas that convert numerical or symbolic structure into rigorous analytic consequences;
- test and refute weak constructions rapidly;
- preserve all useful negative and positive results;
- improve the organization of the multi-agent research process;
- and build a reliable, cumulative, adversarially reviewed path toward the final counterexample.

**The goal is ambitious. We will achieve it.**
