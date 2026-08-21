# R-9506 — Coefficient-blind local-to-Bohr transference loses one power

Claim ID: `R-9506`  
Title: Generic Farey-frame and prime-by-prime norm bounds cannot prove the critical analytic-totient moment  
Status: **PROPOSED SCOPE REFUTATION — elementary asymptotic model**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: `L-9513`, `R-9503`

## 1. The model cluster

For \(D<d\le2D\), consider
\[
F_D(x)=\sum_{D<d\le2D}e^{2\pi i x/d}.
\]

Set \(x=Dy\). Uniformly for \(1\le y\le2\),
\[
\frac1D F_D(Dy)
\longrightarrow
\int_1^2 e^{2\pi i y/u}\,du.
\]

The limiting analytic function is not identically zero. Hence
\[
\boxed{
\int_D^{2D}|F_D(x)|^2\,dx\asymp D^3.
}
\tag{R-9506.1}
\]

Thus a coefficient-independent local-to-Bohr inequality loses one full power:
the complete-period square scale is \(D\), whereas a critical physical interval
can carry \(D^3\) energy for an unsigned cluster.

## 2. Consequence

The desired \(D^{2+\varepsilon}\) estimate must use cancellation specific to the
Möbius or prime coefficients. No theorem depending only on:

- Farey spacing;
- the number of frequencies;
- bounded variation of the cutoff;
- a generic Bessel/frame constant;
- positivity of the complete-period Gram

can close the proof.

## 3. Prime-by-prime obstruction

At critical normalization, one prime acts by
\[
I-p^{-1/2}T_{\log p}.
\]
Its norm on a translation-invariant Hilbert energy is
\[
1+p^{-1/2}>1.
\]
Therefore multiplying independent contraction estimates over primes is
impossible; the full signed arithmetic packet must be assembled before the
norm is taken.

## 4. Scope

This does not refute a Möbius-weighted dispersion theorem. It proves only that
the remaining gain is genuinely arithmetic and cannot be supplied by a
coefficient-blind harmonic-analysis wrapper.
