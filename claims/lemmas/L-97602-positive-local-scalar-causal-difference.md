# L-97602 — The unsieved 5:3 scalar has a positive one-prime causal difference

Claim ID: `L-97602`  
Status: **PROVED EXACT NARROW POSITIVITY THEOREM**  
Created: 2026-08-17  
RH status: **not assumed**

Let

\[
Q_*(Y)=5Q_Y(2)+3Q_Y(3)
       =\sum_{m\ge1}{q_*(m)\over\sqrt m}\log(Y/m)_+,
\]

with the positive dictionary of `L-97600`.  For every prime `p>=67` and every
`Y>=p`,

\[
\boxed{Q_*(Y)-p^{-1/2}Q_*(Y/p)\ge0.}
\]

Indeed, for indices not divisible by `p` the difference keeps the positive
coefficient `q_*(n)`.  At indices `pm`, the only nonzero coefficient changes
are

\[
q_*(p)-q_*(1)=6,
\quad q_*(2p)-q_*(2)=-9,
\quad q_*(4p)-q_*(4)=3.
\]

Writing `y=Y/p`, the exceptional contribution, multiplied by `sqrt(p)`, is

\[
b(y)=6\log y-{9\over\sqrt2}\log(y/2)_+
     +{3\over2}\log(y/4)_+.
\]

On `[1,2]` this is `6 log y`.  On `[2,4]` it is affine in `log y` with negative
slope and has positive value `(12-9/sqrt2)log2` at `4`.  On `[4,infinity)` its
slope is `15/2-9/sqrt2>0`.  Hence `b(y)>=0`.

This result is deliberately narrow.  It does not survive arbitrary signed
`P_61` colour convolution and does not compensate completed odd histories.
