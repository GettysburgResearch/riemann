# R-19845 — An unshifted complete relative Loewner bound already contains RH

Claim ID: `R-19845`  
Status: **PROVED SCOPE REFUTATION**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-07  
Scope: corrects the proof boundary of `T-19811` and every complete unshifted local-Weyl proposal

## 1. Statement

Let `Q_L` be the localized Weil form on a support interval increasing to the
whole logarithmic line, and let `D_L>=0` be any nonnegative form whose domain
contains a common compactly supported Weil core. Suppose along a cofinal support
sequence

\[
 \boxed{
 Q_L\succeq(1-\eta_L)c_LD_L,
 \qquad c_L>0,
 \qquad 0\le\eta_L<1.}
 \tag{R-19845.1}
\]

Then `Q_L>=0` on the complete common form core for every sufficiently large
selected support. Consequently the global Weil form is nonnegative on every
compactly supported test function, and Weil's criterion gives RH.

Thus a hypothesis such as

\[
 (1-\eta_L)(\log R_L)D_L
 \preceq Q_L
 \preceq(1+\eta_L)(\log R_L)D_L
 \tag{R-19845.2}
\]

is not a routine local-Weyl input preceding the RH argument. Its lower half is
already the cofinal positivity theorem.

## 2. Proof

Fix a compactly supported test function `f`. For every sufficiently large
selected support, `f` belongs to the localized form domain. Equation
(R-19845.1) gives

\[
 Q_W(f,f)=Q_L(f,f)\ge0.
\]

The value is independent of enlarging the support after it contains `supp f`.
Hence the global Weil form is nonnegative on the compact core. Continuity extends
the inequality to the full Weil test space. Weil's criterion gives RH. QED.

## 3. Correct replacement

The noncircular spectral target is affine and one-sided:

\[
 \boxed{Q_L-\sigma_LH_L\succeq c_LD_L,}
 \tag{R-19845.3}
\]

where `sigma_L` may be negative, together with a target-only upper bound

\[
 Q_L(p_L,p_L)-\sigma_L\le C_LD_L(p_L,p_L).
 \tag{R-19845.4}
\]

If the target energy is negligible relative to the second `D_L` min--max value,
`L-19861` gives a simple isolated even ground state without asserting
`Q_L>=0`.

## 4. Consequence for the repository stack

The following status boundary is mandatory:

```text
unshifted complete lower Loewner estimate: RH-bearing theorem itself;
affine shifted complement estimate:       legitimate intermediate target;
two-sided complete scalarization:          stronger than required.
```

The corrected full proposal must therefore use `L-19861`, not the unshifted
hypothesis in the frozen `T-19811`.