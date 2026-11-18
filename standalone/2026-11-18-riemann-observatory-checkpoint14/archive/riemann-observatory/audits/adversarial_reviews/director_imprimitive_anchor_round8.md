# Director adjudication: finite Euler factors and the zero-at-one anchor

Date: 2026-11-17. Two independent transfer proofs and two independent anchor proofs were read in full, and I independently checked the integer lengths, critical-line multiplier bounds, Hardy normalization and principal counterexample. Evidence: prefix_formula62_imprimitive_transfer.md, witness62_imprimitive_transfer.md and witness62_anchor_nonprincipal.md in this directory. Accepted as scoped ordinary arguments; no novelty or whole-paper audit claim.

## 1. Fixed finite factors preserve the unrestricted constant

Fix χ modulo q, induced by primitive χ*. Let F=L(.,χ*), E=∏_(p|q,p∤q*) (1−χ*(p)p^(−s)), M the product of these primes, and Δ_N the unrestricted ordinary polynomial distance in the full Cauchy norm. Then L(.,χ)=EF. Empty products are allowed, including changes of modulus introducing no new Euler factor.

For every integer J≥0 with N≥M^J, put K=floor(N/M^J) and δ_J=∏_(p|M)(1+p^(−(J+1)/2))−1. Exact polynomial multiplication and uniform critical-line bounds give

    Δ_(MN,F) ≤ Δ_(N,EF) ≤ (1+δ_J)Δ_(K,F)+δ_J.

Indeed EA has length ≤MN. Conversely R_J=∏_(p|M)Σ_(j=0)^J (χ*(p)p^(−s))^j has length ≤M^J and |1−ER_J|≤δ_J. Multiplying a length-K primitive approximant by R_J preserves the length-N budget, and ||FA||_*≤1+||1−FA||_* bounds the multiplier error. Infima need not be attained. Taking J=ceil(2loglogN/log2) makes δ_J=O_q(1/logN), M^J polylogarithmic in N, and log K/log N→1. Multiplication by √logN before passing to the norm limit proves that any finite primitive logarithmic squared constant transfers unchanged. The independent proof using n≤exp√logN inverse-E truncation supplies another valid cutoff.

Under the separately reconstructed primitive GRH theorem, the transferred constant is Σ mρ²/|ρ|² over the inducing primitive critical-line zeros. Added Euler-factor zeros all have real part zero and do not change the critical-line multiplicities. They must not be added to the constant. For a principal imprimitive character they include zero itself, illustrating the failure of an indiscriminate sum over all zeros. The pole at 1 survives since E(1)≠0. Modulus and characters are fixed; no conductor-uniformity follows. Both directions allow arbitrary complex ordinary frequencies, including ramified integers. A support restriction (n,q)=1 or a prescribed reciprocal coefficient array is not preserved by division by E.

## 2. The nonprincipal anchor has an exact obstruction

For every nonprincipal Dirichlet χ, primitive or imprimitive, bounded periodic partial sums Sχ(x)=Σ_(n≤x)χ(n) give

    L(s,χ)/s=∫_0^∞ Sχ(e^u)e^(−su) du,   Re s>0.

On Re s>1/2 this is H², because e^(−u/2)Sχ(e^u) is square integrable. Multiplication by any finite Dirichlet polynomial preserves H². The evaluation kernel at 1 is 1/s and has squared norm 1 with boundary dt/(2π). Thus

    <Lχ A/s,1/s>=L(1,χ)A(1).

If A(1)=0, Pythagoras gives the exact identity

    ||1−Lχ A||_*²=1+||Lχ A||_*².

Consequently the anchored optimum is 1 for every N≥1, unconditionally and uniquely at A=0. In the input convention B→B−B(1), precisely constant B minimize it. No GRH or simplicity assumption changes this conclusion. More generally the identity holds whenever FA/s is genuinely H² and vanishes at 1. Holomorphic continuation without Hardy membership is insufficient.

For a principal character, F has a simple pole with residue r=∏_(p|q)(1−1/p)>0. The summatory coefficients are rx+O_q(1), so F/s=r/(s−1)+H0 with H0∈H². If A(1)=0, then (FA/s)(1)=rA'(1), not zero in general. At N≥2 take A0(s)=1−2^(1−s). A0/(s−1) is the Laplace transform of a compactly supported function on [0,log2], so FA0/s∈H² and its target pairing is rlog2≠0. Optimization over scalar multiples yields squared distance 1−(rlog2)²/||FA0||_*²<1. At N=1 the anchor admits only zero and the minimum is 1.

The Euler-factor sandwich preserves A(1)=0 by multiplication. Thus the existing anchored zeta theorem transfers to principal imprimitive characters. An unanchored premise alone would not establish an anchored conclusion. For nonprincipal characters the exact value is 1, so a naive transfer of the zeta anchoring step would be false.

These are useful normalization and admissible-space controls. The elementary Hardy argument may have precedents; the bounded search in the proponent note is not a priority determination. The next precise question is the optimal constant after a different admissible linear condition, for example one targeting the correct Hardy evaluation rather than imposing the zeta pole cancellation on an entire L-function.
