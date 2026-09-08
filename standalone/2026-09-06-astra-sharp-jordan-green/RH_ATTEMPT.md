# End-to-end attempt: the arithmetic gate closes, the critical transfer does not

Status: **RESEARCH HANDOFF WITH PROVED COMPONENTS AND AN EXPLICIT OPEN LINK**.
No unconditional proof of RH is claimed. This file records the attempted
transfer after JGC26.T1 rather than leaving a reviewer to supply it.

## 1. What changed, compared with the audited programme

The earlier source chain contained TWO different obligations:

    all-scale arithmetic Green-density positivity
        -> positive completed safe-side Laplace source
        -> completed critical source identification and norm exhaustion
        -> absence of shifted Xi poles
        -> RH.

The first arrow is now supplied for every positive real scale, with a sharp
coefficient threshold and explicit margin. The completed safe-side source is
also constructed for every scale, by regrouping its rational and gamma
factors before taking inverse transforms. This avoids a false positivity
claim for the isolated rational factor at s>1.

The new proof is not conditional on the old small-scale threshold, any of its
finite density scans, the prime-deletion MGF bound, or a finite zero census.
Its arithmetic uses the factorial identity and the literal coefficients
F_s(n). The separate mean estimate in REAL_AXIS.md resolves another named
open inequality in PR #440, but is not needed for the all-time proof.

The second arrow above is NOT supplied. Safe Hankel positivity is not the
same object as the critical de Branges--Rovnyak kernel.

## 2. Exact bridge to the completed Xi ratio

Use the usual entire completion

\[
 \xi(w)=\tfrac12 w(w-1)\pi^{-w/2}\Gamma(w/2)\zeta(w).
\]

For Re q>0 the exact identity is

\[
 H_s(q):=\frac{\xi(1+q)}{q\xi(1+s+q)}=A_s(q)Z_s(q),
\tag{B1}
\]

with A_s and Z_s as defined in PROOF.md. In particular the function there is
NOT H_s without correction:

\[
 \mathcal S_a(q)=\frac{q^2+\kappa_*a q+4a^2}
 {q^2(q+a)^2(q+2a)^2(q+4a)^2}
 \left[H_{2a}(q)-A_{2a}(q)\frac{c_{2a}}q\right].
\tag{B2}
\]

The deterministic centered term is mandatory. All nonreal zeta poles of the
meromorphic expressions must be treated with their net orders after common
numerator/denominator cancellation.

The target quotient on the right half-plane is

\[
 \Theta_a(z)=\frac{\xi(1/2-a+z)}{\xi(1/2+a+z)}.
\]

It corresponds to q=z-1/2-a in (B1). Thus its critical boundary z=ix is
q=-1/2-a+ix, not q=ix. Meromorphic continuation of a function does not mean
that its original positive Laplace integral converges at the new point.

## 3. The direct exponential-feature map is not defined

**Proposition JGC26.N1.** Neither the new arithmetic measure omega_a nor the
completed positive measure mu_a has a positive exponential moment. More
precisely, for every a>0 and lambda>=0,

\[
 \int_0^\infty e^{\lambda t}d\omega_a(t)=\infty,
 \qquad
 \int_0^\infty e^{\lambda t}d\mu_a(t)=\infty.
\tag{B3}
\]

For omega_a this follows at once from its continuous density
B_(2a,kappa*)>8a/45. For mu_a write mu_a=nu_a*omega_a, where nu_a is the
nonzero finite positive convolution of the three Erlang and two regrouped
archimedean channels. The absolutely continuous component of mu_a has, for
any fixed T>0 and t>=T, the lower bound

\[
 \frac{8a}{45}\nu_a([0,T])>0.
\]

Choose T with positive mass, which exists because every factor is nonzero
and positive. This proves (B3).

Consequently the evaluation vector t -> exp(-zt) lies outside L2(mu_a) when
Re z<=0. The literal proposal to continue the safe Gram by exponentially
reweighting its positive measure is invalid. In particular it cannot reach
the target in (B1) by simply replacing q with -1/2-a+ix. Multiplication by
exp((1/2+a)t) is also an unbounded operator in the original L2 source metric,
as seen on unit vectors supported on [n,n+1].

This proposition diagnoses THAT candidate map, not every possible signed
renormalization or boundary construction. Subtracting asymptotic states,
contour deformation, or a source-ordered colligation might be useful, but
the resulting signed terms and crossed residues must be bounded afresh.
The positive lower bound proved here does not provide their needed upper
bound or norm identity.

## 4. A finite control against erasing a positive residual port

The following synthetic kernel control is algebraic, not an L-function.
For Re z>0 put b(z)=(z-1)/(z+1), A(z)=1/2, F(z)=A(z)/b(z),
and K_f(z,w)=(1-f(z)conj(f(w)))/(z+conj(w)). On points avoiding 1,

\[
 S(z,w)=\frac{K_A(z,w)}{b(z)\overline{b(w)}},
 \qquad P(z,w)=\frac{K_b(z,w)}{b(z)\overline{b(w)}}.
\]

Both are positive kernels, S is positive definite at every finite set of
distinct nodes, and the exact product identity gives

\[
 S=K_F+P.
\]

At z=w=2 the exact diagonal values are

\[
 S=27/16,\quad P=2,\quad K_F=-5/16.
\tag{B4}
\]

Thus positive source kernels with full finite-rank positivity do not force
exhaustion or positivity of the critical difference. The example is not
boundary-unimodular and has no Euler product; it is used only to reject the
generic positivity-to-exhaustion inference, not as a model of actual Xi.

## 5. The remaining sufficient theorem and its full conclusion

A precise sufficient endpoint is: for each a_j=2^(-j-2), j>=0, prove

\[
 K_{\Theta_{a_j}}(z,w)=
 \frac{1-\Theta_{a_j}(z)\overline{\Theta_{a_j}(w)}}{z+\overline w}
\]

positive semidefinite on every finite packet in its meromorphic domain in
Re z>0, by a source-ordered construction retaining all deterministic,
compensation and net-pole terms. Diagonal positivity gives |Theta|<=1
away from poles, so the meromorphic poles are removable and Theta is Schur.

**Conditional consequence JGC26.C3.** This endpoint implies RH.
Indeed, suppose rho=1/2+d+i gamma is a nontrivial zero with d>0.
Choose j sufficiently large that a_j<d. At z_j=d-a_j+i gamma the denominator
of Theta_(a_j) vanishes. Since xi is nonzero analytic as a function (not
identically zero), rho is an isolated zero; for every sufficiently small
nonzero a_j, xi(rho-2a_j) is nonzero. Therefore the pole is NOT canceled.
This contradicts |Theta|<=1 near z_j. Hence no zero lies to the right of
1/2; the functional equation reflects any left-side zero to the right.
All nontrivial zeros are consequently critical.

This proof retains zero multiplicities and does not assume zero simplicity,
a fixed spectral gap, or a countable-set avoidance argument. The only
zero facts imported here are the usual entire completion, its reflection,
and localization of nontrivial zeros to the critical strip.

**The sufficient endpoint is not proved in this packet.** In the language of
L-91038, both an identification of the new arithmetic feature space with the
pole-removed model source and a norm-exhaustion statement remain necessary.
We do not assume either, label it a consequence of T1, or import a theorem
conditional on Xi innerness as its proof.

## 6. Constructive next target

Use the explicit new measure and its lower metric bound to try to construct
an actual boundary map, with the signed correction in (B2) retained. The
first test is the full polarized identity, not its diagonal or its positive
source component alone. A successful map must also evade (B3) by something
more than direct exponential evaluation. Its norm must be proved in the
inherited metric before identifying it with the Xi Pick kernel.

This is a narrower research frontier than rechecking compact Green-density
knots: their sign is now proved with room to spare. It is not evidence that
RH has become a finite calculation or a routine final lemma.
