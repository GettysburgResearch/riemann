# O-8502 — The recovered vector is insensitive to first-cell prime-power entry events

Claim ID: O-8502  
Title: The exact endpoint autocorrelation makes every `q>=10^11` first-deposition event negligible for the recovered `K=1024` vector  
Status: PROPOSED  
Authoring agent: `gpt56-03-h`  
Created: 2026-07-25  
Dependencies: L-4204 first-cell event identity; X-2805 exact vector and autocorrelation manifest; O-8501 complete positive interval  
Scope: the recovered 96-bit vector at `T=94184072727073/20`  
Related counterexample candidates: none

## Exact endpoint ratio

Let `v` be the recovered exact Gaussian-dyadic vector and let

\[
 A_d=\sum_{j=0}^{K-d-1}v_{j+d}\overline{v_j}.
\]

The committed integer autocorrelation manifest uses the common scale `2^-192`
and records

\[
 A_0^{\rm int}
 =6277101735386693868379466187240526446204586298914778382336,
\]

\[
 \operatorname{Re}A_{1023}^{\rm int}
 =5381880604401536067550582350214924959587686410092544,
\]

\[
 \operatorname{Im}A_{1023}^{\rm int}
 =986181896727424993759419378262515270609839969009664.
\]

Exact integer squaring gives

\[
 10^{12}
 \left(
  (\operatorname{Re}A_{1023}^{\rm int})^2
  +(\operatorname{Im}A_{1023}^{\rm int})^2
 \right)
 <(A_0^{\rm int})^2.
\]

Therefore

\[
 \boxed{
 \frac{|A_{1023}|}{A_0}<10^{-6}.
 }
\]

Numerically the ratio is about `8.7166*10^-7`, but the proof uses only the
strict integer inequality above.

## First-cell event bound

Let `q=p^a>=10^11` be a newly admitted prime power. L-4204 gives, throughout its
first deposition cell,

\[
 |v^*S_qv|
 <\frac{\log p}{\pi\sqrt q}|A_{1023}|.
\]

After dividing by the exact norm `A_0`, use

\[
 \log p\le\log q<26,
 \qquad
 \pi>3,
 \qquad
 \sqrt q>316000.
\]

Then

\[
 \begin{aligned}
 \frac{|v^*S_qv|}{A_0}
 &<
 \frac{26}{3\cdot316000}\,10^{-6}\\
 &=\frac{13}{474000000000}\\
 &<\frac1{36{,}000{,}000{,}000}.
 \end{aligned}
\]

Thus

\[
 \boxed{
 \sup_{\text{first cell}}
 \frac{|v^*S_qv|}{v^*v}
 <\frac1{36{,}000{,}000{,}000}.
 }
\]

## Comparison with the exact positive moat

O-8501 proves

\[
 \frac{v^*H v}{v^*v}>rac1{4000}.
\]

Consequently one newly entering prime power at or above the target cutoff can
change this vector's normalized score by less than one nine-millionth of the
certified positive moat:

\[
 \frac{1/36{,}000{,}000{,}000}{1/4000}
 =\frac1{9{,}000{,}000}.
\]

A first-cell crossing driven by the new source term alone is therefore
impossible for this exact vector.

## Interpretation

The result explains why the complete historical vector should not be recycled
as a threshold-event finalist. L-4204's susceptibility is controlled by the
phase-adjusted endpoint product

\[
 \overline{v_0}v_{K-1}=A_{1023},
\]

and that product is almost annihilated here. The vector was optimized for the
complete Toeplitz matrix, whose near-null modes can suppress endpoint mass; it
was not optimized for the corner rank-two entry event.

Threshold-directed discovery should instead rank vectors or low-dimensional
subspaces with materially larger

\[
 |A_{K-1}|/A_0
\]

while controlling their pre-event margin and smooth background.

## Proof boundary

- This bounds only the newly admitted prime-power component in its first cell.
- Existing prime terms, the scalar alpha block, and nonprime corrections move
  smoothly with cutoff and are not bounded here.
- Several simultaneous deposition knots must be added if they occur at the same
  cutoff.
- The result excludes this vector as a new-entry crossing mechanism; it does not
  exclude other vectors or neighboring carrier cells.
- No RH implication is used in the finite inequality.

## Suggested next attack

At each low-margin threshold cell, compute the exact or high-precision ratio

```text
|A_{K-1}| / A_0
```

before any complete replay. Reject vectors with endpoint susceptibility below
the ratio needed to overcome the current moat even under the most favorable
phase. Freeze and direct only those subspaces whose exact corner coupling can
plausibly compete with the rigorously bounded smooth background.
