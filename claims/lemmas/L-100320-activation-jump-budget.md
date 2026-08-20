# L-100320 — Product-threshold Euler activation prefixes lie in `(0,1]`

Claim ID: `L-100320`  
Status: **PROVED EXACT HEREDITARY ACTIVATION THEOREM**  
Created: 2026-08-20  
RH status: **not assumed**

Let the labelled prime activities be

\[
r_i=q_i^{-3/2},
\]

using one label for every ordinary prime and a second distinct label for `67`.
For a finite set `A` of labels write

\[
q_A=\prod_{i\in A}q_i,
\qquad
r_A=\prod_{i\in A}r_i=q_A^{-3/2}.
\]

For `y>=1`, let

\[
\mathcal I_y=\{A:q_A\le y\}
\]

and define the signed activation prefix

\[
S_{3/2}(y)=\sum_{A\in\mathcal I_y}(-1)^{|A|}r_A.
\]

Then

\[
\boxed{0<S_{3/2}(y)\le1.}
\]

## Lower bound

Put

\[
M_j(y)=\sum_{A\in\mathcal I_y,\ |A|=j}r_A
\]

and

\[
R=\sum_i r_i.
\]

The labelled prime sum satisfies `R<1`; this is the elementary `3/2` prime
mass bound already used in the quadratic SHARP positivity theorem.

If `A in I_y` and `i in A`, then `A\setminus{i} in I_y`. Double counting removals gives

\[
jM_j(y)
=\sum_{B\in\mathcal I_y,\ |B|=j-1}r_B
\sum_{i\notin B:\ B\cup\{i\}\in\mathcal I_y}r_i
\le R M_{j-1}(y).
\]

Hence

\[
M_{2k+1}(y)<M_{2k}(y).
\]

Pairing consecutive levels in the finite alternating sum proves
`S_(3/2)(y)>0`.

## Upper bound

Map each nonempty even `A in I_y` to the odd parent obtained by removing its
largest label.  For a fixed odd parent `B`, every preimage is `B union {i}` with
`i>max B`, and its total mass is at most

\[
r_B\sum_{i>\max B}r_i<Rr_B<r_B.
\]

Thus the total mass of nonempty even sets is strictly smaller than the total
mass of odd sets.  Since the empty set contributes one,

\[
S_{3/2}(y)=1+M_{\rm even,nonempty}(y)-M_{\rm odd}(y)\le1.
\]

The duplicate `67` labels are distinct in the ordering and cause no change to
the proof.

## Scope

This theorem closes the sign and size of the complete activation-jump prefix.
It does not orient the continuous critical drift between activations.
