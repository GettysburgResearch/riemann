# L-0601 — Prime-power derivative jump of the cutoff-free finite Weil path

Claim ID: L-0601  
Title: Prime-power derivative jump of the cutoff-free finite Weil path  
Status: PROPOSED  
Authoring agent: `gpt56-01-a`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `D-0001`; exact prime source in the finite Guinand--Weil normalization  
Scope: one-sided differentiation at a prime-power cutoff  
Related counterexample candidates: none

## Statement

Let `q=p^a` be a prime power, let `u=log(c)`, and let `Q_N(c)` be the
cutoff-free full-index matrix of `D-0001` on `{-N,...,N}`. The path is
continuous at `u_0=log(q)`, and its one-sided derivative has the exact jump

\[
 \frac{dQ_N}{du}(u_0+)-\frac{dQ_N}{du}(u_0-)
 =-\frac{2}{a\sqrt q}\,\mathbf 1\mathbf 1^{\mathsf T}.
\]

Under the real-even isometry

\[
 u_0=v_0,\qquad u_k=u_{-k}=v_k/\sqrt2,
\]

the jump is

\[
 -\frac{2}{a\sqrt q}\,r_Nr_N^{\mathsf T},
 \qquad r_N=(1,\sqrt2,\ldots,\sqrt2)^{\mathsf T}.
\]

Consequently, for a fixed real-even vector `v`, the jump in its Rayleigh
derivative is

\[
 -\frac{2}{a\sqrt q}
 \left(v_0+\sqrt2\sum_{k=1}^{N}v_k\right)^2.
\]

## Definitions

Put

\[
 \epsilon_q(u)=1-\frac{\log q}{u},\qquad
 w_q=\frac{\Lambda(q)}{\sqrt q}=\frac{\log p}{\sqrt q}.
\]

The single newly admitted prime-power source is

\[
 \psi_q(x;u)=-\frac{w_q}{\pi}\sin(2\pi x\epsilon_q(u)).
\]

Its divided-difference block is denoted `P_q(u)`.

## Proof

At `u=u_0=log(q)`, one has `epsilon_q(u_0)=0`, so every value and derivative
of the sine source used in the divided-difference entries is zero. Therefore
`P_q(u_0)=0`, proving continuity when the term is admitted.

For `m != n`,

\[
 (P_q(u))_{mn}
 =-\frac{w_q}{\pi}
 \frac{\sin(2\pi m\epsilon_q(u))-\sin(2\pi n\epsilon_q(u))}{m-n}.
\]

For `m=n`,

\[
 (P_q(u))_{nn}
 =-2w_q\epsilon_q(u)\cos(2\pi n\epsilon_q(u)).
\]

Since

\[
 \epsilon_q'(u_0)=\frac{\log q}{u_0^2}=\frac1{\log q},
\]

differentiation at `u_0+` gives `-2w_q/log(q)` in every entry, diagonal and
off-diagonal. The term is absent on the left. Finally,

\[
 \frac{2w_q}{\log q}
 =\frac{2\log p}{\sqrt q\,a\log p}
 =\frac{2}{a\sqrt q}.
\]

Thus the full jump is the asserted negative rank-one matrix.

If `V_N` is the real-even isometry, then
`V_N^{\mathsf T}\mathbf1=r_N`, so congruence by `V_N` proves the even-sector
formula. Contracting against `v` proves the Rayleigh formula.

## Analytic domain audit

Only real logarithms with `c>1` are used. The result differentiates a finite
prime-power source; no zeta continuation, contour, branch, or infinite sum is
used in the proof. The cutoff-free archimedean and pole blocks are smooth at
the threshold and cancel from the right-minus-left jump.

## Dependency audit

The only substantive dependency is that `D-0001` has the displayed prime
source and that `u=log(c)` is the path parameter. A sign change in that source
would reverse this lemma and must be checked in the independent `Q-0004`
normalization audit.

## Gap audit

- This is a derivative jump, not a proof that an eigenvalue crosses zero.
- The smooth pole, archimedean, and previously admitted prime terms continue to
  move on both sides of the threshold.
- An eigenvector can nearly annihilate `r_N`, making the first-order edge signal
  negligible.
- Ordinary finite differences are tests of this formula, not its proof.

## Adversarial tests

`X-0601` checks primes and higher prime powers, full-to-even projection,
left/threshold/right continuity, convergence of finite-difference quotients,
and exact annihilation on the hyperplane `r_N^T v=0`.

## Remaining uncertainty

The calculus above is self-contained once the prime-source normalization is
accepted, but the project-level status remains `PROPOSED` pending an independent
source/sign reconstruction.

## Suggested next attack

At every prime power, rank directions by both their baseline Rayleigh value and
`|r_N^T v|`. Resolve the full smooth path immediately to the right, rather than
assuming the rank-one jump acts against a frozen background.
