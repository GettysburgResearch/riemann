# Primitive Möbius continuation with a fixed sixth-power-free label

23 October 2026. Proposed theorem, independent review pending. This extends
the complete primitive scalar calculation in PR1015 to a fixed good
sixth-power-free numerator label. Its final corollary controls an actual
Gauss-vector projection on the inverse coefficient, including its pole
and continuous part. It does not control the orthogonal complement.

## 1. Statement and imported proof components

Keep the actual coefficients b_n, fixed ray data, smooth annular profiles,
and fixed-during-the-row-sum puncture Q of `LABEL_UNIFORM_MOBIUS_RESIDUES.md`
(SHA256 `12c765c1fdcccec8ebb087b7608b80bb7b2d30114bf664ac1e43a2966b9d8f89d`).
Let R be good and sixth-power-free, with H=NR, and set

\[
 \mathcal P_R(U)=\sum_n b_n\mathcal E_U[H_\nu(nR,\cdot)],
 \qquad
 \mathcal E_U[F]={1\over2\pi i}\int_{(1+\eta)}
 F(u)\widehat w(u-1/2)U^{u-1}\,du.                    \tag{P1}
\]

Here H is the primitive series with literal modulus exclusion (c,nR)=1,
and 0<eta<1/12. The proposed conclusion is

\[
 \boxed{\quad |
 \mathcal P_R(U)|^2\ll(UDHNQ)^\epsilon
       \{U+D^{11/12}H^{1/12}+(DH)^{1/2}\}.\quad}       \tag{P2}
\]

For H<=D the middle term dominates the last. The proof imports the
exact local inversion in paper10 v2, (3.1)--(3.7),
<https://rstation.ai/api/v1/papers/riemann_hypothesis_10/versions/2/download>,
and the complete m-prime calculation in PR1015, commit
`e87c5f669f81fe6371af926917d1c5b21023bce8`, file
`standalone/2026-10-22-residue-remainder-followup/MOBIUS_PRIMITIVE_SCALAR_REMAINDER.md`.
The latter's equations (10)--(19) supply the precise free inverse
coefficient, balanced reciprocal-completion split, and summable local
weights. We describe all changes caused by R; the theorem is not an
application of its R=1 conclusion as a black box.

## 2. Eliminate fixed R-primes first

Write g=(n,rad R), n=g*m, so g divides rad R, (m,R)=1, m squarefree,
and its length is A=D/g. The outside coefficient has modulus g^(-1/2).
At p|R put a=v_p(R), epsilon=1_{p|g}, and

    j=(a+epsilon) modulo6, chosen in {0,...,5}.

Reduction modulo six is made only in the primitive series, where
(c,p)=1: the factor chi_c(p^6) is exactly one. The exclusion p remains
even if j=0. No sixth-power periodicity of a full continuous series
is used.

For j<=4 the exact local inversion has two terms, with numerator
valuations j and 4-j, over 1-nu(p)^6 q^(5-6u). The selected term
has a fixed root times

    q^(j+1/2-(j+1)u) * bar(chi_p(m))^(j+1).

For j=5 there is just the full-series term over the same denominator.
Let J denote the set of selected fixed primes, and put

\[
 t=\prod_{p\in J}p^{j_p+1},\qquad
 h'=\prod_{p\mid R}p^{j'_p},\qquad
 j'_p=4-j_p\ (p\in J),\quad j'_p=j_p\ (p\notin J).   \tag{P3}
\]

After reciprocity and a finite fixed ray partition, the free coefficient
is mu(m)*bar chi_m(t). All other local phases are outside that sum.
The monomials give outside modulus J^(-1/2), and physical scale U/t.
Here and below J in a norm power means the norm of the product of its
primes. Expand the fixed-prime Euler denominator in k_R supported on R:
its outside weight is k_R^(-1) and its additional scale is k_R^(-6).

Thus a fixed g,J,k_R branch is a scalar of outside size

    g^(-1/2) J^(-1/2) k_R^(-1),

at physical scale V=U/(t*k_R^6), with column length A=D/g,
fixed numerator multiplier h', and fixed coefficient twist bar chi_m(t).
The remaining primitive exclusions are those at m. The finite ray
interchanges for odd j+1 are retained; all remain in the same fixed
bad-prime vector. In particular, the growing good-prime twist is not
called a fixed ray character.

## 3. The m-prime finite and reflected estimates

Now perform the exact squarefree m-prime inversion of PR1015. Its
selected divisor is d|m; write d=f*d0 and use its notation
e=e0*e1, v=rad(k_m)/(rad(k_m),d)=e0*v0. These factors are all prime
to R. Its free inverse character is unchanged except for the fixed
multiplier t and the local R-part l of the full modulus:

    bar chi_(free m)(c0*(e*d0)^2*l*t).

The actual free coefficient is still mu times fixed ray data. The
puncture includes QR. For fixed R-local modulus choices, the map from
c0 to this inverse row is injective. The inverse input may use all
rows; any sixth-power factors retain their zero masks. The local
ratios |g6(m*h',p^j)|/q^j are at most one, and there are H^epsilon
possible fixed R-local branches, exactly as in L6--L10.

If T is the current external core scale, the two inverse row lengths
in PR1015 equation(13) become

\[
 H_o={tT\over k_m^6 f^6},\qquad
 H_r={t h'A k_m^6 d_0^6\over T}.                    \tag{P4}
\]

The l-factor cancels in the ratio of inverse-row norm to physical
modulus norm. The reflected h' appears through the numerator length;
there is no h' in H_o. The scalar lambda and the free column length
are precisely those of its equation(12), with D replaced by A.

Use the same exact reciprocal-completion variable a, but split at

\[
 C_{d,k_m}=V^{1/6}(Ah')^{-1/12}k_m^{-1}d^{-1/2}.       \tag{P5}
\]

For a<=C use completed reflection; above it use the original finite
sum minus its full pole. If C<1, use the original expression everywhere.
The cutoff is independent of the remaining free column, so the pole
below remains a complete progression pairing. Both row lengths in P4
contain t; it therefore cancels from the balanced cutoff.

Repeating the explicitly summable nonvolume weights in PR1015
(15)--(17) gives core amplitude

\[
                   A^{11/24}t^{1/12}(h')^{1/24}.      \tag{P6}
\]

The weights in e,f,d0,v0,k_m are unchanged, with smallest Euler exponent
7/6. The volume calculation (18)--(19) gives sqrt(t*V): its intermediate
factor sqrt(t)*(h')^(1/4) cancels against the h'-dependence of the
d0-cutoff. All original, reflected, and reciprocal completion ideals
are retained. The kernel arguments and derivative bounds are those
of the frozen completed FE lemma; no growing vector dimension occurs.

After the outside factors from section2, the volume square is
U*g^(-1)J^(-1)k_R^(-8), and hence sums to U times a subpower.
For the nonvolume square the fixed-prime weight is

\[
 g^{-1}J^{-1}k_R^{-2}(D/g)^{11/12}t^{1/6}(h')^{1/12}. \tag{P7}
\]

At p|R its exponent, excluding D, is

    -23epsilon/12 + j/12                         (unselected),
    -23epsilon/12 + (j-6)/12                     (selected).

Each is at most a/12, where a=v_p(R). The possible j=0 after reducing
a+epsilon=6 only decreases the exponent. Minkowski over g,J and k_R
therefore gives squared nonvolume cost D^(11/12)H^(1/12), up to a
subpower. The sum of k_R^(-1) in amplitude is a finite-prime Euler
product bounded by H^epsilon.

## 4. Partial poles: collapse the selected fixed-prime phases first

It is essential not to estimate a twisted h'-residue separately. At
theta=7/6, the exact residue density gives, for every selected prime,

    a_j(theta)*rho_full,partner = q^(-1)*rho_full,original.

This follows by taking residues in D_j=H_j+a_j H_partner and using
rho_H=(q/(q+1))*rho_D in each retained ray component. Thus the selected
term contributes minus q^(-1), including its phase. At j=5 the same
identities force the residue to vanish. Reduction of a+epsilon=6 is
compatible with the source's full-residue sixth-power periodicity.
These are residue statements only.

Apply this relation successively at the fixed R-primes and at the
selected m-primes. The original-branch pole in each fixed d,k_m,g,J,k_R
block, before the reciprocal a-tail, is exactly a unit phase times

\[
 U^{1/6}J^{-1}d^{-1}k_R^{-2}k_m^{-2}
                         P_{g d v}(D;R),             \tag{P8}
\]

where P_b(D;R) is the full-residue pairing on the original n-coefficient
with b|n and with the fixed gcd(n,rad R)=g restriction. This includes
the n-normalization; there is no extra g^(-1/2) outside P_b.
The remaining fixed restrictions become punctures after n=b*l.

The scalar residue theorem L2 gives directly

\[
 |P_b(D;R)|^2\ll(DHNQ)^\epsilon
       \{D^{2/3}b^{-5/3}+(DH)^{1/3}b^{-1}\}.          \tag{P9}
\]

Every b with a nonempty annulus is O(D). The factor from the reciprocal
a-tail is at most min(1,C^(-1))<=C^(-1), with C from P5. Combining
P8--P9 gives the two amplitudes

\[
 D^{5/12}J^{-1}t^{1/6}(h')^{1/12}g^{-11/12}
           k_R^{-1}k_m^{-1}d^{-4/3}v^{-5/6},           \tag{P10}
\]

\[
 D^{1/4}H^{1/6}J^{-1}t^{1/6}(h')^{1/12}g^{-7/12}
           k_R^{-1}k_m^{-1}d^{-1}v^{-1/2}.             \tag{P11}
\]

The first d,k_m sum converges absolutely. In the second, d<=O(D) and
the d^(-1) weight costs only a subpower: at a prime in d the local
weight is q^(-1)/(1-q^(-1)); at a prime outside d occurring in k_m
it is q^(-3/2)/(1-q^(-1)). Rankin with any positive internal epsilon
makes the first Euler product convergent. This is a finite supported
sum, not an asserted absolutely convergent d^(-1) series.

At each fixed p|R, the remaining factors in either P10 or P11, apart
from the displayed global H^(1/6) in P11, are bounded by q^(a/12).
For an unselected prime this is immediate from j<=a+epsilon and
the negative g exponent. For a selected prime use
-1+(j+1)/6+(4-j)/12=(j-6)/12. Consequently all partial poles have
total squared cost

\[
                         D^{5/6}H^{1/6}+(DH)^{1/2}.   \tag{P12}
\]

The first term is dominated by D^(11/12)H^(1/12) when H<=D, and
by (DH)^(1/2) when H>D. This proves P2 after adding section3.
Subunit physical scales remain exact negative-pole branches; they
were included in the a-tail throughout.

## 5. An actual whole Gauss-vector projection

For distinct good sixth-power-free labels NR<=K<=D, summing P2 gives

\[
 \sum_R|\mathcal P_R(U)|^2\ll(UDKNQ)^\epsilon
                 \{KU+D^{11/12}K^{13/12}\}.           \tag{P13}
\]

Use the exact primitive adjoint identity in paper10 Section7, with
v_R(z)=U^(-1/2)sqrt(w(Nz/U))*gamma_1(z)*bar chi_z(R), and the actual
inverse coefficient alpha=bar b. Suppose its Gram matrix is conditioned
in the proved PR1013 range K<=U^(1/2-delta). The complete residue vector
bound S1 supplies its pole part for K<=D^(1/7). The squared norm of
the actual projection of A_U*alpha onto span{v_R} is therefore at most

\[
 \boxed{\quad(UDKNQ)^\epsilon
       \{KU+D^{11/12}K^{13/12}+U^{1/3}D^{2/3}\}.\quad} \tag{P14}
\]

The conjugations in the adjoint identity do not change this norm.
This is a projection bound for the specific inverse coefficient,
not a full arbitrary-coefficient operator estimate.

For U=D^h with 1/2<h<1, it is strictly smaller than the inherited
nonvolume inverse bound U^(1/6)D^(5/6) whenever K=D^k with

\[
 0<k<\min\{(2h-1)/13,\;5(1-h)/6,\;1/7,\;h/2\},    \tag{P15}
\]

with a fixed margin for all epsilon losses and the Gram condition.
Near the previously binding h approximately .859, the first constraint
is about .055. This expands the controlled space beyond one vector
and includes its continuous remainder. The orthogonal complement and
the signed common-kernel first-Poisson return remain unbounded here;
P14 alone does not improve B_flat or prove RH.
