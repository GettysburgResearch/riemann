# C-98010 — Clarification of the finite-cell notation in `L-98014`

Status: **CONTROLLING TRANSCRIPTION CLARIFICATION; NO THEOREM CHANGE**

In the finite-cell paragraph of `L-98014`, the symbol called `I_N` should be read as the value of the full integral at `x`, and therefore should not carry the subscript `N`. The unambiguous form is as follows.

Put

\[
J_N=\int_1^N{A(t)\over\sqrt t}\,dt.
\]

For `N<x<N+1`,

\[
\int_1^x{A(t)\over\sqrt t}\,dt
=J_N+2A(N)(\sqrt x-\sqrt N),
\]

and hence

\[
\boxed{
\mathcal T_x
=4A(N)\sqrt x+{3\over2}J_N-3A(N)\sqrt N.
}
\]

Thus `mathcal T_x` is affine in `sqrt(x)` on the cell, with slope `4A(N)`. Its cell minimum is at the left or right endpoint according to the sign of `A(N)`. The global root still has a jump at an integer activation because `T(1)=1`; both one-sided states must be checked.
