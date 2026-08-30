# R-104514 — A derivative-line proportion alone cannot control its parent

Claim ID: `R-104514`  
Status: **EXACT MECHANISM REFUTATION**  
Created: 2026-08-23  
RH status: **unproved**

## Statement refuted

There is no function `C:(0,1] -> (0,1]` such that every even real Cartwright
entire function `f` satisfies

\[
P_{\mathbb R}(f')\ge p
\quad\Longrightarrow\quad
P_{\mathbb R}(f)\ge C(p),
\]

where `P_R` is the asymptotic proportion of zeros on the real axis, counted
with multiplicity in symmetric boxes.

## Exact counterexample

Take

\[
f(z)=2+\cos z.
\]

This is even, real entire, of exponential type one, bounded on the real axis,
and therefore belongs to the Cartwright class.

For real `x`,

\[
f(x)=2+\cos x\ge1,
\]

so `f` has no real zero.

Its derivative is

\[
f'(z)=-\sin z,
\]

whose zeros are precisely `pi Z`, all real and simple.  Thus

\[
P_{\mathbb R}(f')=1,
\qquad
P_{\mathbb R}(f)=0.
\]

For completeness, the zeros of `f` satisfy `cos z=-2`.  Writing
`z=x+iy`, the imaginary part is `-sin x sinh y`.  Since no real `x` has
`cos x=-2`, one must have `x=(2j+1)pi` and

\[
\cosh y=2,
\qquad
 y=\pm\operatorname{arcosh}2.
\]

All parent zeros are therefore genuinely nonreal.

## Xi consequence

A lower bound for the critical-line proportion of `xi'''` cannot, by itself,
produce any positive lower bound for `xi''`.  Any successful Xi reverse-Rolle
theorem must use an additional source-visible hypothesis.  The exact residue
coherence in `L-104522` is one possible hypothesis; it is not presently known
for Xi at level three.

This refutation does not contradict Conrey's independent fixed-order theorem,
which directly proves a positive—and much stronger—bound for `xi''`.
