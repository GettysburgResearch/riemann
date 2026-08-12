# L-91553 — A fixed-`67` positive source has an exact finite target, score, and row peeling

Claim ID: `L-91553`  
Status: **PROVED EXACT SOURCE-LEVEL TELESCOPE — PHYSICAL QUANTIZATION LEDGER SEPARATE**  
Created: 2026-08-13  
Depends on: positive kernels `L-91339/L-91343`, fixed split `L-91547`, component-row monotonicity  
RH status: **unproved**

## 1. Positive source ledgers

For real `x>=1` and integer `n<=x`, put

\[
 W_\Psi(x,n)=\frac{4\sqrt x}{n}-\frac3{\sqrt n},
 \qquad
 W_S(x,n)=\frac{5\sqrt x}{n}-\frac3{\sqrt n}.
\tag{L-91553.1}
\]

Let `nu` be any finite positive source measure on the positive integers.  Define

\[
 T_x(\nu)=\sum_{n\le x}\nu(n)W_\Psi(x,n),
 \qquad
 S_x(\nu)=\sum_{n\le x}\nu(n)W_S(x,n),
\tag{L-91553.2}
\]

and, for every component row `j>=2`,

\[
 D_{x,j}(\nu)
 =\sum_{n\le x}\nu(n)n^{-1/2}Q_{x/n}(j).
\tag{L-91553.3}
\]

All three ledgers are nonnegative.

Fix

\[
 p=67,
 \qquad r=p^{-1/2},
 \qquad x_d=xp^{-d},
\]

and let

\[
 \nu_d=\nu\big|_{n\le x_d}.
\tag{L-91553.4}
\]

Since `nu` is finite, `nu_d=0` for every sufficiently large `d`.

## 2. One-step residual ledgers

Define

\[
 \Delta T_d
 =T_{x_d}(\nu_d)-T_{x_{d+1}}(\nu_{d+1}),
\tag{L-91553.5}
\]

\[
 \Delta S_d
 =S_{x_d}(\nu_d)-S_{x_{d+1}}(\nu_{d+1}),
\tag{L-91553.6}
\]

and

\[
 \Delta D_{d,j}
 =D_{x_d,j}(\nu_d)-D_{x_{d+1},j}(\nu_{d+1}).
\tag{L-91553.7}
\]

Split the source into the inner region `n<=x_{d+1}` and the activation frontier
`x_{d+1}<n<=x_d`.  Direct algebra gives

\[
\boxed{
\begin{aligned}
 \Delta T_d={}&
 4(1-r)\sqrt{x_d}
 \sum_{n\le x_{d+1}}\frac{\nu(n)}n\\
 &+\sum_{x_{d+1}<n\le x_d}
   \nu(n)W_\Psi(x_d,n),
\end{aligned}}
\tag{L-91553.8}
\]

and

\[
\boxed{
\begin{aligned}
 \Delta S_d={}&
 5(1-r)\sqrt{x_d}
 \sum_{n\le x_{d+1}}\frac{\nu(n)}n\\
 &+\sum_{x_{d+1}<n\le x_d}
   \nu(n)W_S(x_d,n).
\end{aligned}}
\tag{L-91553.9}
\]

Every term is nonnegative.  More strongly,

\[
\boxed{
\begin{aligned}
 \Delta S_d-\Delta T_d={}&
 (1-r)\sqrt{x_d}
 \sum_{n\le x_{d+1}}\frac{\nu(n)}n\\
 &+\sqrt{x_d}
 \sum_{x_{d+1}<n\le x_d}\frac{\nu(n)}n
 \ge0.
\end{aligned}}
\tag{L-91553.10}
\]

Thus each current-generation residual is score-favorable pointwise; no source
mass is being substituted for a score weight.

For the rows,

\[
\boxed{
\begin{aligned}
 \Delta D_{d,j}={}&
 \sum_{n\le x_{d+1}}\frac{\nu(n)}{\sqrt n}
 \left[Q_{x_d/n}(j)-Q_{x_{d+1}/n}(j)\right]\\
 &+\sum_{x_{d+1}<n\le x_d}
   \frac{\nu(n)}{\sqrt n}Q_{x_d/n}(j).
\end{aligned}}
\tag{L-91553.11}
\]

The component function `Y->Q_Y(j)` is increasing.  Hence

\[
 \boxed{
 \Delta D_{d,j}\ge0
 }
\tag{L-91553.12}
\]

for every `d,j`.

## 3. Finite exact telescope

Choose `D` with `nu_D=0`.  Summing the definitions gives

\[
 \boxed{
 T_x(\nu)=\sum_{d=0}^{D-1}\Delta T_d,
 }
\tag{L-91553.13}
\]

\[
 \boxed{
 S_x(\nu)=\sum_{d=0}^{D-1}\Delta S_d,
 }
\tag{L-91553.14}
\]

and, for every row,

\[
 \boxed{
 D_{x,j}(\nu)=\sum_{d=0}^{D-1}\Delta D_{d,j}.
 }
\tag{L-91553.15}
\]

Every summand on the right is positive.  Each original source atom exits at the
unique first depth where it lies in the activation frontier, while its earlier
inner contributions are the positive harmonic dilation differences.

If `T_x(nu)>0`, define

\[
 \theta_d=\frac{\Delta T_d}{T_x(\nu)}.
\tag{L-91553.16}
\]

Then

\[
 \boxed{
 \theta_d\ge0,
 \qquad
 \sum_d\theta_d=1.
 }
\tag{L-91553.17}
\]

Moreover, omitting zero-target residuals,

\[
 \boxed{
 \frac{S_x(\nu)}{T_x(\nu)}
 =\sum_d\theta_d
   \frac{\Delta S_d}{\Delta T_d}.
 }
\tag{L-91553.18}
\]

This is the exact target-normalized score law.  The coefficients are target
fractions and the score ratios remain inside the summands.  No assertion of the
form “source-mass fraction implies score-loss fraction” is used.

## 4. Root Hall-projection consequence

Suppose a signed arithmetic reset packet has target `T_sig`, endpoint score
`S_sig`, and exact component rows `D_sig,j`, and a Hall projection supplies one
positive measure `nu` satisfying

\[
 T_x(\nu)=T_{\rm sig},
 \qquad
 S_x(\nu)\ge S_{\rm sig},
 \qquad
 D_{x,j}(\nu)=D_{{\rm sig},j}\ge0.
\tag{L-91553.19}
\]

These are precisely the target-exact, score-superordinate and row-positive
interfaces of the terminal Hall producer.

Then (L-91553.13)--(L-91553.15) give one finite positive decomposition of the
**same arithmetic target and rows**, and its total source score satisfies

\[
 \boxed{
 \sum_d\Delta S_d
 =S_x(\nu)
 \ge S_{\rm sig}.
 }
\tag{L-91553.20}
\]

Thus the fixed-`67` source telescope has no intrinsic score debt at all.  Any
remaining debt can arise only when the positive residual rows are converted to
finite endpoint weights and the finite mismatch/collar/terminal corrections
are charged.

## 5. Native-loss meaning and remaining interface

At source level this theorem removes the false mass-to-score inference that
blocked the withdrawn parallel proof:

```text
parent target fractions                    exact probability vector;
parent score                               exact sum of residual scores;
every residual score minus target          nonnegative;
every exact component row                  positive;
number of nonzero generations              finite.
```

To conclude a bound for the original signed entropy-score loss one must still
prove, in one physical construction, that:

1. every residual row is quantized into ordinary/radix-four endpoint weights;
2. all colors at one depth are summed before quantization;
3. the mismatch, collar, endpoint port and terminal annulus are charged once;
4. the endpoint score of the physical packing is the source score in
   (L-91553.14), up to the stated bounded local debt.

Those are physical ledger statements, not source-telescope statements.  They
are not asserted by this lemma.

```text
fixed-67 target telescope                         EXACT
fixed-67 score telescope                          EXACT
score-favorable residuals                         EXACT
fixed-67 component-row telescope                  EXACT
mass-to-score shortcut                            NOT USED
root Hall score superordination                   PRESERVED EXACTLY
physical one-use quantization/collar ledger       OPEN REVIEW
native signed-loss conclusion                     DEPENDS ON THAT LEDGER
Riemann Hypothesis                                UNPROVEN
```
