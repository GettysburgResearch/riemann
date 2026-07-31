# T-18501 — Cardinal–radical packets satisfy the certified-zero count cofinally

Claim ID: `T-18501`  
Title: Exact finite-section cardinal repair turns the final count into a right-inverse norm comparison  
Status: `PROPOSED — CONSTRUCTED-PACKET COUNT CLOSED; COMPLETE-LOW CAPTURE SEPARATE`  
Authoring agent: `gpt56-03-m`  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: `L-18501`; `T-14306`; `L-14321`; the exact cardinal–radical quadratic-tail identities  
Scope: the boxed count in Issue #185

## 1. Packet from exact cardinal and radical coordinates

Fix a finite selected set `Z` of proof-grade simple critical-line zeros and a
finite exact global radical packet `R_m`. At logarithmic support `[-L,L]`, use
the exact finite-section repairs of `T-14306`:

\[
\widetilde C_{Z,L}
=P_LC_Z(V_ZP_LC_Z)^{-1},
\qquad
V_Z\widetilde C_{Z,L}=I,
\tag{T-18501.1}
\]

and

\[
K_{m,Z,L}
=P_LR_m-\widetilde C_{Z,L}V_ZP_LR_m,
\qquad
V_ZK_{m,Z,L}=0.
\tag{T-18501.2}
\]

Put

\[
U_{m,Z,L}
=\operatorname{Ran}\widetilde C_{Z,L}
 \oplus\operatorname{Ran}K_{m,Z,L}.
\tag{T-18501.3}
\]

Then, exactly,

\[
U_{m,Z,L}\cap\ker V_Z
=\operatorname{Ran}K_{m,Z,L}.
\tag{T-18501.4}
\]

Let `G_(C,L)>0` be the declared metric on this finite packet. The evaluation
map and the right inverse must live on the same represented space. If the
packet is first harmonically lifted by `J_C`, replace `V_Z` by

\[
V_Z^C=V_ZJ_C
\]

and construct an exact right inverse for that lifted map. An unlifted cardinal
inverse may not be paired with a lifted Gram.

Let `C_(Z,L)^C` denote the exact right inverse on the represented packet and put

\[
\boxed{
\Lambda_{m,Z,L}
=\lambda_{\max}
 \left(
  (C_{Z,L}^C)^*G_{C,L}C_{Z,L}^C
 \right).
}
\tag{T-18501.5}
\]

This number is finite and positive. For the unlifted packet one may take
`C_(Z,L)^C=widetilde C_(Z,L)`. For a lifted packet, surjectivity and the right
inverse are finite exact gates; for example they are automatic when the
ambient harmonic correction lies in the selected-evaluation kernel.

## 2. Selected and enlarged certified-zero Grams

The selected positive Gram is

\[
K_{Z,L}^C=(V_Z^C)^*V_Z^C.
\tag{T-18501.6}
\]

Let `K_(T,L)^C` be any larger positive Gram assembled from a finite proof-grade
set of actual critical-line zeros containing `Z`, in the same packet and
normalization. Then

\[
\boxed{
K_{T,L}^C\succeq K_{Z,L}^C.
}
\tag{T-18501.7}
\]

No completeness of all zeros below a growing height is required for this
Loewner inequality.

Let `S_(U,L)` be the exact finite Schur or Weil form on the represented packet.
Assume a source-bound residual estimate

\[
\boxed{
S_{U,L}\succeq K_{T,L}^C-B_{T,m,Z}(L)G_{C,L},
\qquad B_{T,m,Z}(L)\ge0.
}
\tag{T-18501.8}
\]

For the exact packet of `T-14306`, this budget is supplied by the quadratic
cardinal/radical localization identities. At fixed finite `m`, `Z`, and finite
certified block `T`,

\[
\boxed{
B_{T,m,Z}(L)\longrightarrow0
\qquad(L\to\infty).
}
\tag{T-18501.9}
\]

Indeed the exact global cardinal block is positive identity, the exact global
radical block and its cross terms vanish, and every finite-section error is
quadratic or bilinear in the discarded cardinal and radical tails. This route
does not require certifying every zeta zero to an unbounded height.

## 3. Exact count theorem

Choose `beta_(m,Z,L)>0` satisfying

\[
\boxed{
B_{T,m,Z}(L)+\beta_{m,Z,L}
<\Lambda_{m,Z,L}^{-1}.
}
\tag{T-18501.10}
\]

Apply `L-18501` to the represented evaluation map `V_Z^C`, its exact right
inverse, and the metric `G_(C,L)`. Together with (T-18501.7), it gives

\[
\boxed{
N_{
G_{C,L}^{-1/2}K_{T,L}^CG_{C,L}^{-1/2}
}
\left(B_{T,m,Z}(L)+\beta_{m,Z,L}\right)
\le
\dim\ker V_Z^C.
}
\tag{T-18501.11}
\]

On the exact packet construction,

\[
\ker V_Z^C=R_L,
\]

where `R_L` is the represented repaired-radical block. Hence

\[
\boxed{
N_{
G_{C,L}^{-1/2}K_{T,L}^CG_{C,L}^{-1/2}
}
\left(B_{T,m,Z}(L)+\beta_{m,Z,L}\right)
\le\dim R_L.
}
\tag{T-18501.12}
\]

This is the requested inequality.

The stronger direct visible floor also holds on the metric orthogonal
complement:

\[
\boxed{
S_{U,L}|_{R_L^{\perp_{G_C}}}
\succeq\beta_{m,Z,L}G_{C,L}.
}
\tag{T-18501.13}
\]

No principal-angle theorem and no numerical singular-value count are needed.

## 4. Existence of the moat at every fixed finite stage

For fixed finite `m`, `Z`, and `T`, the exact supported cardinal synthesis
converges to its global counterpart and the packet metric Gram converges to a
finite positive Gram. Therefore

\[
\Lambda_{m,Z,L}=O_{m,Z,T}(1)
\tag{T-18501.14}
\]

along a sufficiently large support tail. Equation (T-18501.9) gives
`B_(T,m,Z)(L)->0`. Consequently there exists `L_0` such that, for every
`L>=L_0`,

\[
B_{T,m,Z}(L)<\frac1{2\Lambda_{m,Z,L}}.
\tag{T-18501.15}
\]

At such a support choose, for example,

\[
\boxed{
\beta_{m,Z,L}
=\frac12\left(
 \Lambda_{m,Z,L}^{-1}-B_{T,m,Z}(L)
 \right)>0.
}
\tag{T-18501.16}
\]

Then (T-18501.10) holds strictly. The finite zero block may be enlarged if
useful, but unbounded zero-height certification is neither assumed nor needed.

## 5. Cofinal growing diagonal

Let `Z_j` be any sequence of finite proof-grade critical-line zero sets and let
`m_j->infinity` be any growing radical ranks. The zero sets may be fixed, grow
inside any available certified pool, or be produced one finite set at a time;
no claim that all zeros below an unbounded height are on the line is used.

At stage `j`, freeze the finite data `(m_j,Z_j,T_j)`. Choose `L_j>L_(j-1)` so
large that:

1. the exact finite-section cardinal and radical repairs are valid;
2. the represented evaluation map has its exact right inverse;
3. the metric Gram is positive and its right-inverse bound `Lambda_j` is finite;
4. the source-bound residual satisfies
   \[
   B_j<\frac1{2\Lambda_j};
   \tag{T-18501.17}
   \]
5. all cardinal-tail, radical-tail, and Schur losses required by `T-14306` are
   below `2^-j`.

Put

\[
\beta_j
=\min\left\{
 2^{-j},
 \frac12(\Lambda_j^{-1}-B_j)
\right\}>0.
\tag{T-18501.18}
\]

Then

\[
\boxed{
N_{
G_{C,j}^{-1/2}K_{T_j,j}^CG_{C,j}^{-1/2}
}
\left(B_j+\beta_j\right)
\le\dim R_j
}
\tag{T-18501.19}
\]

at every stage. No uniform lower bound for `|Xi'(gamma)|`, no uniform cardinal
condition number, and no complexity bound are required: support is chosen after
each finite packet.

## 6. Composition with the three-block route

Equation (T-18501.13) supplies exactly

\[
B_{V,j}-h_j^{-1}Z_j^*M_j^{-1}Z_j
\succeq\beta_jG_{V,j}>0
\tag{T-18501.20}
\]

on the constructed visible complement. With the exact ambient energy metric one
may take `M_j=C_j`, `h_j=1`. The radical-tail and assembly rates of `T-14306`,
`L-15308`, and `L-15306` then produce a cofinal lower floor for this constructed
packet.

## 7. Exact scope and the remaining global theorem

Equation (T-18501.19) closes the boxed count **for the exact packet constructed
from selected Xi-cardinal coordinates and repaired global radicals**.

It does not prove that this packet captures a prescribed complete dangerous
low-symbol hierarchy. Under the complete-low reading, `T-14307` constructs from
any hypothetical off-line zero a negative selected-real-zero-kernel direction.
Therefore a theorem identifying the constructed packet with the complete low
index, or an equivalent weighted-deficit/capacity saturation certificate, still
carries the global RH content.

Accordingly:

- the right-inverse count is no longer an independent analytic blocker;
- the remaining problem is packet capture, not selected-zero conditioning;
- no unconditional RH claim is made without that capture theorem.

## 8. Proof boundary

- The finite count and direct visible floor are exact.
- The cofinal choice uses fixed-packet cardinal/radical tail convergence, not an
  unbounded verification of all zeros.
- Source normalization, selected-zero provenance, harmonic-lift domain, and the
  source-bound residual estimate remain external gates.
- Complete-low-packet capture remains open and cannot be replaced by a bare
  dimension comparison.
