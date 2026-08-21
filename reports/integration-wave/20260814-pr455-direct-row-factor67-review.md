# Independent review of PR #455: hardened direct native-row factor-67 proposal

Review cutoff: `2026-08-14T09:03:00Z`  
Repository: `gfreund123/riemann`  
Main at freeze: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
PR: `#455`  
Base: `research/gpt56-pro/91663-direct-root-review-response`  
Base SHA: `f41797c91497dc462f549a127d8494bbe4ccde2f`  
Reviewed live head: `9dba11b2f1130c0aa8dba5846ec3c2e658326474`  
Latest reviewed commit: `harden: firewall finite-window positivity from the global sign problem`  
Status at freeze: open, draft, mergeable

## Executive verdict

The proposal contains several correct and useful local theorems, including the fixed-67 entropy inequality, the exact native ordinary/detail response identity, same-index child replacement, and the abstract logarithmic packet envelope.

The full theorem does **not** survive review. There is an exact normalization contradiction in the new load-bearing source-entry theorem `L-91668`:

\[
\boxed{
\text{the cited two-channel realization produces }3c_X,\text{ not }c_X.
}
\]

This invalidates `L-91668.10--11`, the claimed positivity/ownership realization of the native row, and the downstream use of that row in `L-91663`, `L-91669`, and `T-91655`.

Independently, the continuum equality score packet and the finite arithmetic row are still asserted to be two realizations of one root datum without an exact score-and-row-preserving realization theorem. The latest firewall `R-91658` correctly identifies this bridge as load-bearing, but no later theorem supplies it.

The repository hardening record is also not frozen at the live head: the current manifest contains stale blobs for the current `L-91669` and `T-91655`, omits `R-91658`, and the retained hardening replay does not test the failed normalization identity.

```text
fixed-67 entropy theorem L-91666                    VERIFIED
native response Gamma(c_X)=w_X, Xi(c_X)=Omega_X    VERIFIED
same-index arbitrary-child replacement              VERIFIED CONDITIONAL
one-prime target/score/row cocycle                   VERIFIED
source ownership as a combinatorial partition       VERIFIED
L-91668 root row observation                         FALSE / EXACT FACTOR-3 ERROR
continuum equality -> finite c_X realization         UNPROVEN / GAP
one-row ownership ledger L-91669                     UNPROVEN / DEPENDS ON FALSE INPUT
current dependency manifest                          STALE / INCOMPLETE
T-91655 full direct-row theorem                      REJECTED AS PROOF
Riemann Hypothesis                                   UNPROVEN
```

## 1. Exact counterexample to `L-91668.10`

### 1.1 The realization formula imported from `L-91330`

For a squarefree source index `n` and `Y=X/n`, the imported channel weight is

\[
w_a(X,n)
=\frac{a\sqrt X}{n}-\frac1{\sqrt n}
=\frac1{\sqrt n}(a\sqrt Y-1).
\]

`L-91330` defines the normalized component profile

\[
\mathcal Q_{j,a}(Y)
=\frac{Q_Y(j)}{a\sqrt Y-1}.
\]

Consequently the row observation of one unit of channel source is exactly

\[
\boxed{
w_a(X,n)\mathcal Q_{j,a}(Y)
=\frac1{\sqrt n}Q_Y(j).
}
\tag{1}
\]

### 1.2 Apply the coefficients actually used by `L-91668`

`L-91668.5` uses the positive split

\[
w_\Psi
=(1+\kappa_*)w_{a_*}
 +(2-\kappa_*)w_1.
\]

Applying the cited realization (1) to both labelled channels gives

\[
\begin{aligned}
&(1+\kappa_*)w_{a_*}\mathcal Q_{j,a_*}
 +(2-\kappa_*)w_1\mathcal Q_{j,1}\\
&\qquad=
\bigl[(1+\kappa_*)+(2-\kappa_*)\bigr]
\frac1{\sqrt n}Q_Y(j)\\
&\qquad=
\boxed{3\frac1{\sqrt n}Q_Y(j)}.
\end{aligned}
\tag{2}
\]

The parity observation multiplies this by `mu(n)`. Therefore the signed atomwise observation is

\[
\boxed{
3\frac{\mu(n)}{\sqrt n}Q_{X/n}(j),
}
\]

not the single copy claimed in `L-91668.10`.

This is not a zero-times-undefined boundary issue. For example, take `n=1`, `X=67`, and `j=2`; the positive component formula gives `Q_67(2)>0`. Thus equations (2) and `L-91668.10` disagree on an active physical row coordinate.

### 1.3 Consequence at the root

Under the realization actually cited by the theorem, the root observation is

\[
R_{\rm root,X}=3c_X,
\]

whereas `L-91668.11` asserts `R_root,X=c_X`.

Since `L-91663` proves

\[
\Gamma(c_X;q)=w_X(q),
\qquad
\Xi(c_X;q)=\Omega_X(q),
\]

the realized row `3c_X` has responses `3w_X` and `3Omega_X`. It is not the native-capacity row consumed by the direct child-replacement theorem.

An explicit factor `1/3` could be proposed as a repair, but no such factor exists in `L-91330`, `L-91668`, the dependency manifest, or the replays. Adding it would require retyping and rechecking the target/score/row Hall interfaces; it is not a notation-only correction.

Therefore:

\[
\boxed{
L\text{-}91668.10\text{ and }L\text{-}91668.11\text{ are false as written.}
}

## 2. The continuum equality-score bridge remains unproved

The latest firewall `R-91658` correctly withdraws the earlier attempt to delete the outer equality realization. It now requires one normalization bridge among:

1. the continuum equality datum of `L-26204/L-91557`;
2. the positive first-window endpoint realization of `L-91107--L-91115`;
3. the exact finite native row claimed in `L-91668`;
4. the assertion that all three are stages of one source-faithful root packet.

No theorem in the frozen head proves this complete bridge.

### 2.1 What is exact on the finite arithmetic side

The finite native row is

\[
c_X(j)=
\sum_{k\le X}\frac{\mu(k)}{\sqrt k}Q_{X/k}(j).
\]

Its ordinary and detail responses are exactly `w_X` and `Omega_X`. Its literal score can also be computed exactly. Writing

\[
E(Y)=\sum_jQ_Y(j)G_j
=\sum_{2\le m\le Y}
 \frac{\log m}{\sqrt m}\log\frac Ym,
\]

one obtains

\[
\begin{aligned}
\mathcal S(c_X)
&=\sum_{k\le X}\frac{\mu(k)}{\sqrt k}E(X/k)\\
&=\sum_{km\le X}
  \frac{\mu(k)\log m}{\sqrt{km}}
  \log\frac{X}{km}\\
&=\sum_{r\le X}
  \frac1{\sqrt r}\log\frac Xr
  \sum_{m\mid r}\mu(r/m)\log m\\
&=\boxed{
  \sum_{r\le X}\frac{\Lambda(r)}{\sqrt r}
  \log\frac Xr
  =P_\Lambda(X)}.
\end{aligned}
\tag{3}
\]

### 2.2 What is exact on the continuum side

`L-26204/L-91557` assign the complete continuum equality datum the critical score

\[
\boxed{4\sqrt X}.
\tag{4}
\]

Equation (4) is not the literal score identity (3). The intended recursion may improve the canonical child packing, so this mismatch is not by itself a contradiction. But a proof must exhibit an exact positive, source-faithful realization showing that the declared continuum score (4) is carried by the same packet whose physical row is `c_X`, with every current correction charged once.

`L-91669` and `T-91655` state that the outer endpoint producer and `c_X` are “two representations/stages of the same normalized root equality datum.” That sentence is the missing theorem, not its proof. `L-91557` itself classifies the final physical ordinary/radix-four assembly as a separate review-bearing obligation.

The proposal therefore faces the following dichotomy:

```text
If the outer endpoint producer is a second physical row,
then appending it to c_X double-spends native capacity.

If it is only a proof-side score certificate,
then an exact realization theorem must transfer its 4 sqrt(X) score
onto c_X-R_ch and the recursive child without changing the row ledger.
```

The one-row ownership rule prevents the first error, but does not prove the second statement. The failed `L-91668` normalization was supposed to provide the missing source-faithful identification.

## 3. The retained hardening replay does not test the failed interface

`X-91668-hardened-direct-row-review/verify.py` checks:

- squarefree source ownership on finitely many endpoints;
- generic survival/hazard coefficients summing to one;
- synthetic ordinary/detail replacement inequalities;
- a terminal-mass telescope;
- the blobs listed in the manifest.

It does **not** evaluate the balanced/reserve row realization in `L-91668.10`. In particular, it never checks

\[
(1+\kappa_*)+(2-\kappa_*)=1;
\]

which would immediately fail, because the left side is `3`.

The retained result also explicitly records:

```text
actual_frozen_hall_cells_replayed_here = false
a endpoint contour replay              = false
rh_established_by_replay               = false
```

Thus the `PASS_HARDENED_DIRECT_ROW_REVIEW_PACKET` classification is not evidence for the false root-row identity.

## 4. The live dependency freeze is stale and incomplete

The PR body still names the earlier proposal head

```text
1a6443778095ef2af434c28a53ab2edb347499e3
```

while the reviewed remote head is

```text
9dba11b2f1130c0aa8dba5846ec3c2e658326474.
```

At the live head, `t91655-dependency-manifest.json` records:

```text
L91669 blob 2563665b26e63df8bb21c1fdb74769a34aeed4f4
T91655 blob 393df457e9036c34b7ab562e48d755bc395690c5
```

but the actual current blobs are:

```text
L91669 blob ed35b6487733a04097bb9d16ef8c04b34fd41597
T91655 blob 7c282e7d5214f2ac6a43200d810b2531274da397.
```

The current manifest also omits the newly normative firewall `R-91658`.

Consequently the retained result saying all 19 local blobs matched authenticates an earlier tree, not the final theorem currently presented for review. A fresh execution of the manifest check against the live head would fail on at least the two displayed blob mismatches.

The user-supplied summary also advertises files that are not present at the frozen head:

```text
standalone/.../REVIEW_SPECIFICATION.md
experiments/X-91669-hostile-direct-row-audit/
integration/2026-08-14/t91654-hardening-lock-v2.json
claims/lemmas/L-91668-direct-row-reset-normal-form-and-ledger-uniqueness.md
```

The actual standalone directory contains only `README.md` and `CLAIM_STATUS.md`; the actual hardening experiment is `X-91668-hardened-direct-row-review`; and the actual integration directory contains the older direct-root lock, supplement lock, handoff, and dependency manifest.

Therefore the claims “final immutable hardening lock” and “complete normative hostile-reconstruction packet” are not durable at the reviewed head.

## 5. Mathematics that survives

### 5.1 `L-91666` fixed-67 entropy inequality

The statement

\[
E(Y)-E(Y/67)
\ge5(\sqrt Y-\sqrt{Y/67})
\qquad(Y\ge67)
\]

survives review. The cell derivative formula is correct; the finite corridor contains 402 cells; and the analytic tail from `Y=469` has the claimed positive derivative. The retained directed margins are large rather than close sign calls.

### 5.2 Native response identities

The Möbius convolution giving

\[
\Gamma(c_X)=w_X,
\qquad
\Xi(c_X)=\Omega_X
\]

is exact.

### 5.3 Same-index child replacement

Once a nonnegative parent packet and canonical child are correctly typed, the identity

\[
d_X=R_{\rm parent}-R_{\rm ch}+d_{\rm ch}
\]

and the ordinary/detail no-overdraw inequalities are exact. No affine row-index lift or fractional physical column is required.

### 5.4 One-prime native cocycle

The survival/hazard row coefficients

\[
\kappa_s=1-p^{-1},
\qquad
\kappa_h=p^{-1}
\]

sum to one. The local raw-residual-plus-child to controlled-branch identity in target, row-budgeted score, and literal row is algebraically valid on its frozen one-prime inputs.

### 5.5 Conditional envelope and finite dual

The formal loss identity

\[
\operatorname{Loss}_X(d_X)
=
[J_X-J_{\rm ch}-\mathcal S(R_{\rm parent}-R_{\rm ch})]
+\operatorname{Loss}_{\rm ch}(d_{\rm ch})
\]

is correct when all terms are one typed packet. A uniform current bound gives a coefficient-one logarithmic recurrence. The finite von-Mangoldt dual inequality also has the correct sign.

These results are valuable route infrastructure. They do not repair the false root entry.

## 6. Reviewed proof DAG

```text
fixed-67 entropy theorem                          VERIFIED
native response of c_X                            VERIFIED
least-prime ownership labels                      VERIFIED
balanced/reserve positive source split            TARGET IDENTITY ONLY
balanced/reserve source -> c_X row                 FALSE: produces 3 c_X
leafwise Hall Fubini -> native parent row          BLOCKED
same-index child replacement                      VERIFIED CONDITIONAL
one-use current score ledger                       BLOCKED BY ROOT TYPE
Loss_X <= Loss_(X/67)+C                            CONDITIONAL
Loss_X=O(log X)                                    CONDITIONAL
F_Lambda <= Loss_X                                 VERIFIED
subquadratic F_Lambda -> RH                        IMPORTED / NOT REACHED
Riemann Hypothesis                                 UNPROVEN
```

The first failed arrow is

\[
\boxed{
\text{positive balanced/reserve root source}
\not\longrightarrow
\text{one copy of the native row }c_X.
}
\]

## 7. Required repair

A valid successor must provide one frozen theorem that simultaneously:

1. defines the exact realization of each balanced/reserve source atom in the native row space;
2. reproduces **one**, not three, copies of `mu(n)n^(-1/2)Q_(X/n)`;
3. retains the target Hall identities and score superordination under the corrected scaling;
4. identifies the positive finite-window continuum equality packet with that same finite realization;
5. proves the one-use collar/mismatch/top/port ledger in the same data type;
6. regenerates a lock from the final theorem blobs and reruns the validator on that exact head.

Until those obligations are discharged, neither the current row positivity nor the score recurrence applies to the native RH packet.

## Final classification

\[
\boxed{
\text{PR #455 at }9dba11b2\ldots\text{ does not establish its stated theorem.}
}
\]

\[
\boxed{
L\text{-}91668\text{ is false as written by an exact factor-3 calculation.}
}

\[
\boxed{
T\text{-}91655\text{ is an unproved architecture, not a proof of RH.}
}

\[
\boxed{
\mathrm{RH}\text{ remains unproved.}
}
