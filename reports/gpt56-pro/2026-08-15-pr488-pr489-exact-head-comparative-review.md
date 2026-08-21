# Exact-head comparative review of PR #488 and PR #489

**Review type:** review-only; no proposal file edited  
**Review date:** 2026-08-15  
**Repository:** `gfreund123/riemann`  
**Method:** lightweight exact-head reconstruction, dependency-path inspection, and finite algebra checks only  
**Riemann Hypothesis status:** **unproved**

## Frozen objects

```text
superseded historical provenance only:
PR #481 reviewed head: f41bbd7608cc70bc2a8002d43ef99b5e35977968
PR #468 reviewed head: 8085903e190589e3117a0c7494fb1150c2222401

live comparison:
PR #488 head: 9acd381fa168db02a03646ab16851daebbf4d0fd
PR #489 head: 0bb487c8a0782f601be0a3041743b357ad93726a
PR #489 base: 9acd381fa168db02a03646ab16851daebbf4d0fd
```

The exact GitHub genealogy is therefore clean: PR #489 is one commit stacked directly on the requested PR #488 head. All findings below are head-specific. Nothing is projected backward onto an earlier head or forward onto an unpublished successor.

A minor publication-hygiene note is worth preserving: the PR #488 body still contains an older publication line naming `57a9afee...`, while GitHub's live PR head is the requested `9acd381f...`. This review uses the live metadata and exact requested head.

---

# 1. Superseded historical provenance

These two notes are **not verdicts on later heads**.

## PR #481 at `f41bbd7...`

The frozen review found that the successor materially repaired the earlier weighted-child, normalization, small-column, activation-knot, and strict-reserve defects. It nevertheless requested changes because the concrete fully corrected current/full-child native-capacity identity and hereditary descendant closure had not yet been reconstructed at that head.

This is retained only as provenance for why later packets introduced the common-parent compiler, one-shot terminalization, first-owner restriction, and explicit native-slack ledgers.

## PR #468 at `8085903...`

The frozen review found a publication mismatch: the summarized complete `L-91696/T-91697` package was not present at that reviewed head. The live files then available contained the Target-Lorenz optimizer and determinant reduction, but not the advertised complete determinant and endpoint composition.

This is retained only as provenance. It says nothing about descendants or later republished artifacts.

---

# 2. Executive verdicts

```text
shared dependency spine:
CONDITIONAL PASS AT THE DECLARED FROZEN-INPUT SCOPE
no new algebraic or normalization defect found by the lightweight checks;
large analytic Hall/profile, all-column, and endpoint inputs were not rerun.

PR #488 one-shot / zero-port closing layer:
PASS — NO CHANGES REQUESTED TO THE CLOSING IMPLEMENTATION
on the frozen shared inputs, the one-shot construction avoids the recursive
capacity-substitution gate and has a coherent single-owner ledger.

PR #489 recursive / portful closing layer:
REQUEST CHANGES — GATE B IS NOT ESTABLISHED
L-92881.1 supports a labelled current/child source partition, but L-92881.2
upgrades actual child responses to full child capacities without the additional
positive capacity decomposition required by the inherited compiler. L-92883
then treats the resulting coordinatewise reserve as one positive source packet
of mass <3020, which is not established for the signed retained-cell mismatch.
```

The targeted conclusions are:

1. `L-92881` does **not** presently establish the full labelled source-to-**capacity** identity used by the recursive proof. Its current/child source partition is supported; its complete child-capacity reservation is the broken arrow.
2. The scaling from the mass-one `T-91312` envelope to `L-92884.3` is mathematically correct **once HTR is supplied**. The exact head contains `L-91751`, which supplies HTR, but `L-92884` does not cite or lock that theorem explicitly.
3. Same-index placement really does preserve the numerical detail vector and hence the `Y_4` pairing.
4. PR #488 gives every used reserve exactly one root owner and uses no matrix port. PR #489's intended direct-sum port separation is sound in form, but `L-92882` still needs an explicit source-disjoint partition of the branch port shares to rule out multiple uses of the one uncolored root port.

---

# 3. Shared dependency spine

## 3.1 Exact genealogy and reachable objects

The following load-bearing objects are reachable at both reviewed heads through PR #488's ancestry:

```text
L-91658  same-index complete-datum functor
L-91732  actual target-mass child normalization
L-91733  retained-cell all-column mismatch theorem
L-91750  common-parent typed compiler
L-91751  hereditary positive-packet class and HTR
L-91753  one-shot terminalization
L-91754  exact measurable whole-cell Hall integration
L-91755  one-shot port-free total row
L-91756  one-shot root slack <61000
L-91840  restriction before quadrature
L-91841  first-owner-restricted child operators
L-91842  source-partitioned aggregate port theorem
L-91843  sequential source ledger
L-91844  direct Y4 cost compilation
T-91312  conditional subcritical target-mass consumer
```

PR #489 adds `L-92880--L-92884/T-92880`; it does not replace the inherited one-shot route.

## 3.2 First-owner and target-mass bookkeeping

`L-91841` supplies the exact disjoint projections

\[
R_\infty+\sum_jR_j=I,
\qquad
R_iR_j=0\quad(i\ne j),
\]

and defines the restricted child operator

\[
U_j^{(1)}=U_{p_j}R_j.
\]

This is the correct source-level answer to multiple rough-prime divisibility: an atom has one least-prime owner, not one copy in every active prime branch.

`L-91732` independently gives both usable target-mass interfaces:

\[
\sum_i\alpha_i m(B_iP)<\frac18m(P)
\]

for one global prime list, and

\[
P=P^{\rm cur}+
\sum_b\beta_bU_b\widetilde P_b,
\qquad
m(\widetilde P_b)=m(P),
\qquad
\sum_b\beta_b<\frac18
\]

for actual-mass grouped children. The normalization and the coefficient budget use the same SHARP target mass.

**Verdict:** verified at the finite positive-linear level.

## 3.3 Same-index placement and the `Y_4` pairing

This targeted point passes.

`L-91658` explicitly distinguishes normalized placement `U_m` from arithmetic scaling. Normalized placement changes endpoint and provenance labels but leaves the numerical packet coordinates unchanged:

\[
(q,\Gamma,\Xi,J,T,S,E,b)_X(U_mP_Y)
=(q,\Gamma,\Xi,J,T,S,E,b)_Y(P_Y).
\]

Consequently

\[
\Delta_X(U_mP_Y)=\Delta_Y(P_Y),
\]

and, for a numerical slack vector,

\[
\langle Y_4,U_ms\rangle=\langle Y_4,s\rangle.
\]

This is compatible with `L-91378`, because `Y_4` pairs against the same integer detail coordinates. There is no hidden `q\mapsto mq` physical-column dilation in this functor.

**Verdict:** verified exactly. No change requested.

## 3.4 Does `T-91312` scale to `L-92884.3`?

Yes, conditionally, and the missing condition is identifiable.

`T-91312` defines the envelope on mass-one packets and assumes positive homogeneity. Once HTR holds, it yields a constant `C_+` with

\[
\Delta(P)\le C_+m(P)
\]

for every positive packet in the hereditary class.

The actual-mass normalization of `L-91732` gives

\[
m(\widetilde P_b)=M_X<3020,
\qquad
\sum_b\beta_b<\frac18.
\]

Therefore

\[
\sum_b\beta_b\Delta(\widetilde P_b)
\le
C_+M_X\sum_b\beta_b
<
\frac{3020}{8}C_+.
\]

So the numerical scaling in `L-92884.3` is correct.

However, `T-91312` is explicitly a conditional consumer whose HTR entry is open in that theorem. The reviewed exact head also contains the later `L-91751`, which proves an all-coordinate hereditary reset and even a direct terminalization bound. `L-92884` should therefore cite and freeze `L-91751` explicitly. Citing only `L-91736/T-91312` leaves the formal dependency list incomplete, because `L-91736` itself says the positive causal identity and source ownership must be reconstructed.

**Verdict:** algebra verified; dependency crosswalk needs a small repair. This is not the primary blocker in PR #489.

## 3.5 Shared analytic boundary

The following large inputs were deliberately not rerun:

```text
factor-67 finite Hall/prefix/profile theorem;
all-column adjacent-error and terminal estimates;
positive quantizer analytic realization;
prime-square moat;
one-sided endpoint inequality;
Mellin pole audit and Landau one-sign theorem.
```

The static comparison found no new normalization contradiction in those shared interfaces. Their truth remains a frozen independent-reconstruction obligation.

**Shared-spine verdict:**

\[
\boxed{
\text{CONDITIONAL PASS AT THE DECLARED FROZEN-INPUT SCOPE.}
}
\]

---

# 4. PR #488 — one-shot, empty recursion, zero port

## 4.1 Why the one-shot implementation avoids the hard recursive substitution

The inherited compiler `L-91750` proves an exact typed identity in terms of the **actual child packet responses**. Its radix-four coordinate is

\[
\Omega_X
=
\Xi(P_X^{\rm cur})+e_X+
\int a(b)U_b\Xi(P_b),
\qquad e_X\ge0.
\]

The same file explicitly warns that replacing the displayed child responses by their full declared capacities would require an additional sign theorem. It writes the candidate reserve as

\[
e_X+
\int a(b)U_b[\Xi(P_b)-\Omega(P_b)]
\]

and says the preferred one-shot closure avoids that convention.

PR #488 does exactly that. It never discards the actual positive child-coloured rows and then asks for replacement rows. All colours are retained inside one finite total row. Thus the one-shot endpoint argument needs only

\[
\Xi(d_X)\le\Omega_X,
\]

not an identity reserving another copy of every child's full packet capacity.

This distinction is decisive. It is why the defect identified below in PR #489 does not propagate back into PR #488.

## 4.2 Labelled source ownership

The closing packet has concrete single-owner devices:

- `L-91840` restricts the signed defect measure before cell integration;
- `L-91841` gives exact first-owner disjointness;
- `L-91754` performs one exact measurable Hall integration and one global quantizer;
- all causal children remain internal labels of the same final row;
- the exported child family is empty.

The one-shot specialization therefore has

\[
\sum_b\beta_b=0.
\]

No root source is recursively reused.

## 4.3 Zero-port claim

The zero-port specialization is coherent, not a missing payment.

`L-91755` constructs the physical nonnegative row directly and does not invoke the coloured state completion or Schur-complement realization for which the auxiliary matrix port was introduced. Mismatch and collar terms are paid as analytic capacity comparisons; omissions and thinning remove positive root source. Therefore the auxiliary matrix coordinate is outside the controlling producer.

`L-91842` separately gives a portful aggregation firewall, but its PR #487/#488 specialization is

\[
D=P=0.
\]

Since the one-shot route does not use that state-completion operation, there is no positive port demand waiting to be assigned.

**Owner:** none is needed because the coordinate is absent.  
**Child port:** zero.  
**`Y_4` cost:** zero.

## 4.4 Root reserve ownership and direct `Y_4` cost

The final row is thinned once and tested once against all physical columns. The external root slack is never transferred to a child. `L-91844` names the complete one-shot slack classes:

```text
thinning;
nonterminal retained-cell/collar comparison;
terminal comparison;
omissions.
```

Terminal, taper, and base vectors retained in the current row are not also charged as slack. No port term is present.

The retained constants are internally consistent under lightweight arithmetic. At `X=10^12`, the worst endpoint of the stated large-`X` range:

```text
square-root thinning estimate   approximately 11788.66 < 12012
nonterminal bound               approximately 3.307 < 4
terminal bound                  4452 * 11 = 48972
omission allowance              <1 on the frozen estimate
sum                             60989 < 61000
```

The inequalities `67^{-1/2}<1/8` and

\[
61000<2(4\sqrt X-3)
\]

also hold with enormous margin at `X=10^12`.

## 4.5 Scope of the verdict

The recursive form displayed in `L-91843.3` should not be used as independent proof of PR #489's full-capacity replacement. The one-shot specialization is different:

\[
\Omega_X=\Xi(d_X)+r_X,
\qquad r_X\ge0,
\]

with no exported child capacities. It is supported by the actual final row and direct all-column comparison.

The review therefore reaches:

\[
\boxed{
\text{PR \#488 ONE-SHOT/ZERO-PORT CLOSING LAYER: PASS.}
}
\]

No change is requested to this closing implementation. `T-91840` remains a candidate composition on frozen analytic inputs, not an independently accepted proof of RH.

---

# 5. PR #489 — recursive, full-child capacity reservation, portful cross-check

## 5.1 Gate A

`L-92880` uses one target Hall flow for target, score, and every declared component row. The monotonicity directions are consistent:

- the score-per-target ratio decreases with the normalized endpoint variable;
- the row-per-target profile increases on the frozen causal support;
- a no-upward edge therefore leaves nonnegative row bonus and score superordination.

No new finite-algebra error was found in this Gate A compilation. Its analytic Hall/profile inputs remain frozen.

**Gate A verdict:** conditional pass on the frozen inputs.

## 5.2 P1 — `L-92881.1` is supported, but `L-92881.2` is not established

`L-92881.1` states a labelled positive current/child source partition

\[
P_X^{\rm ret}
=
P_X^{\rm cur}
+
\sum_b\beta_bU_b\widetilde P_b.
\]

This part is supported by the exact aggregate causal identity of `L-91732`, the first-owner restrictions of `L-91841`, and positive integration. It is reasonable to treat `L-92881.1` as an exact source/row identity.

The next line is stronger:

\[
\Omega_X
=
\Xi(c_X)+r_X+
\sum_b\beta_bU_b\Omega_{Y_b},
\qquad r_X\ge0.
\tag{*}
\]

This no longer follows merely by observing the source partition. The inherited exact compiler `L-91750` gives child **responses**:

\[
\Omega_X
=
\Xi(P_X^{\rm cur})+e_X+
\sum_b\beta_bU_b\Xi(P_b),
\qquad e_X\ge0.
\]

To replace every `\Xi(P_b)` by `\Omega(P_b)`, one needs an additional positive decomposition proving

\[
e_X
\ge
\sum_b\beta_bU_b[\Omega(P_b)-\Xi(P_b)].
\]

Equivalently, the residual after reserving all complete child capacities must be realized and proved nonnegative.

`L-91750` flags this exact issue and says the one-shot route avoids it. `L-91843` and `L-92881` subsequently assert that source telescoping supplies the stronger capacity identity, but neither file displays the missing positive source packet whose observation is the complete child-capacity surplus, nor a stagewise equality proving that this surplus is paid from a disjoint root reserve.

The operation list and ownership table establish labels. They do not by themselves prove the capacity inequality needed to replace actual child rows by arbitrary feasible child rows.

Therefore:

```text
L-92881.1 labelled current/child source identity      SUPPORTED
L-92881.2 full-child native-capacity identity         GAP
L-92881.5 arbitrary child-row insertion               NOT REACHED
```

This is the first broken arrow in PR #489's recursive Gate B.

## 5.3 P1 — `L-92883` does not establish a positive reserve packet of mass `<3020`

The all-column theorem `L-91733` treats the retained finite/continuum mismatch through the signed adjacent defect

\[
\varepsilon_X(n)
=d_X^\star(n)-
\int_n^{n+1}d_X^\star(t)\,dt.
\]

Its cumulative correction is signed. The theorem proves that one common thinning leaves a **coordinatewise positive detail reserve after paying the signed correction**.

That does not automatically imply that the resulting reserve vector is the observation of a positive typed source packet in the causal cone.

`L-92883` makes precisely this upgrade. It introduces one positive packet `R_X^{\rm phys}` containing thinning, omissions, activation collars, retained-cell comparison, and terminal reserve, and asserts

\[
m(R_X^{\rm phys})<3020.
\]

It then applies `L-91385`:

\[
\mathcal H(R_X^{\rm phys})
\le5\log(3X)m(R_X^{\rm phys}).
\]

But `L-91385` applies to positive typed causal packets. Coordinatewise nonnegativity of a radix-four slack after subtracting a signed mismatch is not enough. A positive source realization, with its target mass and complete typed coordinates, must be exhibited.

Neither `L-91733` nor `L-91843` supplies that realization for the signed retained-cell comparison. `L-91843` calls the stage-13 output an unused detail packet, but does not construct a positive source subpacket whose target mass is bounded by the retained root target.

Thus the logarithmic estimate

\[
\langle Y_4,r_X\rangle<15100\log(3X)
\]

is presently unsupported.

A repair has two possible forms:

1. construct an explicit positive typed packet `R_X^{\rm phys}` with observation exactly `r_X` and prove its target mass is below the retained root mass; or
2. abandon the `L-91385` packet-mass shortcut and estimate the actual named root slack classes directly against `Y_4`, as PR #488 does.

## 5.4 `T-91312` and `L-92884.3`

The coefficient and mass calculation in `L-92884.3` is correct after HTR:

\[
\sum_b\beta_b\Delta_{Y_b}
<
\frac{3020}{8}C_+.
\]

The exact head contains `L-91751`, which proves the needed positive-packet HTR and even gives a direct first-generation terminalization bound. Therefore this part is repairable by adding `L-91751` to the normative dependency list and lock.

As written, however, `L-92884` cites `T-91312` as though that theorem supplied its own hereditary entry. It does not. `T-91312` explicitly declares HTR to be its open hypothesis.

**Verdict:** correct scaling; incomplete dependency declaration. Not the principal Gate B failure.

## 5.5 Same-index `Y_4` equality

`L-92884.2` is valid provided the vector cocycle exists. Normalized same-index placement preserves the numerical detail coordinates, so

\[
\langle Y_4,U_bs_b\rangle
=
\langle Y_4,s_b\rangle.
\]

No correction is requested on this point.

## 5.6 Port ownership

The intended direct-sum model is conceptually correct:

```text
physical detail reserve r_X         root-owned detail coordinate;
Schur port                           separate root-owned matrix coordinate;
recursive child port                zero;
Y4 pairing of direct-sum port        zero.
```

`L-92882` proves the branchwise PSD inequality

\[
D_b\preceq M_b
\]

and positive integration preserves it. The remaining ownership requirement is to show that the `M_b` are source-disjoint shares of the **one** uncolored root port, not one copy of the same full port for every branch.

The inherited `L-91725` explicitly forbids branchwise testing against independent copies of the full port. `L-91842` likewise requires a source-partitioned port share for every correction class.

`L-92882` calls `M_b` the available port of each actual branch, but does not display an identity such as

\[
P_s^{\rm port}
=
M_{\infty,s}
+
\sum_b M_{b,s},
\qquad
M_{b,s}M_{b',s}\text{ source-disjoint for }b\ne b',
\]

or the corresponding first-owner restriction tying `M_b` to `R_b`.

This should be added. If the intended definition is

\[
M_b=\operatorname{Port}(R_bP_s),
\]

with the same first-owner projections as the source partition, the aggregation is legitimate. Without that equation, the one-owner claim remains asserted rather than reconstructed.

The direct-sum and optional auxiliary-packet port representations must also remain alternatives. The direct-sum port has zero `Y_4` cost; the optional packet representation may have the stated logarithmic bound. They should not be charged simultaneously. The current prose distinguishes them, so no actual double charge was found, but the final theorem should select one model explicitly.

## 5.7 PR #489 verdict

The recursive vector cocycle algebra in `L-92884.1--.2` is correct **if** the full-capacity root identity exists. The exact head has not established that premise, and the alternative logarithmic root-cost proof additionally lacks a positive reserve-packet realization.

Therefore:

\[
\boxed{
\text{PR \#489 RECURSIVE/PORTFUL CLOSING LAYER: REQUEST CHANGES.}
}
\]

```text
L-92880 Gate A                                  conditional pass
L-92881.1 current/child source partition        supported
L-92881.2 full-child capacity reservation       gap / first broken arrow
L-92882 branch port domination                  algebra valid; share partition incomplete
L-92883 positive-reserve mass/Y4 theorem        gap
L-92884.3 target-mass scaling                   valid after explicit L-91751 HTR import
L-92884 Gate B                                  not established
T-92880 complete composition                    not established
Riemann Hypothesis                              unproved
```

---

# 6. Exact owner comparison

| Object | PR #488 one-shot owner | PR #489 intended recursive owner | Review finding |
|---|---|---|---|
| Hall residual / row bonus | current colour inside final row | root current | coherent |
| rough source with several active primes | unique first owner `R_j` | unique first owner `R_j` | verified |
| child row | internal colour; not exported | one normalized child class | source partition supported |
| child full declared capacity | not separately reserved | reserved in `L-92881.2` | **not established in #489** |
| bottom/top/knot omission | one root unused/slack owner | one root unused/slack owner | coherent |
| signed retained-cell mismatch | directly bounded in final root slack | absorbed into alleged positive `R_X^phys` | **positive packet realization missing in #489** |
| global quantizer | once on common parent | intended once on common parent | labels/order need to remain explicit |
| square-root thinning | once at root | once at root | coherent |
| finite base / taper / terminal retained row | current once | current once | do not also charge as slack |
| auxiliary Schur port | absent / zero | one root direct-sum matrix coordinate | branch share partition must be displayed |
| child port | zero | zero | verified design |

---

# 7. Lightweight checks performed

The review intentionally did not run the large directed or analytic campaigns. It performed only:

```text
GitHub PR head/base metadata verification;
exact path and blob reachability at both requested SHAs;
dependency-text crosswalks;
source-owner and coefficient normalization checks;
finite recurrence and constant checks;
comparison of actual-response versus full-capacity identities;
port-coordinate scope checks.
```

Numerical spot checks:

```text
1/sqrt(67)                 = 0.122169... < 0.125
p=67 projective demand     = 0.107244... < 1/9
3020/8                     = 377.5
X=10^12 thinning bound     = 11788.66... < 12012
X=10^12 nonterminal bound  = 3.3067... < 4
61000 threshold RHS        = 7,999,994
```

These checks authenticate only the local algebra discussed above.

---

# 8. Final comparative conclusion

The two proposals are not equally exposed to the same interface risk.

PR #488 retains the actual already-realized child colours inside one final physical row. It never needs to prove that the parent has reserved the full feasible capacity of independently replaceable children. It also uses no Schur port. On the declared frozen inputs, its one-shot/zero-port closing layer survives the requested checks.

PR #489 exports children and therefore must prove a strictly stronger statement: the root owns the **complete** child capacities and a nonnegative remainder after reserving them. The inherited compiler explicitly identifies this as an extra sign/realization requirement. `L-92881` does not yet supply it, and `L-92883` further assumes a positive reserve packet not constructed from the signed mismatch ledger.

Accordingly:

\[
\boxed{
\begin{aligned}
&\text{shared spine: conditional pass at frozen-input scope;}\\
&\text{PR \#488 closing layer: pass;}\\
&\text{PR \#489 closing layer: request changes;}\\
&\text{Riemann Hypothesis: unproved.}
\end{aligned}
}
\]
