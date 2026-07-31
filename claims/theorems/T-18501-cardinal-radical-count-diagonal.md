# T-18501 — Cardinal–radical packets satisfy the certified-zero count cofinally

Claim ID: `T-18501`  
Title: Exact finite-section cardinal repair turns the final count into a right-inverse norm comparison  
Status: `PROPOSED — CONSTRUCTED-PACKET COUNT CLOSED; COMPLETE-LOW CAPTURE SEPARATE`  
Authoring agent: `gpt56-03-m`  
Created: 2026-07-31  
Dependencies: `L-18501`; `T-14306`; `L-14321`; `L-15305`; absolute convergence of the fixed-packet zero tail  
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

Let `G_(C,L)>0` be any declared metric on this finite packet.  The evaluation
map and the right inverse must live on the same represented space.  In
particular, if the packet is first harmonically lifted by a map `J_C`, replace
`V_Z` by the lifted map `V_Z^C=V_ZJ_C` and repeat the same finite right-inverse
repair there; an unlifted right inverse may not be paired with a lifted Gram.
For fixed cardinal data the lifted evaluation matrix tends to the exact global
cardinal identity whenever the harmonic cross tail tends to zero, so the same
Neumann inversion used in `T-14306` applies.  Define

\[
\boxed{
\Lambda_{m,Z,L}
=\lambda_{\max}
 \left(
  \widetilde C_{Z,L}^*G_{C,L}\widetilde C_{Z,L}
 \right).
}
\tag{T-18501.5}
\]

This number is finite and positive.

## 2. Full certified-zero Gram

Let `T` exceed every selected ordinate in `Z`. Let

\[
K_{T,L}^C
\tag{T-18501.6}
\]

be the complete positive Gram of all independently certified critical-line
zeros through height `T`, restricted to `U_(m,Z,L)`, with multiplicities and the
same normalization as `G_(C,L)`. Since this block contains the selected set,

\[
\boxed{
K_{T,L}^C\succeq V_Z^*V_Z.
}
\tag{T-18501.7}
\]

Let `B_(T,L)` be a complete absolute omitted-zero budget such that the exact
finite Schur or Weil form obeys

\[
S_{U,L}\succeq K_{T,L}^C-B_{T,L}G_{C,L}.
\tag{T-18501.8}
\]

For each fixed finite packet, absolute convergence of the zero dictionary gives

\[
B_{T,L}\longrightarrow0
\qquad(T\to\infty).
\tag{T-18501.9}
\]

## 3. Exact count theorem

Choose `beta_(m,Z,L)>0` satisfying

\[
\boxed{
B_{T,L}+\beta_{m,Z,L}
<\Lambda_{m,Z,L}^{-1}.
}
\tag{T-18501.10}
\]

Then `L-18501` gives

\[
\boxed{
N_{
G_{C,L}^{-1/2}K_{T,L}^CG_{C,L}^{-1/2}
}
\left(B_{T,L}+\beta_{m,Z,L}\right)
\le
\dim\operatorname{Ran}K_{m,Z,L}.
}
\tag{T-18501.11}
\]

Since `K_(m,Z,L)` is injective for sufficiently large support,

\[
\dim\operatorname{Ran}K_{m,Z,L}=m.
\tag{T-18501.12}
\]

Thus the requested inequality holds with

\[
R_L=\operatorname{Ran}K_{m,Z,L}.
\]

In fact the stronger direct visible floor holds on the metric orthogonal
complement of `R_L`:

\[
\boxed{
S_{U,L}|_{R_L^{\perp_{G_C}}}
\succeq\beta_{m,Z,L}G_{C,L}.
}
\tag{T-18501.13}
\]

No principal-angle theorem and no numerical singular-value count are needed.

## 4. Existence of the threshold at every fixed finite stage

At a fixed finite packet, choose any rational

\[
0<\beta<\frac1{2\Lambda_{m,Z,L}}.
\tag{T-18501.14}
\]

By (T-18501.9), extend the independently certified zero block until

\[
B_{T,L}<\frac1{2\Lambda_{m,Z,L}}-\beta.
\tag{T-18501.15}
\]

Then (T-18501.10) holds. Extending the certified block does not alter the packet
or its selected right inverse; it only adds positive rank-one terms to
`K_(T,L)^C` and shrinks the omitted-zero budget.

This ordering avoids a circular dependence between the selected cardinal set
and the height used only for tail control.

## 5. Cofinal growing diagonal

Let `Z_j` be any growing sequence of finite certified-zero subsets and let
`m_j->infinity` be any growing radical ranks. For each `j`:

1. choose `L_j` large enough for the exact finite-section repair and all tail,
   metric, and Schur estimates required by `T-14306`;
2. compute or outward-enclose the finite number `Lambda_j` in (T-18501.5);
3. choose, for example,
   \[
   \beta_j=\min\left\{2^{-j},\frac1{4\Lambda_j}\right\};
   \tag{T-18501.16}
   \]
4. extend the certified zero block to a height `T_j` for which
   \[
   B_{T_j,L_j}<\frac1{2\Lambda_j}-\beta_j.
   \tag{T-18501.17}
   \]

Then

\[
\boxed{
N_{
G_{C,j}^{-1/2}K_{T_j,j}^CG_{C,j}^{-1/2}
}
\left(B_{T_j,j}+\beta_j\right)
\le\dim R_j
}
\tag{T-18501.18}
\]

at every stage. No uniform lower bound for `|Xi'(gamma)|`, no uniform cardinal
condition number, and no complexity bound are required: all constants are
finite before the support and tail height are selected.

The cardinal and radical localization errors may be made smaller than any
prescribed function of the already chosen positive `beta_j`; their
superexponential fixed-packet decay dominates the finite right-inverse constant.

## 6. Composition with the three-block route

Apply (T-18501.13) to the exact lifted evaluation map and its exact lifted
right inverse. It supplies exactly

\[
B_{V,j}-h_j^{-1}Z_j^*M_j^{-1}Z_j
\succeq\beta_jG_{V,j}>0
\tag{T-18501.19}
\]

for the constructed visible complement, with the ambient energy metric choice
`M_j=C_j`, `h_j=1` when desired. The radical-tail and assembly rates of
`T-14306`, `L-15308`, and `L-15306` then produce a cofinal lower floor for this
constructed packet.

## 7. Exact scope and the remaining global theorem

Equation (T-18501.18) closes the boxed count **for the exact packet constructed
from selected Xi-cardinal coordinates and repaired global radicals**.

It does not prove that this packet captures a prescribed complete dangerous
low-symbol hierarchy. Under the complete-low reading, `T-14307` constructs from
any hypothetical off-line zero a negative selected-real-zero-kernel direction.
Therefore a theorem identifying the constructed packet with the complete low
index, or an equivalent weighted-deficit/capacity saturation certificate, still
carries the global RH content.

Accordingly:

- the right-inverse count is no longer an independent analytic blocker;
- the remaining problem is packet capture, not selected-zero conditioning or
  zero-tail truncation;
- no unconditional RH claim is made without that capture theorem.

## 8. Proof boundary

- The finite count and direct visible floor are exact.
- The cofinal choice uses only fixed-packet absolute zero-tail convergence.
- Source normalization, certified-zero provenance, harmonic-lift domain, and
  the full omitted-zero envelope remain external gates.
- Complete-low-packet capture remains open and cannot be replaced by a bare
  dimension comparison.
