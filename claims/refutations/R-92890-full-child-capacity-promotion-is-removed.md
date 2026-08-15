# R-92890 — The recursive full-child-capacity promotion is removed from the conclusion-producing route

Claim ID: `R-92890`  
Status: **EXACT SCOPE CORRECTION / REVIEW REPAIR**  
Created: 2026-08-15  
Reviews addressed: PR #490 at `6f46c2cf4e84d51c744263f7e92a0e1743de5148`; PR #491 at `f5fb88c80f56e0b4e221c90f6362cf20413db02f`  
Frozen proposal repaired: PR #489 at `0bb487c8a0782f601be0a3041743b357ad93726a`  
RH status: **unproved at this claim**

## 1. The exact compiler identity

The frozen common-parent compiler gives the response identity

\[
\Omega_X
=
\Xi(P_X^{\rm cur})+e_X+
\sum_b\beta_bU_b\Xi(P_b),
\qquad e_X\ge0.
\tag{R-92890.1}
\]

It does **not** by itself give

\[
\Omega_X
=
\Xi(P_X^{\rm cur})+r_X+
\sum_b\beta_bU_b\Omega(P_b),
\qquad r_X\ge0.
\tag{R-92890.2}
\]

Indeed, (R-92890.2) would require

\[
e_X\ge
\sum_b\beta_bU_b\bigl[\Omega(P_b)-\Xi(P_b)\bigr].
\tag{R-92890.3}
\]

No such positive capacity-completion theorem was proved in PR #489. Reviews #490 and #491 are correct on this point.

## 2. The repair

The conclusion-producing construction never performs the promotion
\(\Xi(P_b)\mapsto\Omega(P_b)\).

Every positive child colour produced by the causal split remains inside the one
final physical parent row and is realized by its **actual canonical component
row**. Therefore the exact compiler response (R-92890.1) is the only response
identity used.

Equivalently, the exported recursive family is empty:

\[
\boxed{\sum_b\beta_b=0.}
\tag{R-92890.4}
\]

The historical actual-target-mass normalization remains a valid audit of source
nonduplication, but no independently re-realized child packet appears in the
endpoint proof.

## 3. The external slack is not a source packet

After the complete finite row \(d_X\) has been constructed and its physical
columns have been bounded directly, define

\[
r_X(q)=\Omega_X(q)-\Xi(d_X)(q).
\tag{R-92890.5}
\]

The proof establishes \(r_X(q)\ge0\) **before** using this notation. The vector
\(r_X\) is unused numerical capacity. It is not assigned source mass, a target
coordinate, or a physical packet interpretation.

Thus no argument of the form

```text
coordinatewise nonnegative reserve
therefore one positive source packet of mass M
```

is used.

## 4. Port scope

The conclusion-producing one-shot route invokes no auxiliary Schur state
completion. Its complete auxiliary matrix demand is zero. This is proved
class-by-class in `L-92892`; it is not inferred from a scalar mass or trace
bound.

## 5. Surviving PR #489 work

The following remain useful and are retained:

```text
one common Hall flow for target, score and every row;
actual-target-mass child normalization;
first-owner provenance;
ordinary-q / ordinary-4q ordering before detail;
same-index numerical coordinate covariance;
the native Y4 dual.
```

The recursive full-capacity cocycle and the proposed positive-reserve packet are
not used by `T-92890`.

```text
full-child capacity promotion             RETRACTED FROM CONTROLLING ROUTE
actual child responses                    RETAINED EXACTLY
exported recursive family                 EMPTY
numerical external slack                  DIRECTLY PROVED / NOT A SOURCE PACKET
auxiliary matrix port                     ZERO / CLASSWISE DECOMPILED
Riemann Hypothesis                        UNPROVED AT THIS CLAIM
```
