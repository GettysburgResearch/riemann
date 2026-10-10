# Independent scoped review of signed auxiliary reunion

Reviewer: higher_balanced_attack. This is an independent mathematical review,
not the author's self-check. The reviewer did not edit the reviewed proof.

## Review object and disposition

Reviewed proof: /workspace/scratch/6ec6134c1535/pass2_signed_auxiliary.md.
A byte-identical copy under a packet filename has the same review scope.

Final SHA-256: 6b8277e64adb1121704fbf7dc4553aeda31b598c65e0279d80316a35d66d38bf.
Final byte count: 27,692.

Disposition: PASS within the stated component scope and explicit premises.
The exact divisor reunion, the second row Poisson identity, the finite-ray
scalar, the fixed-order tensor allocation, the sharp reunited-divisor tail,
and the two complete smooth block bounds have been checked. No missing
coprimality condition, norm power, extra zero frequency, or unstated native
higher-moment estimate was found.

This does not certify a full fourth or generalized 2k-th moment, a cofinal
moment hierarchy, the imported canonical mean-square theorem, or a new
zero-free half-plane. For beta less than one, the review treats equation
(4.1) as the explicitly additional uniform finite-order inverse estimate.
The beta equals one specialization uses ideal counting and the cited exact
arithmetic and Poisson identities.

## Sources independently checked

The following local files were read in the relevant sections and their
SHA-256 values were verified.

| Source | Exact scope checked | SHA-256 |
| --- | --- | --- |
| PR #914, commit 0cc0428fedbbfc340044c7451b3d392c1da9a103, A2_COMPLETION.md | Equation (6.3), its R_L convention, all element rows, and strict off-diagonal extraction | d99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad |
| Imported OpenAI/math October 5 paper2.tex at commit adc7f1241b42e322a6451854ab7e4b4c146bf78a | lem:arithmetic, eq:crt-a, eq:convert1, eq:quotient, lem:poisson, and the corresponding arithmetic proof | d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d |
| PR #921, commit 4e6d4aa57ae4cb04d76b2b31279ac367951b469a, HERMITIAN_INCIDENCE.md | Forward coprimality correction and zero extension | 5c1844409097959a772916e1658ec61dfa747da857dd48321869d0a38cbc66e9 |
| PR #913, commit 6498d6cc2eded03159c7332b25fd224ad07f89c1, FOURTH_MOMENT_ATTACK.md | Section 8 statement of the optional common-zero-free uniform reciprocal premise | 354e8f7f5f81d0f8821ea6e821f55546f9c9641ac0690def1ae373000b4b3d08 |

The local source paths are those named explicitly in the reviewed file.
No adjacent PR is silently promoted to a premise.

## 1. Exact signed divisor reunion

At a nonzero original term, squarefreeness of both supported columns forces
b, f, d, z_1, z_2 to be pairwise coprime, where d=(m_1,m_2) and m_i=d z_i.
It does not force (k,f)=1. The common part of the two literal row symbols is
the exact mask 1_{(k,d)=1}; this remains true when k is a nonunit at any
prime of d.

The native Gauss CRT produces psi(d^4), and the original auxiliary factors
produce psi(f^4). Their product is psi(w^4), with w=fd. All columns are
bwz_i and the kernel is independent of the divisor f of w. Hence the
remaining local signed factor is precisely
1_{p does not divide k}-1 at each p dividing w. Its product is
mu(w) 1_{w divides k}. This proves the full divisor collapse without
dropping the original nonunit zeros.

After k=wh there is no new coprimality restriction (h,w)=1. Multiplication
by the fixed primary generator of w is a bijection from all Eisenstein
element h to the elements divisible by w; all six unit multiples survive.
The coefficient calculation gives H/(L Nw sqrt(C)), exactly as in (2.7).

Because z_1 and z_2 are coprime, the original condition m_1 != m_2 is
equivalent to excluding their unit pair. In particular this is an
off-diagonal condition on the original product columns, not on arbitrary
factor tuples.

The sharp selection Nw >= R is constant through every divisor partner.
Its original pullback is N(f (m_1,m_2)) >= R. It is therefore valid before
or after reunion. A selection on f alone would not have this property.

## 2. Second Poisson normalization and finite-ray coefficient

At each prime of z_1 z_2 the local character exponent is 1 or 5, so the
primitive pair character is nonprincipal and primitive at its exact
squarefree modulus. Both the h=0 term and the dual r=0 term vanish.
This justifies their exclusion; inserting an unconditional zero-row
contribution would change the later tail estimate.

With the source self-dual radial transform and
T=Nw C/H, the primitive Poisson prefactor is T/sqrt(C)=Nw sqrt(C)/H.
The dual radial argument is T Nr/C=Nw Nr/H. Radial Fourier inversion
returns Phi after the second transform. The factor psi(w)^5 equals
conjugate(psi(w)) on the retained coprime support. Thus the normalization
in (3.2) is exact and cancels the first prefactor down to 1/L.

The CRT Gauss scalar is
gamma_1(z_1) gamma_{-1}(z_2) chi_{z_1}(z_2)
conjugate(chi_{z_2}(z_1)).
The last two factors equal the source's symmetric sign-valued
reciprocity bicharacter. Multiplying by the two native a_xi coefficients,
using eq:convert1 and
gamma_{-1}(z)=chi_z(-1) conjugate(gamma_1(z)), leaves exactly
mu(z_1) mu(z_2) xi(z_1) conjugate(xi(z_2)) G(z_1 z_2^{-1}).
The quotient convention is exactly eq:quotient with a=z_2 and b=z_1.
No archimedean alpha factor remains.

Consequently (3.6) has precisely the native phases at the element row rw.
The expansion of G is on its fixed finite ray group, so it adds only a
fixed finite family of coefficient characters. It does not represent a
moving angular Fourier expansion.

## 3. Pointwise tensor estimate and true kth convolution coefficients

The forward local quotient (1-sum t_i)/product(1-t_i) has coefficient
1-|I| on a nonconstant monomial with support I. It has no one-axis terms.
At the common beta weight its absolute Euler factors are
1+O((Np)^(-2 beta)), and their product converges because beta>1/2.
The finite omitted-prime factors are subpower in the stated moving
modulus. Nonunit row phases set the corresponding variables to zero;
the correction does not replace them with value one.

The shifts require (4.1) at every smaller scale, with finite smooth-test
seminorm control. Both requirements are explicitly stated. A shifted
scale below the fixed support threshold contributes nothing. Mellin
separation of the fixed coupled profile introduces only polynomial test
seminorm growth, absorbed by rapid Mellin decay.

For fixed g=bw, each prime of g has exactly one left and one right
factor index. Thus the disjoint g_ij allocation is exact and has at most
k^(2 omega(g)) possibilities. The remaining 2k axes are pairwise disjoint
across both columns and avoid gS, or q_0 gS for the stated moving mask.
Their scales have products L/Ng on each side. Applying the tensor
estimate to these actual inverse coefficients gives (L/Ng)^(2 beta).
The argument never applies an inverse estimate to arbitrary arithmetic
coefficient weights.

The primitive unit-pair subtraction is harmless because it can contribute
only when Ng is comparable to L. Its fixed-order divisor coefficient is
subpower, and the proposed bound is then of constant scale.

## 4. Sharp quantitative tail and unrestricted rows

The nonzero Eisenstein row lattice has O(T) elements of norm at most T.
Combining this with Schwartz decay gives H/Nw for Nw<=H and an
arbitrarily high power of H/Nw when Nw>H. Excluding the zero row is
necessary for the second assertion and has already been proved exactly.

On row annuli for N(rw), the reference parameter can be enlarged to
D_j=2^j D. If the original polynomial conductor exponent is at least one,
the row conductor, fixed column scales, and moving exclusions all remain
in the declared domain of (4.1). The incurred factor 2^(j epsilon_0) is
absorbed by the fixed Schwartz power. This handles every nonzero row,
including the unrestricted Schwartz tail; it does not truncate the row
family.

After the primitive-column estimate, the positive majorant is
D^epsilon H L^(2 beta-1) times
sum_b (Nb)^(-2 beta) times sum_{Nw>=R}(Nw)^(-2 beta-1).
The first series converges, and elementary ideal counting bounds the
second by R^(-2 beta). The proof correctly absorbs finite support and
divisor losses before extending the positive majorant to all ideals.
No boundary smoothing is needed for the sharp w cutoff.

The sufficient condition R>=L^((2 beta-1)/(2 beta)) follows exactly.
The displayed fourth-order exponents, including the rational
139999/160000 specialization, were independently recalculated.

## 5. Complete smooth blocks and cancellation in w

The two matrix allocations for b and w are exact and preserve all
disjointness. Once the b-matrix and singleton tuples are fixed, the
w_ij variables have the literal coefficient
mu(w_ij) conjugate(psi_{z_1,z_2}(w_ij)).
This is a finite-order character with the stated polynomial conductor.
It is independent of r. The correct moving exclusion is q_0 b z_1 z_2 S;
there is no exclusion by r.

Each w_ij divides one of the original native factors of norm O(D).
Therefore its dyadic scale lies within the X<=C D domain of (4.1),
even though the complete product w can have norm of order D^k.

On normalized smooth dyads, derivatives of the coupled V arguments
remain uniformly bounded: wherever a derivative of V is nonzero, the
original arguments lie in its fixed compact support. Derivatives of
Phi(Nw Nr/H) have arbitrarily large decay in 1+W Nr/H.
Thus the k^2-variable tensor estimate yields W^beta with the same
Schwartz row decay.

There are O(D^epsilon B) frozen b-assignments and
O(D^epsilon Z^2) singleton tuples. The support gives Nz_i comparable
to Z=L/(BW), so these counting bounds are uniform, including nonempty
bounded subunit scales. Division by L and the nonzero row count H/W
give H Z W^(beta-2). The independent fixed-column argument gives
H Z^(2 beta-1)/W. Taking the minimum is valid; multiplying the two
savings is not done.

For beta<1, the first bound is strictly smaller when W>Z^2 and the
second when W<Z^2. For beta=1 the bounds agree identically.
The author's final wording correction states this endpoint explicitly.

## Verification record and limitations

An independent exact integer check covered the local divisor identity
for every row divisibility pattern on zero through eight labelled primes:
511 cases passed. Exact rational arithmetic reproduced the three
displayed fourth-order tail exponents and cutoffs. These finite checks
supplement the local and analytic proofs; they do not prove an infinite
moment estimate or the optional hypothesis (4.1).

The final delta from the previous SHA
0812e6d5b4615c017f320f6333d5fa2868f1120d5b8b1b46702463c4fa8976cb
was inspected and is limited to the beta=1 comparison clarification.
The reviewed final proof is bound only by the final SHA stated above.

The remaining b=w=1 primitive block is not controlled at normalized size H
by these arguments. The proof correctly identifies it as a remaining
obstruction. The new theorem removes a genuine large reunited-divisor
component at every fixed order; it does not establish the full hypothesis.

