# The quadratic pair mean also covers spherical cubic blocks

Status: proposed corollary with proof, for independent review.
This note extends the *stated family* in the neighboring quadratic-pair
mean to angular order zero. It does not improve the numerical zero-free
boundary or supply the missing average over quadratic conductors.

Dependency: ../mixed/QUADRATIC_PAIR_ABSORPTION.md, equations (Q1)--(Q13),
with its exact finite-profile and divisor-resummation dependencies.
The present proof replaces only its use of nonzero angular order to
remove constant terms. All normalization, height and conductor bounds
are the same as in that note.

## 1. Statement

Work over \(E=\mathbb Q(\omega)\). Let \(S\) be a nonunit primary
squarefree element prime to \(6\), put \(H=NS\), and let \(\xi_S\)
be a primitive quadratic character with conductor \(S\). Keep the
source zero extension at every prime of \(S\). Write
\[
 \eta_j=\xi_S(\cdot/S)_3^j,\qquad j\in\{0,2\}.
 \tag{1.1}
\]
For \(r\) primary and squarefree, \((r,S)=1\), and one of the
four actual ramified cubic profiles \(\kappa\), define
\[
 Q_{r,S,j,\kappa}(s)=
 L_E^{(3rS)}(3s-\tfrac12,\xi_S)
 \sum_c\widetilde g(c)\kappa(c)\eta_j(c)
       \overline{(c/r)_3}(Nc)^{-s}.
 \tag{1.2}
\]
The notation for the incomplete Hecke factor is the one in (Q2);
the fixed ramified normalization at \(3\) is retained in the
corresponding scalar channel. The vector includes both \(j\)'s
and all four \(\kappa\)'s.

For \(0<\delta<1/6\), the proposed mean is
\[
 \sum_{\substack{Nr\le R\\(r,S)=1}}^*
       \|\mathbf Q_{r,S}(\tfrac12+\delta+it)\|^2
 \ll_{\delta,\epsilon}(RH)^\epsilon(1+|t|)^C
 \{R+R^{1/2-\delta}H^{1-2\delta}
                      +R^{1-\delta}H^{2/3-2\delta}\}.
 \tag{1.3}
\]
For \(1/3<p<1/2\), the reflected bound is
\[
 \begin{split}
 \sum_{\substack{Nr\le R\\(r,S)=1}}^*
       \|\mathbf Q_{r,S}(p+it)\|^2
 \ll (RH)^\epsilon(1+|t|)^C\{&
 R^{2-2p}H^{2-4p}\\
 &+R^{1-p}H^{2-2p}
 +R^{3/2-p}H^{5/3-2p}\}.
 \end{split}
 \tag{1.4}
\]
These are (Q4)--(Q5) with \(\ell=0\). In particular, for each
fixed such quadratic conductor,
\[
 \sum_{Nr\le R}^*\|\mathbf Q_{r,S}(\tfrac12+\delta+it)\|^2
                   \ll_{S,\delta,\epsilon}R^{1+\epsilon}(1+|t|)^C .
 \tag{1.5}
\]

For arbitrary \(|b_v|\le1\) and fixed smooth compactly supported
\(W_A,W_B\), put
\[
 T_{\xi_S}(A,B)=
 \sum_{u,v}b_v\widetilde g(uv)\xi_S(uv)
                  W_A(Nu/A)W_B(Nv/B).
 \tag{1.6}
\]
Then, with every original common-prime zero retained,
\[
 |T_{\xi_S}(A,B)|\ll (ABH)^\epsilon A^{1/2}
                      \{B+B^{3/4}H^{1/2}+BH^{1/3}\}.
 \tag{1.7}
\]
For fixed \(S\), this is
\[
                  |T_{\xi_S}(A,B)|\ll_{S,\epsilon}
                                      (AB)^\epsilon A^{1/2}B .
 \tag{1.8}
\]
Thus \(A=B=X^{1/2}\) gives \(X^{3/4+\epsilon}\) for this
guarded spherical block, without a Hecke zero-free assumption.
The nontrivial quadratic guard cannot be removed: the untwisted
spherical cubic series has its known nonzero \(5/6\) residue.

## 2. The local reason every component is entire

Choose any prime \(\mathfrak p\mid S\). Relative to its sextic
character \(\chi_{\mathfrak p}\), the two twists in (1.1) have
digits
\[
                     d_0=3,\qquad d_2=3+2\cdot2=1\pmod6 .
 \tag{2.1}
\]
Both are odd. The four ramified profiles concern only \(3\), and
the moving level \(r\) is coprime to \(S\), so neither changes (2.1).

Let \(v_0\) be the local spherical theta vector at \(\mathfrak p\).
For the normalized additive Fourier coefficients
\(\alpha_{\mathfrak p,d}\) of \(\chi_{\mathfrak p}^d\), define
\[
 v_d=\sum_{z\bmod\mathfrak p}
                  \alpha_{\mathfrak p,d}(z)
                  \pi(n(z/\pi_{\mathfrak p}))v_0 .
 \tag{2.2}
\]
Its Whittaker coefficient at an integral torus argument \(x\)
is multiplied exactly by \(\chi_{\mathfrak p}(x)^d\), including
the zero at nonunits. On the completed index \(x=cd^3\), this
is the coefficient \(\eta_j(c)\xi_S(d)\) in (1.2).
Hence (2.2) implements the complete series, rather than twisting
only its squarefree part and forgetting the cube factor.

Choose a cube unit \(b\) with \(\chi_{\mathfrak p}(b)^3=-1\).
The split root relation and the spherical invariance of \(v_0\)
give
\[
                 \pi(a(b))v_d=\chi_{\mathfrak p}(b)^d v_d=-v_d.
 \tag{2.3}
\]
There is no torus cocycle because \(b\) is a cube.

On the ordinary Jacquet module of the unramified cubic theta
representation, \(a(b)\) acts as the identity. In the pinned
normalization the two possible inducing exponents are \(1/3\)
and \(2/3\); their unit restrictions and the central cube-unit
character are trivial. Smooth compact-group semisimplicity rules
out an extension with a nontrivial unipotent action. This is the
same source Jacquet statement used in ALL_FIELD_AUXILIARY_GUARD.md,
Section 4, and its validity at this good local place does not
require \(E\) to contain \(\mu_{12}\).

Thus (2.3) implies that the image of \(v_d\) in the Jacquet
module is zero. The reflected vector has the same property:
\[
 a(b)w=bI\cdot w a(b^{-1}),
 \tag{2.4}
\]
and the central cube unit \(bI\) acts trivially. Consequently
\(\pi(w)v_d\) also has eigenvalue \(-1\) under \(a(b)\), while
its Jacquet image would have eigenvalue \(1\). It too is zero.

Every ramified cusp operator at \(3\) and every moving-prime
operator at \(r\) commutes with this local argument.
The reflected pair exchanges \(j=0\) and \(j=2\), as in (Q6);
both new digits remain odd. Therefore every component of the
closed pair has both constant terms zero in the split Mellin
integral. Each completed function in (1.2) is entire.

This argument also explains why it is not enough to notice that
one original scalar series has no pole: the cancellation holds
for the full reflected vector before its finite-profile extraction.

## 3. The unchanged mean and bilinear proof

The exact primitive finite transform, the four-profile extraction
at \(3\), and the divisor resummation at \(r\) in the pair note
do not use \(\ell\ne0\). Their only such use is the constant-term
claim following (Q8), now supplied by Section 2.

At \(s=1/2-\delta+it\), the gamma quotient with angular order
zero has the same vertical power \((1+|t|)^{4\delta}\).
Its numerator gamma arguments on this line have positive real
parts, and the Gaussian contour shift used for absorption crosses
no theta pole because all completed components are entire.
The local ramified geometric ratios still converge for
\(\Re s>1/6\), containing the reflected range
\(\Re s>1/3\) used in (1.4).

The preliminary finite-conductor supremum is finite by the source
split Mellin growth bounds. The cubic large sieve on the original
side sees only bounded coefficients \(\kappa(c)\eta_j(c)\).
The cube factor has coefficient \(\xi_S(d)\), of modulus at most
one. All three cube sums therefore retain their convergent source
exponents. Equations (Q8)--(Q11), the same positive-divisor
partial summation, and the same choice
\[
 Y=C_0R^{1/2+\theta}H(1+|t|)^2
 \tag{3.1}
\]
give the contraction and prove (1.3), uniformly in nonunit \(S\).
Reflecting proves (1.4).

Finally use exact cubic Gauss multiplicativity in (1.6).
Mellin inversion in \(u\) produces the \(j=0\) series with cubic
row \(r=v\). On \(\Re s=1/2+\delta\), the reciprocal of its
completed quadratic Hecke factor is bounded by absolute Euler
convergence, since \(\Re(3s-1/2)>1\). Cauchy in \(v\), followed
by (1.3), gives (1.7), absorbing arbitrarily small fixed
\(\delta\) into the epsilon allowance. This is precisely the
proof of (Q12), now justified at angular order zero.

## 4. Relation to the physical guard and remaining obstruction

In ALL_FIELD_AUXILIARY_GUARD.md the cubic target twist and the
new-prime row-unit valuation \(-1\) combine to digit \(3\).
Over E the resulting fixed local quadratic factor is of the type
in (1.6). Thus the new mean also controls the spherical cubic
blocks selected by that guard.

It does not supply the joint conductor average needed at the
boundary-determining mixed terminal. If the quadratic conductor
itself is a moving row of norm \(K\), the terms in (1.7) retain
their displayed \(H=K\) costs. At the physical scale
\(U=KL\), the pair note's calculation (Q14)--(Q15) still applies
and gives no strict saving over the inherited \(KL\) bound in
the adverse range \(K\gg L\). Freezing the auxiliary guard prime
does not freeze that separate moving quadratic conductor.
