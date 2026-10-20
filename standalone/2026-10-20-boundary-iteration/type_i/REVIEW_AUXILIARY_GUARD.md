# Independent review of the finite-place cubic guard

Date: 2026-10-20. Reviewer: Type-I subagent, independently of the author
of the proposed guard.

**Verdict:** no outstanding issue was found in the local arithmetic,
constant-term cancellation, exact Poisson return, or transfer of the
sharper additive Gram estimate in the frozen note below. This review
supports that adapter under its stated source inputs. It is not an
independent certification of the entire zero-free bootstrap or of every
imported preprint.

## Frozen evidence

The reviewed file is ../global/ALL_FIELD_AUXILIARY_GUARD.md, SHA256
c87cfe0290d28a685c79c79b056907b07cd8f4ec62360a855c1648f7c673695e.

The first pass reviewed SHA256
0b9186e02af57ad5c5351c7d9995ce31dfabd64b6e81bdc48c645ea4362d1c73.
The final pass additionally checked the explicit low-side formula (6.1),
the reconstructed Weil/Gauss unit character, and the scalar \(bI\)
in Weyl conjugation. These additions agree with the calculations below.

I checked the following immutable source files at the commit specified
in that note, not just its paraphrases:

| Source | SHA256 |
|---|---|
| Ope26b 02-arithmetic.tex | 892ce2d22b787810e4e7dc3dda9ac54877a3b749e5cc87c1e21868c1a72f492b |
| Ope26b 03-theta.tex | fb55e83219ef28a92f0be4f5fce77207be96c6573c3660e5182eb0f435016587 |
| Ope26b 04-reflection.tex | d76f23137518b7b6ffb491f86598570ec1a89adf43320775eafed5661ce30407 |
| Ope26b 05-poisson.tex | bd5e53c2d9436aa1c621dca2d1c423035b610b423f064f7d5b6e19f3d9f31992 |
| Liu 2610.26835v1, locally extracted text | c4bf60ae996c21718a97bbff7a7bd27522fd8c20900589f4221ebb5f1152d28a |

The exact Liu locators for the sharper Gram return are
S13.SS2.p18 through S13.SS2.p25, culminating in (13.7).
The theta central datum is Ope26b eq:theta-central-datum;
the row correction is eq:reflection-moving-twist through
eq:reflection-S-character. The high-side Fourier argument is in
eq:finite-Poisson-transform and the subsequent unfolding into
eq:Poisson-orbits.

## 1. Auxiliary prime, generators and character orientation

Choose the initial fixed set to contain the target's finite conductor
and every bad theta/additive place. A sufficiently deep identity ray
condition on a principal prime \(\mathfrak p_*=(\pi)\) makes \(\pi\)
a sixth power at every old finite place. At the good new place,
the tame pairing of two units is one. Reciprocity therefore makes
every old S-unit a sixth power locally at \(\mathfrak p_*\).

The old S-unit image thus has trivial new coordinate, while \(\pi\)
has trivial old coordinates and spans the new valuation line. The
new unit line is a complementary isotropic line. Consequently
\(B_S=B_{S_0}\oplus B_*\) is an actual allowed complement. Exterior
allowed generators can have new valuation zero, with balancing done
by old sixth-power units. This changes no moving length or dimension.

Writing \(H_*(\pi,u)=\chi_*(u)^{-1}\), reciprocity on an allowed
exterior \(A\) gives
\[
  H_*(A,\pi)\prod_{\mathfrak q\mid A}
                  H_{\mathfrak q}(A,\pi)=
  \chi_*(A)\chi_{\mathfrak A}(\pi)^{-1}=1.
\]
Thus \(\psi(\mathfrak A)=\chi_*(A)^2
=\chi_{\mathfrak A}(\pi)^2\), with the orientation claimed in the
note. The extension \(\lambda_*(\pi^e u)=\chi_*(u)^2\) is trivial on
all enlarged S-units and on the norm section.

The original exterior Gauss data remain consistent: old allowed
generators of ideals prime to the new prime are still allowed with
the adapted complement. Old residue representatives are integral
at the new place, whose additive character is then trivial in the
Gauss sum. Hence the original \(\Lambda,G\) characters can be retained
at exterior primes, and they are unramified at \(\mathfrak p_*\).
No unmentioned new target twist enters through their normalization.
Equivalently, without requiring any particular generator to be kept,
the source Weil-index construction of \(G\) is trivial on the new
unit line: its unramified local Weil character and the Kummer factor
of \(4\) are trivial there. This is the normalization-independent
check made explicit in the frozen version.

## 2. Physical support and the surviving unit digit

The new local test and norm-one weight satisfy the exact low-side
identity
\[
 \lambda_*(t_0)
 W_{0,*}(m/t_0)
 =\lambda_*(m)\,
       \mathbf1_{\{v_*(m)=v_*(t_0)\}} .
\tag{R1}
\]
The finite coordinate of the norm section is one. Together with
the mask on \(t_0\), this forces \(v_*(m)\equiv-1\pmod6\).
The direct average is therefore a restriction of the existing row
set, with a unitary row phase and a fixed ideal-column twist
\(\psi(\mathfrak s)^{-1}\).

Write \(m=\varepsilon_m m_0\) with \(v_*(m_0)=0\).
On units the actual row correction is
\[
 H_*(\varepsilon_m,u)^{-1}
   =\chi_*(u)^{v_*(\varepsilon_m)}
   =\chi_*(u)^{-1}.
\]
The theta coefficient twist contributes \(\chi_*^{-2}\).
Their product is \(\chi_*^{-3}=\chi_*^3\), rather than the
digit obtained by omitting the row-unit correction.

## 3. Weighted constant-term cancellation

There is a cube unit \(b\) with \(\chi_*(b)=-1\): take the cube of
a unit whose sextic character is primitive. Its class belongs to
the whole new unit line \(B_*\), so multiplication by \(b\)
preserves the actual \(B_S\) cutoff as well as the norm sheet.

The source central inducing datum on diagonal cubes is
\(\lvert x^3/y^3\rvert^{1/6}\). On cube units it is one.
The two ordinary Jacquet constituents have that central datum and
its Weyl conjugate, including the modular normalization; both are
one on cube units. This proves the needed unit action, rather
than inferring it from absolute values of the valuation eigenvalues.
Exactness passes it to the exceptional subquotient. Any possible
extension splits on the relevant finite quotient of the compact
unit group over \(\mathbb C\), so it cannot add a unipotent unit
action.

The covering cocycle is trivial with a cube argument. Therefore
both the direct constant term and its Weyl-reflected counterpart
are unchanged under the same substitution. The actual weight
\(L_{\upsilon_m}^{-1}\), however, changes by
\(\chi_*(b)^{-3}=-1\). Each weighted constant term vanishes
separately. This works for the fixed cutoff vector as well as a
spherical vector. It is not a claim that the unweighted theta
constant is zero.

## 4. Full local Fourier calculation and principal frequency

Let the additive character have conductor \(\mathcal O_*\), use
self-dual additive measure with volume of \(\mathcal O_*\) equal to
one, and put
\[
 \tau_-(\lambda_*)=\sum_{\bar x\in k_*^\times}
             \lambda_*(x)e_*(-x/\pi).
\]
For \(f=\lambda_*\mathbf1_{\mathcal O_*^\times}\),
\[
 \widehat f(\pi^{-1}u)
   =q_*^{-1}\tau_-(\lambda_*)\lambda_*(u)^{-1}.
\tag{R2}
\]
This follows by splitting into residue classes and changing
\(\bar x\) to \(\bar u^{-1}\bar x\). At nonnegative Fourier
valuation the nontrivial multiplicative character sums to zero.
At valuation below \(-1\), integration over each principal-unit
coset is zero because its additive character is nontrivial.
These exhaust all valuations. Also
\(\lvert\tau_-(\lambda_*)\rvert=q_*^{1/2}\).
The alternative Fourier sign changes only its fixed Gauss scalar;
indeed the cubic character is one at \(-1\).

The source's exact Fourier argument is \(t_0\ell_{q_sX}h/(sA)\).
The note's norm-one substitution gives, without any absolute value,
\[
 \psi(s)^{-1}\psi(A)^{-1}\lambda(t_0)
       =\lambda(t)\lambda(h)^{-1}.
\tag{R3}
\]
The transformed mask requires
\(v_*(t)\equiv v_*(h)-1\pmod6\). Equation (R2) requires
\(v_*(t)=-1\), so the surviving frequencies have
\(v_*(h)\equiv0\pmod6\). For them the two unit characters in the
Mellin pairing cancel. The local factor is a nonzero fixed scalar
times \(q_*^z\).

Thus the ideal twists cancel coefficientwise before forming
\(\mathcal F_{u,\eta}\), and the latter contains the original
target \(\eta\). On \(h=ur^6\), the residual phase is
\(\lambda(u)^{-1}\), independent of the exterior ideal \(r\).
The principal frequency \(u=1\) survives with phase one and a
nonzero Mellin factor at \(z=1/6\). There is no positive-sign
requirement on this factor: its nonvanishing is the property used
in the scalar comparison.

## 5. The sharper additive Gram bound really survives

Equation (R1) is useful here: the modified average does not create
an arbitrary arithmetic column coefficient. After the same common
norm-profile separation, its column coefficient is exactly the
source coefficient multiplied by \(\psi(s)^{-1}\). The physical
valuation restriction can be removed from the positive row norm,
and its phase disappears in that norm.

In the source common-support decomposition \(s_1=Da,s_2=Eb\),
the extra factor is
\[
 \psi(D)^{-1}\psi(E)\,
                    \psi(a)^{-1}\psi(b).
\]
The first part is an outer unit scalar. The residual pair is
therefore the same coprime two-column sum with common character
\(\lambda_{\varepsilon,j}\psi^{-1}\), not two unrelated twists.
Its exterior conductor and extra radical are still bounded by
the norm of \(j\), up to fixed S-data.

For a nonprincipal inducing character, the source estimate (13.5)
therefore applies unchanged. For a principal inducing character,
the necessary exterior valuation condition is still
\(v_{\mathfrak q}(j)\equiv0\pmod6\); this is explicitly retained
for every fixed S-supported twist in S13.SS2.p25.1.
The exceptional count, complete common-divisor expansion and
diagonal contribution thus keep precisely the three terms in
(13.7). A fixed finite local norm slice and its characters have
only fixed seminorm cost. Consequently the sharper direct
exponent (13.8), rather than just a coarse sieve bound, survives.

## 6. Scope of the reviewed conclusion

Selected primes are outside the enlarged fixed set. Their ideal
generators have new valuation zero. Hence they preserve the
physical congruence and the digit-three constant-term
cancellation in every compensated term. Equation (R3) holds
before each selected-prime Euler calculation, so those local
factors retain the original target and all their zeros.

On the high side, the remaining frequency condition is a fixed
S-class restriction and the remaining phase has modulus one.
Positive mean and counting estimates may be restricted to it.
The principal row remains present. These facts support the
adapter's claimed preservation of the comparison exponents.

The review does not assert a smaller numerical value of
\(B_{\flat}\), a result uniform in the auxiliary prime, or RH.
It supports removal of the previously missing resonant case
within the stated all-field bootstrap. The final bootstrap,
field descent and closed unitary-family hypotheses must still be
read in their own accompanying theorem.
