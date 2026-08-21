# M-23812 — Consolidated review packet for weighted shell-tail carry transport

Methodology ID: `M-23812`  
Title: One frozen review spine, one explicit arithmetic hinge, and no inherited status inflation  
Status: **REVIEW-READY PROTOCOL — RH NOT CLAIMED PROVED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #238

## 1. Purpose

This file is the canonical review front door for the weighted shell-tail carry proposal. It supersedes the former two-contact and abstract `SGQB(K)` review orders as the preferred route, without deleting their historical files.

The proposal is complete as a **conditional composition** and incomplete as an unconditional proof. The sole new asymptotic assertion is `WSTS`; every other step has an explicit finite or elementary proof object on the branch or a frozen imported dependency.

```text
parabolic carry seed
-> exact fixed-ratio continuum shell order
-> finite shell profile + summable floor error
-> weighted prime upper-tail charge
-> exact zero-cost signed carry transport
-> in-support shell assembly
-> WSTS
-> prime ramp >= 4 sqrt(X)-X^o(1)
-> square-screw/Landau
-> RH.
```

## 2. Canonical files

Review these files in this order:

1. `claims/lemmas/L-23823-normalized-tail-and-fixed-ratio-shell-majorization.md`
2. `claims/lemmas/L-23824-zero-cost-weighted-prime-tail-transport.md`
3. `experiments/X-23821-weighted-shell-transport/verify.py`
4. `claims/lemmas/L-23825-finite-shell-profile-and-prime-sampling-remainder.md`
5. `claims/lemmas/L-23826-in-support-weighted-tail-charge-and-shell-sum.md`
6. `claims/theorems/T-23811-weighted-shell-tail-carry-proposal.md`
7. `claims/methodology/M-23811-weighted-shell-tail-review-protocol.md`
8. this consolidation file and the frozen TSV manifest.

Imported dependencies are frozen by commit rather than by mutable PR title:

```text
PR #248 head  5f2b25f89afbb90a3bc4ca6d40148f530303eb54
PR #202 head  d4c8e59f8f3f992a76fd48ad13bef78505dca7cc
```

Only the following imported statements are used:

```text
PR #248:
  parabolic seed objective;
  signed divisor-gradient consumer;
  ordinary-prime reduction with O(log^2 X) prime-power tail;
  exact prime-incidence block algebra.

PR #202:
  square-screw identity at square endpoints;
  square-sampling / one-sided Landau pole-exclusion transfer.
```

No status of either imported full proposal is inherited.

## 3. Exact theorem ledger

### 3.1 Continuum shell theorem

`L-23823` is now self-contained. It derives the reciprocal-cell formula, proves that

\[
J(\theta)=H(\theta)/\sqrt\theta
\]

is nondecreasing, and therefore proves

\[
H_c(\theta)\le0
\]

for every fixed ratio `c`. For the dyadic shell it proves the quantitative moat

\[
H_{1/2}(\theta)
\le-\frac{\log2}{5}\sqrt\theta
\qquad(0<\theta\le1/4).
\]

No prime theorem, source-rank assertion, or reflected positivity is used.

### 3.2 Finite weighted transport

`L-23824` proves that logarithmically weighted upper-tail domination is exactly the finite order needed for a zero-objective signed carry correction. For arbitrary residual `r`, the least one-boundary charge in this transport class is

\[
\mathcal B(r)
=\max_j\left(\sum_{i\ge j}(\log p_i)r_i\right)_+.
\]

`L-23826` pays the charge at the largest prime already in the endpoint, so no oversupport coordinate is introduced.

### 3.3 Finite shell reduction

`L-23825` proves

\[
r_X(q)=X^{-1/2}E(q/X)
+O\!\left(q^{-3/2}[1+\log(X/q)]\right)
\]

and the analogous shell formula. The floor error is absolutely summable in the logarithmically weighted prime norm. Stieltjes summation gives

\[
\sum_{z\le p\le X}(\log p)s_X(p)
=
\sqrt XH_{1/2}(z/X)+\mathcal E_X(z)+O(\log^2X).
\]

The first term is nonpositive; only the source-specific sampling remainder remains.

### 3.4 Shell assembly and RH deduction

`L-23826` composes the signed shell certificates on the dyadic chain. `T-23811` proves that `WSTS` implies

\[
\sum_{q=p^a\le X}
\frac{\Lambda(q)}{\sqrt q}\log(X/q)
\ge4\sqrt X-X^{o(1)},
\]

and then RH through the frozen square-screw/Landau interface.

## 4. Sole unproved theorem

For `Y=floor(X/2)`, put

\[
s_X(p)=r_X(p)-\mathbf1_{p\le Y}r_Y(p)
\]

and

\[
\mathcal B_X
=
\max_z
\left(
\sum_{z\le p\le X}(\log p)s_X(p)
\right)_+.
\]

The remaining theorem is

\[
\boxed{
\textbf{WSTS:}\qquad
\mathcal B_X\le C_\varepsilon X^\varepsilon
\quad\text{for every }\varepsilon>0.}
\]

A sufficient equivalent review target after the proved negative continuum term is retained is

\[
\sup_z(\mathcal E_X(z))_+=X^{o(1)}.
\]

This is RH-bearing. It is not described as routine, numerical, or implied by the classical PNT.

## 5. Component status for the reviewer

```text
L-23823 reciprocal-cell and shell calculus          PROPOSED COMPLETE
L-23824 weighted transport algebra                  PROPOSED COMPLETE
X-23821 rational transport replay                   EXACT FINITE CONTROL
L-23825 finite-to-continuum and Stieltjes reduction PROPOSED COMPLETE
L-23826 in-support assembly                         PROPOSED COMPLETE
T-23811 WSTS -> RH                                  COMPLETE CONDITIONAL
WSTS                                                OPEN / RH-BEARING
accepted proof of RH                                NO
```

A reviewer may promote or reject each component independently. Failure of `WSTS` or of its proposed future proof does not invalidate the exact continuum or transport lemmas.

## 6. Mandatory adversarial mutations

Reject a completion if it does any of the following:

```text
uses an unweighted residual tail;
reverses the transport order;
omits the destination endpoint-removal block;
pays a shell charge outside the current endpoint;
drops a prime or prime-square row;
replaces H_c by |H_c|;
takes absolute values of d[theta(t)-t] before adding the negative moat;
omits a dyadic shell;
uses only a classical absolute PNT error;
loses the fixed-ratio 2/3 Mertens/Farey mutation;
proves only an average-in-X or finite-ladder estimate;
imports the old two-contact, SGQB, Green-energy, or reflected-reserve hinge as though proved.
```

## 7. Acceptance conditions

A review may promote the full proposal only after all of the following are reconstructed:

1. the exact derivative and continuity claims in `L-23823`;
2. the raw and weighted amounts in one transport pair;
3. zero total prime-objective cost of the pair;
4. the finite floor-error exponent and its weighted summability;
5. the Stieltjes sign and endpoint conventions;
6. in-support shell telescoping;
7. a proof of `WSTS` at all sufficiently large endpoints;
8. the imported square-screw/Landau normalization at the frozen dependency head.

## 8. Publication discipline

The branch is suitable for adversarial review as a full proposal. It is not suitable for a public statement that RH has been proved. The correct summary is:

```text
complete review-ready architecture;
one explicit RH-bearing theorem open;
no accepted proof of RH.
```
