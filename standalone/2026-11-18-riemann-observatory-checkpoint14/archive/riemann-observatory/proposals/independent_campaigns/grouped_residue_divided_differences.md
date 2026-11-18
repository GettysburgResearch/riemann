# An exact grouped-residue identity and the remaining arithmetic estimate

Round2,2026-11-17. Status: established interpolation identity specialized here to BCF's residue kernel; no novelty claim. The identity is fully elementary and does not establish a new estimate for zeta.

## Source match

BCF1211.5191v1 Lemma2,p.6, writes the zero term as sums of residues

Res_(z=rho) N^(z-s)/[zeta(z)(z-s)²].

Its Lemma3 controls individual simple-zero residues using an inverse derivative moment hypothesis. De Boor math/0502036v1 §9 Eq.(51),p.63, expresses a divided difference by a contour integral with denominator the node polynomial; Eq.(52),pp.63–64, gives its Hermite–Genocchi derivative integral. These formulas explain exactly how finitely grouped residue cancellations can be retained rather than discarded by an absolute termwise bound. They do not supply the arithmetic size estimate.

## Proposition E-RESIDUE-001

Let U be an open convex subset of C avoiding the pole1 of zeta. Suppose its zeta zeros, counted with multiplicity, are the finite multiset rho_1,...,rho_m, m>=1, with no other zeros in U. Put

q_C(z)=product_(j=1)^m(z-rho_j), g_C(z)=zeta(z)/q_C(z),

with removable singularities filled in. Then g_C is analytic and nonvanishing on U. Let N>1 be real and s outside U. Define

F_C(z)=N^(z-s)/[(z-s)²g_C(z)],

where N^(z-s)=exp((z-s)log N), using the real logarithm. Then

sum_(distinct rho in C)Res_(z=rho) N^(z-s)/[zeta(z)(z-s)²]
   =[rho_1,...,rho_m] F_C.                              (R1)

Repeated nodes on the right are confluent Hermite divided differences. In particular, if the cluster is a single root of multiplicitym, its contribution is F_C^(m-1)(rho)/(m-1)!.

Proof. On a contour in U enclosing all cluster zeros, the integrand is F_C(z)/q_C(z). The residue theorem gives the sum on the left, while the standard contour formula for divided differences gives the right. Such a contour exists because the finite convex hull of the nodes is compact inside the convex open domain U. Equivalently prove the identity at distinct nodes by partial fractions and pass to confluent limits analytically.

Let K be the convex hull of the nodes. Hermite–Genocchi gives the separation-free local bound

|cluster contribution|<=sup_(z in K)|F_C^(m-1)(z)|/(m-1)!. (R2)

The bound contains no reciprocal internal zero distance. It is useful only if the zero-removed factor and its derivatives can themselves be controlled.

## An explicit conditional analytic estimate

Assume r>0 is such that K_r={z:dist(z,K)<=r} is compactly contained in U and s is outside K_r. Put

M_C=sup_(z in K_r)|1/g_C(z)|,

d_C=dist(s,K_r)>0, b_C=max_(z in K_r)Re(z-s).

Cauchy's derivative estimate on each radius-r disk centered in K, followed by(R2), gives

|cluster contribution|<=N^(b_C) M_C/[d_C² r^(m-1)].       (R3)

Every quantity is specified, including the cluster's isolation radius and multiplicity. Internal collisions cause no algebraic singularity in(R1), but M_C, r, and m may still make(R3) very large. If zeta has a pole or an unremoved zero in U, the analytic inverse argument fails; those hypotheses cannot be omitted.

For two simple zeros, R1 is exactly(F_C(rho_1)-F_C(rho_2))/(rho_1-rho_2). Its two partial-fraction terms can each have large1/(rho_1-rho_2) factors while the divided difference is controlled by a derivative. This is the same finite-cluster cancellation mechanism as the stable Gram basis, now applied to the actual residue kernel.

## Precise obstruction to an arithmetic transfer

The local algebra is not the missing theorem. A useful replacement for BCF's individual inverse-derivative moment would need a zero-cluster covering, isolation radii r_C, and uniform arithmetic control of M_C (or the derivative quantity inR2) such that the sum of grouped residue bounds converges and has the growth needed for the weighted critical-line norm calculation. The continuum/discrete Gram theorems do not bound M_C.

For example, if all nodes have real part1/2 and Re(s)=1/2+epsilon, then b_C<=r_C-epsilon. Choosing r_C of order1/log N keeps N^(r_C) bounded, but r_C^(-(m-1)) contributes(log N)^(m-1). The cluster size, separation from other zeros, and zero-removed reciprocal factor remain decisive. This observation does not assert that such isolating discs can be chosen uniformly or that the resulting majorants are summable.

An explicit sufficient condition for absolute convergence of the grouped residue series at fixedN,s is

sum_C N^(b_C) M_C/[d_C² r_C^(m_C-1)]<infinity.

A contour-shift theorem additionally needs uniform tails and integrable majorants as s moves; pointwise convergence is insufficient. No such zeta estimate is proved here. Nor is this sufficient condition claimed weaker than BCF's hypothesis: comparing them requires arithmetic information not supplied by the interpolation identity.

Next practical problem: choose a tractable finite family of zero clusters from rigorously isolated zeros and compute validated enclosures of M_C on zero-free contours. Compare the grouped bound with the sum of individual-residue absolute bounds, preserving the dependence on contour distance andN. Such a finite experiment would test conditioning, not RH.
