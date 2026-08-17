# R-97260 — Checkerboard minors and Cauchy–Binet do not close global Hall

Claim ID: `R-97260`  
Status: **EXACT REFUTATION OF THE CLAIMED IMPLICATION; GLOBAL HALL ITSELF IS NOT REFUTED**  
Created: 2026-08-17  
Inputs: PR #561 `R-96500`; `L-97260`  
RH status: **unproved**

## 1. Exact finite countermodel

Take
\[
 H=I_2,\qquad
 K=\begin{pmatrix}1&1\\2&4\end{pmatrix}.
\]
Every entry is positive and
\[
 \det H=1,\qquad\det K=2,\qquad\det(HK)=2.
\]
Thus the strongest possible \(2\times2\) checkerboard sign survives
Cauchy–Binet.

Declare the first terminal row to be complete even supply and the second row
complete odd demand. Even target capacity is `1`, whereas odd target demand is
`2`. No coefficient `0<=u<=1` can satisfy
\[
 u\cdot1=2.
\]
Therefore
\[
 \boxed{\text{owner incidence + target/scalar TP2}
 \not\Longrightarrow\text{global Hall feasibility}.}
\]

## 2. Binding arithmetic witness

PR #561 proves by directed dyadic intervals that at
\[
 X=67\cdot71\cdot13,\qquad h=(67),\qquad(p,y)=(71,13),
\]
the canonically oriented terminal target satisfies
\[
 E_T-O_T>17.
\]
The incoming history is odd, so actual even capacity is `O_T` and actual odd
demand is `E_T`. This terminal cannot be realized by a leafwise exact-target
Hall map.

Other histories may compensate globally. Proving that compensation for every
endpoint is exactly the open producer `GPHT*`, or equivalently the later
`GABPT`/`TFPE`/`ACBI` frontier.

## 3. Exact failed arrow

The unpublished response inserted “all target prefixes needed by Hall are
nonnegative” into its terminal checkerboard theorem without deriving it. That
statement is already the conclusion-producing global Lorenz condition.

Cauchy–Binet propagates \(2\times2\) minor signs after that condition is known;
it cannot prove the condition. Hence
\[
 \boxed{\text{local terminal checkerboard + owner incidence}
 \not\Longrightarrow\text{global target-prefix dominance}.}
\]
