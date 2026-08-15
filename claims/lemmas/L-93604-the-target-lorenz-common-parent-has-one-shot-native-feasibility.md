# L-93604 — The Target-Lorenz common parent has one-shot native feasibility

Claim ID: `L-93604`  
Status: **PROPOSED COMPLETE ALL-COLUMN REALIZATION ON FROZEN ENDPOINT ESTIMATES — REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-93603`, `R-93600`, `L-91733`, frozen terminal omission theorem, positive radix-four inversion  
Replay: `X-93601-target-lorenz-native-endpoint`  
RH status: **unproved**

For integer `X>=10^12`, put

\[
K=\left\lfloor X/67\right\rfloor+1,
\qquad
\tau_K=\frac{\sqrt K}{\sqrt K+130}.
\]

## 1. Ideal one-parent identity

Before finite endpoint observation, the exact source-tree identity and the
pointwise Target-Lorenz replacement show that the common ideal row uses the
same native parent datum as the original signed source. Genuine bottom/top
omissions remove positive source, and the common thinning is applied once.
Thus the ideal retained detail use is at most

\[
\tau_K\Omega_X.
\tag{L-93604.1}
\]

This is derived from the source identity; it is not obtained by reserving a
copy of `Omega(child)` for every internal child colour.

## 2. Separate signed observation ledger

Let `e_X` be the combined retained-cell finite/continuum and intrinsic collar
comparison after the one global quantizer. It is a signed observation vector,
not a positive source packet. `L-91733` proves, for every nonterminal physical
column `q>=2`,

\[
|e_X(q)|<\frac{971}{4q\sqrt K},
\qquad
\frac{|e_X(q)|}{\Omega_X(q)}<\frac{129}{\sqrt K}.
\tag{L-93604.2}
\]

Hence the actual finite row `d_X` satisfies

\[
\begin{aligned}
\Xi_{d_X}(q)
&<\tau_K\left(1+\frac{129}{\sqrt K}\right)\Omega_X(q)\\
&=\frac{\sqrt K+129}{\sqrt K+130}\Omega_X(q)
<\Omega_X(q).
\end{aligned}
\tag{L-93604.3}
\]

This includes the full range `2<=q<K`; no small physical column is omitted.

## 3. Terminal and ordinary columns

The frozen top-omission comparison leaves strict terminal reserve

\[
581X^{-3/2}>0,
\]

and triangular support gives zero response above the retained endpoint range.
Therefore

\[
\boxed{
 d_X\ge0,
 \qquad
 \Xi_{d_X}(q)\le\Omega_X(q)
 \quad(q\ge2).
}
\tag{L-93604.4}
\]

Positive radix-four inversion gives simultaneously

\[
\boxed{C_{d_X}(q)\le w_X(q).}
\tag{L-93604.5}
\]

Only after (L-93604.4) is proved do we define

\[
\boxed{r_X=\Omega_X-\Xi_{d_X}\ge0.}
\tag{L-93604.6}
\]

The exported recursive family is empty: all actual rough-child responses are
internal colours of `d_X`. The root-global matrix port and large-`X` base
correction are identically zero. This is a one-use native allocation, not a
recursion over promoted full child capacities.
