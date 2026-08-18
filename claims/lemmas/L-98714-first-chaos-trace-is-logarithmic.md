# L-98714 — The genuine first-chaos heat trace is logarithmic, not linear in T

Claim ID: `L-98714`  
Status: **PROVED UNCONDITIONAL TRACE ASYMPTOTIC**  
Created: 2026-08-18  
Depends on: `L-98700`  
RH status: **not assumed**

In the finite generalized-prime Fock model, the squared norm of the heated
one-particle vector is

\[
I_{\theta}(T)
=\theta\sum_{q\in\mathcal Q}
 \frac{\lambda_\diamond(q)}q
 e^{-(\log q)^2/(2T)}.
\tag{L-98714.1}
\]

For odd prime powers, `lambda_diamond(p^r)=1/r`. The terms with `r>=2` are
absolutely summable, as is the complete dyadic contribution. The first powers
give

\[
\sum_{p\ {\rm odd}}
 \frac1p e^{-(\log p)^2/(2T)}
=\frac12\log T+O(1)
\tag{L-98714.2}
\]

by Mertens' prime-harmonic theorem and partial summation. Hence

\[
\boxed{
I_\theta(T)=\frac\theta2\log T+O(\theta).
}
\tag{L-98714.3}
\]

Thus the phrase “the first-chaos trace is at most `96 theta T`” is only a very
loose inequality; it does not derive the exponential factor in `L-98703.1`.
The missing exponential control lies in the coherent collapse and the
cross-history blocks. Those are exactly the blocks whose phase-blind norm has
type `1/2` by `L-98713`.
