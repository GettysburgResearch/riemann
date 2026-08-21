# R-21501 — An unrephased quarter-power amplitude does not satisfy the support-sieve derivative gate

Claim ID: `R-21501`  
Status: **PROVED SCOPE CORRECTION**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Target: `L-19821-critical-strip-growth-closes-support-average.md` at PR #202 head `585cda919808429a759cf0bf7ab054af40f9a6d2`

## Statement

The bound

\[
 \|A_\gamma(R)\|+\|\partial_RA_\gamma(R)\|
 \ll R^{1/4}(\log R)^C
 \tag{R-21501.1}
\]

does not imply the amplitude hypothesis of the parent support large sieve
`L-16226`, namely

\[
 \|A_\gamma(R)\|+T\|\partial_RA_\gamma(R)\|
 \le B_T,
 \qquad T\le R\le2T.
 \tag{R-21501.2}
\]

In the actual normalized tail factor

\[
 e^{-isx_R},
 \qquad x_R={1\over2}\log {R\over2\pi},
 \qquad s=\gamma+i\delta,
 \tag{R-21501.3}
\]

the real oscillation contributes

\[
 \partial_Re^{-i\gamma x_R}
 =-{i\gamma\over2R}e^{-i\gamma x_R}.
 \tag{R-21501.4}
\]

For `gamma asymp T` and `R asymp T`, this derivative has the same order as the
amplitude itself.  Hence the left side of (R-21501.2) is larger by a factor
`Theta(T)` if the oscillation remains inside `A_gamma`.

## Exact scalar control

Take the scalar family

\[
 A_\gamma(R)=e^{-i\gamma x_R}
 \tag{R-21501.5}
\]

with `gamma=T` and `R in [T,2T]`.  Then

\[
 |A_\gamma(R)|=1,
 \qquad
 |\partial_RA_\gamma(R)|={T\over2R}\le{1\over2},
 \tag{R-21501.6}
\]

so an unscaled derivative statement of the form (R-21501.1) holds with a
constant envelope.  But

\[
 |A_\gamma(R)|+T|\partial_RA_\gamma(R)|
 =1+{T^2\over2R}
 \ge1+{T\over4},
 \tag{R-21501.7}
\]

which is not subpolynomial and cannot be inserted into the claimed
quarter-power large-sieve bound.

## Correct repair

Move `e^{-i gamma x_R}` into the real support phase and retain only
`e^(delta x_R)` in the amplitude.  The exact repair and the resulting phase
geometry are `L-21503`.

## Consequence

The original `L-19821` support-average conclusion is **GAP/BLOCKED as written**.
The quarter-power magnitude estimate survives, but it does not by itself close
the horizontal-displacement theorem.  `L-21503` is a new proposed theorem and
does not retroactively verify the frozen original.
