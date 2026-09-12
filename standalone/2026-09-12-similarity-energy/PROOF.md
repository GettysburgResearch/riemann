# Nonlocal similarity energy and the complete xi zero defect

Date: 2026-09-12. Status: PROPOSED COMPONENT ARGUMENTS; independent mathematical review required.
RH is not proved. The actual-source vanishing energy-excess estimate in Section 8 is OPEN.
This is a continuation of the gamma-defect programme, not an integration or acceptance update.

## 1. Exact source and scope

Use the classical full-line theta density
\[
 \phi(t)=\sum_{n\ge1}(4\pi^2 n^4 e^{9t/2}-6\pi n^2e^{5t/2})
                       e^{-\pi n^2 e^{2t}},\qquad
 w(t)=\phi(t)/\Xi(0).
\]
The density w is positive, even, smooth, and integrates to one. Put
\[
 C(t)=\int_{-\infty}^t w(x)\,dx,\quad Q(t)=1-C(t),\quad
 \mu_2=\int t^2w(t)\,dt.
\]
On H=L2(R,w dt), the centered antiderivative is
\[
 (Kf)(x)=\int_{\mathbb R}[\mathbf1_{t<x}-Q(t)]f(t)\,dt.
\]
The integration measure in this formula is dt, not w(t)dt. Its weighted kernel
is [1_{t<x}-Q(t)]/w(t). The frozen #834 manuscript derives
\[
 I_w:=\|K\|_2^2=\int_{\mathbb R}C(t)Q(t)/w(t)\,dt<\infty,\quad
 \operatorname{Tr}K^2=-\mu_2,
\]
and identifies nonzero eigenvalues, with algebraic multiplicity, as -i/rho
for the zeros rho of Xi. These are inherited proposed operator results,
not independently accepted by this continuation. The eigenvector relation
can also be checked directly by differentiating the centered antiderivative
of exp(i rho t). Multiplicities require the corresponding derivative chains.

The theta tail pays every integral below: log w and w'/w lie in H, and
the integrations by parts have zero endpoint terms. Define
\[
 \Delta_\Xi=\frac14\sum_{\Xi(\rho)=0}
       \operatorname{mult}(\rho)(\operatorname{Im}\rho)^2/|\rho|^4.
\]
Every individual zero occurs in this convention. It agrees with one
first-quadrant-quartet term per multiplicity. No actual nonreal zero is asserted.

## 2. A full-source norm upper certificate for the defect

For every bounded invertible S on H, let A=SKS^{-1}. Then
\[
 \boxed{8\Delta_\Xi\le\|SKS^{-1}\|_2^2-\mu_2.}                 (1)
\]
No condition-number bound uniform over a sequence of S is required.

Proof. Let H_A=(A+A*)/2. Hilbert--Schmidt multiplication and trace cyclicity give
\[
 \|H_A\|_2^2=\tfrac12(\|A\|_2^2+\operatorname{Re}\operatorname{Tr}A^2)
            =\tfrac12(\|A\|_2^2-\mu_2).
\]
For any finite collection of nonzero eigenvalues, take its finite-dimensional
invariant sum of generalized eigenspaces and an orthonormal Schur basis there.
The squared real parts of its diagonal entries are bounded by the complete
Hilbert--Schmidt norm squared of H_A. Exhausting the nonzero spectrum gives
\[
 \sum_\lambda\operatorname{mult}(\lambda)(\operatorname{Re}\lambda)^2
 \le\|H_A\|_2^2.
\]
For lambda=-i/rho, (Re lambda)^2=(Im rho)^2/|rho|^4. This proves (1).
This proof does not replace A^2 by A*A, assume normality, require simple zeros,
or discard a quasinilpotent part of A.

Thus an explicit sequence S_j with full energy at most mu_2+epsilon_j,
epsilon_j tending to zero, would prove RH. The existence of this sequence
for actual theta has NOT been established here.

## 3. Two exact nonlocal eliminations, without computing zeros

The constant direction accounts for a whole mu_2 of nonspectral
Hilbert--Schmidt energy. Since K*1=0 and K1=t, the similarity that multiplies
1 by R and fixes its orthogonal complement has energy
\[
 I_w-\mu_2+\mu_2/R^2.
\]
Letting R grow in (1) gives 8 Delta_Xi <= I_w-2mu_2. Each finite R is an
ordinary bounded invertible similarity; no limiting invertible operator is claimed.

A second direction can also be eliminated explicitly. Put
\[
 J=\int (w')^2/w,\quad V=\operatorname{Var}_w(\log w),\quad
 e_0=1,\quad e_1=(w'/w)/\sqrt J.
\]
The vectors e0,e1 are orthonormal. K*e1=-e0/sqrt(J). The orthogonal complement
Z of their span is K-invariant. Moreover
\[
 Ke_0=-e_1/\sqrt J+r_0,\quad
 Ke_1=r_1,\quad r_0,r_1\in Z,
\]
\[
 \|r_0\|^2=\mu_2-J^{-1},\qquad \|r_1\|^2=V/J.
\]
Here K(w'/w)=log w-E_w log w; integrating t w' gives -1.
Cauchy--Schwarz gives mu_2 J>=1. In the decomposition e0,e1,Z,
\[
 K=\begin{pmatrix}0&0&0\\-J^{-1/2}&0&0\\r_0&r_1&C_Z\end{pmatrix}.
\]
For S_R=diag(R^2,R,I_Z), EXACTLY,
\[
 \boxed{\|S_RKS_R^{-1}\|_2^2
 =I_w-\mu_2-V/J+(1+V)/(JR^2)+(\mu_2-J^{-1})/R^4.}          (2)
\]
Both couplings r0 and r1 have been included. Consequently
\[
 \boxed{8\Delta_\Xi\le I_w-2\mu_2-V/J.}                    (3)
\]
These are analytic bounds, not newly evaluated numerical enclosures of I_w,J,V.
In particular (3) also proves the right side is nonnegative. There is no
assertion it equals zero for theta.

More generally, the finite span of q_j=w^(j)/w, 0<=j<m, is invariant under K*.
Its quotient block is nilpotent. After orthogonalization, successive diagonal
powers of R suppress that finite block and its outgoing coupling. This is useful
preprocessing, not a proof that the surviving infinite root space is skew-adjoint.
The repository's real-zero crowding obstruction specifically prevents treating
that last assertion as automatic.

## 4. Exact finite-matrix optimization: neither tail nor coupling is omitted

Choose an orthogonal finite-rank projection P and write
\[
 K=\begin{pmatrix}A&B\\C&D\end{pmatrix}
\]
relative to PH plus (I-P)H. For a positive-definite matrix G on PH, let
S_G=G^(1/2) direct_sum I. Then
\[
 \boxed{E_P(G)=
 \operatorname{Tr}(GAG^{-1}A^*)+
 \operatorname{Tr}(GBB^*)+
 \operatorname{Tr}(G^{-1}C^*C)+\|D\|_2^2.}                (4)
\]
This is the COMPLETE transformed norm, not a Galerkin proxy. Equivalently,
\[
 E_P(G)=I_w+\operatorname{Tr}(GAG^{-1}A^*)-\|A\|_2^2
       +\operatorname{Tr}((G-I)BB^*)
       +\operatorname{Tr}((G^{-1}-I)C^*C).                (5)
\]
The last two terms need not be positive. Dropping either can invent a
certificate. Formula (1) applies only after their complete source values are paid.

In a real orthonormal polynomial basis p_j, write
R_j(t)=integral_t^infinity p_j(x)w(x)dx for j>=1, R_0=0. Then
K*p_j=R_j/w and
\[
 (BB^*)_{ij}=\int R_i(t)R_j(t)/w(t)\,dt-(AA^*)_{ij}.
\]
The matrix C*C comes from complete polynomial moments of Kp_j. The remaining
D norm is obtained by subtracting the three finite block norms from I_w.
These are finite MANY source integrals; their physical domains are still infinite.
No numerical evaluation of this complete theta matrix data is claimed here.

For increasing polynomial projections P_d, put e_d=inf_{G>0} E_{P_d}(G).
Then e_d is nonincreasing and e_d>=mu_2+8Delta_Xi.
This class exhausts all bounded positive metrics: for bounded coercive G,
G_d=I+P_d(G-I)P_d converges strongly to G, with uniformly bounded inverses.
Functional calculus gives strong convergence of square roots and inverse
square roots. Multiplication of uniformly strongly convergent operators with
a Hilbert--Schmidt K then gives convergence in Hilbert--Schmidt norm.
Polynomials are complete in H: orthogonality to every polynomial forces all
derivatives at zero of the entire Fourier transform of f w to vanish, and
Fourier uniqueness gives f=0. Cauchy--Schwarz and the theta exponential moments
justify that entire transform.
An arbitrary bounded similarity reduces to its positive polar factor without
changing its energy. Thus finite nonlocal matrices do not restrict the infimum
relative to bounded similarities. This is NOT a proof that the infimum is mu_2.

The finite objective has the formal stationary equation, where R=BB*, Q=C*C,
\[
 A G^{-1}A^*+R
   =G^{-1}(A^*GA+Q)G^{-1}.                               (6)
\]
No minimizer is assumed to exist on the unrestricted positive cone: the
explicit constant-direction elimination already illustrates escape to its boundary.

An exact descent step is available. For any unit vector e, let P=e tensor e,
a=||(I-P)A*e||^2 and b=||(I-P)Ae||^2. Scaling e by r changes the full energy by
(r^2-1)a+(r^-2-1)b. For a,b>0 its best decrease is (sqrt(a)-sqrt(b))^2,
at r^2=sqrt(b/a). This retains the whole row and column, not just their projections.
It supplies an algorithmic direction, not a theorem that repeated balancing
reaches the required theta value.

## 5. Why pointwise multiplication is insufficient

Let S be multiplication by a bounded function with bounded inverse.
Only its modulus matters to the energy. Set r(x)=|S(x)|^2 w(x)>0.
Directly from the original kernel and Tr K^2=-mu_2,
\[
 E(S)-\mu_2=\int_{x<t}
 \left[Q(t)\sqrt{r(x)/r(t)}
       -C(x)\sqrt{r(t)/r(x)}\right]^2 dx\,dt.               (7)
\]
The lower bound is not approachable by arbitrary pointwise choices.

Choose three ordered, disjoint, equal-length compact intervals I1<I2<I3,
with I2 strictly to the right of the median. There are m,c>0 such that all
three pair weights C(x)Q(t) are >=m and log(C(y)/Q(y))>=c on I2.
Put
ell_(x,t)=log(sqrt(Q(t)r(x)/(C(x)r(t)))).
For x<y<z,
\[
 ell_(x,y)+ell_(y,z)-ell_(x,z)
       =\tfrac12\log(Q(y)/C(y)).
\]
Each integrand in (7) is at least 4m ell^2 because sinh(v)^2>=v^2.
Cauchy--Schwarz for the three logarithms and integration over the three
intervals, each of length L, give
\[
 \boxed{E(S)-\mu_2\ge m c^2L^2/3>0.}                    (8)
\]
This obstruction is not specific to a particular numerical weight. Nonlocal
mixing, rather than ever more elaborate pointwise reweighting, is required.

## 6. Diagonal scaling in the polynomial basis also has a theta obstruction

For this section standardize the theta coordinate to variance one and denote
its fourth and sixth moments by a and b. Let p0,p1,... be its real orthonormal
polynomials with positive leading coefficients, and k_ij=<p_i,Kp_j>.
The centered antiderivative increases polynomial degree by one, hence k_41=0.
Elementary orthogonalization and integration give the nonzero cycle
\[
 c_*:=k_{14}k_{43}k_{32}k_{21}
      ={(6-a)b-5a^2\over180(a-1)}.                        (9)
\]
For example p2=(x^2-1)/sqrt(a-1),
p3=(x^3-a x)/sqrt(b-a^2), and
p4=(x^4+A x^2+B)/sqrt(h4), where
A=-(b-a)/(a-1), B=-a-A.
The three upward integration coefficients telescope to sqrt(h4)/24.
The remaining coefficient is [b/5+A a/3+B]/sqrt(h4), proving (9).
Existence of p4 follows from the positive density; its norm cancels.

Use the previously reported whole-theta moment enclosures from frozen #842:
2.7911<a<2.7912 and 12.2172<b<12.2173. These are inherited numerical inputs,
not recomputed here. Rational endpoint arithmetic gives c_*>7/10000.

For ANY bounded invertible diagonal similarity in this orthonormal basis,
the four-entry cycle product is unchanged. Write E=1+e for its full energy.
Identity (1)'s Hermitian-part calculation gives e>=0. Since the reverse
entry k_41 is zero, the squared transformed 14 entry is <=e.
Each of the other three squared entries is <=E. Therefore
\[
 e(1+e)^3\ge c_*^2>(7/10000)^2.
\]
In particular exact rational comparison yields
\[
 \boxed{E>1+1/3000000.}                                 (10)
\]
This is an obstruction to the restricted diagonal-scaling method, NOT a
positive lower bound on Delta_Xi and NOT evidence against RH. General positive
matrices with off-diagonal mixing are not covered by (10).

## 7. Relationship to the gamma work and what is not repeated

#868 proves a particular local nonreal-pair annihilation under a prescribed
centered gamma scale update. #869 supplies a Bessel-anchor global signed
Jensen balance, and #875 supplies a gamma-shape current including every
fixed-step exception and collision. Their global signed-production premise
remains open. This packet does not claim those balances anew.

The proposed change is to upper-bound the TOTAL same limiting defect by (1),
using a sequence of complete nonlocal metric energies. A fixed bounded exact
symmetrizer is neither constructed nor needed. Condition numbers may grow.
Earlier operator-crowding obstructions therefore do not by themselves refute
this sufficient target. Conversely they cannot prove it.

The unfinished preceding scout suggested improvement in some nonlocal finite
models. Its complete numerical source/tail record was not recovered and
authenticated for this delivery, so no scout values or numerical improvement
are adopted as accepting evidence here.

## 8. The precise remaining end-to-end theorem

A sufficient theorem is to give dimensions d_j, explicit positive matrices G_j,
and proved COMPLETE source enclosures satisfying
\[
 E_{P_{d_j}}(G_j)\le\mu_2+\epsilon_j,\qquad\epsilon_j\downarrow0. \tag{OPEN}
\]
Then (1) yields Delta_Xi=0, and every xi zero is central, with multiplicities
retained. This conclusion does not require simplicity or convergence of G_j.

OPEN has not been proved. Exact decrease, finite optimization, increasingly
ill-conditioned similarities, or real eigenvalues of a truncated block do
not imply it. In particular (4) must include BB*, C*C and D throughout.
The new concrete results are the defect inequality, the explicit two-score
energy reduction, exact finite objective/exhaustion, and the two strict
obstructions to overly restricted metric classes. They are proposed component
arguments, not a completed RH proof awaiting routine checks.
