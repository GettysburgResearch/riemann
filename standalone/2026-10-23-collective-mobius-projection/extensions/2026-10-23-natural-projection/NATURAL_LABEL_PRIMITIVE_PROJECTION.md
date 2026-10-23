# A natural-length squarefree-label primitive projection

23 October2026. Proposed final assembly, independent review requested.
All earlier frozen notes remain unchanged. This concerns the actual
primitive projection, not its complementary inverse vector.

Inputs:
- COHERENT_PRIMITIVE_REMAINDER_VECTOR.md, SHA256
  bb321aae05c906187371ea7cd7a01062b19f0c0a2d889b3106c4d6e48eaaeca4.
- COHERENT_PRIMITIVE_VOLUME_SQUAREFREE.md, SHA256
  5c94ecba69197b8f129d47b5891d7a2d0adcd1835dd39778b3f03ed68e03f5ed.
- root/LOCAL_SUPPORT_VECTOR_REFINEMENT.md, SHA256
  499e1333611699c91a6c3b2cf5376f5b702bca74254b222bab47fdc93043f1dc.
- global/FIXED_PROGRESSION_RESIDUE_VECTOR.md, SHA256
  50681c59e39a1e86bb63ab792cc252e39d35b11f17576d1df5475f69de874f43.

Use all their actual Möbius, fixed profile/ray, literal-zero, puncture,
and upstream-source conventions. Labels in this note are SQUAREFREE.

The proposed continuous-vector theorem is
\[
 \sum_{\substack{NR\le K\\R\ {\rm sf}}}|\mathcal P_R(U)|^2
 \ll ((2+U)DKNQ)^\epsilon
 [U+D^{11/12}K^{1/12}+D^{5/6}K],
 \quad U\ge1,\quad K\le D^{1/7}.                    \tag{N1}
\]

## 1. The exact reassembled partial-pole interface

Remove the R-supported denominator before estimating the numerator
vector, as in CP section1. In its local expansion choose the selected
set J and only its shared subset G=J intersect support(n). Do not
classify gcd(n,R0) at the unselected remaining label R0.
The unselected local term is the full series with the actual numerator
digit, so it already contains both possibilities p|n and p not dividing n.
For squarefree R these are digits2 and1. No modulo-six exception occurs.

After fixing J,G, write n=Gm. The condition on m at the selected primes
is a fixed puncture J. The later n-prime inversion uses d and k supported
outside R. For each fixed d,k, its restrictions (d*rad(k),R0)=1 select
a subset of labels; they do not impose (m,R0)=1. Writing
v=rad(k)/(rad(k),d) and b=Gdv leaves the original coefficient with b|n,
and fixed punctures at b and the selected primes. The residual n/b
may share arbitrary unselected primes with R0.

At the residue theta, apply the exact paired local identity at each
selected label prime and each selected n-prime. For either squarefree
label digit j=1 or2, the selected partner times its local coefficient
equals q^-1 times the original full residue, with the minus sign of
inversion retained. At the n-selected primes this is precisely the
source identity sigma_d(n)*rho(nd²)=mu(d)d^-1/6*rho(n).
These operations reconstruct the original numerator nR. Therefore
the partial pole before its reciprocal a-tail is exactly a fixed phase
times
\[
 U^{1/6}P^{-1}d^{-1}k^{-2}P_b(D;R),\qquad b=Gdv,     \tag{N2}
\]
where P is the selected radical norm. The pairing P_b has only the
fixed punctures just described. There is no residual moving
coprimality condition involving the free n/b and R0.

Use the common cutoff CP5:
\[
 C=U^{1/6}(DKP^6)^{-1/12}k^{-1}d^{-1/2}.
\]
It is independent of the remaining free n and label coordinates
after their common norm-dyad separation. The entire a-tail is at
most min(1,C^-1)<=C^-1. Multiplying N2 gives exactly
\[
 (DK)^{1/12}P^{-1/2}d^{-1/2}k^{-1}P_b(D;R).          \tag{N3}
\]
These are the arithmetic hypotheses F3 of the fixed-progression note.
In particular this is not an insertion of its vector bound into the
old scalar proof's exact-gcd block.

For completeness, P_b is estimated at free lengthD/b by translating
each label R to the sixth-free reduction of bR. At residues only,
this map is injective and its norm is at mostbK. Shared b/R primes
are therefore permitted; no continuous sixth-power periodicity is used.
The fixed b/J punctures are uniform during this row average.

The whole-b split M=D1/7 from F4--F5 now applies. For b<=M it uses
the coherent progression estimate, and for b>M the scalar tail.
The complete squared partial-pole cost is
\[
 D^{5/6}K^{1/6}+D^{31/42}K^{7/6}+D^{1/2}K^{3/2}
 \ll D^{5/6}K.                                     \tag{N4}
\]
Divisor Cauchy for selected choices is taken at each original label
before summing squared P^-1 weights. Their supported sum is subpower.
The k/v sums retain their actual support, and the finite d^-1 tail
is not declared absolutely convergent.

## 2. The retained-support continuous plateau

Use root's improved completed finite bound in CP's common-row
calculation. With fixed multiplier q0 and remaining label rangeB,
the completed nonvolume plateau amplitude is
lambda*X5/12*B1/2*q0^1/12, replacing the old B7/12.
The same completion ideals and finite support are retained.
Consequently CP7 is replaced by
\[
 D^{5/12}K^{1/2}
 G^{-11/12}P^{-1/2}t_{\rm out}^{1/12}A_R^{-1/2}
 k^{-1}e^{-5/4}f^{-23/12}d_0^{-5/4}v_0^{-11/12}.     \tag{N5}
\]
Before e aggregation all ordinary n-prime weights converge as in CP.
After aggregation they remain negative powers of their dyad norms.
For ordinary selected primes, outside-modulus amplitude weights
are at most p^-5/6 and inside-modulus weights at most p^-1;
their squared sums converge. These include both selected squarefree
cases epsilon0 and1. Thus N5 has squared cost D5/6K.

The original-only w=e*d0 aggregation of the volume note also retains
this improved plateau: its w-dyad weight is w^-5/12, and its k^-1
sum is cut off by the exact original finite support. Hence it costs
only a subpower and introduces no new label power.
The balanced nonvolume term remains D11/12K1/12.
The volume note gives U, with both its nonempty-head and empty-head
ranges checked. Adding N4 proves N1 for U>=sqrt(DK).

For smaller U use the primitive finite-minus-whole-pole identity.
The primitive modulus is squarefree and coprime to nR. Direct
sixth-free large sieve, with the actual inverse coefficient, gives
\[
 (1+K/U+K^{5/6}U^{-2/3}+K^{1/3}U^{-1/6})
       (U+D^{5/6}U^{1/6}).
\]
For 1<=U<=sqrt(DK), each term is bounded by
D11/12K1/12+D5/6K in K<=D1/7. The whole pole costs
U1/3D2/3<=D5/6K1/6, also smaller. This proves the all-scale form
needed to restore the R-supported denominator by CP3.
When that restoration evaluates U/k^6 below the physical unit
support, the original finite sum is exactly zero and the term is
its negative whole pole. Its U^(1/3) scaling gives the convergent
subunit tail already retained in the all-scale inputs; it is not
replaced by a divergent constant bound.

## 3. Actual projection at the natural label length

The conditioned Gram theorem and the whole primitive residue vector
give
\[
 \|P_K A_U\overline b\|^2
 \ll ((2+U)DKNQ)^\epsilon
 [U+D^{11/12}K^{1/12}+D^{5/6}K+U^{1/3}D^{2/3}],     \tag{N6}
\]
for K<=D1/7 and K<=U^(1/2-delta).
The frame here consists of the distinct squarefree labels; it is
a subset of the previously conditioned sixth-free frame.

At U=D^h and the natural label range K=D/U, for every fixed
6/7<h<1, all four terms beat the inherited full inverse nonvolume
resource D^(5/6+h/6). Their exponents are
\[
 h,\quad1-h/12,\quad11/6-h,\quad2/3+h/3.
\]
The Gram condition is satisfied with fixed margin in this range.
For example U=D7/8 and K=D1/8 give a projected bound D23/24,
versus the old resource D47/48, a saving1/48.

This is a growing, naturally scaled physical projection theorem.
A smaller upper bound for this projection does not bound its
orthogonal complement. The full signed first-Poisson return still
requires that missing estimate. No smaller B_flat or proof of RH
is inferred from N6.

