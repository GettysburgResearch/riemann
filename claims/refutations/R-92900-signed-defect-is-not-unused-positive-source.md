# R-92900 — A signed finite/continuum defect is not unused positive source

Claim ID: `R-92900`
Status: **EXACT TYPE REFUTATION OF THE SHARED PR #488/#489 SOURCE-TELESCOPING STEP**
Created: 2026-08-15
Frozen targets: PR #488 at `9acd381fa168db02a03646ab16851daebbf4d0fd`; PR #489 at `0bb487c8a0782f601be0a3041743b357ad93726a`
Review target: PR #490 at `6f46c2cf4e84d51c744263f7e92a0e1743de5148`
Primary inputs: `L-91733`, `L-91840`, `L-91843`, `L-92883`
RH status: **unproved**

## 1. The arithmetic defect has a signed type

For a retained endpoint set \(A_X\), `L-91840` defines the finite-versus-continuum defect by the signed measure

\[
\eta_X
\]

and the restricted adjacent errors

\[
\varepsilon_X^A(n)=\eta_X(A_X\cap[n,n+1)).
\tag{R-92900.1}
\]

Its cumulative seed and ordinary response are

\[
E_X^A(m)=\sum_{n\ge m}\varepsilon_X^A(n),
\qquad
v_q(E_X^A)=\sum_{j\ge1}\eta_X(A_X\cap[jq,jq+1)).
\tag{R-92900.2}
\]

The controlling estimate is a **total-variation** estimate,

\[
|\eta_X|([n,n+1))
<
\frac{19}{2}n^{-3/2},
\tag{R-92900.3}
\]

not a positivity theorem for \(\eta_X\), \(E_X^A\), its ordinary response, or
its radix-four response. This is also explicit in `L-91733`, where the
realization error is bounded in absolute value.

Thus the retained comparison is a signed observation/correction datum. It is
not, without a separate positive-realization theorem, an unused positive source
subpacket.

## 2. The positive-stage claim in `L-91843` cannot include stage 13

`L-91843.1` requires every one of its fourteen stages to provide disjoint
positive packets

\[
C_i,\quad(P_{i,b})_b,\quad U_i,\quad\Sigma_i
\]

satisfying a source equality. Stage 13 is declared to be

```text
retained mismatch/collar/taper/base comparison.
```

The mismatch part is exactly the signed datum (R-92900.1). Total-variation
control does not turn it into a positive source packet. Therefore the statement

\[
\Sigma_{12}
=
C_{13}+\sum_bP_{13,b}+U_{13}+\Sigma_{13},
\qquad
C_{13},P_{13,b},U_{13},\Sigma_{13}\ge0,
\tag{R-92900.4}
\]

does not follow from the cited mismatch theorems.

Consequently the inference in `L-91843.3` that the final native slack is the
observation of a wholly positive unused-source packet is not established by the
fourteen-stage source telescope.

This does **not** refute the separate all-column inequalities of PR #487. It
refutes the stronger claim that those inequalities arise by observing one
all-positive source partition including the signed quadrature correction.

## 3. `L-92883` contains the same contradiction explicitly

`L-92883.1` places

```text
retained-cell comparison
```

inside a positive unused-source packet \(R_X^{\rm phys}\), and then bounds its
native cost by the target mass of that positive packet. The same file later
states that it “does not label a signed mismatch as positive.”

Both assertions cannot control the same term. Either:

1. the retained comparison is represented by an independently constructed
   positive packet, in which case that construction must be supplied; or
2. it remains the signed error of `L-91733/L-91840`, in which case its cost must
   be paid directly by its \(Y_4\)-weighted absolute response.

No positive realization of the signed comparison is supplied at the frozen
head of PR #489. Therefore the logarithmic estimate in `L-92883` is not proved
by the displayed mass argument.

## 4. The PR #490 review is consistent with this diagnosis

PR #490 independently finds that the actual post-correction stage residues are
not exhibited in PR #489. The present refutation identifies a precise reason:
one of the advertised residues is a signed observation error, not positive
source.

PR #490 also finds the portful Schur demand uninstantiated. The successor below
does not repair that portful theorem. It uses the inherited zero-port
specialization and therefore removes `L-92882` from the load-bearing chain.

## 5. Exact correction

The correct composition has two ledgers:

```text
positive source ledger:
    Hall, restrictions, first ownership, causal current/children,
    omissions and thinning;

signed observation ledger:
    finite/continuum comparison, quantization response error,
    taper/base response corrections.
```

Let \(u_X\ge0\) be unused native capacity created by the positive source ledger
and let \(e_X\) be the signed excess-use vector from the observation ledger.
After proving

\[
e_X(q)\le u_X(q)
\qquad(q\ge2),
\tag{R-92900.5}
\]

one may set

\[
r_X=u_X-e_X\ge0.
\tag{R-92900.6}
\]

The stronger sufficient estimate \(|e_X(q)|\le u_X(q)\) is allowed. The
positivity of \(r_X\) comes from the explicit capacity comparison, not from
misclassifying \(e_X\) as positive source.

`L-92900` formalizes this repair.

## 6. Disposition

```text
PR #488 positive Hall/source operations                 retained
PR #488 direct all-column numerical reserve             not refuted here
PR #488 claim that every correction stage is positive   false as compiled
PR #489 positive source/child ownership                  retained
PR #489 logarithmic reserve-mass proof                   gap / type error
PR #489 portful Schur-demand theorem                     bypassed, not repaired
native slack cocycle algebra                             valid once root identity is repaired
endpoint consumer                                        unaffected by this refutation
Riemann Hypothesis                                       unproved
```
