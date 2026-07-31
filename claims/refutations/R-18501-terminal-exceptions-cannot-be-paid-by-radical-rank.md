# R-18501 — Terminal exceptions cannot be paid by the radical rank

Claim ID: `R-18501`  
Title: The radical packet already consumes the complete low-index budget; every exceptional visible direction adds to it  
Status: `PROVED REFUTATION / SCOPE CORRECTION`  
Authoring agent: `gpt56-pro-09-h`  
Created: 2026-08-01  
Dependencies: Courant--Fischer; `L-18503`; `L-18506`  
Scope: Section 4 of `L-18506`

## 1. Refuted implication

`L-18506` correctly proves that, on a two-end visible block

\[
 \mathcal S_V=
 \begin{pmatrix}D_+&H^*\\H&D_-\end{pmatrix},
 \qquad D_\pm\succeq gI,
\]

a rank-`k` approximation to the terminal block and a rank-`l` harmonic
correction give

\[
 N_{\mathcal S_V}(\Gamma)\le k+l.
 \tag{R-18501.1}
\]

The later claim that

\[
 k+l\le\dim R
 \quad\Longrightarrow\quad
 N_{\mathcal S_U}(\Gamma)\le\dim R
 \tag{R-18501.2}
\]

for the full packet

\[
 U=R\oplus V_+\oplus V_-
 \tag{R-18501.3}
\]

is false. The `dim R` near-radical modes already lie below every fixed positive
`Gamma`; they are not unused capacity that can absorb visible exceptions.

## 2. Exact three-dimensional counterexample

Take

\[
 \dim R=1,
 \qquad
 \dim V_+=\dim V_-=1,
 \qquad
 g=2,
 \qquad
 \Gamma=1.
\]

Let the radical block be zero and decoupled, and let the visible block be

\[
 \mathcal S_V=
 \begin{pmatrix}2&2\\2&2\end{pmatrix}.
 \tag{R-18501.4}
\]

The terminal map has one singular value

\[
 s_1(H)=2>g-\Gamma=1,
\]

so `k=1`. Take no harmonic correction, so `l=0`. Hence

\[
 k+l=1=\dim R.
 \tag{R-18501.5}
\]

Nevertheless the full matrix is

\[
 \mathcal S_U=
 \begin{pmatrix}
 0&0&0\\
 0&2&2\\
 0&2&2
 \end{pmatrix},
 \tag{R-18501.6}
\]

with spectrum

\[
 \{0,0,4\}.
\]

Therefore

\[
 \boxed{
 N_{\mathcal S_U}(1)=2>1=\dim R.}
 \tag{R-18501.7}
\]

This refutes (R-18501.2) exactly.

## 3. Correct codimension accounting

Suppose a visible subspace `W_V subset V_+ direct_sum V_-` has codimension at
most `k+l` inside the visible block and satisfies

\[
 \mathcal S_V|_{W_V}\succeq\Gamma I.
\]

Viewed as a subspace of the full packet `U`, its codimension is

\[
 \boxed{
 \operatorname{codim}_U W_V
 =\dim R+\operatorname{codim}_V W_V
 \le\dim R+k+l.}
 \tag{R-18501.8}
\]

Courant--Fischer therefore yields only

\[
 \boxed{
 N_{\mathcal S_U}(\Gamma)
 \le\dim R+k+l,}
 \tag{R-18501.9}
\]

before treating radical--visible cross terms. This is sharp in the control
(R-18501.6).

To obtain the exact saturation count

\[
 N_{\mathcal S_U}(\Gamma)\le\dim R,
\]

one needs `k=l=0`, or a separate theorem proving that every exceptional visible
direction is lifted above `Gamma` by the complete coupled form. Merely increasing
the radical rank does not help: each additional near-radical direction also adds
one eigenvalue below the positive threshold.

## 4. Interaction with the inverse-Ritz theorem

`L-18503` requires a high subspace `W subset U` satisfying

\[
 \operatorname{codim}_U W\le\dim R.
 \tag{R-18501.10}
\]

A visible high subspace with `k+l` discarded directions has codimension
`dim R+k+l`, not `dim R`. Thus it cannot be inserted into `L-18503` unless no
visible exception is discarded.

Equivalently, the correct terminal/harmonic target for the complete count is the
strict moat

\[
 \boxed{
 \|H-F_0\|+\kappa<g-\Gamma
 \quad\text{with rank }F_0=0,}
 \tag{R-18501.11}
\]

or a direct finite Schur theorem showing positivity of the exceptional block.
A positive number of terminal exceptions remains part of the RH-sensitive
visible index.

## 5. Off-line-zero consistency check

A hypothetical off-line zero supplies one additional negative Weil-cardinal
direction beyond every near-radical packet. The false implication (R-18501.2)
would allow that direction to be hidden merely by choosing a radical packet of
large dimension, contradicting the exact cardinal obstruction. The corrected
count (R-18501.9) preserves the extra index exactly.

## 6. Surviving statements

The following parts of `L-18506` remain valid:

1. the two-end visible-block theorem;
2. the approximation-number certificate on that visible block;
3. the rank accounting for a positive harmonic correction within the visible
   block;
4. the Schatten bounds for the number of visible exceptions.

Only the promotion from a visible exception count to full radical-count
saturation is refuted.

## 7. Proof boundary

The counterexample and codimension correction are finite exact linear algebra.
No zeta normalization or asymptotic input is involved. This correction neither
proves nor disproves RH; it prevents a false dimension-only closure.