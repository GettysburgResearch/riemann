# Latest-pass recovery and the post-Hall frontier

Date: 2026-08-14  
Repository: `gfreund123/riemann`  
Live main observed: `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`  
Recovered proposal: PR #455 at `9dba11b2f1130c0aa8dba5846ec3c2e658326474`  
Independent refutation: PR #456 at `a72c1a0505b3bd79f99ad5ec207c39dd052c45a6`  
This branch: `research/gpt56-pro/91670-post-hall-successor-frontier`

## Executive status

The previous handoff failed to report substantial work which had in fact been deposited on PR #455.  That work is preserved, but the independent stopped-leaf Hall counterexample on PR #456 remains fatal to the complete conclusion.

The exact status is

```text
source ownership and least-prime stopping partition       strengthened exactly
native Möbius ordinary/detail response                    retained exactly
same-index child replacement                              retained conditionally
finite-window equality-realization scope                  corrected
one-use current/recursive bookkeeping                     materially hardened
universal stopped-leaf no-upward Hall producer            false
T-91655 complete conclusion                               withdrawn as proof
Riemann Hypothesis                                        unproved
```

## I. Work recovered from the latest pass

### 1. Exact labelled source ownership

`L-91668` supplies the positive two-channel least-prime source tree and assigns every active squarefree source atom one owner.  At fixed physical endpoint `X`, the stopping tree is finite and has the mutually singular decomposition

\[
 \boldsymbol\mu_{\rm root,X}
 =\boldsymbol\mu_{\rm cur,X}
  \oplus\bigoplus_{v\in\mathcal L_X}\boldsymbol\mu_v.
\]

The signed observation of the complete labelled tree is exactly

\[
 c_X(j)=\sum_{n\le X}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
\]

The retained structural replay checks `121696` source records and `126638` least-prime recursion edges.  This removes source-owner ambiguity and proves that no arithmetic atom is silently duplicated before the disputed Hall step.

### 2. Finite-window equality realization, not global positivity

`R-91658` corrects an overcompressed draft.  The reciprocal-zeta equality weight `L_*` is used only on the certified positive quotient window

\[
 0\le u\le\log(c_0^{-1}),
 \qquad c_0=0.01844367547104\ldots .
\]

No global positivity of `L_*` is assumed.  The endpoint quantization, collar, mismatch, top omission and corrected boundary reserve remain a one-use realization layer.  They are neither removed nor added as an independent second copy of `c_X`.

### 3. One-use ledger and exact same-index replacement

The hardened ledger records that the complete current row must be summed before the canonical child is subtracted.  Given a genuine positive parent row `R_parent`, its canonical child `R_ch`, and any child-feasible row `d_ch`, the replacement

\[
 d_X=R_{\rm parent}-R_{\rm ch}+d_{\rm ch}
\]

satisfies, for every physical integer column,

\[
 \Gamma(d_X;q)
 =\Gamma(R_{\rm parent};q)-\Gamma(R_{\rm ch};q)
  +\Gamma(d_{\rm ch};q)
 \le\Gamma(R_{\rm parent};q),
\]

\[
 \Xi(d_X;q)
 =\Xi(R_{\rm parent};q)-\Xi(R_{\rm ch};q)
  +\Xi(d_{\rm ch};q)
 \le\Xi(R_{\rm parent};q).
\]

This is valid infrastructure.  It does not create the required positive parent row.

### 4. Fail-closed dependency and structural replay

PR #455 froze nineteen load-bearing blobs and prohibited the historical shortcuts

```text
L91659
AFFINE67
P53_AT_P61
SOURCE_FRACTION_LOSS
HALL_TREE_COMMUTATION
OUTER_PACKET_DUPLICATION
```

The replay result

```text
PASS_HARDENED_DIRECT_ROW_REVIEW_PACKET
proof object 01de592e71de67768a8c6bf42dd303db6bb9795674f73adab3073684cd012218
```

is a structural and ledger regression.  It explicitly states that the actual frozen Hall cells are not replayed there and that the replay does not establish RH.

## II. The decisive refutation survives every hardening step

The disputed theorem applies a no-upward Hall projection to every stopped one-prime leaf.  Such a leaf may have

\[
 p=67,\qquad y=13,\qquad x=py=871,
\]

and negative threshold `t=13`.  For the survival channel,

\[
 \alpha_s=\frac{2(2+1/\sqrt{67})}{3+1/\sqrt{67}},
\]

and

\[
 A_{13}=\sum_{n\le13}\frac{\mu(n)}n=-\frac{2323}{30030}.
\]

The necessary Hall prefix is

\[
 \mathcal H_{\alpha_s,13}(871)
 =\alpha_s\sqrt{871}\,A_{13}-B_{13},
\]

where

\[
 B_{13}=\sum_{n\le13}\frac{\mu(n)}{\sqrt n}.
\]

The directed enclosure on PR #456 gives

\[
 -2.140<\mathcal H_{\alpha_s,13}(871)<-2.139.
\]

The omitted physical branch prefactor is positive.  Hence the survival Hall prefix is strictly negative and the required no-upward transport does not exist.

The issue is structural, not a finite-range omission.  For fixed `y=13`, the factor `\alpha_s(p)\sqrt p` increases with `p`, while `A_{13}<0`, so the obstruction persists and strengthens along an infinite family of rough primes.

Therefore every theorem which contains the universal implication

```text
stopped one-prime leaf
 -> branchwise no-upward Hall transport
 -> positive parent row
```

is false as written.  In particular the Hall-dependent portions of `L-91621`, `L-91668`, `L-91669`, and `T-91655` cannot be used as proof-level inputs.

## III. What remains valid after the refutation

The following statements survive independently:

1. the exact labelled least-prime source partition before Hall;
2. the exact native ordinary/detail formulas
   \[
   \Gamma_Y(q)=q^{-1/2}H(Y/q),
   \qquad
   \Xi_Y(q)=q^{-1/2}[H(Y/q)-H(Y/(4q))];
   \]
3. the Möbius collapse
   \[
   \Gamma(c_X;q)=w_X(q),
   \qquad
   \Xi(c_X;q)=\Omega_X(q);
   \]
4. conditional same-index child replacement;
5. the corrected finite-window scope for the equality realization;
6. the corrected fixed-67 entropy base and the separate global score inequality, subject to reconstruction of its own proof packet;
7. the corrected `P_61` normalization below `14/3` as an abstract reserve.

None of these statements supplies the missing positive parent decomposition.

## IV. The correct successor theorem

The branchwise no-upward Hall route must be abandoned.  The next producer must solve the **joint survival-hazard native cone problem** before either branch is projected separately.

For each stopped leaf `(p,y)` and each frozen Boolean source label, let the exact signed leaf datum be

\[
 \mathcal D_{p,y}
 =(	ext{target},\text{native score},\text{literal row},
   \text{ordinary response},\text{detail response},\text{port}).
\]

Construct one finite family of nonnegative physical packets with coefficients `x_k\ge0` and target-null row bonuses `b_j\ge0` such that, simultaneously,

\[
 \sum_k x_k T_k=T(\mathcal D_{p,y}),
\]

\[
 \sum_k x_k S_k\ge S(\mathcal D_{p,y}),
\]

\[
 R(\mathcal D_{p,y})
 =\sum_kx_kR_k+b,
 \qquad b\ge0,
\]

\[
 \sum_kx_k\Gamma_k(q)\le\Gamma(\mathcal D_{p,y};q),
\]

\[
 \sum_kx_k\Xi_k(q)\le\Xi(\mathcal D_{p,y};q),
\]

with one shared boundary-port inequality and with every source label used once.

This is a finite cone-membership problem after the `P_61` Boolean block and the finite physical row templates are frozen.  It must be checked jointly: separate survival and hazard Hall prefixes are neither assumed nor required.

A production certificate has the exact primal/dual alternative

\[
 Bx=b,\qquad Gx\le c,\qquad x\ge0,
\]

or one rational Farkas separator

\[
 y^TB+z^TG\ge0\ \text{on every allowed packet},
 \qquad y^Tb+z^Tc<0.
\]

A rational feasible point closes the stopped-leaf producer.  A rational separator gives an exact obstruction and prevents another false completion.

## V. Recommended integration status

```text
PR #455 / T-91655                           do not integrate as proof
PR #456 stopped-leaf counterexample         retain as exact refutation
L-91668 source ownership before Hall        retain separately
native Möbius response identities           retain separately
same-index replacement algebra              retain conditionally
next proof target                            joint native cone producer
RH                                           unproved
```

This report is the recovered content of the unpublished pass.  It deliberately does not present the hardening packet as a successful answer to PR #456.