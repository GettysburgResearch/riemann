# T-23701 — Reflected Bohr contagion proposal: corrected disposition

Claim ID: `T-23701`  
Title: Conditional RH chain from bounded-rank contagion  
Status: **GAP/BLOCKED — LOAD-BEARING `BCT(K)` REFUTED BY `R-23702`**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Corrected: 2026-08-07  
Issue: #237

## 1. Conditional chain that remains valid

Let

\[
I_c(x)=M(x)-M(cx),
\qquad
Q_c(t)=e^{-t/2}I_c(e^t).
\]

The fixed-ratio shell transform is

\[
\mathcal LQ_c(z)
={1-c^{z+1/2}\over(z+1/2)\zeta(z+1/2)},
\]

so subexponential block energy of `Q_c` is RH-equivalent in the imported
normalization.

The exact finite inverse packet, direct terminal/balanced partition, terminal
Euler cancellation, and multiplicative Bohr lift remain valid proposed inputs.
If one had a balanced recurrence

\[
E_K(J)
\le
\exp\{(\varepsilon_K+o_K(1))J\}
\left[1+\max_{u\le(1-\delta)J+O_K(1)}E_K(u)\right]
\]

with `epsilon_K -> 0`, the inherited scale-contraction theorem would imply RH.

## 2. Failed completion mechanism

The original proposal attempted to obtain

\[
\varepsilon_K={C_0\over K}
\]

by proving that every surviving same-scale resonance face had absolute rank at
most `C_0`.

`R-23702` refutes that assertion.  The exact fixed-logarithm Möbius slice
contains balanced squarefree product cubes of arbitrary rank `K`, with all
products inside one fixed-ratio shell and all fully recombined coefficients
nonzero.  Collapsing the factors to one product coordinate replaces rank `K`
by a coordinate of full output-scale range and does not recover the `C_0/K`
enumeration loss.

Therefore equations in the original proposal that used the bounded-rank count
to close the balanced recurrence are withdrawn.

## 3. Correct remaining theorem

The exact arithmetic frontier is again the source-specific signed balanced
Möbius estimate:

\[
\boxed{
E_K(J)
\le
\exp\{(\varepsilon_K+o_K(1))J\}
\left[1+\max_{u\le(1-\delta)J+O_K(1)}E_K(u)\right],
\qquad
\varepsilon_K\to0.
}
\]

A proof must cancel high-rank opposite-parity families after complete source
recombination.  Generic rank, cluster-operator, or endpoint-count arguments are
insufficient.

## 4. Status

```text
fixed-ratio Möbius shell / RH transfer      retained proposed exact
finite inverse and terminal closure          retained proposed
exact multiplicative Bohr lift               retained proposed exact
absolute bounded-rank contagion BCT(K)       refuted
C_0/K balanced estimate                      withdrawn
signed balanced Möbius contraction           open / RH-bearing
Riemann Hypothesis                            unproved
```

The frozen full-proposal version remains visible in Git history.  It must not be
passed to reviewers as a valid completed proof.
