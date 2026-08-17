# L-96603 — Every annular terminal leaf and the complete two-row root are positive

Claim ID: `L-96603`  
Status: **CANDIDATE-COMPLETE UNCONDITIONAL PRODUCER THEOREM**  
Created: 2026-08-17  
Depends on: `L-96601`, `L-96602`

A terminal rough current has `Z=py`, where `p>=67` and `1<=y<67`. By
(L-96602.3) and `L-96601`,

\[
\begin{aligned}
 E_{2,Pp}(py)
 &>\frac75-\frac{5/2}{\sqrt{67}}
 >\frac{87}{80}>0,\\
 E_{3,Pp}(py)
 &>\frac12-\frac1{\sqrt{67}}
 >\frac38>0.
\end{aligned}
\tag{L-96603.1}
\]

The strict rational bounds use only `sqrt(67)>8`. A terminal outer packet with
no rough owner has scale below `67` and is nonnegative by the first line of
(L-96601.2).

Now apply the finite tree of `L-96602` to the positive parity-labelled annular
root source. Every coefficient `s_k`, `lambda_i`, and `alpha_i` is nonnegative;
every current leaf satisfies (L-96603.1); every child is treated recursively;
and the process terminates. Therefore the signed observations of the complete
root obey

\[
 \boxed{a_X(2)\ge0,\qquad a_X(3)\ge0\qquad(X\ge1).}
 \tag{L-96603.2}
\]

Here

\[
 a_X(j)=c_X(j)-c_{X/4}(j)
 =\sum_{n\le X}\frac{r_j(n)}{\sqrt n}
   \min\!\left(\log4,\log\frac Xn\right)_+,
\]

with the exact `r_2,r_3` dictionaries of PR #547. The source observation is
therefore the actual two-row annular Riesz state, not a rough lift or promoted
capacity.

Immediate falsifiers are: a failure of the quadrature bound; an event outside
the `P_61` certificate; a duplicated finite color; a negative terminal grouped
row; or a mismatch between the root observation and the Riesz formulas.
