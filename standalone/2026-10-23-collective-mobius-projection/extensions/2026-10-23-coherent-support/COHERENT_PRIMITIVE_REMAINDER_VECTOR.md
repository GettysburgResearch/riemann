# Simultaneous primitive continuation with growing sixth-free labels

23 October 2026. Proposed analytic deduction, submitted for independent
review. All earlier frozen files remain unchanged. Inputs are the PR1015
functional equation and primitive local inversion, the inherited actual
Möbius inverse-row estimate, and the sixth-free large sieve.

Use the coefficient, fixed smooth annulus, fixed ray profiles, angular
type, punctures, and literal zeros of LABEL_UNIFORM_MOBIUS_RESIDUES.md.
Source pins are corrected in SOURCE_PIN_ERRATUM.md. Let P_R(U) be the
primitive raw continuous scalar of PRIMITIVE_LABEL_CONTINUATION.md,
SHA256 a10b7626fc5a7ab7315f8327c53b2fcbe1381a2f04816a04aa697309803976ee.

For good sixth-power-free labels the proposed bound is
\[
 \boxed{\sum_{NR\le K}|\mathcal P_R(U)|^2
 \ll(UDKNQ)^\epsilon
 \{KU+D^{11/12}K^{1/12}+D^{5/6}K^{7/6}\},\quad
 1\le K\le D^{1/7},\ U\ge1.}                         \tag{CP1}
\]
The middle label exponent improves the previous scalar-summation
exponent13/12 to1/12. The last term retains both the completed-vector
plateau and a scalar bound for the partial-pole tails.

## 1. Order of the local operations

The full coherent theorem is COHERENT_FULL_REMAINDER_VECTOR.md,
SHA256 f6058c80c4bde0f049f7f7a50740cfae4d4a158a88e1bc6c0cb8534be8f215a4.
Its all-scale extension is COHERENT_FULL_ALL_SCALES.md, SHA256
55404b197241570cb4a343e7f0e53d5957a17e6077ef418312e048b9b3649dc3.
They provide
\[
 B(D,K)=D^{11/12}K^{1/12}+D^{5/6}K^{7/6}.             \tag{CP2}
\]

At each label prime use the actual numerator digit
\(j=(a+\epsilon)\bmod6\), where \(a=v_pR\) and
\(\epsilon=1_{p\mid n}\). Apply label-prime inversion first.
Every selected prime shared by n and R belongs to this operation.
The subsequent squarefree-n inversion applies only at n-primes
outside the remaining label. An unselected label prime may still
divide the remaining free n-variable; the full-vector local table
retains this case.

The label-supported denominator
\(\prod_{p\mid R}(1-\nu(p)^6(Np)^{5-6u})^{-1}\)
is independent of n and of the selected choices. It may be restored
after the entire denominator-free numerator vector is estimated.
The n-supported denominator uses only primes outside R, so no
shared prime is counted twice. For the label denominator use
\[
 \left|\sum_{\operatorname{supp}k\subseteq R}{F_R(U/(Nk)^6)\over Nk}
 \right|^2
 \le\left(\sum_{\operatorname{supp}k\subseteq R}(Nk)^{-\delta}\right)
 \sum_{\operatorname{supp}k\subseteq R}
 (Nk)^{-2+\delta}|F_R(U/(Nk)^6)|^2,\quad0<\delta<1.    \tag{CP3}
\]
The first factor is \(O_\epsilon((NR)^\epsilon)\).
After exchanging positive sums, the unrestricted k sum converges.
The volume KU is reduced by k^-6, and the nonvolume bound is
uniform in the physical scale. Outside unit phases are harmless.
This operation removes no arithmetic zero inside F.

## 2. Selected labels and the common inverse row

Let J be the selected label-prime set, P its radical norm, G the
norm of the part shared by n, and A_R the original label norm on J.
Let S be the norm of the subset also occurring in the full Gauss
modulus. Put \(B=K/A_R\) for the remaining label range. These norms
are first placed in dyadic ranges.

For an ordinary selected branch \(a+\epsilon\le4\), inversion
changes the numerator digit j to4-j and introduces the character
of exponent -(j+1), with outside squared weight q^-1-epsilon.
Set t=product p^(j+1), h'=product p^(4-j). Then
\(t h'=P^5\), and on these branches \(t=A_RGP\).
If a selected p also occurs in the full modulus, that modulus has
digit5-j. Its total inverse-row digit is six, with an extra squared
factor q^-1. This is a puncture, not a nontrivial free character.

For the ordinary n-prime decomposition of PR1015 retain
\[
 d=f d_0,\quad e=e_0e_1,\quad v=e_0v_0,\qquad
 X=D/(G e f d_0v_0).
\]
The exact common inverse row after full Gauss extraction is
\[
 r=c_0(e d_0)^2t_{\rm out}S^6,                       \tag{CP4}
\]
up to fixed ray sectors. Here t_out uses selected primes outside
the full modulus. Both free characters are bar(chi_m(r)) and
bar(chi_R0(r)). The selected multiplier twists the entire free
numerator m*R0. All natural zeros are retained. There is no
arbitrary multiplier depending jointly on R0 and the column.

Apply the R0 sieve separately for each selected J, and KEEP its
resulting inverse-row norm restricted to rows CP4. Only afterwards
sum those positive restricted norms over selected primes outside
the modulus. Each final row r has divisor-many representations
by t_out, (ed0)^2, and c0. This removes a count of selected labels
at subpower cost. It is neither a claim of a unique representation
nor an enlargement of the column length before the sieve.
Selected primes inside the modulus are frozen separately and have
convergent positive weights below. Norm dyads and Mellin separation
supply common smooth profiles before applying the inverse-row bound.

## 3. Continuous terms

For a denominator-free label component, the original and reflected
inverse scales in the reciprocal a-sum are
\[
 L_o=U/(k_m^6f^6a^6),\qquad
 L_r=DKP^6k_m^6d_0^6a^6/U.
\]
The balancing point is
\[
 A=U^{1/6}(DKP^6)^{-1/12}k_m^{-1}d^{-1/2}.           \tag{CP5}
\]
An empty head is treated by the original finite-minus-pole identity,
as in the all-scale extension. No contour estimate is invoked
merely because a formal cutoff lies below one.

The balanced nonvolume amplitude, with every outside scalar, is
\[
 D^{11/24}K^{1/24}P^{-1/4}G^{-11/12}S^{-1/2}
 k_m^{-1}e^{-17/12}f^{-13/6}d_0^{-7/6}v_0^{-11/12}.   \tag{CP6}
\]
The ordinary n-prime Euler sums converge. A v0-only prime also
occurs in k_m, giving total exponent at least23/12; the other
least exponent is7/6. The squared P and S factors on the selected
inside-modulus part cost at least S^-3/2 and sum positively.
For the outside part, aggregate the restricted inverse-row norms
after CP4, before replacing them by the unrestricted inverse norm.
Squaring CP6 gives the middle term of CP1.

The completed finite-vector plateau amplitude is
\[
 D^{5/12}K^{7/12}
 G^{-11/12}P^{-1/2}t_{\rm out}^{1/12}A_R^{-7/12}
 k_m^{-1}e^{-5/4}f^{-23/12}d_0^{-5/4}v_0^{-11/12}.    \tag{CP7}
\]
Retaining f^6 in the inverse row rather than putting it in a fixed
puncture changes f^-23/12 to f^-17/12, still summable.
Again v0-only primes occur in k_m. At an ordinary selected prime,
the amplitude exponents are
\[
 -(10\epsilon+5+6a)/12\le-11/12
       \quad(p\text{ outside modulus}),
\]
\[
 -(11\epsilon+6+7a)/12\le-13/12
       \quad(p\text{ inside modulus}).
\]
Their squared Euler weights converge after divisor Cauchy.
The original finite support makes the plateau's harmonic sums
finite; the infinite subunit pole is treated separately.
Thus CP7 costs D^(5/6)K^(7/6), up to subpowers.

The exceptional shared case a=5,epsilon=1 has reduced digit zero
and must NOT use t=A_RGP. For an unselected such part E, primitive
reduction replaces H(p^6) by H(1) with its puncture retained.
Write R=E^5R1,n=Em. The outside squared weight is E^-1 and the
remaining scales are D/E,K/E^5. The two CP2 weights become
E^-7/3 and E^-23/3 and sum positively. This does not assert the
false full continuous-series identity D(p^6)=D(1).
There is a further moving exclusion that must be retained. More
precisely, let T be the radical of the fifth-power part of R and
G=gcd(n,T). Write R=G^5R',n=Gm, so the reduced numerator is mR'
and (m,T)=1. Expand the remaining condition exactly as
1_(m,T/G)=sum_(E|gcd(m,T/G)) mu(E). Put m=Ez and
R=G^5E^5R2. The free z is punctured only at fixed GE; R2 is
coprime GE but may share arbitrary primes with z. The full
numerator is E^6*z*R2, never reduced modulo sixth powers.
The outside amplitude is (GE)^-1/2, the free length D/(GE),
and the remaining label range K/(GE)^5.
At each p|E the only full-modulus branches are j=0,6,7, with
Gauss ratios 1,1-q^-1,q^-1/2. Their free characters are either
trivial with their puncture, or bar(chi_z(p^7)) and
bar(chi_R2(p^7)); thus the common-column identity is preserved.
The balanced squared weight is G^-7/3 E^-11/6 for j=0,6;
j=7 gains another E^-1. The plateau weights in E are
E^-23/3, E^-20/3, E^-15/2, while G contributes G^-23/3.
All sum positively after divisor Cauchy over G,E for each
original label. This exact finite extension repairs the moving
fifth-power exclusion; it is not a positive deletion of it.
For its selected branch, t=p,h'=p4, free length D/p, remaining
label K/p5 and outside amplitude p^-1. The original inverse
length is U and the reflected length DK/U; the balanced term
has extra amplitude p^-17/12, already absolutely summable.
An additional occurrence in the full modulus only helps.

## 4. Volume and partial poles

Keep the old scalar volume bound U per label, hence KU.
The old scalar primitive proof P4--P7 uses the same cutoff CP5:
shared unselected n/R0 primes cancel between the free-column
length and reflected numerator norm. Thus two incompatible
free splits are not being combined.

For partial-pole tails, scalar P9--P12 summed over labels gives
\[
 D^{5/6}K^{7/6}+D^{1/2}K^{3/2}.
\]
The second is bounded by the first for K<=D. No new coherent
residue cancellation is assumed. The whole primitive pole is
excluded from the raw continuous scalar. Restoring CP3 proves
CP1 for U>=sqrt(DK).

For smaller U use the primitive finite-minus-whole-pole identity.
At good primes the primitive modulus is squarefree and coprime
to nR, so the zero-extended large sieve and the actual inverse
estimate give the coarse finite vector envelope
\[
 U+D^{5/6}U^{1/6}+K^2+D^{5/6}K^{7/6}.
\]
The whole pole costs U^(1/3)D^(2/3), by S1.
For U<=sqrt(DK), all terms are bounded by CP2 when K<=D^(1/7).
This proves the all-scale assertion used in CP3.

## 5. Actual physical projection and its limitation

The PR1013 half-range Gram theorem gives
\[
 \|P_K A_U\overline b\|^2
 \ll(UDKNQ)^\epsilon
 [KU+D^{11/12}K^{1/12}+D^{5/6}K^{7/6}+U^{1/3}D^{2/3}], \tag{CP8}
\]
provided K<=U^(1/2-delta) and K<=D^(1/7).
Here A_U bar(b) is multiplication, with the actual adjoint
orientation in the witness-frame definition retained.

For U=D^(6/7),K=D^(1/12), the four exponents are
79/84,133/144,67/72,20/21. Thus CP8 is D^(20/21+epsilon),
against the inherited full inverse nonvolume exponent41/42,
over growing labels of size D^(1/12).

This controls the projection only. Its complementary row vector
is not bounded at the improved scale. No smaller B_flat follows.

