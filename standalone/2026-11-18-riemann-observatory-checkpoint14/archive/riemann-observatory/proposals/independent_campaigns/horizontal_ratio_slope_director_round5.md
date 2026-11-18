# Horizontal-ratio regularization detects zero multiplicity

2026-11-17. Director's reconstruction. **Proposed scoped theorem, awaiting completed independent adjudication and prior-literature search.** The estimate J_epsilon=O(epsilon) is already Proposition2 of Balazard–de Roton, PAPER-C103. No novelty, simplicity proof, or unconditional RH consequence is claimed here. This note asks for the exact leading coefficient of that published quantity, under RH.

## Precise proposed result

Assume RH. For each distinct ordinate gamma of a nontrivial zeta zero let m_gamma be its analytic multiplicity. Both positive and negative ordinates occur separately in the following sum. Put

J_epsilon=(2pi)^(-1) integral_R |zeta(1/2+it)/zeta(1/2+epsilon+it)-1|^2 dt/(1/4+t^2), epsilon>0.

The proposed identity is

lim_(epsilon down to0) J_epsilon/epsilon
= Sum_(distinct gamma) m_gamma[1-binomial(2m_gamma,m_gamma)/4^(m_gamma)]/(1/4+gamma^2).   (S1)

The series is absolutely convergent. Writing C0=xi'(1)/xi(1)=1+EulerGamma/2-log(4pi)/2, it follows that the limit is at least C0, with equality if and only if all nontrivial zeros are simple (RH remains assumed). It is strictly less than 2C0. No finite-epsilon computation certifies the infinite limit or simplicity.

## 1. A contractive quotient and a positive mass identity

Let F(w)=xi(1/2+w), using the standard entire completed xi, and

H_epsilon(w)=F(w)/F(w+epsilon), Re(w)>=0.

The paired Hadamard product under RH and

d/dx |gamma^2+(x+it)^2|^2=4x(gamma^2+x^2+t^2)>=0

show that H is holomorphic and contractive in the right half-plane, continuous at every finite boundary point. In particular its denominator has no zero there. This is the same source-independent Schur/Poisson mechanism already independently checked for the O(epsilon) estimate.

Let dnu(t)=dt/[2pi(1/4+t^2)]. Bounded harmonic Poisson integration gives

mu_epsilon(R):=integral_R (1-Re H_epsilon(it))dnu(t)/epsilon
=[1-H_epsilon(1/2)]/epsilon -> F'(1/2)/F(1/2)=C0.   (S2)

The integrands define nonnegative finite measures. No boundary value at infinity is needed: a disk map, mean value and bounded convergence suffice. The logarithmic derivative of the paired product at the positive real point gives the absolutely convergent identity

C0=(1/2) Sum_(distinct gamma) m_gamma/(1/4+gamma^2).   (S3)

All zeros of F on the boundary are isolated. The classical fact zeta(1/2)!=0 excludes an ordinate zero; the argument would also work at zero if one explicitly included that multiplicity.

## 2. Local limits at one zero, retaining multiplicity

Fix an ordinate gamma, choose a small closed interval I around it containing no other zero ordinate, and factor

F(w)=(w-i gamma)^m a(w), m=m_gamma,

with a nonzero and analytic in a neighborhood of the short closed rectangle to the right of I. Then for tau=t-gamma,

H_epsilon(it)=B_epsilon(t) R_epsilon(t),
B_epsilon(t)=(i tau/(epsilon+i tau))^m,
R_epsilon(t)=a(it)/a(epsilon+it).

Because F(it) is real and a(it) has constant argument on I, Re(a'/a)(it)=0, including its removable value at the zero. Uniform analytic Taylor estimates therefore give

|R_epsilon-1|=O_I(epsilon), Re(R_epsilon-1)=O_I(epsilon^2).

Also |B_epsilon|<=1 and |B_epsilon-1|<=C_m min(1,epsilon/|tau|). It follows by elementary expansion that the difference between either local real defect or local squared defect for H and for B has integral

O_I(epsilon^2 log(1/epsilon))=o(epsilon).

Here the fixed smooth Poisson weight is bounded on I. For the real defect, write B(R-1)=(B-1)(R-1)+(R-1); for the square use the cross term and |R-1|^2. This explicitly avoids an unjustified uniform O(epsilon) error after division by epsilon.

For b_m(u)=(iu/(1+iu))^m one has the exact integrals

integral_R [1-Re b_m(u)]du=m pi,
integral_R [1-|b_m(u)|^2]du=2m pi binomial(2m,m)/4^m,
integral_R |1-b_m(u)|^2du=2m pi[1-binomial(2m,m)/4^m].   (S4)

The first follows by binomial expansion in (1+iu)^(-1): the first power has real integral pi and all higher powers integrate to zero by their primitives. The second follows by integration by parts on 1-(u^2/(1+u^2))^m and the beta integral. The third is twice the first minus the second. All real-defect and squared-defect integrands are nonnegative and O_m((1+u^2)^(-1)), so rescaling tau=epsilon u and dominated convergence are valid.

Consequently

mu_epsilon(I) -> m/[2(1/4+gamma^2)],
integral_I |1-H_epsilon(it)|^2dnu(t)/epsilon
 -> m[1-binomial(2m,m)/4^m]/(1/4+gamma^2).   (S5)

## 3. Exhaustion of all mass supplies the missing global tail argument

For any finite set of zeros choose pairwise disjoint intervals as above. Their limiting mu masses add. By (S3), exhausting the distinct zeros exhausts the entire limiting mass C0 in (S2). Pointwise contractivity gives

|1-H_epsilon(it)|^2 <= 2[1-Re H_epsilon(it)].

Thus the limsup squared-defect contribution outside these finitely many intervals is at most twice C0 minus twice their limiting mu mass. This bound tends to zero as the finite set exhausts all zeros. Finite sums of the local limits (S5) therefore converge to the total squared-defect slope in (S1), with xi in place of zeta. This proves tail control without uniform zero separation, a multiplicity bound, a rate for zero gaps, or a growing-height local approximation.

## 4. Removing the completion does not alter the slope

Let A(s)=s(s-1)pi^(-s/2)Gamma(s/2), s=1/2+it. The actual quotient is

zeta(s)/zeta(s+epsilon)=H_epsilon(it) A(s+epsilon)/A(s).

For small epsilon the strip 1/2<=Re(s)<=5/8 has no zeros or poles of A. Its logarithmic derivative is O(log(|t|+3)). As checked independently in the C103 Poisson audit, g_epsilon=A(s+epsilon)/A(s) satisfies

||g_epsilon-1||_(L2(dnu))=O(epsilon).

Contractivity implies that the L2 distance between the zeta and xi quotients is O(epsilon). The xi squared-defect norm is O(epsilon) by (S2); hence their squared norms differ by O(epsilon^(3/2))+O(epsilon^2)=o(epsilon). The leading coefficient is identical. This step needs the norm estimate, not just pointwise completion convergence.

## 5. Multiplicity consequence and exact next steps

Let c_m=binomial(2m,m)/4^m. Then c_1=1/2 and c_(m+1)/c_m=(2m+1)/(2m+2)<1. Comparing (S1) with (S3) proves

lim J_epsilon/epsilon-C0
= Sum_(distinct gamma) m_gamma(1/2-c_(m_gamma))/(1/4+gamma^2)>=0,

with equality exactly when every m_gamma=1. The strict upper bound 2C0 follows because all c_m are positive and at least one zero exists. This is an analytic multiplicity diagnostic under RH, not an independent route to establishing its minimum.

Independent reviewers should challenge the local real-part Taylor estimate, all-mass exhaustion, branch conventions and completion norm. Search C103's later sections, Burnol's Hilbert-space identities, and horizontal regularization/Hardy boundary energy literature before assessing priority. A useful possible next problem is an effective remainder under explicit spacing/multiplicity assumptions; neither the proof nor ordinary numerical agreement supplies such a rate.
