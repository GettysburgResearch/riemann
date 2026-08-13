# R-91655 — PR #450 correctly rejects `L-91659`, but its port and butterfly obligations do not bind the direct-row repair

Claim ID: `R-91655`  
Status: **EXACT REVIEW-SCOPE CORRECTION AND SUPERSESSION MAP**  
Created: 2026-08-14  
Reviewed proposal: PR #447 at `d44c45b3ececa878296914a49e49279b10a1f637`  
Reviewed report: PR #450 at `734040fba4d299256feb13aaeb45e60468ef6d1f`  
RH status: **unproved; the replacement proposal requires independent reconstruction**

## 1. The central review objection is accepted

`L-91659` defined the coordinatewise complement

\[
 \mathcal C_X=\mathcal N_X-\mathcal R_X
\]

and then inferred, from a table of heterogeneous imports, that

\[
 d_X^{\rm edge}+d_X^{\rm outer}+d_X^{\rm port}
 \in\mathcal F_X(\mathcal C_X).
\]

That inference was not proved. In particular, the file did not display one
simultaneous inequality for the **sum** of the proposed current rows against the
ordinary, radix-four and boundary coordinates remaining after `mathcal R_X`
was removed. PR #450 is correct on this point.

Accordingly:

```text
L-91659                                           SUPERSEDED AS ROOT PROOF
T-91652 Sections 5--6                             SUPERSEDED AS CONCLUSION STEP
R-91654/L-91661/L-91662 and the causal envelope   RETAINED
```

The replacement is `L-91663/L-91665/T-91653`.

## 2. The asserted absence of a `P_61/67` port adapter is false

PR #450 correctly observes that the `P_53` estimate

\[
 \prod_{p\le53}(1+p^{-1})<9/2
\]

cannot simply be reused after adjoining `59,61`. Indeed

\[
 \prod_{p\le61}(1+p^{-1})
 =\frac{399441300081868800}{86204059532560853}
 >\frac92.
\]

But the repository already contains the corrected `P_61/67` theorem
`L-91320-absorbing-59-and-61-makes-the-schur-port-dominate-every-rough-state-correction.md`.
It proves

\[
 \prod_{p\le61}(1+p^{-1})<\frac{14}{3}
\]

and retains the strict pointwise Schur reserve

\[
 \begin{pmatrix}
  \mathcal V_{P_{61}}&\mathcal B_{P_{61}}\\
  \mathcal B_{P_{61}}&\mathcal V_{P_{61}}
 \end{pmatrix}
 \succeq \frac19\mathcal V_{P_{61}}I_2.
\]

Thus:

```text
reuse of the P53 constant 9/2 at P61                  INVALID
existence of a P61/67 port estimate                    ALREADY PROVED
conservative routing through the old port architecture SEPARATE
```

The direct-row replacement does not use that port as a recursive capacity
coordinate; the theorem remains a current, one-use cross-check.

## 3. The butterfly baseline gates do not bind the direct-row repair

`L-91321` represents an interval seed by signed adjacent butterflies plus a
positive boundary atom. Its scope leaves baseline-center and boundary-placement
questions open. Those questions bind a proof using that literal decomposition.

The replacement uses the target-Hall identity of `L-91545`:

\[
 R(E)-R(O)=R(c)+B,
 \qquad c\ge0,\quad B\ge0.
\]

Here `R(c)` is already a positive canonical row and `B` a positive target-null
row bonus. No negative butterfly center or separate boundary atom is inserted.
The review obligations are real for the old realization and inapplicable to the
new one.

## 4. `L-90029` is now used in the correct direction

PR #450 correctly says that `L-90029` is conditional:

\[
 \Xi(d)\le\Omega_X
 \Longrightarrow
 \Gamma(d)\le w_X.
\]

`L-91659` did not prove the antecedent for its combined row. The replacement
`L-91663` displays, for every physical integer column `q`,

\[
 \Xi(d_X;q)
 =\Omega_X(q)-\Xi(R_{\rm ch};q)+\Xi(d_{\rm ch};q)
 \le\Omega_X(q).
\]

Only afterward is the positive radix-four telescope invoked.

## 5. A further score-scope correction not identified by PR #450

The exact same-index capacity identity does not by itself transfer the
continuum equality score `4 sqrt(X)` to the final finite row with absolute
loss. That transfer also needs the finite/continuum mismatch, quantization,
terminal-annulus and boundary ledger. The historical wording in
`L-91557/T-91561` compressed those interfaces too aggressively.

The replacement therefore does not claim

```text
finite native row score >= 4 sqrt(X) - absolute constant.
```

It proves the coefficient-one one-generation recurrence of `L-91665` and pays
one bounded analytic/discrete charge per factor-67 generation. The resulting
`O(log X)` debt is sufficient for the endpoint consumer and matches the exact
scope of `T-91101`.

## 6. Correct proof boundary

```text
PR #450 rejection of the L-91659 “consequently” step CORRECT
PR #450 claim that no P61/67 port estimate exists     INCORRECT
butterfly gates for the old realization                REAL
those gates for the direct Hall row                     NOT APPLICABLE
detail antecedent for L-90029                           DISPLAYED EXACTLY
constant all-depth score transfer                       NOT USED
new full composition                                    PROPOSED / REVIEW REQUIRED
Riemann Hypothesis                                      UNPROVEN
```
