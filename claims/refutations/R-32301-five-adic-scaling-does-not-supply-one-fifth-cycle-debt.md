# R-32301 — Five-adic scaling does not by itself supply a factor-one-fifth Cycle-Debt contraction

Claim ID: `R-32301`  
Title: The critical square-root capacity mode is neutral under factor-five dilation; any strict five-adic contraction must be produced by an additional arithmetic cycle theorem  
Status: **EXACT SCOPE CORRECTION / CROSS-BRANCH FIREWALL**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Target: PR #322 `T-30107` and its phrase "expected contraction is the exact scaling reserve 1/5"  
Scope: refutes the claim that the coefficient `1/5` follows from critical scaling alone; does not refute existence of a nontrivial five-state cycle certificate

## 1. Exact critical source scaling

Retain the prime-ramp target

\[
w_X(q)=q^{-1/2}\log(X/q)
\]

and its Möbius divergence `r_X`.  For `X=5Y`, PR #322 correctly proves

\[
\boxed{
\sum_{j=0}^4r_X(5a+j)=5^{-1/2}r_Y(a).
}
\tag{R-32301.1}
\]

The factor `5^{-1/2}` is exactly critical for the source-adapted capacity metric of PR #272, whose balanced edge weights satisfy

\[
\omega_{n,j}\asymp_\eta \sqrt n.
\]

Scaling node labels by five multiplies the natural square-root capacity by `sqrt(5)`. Consequently the coefficient `5^{-1/2}` cancels that scaling at first order. It does not create a factor `1/5` reserve.

## 2. Exact finite witness

For the central edge `[2,1]`,

\[
\omega_{2,1}=2^{-1/2}.
\]

Its literal factor-five lift is `[10,5]`, with

\[
\omega_{10,5}
=2^{-1/2}+3^{-1/2}+6^{-1/2}+7^{-1/2}+8^{-1/2}+9^{-1/2}+10^{-1/2}.
\]

Therefore a coefficient scaled by `5^{-1/2}` has capacity ratio

\[
\boxed{
{5^{-1/2}\omega_{10,5}\over\omega_{2,1}}>1.
}
\tag{R-32301.2}
\]

It is enough to retain only the positive columns `q=2,3,6`. Dividing their scaled contribution by `omega_(2,1)=1/sqrt(2)` gives

\[
{1\over\sqrt5}+\sqrt{2\over15}+{1\over\sqrt{15}}.
\]

Each term has the following exact rational lower bound:

\[
{1\over\sqrt5}>{4\over9},
\qquad
\sqrt{2\over15}>{1\over3},
\qquad
{1\over\sqrt{15}}>{1\over4}.
\]

Indeed these reduce after squaring positive quantities to

\[
{1\over5}>{16\over81},
\qquad
{2\over15}>{1\over9},
\qquad
{1\over15}>{1\over16}.
\]

Hence

\[
{1\over\sqrt5}+\sqrt{2\over15}+{1\over\sqrt{15}}
>{4\over9}+{1\over3}+{1\over4}
={37\over36}>1.
\tag{R-32301.3}
\]

This proves (R-32301.2) without floating-point arithmetic.

Thus even the canonical lifted edge is not contracted by `1/5`; its critical capacity is of the same order as the original edge.

## 3. The neutral scalar is the old half-moment

Define

\[
\mathfrak H_X=-\sum_m r_X(m)\sqrt m,
\]

the exact half-moment of PR #277 `L-23812`.

The pure lower-scale component in one five-adic block is

\[
5^{-1/2}r_Y(a)e_{5a}.
\]

Its contribution to the square-root moment is exactly

\[
-5^{-1/2}r_Y(a)\sqrt{5a}
=-r_Y(a)\sqrt a.
\tag{R-32301.4}
\]

Hence the critical mode has eigenvalue **one**, not `1/5`, under the raw factor-five scaling.

The remaining residue commutators may still modify or cancel this mode, but that is precisely the new arithmetic content which a five-state automaton would have to prove. It cannot be removed from the proof by quotienting the critical mode without a separate estimate.

## 4. Cross-branch identification

PR #277 proves the exact coefficient identity

\[
\mathfrak H_X
=-\sum_{q\le X}h_{1/2}(q)q^{-1/2}\log(X/q),
\]

with reciprocal-zeta Dirichlet series. New `L-32301` further proves

\[
\operatorname{sgn}h_{1/2}(n)=(-1)^{\omega(n)}.
\]

Therefore the mode which PR #322 proposes to quotient is the same coherent parity-sensitive Möbius mode that survived the binary–ternary audit. It is not a harmless scaling eigenvector.

## 5. Correct five-adic frontier

A valid five-adic completion may still exist, but it must prove an identity of the form

\[
\text{critical lower-scale mode}
+\text{four residue commutators}
\longmapsto
\text{strictly smaller Cycle Debt}
\]

using explicit legal Pascal cycles.

A finite matrix on the transverse quotient is insufficient unless the proof also emits the critical-mode row and proves its cancellation or lower-scale payment.

## 6. Verdict

```text
five-block source identity                         RETAINED
finite residue automaton as a research target      RETAINED
factor 1/5 from critical scaling alone              FALSE
critical square-root mode                           NEUTRAL
critical mode = PR #277 half-moment                EXACT IDENTIFICATION
strict five-adic Cycle-Debt recurrence              UNPROVEN
RH                                                   UNPROVEN
```
