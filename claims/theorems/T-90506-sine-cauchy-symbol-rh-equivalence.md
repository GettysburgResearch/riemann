# T-90506 — Sine-symbol and Cauchy-sandwich equivalences for RH

Claim ID: `T-90506`  
Status: **FULL EXACT EQUIVALENCE PROPOSAL — SCALAR SYMBOL SIGN OPEN; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: `L-90510`, `L-90511`; Xi-cardinal capture on PR #365

Let

\[
 \mathfrak m(\tau)
 =2\pi\mu(\tau)
  -2\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
        \cos(\tau\log n)
\]

as an even tempered distribution, and let

\[
 \mathcal S h(\tau)=\sqrt{2/\pi}
 \int_0^\infty h(x)\sin(\tau x)\,dx.
\]

Then

\[
 \boxed{
 \mathrm{RH}
 \iff
 \langle\mathfrak m,|\mathcal Sh|^2\rangle\ge0
 \quad\forall h\in C_c^\infty(0,\infty).
 }
 \tag{T-90506.1}
\]

For every `1/2<a<c`, this is also equivalent to positivity of the trace-class Cauchy sandwich

\[
 K_aM_{r_c}M_{\mathfrak m}M_{r_c}K_a,
\]

where

\[
 K_a(\tau,\sigma)
 ={a\over\pi}
 \left[{1\over a^2+(\tau-\sigma)^2}
       -{1\over a^2+(\tau+\sigma)^2}\right],
 \qquad
 r_c(\tau)=(c^2+\tau^2)^{-1}.
\]

Equivalently, its Fredholm determinant has no positive real zero, its heat trace is nonpositive for every positive time, and all shifted spectral moment Hankel matrices are positive semidefinite.

This is the scalar endpoint of the Fredholm programme: prove a Wiener–Hopf factorisation or reflection-positive square representation for the one distribution `m`. No unconditional such factorisation is claimed.
