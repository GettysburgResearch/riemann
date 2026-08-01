# R-15111 — Common finite-jet subtraction does not cancel quartic contacts

Claim ID: `R-15111`  
Status: **PROVED EXACT ORDER-FOUR OBSTRUCTION**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `L-15134`; elementary rational matrix algebra  
Scope: refute automatic contact cancellation from common subtraction, grading, and lower moments  
Related counterexample candidates: none

## 1. Statement

A common linear finite-jet subtraction, exact anti-commuting grading, equality of
the quadratic trace, and vanishing cubic traces do **not** imply the genuine
order-four contact-free diagonal identity.

Thus the contact-free theorem requested at the classical source interface needs
the nonlinear Ward identity of `L-15134`; it cannot be inferred from the
already established lower-order structure.

## 2. Exact graded data

Take Gram `G=I_4` and let the grading exchange the first two and last two
coordinates:

\[
 \Gamma=
 \begin{pmatrix}
 0&1&0&0\\
 1&0&0&0\\
 0&0&0&1\\
 0&0&1&0
 \end{pmatrix}.
 \tag{R-15111.1}
\]

Define the raw and renormalized seam operators

\[
 A=\operatorname{diag}(1,-1,2,-2),
 \tag{R-15111.2}
\]

\[
 K=\operatorname{diag}
 \left(\frac{11}{5},-\frac{11}{5},
       \frac25,-\frac25\right),
 \tag{R-15111.3}
\]

and let the finite-jet counterterm operator be

\[
 D=A-K
 =\operatorname{diag}
 \left(-\frac65,\frac65,
       \frac85,-\frac85\right).
 \tag{R-15111.4}
\]

All three matrices are self-adjoint and

\[
 \Gamma A\Gamma=-A,
 \qquad
 \Gamma K\Gamma=-K,
 \qquad
 \Gamma D\Gamma=-D.
 \tag{R-15111.5}
\]

Hence every odd power trace vanishes exactly.

## 3. All lower gates pass

The quadratic traces agree:

\[
 \boxed{
 \operatorname{Tr}A^2
 =\operatorname{Tr}K^2=10.}
 \tag{R-15111.6}
\]

The cubic traces vanish:

\[
 \boxed{
 \operatorname{Tr}A^3
 =\operatorname{Tr}K^3
 =\operatorname{Tr}D^3=0.}
 \tag{R-15111.7}
\]

Take the displayed one-contour counterterm probe to be any fixed linear probe
which, on this datum, has value

\[
 q_4=\operatorname{Tr}D=0.
 \tag{R-15111.8}
\]

Thus the counterterm is invisible to this one-leg scalar readout.

## 4. Quartic contact anomaly

The raw quartic trace is

\[
 \operatorname{Tr}A^4=34,
 \tag{R-15111.9}
\]

whereas the renormalized connected cycle is

\[
 \operatorname{Tr}K^4
 =\frac{29314}{625}.
 \tag{R-15111.10}
\]

Therefore

\[
\boxed{
 \operatorname{Tr}A^4-\operatorname{Tr}K^4
 =-\frac{8064}{625}\ne0.}
 \tag{R-15111.11}
\]

Since `A` and `D` commute, the required quartic Ward counterterm is

\[
\begin{aligned}
 q_4^{\rm required}
 ={}&4\operatorname{Tr}(A^3D)
 -6\operatorname{Tr}(A^2D^2)\\
 &+4\operatorname{Tr}(AD^3)-\operatorname{Tr}D^4.
\end{aligned}
 \tag{R-15111.12}
\]

The component values are

\[
 \operatorname{Tr}(A^3D)=\frac{116}{5},
 \tag{R-15111.13}
\]

\[
 \operatorname{Tr}(A^2D^2)=\frac{584}{25},
 \tag{R-15111.14}
\]

\[
 \operatorname{Tr}(AD^3)=\frac{1616}{125},
 \tag{R-15111.15}
\]

\[
 \operatorname{Tr}D^4=\frac{10784}{625}.
 \tag{R-15111.16}
\]

Substitution gives

\[
\boxed{
 q_4^{\rm required}=-\frac{8064}{625},}
 \tag{R-15111.17}
\]

not the one-leg value `q_4=0`.

Thus the finite scalar and connected cycle disagree at the first nontrivial
even order even though:

1. the same Gram is used;
2. the raw, counterterm, and renormalized operators share one exact grading;
3. the order-two moments agree;
4. cubic parity is exact;
5. the counterterm is invisible to the chosen linear one-contour probe.

## 5. Meaning for collision/contact terms

The anomaly (R-15111.17) is made from mixed cyclic words containing both raw
seam and counterterm insertions.  A linear subtraction removes one one-leg
coordinate. It does not remove these closed mixed loops.

The example is finite and contains no convergence, distribution-extension, or
precision issue. Therefore no window limit, Hilbert--Schmidt majorant, or
identity theorem can repair the mismatch.

## 6. Exact scope

This result does not prove that the manuscript's particular Riemann finite-jet
data have the value (R-15111.17). It proves that the desired cancellation is not
a formal consequence of the hypotheses currently displayed in the manuscript.
A valid proof must establish the nonlinear all-orders Ward hierarchy

\[
 q_\ell=-\mathcal P_\ell(A,D)
\]

for the actual contour tensors, or prove that the counterterm range is a
seam-radical so every contact word vanishes.

## 7. Verdict

\[
\boxed{
 \text{common linear finite-jet subtraction}
 \not\Longrightarrow
 \text{contact-free cyclic diagonal identity}.}
\]

The smallest surviving obstruction is the exact quartic contact anomaly.