# Independent review of the bounded-continuation criterion

Reviewer: positivity lane. Date: 2026-10-30.  
Reviewed source: `swarm/arithmetic/normality_gate.md`.  
Reviewed SHA-256: `b71cd0894e5aa8d635b41d34e6da609c197f8b722c0d3421a434f15d7b737262`.

**Verdict: no mathematical blocker.** The conditional proposition follows from its three stated hypotheses and the already proved right-half-plane convergence. None of those missing target-strip hypotheses is established by this note. The conclusion correctly includes every fixed primitive conductor, not just zeta.

## Pole clearing and normal-family extraction

The arithmetic detector has only simple poles in the stated disk: logarithmic derivatives have simple poles with multiplicity as residue, coincident locations add positive residues, the compensator cancels the pole at 1, and the imprimitive Euler-factor singularities lie on \(\Re s=0\), outside the domain. Multiplication by the scale \(R\) in \(f_Q(z)=R R_Q^*(c+Rz)\) preserves residues.

Subtracting all principal parts inside the disk therefore gives a holomorphic \(h_Q\). Contributions from outside the disk remain in this regular part, as the note explicitly requires.

A finite Blaschke product with one factor for each distinct pole cancels every pole. The estimate
\[
\left|\frac{B_Q(z)}{z-a}\right|
\le \frac1{|1-\bar a z|}\le\frac1{1-r},
\qquad |z|\le r<1,
\]
is correct, including its removable value at \(z=a\). Thus the positive total-residue bound and local bounds on \(h_Q\) give local bounds on \(A_Q=B_Qf_Q\).

The unweighted budget supplies \(B_Q(z_0)\ge e^{-B}>0\) after phase normalization. Montel extraction gives a nonzero holomorphic limit \(B\); a further subsequence gives a holomorphic limit \(A\). On the nonempty right-hand open set, \(A_Q\to0\), so the identity theorem yields \(A\equiv0\).

## Contour contradiction

For a fixed inherited zero, a small circle can be chosen inside the disk whose boundary avoids the discrete zero set of \(B\). On that boundary, uniform convergence and a positive minimum of \(|B|\) imply that \(B_Q\) is nonzero for all sufficiently large \(Q\), and \(f_Q=A_Q/B_Q\to0\) uniformly. Hence its normalized contour integral tends to zero.

Every residue inside is positive. A zeta zero of multiplicity \(m\) contributes at least \(m\) for every \(Q\). A zero of a fixed primitive character of conductor \(d\ge2\) contributes at least \(m\lfloor Q/d\rfloor/(Q-1)\to m/d>0\). Either contradicts that convergence. No assertion of spherical normality at colliding poles is needed.

The stated scope warning is essential and correct: continuation to zero would exclude all fixed-conductor Dirichlet zeros in the disk. It is stronger than merely obtaining a zeta-only contour bound below one.

## Weighted mass, obstruction examples, and quantitative limitation

A bound on the sum of residues does not bound the unweighted Blaschke budget: residues as small as \(1/(Q-1)\) can occur at many distinct locations. One Blaschke zero is required at each location regardless of that residue. The note keeps these two controls separate.

Both obstruction examples check:

- \(e^{-N(s-a)}/(s-a)\) has a persistent residue-one pole and right-half-plane convergence to zero, but its entire regular part equals \(-N\) at \(a\).
- \(z^{N-1}/(z^N-r^N)\) has \(N\) residues \(1/N\), zero regular part, and total mass one. Its limits on the two sides of \(|z|=r\) are incompatible with meromorphic normality across that circle; its Blaschke denominator at zero has modulus \(r^N\).

The two-constants discussion correctly includes the denominator cost. Its stated convergence condition is a sufficient schematic quantitative requirement on fixed nested domains; a pole-count estimate alone supplies no usable uniform lower bound on that denominator. The paragraph does not claim an arithmetic estimate establishing the requirement.

The source-attribution discussion appropriately labels the shifted-prime mechanism classical and limits the exact bibliographic claims to material actually inspected. This review establishes the analytic validity of the conditional continuation argument, not global novelty or any unproved target-strip estimate.

