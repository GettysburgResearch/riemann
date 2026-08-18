# L-97632 — High-child parity contraction gives the strict `1/960` margin

Claim ID: `L-97632`  
Status: **PROPOSED SOURCE-COMPLETE INDUCTION; ATOMWISE ROOT IDENTITY IS THE REVIEW TARGET**  
Depends on: `L-97630`, `L-97631`

Only children with
\[
y_i=\frac{x}{p_i}\ge239
\]
remain recursive. Put
\[
h_x=\sum_{y_i\ge239}\alpha_iM(y_i).
\]
Monotonicity of the unsigned source and the factor-67 coefficient estimate give
\[
h_x<\frac18M(x).
\]

For the complete current packet `C_x`, the corrected bias gives
\[
\frac1{40}(M(x)-h_x)
\le f(C_x)
<\frac16(M(x)-h_x).
\]
Assume inductively
\[
0\le f(P_{y_i})\le\frac16M(y_i).
\]
The parity-covariant parent identity is
\[
f(P_x)=f(C_x)-\sum_{y_i\ge239}\alpha_i f(P_{y_i}).
\]
Consequently
\[
\begin{aligned}
f(P_x)
&\ge\frac1{40}(M-h_x)-\frac16h_x\\
&=\frac1{40}M-\frac{23}{120}h_x\\
&>\left(\frac1{40}-\frac{23}{120}\frac18\right)M\\
&=\boxed{\frac1{960}M>0}.
\end{aligned}
\]
The upper bound `f(P_x)<=M(x)/6` is inherited simultaneously. Rank decreases
by at least a factor `67`, so the proposed induction is finite for each endpoint.

The remaining hostile-review obligation is atomwise: the current and high
children must be disjoint literal subobjects of the native source, preserve
activation and coefficients, and have root signed marginal exactly equal to
the annular scalar.
