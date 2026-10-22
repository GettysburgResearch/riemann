# R-32402 — Bottom-coboundary telescoping returns the omitted Haar–Möbius tail

Claim ID: `R-32402`  
Title: Propagating finite cutoff errors through the critical-Haar bottom functional telescopes exactly to the omitted reciprocal-zeta source; it is not an independent boundary estimate  
Status: **EXACT SCOPE CORRECTION / NO-GO**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #333 `L-32403/L-32404`  
Scope: rules out a false scalar shortcut for HBC; does not refute HBC or RH

## 1. The tempting shortcut

PR #333 defines the central operator `C` and the critical-Haar bottom functional

\[
\mathcal B(f)=-(1+\sqrt2)f(2)+\sqrt2 f(3)+\sqrt2 f(4),
\]

with the exact coboundary identity

\[
\boxed{
\mathcal B(f)=\langle\nu_2,(I-\mathcal C)f\rangle_{q\ge2}
}
\tag{R-32402.1}
\]

for finite states, where

\[
\nu_2=\mu-\sqrt2\,\delta_2*\mu.
\]

Hence for every finitely supported `g`, since repeated central splitting strictly reduces support,

\[
\boxed{
\sum_{a\ge0}\mathcal B(\mathcal C^ag)
=\langle\nu_2,g\rangle_{q\ge2}.
}
\tag{R-32402.2}
\]

This might appear to make propagation of every boundary injection harmless: sum its entire future orbit first, then use only one source pairing.

That inference is false as a completion mechanism.

## 2. Finite tail truncation

Let

\[
w_X^\infty(q)=q^{-1/2}\log(X/q)
\]

be the uncut analytic profile, and let

\[
w_X^{[M]}(q)=w_X^\infty(q)\mathbf1_{q\le M}.
\]

For integers `M>X`, define the omitted finite tail

\[
\boxed{
 g_{X,M}(q)
 =-w_X^\infty(q)\mathbf1_{X<q\le M}.
}
\tag{R-32402.3}
\]

This is finitely supported, so (R-32402.2) applies without any convergence issue:

\[
\boxed{
\sum_{a\ge0}\mathcal B(\mathcal C^a g_{X,M})
=-\sum_{X<q\le M}
\frac{\nu_2(q)}{\sqrt q}\log\frac Xq.
}
\tag{R-32402.4}
\]

Equivalently,

\[
\boxed{
\sum_{a\ge0}\mathcal B(\mathcal C^a g_{X,M})
=\sum_{X<q\le M}
\frac{\nu_2(q)}{\sqrt q}\log\frac qX.
}
\tag{R-32402.5}
\]

Thus complete propagation has not eliminated the arithmetic source. It has reconstructed it exactly.

## 3. The limiting obstruction is the RH-bearing tail

PR #333 proves

\[
\sum_{q\le Y}{\nu_2(q)\over\sqrt q}\log{Y\over q}
=\mathcal H_2(Y),
\]

with Mellin transform

\[
{1-2^{-z}\over z^2\zeta(z+1/2)}.
\]

Therefore controlling the limit of (R-32402.5), uniformly with subpower size as `M` is removed, is not a source-free boundary estimate. It is the same reciprocal-zeta tail encoded by the critical Haar scalar.

In particular, one may not argue

```text
fresh boundary has small local norm
+ bottom functional is a coboundary
=> complete propagated bottom correction is polylogarithmic.
```

The first statement controls a chosen representation of each injection. The second statement sums its propagation exactly. Their composition returns the coherent signed Haar–Möbius tail before any absolute value, and that tail is RH-bearing.

## 4. Correct use of the coboundary identity

Equation (R-32402.2) is still valuable. It proves that **propagation itself introduces no additional scalar amplification**. Any successful HBC proof may therefore work directly with the source pairing of the complete recombined cutoff state rather than estimating every intermediate orbit.

But the resulting pairing must be bounded by a genuinely arithmetic mechanism. Candidate mechanisms include:

- the source-coupled reflected Selberg matrix;
- Cycle-Debt/Pascal recombination preserving the principal mode;
- a new one-sided observable which signs the Haar source.

The coboundary identity alone is not such a mechanism.

## 5. Proof boundary

Proved exactly:

- finite boundary propagation telescopes to the source pairing (R-32402.4);
- the tempting scalar propagation shortcut is not independent of the RH-bearing source.

Not disproved:

- HBC;
- a source-specific bound on the complete Haar cutoff state;
- RH.