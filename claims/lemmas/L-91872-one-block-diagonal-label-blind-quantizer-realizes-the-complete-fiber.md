# L-91872 — One block-diagonal, label-blind quantizer realizes the complete native fibre

Claim ID: `L-91872`  
Status: **PROVED FORMAL POSITIVE REALIZATION; FACTOR-67 INSTANTIATION REVIEW REQUIRED**  
Created: 2026-08-15  
Inputs: `L-91871`, `L-91110`, `L-91821`  
RH status: **unproved**

## 1. Disjoint physical target

The common physical target is the disjoint union

\[
 \mathcal T_X=\mathcal T_X^{\rm anc}\dotplus\mathcal T_X^{\rm bulk}.
\tag{L-91872.1}
\]

The bulk is the tagged complete-cell union

\[
 \mathcal T_X^{\rm bulk}
 =\coprod_{n=K+2}^{X-W-3}\{n\}\times[0,1).
\tag{L-91872.2}
\]

The anchored target consists of already finite positive rows. Shared geometric
endpoints do not identify the two blocks.

## 2. The sole quantizer

Define

\[
\boxed{
 Q_X^{\rm nat}=I_{\rm anc}\oplus Q_{\rm bulk},
}
\tag{L-91872.3}
\]

where `I_anc` is the identity on anchored rows and `Q_bulk` is the positive
martingale B-spline kernel. This is one Markov operator on the disjoint target.
It depends only on the physical target point and not on source sign, Hall edge,
first owner, child label or path history.

The final unthinned row is the output marginal

\[
 d_X^0(j)=
 \Gamma_X^0(\mathrm{native\ source}\times
 \mathrm{owners}\times\mathcal T_X\times\{j\}).
\tag{L-91872.4}
\]

It is coefficientwise nonnegative.

## 3. Explicit thinning discard

Apply

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130}
\]

once to the whole coupling. Define the discarded native occurrence marginal

\[
 d\Sigma_X^{\rm disc}=(1-\tau_K)d(\Sigma_X^++\Sigma_X^-).
\tag{L-91872.5}
\]

Scale every Hall/Lorenz incidence and residual measure by `tau_K`. For each
positive or negative input marginal define the complementary discard
`(1-tau_K)Sigma_X^+` and `(1-tau_K)Sigma_X^-`. Then

\[
\boxed{
 \text{retained positive incidence}+\text{positive discard}=\Sigma_X^+,
}
\]

\[
\boxed{
 \text{retained negative incidence}+\text{negative discard}=\Sigma_X^-.
}
\tag{L-91872.6}
\]

These are incidence-marginal identities. They do not equate scalar output mass
with total absolute input mass. No input incidence disappears and no discarded
incidence is assigned to a child.

## 4. Ordinary `q`, ordinary `4q`, and detail

For every ordinary response functional `C_q`, positivity and Tonelli give

\[
 C_q(d_X)=\int C_q(Q_X^{\rm nat}(t,\cdot))d\Gamma_X(t).
\tag{L-91872.7}
\]

The same formula is evaluated independently at `4q`. Only afterward define

\[
 \Xi_q(d_X)=C_q(d_X)-2C_{4q}(d_X).
\tag{L-91872.8}
\]

Thus detail is the difference of two observations of the same total row. No
branchwise detail inequality is subtracted from another branchwise inequality.

## 5. No recursive export or auxiliary port

All first-generation child packets have already received their physical
same-index placement inside `Gamma_X`. The exported recursive family is empty.
The operation list uses no coloured state completion, so the auxiliary Schur
port demand is zero.

## 6. Signed comparison ledger

The retained-cell finite/continuum defect, intrinsic bulk collar and terminal
comparison form a signed observation vector `e_X`. They are applied after the
positive source sum and are never inserted into the positive source marginal.
Literal omissions and thinning provide positive unused capacity `u_X`.

```text
one physical target                    tagged disjoint union
one quantizer                          identity plus bulk Markov kernel
label dependence                       forbidden
q/4q assembly                          common row first
exported children                      empty after placement
auxiliary port                         zero
signed comparison                      separate ledger
```
