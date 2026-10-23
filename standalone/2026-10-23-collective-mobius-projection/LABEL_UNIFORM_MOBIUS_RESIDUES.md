# Label-uniform scalar Möbius pairing with the full and primitive sextic residues

23 October 2026. Status: proposed analytic lemma, independent review pending.
This is a scalar theorem for each fixed numerator label, with uniform dependence
on that label. It does not control arbitrary linear combinations of labels or
the complementary operator in the signed inverse moment. No smaller zero-free
boundary is claimed here.

## 1. Precise inputs and statement

Use the good Eisenstein ideals, fixed modulo-36 original sections, literal
nonunit zeros, and Mellin normalization of PR1015 at commit
`e87c5f669f81fe6371af926917d1c5b21023bce8`, specifically
`MOBIUS_FULL_SERIES_SCALAR_REMAINDER.md` (SHA256
`b45267a73c0123cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a`)
and `COMPLETED_FE_KERNEL.md` (SHA256
`6f050d0e66769b4989a4b7c42f1a555ee10a2ee05a14ea1585595c784425066e`).
The primary finite-vector functional equation is Bröker--Hoffstein,
<https://arxiv.org/html/1312.0568v1>, (3.1), (3.8)--(3.10).
The full/primitive residue density, at every numerator valuation, is
rStation paper 8 version 1, Section 3:
<https://rstation.ai/api/v1/papers/riemann_hypothesis_8/versions/1/download>.
These are imported analytic statements; this note does not recertify them.

Within exponents, ideal letters denote their norms. Let h be any fixed good
nonzero ideal, not necessarily squarefree, and write H=Nh. Fix smooth annular
W,w, fixed ray data, a numerator ray-sector filter, and a puncture Q fixed
throughout every row average. Set

\[
 b_n={\mu(n)\nu_0(n)\over\sqrt{Nn}}W(Nn/D)1_{(n,Q)=1},\qquad
 P_h^{\rm full}(D)=\sum_n b_n\rho_{\rm full,\nu}(nh),\qquad
 P_h^{\rm prim}(D)=\sum_n b_n\rho_{\rm prim,\nu}(nh).       \tag{L1}
\]

The proposed conclusion is

\[
 \boxed{\ |P_h^{\rm full}(D)|^2+|P_h^{\rm prim}(D)|^2
   \ll_\epsilon(DHNQ)^\epsilon
          \{D^{2/3}+(DH)^{1/3}\}.\ }                    \tag{L2}
\]

In particular the scalar bound is D^(2/3+epsilon), uniformly for H<=D.
The earlier reference-scale estimate was D^(2/3)H^(1/3). The improvement
comes from the completed functional equation applied to the actual Möbius
pairing; it is not a replacement of the Möbius coefficient by arbitrary data.

The exact inverse input is the inherited actual-coefficient bound

\[
 I(T,A;Q')=\sum_{0<Nr\le T}\left|\sum_m
 {\mu(m)\xi(m)\over\sqrt{Nm}}V(Nm/A)1_{(m,Q')=1}
                  \overline{\chi_m(r)}\right|^2
 \ll(TANQ')^\epsilon\{T+T^{1/6}A^{5/6}\}.             \tag{L3}
\]

Here xi is fixed ray data, and V has the permitted smooth norm twists and
their polynomial seminorm cost. The puncture is fixed during the r-sum.
The all-row form of L3 suffices; all rows can alternatively be reduced by
sixth powers while retaining their zero masks. No growing ray character
is inserted into xi.

## 2. Full finite moduli with an arbitrary fixed numerator label

For a fixed common smooth annular profile in n/D and c/U, consider

\[
 S_h(U)=\sum_n b_n\sum_c{\nu(c)g_6(nh,c)\over Nc}
                       \Phi(Nn/D,Nc/U).                \tag{L4}
\]

We claim the uniform bound

\[
 |S_h(U)|^2\ll(UDHNQ)^\epsilon
                    \{U+U^{1/6}D^{5/6}\},\quad U\ge1. \tag{L5}
\]

First write n=g e m, where g=(n,rad(h)), e consists of those primes outside
h that occur in c, and m is the remaining squarefree part. The factors
g,e,m are pairwise coprime, g divides rad(h), and (em,h)=1. At a prime
outside h, the nonzero local possibilities are modulus exponent one when
the prime does not divide n, or exponent two when it divides n. Thus

\[
             c=e^2 l c_0,\qquad l\mid h^\infty,        \tag{L6}
\]

where c0 is squarefree and (c0,nh)=1. For each fixed g, the possible local
exponents j=v_p(l) are determined by v=v_p(h)+1_{p|g} as follows. For
6 not dividing j, the only possible nonzero valuation is j=v+1. For
6 dividing j, the local character is principal and its Ramanujan sum
vanishes unless j<=v+1. The case j=0 is included. There are at most
O(v+2) choices at p, hence H^epsilon possibilities in total, with fixed
epsilon-dependent constant. In every case

\[
                |g_6(nh,p^j)|/(Np)^j\le1.             \tag{L7}
\]

At p|e the ratio is (Np)^(-1/2). After extracting the n-normalization,
the scalar before the c0^(-1/2) coefficient is therefore at most

\[
                         e^{-1}g^{-1/2}.               \tag{L8}
\]

The free m-dependence must be tracked before using L7. Fourier scaling
at p^j supplies bar(chi_p(m))^j; at e it supplies the square of that
character, and c0 supplies its first power. Fixed reciprocity sectors
therefore give precisely

\[
                   \overline{\chi_m(c_0e^2l)}.         \tag{L9}
\]

For j divisible by six this is the appropriate coprimality mask, not
a discarded factor. All remaining Gauss roots, fixed h-factors, and CRT
phases are outside the m-sum. They have modulus at most one after L7--L8
are extracted. The free coefficient is the original mu(m), with fixed
ray data and puncture Qeh. The puncture records (m,h)=1 even at primes
of h absent from l. The modulus c0 gives its own natural zero mask.

For fixed e,g,l, the map c0 -> c0 e^2 l is injective and has norm O(U).
Cauchy in c0, using sum_(c0~U/(e^2 l))1/Nc0=O(1), gives

\[
 |S_{e,g,l}(U)|^2\ll e^{-2}g^{-1}I(CU,D/(eg);Qeh).    \tag{L10}
\]

The volume square roots sum with e^(-1), costing a logarithm. The
nonvolume square roots sum with e^(-17/12). The g-divisor sum and all
admissible l choices cost H^epsilon. Thus Minkowski proves L5. Empty
or bounded-size annuli with subunit residual lengths are treated with
the exact support, or a fixed enlargement of a unit row ball. Common
profiles are separated in their two annular norm coordinates using the
same Mellin/Fourier seminorm argument as PR1015. In particular a
row-dependent arithmetic coefficient has not been inserted into L3.

The finite physical normalization U^(-1/2)g_6(nh,c)/sqrt(Nc) differs
from L4 on a modulus annulus only by a fixed smooth norm profile, and
satisfies L5 as well.

## 3. Reflect the completed scalar before estimating its residue

Let Z_nh(u)=zeta_S(6u-5)D_nh(u), and use the contour functional

\[
 F_h(Y)=\sum_n b_n{1\over2\pi i}\int_{(1+\eta)}
 Z_\nu(nh,u)\widehat w(u-1/2)Y^{u-1}\,du,
                    \quad0<\eta<1/12.                 \tag{L11}
\]

The completed-reflection kernel of PR1015 retains the same numerator nh
and the same Gauss orientation. Its reflected argument is
Nc(Nb)^6Y/N(nh). Therefore its effective row scale is

\[
                         C=DH/Y.                       \tag{L12}
\]

Apply L5 on each modulus dyad, retaining every reflected completion
ideal b, including bad-prime ideals. The kernel is O(x^(1/6-delta))
at zero and rapidly decreasing at infinity. The two square-root
completion weights are b^(-4) and b^(-3/2). Exactly as in the frozen
kernel proof, the dyad and completion sums converge and yield

\[
 |F_h(Y)|^2\ll(YDHNQ)^\epsilon
                       \{C+C^{1/6}D^{5/6}\}.           \tag{L13}
\]

The finite local vector is partitioned by the residue class of nh at
the fixed bad places, so its cardinality and fixed rescalings do not
grow with H. The pole crossed in the reflected expansion is canceled
by 1/G(-s), as in the imported completed kernel. No new residue is
silently dropped.

On the original side the exact completed finite-minus-pole identity is

\[
 F_h(Y)=\sum_{b\ {\rm good}}{1\over Nb}S_h^{\rm phys}(Y/(Nb)^6)
       -\zeta_S(2)\widehat w(2/3)Y^{1/6}P_h^{\rm full}(D). \tag{L14}
\]

For the purpose of bounding the residue, choose once and for all a
nonnegative nonzero w, so that its displayed Mellin value is positive.
The first term in L14 is bounded by the square root of
I(Y,D), through L5 and the same convergent completion weights. Combining
L13 and L14 thus proves, without an imported residue estimate,

\[
 |P_h^{\rm full}(D)|^2\ll(YDHNQ)^\epsilon Y^{-1/3}
 \{Y+Y^{1/6}D^{5/6}+DH/Y+(DH/Y)^{1/6}D^{5/6}\}.       \tag{L15}
\]

If H<=D take Y=D; every quantity inside braces is O(D). If H>D take
Y=sqrt(DH)>=D; both row scales coincide, and both inverse inputs are
O(Y). These choices prove the full-residue half of L2.

## 4. Transfer the whole residue to its primitive density

At the residue only, paper 8 gives

\[
 \rho_{\rm prim}(nh)=\rho_{\rm full}(nh)
       \prod_{p\mid nh}(1+(Np)^{-1})^{-1}.             \tag{L16}
\]

The h-factor is fixed and at most one. Expand the remaining n-factor as

\[
 \prod_{p\mid n,\,p\nmid h}{Np\over Np+1}
 =\sum_{d\mid n,\,(d,h)=1}{\mu(d)\over\prod_{p\mid d}(Np+1)}.
                                                               \tag{L17}
\]

Put n=dm in each term. The new length is A=D/Nd, label is dh, and
puncture is Qd. The scalar outside the normalized Möbius coefficient
in m has modulus at most d^(-3/2). The fixed numerator sector is still
one of the original finite sections. The full-residue bound just proved
therefore bounds the squared term by

\[
 (DHNQ)^\epsilon
 \{D^{2/3}d^{-11/3}+(DH)^{1/3}d^{-3}\}.                \tag{L18}
\]

Both square-root weights sum absolutely. This proves the primitive
half of L2, including all shared primes of n and h. No density identity
away from the pole has been used.

## 5. Full-series remainder consequence and exact limitation

For a general fixed annular w, let R_h(U) be L11 with raw D in place
of completed Z. Exact reciprocal completion on the original line is

\[
                 R_h(U)=\sum_a{\mu(a)\over Na}F_h(U/(Na)^6). \tag{L19}
\]

For U>=sqrt(DH), split at A=U^(1/6)(DH)^(-1/12)>=1. Use L13 for
a<=A and the exact original finite-minus-pole identity for a>A, keeping
all subunit scales. The squared reflected/original volume costs are
(DH)^(1/2); the nonvolume costs are D^(11/12)H^(1/12). By L2 the
squared tail-pole cost is at most
(DH)^(1/6)[D^(2/3)+(DH)^(1/3)], which is dominated by these two terms.
Consequently

\[
 \boxed{\ |R_h(U)|^2\ll(UDHNQ)^\epsilon
       \{D^{11/12}H^{1/12}+(DH)^{1/2}\},\quad U\ge\sqrt{DH}.\ } \tag{L20}
\]

For H<=D the first term dominates. This is a full-series scalar
remainder. The moving-coprimality primitive remainder requires its own
valuation-sensitive inversion, and is not asserted in L20. Even a
primitive analogue would not control the complementary operator or
the full signed initial Poisson return. L2 can be inserted into a
residue projection only with its actual label sum and Gram factors
retained; summing it trivially over H<=K gives a factor K, not a
label-independent vector norm.
