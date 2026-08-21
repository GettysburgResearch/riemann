# O-32302 — The first arithmetic wall in SHARP begins at quotient eight

Status: **EXACT SCOPE OBSERVATION**

`L-32304` proves every coefficient `c_T(j)>0` for `j>T/8`.

The reason the proof stops exactly there is visible already in the finite Mobius state. For

\[
K=\left\lfloor\frac{T}{j}\right\rfloor,
\qquad
u_T(j)=\frac{A_K}{\sqrt j}-\frac{M_K}{\sqrt T},
\]

one has the same partial sums at `K=7,8,9`, because `mu(8)=mu(9)=0`:

\[
A_7=A_8=A_9,
\qquad
M_7=M_8=M_9=-2.
\]

But the ratio interval `T/j in [8,9)` is large enough that

\[
2+A_7\sqrt{T/j}
\]

can cross zero. Thus positivity of the underlying Mobius state, which was sufficient in the outer seven eighths, is no longer available from quotient `K=8` onward.

SHARP itself remains positive in every directed endpoint test on PR #329 through `T=10^6`. Therefore the inner eighth is not known to fail; rather, it is the first region where the normalized tail `S_T(j)/(j-1)` must genuinely compensate negative local Mobius states.

This is the correct next target for a direct SHARP proof. It is not an invitation to extrapolate finite signs.
