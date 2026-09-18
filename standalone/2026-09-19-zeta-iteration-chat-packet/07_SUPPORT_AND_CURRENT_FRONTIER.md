# 07 — The published support packet and the latest exact frontier

This chapter integrates the substance of the seven-file packet originally
published as PR #901 at `001fe76229324946a915d4db84282324f7ff9673`.
Its full proof remains unchanged in the sibling
[PROOF.md](../2026-09-18-vasyunin-support-leakage/PROOF.md), with original
sources, checker, validation and result record. All component proofs remain
PROPOSED pending independent mathematical review; classical inputs are credited.

## Classical Vasyunin duals force every fixed coefficient

For r>=2 let U_r^div(k)=1_{k|r}mu(r/k),

$$
d_r(k)=k(k+1)(U_r^{\rm div}(k)-U_r^{\rm div}(k+1)).
$$

The support is [1,r]. Summation by parts gives

$$
\langle b_n,d_r\rangle=-\delta_{nr},\quad
\langle1,d_r\rangle=\mu(r),\quad\langle k,d_r\rangle=0.
$$

This is Vasyunin's classical biorthogonal construction, credited through
Balazard [B18]; the original 1996 paper was not independently audited. For
A=sum c_n b_n,

$$
|c_r+\mu(r)|^2\le\|d_r\|^2\|1-A\|^2.
$$

Norm approximation therefore forces c_r->-mu(r) for every fixed r. This does
not justify interchanging a coefficient limit with an infinite sum.

The concrete vector d_6=(4,0,-12,0,-30,42) has norm squared 92 and target pairing
1. It annihilates every prime-power b-index. Moreover

$$
\langle s_n,d_r\rangle=-r\mu(n/r)1_{r|n},
$$

so d_6 also annihilates every prime-power s-index. Both prime-power-only
approximation classes have a permanent error floor 1/92. For omitted indices
{6,10,14,15}, simultaneous projection improves the floor to
3562158/256250081. These are all-cutoff theorems from finite-support functionals,
not claims inferred from high-zero computations.

## Permitted supports and arbitrary interaction order

For any S subset {2,3,...},

$$
1\in\overline{\operatorname{span}}\{b_n:n\in S\}
\iff [\mathrm{RH}\text{ and every squarefree }n\ge2\text{ belongs to }S].
$$

Necessity uses the duals and the classical full criterion. Sufficiency imports
Bagchi [G06, Remark 4], under RH, for squarefree-only approximation of this
target. This is target-specific, not density of squarefree b_n in all H.
Every fixed bound on the number of distinct prime factors in allowed b-indices
fails; a missing squarefree product with one more prime supplies a witness.
The same bounded-interaction obstruction applies to s-indices, but the full
classification is only asserted for b-supports. Exact Schur elimination is not
contradicted, because it retains the eliminated coordinates' effects.

## The integer dual Gram and its finite geometry

Let F_N(r,s)=<d_r,d_s>. It is positive definite, and

$$
F_N(r,s)=2\sum_{a|\gcd(r,s)}a^2\mu(r/a)\mu(s/a)
-\sum_{a|r,b|s,|a-b|=1}ab\mu(r/a)\mu(s/b).
$$

The second term is an adjacent-divisor correlation, not an optional small error.
For example F(2,3)=-2, whereas the first term alone gives +2.

The dual span V_N^dual is exactly the space supported on [1,N] and orthogonal
to the ramp x_N(k)=k there. Put a_N=H_{N+1}-1 and z_N=N+1-H_{N+1}. Then

$$
P_{V_N^{\rm dual}}1(k)=1-a_N k/z_N\ (k\le N),\quad0\ (k>N),
$$
$$
\operatorname{dist}(1,V_N^{\rm dual})^2
=\frac1{N+1}+\frac{a_N^2}{z_N}\sim\frac{\log^2 N}{N}.
$$

The dual family is unconditionally complete: annihilating all d_r forces all
successive differences of f to be equal, hence f(k)=k f(1), which belongs to H
only for f=0. This does NOT prove completeness of the b_n family. The dual Gram
F_N is not G_N and cannot be interchanged with it.

## Exact head / ramp / tail decomposition

Let t_{N,n}=sum_{k<=N}b_n(k)/(k+1). Pythagoras in the three orthogonal spaces
V_N^dual, span(x_N), and the tail k>N gives

$$
\boxed{\|1-A_c\|^2=(c+\mu_N)^TF_N^{-1}(c+\mu_N)
+\frac{(a_N-t_N^Tc)^2}{z_N}
+\sum_{k>N}\frac{|1-A_c(k)|^2}{k(k+1)}.}
$$

All three terms are retained. Exact matching of the first forces c=-mu_N;
on k<=N its residual equals k m_N, m_N=sum_{n<=N}mu(n)/n. Thus its remaining
head energy is z_N m_N^2 plus the genuine tail, neither shown to vanish.

Applied to the basis itself, the identity gives

$$
G_N=F_N^{-1}+t_Nt_N^T/z_N+T_N^{\rm tail}.
$$

The inverse dual Gram can be evaluated without inverting an integer matrix:

$$
(F_N^{-1})_{mn}=\sum_{k\le N}\frac{b_m(k)b_n(k)}{k(k+1)}
-t_{N,m}t_{N,n}/z_N.
$$

Every term here is rational. The logarithms in the full source v arise after
the infinite arithmetic sums are completed.

## A uniform correction bound in the ACTUAL norm

Let R_N^Gram=t_Nt_N^T/z_N+T_N^tail. It is PSD and has trace below 11 for all N>=2.
Indeed z_N>=N/2, 0<=t_{N,n}<=1+log(N/n), and sum t_{N,n}^2<=5N by the integral
of (1-log x)^2 on (0,1). The ramp trace is at most 10. The tail trace is at most
(N-1)/(N+1)<1 by telescoping. Thus

$$
0\preceq G_N-F_N^{-1},\qquad\operatorname{tr}(G_N-F_N^{-1})<11.
$$

The inverse comparison is G_N^{-1}<=F_N, an UPPER comparison. A bounded-trace
perturbation need not be small relative to a tiny eigenvalue, nor is its
quadratic form on a growing signed Mobius vector controlled by a vanishing
bound. This is a genuine component estimate but not the missing source estimate.

## The logarithmic mollifier's first term is already prime-counting variance

For c_n=-mu(n)(1-log n/log N) and tau_N=T_N^scalar/log N, the prefix residual is
k tau_N-psi(k)/log N. Projecting off the ramp removes tau_N and gives

$$
(c+\mu_N)^TF_N^{-1}(c+\mu_N)=\mathcal V_N/(\log N)^2,
$$
$$
\mathcal V_N=\min_{a\in\mathbb R}\sum_{k\le N}
\frac{(\psi(k)-ak)^2}{k(k+1)}
=\sum_{k\le N}\frac{\psi(k)^2}{k(k+1)}
-\frac{(\sum_{k\le N}\psi(k)/(k+1))^2}{z_N}.
$$

If V_N=O(N^{2 alpha}), 0<=alpha<1/2, the latest note proves zeta is zero-free
on Re s>1/2+alpha. Compare minimizing slopes at dyadic lengths: their differences
are O(2^{j(alpha-1/2)}), so they converge to a fixed slope a_infinity. Replacing
all slopes by that limit preserves the weighted error bound. Dyadic
Cauchy--Schwarz makes integral_1^infinity (psi(x)-a_infinity x)x^{-s-1}dx
holomorphic in the claimed half-plane. Initially in Re s>1 it equals

    -zeta'(s)/(s zeta(s))-a_infinity/(s-1).

Holomorphy at 1 forces a_infinity=1. A zero rho would contribute a nonremovable
pole of residue -m_rho/rho. This proves the implication, not its upper-bound
hypothesis. In particular subpolynomial V_N would suffice for RH; it is not
proved. The obstruction is present in the finite HEAD as well as the tail.

## Execution and scope

The original packet reported 8,940 counted exact comparisons, normal and
optimized runs, ten named controls, and two actual CLI rejections. Those
historical receipts remain intact. Fresh replay for this expansion is in
VALIDATION. No whole-repository scientific validator, Lean build, remote CI,
independent proof acceptance, or all-scale arithmetic upper estimate is implied
by a successful finite reconstruction or by publication.
